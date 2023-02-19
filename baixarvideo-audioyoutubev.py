from pytube import YouTube

#Script que baixa vídeos do youtube
#Atenção! tenha instalado a biblioteca pytube no seu python

# solicita ao usuário que insira o URL do vídeo
url = input("Insira o endereço do vídeo do YouTube: ")

# verifica se o URL inserido corresponde ao padrão esperado
if "youtube.com/watch?v=" not in url:
    print("Endereço inválido do YouTube. Certifique-se de que é um URL de vídeo válido do YouTube.")
else:
    # criar objeto YouTube
    yt = YouTube(url)

    # exibe as opções de stream disponíveis
    print("Selecione uma opção: ")
    print("1. Vídeo + Áudio")
    print("2. Apenas Áudio")
    
    option = int(input("Digite o número da opção desejada: "))
    
    if option == 1:
        # exibe as opções de stream de vídeo com áudio disponíveis
        print("Selecione a resolução desejada: ")
        streams = yt.streams.filter(file_extension='mp4', only_video=False, only_audio=False)
        for i, stream in enumerate(streams):
            print(f"{i + 1}. Resolução: {stream.resolution}, Formato: {stream.mime_type}, Tamanho: {round(stream.filesize_approx/(1024*1024), 2)} MB")

        # solicita ao usuário que escolha uma opção
        choice = int(input("Digite o número da opção desejada: "))

        # baixa o stream selecionado
        ys = streams[choice-1]
        ys.download()
        print("Download completo!")
    
    elif option == 2:
        # exibe as opções de stream de áudio disponíveis
        print("Selecione a qualidade desejada: ")
        streams = yt.streams.filter(file_extension='mp4', only_audio=True)
        for i, stream in enumerate(streams):
            print(f"{i + 1}. Qualidade: {stream.abr}, Formato: {stream.mime_type}, Tamanho: {round(stream.filesize_approx/(1024*1024), 2)} MB")

        # solicita ao usuário que escolha uma opção
        choice = int(input("Digite o número da opção desejada: "))

        # baixa o stream selecionado
        ys = streams[choice-1]
        ys.download()
        print("Download completo!")
    
    else:
        print("Opção inválida. Tente novamente.")
