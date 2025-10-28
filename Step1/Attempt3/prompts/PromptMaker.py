import random
from langchain_core.messages import SystemMessage, HumanMessage
from prompts.agent_prompt import AGENT_SYS_PROMPT, HUMAN_PROMPT
import pandas as pd
import numpy as np

class PromptBuilder:
    def __init__(self):
        self.system_message = [SystemMessage(AGENT_SYS_PROMPT)]


    def building_human_prompt(self, CodeFix: str, BuggyCode: str, Gumtree: str):
        normalize_gumtree_list = Gumtree.replace("'", "")[1:-1].split(", ")
        all_nodes = []
        for mutop in normalize_gumtree_list:
            node = mutop.split(" ")[1]
            all_nodes.append(node)
        np_subjects = np.array(all_nodes)

        # all labels from the current TP
        labels, _ = np.unique(np_subjects, return_counts=True)

        # all possible nodes
        df = pd.read_excel("prompts/mut_op_java_file.xlsx")
        all_ops, _ = np.unique(df["java_node"], return_counts=True)

        ops_for_gpt = []
        length_labels = len(labels)
        length_list_operators = len(all_ops)
        
        if length_labels > 1:
            adds_new_ops = (length_labels-1)*2
            total_options_num = 4 + adds_new_ops
        else:
            total_options_num = 4 # 4 options + the correct node

        if total_options_num <= 12: # limit for multi ops. MAX 5 nodes as labels
            while True:
                rand_index = random.randint(0,(length_list_operators-1))
                if not all_ops[rand_index] in labels:
                    ops_for_gpt.append(all_ops[rand_index])
                    if len(ops_for_gpt) == total_options_num:
                        break
            ops_for_gpt += labels.tolist()
            final_length_ops = len(ops_for_gpt)
            random.shuffle(ops_for_gpt)
        else:
            ops_for_gpt = all_ops.tolist()
            final_length_ops = 18

        final_prompt = HUMAN_PROMPT.format(
            CodeFix=CodeFix,
            BuggyCode=BuggyCode,
            final_length_ops=final_length_ops,
            ops_for_gpt=ops_for_gpt
        )
        return self.system_message + [HumanMessage(final_prompt)]
    


