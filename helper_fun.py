import re

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""

if __name__=="__main__":
    s = "projects/mira-chatbot-food-deliver-rf9k/agent/sessions/04975834-cc4c-3296-ee72-e71abf10b1e6/contexts/ongoing-order"
    print(extract_session_id(s))