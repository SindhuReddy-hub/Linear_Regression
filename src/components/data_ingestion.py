import numpy as np
import pandas as pd
import os
from pathlib import Path
import matplotlib.pyplot as plt
#from src.linear.logging import logger
from sklearn.model_selection import train_test_split
print("currnt path ",os. getcwd())
from src.linear.logging import logger
from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class DataIngestionConfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','data.csv')
class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        logger.info('Enter the data ingestion method')
        try:
            df=pd.read_csv('data\cars.csv')
            logger.info("reading the dataset")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logger.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logger.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except:
            print("Exception raised in data ingestion")
        
