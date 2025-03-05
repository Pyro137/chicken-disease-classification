
from cnnClassifier.constant import *
from cnnClassifier.utils.common import read_yaml,create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig
class ConfigurationManager:
    def __init__(self, config_yaml=CONFIG_FILE_PATH,params_yaml=PARAMS_FILE_PATH):
        self.config = read_yaml(config_yaml)
        self.params = read_yaml(params_yaml)

        create_directories([self.config.data_ingestion.root_dir])
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config