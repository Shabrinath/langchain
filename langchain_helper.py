from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_technologies_for_role(job_role):
    # Chain 1: Generate a list of technologies to learn for a specific engineering role
    prompt_template_technologies = PromptTemplate(
        input_variables=['job_role'],
        template="I want to become a {job_role} engineer. Please suggest technologies I need to learn to become a {job_role} engineer. Provide only a one word and 1 liner description list of technologies. format skill: <1 liner description>, skill2: <description>. provide comma separeted and dont have any commas in between description"
    )

    tech_chain = LLMChain(llm=llm, prompt=prompt_template_technologies, output_key="skills_list")

    response = tech_chain({'job_role': job_role})

    return response

if __name__ == "__main__":
    print(generate_technologies_for_role("DevOps"))

