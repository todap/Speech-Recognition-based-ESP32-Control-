import websocket
import speech_recognition as sr
import requests

# WebSocket server address
server_address = "ws://192.168.43.251:81"  # Replace <ESP32_IP_ADDRESS> with the actual IP address of your ESP32

# Sentiment analysis API URL
sentiment_analysis_url = "" #Enter the URL of the API here

# Function to handle WebSocket open event
def on_open(ws):
    print("WebSocket connection established")
    text = speech_to_text()
    sentiment = perform_sentiment_analysis(text)
    if sentiment == '1':
        ws.send("on")
    elif sentiment == '0':
        ws.send("off")
    else:
        print("Neutral sentiment, no action taken.")

# Function to handle WebSocket message received event
def on_message(ws, message):
    print("Received message:", message)

# Function to handle WebSocket close event
def on_close(ws):
    print("WebSocket connection closed")

# Connect to WebSocket server
websocket.enableTrace(True)
websocket_address = server_address

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise if necessary
        recognizer.adjust_for_ambient_noise(source)

        # Listen to the audio from the microphone
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        
        # Recognize the speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        
        # Print the recognized text
        print("You said:", text)

        return text

    except sr.UnknownValueError:
        print("Could not understand audio")
        return None

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

def perform_sentiment_analysis(text):
    try:
        # Send the text to the sentiment analysis API
        response = requests.post(sentiment_analysis_url, json={"input": text})
        if response.status_code == 200:
            sentiment = response.json().get("output")
            print("Sentiment:", sentiment)
            return sentiment
        else:
            print("Error occurred while performing sentiment analysis:", response.text)
            return None
    except Exception as e:
        print("Error occurred while performing sentiment analysis:", str(e))
        return None

ws = websocket.WebSocketApp(websocket_address, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()