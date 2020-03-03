import yaml
import json
import string


class Updater(object):
    def __init__(self, url):
        app_update_filepath = 'sub_config/app-update/app-update.yml'
        update_info = yaml.load(open(app_update_filepath))
        self.url = update_info['url'] + '/win-unpacked'
        self.exe = self.get_exe_version()

    def get_exe_version(self, operation='update'):
        with open('sub_config/config/config.json') as json_file:
            data = json.load(json_file)
            if 'exe' in data:
                return self.get_exe_from_config(data, operation=operation)
            else:
                return self.get_exe_from_channel(operation=operation)

    def get_exe_from_config(self, data, operation='update'):
        if data['exe'] == 'Kiwi-Backup' or data['exe'] == 'Kiwi-Sante':
            return data['exe'] + '.exe'
        elif operation == 'update':
            if data['exe'] == 'Kiwi-Backup.exe' or data['exe'] == 'Kiwi-Sante.exe':
                return data['exe']
            else:
                return 'Backup.exe'
        else:
            return data['exe']

    def get_exe_from_channel(self, operation='update'):
        channel = string.rsplit(self.url, '/')
        if 'classic' in channel:
            return 'Kiwi-Backup.exe'
        elif 'sante' in channel:
            return 'Kiwi-Sante.exe'
        elif operation == 'task_update':
            return self.url


