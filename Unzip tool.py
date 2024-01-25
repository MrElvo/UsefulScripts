import os
import zipfile

def unzip_all_folders(root_dir):
    """Unzips all zip files found in the specified root directory and its subdirectories."""

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".zip"):
                zip_file_path = os.path.join(root, file)
                try:
                    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                        zip_ref.extractall(os.path.dirname(zip_file_path))  # Extract to the same directory
                    print(f"Unzipped {zip_file_path}")
                except zipfile.BadZipFile:
                    print(f"Error: {zip_file_path} is not a valid zip file.")
                except Exception as e:
                    print(f"Error unzipping {zip_file_path}: {e}")

if __name__ == "__main__":
    root_dir = input("Enter the path to the root directory: ")
    unzip_all_folders(root_dir)