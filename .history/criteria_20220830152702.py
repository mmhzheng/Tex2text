

class Criteria : 
    """
    Abstraction for user-defined criterias.
    """
    def __init__(self, expr : str):
        self.pattern = “
        self.substitute = ""
        pass
    
    def apply(self, line : str ) -> str:
        """_summary_
        Args:
            line (str): original string.
        Returns:
            str: processed string.
        """
        
        