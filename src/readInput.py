import os

class ReadInput:
    def __init__(self, fileName) -> None:
        self.__filename = fileName
        self.__path = os.path.dirname(os.path.abspath(__file__))
    
    def read(self) -> list:
        path = os.path.join(self.__path, "input", self.__filename)
        print(path)
        try:
            with open(path, "r") as grafoFile:
                lines = grafoFile.read().splitlines()
                return lines
        except FileNotFoundError:
            print("file not found!")


            
    

