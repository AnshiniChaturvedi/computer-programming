1. Nested Dictionary Access and Manipulation
Q: Given a dictionary:
employee = {"name": "Ayushi", "details": {"age": 25, "department": "IT"}}
Update the department to "HR".

A:
employee["details"]["department"] = "HR"
print(employee)  
