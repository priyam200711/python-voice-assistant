import yt_dlp
import webbrowser

from speech import speak


def play_youtube(query):
    try:
        speak(f"Searching YouTube for {query}")

        options = {
            "quiet": True,
            "noplaylist": True,
            "extract_flat": True
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            results = ydl.extract_info(
                f"ytsearch1:{query}",
                download=False
            )

        videos = results.get("entries", [])
        video = next((v for v in videos if v), None)

        if video:
            video_id = video.get("id")
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            speak(f"Opening {query} on YouTube")
            webbrowser.open(video_url)

        else:
            speak("Sorry, I could not find that video")

    except Exception as e:
        print("YouTube error:", e)
        speak("Sorry, I could not play that video")