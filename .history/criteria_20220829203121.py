

class Criteria : 
    """
    Abstraction for user-defined criterias.
    """
    def __init__(self, expr : str):
        pass
    
    def apply(self, line : str ) -> str:
        """_summary_
        Args:
            line (str): 
        Returns:
            str: processed string.
        """
        