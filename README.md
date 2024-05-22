# Voice Control ESP32 with Sentiment Analysis

This project allows you to control an ESP32 device using voice commands and sentiment analysis. It consists of two Python scripts (`speech_recog_using_API.py` and `speech_reg.py`) and an Arduino sketch for the ESP32.

## Prerequisites

### Python Dependencies

- `websocket`
- `speech_recognition`
- `requests`

You can install these dependencies using pip:
`pip install websocket speech_recognition requests`
### Hardware Requirements

- ESP32 board
- Wi-Fi network credentials

## Setup

1. **ESP32 Setup**:
   - Upload the provided Arduino sketch to your ESP32 board.
   - Update the `ssid` and `password` variables with your Wi-Fi network credentials.

2. **Python Script Setup**:
   - **For `speech_recog_using_API.py`**:
     - Update the `server_address` variable with the IP address of your ESP32 device.
     - Provide the URL of the sentiment analysis API in the `sentiment_analysis_url` variable.
   - **For `speech_reg.py`**:
     - Update the `websocket_url` variable with the WebSocket URL of your ESP32 device (e.g., `ws://172.20.10.6:81`).

## Usage

1. **With Sentiment Analysis (`speech_recog_using_API.py`)**:
   - Run the `speech_recog_using_API.py` script.
   - Speak into the microphone when prompted.
   - The script will perform sentiment analysis on the recognized text and send the corresponding "on" or "off" command to the ESP32 device based on the sentiment score.

2. **Without Sentiment Analysis (`speech_reg.py`)**:
   - Run the `speech_reg.py` script.
   - Speak into the microphone when prompted.
   - If the script recognizes the word "on", it will send the "on" command to the ESP32 device, turning on the built-in LED.
   - If the script recognizes the word "off", it will send the "off" command to the ESP32 device, turning off the built-in LED.

## Note

- Make sure that the ESP32 device and the computer running the Python scripts are connected to the same Wi-Fi network.
- For `speech_recog_using_API.py`, you need to provide a valid sentiment analysis API URL. If you don't have one, you can modify the script to use a different approach or remove the sentiment analysis part.
