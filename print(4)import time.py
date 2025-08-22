print(4)import time

from google import genai


client = genai.Client()


prompt = """A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.

A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'"""


# Start the generation job

operation = client.models.generate_videos(

    model="veo-3.0-generate-preview",

    prompt=prompt,

)


# Poll for the result

while not operation.done:

    print("Waiting for video generation to complete...")

    time.sleep(10)

    operation = client.operations.get(operation)