import os

def is_hidden(path):
    parts = os.path.normpath(path).split("/")
    return any(part.startswith('.') for part in parts if part)