import os
from typing import Tuple
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from agents.linkedin_lookup_agent import run as linkedin_lookup_agent
from parsers.output import summary_parser, Summary
from third_parties.linkedin import scrape_linkedin_profile_summary

load_dotenv()

mock = lambda: True if os.getenv("MOCK") == "True" else False


def ice_break_with(name: str) -> Tuple[Summary, str]:
    summary = """
        Given the information {information} about a person, please provide me with:
        1. A short summary
        2. A list of two facts about this person
        {format_instructions}, 
        {signature}
        """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions(),
            "signature": "Add thanks you message at the end of the summary."
        },
    )

    llm = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo")
    chain = summary_prompt_template | llm | summary_parser
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile_summary(linkedin_username, mock=mock())
    res: Summary = chain.invoke(input={"information": linkedin_data})
    return res, linkedin_data.get("profile_pic_url", "")


if __name__ == "__main__":
    print(ice_break_with("Dror Russo"))
