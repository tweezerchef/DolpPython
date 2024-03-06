from openai import OpenAI

client = OpenAI(api_key="<INSERTOPENAIKEY")


class StoryAgent:
    def __init__(self, role, description, character_role="user"):
        self.role = role
        self.description = description
        self.character_role = character_role

    def generate_text(self, prompt, max_tokens=150):
        system_prompt = {"role": "system", "content": prompt}
        character_action = {"role": self.character_role, "content": self.description}

        complete_prompt = [system_prompt, character_action]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=complete_prompt,
            max_tokens=max_tokens,
            temperature=0.7,
        )

        return response.choices[0].message.content


def main(prompt):

    hero_agent = StoryAgent("Hero", "a hero with superpowers", "user")
    sidekick_agent = StoryAgent(
        "Sidekick", "a sidekick that often causes trouble", "user"
    )
    narrator_agent = StoryAgent(
        "Narrator", "narrates the story, providing context and background", "assistant"
    )
    evil_agent = StoryAgent("Villain", "a villain with dark powers", "user")
    random_agent = StoryAgent("Random", "a wildcard character", "user")

    agents = [hero_agent, sidekick_agent, narrator_agent, evil_agent, random_agent]

    story = ""
    for agent in agents:
        story_part = agent.generate_text(prompt, max_tokens=100)
        story += f"{agent.role}: {story_part.strip()}\n\n"

    print(story)


if __name__ == "__main__":
    prompt = input("Enter your story prompt: ")
    main(prompt)
