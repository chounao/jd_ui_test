from common.read_tools import ReadFileData
import yaml


class yaml_tool:
    def save_yaml(self,path,save_data):
        """保存yaml"""
        print(path,save_data)
        with open(path, "w", encoding="utf-8") as f:
            f.write(save_data)
    def save_yaml_dict(self,path,save_data):
        """保存成字典"""
        with open(path,"w",encoding="utf-8")as f:
            yaml.dump(save_data,f)
    def read_yamlDatas(self,path):
        """获取token和参数方法"""
        self.token_data =ReadFileData.load_yaml(path)

        return self.token_data
    def read_data(self,key,value,path):
        try:
            self.data = self.read_yamlDatas(path)
            if key in self.data.keys():
                return self.data[key][value]
        except :
            print("找不到对应的%s ",key)