import yaml
import os.path

# Creates config.yml from passed arguments and/or receives data from config.yml


class Config:
    def __init__(self, token=None) -> None:
        self.YAML_PATH = "/config/conf.yaml"
        self.yaml_exists = os.path.exists(self.YAML_PATH)
        self.token = token

        if self.yaml_exists:
            self.read_yaml()
        else:
            self.create_yaml()

    def read_yaml(self):
        pass

    def create_yaml(self):
        pass
