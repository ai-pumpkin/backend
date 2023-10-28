from openaiclient import OpenAIClient
from elevenlabs import clone, generate, play
import yaml


class SaySomething(object):
    def __init__(self):
        with open("config/config.yaml", "r") as f:
            config = yaml.safe_load(f)
        open_ai_key = config["openai"]
        self.oac = OpenAIClient(
            api_key=open_ai_key,
            model="gpt-3.5-turbo",
        )

    def write(self, image_tags):
        prompt = f"You are a scary pumpkin during Halloween. There is a person in front of you that you are trying to scare. I took a picture of this person and I am going to describe it to you using tags. Delimited by  {image_tags}. Write a creepy sentence about this person using details about the person and their surroundings."
        response = self.oac.chat_completion(prompt)

    def talk(self, image_tags):
        # response = self.write(image_tags)
        voice = self.clone()
        audio = generate(
            text="Hello! Are you scared yet? I'm behind you... Look at the mirror, I'm right here, right behind you. Can you see me?",
            voice="voice",
            model="eleven_multilingual_v2",
        )

        play(audio, use_ffmpeg=False)

    def clone(self):
        voice = clone(
            name="Creepy girl",
            description="Creepy little girl talking and whispering and laughing. Scary voice. Very creepy and disturbing.",
            files=["girl_voice.mp3"],
        )


def main():
    ss = SaySomething()
    ss.talk(image_tags="")


if __name__ == "__main__":
    main()
