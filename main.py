# main.py
import yt_dlp
import whisper

def main():
    download_video("https://www.youtube.com/watch?v=0dG7UIWu2ik")
    loaded_model = load_model()
    if loaded_model:
        transcribe_speech(loaded_model, "/resources/good_speech.mp3")
    print("Python application using yt-dlp and whisper")

def download_video(rawUrl):
    yt_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '/resources/good_speech'
    }
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        try:
            ydl.download([rawUrl])
        except yt_dlp.DownloadError as e:
            print('Error downloading video:', e)

def load_model():
    try:
        model = whisper.load_model('small')
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print("Error loading model:", e)
        return None

def transcribe_speech(model, audio_file):
    try:
        result = model.transcribe(audio_file)
        print(result)
        with open("/resources/transcription.txt", "w") as text_file:
            text_file.write(result["text"])
        print("Transcription saved successfully.")
    except Exception as e:
        print("Error transcribing speech:", e)

if __name__ == "__main__":
    main()
