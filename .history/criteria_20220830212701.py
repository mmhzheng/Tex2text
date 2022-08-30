import re
from enum import Enum

class SubstituteType(Enum):
    """
    A enum class for flow attributes
    """
    Empty = 1
    Reserve = 2
    Symbol = 3

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
            self.substitute = SubstituteType.Symbol
            
        if flag == "":
            self.flag = 0
        else:
            self.flag = re.S
        pass
    
    def apply(self, line : str ) -> str:
        """_summary_
        Args:
            line (str): original string.
        Returns:
            str: processed string.
        """
        print(f"{self.pattern}")
        if self.substitute == SubstituteType.Reserve:
            match = re.search(self.pattern, line, flags=self.flag)
            if match is not None:
                text = match.group(1)
                return re.sub(self.pattern, r'\1 XBACKSLASHXcdot \2', line, flags=self.flag).replace('XBACKSLASHX', text)
            else:
                return line
        elif self.substitute == SubstituteType.Empty:
            return re.sub(self.pattern, "", line, flags=self.flag)
        else:
            return re.sub(self.pattern, "SYMBOL", line, flags=self.flag)

            
        
def parse_criterion(line: str) -> Criteria:
    items = line.split("->")
    pattern = r'{}'.format(items[0].strip())
    targets = items[1].strip().split(":")
    if len(targets) > 1:
        return Criteria(pattern, r'{}'.format(targets[0]), r'{}'.format(targets[1]))
    else:
        return Criteria(pattern, r'{}'.format(targets[0]), "")
