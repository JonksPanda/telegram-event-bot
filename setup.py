import yaml
import os.path

# Creates config.yml from passed arguments and/or receives data from config.yml


class Config:
    def __init__(self, token=None) -> None:
        self.YAML_PATH = "./config/conf.yaml"
        self.yaml_exists = os.path.exists(self.YAML_PATH)
        self.token = token

        if self.yaml_exists:
            self.read_yaml()
        else:
            self.create_yaml()

    def read_yaml(self):
        print("reading settings from config file..")
        with open(self.YAML_PATH, "r") as f:
            print(yaml.load(f, Loader=yaml.FullLoader))

    def create_yaml(self):
        print("no config file found! Generating new file on ./config/conf.yaml")
        yaml_input = [{"credentials": {"token": self.token}}]
        with open(self.YAML_PATH, "w") as f:
            yaml.dump(yaml_input, f)
        self.read_yaml()
