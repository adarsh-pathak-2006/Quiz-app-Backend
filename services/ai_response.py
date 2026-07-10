from services.build_prompt import build_prompt
from services.ai_integration import return_response

def response(topic, difficulty, no_of_ques):
    prompt=build_prompt(topic=topic, difficulty=difficulty, no_of_ques=no_of_ques)
    final_output=return_response(prompt)

    return final_output