from src.config_reader import read_config
from src.data_ingestion import DataIngestion
from src.data_processing import DataProcessing
from src.model_training import ModelTraining

if __name__ == "__main__":
    config_path = "config/config.yaml"

    data_ingestion = DataIngestion(config_path)
    data_ingestion.run()

    data_processing = DataProcessing(config_path)
    data_processing.run()

    model_training = ModelTraining(config_path)
    model_training.run()
