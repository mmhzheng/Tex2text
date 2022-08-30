import re

class Criteria : 
    """
    Abstraction for user-defined criterias.
    """
    def __init__(self, expr : str):
        self.pattern = ""
        self.substitute = ""
        self.flag = ""
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
        


def parse_criterions(lines: list(str)) -> list(Criteria):
    for line in lines:
        items = line.split("->")