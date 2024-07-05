import pandas as pd
import geopandas as gpd

from .util import gauge_id_is_valid, resolve_camels_de_root_path


def get_timeseries(gauge_id: str, variables: list[str] = None) -> pd.DataFrame:
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
    root = resolve_camels_de_root_path()
    df = pd.read_csv(root / "timeseries" / f"CAMELS_DE_hydromet_timeseries_{gauge_id}.csv", parse_dates=["date"], index_col="date")
    
    if variables is not None:
        # make sure variables is a list
        if not isinstance(variables, list):
            variables = [variables]

        # check if variables are in columns
        for variable in variables:
            if variable not in df.columns:
                raise ValueError(f"{variable} is not a valid variable.")
        
        # return only the selected variables
        return df[variables]
    
    return df

def get_catchments(gauge_id: str = None) -> gpd.GeoDataFrame:
    """
    Function to get the catchment boundaries.  
    If a gauge_id is provided, only the catchments for that station are returned.

    
    Parameters
    ----------
    gauge_id : str, optional
        The id of the station to get the catchments for.

    Returns
    -------
    gpd.GeoDataFrame
        The catchments GeoDataFrame table.

    """
    root = resolve_camels_de_root_path()
    catchments = gpd.read_file(root / "CAMELS_DE_catchment_boundaries" / "catchments" / "CAMELS_DE_catchments.gpkg")
    
    if gauge_id is not None:
        if not gauge_id_is_valid(gauge_id):
            raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
        return catchments[catchments["gauge_id"] == gauge_id]
    
    return catchments

def get_attributes(type: str, gauge_id: str = None, variables: list[str] = None) -> pd.DataFrame:
    """
    Function to get the attributes of a specific type.
    If a gauge_id is provided, only the attributes for that station are returned.
    
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
    if type not in ["topographic", "soil", "landcover", "hydrogeology", "humaninfluence", "climatic", "hydrologic", "simulation_benchmark"]:
        raise ValueError(f"{type} is not a valid attribute type, must be one of ['topographic', 'soil', 'landcover', 'hydrogeology', 'humaninfluence', 'climatic', 'hydrologic', 'simulation_benchmark']")
    
    # Resolve the root path of the CAMELS-DE dataset
    root = resolve_camels_de_root_path()

    # Load the attributes
    df = pd.read_csv(root / f"CAMELS_DE_{type}_attributes.csv")

    if gauge_id is not None:
        if not gauge_id_is_valid(gauge_id):
            raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
        return df[df["gauge_id"] == gauge_id]
    
    if variables is not None:
        # make sure variables is a list
        if not isinstance(variables, list):
            variables = [variables]

        # check if variables are in columns
        for variable in variables:
            if variable not in df.columns:
                raise ValueError(f"{variable} is not a valid variable.")
        
        # return only the selected variables
        return df[variables]
    
    return df
