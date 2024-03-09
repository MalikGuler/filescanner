import os

def list_files(directory):
    with open("dosya_bilgileri.txt", "w", encoding="utf-8") as file:
        for root, dirs, files in os.walk(directory):
            for dirname in dirs:
                try:
                    dir_path = os.path.join(root, dirname)
                    file.write(f"Directory: {dir_path}\n")
                    file.write("-" * 30 + "\n")

                    # Alt dizinlerin içeriğini de dolaş
                    for sub_root, sub_dirs, sub_files in os.walk(dir_path):
                        for filename in sub_files:
                            try:
                                file_path = os.path.join(sub_root, filename)
                                file_size = os.path.getsize(file_path)
                                file_name, file_extension = os.path.splitext(filename)
                                file.write(f"Path: {file_path}\n")
                                file.write(f"Name: {file_name}\n")
                                file.write(f"Extension: {file_extension}\n")
                                file.write(f"Size (bytes): {file_size}\n")
                                file.write("-" * 30 + "\n")
                            except UnicodeEncodeError:
                                print(f"Skipping file due to encoding error: {file_path}")
                except UnicodeEncodeError:
                    print(f"Skipping directory due to encoding error: {dir_path}")

if __name__ == "__main__":
    directory = "C:\\"  # C dizinini otomatik olarak gez
    list_files(directory)
    print("Dosya ve klasor bilgileri basariyla kaydedildi.")
