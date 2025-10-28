from typing import TypedDict, Optional, Annotated, List, Any
from langchain_core.messages import AnyMessage
import pandas as pd
import operator
from pydantic import BaseModel

class TpByAgent(BaseModel):
    fixed_code: str
    buggy_code: str
    gumtree_baseline: str
    line_in_dataset: int
    gpt_attempt1: List[str]


class MainState(TypedDict):
    cluster: str
    cluster_url: str
    dataframe: pd.DataFrame
    gpt_response: Annotated[List[TpByAgent], operator.add]
    sliced_for_batch: pd.DataFrame 
    current_offset: int
    tp_request: pd.Series
    final_result_df: pd.DataFrame
    total_requests_from_df: int



    