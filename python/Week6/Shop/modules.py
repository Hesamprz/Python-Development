import json

class Database:
    def __init__(self, file_name):
        self.file_name = file_name
        self.database = []
        self.read_database()

    def read_database(self):
        try:
            with open(self.file_name, 'r') as file:
                self.database = json.load(file)
        except FileNotFoundError:
            self.database = []

    def write_database(self):
        try:
            with open(self.file_name, 'w') as file:
                json.dump(self.database, file)
        except Exception as e:
            print(f"Error writing database: {e}")

    def create_record(self, record):
        self.database.append(record)

    def read_record(self, index):
        try:
            return self.database[index]
        except IndexError:
            return None

    def update_record(self, index, new_record):
        try:
            self.database[index] = new_record
        except IndexError:
            print("Record not found.")

    def delete_record(self, index):
        try:
            del self.database[index]
        except IndexError:
            print("Record not found.")
