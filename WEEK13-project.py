import os

def generate_files():
    file_list = []
    for file in os.listdir():
        if os.path.isfile(file):
            file_dict = {
                "file_name": file,
                "file_path": os.path.abspath(file),
                "file_size": os.path.getsize(file)
            }
            file_list.append(file_dict)
    return file_list

if __name__ == "__main__":
    files = generate_files()
    for file in files:
        print(file)
