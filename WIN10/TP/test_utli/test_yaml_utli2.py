# import yaml
# class YamlUtli2:
#     def __init__(self,yaml_file):
#         self.yaml_file = yaml_file
#
#     def read_yaml(self):
#         with open(self.yaml_file,encoding='utf-8') as f:
#             value = yaml.load(f, Loader=yaml.FullLoader)
#             return value["loginpage2"]
# if __name__ == '__main__':
#     YamlUtli2('../test_yaml/test_yaml.yaml').read_yaml()