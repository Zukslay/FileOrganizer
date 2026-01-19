import os
from hidden_function import is_hidden

def search_text(text):
    home = os.path.expanduser('~')
    paths = []

    for root, _, files in os.walk(home):
        if is_hidden(root):
            continue

        for file in files:
            file_path = os.path.join(root, file)

            if is_hidden(file_path):
                continue
            if file.split(".")[-1] not in ("txt", "md", "rtf", "log", "csv"):
                continue
            
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if text in content:
                        paths.append(file_path)
            except (IOError, OSError, UnicodeDecodeError) as e:
                print(f"Error al leer {file_path}: {e}")
                continue
    return paths

