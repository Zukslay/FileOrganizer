import os
from helper_functions import get_extensions, get_folders, making_folders_get_paths, get_file_paths

#checking if the folder exists
def find(folder_name):
    home = '/home'

    #iterating over all folders
    for dirpath, _, _ in os.walk(home):
        if dirpath.split("/")[-1] == folder_name:
            return dirpath
    raise Exception(f"folder:{folder_name} doesn't exists")

def organizer(folder_path):
    extensions = get_extensions(folder_path)
    folders_names = get_folders(extensions)

    #all the content of the folder
    content = os.listdir(folder_path)
    
    #making the folders and getting the paths
    making_folders_get_paths(folder_path, content, folders_names)
    
    file_paths = get_file_paths(folder_path, content)





print(find("lol"))