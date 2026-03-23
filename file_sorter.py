import os
import shutil

folder_path = input("Enter folder path: ")

if not os.path.isdir(folder_path):
    print("Invalid folder path")
else:
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1][1:]

            if ext:
                new_folder = os.path.join(folder_path, ext)

                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)

                shutil.move(file_path, os.path.join(new_folder, file))

    print("Files sorted successfully.")
