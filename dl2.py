import yt_dlp

def download_video_720p(url, output_path='.'):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'merge_output_format': 'mp4',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'quiet': False,
        'noplaylist': True,
        'restrictfilenames': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("✅ Download complete!")
        except Exception as e:
            print(f"❌ Error downloading video: {e}")

if __name__ == '__main__':
    video_url = input("Enter YouTube video URL: ")
    download_video_720p(video_url)

