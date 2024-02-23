import yt_dlp
def donwload_from_yt(url):
    filaname = url.split("=")[1]
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': f'./{filaname}.mp4',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=True)
    return f'./{filaname}.mp4'

donwload_from_yt("https://youtu.be/6Jxzt6p-ozo?si=ZynwW_RYHGystk00")