from updater import Updater
import yaml


class Test(object):
    def __init__(self):
        app_update_filepath = 'sub_config/app-update/app-update.yml'
        update_info = yaml.load(open(app_update_filepath))
        url = update_info['url'] + '/win-unpacked'
        self.exe = Updater(url=url).exe


exeCollector = Test()
print exeCollector.exe
