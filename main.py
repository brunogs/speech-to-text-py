# main.py
import yt_dlp
import whisper

def main():
    downloadVideo("https://www.youtube.com/watch?v=0dG7UIWu2ik")
    print("Python application using yt-dlp and whisper")

def downloadVideo(rawUrl):
    yt_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '/resources/good_speech1'
    }
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        try:
            ydl.download([rawUrl])
        except yt_dlp.DownloadError as e:
            print('Error downloading video:', e)

if __name__ == "__main__":
    main()
