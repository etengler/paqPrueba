"""Main module."""

import ipyleaflet

class Map(ipyleaflet.Map):
    """Esta es la clase map que hereda de ipyleaflet.Map.

    Args:
        ipyleaflet (Map): La clase ipyleaflet.Map.
    """    
    
    def __init__(self, center= [20, 0], zoom=2, **kwargs):
        """Inicializa el mapa

        Args:
            center (list, optional): Setea el centro del mapa. Por default toma estos valores [20, 0].
            zoom (int, optional): Setea el zoom del mapa. Por default toma el valor 2.
        """        
        super().__init__(center=center, zoom=zoom, **kwargs)
        self.add_control(ipyleaflet.LayersControl())


   