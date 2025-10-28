from typing import TypedDict, Optional, Annotated, List
from langchain_core.messages import AnyMessage


# class  MessagesStruct()
class MainState(TypedDict):
    # id for data saving
    cluster: str
    cluster_url: str

    # list of all sys and human message with code inside
    pair_tp_list: Optional[List[List[AnyMessage]]]

    # controle of pair_tp_list for each batch analysis
    total_requests_from_df: int
    current_offset: int

    sliced_for_batch: List[AnyMessage]
    
    gpt_response: Annotated[List[List[str]], lambda current, new: current + [new]]
