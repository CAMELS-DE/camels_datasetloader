import os
from pathlib import Path
import configparser

import pandas as pd


def resolve_camels_de_root_path() -> Path:
    """
    Resolve the root path of the CAMELS-DE dataset.  
    Can be set via the environment variable CAMELS_ROOT_PATH or in a config.ini file.
    
    Returns
    -------
    Path
        The root path of the CAMELS-DE dataset.
        
    """
    # Check environment variable
    env_path = os.getenv('CAMELS_ROOT_PATH')
    if env_path:
        return Path(env_path)
    
    # Fallback to configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')  # Assuming your config file is named config.ini
    if 'CAMELS_DE' in config and 'CAMELS_ROOT_PATH' in config['CAMELS_DE']:
        return Path(config['CAMELS_DE']['CAMELS_ROOT_PATH'])
    
    # If neither is set, raise an error or return a default path
    raise ValueError("CAMELS_ROOT_PATH is not set in environment variables or config.ini")

def gauge_id_is_valid(gauge_id: str) -> bool:
    """
    Check if a gauge id is a valid CAMELS-DE ID.
    
    Parameters
    ----------
    gauge_id : str
        The gauge id to check.
    
    Returns
    -------
    bool
        True if the gauge id is valid, False otherwise.
    
    """
    root = resolve_camels_de_root_path()
    return gauge_id in pd.read_csv(root / "CAMELS_DE_topographic_attributes.csv")["gauge_id"].values