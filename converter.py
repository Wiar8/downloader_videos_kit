import moviepy.editor as mp
import os

def convert_to_mp3(folder_path, output_folder):
    # Crea la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Recorre todos los archivos en la carpeta de entrada
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):  # Asegura que solo procesa archivos .mp4
            # Construye la ruta completa del archivo actual
            full_path = os.path.join(folder_path, filename)
            # Carga el video con MoviePy
            video_clip = mp.VideoFileClip(full_path)
            # Construye el nombre del archivo de salida
            output_filename = os.path.splitext(filename)[0] + ".mp3"
            # Construye la ruta completa de salida
            output_path = os.path.join(output_folder, output_filename)
            # Extrae el audio y lo guarda en formato mp3
            video_clip.audio.write_audiofile(output_path)
            print(f"{filename} has been converted to mp3 and saved to {output_folder}")

if __name__ == "__main__":
    # Define la carpeta de entrada y salida
    music_folder = "music"
    output_folder = "music_mp3"
    # Llama a la función de conversión
    convert_to_mp3(music_folder, output_folder)
    print("All files have been converted.")