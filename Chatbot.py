import serial
import speech_recognition as sr
import pyttsx3
import requests

# 🔑 Put your OpenRouter API key here
API_KEY = "YOUR_OPENROUTER_API_KEY"

# 🔌 Connect micro:bit (change COM port if needed)
ser = serial.Serial('COM3', 115200)

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# 🎤 Listen to voice
def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You:", text)
            return text
        except:
            print("❌ Could not understand")
            return ""

# 🤖 Ask FREE AI
def ask_ai(prompt):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openrouter/free",   # ✅ Always free
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        result = response.json()

        if 'choices' in result:
            return result['choices'][0]['message']['content']
        else:
            print("API Error:", result)
            return "Sorry, error in AI response."

    except Exception as e:
        print("Error:", e)
        return "Connection error."

# 🔊 Speak response
def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

# 🔁 Main loop
print("🚀 System Ready. Press micro:bit button A")

while True:
    try:
        if ser.in_waiting:
            data = ser.readline().decode().strip()
            print("micro:bit:", data)

            if data == "start":
                user_text = listen()
                if user_text:
                    ai_reply = ask_ai(user_text)
                    speak(ai_reply)

    except KeyboardInterrupt:
        print("Stopped")
        break
