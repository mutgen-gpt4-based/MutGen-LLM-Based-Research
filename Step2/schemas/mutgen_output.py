from pydantic import Field, BaseModel

class MutationGenerated(BaseModel):
    reasoning: str = Field(description="A step-by-step explanation of how you analyzed the fixed_code and applied each rule from the modifications_list to generate the final mutant version.")
    mutant: str = Field(description="The final, complete buggy code snippet. This should contain only the code, with NO extra text or markdown.")