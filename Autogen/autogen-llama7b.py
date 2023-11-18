import autogen
import openai


config_list = [
    {
        "api_type": "open_ai",
        "api_base":"http://localhost:1234/v1",
        "api_key": "NULL"
    }
]



llm_config ={
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name="assistant",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    system_message="you are coding specialist in python ",
    llm_config= llm_config
)

user_proxy = autogen.UserProxyAgent(
    name ="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web","use_docker":False},
    llm_config=llm_config,
    system_message="""if the task you are answering is completed and you are satisfied from the answer reply "TERMINATE" and don't make any new answer.
    Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
give me the time and the date from greece using python 
"""

user_proxy.initiate_chat(
    assistant,
    message=task,
    clear_history=None
)
