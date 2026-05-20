from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class KeywordValidatorInput(BaseModel):
    keywords: str = Field(..., description="Comma separated App Store keywords")


class KeywordLengthValidator(BaseTool):
    name: str = "Keyword Length Validator"
    description: str = (
        "Validates App Store keyword field length. "
        "Checks whether total character count is under 100."
    )

    args_schema: Type[BaseModel] = KeywordValidatorInput

    def _run(self, keywords: str) -> str:
        count = len(keywords)

        if count <= 100:
            return (
                f"Validation Result: PASS\n"
                f"Character Count: {count}/100"
            )

        return (
            f"Validation Result: FAIL\n"
            f"Character Count: {count}/100\n"
            f"Reduce keyword length."
        )