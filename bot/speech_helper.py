from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def respond(chat):
    chatbot = ChatBot('WowoBot')

    # First, lets train our bot with some data
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Get a response to the input text 'I would like to book a flight.'
    response = chatbot.get_response(chat)
    if response.confidence <= 0.4:
        return "Maaf, Wowo belum mengerti maksudmu, bolehkah diulang lagi? :("
    else:
        return str(response)