import os
import langchain
import langchain_community
from langchain.agents import initialize_agent
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "<YOUR_OPENAI_API_KEY>"


def create_agent(agent_type, llm):
    if agent_type == "Hero":
        return initialize_agent(
            tools=[
                langchain.PromptTemplate(
                    template="You are a superhero with great powers.",
                    input_variables=["prompt"],
                )
            ],
            llm=llm,
            agent="hero",
        )
    elif agent_type == "Annoying Sidekick":
        return initialize_agent(
            tools=[
                langchain.PromptTemplate(
                    template="You are the hero's annoying sidekick who always gets in the way.",
                    input_variables=["prompt"],
                )
            ],
            llm=llm,
            agent="sidekick",
        )
    elif agent_type == "Narrator":
        return initialize_agent(
            tools=[
                langchain.PromptTemplate(
                    template="You are the narrator of the story.",
                    input_variables=["prompt"],
                )
            ],
            llm=llm,
            agent="narrator",
        )
    elif agent_type == "Evil":
        return initialize_agent(
            tools=[
                langchain.PromptTemplate(
                    template="You are a supervillain with great powers.",
                    input_variables=["prompt"],
                )
            ],
            llm=llm,
            agent="evil",
        )
    elif agent_type == "Random":
        return initialize_agent(
            tools=[
                langchain.PromptTemplate(
                    template="You are a random character that can be anything.",
                    input_variables=["prompt"],
                )
            ],
            llm=llm,
            agent="random",
        )


def main():
    llm = OpenAI(model_name="gpt-3.5-turbo-0125")
    agents = [
        create_agent("Hero", llm),
        create_agent("Annoying Sidekick", llm),
        create_agent("Narrator", llm),
        create_agent("Evil", llm),
        create_agent("Random", llm),
    ]
    chain = langchain.ConversationChain(llm=llm, agents=agents)

    prompt = input("Enter a story prompt: ")
    story = chain.run(prompt)

    print(story)


if __name__ == "__main__":
    main()
