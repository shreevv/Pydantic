#Annotated and Field Validator
from typing import Annotated, Optional, List, Dict
from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator

class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the patient",
            description="The name of the patient within 50 characters",
            examples=["Nitish", "Shree"],
        ),
    ]

    email: Annotated[
        EmailStr,
        Field(
            title="Email of patient",
            description="Email of the patient. Those of affiliated companies would get discounts.",
            examples=["abcxyz@gmail.com"],
        ),
    ]

    linkedin_url: Annotated[
        AnyUrl,
        Field(
            title="LinkedIn URL of patient",
            description="Should be a valid LinkedIn URL",
            examples=["https://www.linkedin.com/in/shreedutt"],
        ),
    ]

    age: Annotated[
        int,
        Field(
            title="Age of the patient",
            description="Age should be greater than zero",
            examples=[21],
        ),
    ]

    weight: Annotated[
        float,
        Field(
            gt=0,
            title="Weight of the patient",
            description="Weight should be greater than zero (in kg)",
            examples=[72.5],
        ),
    ]

    married: Annotated[
        bool,
        Field(
            title="Marital Status",
            description="Whether the patient is married",
            examples=[False],
        ),
    ]

    allergies: Annotated[
        Optional[List[str]],
        Field(
            title="Allergies",
            description="List of allergies, if any",
            examples=[["Peanuts", "Dust"]],
        ),
    ] = None

    contact_details: Annotated[
        Dict[str, str],
        Field(
            title="Contact Details",
            description="Dictionary containing contact information",
            examples=[
                {
                    "phone": "+91-9876543210",
                    "emergency_contact": "+91-9123456789",
                }
            ],
        ),
    ]

@field_validator('email')
@classmethod
def email_validator(cls,value):
    valid_domains=['hdfc.com','icici.com']
    domain_name=value.split('@'[-1])
    if domain_name not in valid_domains:
        raise ValueError('Not a valid domain')
    return value

@field_validator('name')
@classmethod
def transform_name(cls,value):
    return value.upper()

@field_validator('age')
@classmethod
def validate_age(cls,value):
    if 0<value<100:
        return value
    else:
        raise ValueError("Age should be in between 0 and 100")