import yaml
class YamlUtli:
    def __init__(self,yaml_file):
        self.yaml_file = yaml_file

    def read_yaml(self):
        with open(self.yaml_file,encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            print(value['loginpage'])

if __name__ == '__main__':
    YamlUtli('/APP_QQ_login/test_yaml/test_yaml.yaml').read_yaml()