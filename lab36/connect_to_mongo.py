# mongodb://Iva:1234@127.0.0.1:27017


# mongosh "mongodb+srv://cluster0.qprcu.mongodb.net/" --apiVersion 1 --username PythonCourse

# mongodb+srv://PythonCourse:<password>@cluster0.qprcu.mongodb.net/



from pymongo import MongoClient
from pprint import PrettyPrinter

printer = PrettyPrinter()


client = MongoClient('mongodb://Iva:1234@127.0.0.1:27017')
dbs = client.list_database_names()
print(dbs)

db = client.python_course
collections = db.list_collection_names()
print(collections)

documents = list(db.todos.find())
print(documents)
printer.pprint(documents)



