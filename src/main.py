from src.config_reader import read_config
from src.data_ingestion import DataIngestion

data_ingestion = DataIngestion(read_config("config/config.yaml"))
data_ingestion.run()
