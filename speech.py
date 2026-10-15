import speech_recognition as sr
import subprocess

recognizer = sr.Recognizer()


def speak(text):
    print("Assistant:", text)

    safe_text = text.replace("'", "''")

    command = (
        "Add-Type -AssemblyName System.Speech; "
        "$s = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
        f"$s.Speak('{safe_text}'); "
        "$s.Dispose()"
    )

    subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        check=False
    )


def listen(timeout=10, phrase_time_limit=8):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)

        audio = recognizer.listen(
            source,
            timeout=timeout,
            phrase_time_limit=phrase_time_limit
        )

    return recognizer.recognize_google(audio).lower()