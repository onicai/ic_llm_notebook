import pprint
import time
from .ic_py_canister import get_canister

# get ic-py based LLM Canister instance
canister_name = ""
candid_path = "ic-llm.did"
network = "ic"
canister_id = "w36hm-eqaaa-aaaal-qr76a-cai"
LLM = get_canister(canister_name, candid_path, network, canister_id)

# Helper function to chat with DFINITY's LLM Canister
def call_llm_canister(
    model: str = "llama3.1:8b",
    system_prompt: str = "",
    user_prompt: str = "",
    messages: list = [],  # conversation so far, will be updated with the response
    debug_verbose: int = 0,
) -> list:

    # Prepare the chat_message and append it to the messages list
    if system_prompt != "":
        role = {"system": None}
        chat_message = {"role": role, "content": system_prompt}
        messages.append(chat_message)
    if user_prompt != "":
        role = {"user": None}
        chat_message = {"role": role, "content": user_prompt}
        messages.append(chat_message)

    # Prepare the chat_request to send to the LLM Canister
    chat_request = {
        "model": model,
        "messages": messages,
    }

    if debug_verbose > 0:
        print("---------------------------------------------------------")
        print("DEBUG: This is the chat_request send to the LLM Canister:")
        pprint.pprint(chat_request)

    # Handle exceptions in case the Ingress is busy and it throws this message:
    # Ingress message ... timed out waiting to start executing.
    max_retries = 5
    retry_delay = 2  # seconds
    for attempt in range(1, max_retries + 1):
        try:
            response = LLM.v0_chat(chat_request)
            if debug_verbose > 0:
                print("---------------------------------------------------------")
                print("DEBUG: This is the raw response returned by the LLM Canister:")
                pprint.pprint(response)
            break  # Exit the loop if the request is successful
        except Exception as e:
            print(f"Attempt {attempt} failed with error: {e}")
            if attempt == max_retries:
                print("Max retries reached. Failing.")
                # Re-raise the exception if max retries are reached,
                # which will exit the program
                raise

            print(f"Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)  # Wait before retrying

    # The LLM Canister does not yet support the "assistant" role, but let's assume it will come soon
    # So we can build up a conversation
    role = {"assistant": None}
    chat_message = {"role": role, "content": response[0]}
    messages.append(chat_message)

    return messages