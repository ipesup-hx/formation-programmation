from PIL import Image
from pathlib import Path
import os


def images_to_pdf(input_folder, output_folder, output_filename):
    images = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]
    if not images:
        print("Aucune image PNG trouvée dans le dossier.")
        return
    images.sort()
    image_list = [
        Image.open(
            Path('.')/input_folder/img
        ).convert('RGB') 
        for img in images
    ]

    image_list[0].save(Path('.')/output_folder/f"{output_filename}.pdf", save_all=True, append_images=image_list[1:])
    print(f"PDF créé avec succès : {output_filename}.pdf")


images_to_pdf(
    input_folder=Path('.')/"Séance 2"/"tableaux",
    output_folder=Path('.')/"Séance 2",
    output_filename="tableaux"
)