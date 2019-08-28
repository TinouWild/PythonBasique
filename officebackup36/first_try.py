# client ID: 7b9c81d7-2c01-4d48-86fc-9a7cd9700b85
# client secret: cBPj06Vjh_[HNkntI-e6pEf.h1JKn12H

from O365 import Account
from O365 import MSGraphProtocol
from O365 import FileSystemTokenBackend
import os

path = os.path.dirname(os.path.abspath(__file__))
directory_save = os.path.join(path, 'drive_sauvegarde')
os.makedirs(directory_save, exist_ok=1)


def create_folder(item):
    folder = os.path.join(directory_save, item.name)
    os.makedirs(folder, exist_ok=1)
    print(f"Dossier {item.name} créé avec succès !")
    return folder


def download_file(item, path):
    item.download(to_path=path)
    print(f"Fichier {item.name} téléchargé avec succès !")


protocol = MSGraphProtocol(api_version='beta')
credentials = ('7b9c81d7-2c01-4d48-86fc-9a7cd9700b85', 'cBPj06Vjh_[HNkntI-e6pEf.h1JKn12H')

token_backend = FileSystemTokenBackend(token_path='my_folder', token_filename='my_token.txt')
account = Account(credentials, protocol=protocol, token_backend=token_backend)
account.authenticate(scopes=['basic', 'message_all', 'onedrive_all'])

storage = account.storage()
my_drive = storage.get_default_drive()

for item in my_drive.get_items():
    if item.is_folder and item.child_count > 0:
        folder = create_folder(item)
        for file in item.get_items():
            if file.is_file:
                download_file(file, folder)
    elif item.is_file:
        download_file(item, directory_save)
