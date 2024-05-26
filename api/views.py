from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import cv2
import numpy as np
import os
from django.conf import settings


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


class UrineStripColorDetectionView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        # Clear the images directory
        image_dir = os.path.join(settings.MEDIA_ROOT, 'images')
        for filename in os.listdir(image_dir):
            file_path = os.path.join(image_dir, filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)

        # Save the new file
        file_obj = request.FILES['image']
        file_name = default_storage.save('images/' + file_obj.name, ContentFile(file_obj.read()))
        file_path = default_storage.path(file_name)

        colors = self.extract_colors(file_path)
        color_dict = {
            'URO': colors[0].tolist(),
            'BIL': colors[1].tolist(),
            'KET': colors[2].tolist(),
            'BLD': colors[3].tolist(),
            'PRO': colors[4].tolist(),
            'NIT': colors[5].tolist(),
            'LEU': colors[6].tolist(),
            'GLU': colors[7].tolist(),
            'SG': colors[8].tolist(),
            'PH': colors[9].tolist()
        }
        return Response(color_dict)

    def extract_colors(self, image_path, num_colors=10):
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or unable to load")
        
        aspect_ratio = image.shape[0] / image.shape[1]
        width = 500
        height = int(width * aspect_ratio)
        image = cv2.resize(image, (width, height))

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        pixels = image.reshape(-1, 3)
        pixels = np.float32(pixels)
        _, labels, centers = cv2.kmeans(pixels, num_colors, None,
                                        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2),
                                        10, cv2.KMEANS_RANDOM_CENTERS)
        centers = np.uint8(centers)
        dominant_colors = [centers[i] for i in range(num_colors)]

        return dominant_colors
