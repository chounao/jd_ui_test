import yaml
import json
from configparser import ConfigParser

class MyconfigParser(ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class ReadFileData():
    def __init__(self):
        pass

    def load_yaml(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data

    def load_json(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    def load_ini(self, file_path):
        config = MyconfigParser()
        config.read(file_path, encoding='utf-8')
        data = dict(config._sections)
        # print(data)
        # print(data['HTTP']['jd_loginUrl'])
        return data

class ReadPagedata():
    def read_page(self,page,selectors):
        if hasattr(page,selectors):
            data = getattr(page,selectors)
            by = data(selectors)[0]
            value = data(selectors)[1]
            return by,value
        else:
            return None,None

# if __name__ == '__main__':
#     from common.path_tools import getPath
#     a = ReadFileData()
#     path = getPath()
#     config_path = '\config.ini'  # ini文件路径
#     file_path = path.get_path() + config_path
#     a.load_ini(file_path)
