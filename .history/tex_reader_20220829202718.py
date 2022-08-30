import os

class TexReader:
    """_summary_
    A module used to read tex file and return valid sentence.
    """
    
    def __init__(self, file_path):   
        self._lines = None
        with open(file_path, encoding='utf-8') as file_obj:
            self._lines = file_obj.read()
        if self._lines is None:
            raise RuntimeError("Invalid tex file path.")
        
    def nextline(self) -> str:
        """_summary_
            Read next valid line.
        Returns:
            str: a line of string.
        """
        