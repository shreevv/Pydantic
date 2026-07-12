#Creating a Base Model
from pydantic import BaseModel

class Patient(BaseModel):
    name :str
    age: int
# Storing Info in Dictionary
patient_info={'name':'Shree','age':20}
#Unpacking the dictionary
patient1=Patient(**patient_info)
print(patient1)