from oac import OpenAIClient
from elevenlabs import clone, generate, play
from elevenlabs import set_api_key

import yaml


class SaySomething(object):
    def __init__(self):
        with open("config/config.yaml", "r") as f:
            config = yaml.safe_load(f)
        open_ai_key = config["openai"]
        eleven_key = config["elevenlabs"]["api_key"]
        self.oac = OpenAIClient(
            api_key=open_ai_key,
            model="gpt-3.5-turbo",
        )
        set_api_key(eleven_key)
        self.voice = voice = clone(
            name="Creepy",
            description="Scary voice. Very creepy and disturbing. Sometimes becomes very deep and demonic.",
            files=["demon.mp3"],
        )

    def write(self, image_tags):
        prompt = f"You are a scary pumpkin during Halloween. There is a person in front of you that you are trying to scare. I took a picture of this person and I am going to describe it to you using tags. Delimited by  {image_tags}. Write a creepy sentence about this person using details about the person and their surroundings."
        response = self.oac.chat_completion(prompt)

    def talk(self, image_tags):
        # response = self.write(image_tags)
        audio = generate(
            text="Hello! Are you scared yet? I'm behind you... Hahahahaha. Look at the mirror... I'm right here... Right behind you... Can you see me?",
            voice=self.voice,
            model="eleven_multilingual_v2",
        )

        play(audio, use_ffmpeg=False)


def main():
    ss = SaySomething()
    ss.talk(image_tags="")


if __name__ == "__main__":
    main()
