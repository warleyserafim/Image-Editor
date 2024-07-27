# Instruções para Adicionar Imagens e Rodar o Script

Este guia descreve como adicionar imagens e rodar o script `app.py` para editar imagens. As imagens editadas serão salvas em uma pasta chamada `Editadas` na raiz do projeto.

## Passo 1: Adicionar Imagens na Pasta Original

    1. Crie uma pasta chamada `Original` na raiz do projeto, se ela ainda não existir.
    2. Adicione todas as imagens que você deseja editar dentro da pasta `Original`.

## Passo 2: Rodar o Arquivo app.py

    1. Certifique-se de que você tem o Python instalado em seu sistema. Você pode verificar isso rodando o comando:

        ```bash
        python --version
        ```

    2. Navegue até o diretório onde o arquivo `app.py` está localizado. Por exemplo:

        ```bash
        cd /caminho/para/o/projeto
        ```

    3. Rode o script `app.py` com o seguinte comando:

        ```bash
        python app.py
    ```

## Passo 3: Verificar as Imagens Editadas

    1. Após rodar o script, uma pasta chamada `Editadas` será criada na raiz do projeto.
    2. As imagens editadas serão salvas dentro da pasta `Editadas`.

## Estrutura do Projeto

A estrutura do projeto deve se parecer com isto:

```bash
/projeto-raiz
  ├── app.py
  ├── Original/
  │   ├── imagem1.jpg
  │   ├── imagem2.png
  │   └── ...
  └── Editadas/
      ├── edited_imagem1.jpg
      ├── edited_imagem2.png
      └── ...
