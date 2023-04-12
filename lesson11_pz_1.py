import os

def create_folders():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.mkdir(folder_name)
        print(f'папка {i} создана')
    
# create_folders()

def remove_folders():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.rmdir(folder_name)
        print(f'папка {i} удалена')

# remove_folders()
