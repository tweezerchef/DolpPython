import os
import langchain
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

# Set your OpenAI API key in the environment variables
os.environ["OPENAI_API_KEY"] = "<YOUR_OPENAI_API_KEY>"

# The rest of your code follows


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
    # Include the other agent_type conditions here as in your original code


def main():
    # Instantiate the OpenAI class with the model name.
    # Make sure the OPENAI_API_KEY environment variable is correctly set before this.
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
