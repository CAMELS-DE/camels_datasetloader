import os
from pathlib import Path

import pandas as pd
import geopandas as gpd

from .util import gauge_id_is_valid, resolve_camels_de_root_path
from .get_data import get_timeseries, get_attributes, get_catchments_geometry, get_stations_geometry


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

    def get_attributes(self, type: str, variables: list[str] = None) -> pd.DataFrame:
        """
        Get the attributes of a specific type.
        
        Parameters
        ----------
        type : str
            The type of attributes to get.  
            Must be one of ["topographic", "soil", "landcover", "hydrogeology", "humaninfluence", "climatic", "hydrologic", "simulation_benchmark"].
        variables : list[str], optional
            The variables to get the attributes for.
        
        Returns
        -------
        pd.DataFrame
            The attributes table of the specified type.
        
        """
        return get_attributes(type, self.gauge_id, variables)

    def get_catchments_geometry(self) -> gpd.GeoDataFrame:
        """
        Get the catchment boundaries of the station.
        
        Returns
        -------
        gpd.GeoDataFrame
            The catchments GeoDataFrame table.
        
        """
        return get_catchments_geometry(self.gauge_id)

    def get_stations_geometry(self) -> gpd.GeoDataFrame:
        """
        Get the location of the station.
        
        Returns
        -------
        gpd.GeoDataFrame
            The station GeoDataFrame table.
        
        """
        return get_stations_geometry(self.gauge_id)

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
    
    def get_timeseries(self, gauge_id: str, variables: list[str] = None) -> pd.DataFrame:
        """
        Get the timeseries data of a station.  
        If a list of variables is provided, only the data for those variables is returned.
        
        Parameters
        ----------
        gauge_id : str
            The id of the station.
        variables : list[str], optional
            The variables to get the timeseries data for.
        
        Returns
        -------
        pd.DataFrame
            The timeseries data.
        
        """
        return get_timeseries(gauge_id, variables)
    
    def get_attributes(self, type: str, gauge_id: str = None, variables: list[str] = None) -> pd.DataFrame:
        """
        Get the attributes of a specific type.  
        If a gauge id is provided, only the attributes of that station are returned.
        
        Parameters
        ----------
        type : str
            The type of attributes to get.  
            Must be one of ["topographic", "soil", "landcover", "hydrogeology", "humaninfluence", "climatic", "hydrologic", "simulation_benchmark"].
        gauge_id : str, optional
            The id of the station to get the attributes for.
        variables : list[str], optional
            The variables to get the attributes for.
        
        Returns
        -------
        pd.DataFrame
            The attributes table of the specified type.
        
        """
        return get_attributes(type, gauge_id, variables)
    
    def get_catchments_geometry(self, gauge_id: str = None) -> gpd.GeoDataFrame:
        """
        Get the catchment boundaries.  
        If a gauge id is provided, only the catchments for that station are returned.
        
        Parameters
        ----------
        gauge_id : str, optional
            The id of the station to get the catchments for.
        
        Returns
        -------
        gpd.GeoDataFrame
            The catchments GeoDataFrame table.
        
        """
        return get_catchments_geometry(gauge_id)
    
    def get_stations_geometry(self, gauge_id: str = None) -> gpd.GeoDataFrame:
        """
        Get the station locations.  
        If a gauge id is provided, only the station for that id is returned.
        
        Parameters
        ----------
        gauge_id : str, optional
            The id of the station to get the stations for.
        
        Returns
        -------
        gpd.GeoDataFrame
            The stations GeoDataFrame table.
        
        """
        return get_stations_geometry(gauge_id)