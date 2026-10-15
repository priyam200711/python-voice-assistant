import speech_recognition as sr

from speech import speak, listen
from commands import execute_command


def run_assistant():
    speak("Assistant started. Say wake up to activate me")

    while True:
        try:
            print("\nWaiting for wake word...")

            text = listen()
            print("You said:", text)

            if "wake up" in text:
                speak("Yes, I am listening")

                while True:
                    try:
                        print("\nListening for your command...")

                        command = listen(
                            timeout=10,
                            phrase_time_limit=8
                        )

                        print("You said:", command)

                        should_continue = execute_command(command)

                        if not should_continue:
                            return

                    except sr.WaitTimeoutError:
                        speak("I did not hear anything")

                    except sr.UnknownValueError:
                        pass

        except sr.WaitTimeoutError:
            continue

        except sr.UnknownValueError:
            continue

        except sr.RequestError:
            speak("Speech recognition service error. Please check your internet")

        except KeyboardInterrupt:
            speak("Assistant stopped")
            return

        except Exception as e:
            print("Error:", e)
            speak("Something went wrong")