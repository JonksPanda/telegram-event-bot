import yaml
import os.path

# Creates config.yml from passed arguments and/or receives data from config.yml


class Config:
    def __init__(self, token=None) -> None:
        self.YAML_PATH = "./config/conf.yaml"
        self.yaml_exists = os.path.exists(self.YAML_PATH)
        self.token = token

        if self.yaml_exists:
            print("reading settings from config file..")
            self.read_yaml()
        else:
            print("no config file found! Generating new file on /config/conf.yaml")
            self.create_yaml()

    def read_yaml(self):
        pass

    def create_yaml(self):
        yaml_input = [{"token": self.token}]
        with open(self.YAML_PATH, "w") as file:
            yaml.dump(yaml_input, file)
