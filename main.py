from sensor.logger import logging
from sensor.exception import SensorException
import sys,os
from sensor.entity import config_entity


if __name__=="__main__":
      try:
         try:
            training_pipeline_config = config_entity.TrainingPipelineConfig()
            data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
            print(data_ingestion_config.to_dict())
            #data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            #print(data_ingestion.initiate_data_ingestion())
         except Exception as e:
            print(e)
      except Exception as e:
         print(e)