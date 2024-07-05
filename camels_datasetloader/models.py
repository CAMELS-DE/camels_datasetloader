import os
from pathlib import Path

import pandas as pd

from .util import gauge_id_is_valid, resolve_camels_de_root_path


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
        df = pd.read_csv(self.root / "CAMELS_DE_topographic_attributes.csv")

        if gauge_id is not None:
            if not gauge_id_is_valid(gauge_id):
                raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
            return df[df["gauge_id"] == gauge_id]
        
        return df
    
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
        df = pd.read_csv(self.root / "CAMELS_DE_soil_attributes.csv")

        if gauge_id is not None:
            if not gauge_id_is_valid(gauge_id):
                raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
            return df[df["gauge_id"] == gauge_id]
        
        return df
    
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
        df = pd.read_csv(self.root / "CAMELS_DE_landcover_attributes.csv")

        if gauge_id is not None:
            if not gauge_id_is_valid(gauge_id):
                raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
            return df[df["gauge_id"] == gauge_id]
        
        return df
    
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
        df = pd.read_csv(self.root / "CAMELS_DE_hydrogeology_attributes.csv")

        if gauge_id is not None:
            if not gauge_id_is_valid(gauge_id):
                raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
            return df[df["gauge_id"] == gauge_id]
        
        return df
    
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
        df = pd.read_csv(self.root / "CAMELS_DE_humaninfluence_attributes.csv")

        if gauge_id is not None:
            if not gauge_id_is_valid(gauge_id):
                raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
            return df[df["gauge_id"] == gauge_id]
        
        return df
    
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
        df = pd.read_csv(self.root / "CAMELS_DE_climatic_attributes.csv")

        if gauge_id is not None:
            if not gauge_id_is_valid(gauge_id):
                raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
            return df[df["gauge_id"] == gauge_id]
        
        return df
    
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
        df = pd.read_csv(self.root / "CAMELS_DE_hydrologic_attributes.csv")

        if gauge_id is not None:
            if not gauge_id_is_valid(gauge_id):
                raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
            return df[df["gauge_id"] == gauge_id]
        
        return df
    
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
        df = pd.read_csv(self.root / "CAMELS_DE_climatic_attributes.csv")

        if gauge_id is not None:
            if not gauge_id_is_valid(gauge_id):
                raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
            return df[df["gauge_id"] == gauge_id]
        
        return df
