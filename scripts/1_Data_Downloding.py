"""
Script to download and preprocess weather NC file
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scr.data_downloader import WeatherDataDownloder
from scr.utils import setup_logging, set_seed, create_directories, load_config

def main():
    config = load_config()
    setup_logging()
    set_seed(42)
    create_directories(config)

    print("*"*60)
    print("Weather Data Download")
    print("*"*60)

    downloader = WeatherDataDownloder()
    print("download the dataset from the Copernicus European Open Source")

    row_data = downloader.download_data()
    preprocess_data = downloader.preprocess_data(row_data)

    
    print("*"*60)
    print("Download data completed successfully!")
    print("*"*60)

    if __name__ == "__main__":
        main()

