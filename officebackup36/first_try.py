# client ID: 7b9c81d7-2c01-4d48-86fc-9a7cd9700b85
# client secret: cBPj06Vjh_[HNkntI-e6pEf.h1JKn12H

from O365 import Account
from O365 import MSGraphProtocol
from O365 import FileSystemTokenBackend
import sys
import os

protocol = MSGraphProtocol(api_version='beta')
credentials = ('7b9c81d7-2c01-4d48-86fc-9a7cd9700b85', 'cBPj06Vjh_[HNkntI-e6pEf.h1JKn12H')

token_backend = FileSystemTokenBackend(token_path='my_folder', token_filename='my_token.txt')
account = Account(credentials, protocol=protocol, token_backend=token_backend)
account.authenticate(scopes=['basic', 'message_all', 'onedrive_all'])

# OneDrive
storage = account.storage()
# all_drives = storage.get_drives()
my_drive = storage.get_default_drive()

for item in my_drive.get_items():
    print(item.name)

path = os.path.dirname(os.path.abspath(__file__))
directory_save = os.path.join(path, 'drive_sauvegarde')
os.makedirs(directory_save, exist_ok=1)

def create_folder(item):
    pass
