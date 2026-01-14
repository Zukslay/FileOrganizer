# FileOrganizer made with python
## what it does?
this program organizes the files of a folder into different subfolders according to file format.

<img width="500" height="677" alt="Screenshot 2026-01-14 114223" src="https://github.com/user-attachments/assets/535ab2a7-7140-4813-8473-453ebd4840e4" />

↓↓↓↓

<img width="500" height="672" alt="Screenshot 2026-01-14 114408" src="https://github.com/user-attachments/assets/86c520da-9baf-4507-b6b9-9721600548e0" />  <img width="500" height="678" alt="Screenshot 2026-01-14 114504" src="https://github.com/user-attachments/assets/f6ca1988-a6b8-4caf-88bb-33859f318fea" />

## how it works?
1. searchs trough all no-hidden folders in your home directory searching for the folder you want

2. then detects the different extensions that exist in the folder

3. create the folders where the files go.The folder names have this format → {extension}_files

4. moves all files to the corresponding folder(Files without extensions go to the no_extension folder).

## how to use it?
first you need to install python3
```shell
sudo apt install python3
```
then clone this repository
```shell
git clone https://github.com/Zukslay/FileOrganizer
cd FileOrganizer
```
Execute main.sh with the name or path of the folder you want to organize
```shell
./main.sh exampleName
```
The program can organize folders without knowing their path, as it searches the entire home directory for a folder with the specified name.





