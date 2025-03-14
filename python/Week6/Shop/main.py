from modules import *

db = Database('database.json')

db.create_record({'name': 'Ali', 'age': 25})
db.write_database()

record = db.read_record(0)
print(record)

db.update_record(0, {'name': 'Ali Reza', 'age': 26})
db.write_database()

db.delete_record(0)
db.write_database()
