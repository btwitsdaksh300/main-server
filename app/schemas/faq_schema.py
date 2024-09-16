from pydantic import BaseModel, Field
from typing import Optional

class FAQSchema(BaseModel):
    id: Optional[int] = None  
    question: str = Field(..., min_length=5, max_length=255, description="The FAQ question")
    answer: str = Field(..., min_length=5, max_length=1000, description="The FAQ answer")
    fruit: Optional[str] = Field(None, description="The fruit this FAQ is associated with")

    class Config:
        schema_extra = {
            "example": {
                "question": "What is the nutritional value of an apple?",
                "answer": "An apple contains Vitamin C, dietary fiber, and antioxidants.",
                "fruit": "Apple"
            }
        }
