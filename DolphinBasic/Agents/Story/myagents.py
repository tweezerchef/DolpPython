import os
from langchain.llms import OpenAI
from langchain.agents import TextAgent


class StoryAgent(TextAgent):
    def __init__(self, role, description, openai_model):
        super().__init__()
        self.role = role
        self.description = description
        self.openai_model = openai_model

    def generate_text(self, prompt):
        response = self.openai_model.complete(
            prompt=prompt + " " + self.description,
            model="gpt-3.5-turbo-0125",
            max_tokens=150,
        )
        return response.choices[0].text.strip()


def main(prompt):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai_model = OpenAI(api_key=openai_api_key)

    hero_agent = StoryAgent("Hero Agent", "a hero with superpowers", openai_model)
    sidekick_agent = StoryAgent(
        "Annoying Sidekick Agent", "a sidekick that often causes trouble", openai_model
    )
    narrator_agent = StoryAgent(
        "Narrator Agent",
        "narrates the story, providing context and background",
        openai_model,
    )
    evil_agent = StoryAgent("Evil Agent", "a villain with dark powers", openai_model)
    random_agent = StoryAgent("Random Agent", "a wildcard character", openai_model)

    agents = [hero_agent, sidekick_agent, narrator_agent, evil_agent, random_agent]

    story = ""
    for agent in agents:
        story_part = agent.generate_text(prompt)
        story += story_part + "\n\n"

    print(story)


if __name__ == "__main__":
    prompt = input("Enter your story prompt: ")
    main(prompt)
