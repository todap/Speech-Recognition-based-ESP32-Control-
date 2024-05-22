import speech_recognition as sr
import serial
import websocket
import time
import os

r = sr.Recognizer()

def send_command_to_esp32(command):
    websocket_url = "ws://172.20.10.6:81"  # Replace with your ESP32 WebSocket server URL
    ws = websocket.create_connection(websocket_url)
    ws.send(command)
    if "exit" in command:
        ws.close()

def recognize_speech():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        # text = r.recognize_sphinx(audio)
        

        print("You said: " + text)
        if "on" in text:
            # ser.write(b'1')  # Sending '1' to turn on the LED
            send_command_to_esp32("on")
            print('Sent 1')
        elif "off" in text:
            # ser.write(b'0')  # Sending '0' to turn off the LED
            send_command_to_esp32("off")
            print('Sent 0')


    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Continuously listen for speech
send_command_to_esp32("off")
while True:
    recognize_speech()
                                                                                                                                                                             