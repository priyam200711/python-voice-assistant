import webbrowser
import pyautogui
from pathlib import Path
from datetime import datetime
from urllib.parse import quote_plus

from speech import speak
from youtube import play_youtube
from apps import open_application
from apps import open_folder

def execute_command(command):

    # Pause video
    if "pause video" in command or "stop video" in command:
        pyautogui.press("k")
        speak("Pausing video")

    # Resume video
    elif "resume video" in command:
        pyautogui.press("k")
        speak("Resuming video")

    # Play a YouTube video
    elif command.startswith("play "):
        query = command[len("play "):].strip()

        if query:
            play_youtube(query)
        else:
            speak("Please tell me what you want to play")

    # Search on Google
    elif command.startswith("open folder "):
        folder_name = command.replace("open folder ", "", 1).strip()

        if open_folder(folder_name):
            speak(f"Opening {folder_name}")
        else:
            speak(f"Folder {folder_name} was not found")
    elif command.startswith("search "):
        query = command[len("search "):].strip()

        if query:
            speak(f"Searching Google for {query}")

            search_url = (
                "https://www.google.com/search?q="
                + quote_plus(query)
            )

            webbrowser.open(search_url)
        else:
            speak("Please tell me what you want to search")

    # Open a website
    elif command.startswith("open "):
        website = command[len("open "):].strip()

        websites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "chatgpt": "https://chatgpt.com",
            "chat gpt": "https://chatgpt.com",
            "github": "https://github.com",
            "amazon": "https://www.amazon.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com"
        }

        if website in websites:
            speak(f"Opening {website}")
            webbrowser.open(websites[website])

        elif website:
            speak(f"Trying to open {website}")
            webbrowser.open(
                "https://www." + quote_plus(website).replace("+", "") + ".com"
            )

        else:
            speak("Please tell me which website to open")

    # Tell current time
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # Greetings
    elif "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    # Assistant introduction
    elif "your name" in command or "who are you" in command:
        speak("I am your personal voice assistant")

    # Exit the assistant
    elif "exit" in command or command == "stop":
        speak("Goodbye! Have a nice day")
        return False
        # Open desktop applications
    elif command.startswith("launch ") or command.startswith("open app "):
        app_name = command.replace("open app ", "", 1)
        app_name = app_name.replace("launch ", "", 1).strip()

        if open_application(app_name):
            speak(f"Opening {app_name}")
        else:
            speak(f"Sorry, I do not know how to open {app_name}")
    elif "take screenshot" in command or "capture screen" in command or command == "screenshot":
        try:
            screenshot_folder = Path(
                r"C:\Users\kumar\OneDrive\Pictures\Screenshots\Screenshots"
            )
            screenshot_folder.mkdir(parents=True, exist_ok=True)

            filename = datetime.now().strftime("screenshot_%Y-%m-%d_%H-%M-%S.png")
            filepath = screenshot_folder / filename

            pyautogui.screenshot().save(filepath)

            speak("Screenshot saved successfully")

        except Exception as e:
            print("Screenshot error:", e)
            speak("Sorry, I could not take the screenshot")        
    # Ignore unknown commands
    else:
        pass

    return True