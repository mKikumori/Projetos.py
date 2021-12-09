
class Notes:
    
    def __int__(self, name, date, notes):
        self.__name = name
        self.__date = date
        self.notes = notes
        
    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()

    def write_notes(self, text):
        self.notes += text
        
    def read_notes(self):
        print(self.notes)

    def delete_notes(self, text):
        self.notes -= text
