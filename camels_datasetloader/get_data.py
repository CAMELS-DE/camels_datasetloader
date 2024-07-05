import pandas as pd

from .util import gauge_id_is_valid, resolve_camels_de_root_path


def get_topographic_attributes(gauge_id: str = None) -> pd.DataFrame:
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
    # Resolve the root path of the CAMELS-DE dataset
    root = resolve_camels_de_root_path()

    # Load the topographic attributes
    df = pd.read_csv(root / "CAMELS_DE_topographic_attributes.csv")

    if gauge_id is not None:
        if not gauge_id_is_valid(gauge_id):
            raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
        return df[df["gauge_id"] == gauge_id]
    
    return df
    
def get_soil_attributes(gauge_id: str = None) -> pd.DataFrame:
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
    # Resolve the root path of the CAMELS-DE dataset
    root = resolve_camels_de_root_path()

    # Load the soil attributes
    df = pd.read_csv(root / "CAMELS_DE_soil_attributes.csv")

    # Filter by gauge id if provided
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
    # Resolve the root path of the CAMELS-DE dataset
    root = resolve_camels_de_root_path()

    # Load the landcover attributes
    df = pd.read_csv(self.root / "CAMELS_DE_landcover_attributes.csv")

    if gauge_id is not None:
        if not gauge_id_is_valid(gauge_id):
            raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
        return df[df["gauge_id"] == gauge_id]
    
    return df

def get_hydrogeology_attributes(gauge_id: str = None) -> pd.DataFrame:
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
    # Resolve the root path of the CAMELS-DE dataset
    root = resolve_camels_de_root_path()

    # Load the hydrogeology attributes
    df = pd.read_csv(root / "CAMELS_DE_hydrogeology_attributes.csv")

    if gauge_id is not None:
        if not gauge_id_is_valid(gauge_id):
            raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
        return df[df["gauge_id"] == gauge_id]
    
    return df

def get_humaninfluence_attributes(gauge_id: str = None) -> pd.DataFrame:
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
    # Resolve the root path of the CAMELS-DE dataset
    root = resolve_camels_de_root_path()

    # Load the human influence attributes
    df = pd.read_csv(root / "CAMELS_DE_humaninfluence_attributes.csv")

    if gauge_id is not None:
        if not gauge_id_is_valid(gauge_id):
            raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
        return df[df["gauge_id"] == gauge_id]
    
    return df

def get_climatic_attributes(gauge_id: str = None) -> pd.DataFrame:
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
    # Resolve the root path of the CAMELS-DE dataset
    root = resolve_camels_de_root_path()

    # Load the climatic attributes
    df = pd.read_csv(root / "CAMELS_DE_climatic_attributes.csv")

    if gauge_id is not None:
        if not gauge_id_is_valid(gauge_id):
            raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
        return df[df["gauge_id"] == gauge_id]
    
    return df

def get_hydrologic_attributes(gauge_id: str = None) -> pd.DataFrame:
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
    # Resolve the root path of the CAMELS-DE dataset
    root = resolve_camels_de_root_path()

    # Load the hydrologic attributes
    df = pd.read_csv(root / "CAMELS_DE_hydrologic_attributes.csv")

    if gauge_id is not None:
        if not gauge_id_is_valid(gauge_id):
            raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
        return df[df["gauge_id"] == gauge_id]
    
    return df

def get_climatic_attributes(gauge_id: str = None) -> pd.DataFrame:
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
    # Resolve the root path of the CAMELS-DE dataset
    root = resolve_camels_de_root_path()

    # Load the climatic attributes
    df = pd.read_csv(root / "CAMELS_DE_climatic_attributes.csv")

    if gauge_id is not None:
        if not gauge_id_is_valid(gauge_id):
            raise ValueError(f"{gauge_id} is not a valid CAMELS-DE gauge id.")
        return df[df["gauge_id"] == gauge_id]
    
    return df