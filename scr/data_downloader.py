"""
NC file downloader and preprocessor
"""

import os
import yaml
from netCDF4 import Dataset
import h5py
import pandas as pd
import numpy as np
from typing import Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WeatherDataDownloder:
    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)
        
        self.raw_data_path = self.config["path"]["raw_data"]

        os.makedirs(self.raw_data_path, exist_ok=True)
        os.makedirs(self.preprocess_path, exist_ok=True)
    
    def download_data(self) -> Dict[str, Any]:

        logger.info("Download Weather Data from E-Obs datasets provided by Copernicus")

        file_path = self.config["Paths"]["raw_data"]
        file_path = file_path + config["data"]["dataset_name"]
        dataset = Dataset(file_path, mode='r')
        print(dataset.variables.keys())

        weather_name = (file_path.split('/'))[-1].split('_')[0]
        latitude= pd.Series(dataset.variables['latitude'][:].data)
        longitude= pd.Series(dataset.variables['longitude'][:].data)

        return {
            'weather_name': weather_name,
            'latitude': latitude,
            'longitude': longitude
        }
    
    def preprocess_data(self, dataset_info: Dict[str, Any]) -> Dict[str, pd.DataFrame]:

        logger.info("Finding The Matcing Index")

        min_latitude = round(float(min(dataset_info['latitude'])), 2)
        min_longitude = round(float(min(dataset_info['longitude'])), 2)

        empty_df = pd.DataFrame()
        empty_df['E-OBS Latitude'] = dataset_info['latitude']
        empty_df['E-OBS Longitude'] = dataset_info['longitude']
        empty_df['Index Lat'] = ((dataset_info['latitude'].round(2) - min_latitude) * 10).round(0).astype(int)
        empty_df['Index Long'] = ((dataset_info['longitude'] - min_longitude) * 10).round(0).astype(int)

        return {"processed_df": empty_df}


def main():
    downloader = WeatherDataDownloder()
    
    # Download data
    raw_data = downloader.download_data()
    
    # Preprocess data
    processed_data = downloader.preprocess_data(raw_data)
    
    logger.info("Data download and preprocessing completed!")

if __name__ == "__main__":
    main()









