import os
from tkinter import Tk, Label, Button, filedialog, Frame
from tkinter import ttk
from PIL import Image, ImageDraw

# Função para adicionar tarja com logo
def add_logo_band(image_path, logo_path):
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGBA")
            logo = Image.open(logo_path).convert("RGBA")
            
            # Verifica a orientação da imagem
            if img.height > img.width:
                band_height = int(img.height * 0.05)
                logo_width = img.width
                logo_height = int(logo.height * (logo_width / logo.width))
            else:
                band_height = int(img.height * 0.13)
                logo_width = img.width
                logo_height = int(logo.height * (logo_width / logo.width) * 0.5)

            logo = logo.resize((logo_width, logo_height), Image.ANTIALIAS)

            new_img = Image.new('RGBA', (img.width, img.height + band_height), (255, 255, 255, 255))
            new_img.paste(img, (0, 0), img)

            draw = ImageDraw.Draw(new_img)
            draw.rectangle([(0, img.height), (img.width, img.height + band_height)], fill=(255, 255, 255, 255))

            logo_x = (new_img.width - logo.width) // 2
            logo_y = img.height + (band_height - logo.height) // 2
            new_img.paste(logo, (logo_x, logo_y), logo)

            return new_img
    except Exception as e:
        print(f'Erro ao processar a imagem {image_path}: {e}')
        return None

# Função para processar as imagens
def process_images():
    if not input_folder or not output_folder or not logo_path:
        print("Pastas ou logo não selecionados")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f'Pasta de saída criada: {output_folder}')

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')):
            image_path = os.path.join(input_folder, filename)
            print(f'Processando: {image_path}')
            new_image = add_logo_band(image_path, logo_path)
            if new_image:
                output_path = os.path.join(output_folder, filename)
                try:
                    if output_path.lower().endswith(('.jpg', '.jpeg')):
                        new_image = new_image.convert("RGB")
                    new_image.save(output_path)
                    print(f'Imagem salva em: {output_path}')
                except Exception as e:
                    print(f'Erro ao salvar a imagem {output_path}: {e}')
            else:
                print(f'Falha ao criar a nova imagem para: {image_path}')

    print('Processamento concluído!')

# Funções para selecionar pastas e arquivos
def select_input_folder():
    global input_folder
    input_folder = filedialog.askdirectory()
    input_label.config(text=f'Pasta de entrada: {input_folder}')

def select_output_folder():
    global output_folder
    output_folder = filedialog.askdirectory()
    output_label.config(text=f'Pasta de saída: {output_folder}')

def select_logo_file():
    global logo_path
    logo_path = filedialog.askopenfilename(filetypes=[
        ("PNG files", "*.png"),
        ("JPEG files", "*.jpg"),
        ("JPEG files", "*.jpeg"),
        ("Bitmap files", "*.bmp"),
        ("GIF files", "*.gif"),
        ("TIFF files", "*.tiff"),
        ("All files", "*.*")
    ])
    if logo_path:
        logo_label.config(text=f'Logo: {logo_path}')
        print(f'Logo selecionado: {logo_path}')

# Configuração da interface gráfica
root = Tk()
root.title("Processador de Imagens")

# Estilos
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=10)
style.configure("TLabel", font=("Helvetica", 10), padding=10)
style.configure("Header.TLabel", font=("Helvetica", 12, "bold"))

# Layout
frame = Frame(root, padx=20, pady=20)
frame.pack()

header_label = ttk.Label(frame, text="Processador de Imagens", style="Header.TLabel")
header_label.grid(row=0, columnspan=2, pady=(0, 10))

input_label = ttk.Label(frame, text="Pasta de entrada: Não selecionada")
input_label.grid(row=1, column=0, sticky="w")

input_button = ttk.Button(frame, text="Selecionar Pasta de Entrada", command=select_input_folder)
input_button.grid(row=1, column=1, pady=5, padx=10)

output_label = ttk.Label(frame, text="Pasta de saída: Não selecionada")
output_label.grid(row=2, column=0, sticky="w")

output_button = ttk.Button(frame, text="Selecionar Pasta de Saída", command=select_output_folder)
output_button.grid(row=2, column=1, pady=5, padx=10)

logo_label = ttk.Label(frame, text="Logo: Não selecionado")
logo_label.grid(row=3, column=0, sticky="w")

logo_button = ttk.Button(frame, text="Selecionar Logo", command=select_logo_file)
logo_button.grid(row=3, column=1, pady=5, padx=10)

process_button = ttk.Button(frame, text="Processar Imagens", command=process_images)
process_button.grid(row=4, columnspan=2, pady=(20, 0))

root.mainloop()
