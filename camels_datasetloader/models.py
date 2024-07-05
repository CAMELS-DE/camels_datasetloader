import os
from pathlib import Path

import pandas as pd

from .util import gauge_id_is_valid, resolve_camels_de_root_path
from .get_data import get_timeseries, get_topographic_attributes, get_soil_attributes, get_landcover_attributes, get_hydrogeology_attributes, get_humaninfluence_attributes, get_climatic_attributes, get_hydrologic_attributes, get_climatic_attributes


class Station():
    """
    Class to represent a station in the CAMELS-DE dataset.
    
    """
    def __init__(self, gauge_id: str):
        """
        Parameters
        ----------
        gauge_id : str
            The id of the station (e.g. "DE110000").
        
        """
        if not gauge_id_is_valid(gauge_id):
            raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
        self.gauge_id = gauge_id

    def __repr__(self):
        return f"{self.gauge_id} Station object"
    
    def get_timeseries(self, variables: list[str] = None) -> pd.DataFrame:
        """
        Get the timeseries data of the station.  
        If a list of variables is provided, only the data for those variables is returned.
        
        Parameters
        ----------
        variables : list[str], optional
            The variables to get the timeseries data for.
        
        Returns
        -------
        pd.DataFrame
            The timeseries data.
        
        """
        return get_timeseries(self.gauge_id, variables)
        

class CAMELS_DE():
    """
    Class to represent the CAMELS-DE dataset.
    
    """
    def __init__(self):
        """
        Parameters
        ----------
        root : str
            The root directory of the CAMELS-DE dataset.
        
        """      
        self.root = resolve_camels_de_root_path()
    
    def get_station(self, gauge_id: str) -> Station:
        """
        Get a station by its gauge id.
        
        Parameters
        ----------
        gauge_id : str
            The id of the station.
        
        Returns
        -------
        Station
            The station object.
        
        """
        return Station(gauge_id)
    
    def get_topographic_attributes(self, gauge_id: str = None) -> pd.DataFrame:
        """
        Get the topographic attributes of all stations.  
        If a gauge id is provided, only the attributes of that station are returned.
        
        Parameters
        ----------
        gauge_id : str, optional
            The id of the station to get the attributes for.

        Returns
        -------
        pd.DataFrame
            The topographic attributes.
        
        """
        return get_topographic_attributes(gauge_id)
    
    def get_soil_attributes(self, gauge_id: str = None) -> pd.DataFrame:
        """
        Get the soil attributes of all stations.  
        If a gauge id is provided, only the attributes of that station are returned.
        
        Parameters
        ----------
        gauge_id : str, optional
            The id of the station to get the attributes for.

        Returns
        -------
        pd.DataFrame
            The soil attributes.
        
        """
        return get_soil_attributes(gauge_id)
    
    def get_landcover_attributes(self, gauge_id: str = None) -> pd.DataFrame:
        """
        Get the landcover attributes of all stations.  
        If a gauge id is provided, only the attributes of that station are returned.
        
        Parameters
        ----------
        gauge_id : str, optional
            The id of the station to get the attributes for.

        Returns
        -------
        pd.DataFrame
            The landcover attributes.
        
        """
        return get_landcover_attributes(gauge_id)
    
    def get_hydrogeology_attributes(self, gauge_id: str = None) -> pd.DataFrame:
        """
        Get the hydrogeology attributes of all stations.  
        If a gauge id is provided, only the attributes of that station are returned.
        
        Parameters
        ----------
        gauge_id : str, optional
            The id of the station to get the attributes for.

        Returns
        -------
        pd.DataFrame
            The hydrogeology attributes.
        
        """
        return get_hydrogeology_attributes(gauge_id)
    
    def get_humaninfluence_attributes(self, gauge_id: str = None) -> pd.DataFrame:
        """
        Get the human influence attributes of all stations.  
        If a gauge id is provided, only the attributes of that station are returned.
        
        Parameters
        ----------
        gauge_id : str, optional
            The id of the station to get the attributes for.

        Returns
        -------
        pd.DataFrame
            The human influence attributes.
        
        """
        return get_humaninfluence_attributes(gauge_id)
    
    def get_climatic_attributes(self, gauge_id: str = None) -> pd.DataFrame:
        """
        Get the climatic attributes of all stations.  
        If a gauge id is provided, only the attributes of that station are returned.
        
        Parameters
        ----------
        gauge_id : str, optional
            The id of the station to get the attributes for.

        Returns
        -------
        pd.DataFrame
            The climatic attributes.
        
        """
        return get_climatic_attributes(gauge_id)
    
    def get_hydrologic_attributes(self, gauge_id: str = None) -> pd.DataFrame:
        """
        Get the hydrologic attributes of all stations.  
        If a gauge id is provided, only the attributes of that station are returned.
        
        Parameters
        ----------
        gauge_id : str, optional
            The id of the station to get the attributes for.

        Returns
        -------
        pd.DataFrame
            The hydrologic attributes.
        
        """
        return get_hydrologic_attributes(gauge_id)
    
    def get_climatic_attributes(self, gauge_id: str = None) -> pd.DataFrame:
        """
        Get the climatic attributes of all stations.  
        If a gauge id is provided, only the attributes of that station are returned.
        
        Parameters
        ----------
        gauge_id : str, optional
            The id of the station to get the attributes for.

        Returns
        -------
        pd.DataFrame
            The climatic attributes.
        
        """
        return get_climatic_attributes(gauge_id)
