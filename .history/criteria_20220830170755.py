import re
from enum import Enum

class SubstituteType(Enum):
    """
    A enum class for flow attributes
    """
    Empty = 1
    Reserve = 2
    Stmbol = 3

class Criteria : 
    """
    Abstraction for user-defined criterias.
    """
    def __init__(self, pattern : str, substitute : str, flag : str):
        self.pattern = pattern
        
        if substitute[0] == '$':
            if substitute[1] == '0': 
                self.substitute = SubstituteType.Empty
            else:
                self.substitute = SubstituteType.Reserve
        else:
            self.substitute = SubstituteType.SYMBOLE
            
        self.flag = flag
        pass
    
    def apply(self, line : str ) -> str:
        """_summary_
        Args:
            line (str): original string.
        Returns:
            str: processed string.
        """
        match = re.search(pattern2, line2)
        return re.sub(self.pattern, self.substitute, line, flags=self.flag)
        
        
def parse_criterion(line: str) -> Criteria:
    items = line.split("->")
    pattern = items[0].strip()
    targets = items[1].strip().split(":")
    if len(targets) > 1:
        return Criteria(pattern, targets[0], targets[1])
    else:
        return Criteria(pattern, targets[0], "")