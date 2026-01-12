import os
import shutil
from helper_functions import get_extensions, get_folders, making_folders, get_file_paths

#checking if the folder is hidden
def is_hidden(path):
    parts = os.path.normpath(path).split("/")
    return any(part.startswith('.') for part in parts if part)

#checking if the folder exists
def find_path(folder_name):
    if os.path.isabs(folder_name) and os.path.isdir(folder_name):
        return os.path.abspath(folder_name)
    
    if folder_name.startswith('~'):
        expanded = os.path.expanduser(folder_name)
        if os.path.isdir(expanded):
            return expanded
    
    home = os.path.expanduser('~') 

    #iterating over all folders
    for dirpath, _, __ in os.walk(home):
        if is_hidden(dirpath):
            continue
        print(_)
        basename = os.path.basename(dirpath)
        if folder_name == basename and os.path.isdir(dirpath):
            return dirpath

def organizer(folder_path):
    extensions = get_extensions(folder_path)
    folders_paths = get_folders(extensions, folder_path)
    
    #making the folders
    making_folders(folders_paths)
    
    file_paths = get_file_paths(folder_path)

    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        if "." in file_name:
            ext = os.path.basename(file_path).split(".")[-1]
            folder_name = f"{ext}_files" 
        else:
            folder_name = "no_extension"
        
        if folder_name in folders_paths:
            dest_folder = folders_paths[folder_name]
        else:
            raise Exception(f"{folder_name} doesn't exist")
        
        dest_path = os.path.join(dest_folder, file_name)
        
        if not os.path.exists(dest_path):
            shutil.move(file_path, dest_folder)
        else:
            raise Exception(f"duplicate file:{dest_path}")





print(find_path("lol"))