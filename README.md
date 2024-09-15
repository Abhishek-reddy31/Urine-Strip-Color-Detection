# Urine-Strip-Color-Detection

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2.2-green.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5.1-blue.svg)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow.svg)

## Overview

Urine Strip Color Detection is a web application designed to detect colors on urine strips using image processing techniques. This project leverages the power of Django for the backend, OpenCV for image processing, and vanilla JavaScript for a responsive and interactive frontend.

## Usage

Urine test strips are commonly used to measure various components in the urine, each corresponding to a specific health indicator. A typical urine strip with 10 colors can provide insights into the following:

1. **pH** - Indicates the acidity or alkalinity of the urine. Helps assess kidney health, risk for kidney stones, and can be influenced by diet.
   
2. **Protein** - Detects proteins like albumin. High protein levels can indicate kidney damage or disease.

3. **Glucose** - Tests for sugar levels in urine. High glucose may suggest diabetes or issues with blood sugar regulation.

4. **Ketones** - Measures ketone bodies, byproducts of fat metabolism. High levels may indicate uncontrolled diabetes, fasting, or other metabolic issues.

5. **Blood** - Checks for blood in the urine. This may indicate infection, kidney damage, stones, or other conditions.

6. **Leukocytes** - Detects white blood cells, often a sign of infection or inflammation in the urinary tract.

7. **Nitrites** - Indicates the presence of bacteria that can convert nitrates into nitrites, often signaling a urinary tract infection (UTI).

8. **Bilirubin** - Tests for the presence of bilirubin, which is usually broken down in the liver. Elevated levels may suggest liver dysfunction or bile duct problems.

9. **Urobilinogen** - A byproduct of bilirubin breakdown. High levels may indicate liver disease or hemolytic disorders.

10. **Specific Gravity** - Measures urine concentration, providing insights into hydration status and kidney function.

Each color change on the strip corresponds to a different concentration of the measured substance, helping to assess various aspects of kidney, liver, and metabolic health.


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
- **Vanilla JavaScript**: Plain JavaScript without any additional libraries or frameworks, used for the frontend.

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

**Note**: After uploading the image, kindly wait for a few seconds to let it process the image. Since k-means clustering is used, it may take a few seconds to display the results. The best-case scenario is 5 seconds, and the worst-case scenario is 20 seconds to display the results.

## How to Run the Project

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Abhishek-reddy31/Urine-Strip-Color-Detection.git
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
