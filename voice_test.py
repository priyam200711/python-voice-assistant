import pyttsx3

engine = pyttsx3.init("sapi5")
engine.setProperty("volume", 1.0)
engine.setProperty("rate", 150)

for i in range(5):
    print(f"Speaking test number {i + 1}")
    engine.say(f"Voice test number {i + 1}")
    engine.runAndWait()

print("All tests completed")