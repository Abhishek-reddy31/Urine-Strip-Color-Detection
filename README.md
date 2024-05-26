# Urine-Strip-Color-Detection

Overview
Urine Strip Color Detection is a web application designed to detect colors on urine strips using image processing techniques. This project leverages the power of Django for the backend, OpenCV for image processing, and vanilla JavaScript for a responsive and interactive frontend.

Features
Image Upload: Upload an image of a urine strip and get the color readings.
Color Detection: Extracts and displays the RGB values of the detected colors.
Interactive Frontend: User-friendly interface with animations and responsive design.
About and Contact Pages: Additional informational and contact pages with a consistent and creative design.
Tools and Technologies
Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
Django REST framework: A powerful and flexible toolkit for building Web APIs.
OpenCV: An open-source computer vision and machine learning software library.
NumPy: A fundamental package for scientific computing with Python.
HTML/CSS/JavaScript: For creating a responsive and interactive frontend.
Project Structure
Backend: Django handles the server-side logic, including image upload, processing, and color detection.
Frontend: Vanilla JavaScript, HTML, and CSS for a seamless user experience.
APIs: Built with Django REST framework for handling image upload and processing requests.
Algorithm
The algorithm for detecting colors in the urine strip image involves the following steps:

Upload: The user uploads an image using the frontend form.
Save: The uploaded image is saved to the server.
Read: The image is read using OpenCV.
Process: Resize and convert the image to RGB.
Extract: Extract the dominant colors using k-means clustering.
Output: Return the RGB values of the detected colors.
How to Run the Project
Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/urine-strip-color-detection.git
cd urine-strip-color-detection
Install dependencies:

sh
Copy code
pip install -r requirements.txt
Run the server:

sh
Copy code
python manage.py runserver
Access the application:
Open your browser and go to http://127.0.0.1:8000/.

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For any inquiries or feedback, feel free to contact us via the Contact Page on our website.
