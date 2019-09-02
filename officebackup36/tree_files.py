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
