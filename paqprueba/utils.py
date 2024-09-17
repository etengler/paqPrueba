"""Este modulo contiene las funciones utility para paqprueba
"""

def csv_to_df(csv_file):
    """Convierte un CSV en un pandas data frame

    Args:
        csv_file (str): la direccion del archivo csv
    """
    import pandas as pd

    return pd.read_csv(csv_file)
