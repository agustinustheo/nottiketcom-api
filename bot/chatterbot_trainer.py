
import os

import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

'''
This is an example showing how to create an export file from
an existing chat bot that can then be used to train other bots.
'''

chatbot = ChatBot('WowoBot')

# First, lets train our bot with some data
trainer = ChatterBotCorpusTrainer(chatbot)
directory = 'conversation_dataset'

# trainer.train("./greetings.corpus.json", "./conversations.yaml", "./concert2020-10-10T14-02-28.272419.yml")

for filename in os.listdir(directory):
    # exclude greetings and conversation dataset
    if filename.endswith(".yml") and filename != "conversations.yaml": 
        trainer.train(directory + "/" + filename)

# Now we can export the data to a file
trainer.export_for_training('./my_export.json')

# Get a response to the input text 
response = chatbot.get_response('kakak bisa apa?')

print(response)
