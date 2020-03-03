import json
import string
import os
import yaml


class ExeCollector(object):
    def __init__(self):
        self.url = self.get_url_channel()
        self.get_exe_version()

    def get_exe_version(self):
        with open('sub_config/config/config.json') as json_file:
            data = json.load(json_file)
            if 'exe' in data:
                return self.get_exe_from_config(data)
            else:
                return self.get_exe_from_channel()

    def get_exe_from_config(self, data):
        if data['exe'] == 'Kiwi-Backup' or data['exe'] == 'Kiwi-Sante':
            return data['exe'] + '.exe'
        else:
            return data['exe']

    def get_exe_from_channel(self):
        channel = string.rsplit(self.url, '/')
        if 'classic' in channel:
            return 'Kiwi-Backup.exe'
        elif 'sante' in channel:
            return 'Kiwi-Sante.exe'
        else:
            return self.get_exe_kit_from_channel(self.url)

    def get_url_channel(self):
        update_file = 'sub_config/app-update/app-update.yml'
        update_info = yaml.load(open(update_file))
        return update_info['url']

    def get_exe_kit_from_channel(self, url):
        data = url.split('/')[3]
        exe = data.split('-', 2)[2]
        return exe


print ExeCollector().get_exe_version()
