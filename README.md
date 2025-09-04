# Gerador de Espectrogramas em Python

[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)


Um script em Python para gerar e salvar espectrogramas de forma automatizada a partir de uma coleção de arquivos de áudio. Este projeto utiliza `librosa` para a análise de áudio e `matplotlib` para a visualização.

## Funcionalidades

- **Processamento em Lote:** Converte automaticamente todos os arquivos de áudio de uma pasta de entrada.
- **Suporte a Múltiplos Formatos:** Compatível com os formatos de áudio mais comuns (`.wav`, `.mp3`).

## Instalação

Siga os passos abaixo para preparar o ambiente e executar o projeto.

1.  **Clone o repositório:**
    ```bash
    git clone (https://github.com/Gerador-de-Espectrogramas.git)
    ```
    
2.  **Navegue até a pasta do projeto:**
    ```bash
    cd Gerador-de-Espectrogramas
    ```

3.  **Instale as dependências:**
    Recomenda-se o uso de um ambiente virtual (`venv`) antes de instalar.
    ```bash
    python3 -m venv .venv
    pip install -r requirements.txt
    ```

## Como Usar

**1. Prepare seus arquivos:**

-   Crie a pasta `dataset` na raiz do projeto, caso ela não exista.
-   **Copie todos os seus arquivos de áudio** (`.wav` ou `.mp3`) para dentro da pasta `dataset`.

**2. Execute o Script:**

-   **Uso Padrão:**
    Execute o comando abaixo no terminal. O script usará a pasta `dataset` como entrada e salvará as imagens na pasta `espectrogramas`.

    ```bash
    python src/gerador.py
    ```
