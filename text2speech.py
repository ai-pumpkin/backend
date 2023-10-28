from oac import OpenAIClient
from elevenlabs import clone, generate, play, 
from elevenlabs import set_api_key

import yaml


class SaySomething(object):
    def __init__(self):
        with open("config/config.yaml", "r") as f:
            config = yaml.safe_load(f)
        open_ai_key = config["openai"]

        eleven_key = config["elevenlabs"]
        set_api_key(eleven_key)
        self.voice = clone(
            name="Creepy",
            description="Scary voice. Very creepy and disturbing. Sometimes becomes very deep and demonic.",
            files=["demon.mp3"],
        )
        self.oac = OpenAIClient(
            api_key=open_ai_key,
            model="gpt-3.5-turbo",
        )

    def write(self, image_tags):
        prompt = f"You are pretending to be a scary demon in a haunted house game during Halloween. There is a person in front of you that you are trying to scare. I took a picture of this person and I am going to describe it to you using tags. Delimited by --- below you will find the tags of the image. Say a very creepy one liner sentence that shows you can see the person and their surroundings using the image tags below. The sentence should be simple, few words, but one that makes you feel like someone is watching you. It should start by saying that you can see the person. You shouldn't use all the available tags. Only the ones that are relevant to write one creepy sentence, like in a horror movie. \n Example: [image tags: 'woman', 'glasses', 'door'] ; Sentence: I can see you... Remove your glasses... So you can see me... Go open the door... behind you... I'm right behind you. I... seee... youuu... \n ---- {image_tags}"
        response = self.oac.chat_completion(prompt)
        return response

    def talk(self, image_tags):
        response = self.write(image_tags)
        audio = generate(
            text=response,
            voice=self.voice,
            model="eleven_multilingual_v2",
        )

        play(audio, use_ffmpeg=False)


def main():
    ss = SaySomething()
    response = ss.write(image_tags="girl | glasses | ceiling | cables | balloon | hair")
    print(response)


if __name__ == "__main__":
    main()
