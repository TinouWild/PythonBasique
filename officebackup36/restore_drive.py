from O365 import Account, MSGraphProtocol, FileSystemTokenBackend
import os

d = '/home/etienne/Documents/Perso/PythonBasique/officebackup36/Default Drive'
path = '/home/etienne/Documents/Perso/PythonBasique/officebackup365/'


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print('{}{}/'.format(indent, os.path.basename(root)))
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(sub_indent, f))


list_files(d)
# protocol = MSGraphProtocol(api_version='beta')
# credentials = ('7b9c81d7-2c01-4d48-86fc-9a7cd9700b85', 'cBPj06Vjh_[HNkntI-e6pEf.h1JKn12H')
#
# token_backend = FileSystemTokenBackend(token_path='my_folder', token_filename='my_token.txt')
# account = Account(credentials, protocol=protocol, token_backend=token_backend)
# account.authenticate(scopes=['basic', 'message_all', 'onedrive_all', 'address_book_all'])
#
# storage = account.storage()
# my_drive = storage.get_default_drive()
