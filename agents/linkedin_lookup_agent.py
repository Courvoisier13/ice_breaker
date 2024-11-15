import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub

from tools.tools import get_profile_url_tavily


# new*
def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini",
    )
    template = """
    given the full name {name_of_person}, I want you to get the link to their LinkedIn profile page. Your answer should
    contain only url"""
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google for linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need to get the LinkedIn profile page url",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_url = result["output"]
    return linkedin_url


if __name__ == "__main__":
    lookup(name="eden marco udemy")
