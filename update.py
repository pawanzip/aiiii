from pymongo import MongoClient
Client = MongoClient("localhost:27017")
db = Client.Employee

def update():
    try:
        employeeID = input("Enter the employee ID to update: ")
        
        # Prompt for new details
        employeeName = input("Enter the new employee name: ")
        employeeAge = input("Enter the new employee age: ")
        employeeCountry = input("Enter the new employee country: ")
        
        # Perform the update using update_one with the $set operator
        result = db.employee.update_one(
            {"id": employeeID},
            {
                "$set": {
                    "name": employeeName,
                    "age": employeeAge,
                    "country": employeeCountry
                }
            }
        )
        
        if result.modified_count > 0:
            print("Data updated successfully")
        else:
            print("No data found with the given employee ID, or no changes were made")
    
    except Exception as e:
        print("An error occurred:", str(e))

update()
