import os

#obtaining the .<format> from all files in the folder
def get_extensions(folder_path):
    l = []
    for f in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, f)):
            l.append(f.split(".")[-1])
    return list(set(l))

#all possible names of folders: example "jpg_files"
def get_folders(extensions, folder_path):
    d = {}
    for f in extensions:
        d[f"{f}_files"] = os.path.join(folder_path ,f"{f}_files")
    for f in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, f)):
            d[f] = os.path.join(folder_path, f)
    d["no_extension"] = os.path.join(folder_path, "no_extension")
    return d

def making_folders(folders_paths):
    for path in folders_paths:
        if not os.path.exists(folders_paths[path]):
            os.mkdir(folders_paths[path])

def get_file_paths(folder_path):
    d = []
    for file_name in os.listdir(folder_path):
        path = os.path.join(folder_path, file_name)
        if os.path.isfile(path):
            d.append(path)
    return d