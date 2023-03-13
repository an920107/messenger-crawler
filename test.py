import os

from modules.chatgpt import ChatGPT

gpt = ChatGPT(os.path.abspath("data/gptconfig.json"))

print(gpt.post("我覺得好孤單"))
