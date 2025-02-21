from modules import *

if __name__ == "__main__":
    read_database("database.json")

    create_record({"name": "apple", "price": 20})
    print(read_record(0))
    update_record(0, {"name": "banana", "price": 35})
    print(read_record(0))
    delete_record(0)
    print(read_record(0))

    write_database("database.json")
