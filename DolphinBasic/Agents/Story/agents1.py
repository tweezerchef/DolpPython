import langchain
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

# Initialize OpenAI LLM


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Define Agents
hero_agent = create_agent(
    llm=llm,
    agent_type="hero",
    verbose=True,
    memory=langchain.Memory(),
)
sidekick_agent = create_agent(
    llm=llm,
    agent_type="sidekick",
    verbose=True,
    memory=langchain.Memory(),
)
narrator_agent = create_agent(
    llm=llm,
    agent_type="narrator",
    verbose=True,
    memory=langchain.Memory(),
)
villain_agent = create_agent(
    llm=llm,
    agent_type="villain",
    verbose=True,
    memory=langchain.Memory(),
)
random_agent = create_agent(
    llm=llm,
    agent_type="random",
    verbose=True,
    memory=langchain.Memory(),
)

# Chain Agents Together
chain = langchain.Chain(
    agents=[
        hero_agent,
        sidekick_agent,
        narrator_agent,
        villain_agent,
        random_agent,
    ]
)

# Get Prompt from User
prompt = input("Enter a simple prompt: ")

# Generate Story
result = chain.call({"prompt": prompt})

# Print Generated Story
print(result["output"])
