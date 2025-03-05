from cnnClassifier.utils.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel


class PrepareBaseModelPipeline:
    def __init__(self):
        pass
    def main(self):
        config_manager=ConfigurationManager()
        base_model_config=config_manager.get_prepare_base_model_config()
        prepare_base_model=PrepareBaseModel(base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.updated_base_model()
