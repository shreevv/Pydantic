#Say if we want that every patient above 60 should have a valid contact details
#usage of model validator
from typing import Annotated, Optional, List, Dict
from pydantic import BaseModel, Field, EmailStr, AnyUrl,model_validator

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
@model_validator
def validate_emergency_contact(cls,model):
    if model.age>60 and 'emergency' not in model.contact_detais:
        raise ValueError('Patient older than 60 must have an emergency contact')
    return model