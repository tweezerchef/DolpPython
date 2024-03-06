from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import os

# Make sure your OpenAI API key is correctly set in youment variables


class StoryAgent:
    def __init__(self, role, description):
        self.role = role
        self.description = description

    def generate_text(self, prompt, max_tokens=150):
        complete_prompt = f"{prompt} {self.description}"
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a highly intelligent AI."},
            {"role": "user", "content": complete_prompt},
        ],
        max_tokens=max_tokens,
        temperature=0.7)
        return response.choices[0].message.content


def main(prompt):
    hero_agent = StoryAgent("Hero Agent", "a hero with superpowers")
    sidekick_agent = StoryAgent(
        "Annoying Sidekick Agent", "a sidekick that often causes trouble"
    )
    narrator_agent = StoryAgent(
        "Narrator Agent", "narrates the story, providing context and background"
    )
    evil_agent = StoryAgent("Evil Agent", "a villain with dark powers")
    random_agent = StoryAgent("Random Agent", "a wildcard character")

    agents = [hero_agent, sidekick_agent, narrator_agent, evil_agent, random_agent]

    story = ""
    for agent in agents:
        story_part = agent.generate_text(prompt)
        story += story_part.strip() + "\n\n"

    print(story)


if __name__ == "__main__":
    prompt = input("Enter your story prompt: ")
    main(prompt)
