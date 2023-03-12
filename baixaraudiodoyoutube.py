import yt_dlp

# Defina a URL do vídeo do YouTube que você deseja baixar o áudio
url = 'add o endereço do youtube aki'

# Defina a qualidade do áudio que deseja baixar (valores de 0 a 9)
audio_quality = 3

# Defina as opções para baixar apenas o áudio com a qualidade desejada
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': str(audio_quality),
    }],
}

# Inicialize o objeto yt_dlp e baixe o áudio do vídeo com a qualidade desejada
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

