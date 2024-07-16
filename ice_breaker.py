# import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain!")
    # print(os.environ["OPENAI_API_KEY"])

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(model="llama3")
    
    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/qiangcui0618/",
        mock=True
    )
    
    res = chain.invoke(input={"information": linkedin_data})
    
    print(res)