# import os
from typing import Tuple
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_community.chat_models import ChatOllama
# from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import summary_parser, Summary

def ice_break_with(name: str) -> Tuple[Summary, str]:
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url, mock=False)

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    \n{format_instruction}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instruction": summary_parser.get_format_instructions()
        }
    )
    
    llm = ChatOllama(model="llama3")
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    
    chain = summary_prompt_template | llm | summary_parser
    
    res: Summary = chain.invoke(input={"information": linkedin_data})
    
    return res, linkedin_data.get("profile_pic_url")

if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter")
    ice_break_with(name="Qiang Cui Linkedin Poppulo")