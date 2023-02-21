import pandas as pd
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.config import mongo_client
import os,sys
def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
