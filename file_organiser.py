import os
import shutil

folder = input("Enter folder path: ")

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    if os.path.isfile(file_path):
        extension = filename.split(".")[-1].lower()

        if extension in ["jpg", "png", "jpeg"]:
            category = "Images"
        elif extension in ["pdf", "docx", "txt"]:
            category = "Documents"
        elif extension in ["mp3", "wav"]:
            category = "Audio"
        elif extension == "py":
            category = "Python Files"
        else:
            category = "Others"

        new_folder = os.path.join(folder, category)
        os.makedirs(new_folder, exist_ok=True)

        shutil.move(
            file_path,
            os.path.join(new_folder, filename)
        )

print("Files organized successfully!")