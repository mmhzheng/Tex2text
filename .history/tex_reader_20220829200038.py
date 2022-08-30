import os

class TexReader:
    """_summary_
    A module used to read tex file and return valid sentence.
    """
    
    def __init__(self, file_name):   
        with open(file_path, encoding='utf-8') as file_obj:
            for line in file_obj:
                print(line)