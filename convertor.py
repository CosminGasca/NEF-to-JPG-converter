import rawpy
import imageio
import os

# folderul cu poze NEF
input_folder = r" " #input folder path  
# folderul unde salvezi JPG-urile
output_folder = r" " #output folder path

# creeaza folderul de output daca nu exista
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):

    if filename.lower().endswith(".nef"):
        input_path = os.path.join(input_folder, filename)
        output_name = filename.rsplit(".", 1)[0] + ".jpg"
        output_path = os.path.join(output_folder, output_name)

        try:
            with rawpy.imread(input_path) as raw:
                rgb = raw.postprocess()
                imageio.imsave(output_path, rgb)

            print(f"Convertit: {filename}")
        except Exception as e:
            print(f"Eroare la {filename}: {e}")

print("Gata!")