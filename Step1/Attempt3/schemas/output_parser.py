from pydantic import Field, BaseModel
from typing import List

class OutputStructure(BaseModel):
    mut_op_list: List[str] = Field(description="List of necessary modifications made to the java AST nodes")