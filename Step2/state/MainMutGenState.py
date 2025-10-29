from typing import TypedDict, Optional, Annotated, List, Any
from langchain_core.messages import AnyMessage
import pandas as pd
import operator
from pydantic import BaseModel

class TpByAgent(BaseModel):
    fixed_code: str
    buggy_code: str
    line_in_dataset: int
    mutant_version: str
    gumtree_baseline: str


class MainState(TypedDict):
    cluster: str
    cluster_url: str
    current_offset: int
    dataframe: pd.DataFrame
    sliced_for_batch: pd.DataFrame 
    
    gpt_response: Annotated[List[TpByAgent], operator.add]
    tp_request: pd.Series
    final_result_df: pd.DataFrame
    total_requests_from_df: int



    