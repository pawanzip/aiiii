from pymongo import MongoClient


Client = MongoClient("localhost:27017")


db = Client.Employee


def retrieve():
    try:
        employeeID = input("Enter employee ID to retrieve: ")
        query = {"id": employeeID}
        
    
        result = db.employee.find_one(query)
        
        if result:
            print("Employee Details:")
            print(f"ID: {result['id']}")
            print(f"Name: {result['name']}")
            print(f"Age: {result['age']}")
            print(f"Country: {result['country']}")
        else:
            print("No employee found with the given ID.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")


retrieve()
