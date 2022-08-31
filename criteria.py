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
                self.substitute_type = SubstituteType.Empty
            else:
                self.substitute_type = SubstituteType.Reserve
        else:
            self.substitute_type = SubstituteType.Symbol
            self.substitute_content = substitute
            
        if flag == "":
            self.flag = 0
        else:
            self.flag = re.S

        self._match = pattern
        self._action = substitute + ":" + flag

    @property
    def match(self):
        return self._match
    
    @property
    def action(self):
        return self._action
    
    def apply(self, line : str ) -> str:
        """_summary_
        Args:
            line (str): original string.
        Returns:
            str: processed string.
        """
        if self.substitute_type == SubstituteType.Reserve:
            match = re.findall(self.pattern, line, flags=self.flag)
            for m in match: 
                temp_re = re.sub(self.pattern, r'__TEMPLATE__', line, flags=self.flag, count=1)
                line = temp_re.replace('__TEMPLATE__', m)
                # Problem: text bf change to all
            return line

        elif self.substitute_type == SubstituteType.Empty:
            return re.sub(self.pattern, "", line, flags=self.flag)
        else:
            return re.sub(self.pattern, self.substitute_content, line, flags=self.flag)


def parse_criterion_v1(line) -> Criteria:
    items = line.split("->")
    pattern = r'{}'.format(items[0].strip())
    targets = items[1].strip().split(":")
    if len(targets) > 1:
        return Criteria(pattern, r'{}'.format(targets[0]), r'{}'.format(targets[1]))
    else:
        return Criteria(pattern, r'{}'.format(targets[0]), "")

def parse_criterion_v2(match, action) -> Criteria:
    pattern = match
    targets = action.strip().split(":")
    if len(targets) > 1:
        return Criteria(pattern, r'{}'.format(targets[0]), r'{}'.format(targets[1]))
    else:
        return Criteria(pattern, r'{}'.format(targets[0]), "")
