# Urine-Strip-Color-Detection

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2.2-green.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5.1-blue.svg)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)

## Overview

Urine Strip Color Detection is a web application designed to detect colors on urine strips using image processing techniques. This project leverages the power of Django for the backend, OpenCV for image processing, and vanilla JavaScript for a responsive and interactive frontend.

## Features

- **Image Upload**: Upload an image of a urine strip and get the color readings.
- **Color Detection**: Extracts and displays the RGB values of the detected colors.
- **Interactive Frontend**: User-friendly interface with animations and responsive design.
- **About and Contact Pages**: Additional informational and contact pages with a consistent and creative design.

## Tools and Technologies

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST framework**: A powerful and flexible toolkit for building Web APIs.
- **OpenCV**: An open-source computer vision and machine learning software library.
- **NumPy**: A fundamental package for scientific computing with Python.
- **HTML/CSS/JavaScript**: For creating a responsive and interactive frontend.

## Project Structure

- **Backend**: Django handles the server-side logic, including image upload, processing, and color detection.
- **Frontend**: Vanilla JavaScript, HTML, and CSS for a seamless user experience.
- **APIs**: Built with Django REST framework for handling image upload and processing requests.

## Algorithm

The algorithm for detecting colors in the urine strip image involves the following steps:

1. **Upload**: The user uploads an image using the frontend form.
2. **Save**: The uploaded image is saved to the server.
3. **Read**: The image is read using OpenCV.
4. **Process**: Resize and convert the image to RGB.
5. **Extract**: Extract the dominant colors using k-means clustering.
6. **Output**: Return the RGB values of the detected colors.

## How to Run the Project

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/urine-strip-color-detection.git
    cd urine-strip-color-detection
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the server**:
    ```sh
    python manage.py runserver
    ```

4. **Access the application**:
    Open your browser and go to `http://127.0.0.1:8000/`.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries or feedback, feel free to contact us via the [Contact Page](http://127.0.0.1:8000/contact/) on our website.
