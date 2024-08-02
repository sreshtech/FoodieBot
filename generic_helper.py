import re


def get_str_from_food_dict(food_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string=match.group(1)
        return extracted_string

    return ""



if __name__=="__main__":
    print(get_str_from_food_dict({"samosa":2, "chhole":5}))
    # print(extract_session_id("projects/gabru-lwfx/agent/sessions/fab8817a-af5a-40ac-4c70-36f45d516e9c/contexts/ongoing-tracking"))