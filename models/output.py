# Pydantic

from pydantic import BaseModel, Field


class Output(BaseModel):
    """AI Chat bot response for fixing the code"""
    problem: str = Field(description="Where is the problem in the code")
    code: str = Field(description="Code after fixing the problem")
    explanation: str = Field(description="Explanation of the code")
