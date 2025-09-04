import os
import librosa
import matplotlib.pyplot as plt
import numpy as np

def cria_e_salvar_espectograma(caminho_do_audio, caminho_de_saida):
    try:
        wave, sample_rate = librosa.load(caminho_do_audio, sr=None)
        espectograma = np.abs(librosa.stft(wave))
        espectograma_db = librosa.amplitude_to_db(espectograma, ref=np.max)
        fig, ax = plt.subplots(figsize=(10, 4))
        img = librosa.display.specshow(espectograma_db, sr=sample_rate, x_axis='time', y_axis='log', ax=ax)
        fig.colorbar(img, ax=ax, format='%+2.0f dB', label='Intensidade (dB)')
        nome_do_arquivo = os.path.basename(caminho_do_audio)
        ax.set_title(f'Espectrograma de {nome_do_arquivo}')
        plt.savefig(caminho_de_saida)
    except Exception as e:
        print(f"Erro {e}")
        


pasta_entrada = 'dataset'
pasta_saida = 'espectogramas'

os.makedirs(pasta_saida, exist_ok=True)

arquivos = os.listdir(pasta_entrada)

for arquivo in arquivos:
    if arquivo.endswith('.wav') or arquivo.endswith('.mp3'):
        caminho_completo_entrada = os.path.join(pasta_entrada, arquivo)
        nome = os.path.splitext(arquivo)[0]
        caminho_completo_saida = os.path.join(pasta_saida, f"{nome}.png")
        cria_e_salvar_espectograma(caminho_completo_entrada, caminho_completo_saida)