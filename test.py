import json

myWGappID = "9f2c3f9953a1084d88f94ca9ff78c06e"

class jsnBot:
    jsn_field = []

    def __init__(self, value):
        self.value = None
        self.validate(value)

    def validate(self, value):
        self.value = value

    def __contains__(self, item):
        return item in self.value

    def __str__(self):
        return f"{self.jsn_field}: {self.value}"
    

class playerInfo:
    #strukt
    def __init__(self,value):
        self.namePlayer = value
        

# main prog  