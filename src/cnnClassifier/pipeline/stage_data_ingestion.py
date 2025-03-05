from cnnClassifier.utils.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion




class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        configuration_manager=ConfigurationManager()
        data_ingestion_config=configuration_manager.get_data_ingestion_config()
        data_ingestion=DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

        


