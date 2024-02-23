# If-person-crosses-sent-mail-and-store-data-mongoDB

---

# Object Detection and Alert System

This repository contains a Python script for real-time object detection using YOLOv5 and integration with email notification and MongoDB for storing detected objects.

## Description

The script captures video from a webcam, detects objects in the video frames using YOLOv5, and triggers an email notification and database entry when a person is detected in the frame. The system has a built-in threshold to avoid repetitive notifications.

## Prerequisites

- Python 3.x
- OpenCV
- PyTorch
- YOLOv5
- pymongo
- smtplib

## Setup and Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/your_repository.git
    cd your_repository
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Update the following variables in the script:

    - `gmail_user`: Your Gmail address.
    - `gmail_password`: Your Gmail password.
    - MongoDB connection string (`cluster` variable in `store_on_db` function).

4. Run the script:

    ```bash
    python object_detection_alert.py
    ```

## Configuration

- `times`: Threshold for email notification. Controls the frequency of email alerts.
- `num`: Counter for database entry.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

Feel free to customize the README further to include additional sections, such as acknowledgments, troubleshooting tips, or detailed usage instructions.
