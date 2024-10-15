from pymongo import MongoClient
Client=MongoClient("localhost:27017")
db=Client.Employee
def insert():
    try:
        employeeID=input("Enter employee id")
        employeeName=input("Enter employee Name")
        employeeAge=input("Enter employee Age")
        employeeCountry=input("Enter employee Country")
        db.employee.insert_one({
            "id":employeeID,
            "name":employeeName,
            "age":employeeAge,
            "country":employeeCountry})
        print("Data inserted successfully")

    except Exception:
        print(str(e))
insert()
