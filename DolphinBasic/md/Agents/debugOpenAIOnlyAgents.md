### Introduction

I am a high school student interested in computer science, AI, and programming.  I don't have any formal training, but I have built a few small web development projects using standard Typescript/Javascript with standard libraries like Next.js and React.

I am interested in learning more about AI and how to use existing models in my programs. Most people recommended me to start with Python as it seems to be the language of choice for AI.  I've read the very basics of Python but have created very little actual code.

### Task

While researching AI, I started reading about "AI agents" that can help generate more unique and often more precise output from LLMs. I am interested in learning more about how to build these agents and how to use them to generate stories. What I wanted to build is a series of agents that work together to create a story based on a simple prompt. I have been told I can use Python and the Open AI API  to accomplish this.

### Code I Created

To build the program that would use agents to generate a story, I tried a few different approaches, using different libraries in an attempt to help me create the agents and generate the story. However I figured if I can just use the OpenAI library to do this, it would be much easier. Here is the code I created to try to accomplish this task:

```Python

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


class StoryAgent:
    def __init__(self, role, description):
        self.role = role
        self.description = description

    def generate_text(self, prompt, max_tokens=150):
        complete_prompt = f"{prompt} {self.description}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a highly intelligent AI."},
                {"role": "user", "content": complete_prompt},
            ],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"]


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
```

When I run the code, it correctly asks for a prompt, but then there are a bunch of errors in the console, which I have copied below:

``` Python Console
$ /usr/bin/python3 /media/tom/Linux/Python/DolphinBasic/Agents/Story/myagent3.py
Enter your story prompt:
Traceback (most recent call last):
  File "/media/tom/Linux/Python/DolphinBasic/Agents/Story/myagent3.py", line 50, in <module>
    main(prompt)
  File "/media/tom/Linux/Python/DolphinBasic/Agents/Story/myagent3.py", line 42, in main
    story_part = agent.generate_text(prompt)
  File "/media/tom/Linux/Python/DolphinBasic/Agents/Story/myagent3.py", line 15, in generate_text
    response = openai.ChatCompletion.create(
  File "/home/tom/.local/lib/python3.10/site-packages/openai/lib/_old_api.py", line 39, in __call__
    raise APIRemovedInV1(symbol=self._symbol)
openai.lib._old_api.APIRemovedInV1:

You tried to access openai.ChatCompletion, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.

You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface.

Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`

A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742
```

### Issue

I ran the `openai migrate` command as suggested, but it didn't fix the issue. I do not wish to pin my installation to the old version, as I would like to use the latest version of the library. I am not sure what to do next. Can you help me fix this code so that it works as expected? I want to use the latest version of the OpenAI library and the `gpt-3.5-turbo` model to generate the story based on the prompt but have an API key for any of the models so I'm not tied down to that one necessarily, if you think another model would be better, please use it.

### Solution

Please debug the code and fix the issue so it works as expected. You can use any model you think is best for the task. Please provide a detailed explanation of the changes you made and why you made them. Also, please provide a brief explanation of the code you wrote. Please respond with the updated code first and the explanations after.
