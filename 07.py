# Serialization
from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address: Address

address_dict={'city':'gurgaon','state':'haryana','pin':'122001'}
address1=Address(**address_dict)
patient_dict={'name':'shree','gender':'male','age':35,'address':address1}
patient1= Patient(**patient_dict)
print(patient1)
temp=patient1.model_dump()
print(temp)
print(type(temp))
temp1=patient1.model_dump_json(include=['name','gender'])
temp2=patient1.model_dump(exclude={'address':['state']})
