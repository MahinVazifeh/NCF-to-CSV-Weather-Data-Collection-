
"""
Extract NC and convert it to CSV
"""

import os
import yaml
from netCDF4 import Dataset
import h5py
import pandas as pd
import numpy as np
from typing import Dict, Any
import logging

class WeatherDataExtractor:
    def __init__(self, config_path: str = "config.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)
        
        # I need to call the return of data_downloder functions (both download data and preprocess data)
        self.preprocess_path = self.config["path"]["processed_data"]
        self.weather_name = self.config["data"]["weather_name"]


    def extract_data(self) -> Dict[str, pd.DataFrame]:
        data_tm = {}
        if self.weather_name == 'QQ':
            for loc in range(len(StationLocation)):
                lat = StationLocation['Index Lat'][loc]
                lon = StationLocation['Index Long'][loc]
                temp = []
                for tm in range(len(weather_feature.variables['qq'])):
                temp.append(weather_feature.variables['qq'][tm].data[lat,lon])
                data_tm[loc]= temp
                print(loc, temp)
        dataset = pd.DataFrame(data_tm)
        dataset = dataset.T
        dataset.to_csv('qq_weather_Bigdata_Spain.csv', index = False)
        else:
            for loc in range(len(StationLocation)):
            lat = StationLocation['Index Lat'][loc]
            lon = StationLocation['Index Long'][loc]
            temp = []
            for tm in range(len(weather_feature.variables['tx'])):
                temp.append(weather_feature.variables['tx'][tm].data[lat,lon])
            data_tm[loc]= temp

        dataset = pd.DataFrame(data_tm)
        dataset = dataset.T
            print(loc, temp)