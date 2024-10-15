from pymongo import MongoClient
Client = MongoClient("localhost:27017")
db = Client.Employee

def delete():
    try:
        employeeID = input("Enter the employee ID to delete: ")
        result = db.employee.delete_one({"id": employeeID})
        if result.deleted_count > 0:
            print("Data deleted successfully")
        else:
            print("No data found with the given employee ID")
    except Exception as e:
        print("An error occurred:", str(e))

delete()
