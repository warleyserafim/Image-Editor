from PIL import Image, ImageDraw, ImageFont
import os

# Caminho das pastas de entrada e saída
input_folder = 'originais'
output_folder = 'editadas'
logo_path = 'logo.png'

# Criar pasta de saída se não existir
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f'Pasta de saída criada: {output_folder}')

# Função para adicionar tarja com logo
def add_logo_band(image_path, logo_path):
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGBA")  # Certificar-se de que a imagem suporta transparência
            logo = Image.open(logo_path).convert("RGBA")  # Abrir logo e converter para RGBA

            # Verifica a orientação da imagem
            if img.height > img.width:
                # Imagem no modo retrato
                band_height = int(img.height * 0.05)  # Altura da tarja como 10% da altura da imagem
                logo_width = img.width
                logo_height = int(logo.height * (logo_width / logo.width))
            else:
                # Imagem no modo paisagem
                band_height = int(img.height * 0.13)  # Altura da tarja como 20% da altura da imagem
                logo_width = img.width
                logo_height = int(logo.height * (logo_width / logo.width) * 0.5)  # Reduzir a altura do logo

            logo = logo.resize((logo_width, logo_height), Image.ANTIALIAS)

            # Cria uma nova imagem com espaço adicional para a tarja
            new_img = Image.new('RGBA', (img.width, img.height + band_height), (255, 255, 255, 255))
            new_img.paste(img, (0, 0), img)  # Certificando de usar a transparência da imagem original

            # Criar uma tarja branca na parte inferior
            draw = ImageDraw.Draw(new_img)
            draw.rectangle([(0, img.height), (img.width, img.height + band_height)], fill=(255, 255, 255, 255))

            # Posição do logo na tarja (centralizado horizontalmente)
            logo_x = (new_img.width - logo.width) // 2
            logo_y = img.height + (band_height - logo.height) // 2
            new_img.paste(logo, (logo_x, logo_y), logo)

            return new_img
    except Exception as e:
        print(f'Erro ao processar a imagem {image_path}: {e}')
        return None

# Processar todas as imagens na pasta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(input_folder, filename)
        print(f'Processando: {image_path}')
        new_image = add_logo_band(image_path, logo_path)
        if new_image:
            output_path = os.path.join(output_folder, filename)
            try:
                # Converter de volta para 'RGB' se necessário antes de salvar
                if output_path.lower().endswith('.jpg'):
                    new_image = new_image.convert("RGB")
                new_image.save(output_path)
                print(f'Imagem salva em: {output_path}')
            except Exception as e:
                print(f'Erro ao salvar a imagem {output_path}: {e}')
        else:
            print(f'Falha ao criar a nova imagem para: {image_path}')

print('Processamento concluído!')
