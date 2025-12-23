import os

#obtaining the .<format> from all files in the folder
def get_extensions(folder_path):
    pass

#all possible names of folders: example "jpg_files"
def get_folders(extensions):
    pass

def making_folders_get_paths(folder_path, folder_files, folders_names):
    l = []
    for file_name in folder_files:
        path = os.path.join(folder_path, file_name)
        
        if os.path.isdir(path) and file_name not in folders_names:
            os.mkdir(path)
        
        if os.path.isdir(path):
            l.append(path)
    return l

def get_file_paths(folder_path, folder_files):
    l = []
    for file_name in folder_files:
        path = os.path.join(folder_path, file_name)
        if os.path.isfile(path):
            l.append(path)
    return l