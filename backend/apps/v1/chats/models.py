import json

class Chats():
    def __init__(self):
        pass

    def get_json_data(file_name): # chats.json or users.json
        with open(file_name, "r") as read_file:
            data = json.load(read_file)
        
        return data
    
    def save_chats(data):
        with open("chats.json", "w") as write_file:
            json.dump(data, write_file)

  

        
    