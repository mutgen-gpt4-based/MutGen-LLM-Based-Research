from pydantic import Field, BaseModel
from typing import List
from typing import  Literal

class MutationOperator(BaseModel):
    modification: Literal["Delete", "Insert", "Update", "Move"]
    ast_node: str = Field(description="Which spoon Java node type you are modifying.")
    node_description: str = Field(description="Define what is the Java node assigned in **ast_node**. What this node means?")


class ReasoningAgentSchemaOutput(BaseModel):
    mut_op_list: List[MutationOperator] = Field(description="List of necessary modifications made to the java AST nodes")