import os

def create_folders():
    for i in range(1, 10):
        folder_name = f'dir{i}'
        os.mkdir(folder_name)
        print(f'папка {i} создана')
    
# print(create_folders())

def remove_folders():
    for i in range(1, 10):
        folder_name = f'dir{i}'
        os.rmdir(folder_name)
        print(f'папка {i} удалена')

# print(remove_folders())
