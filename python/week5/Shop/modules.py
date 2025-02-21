import json

database = []

def read_database(file_name):
    global database
    try:
        with open(file_name, 'r') as file:
            database = json.load(file)
    except (FileNotFoundError):
        database = []

def write_database(file_name):
    try:
        with open(file_name, 'w') as file:
            json.dump(database, file)
    except Exception as e:
        print(f"Error writing database: {e}")

def create_record(record):
    global database
    database.append(record)

def read_record(index):
    try:
        return database[index]
    except IndexError:
        return None

def update_record(index, new_record):
    try:
        database[index] = new_record
    except IndexError:
        print("Record not found.")

def delete_record(index):
    try:
        del database[index]
    except IndexError:
        print("Record not found.")
