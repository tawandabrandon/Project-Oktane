from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import random
import pyttsx
import sys
from time import sleep

bot = ChatBot(
    'Oktane',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation'	
        ,
    {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.5
    },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'What is your name?',
            'output_text': 'Oktane'
        },
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        }
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    database='./database.sqlite3'
)
repList = ['but you just asked me that','i told you that already','the answer is still the same you know','are you okay?']
messages = list()
annoyance = 1
peopleImet = list()
response = ""
message = ""
inTraining = False
learnt = ["Now I know how to respond to that","I've learnt!","you never stop learning","and they say computers know everything right? haha"]
speaker = pyttsx.init()

rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate-30)
speaker.setProperty('voice', 'english')

class thing(object):
    def __init__(self, name):
        self.name = name;
        self.descriptions = list()

class Person(object):
    
    def __init__(self, name,nickname):
        self.name = name
        self.nickname = nickname
        self.things = list()
    
def typeOut(message):
    for word in message:
        sleep(0.1)
        sys.stdout.write(word)
        sys.stdout.flush()
    pass

def greet():
    print "Hi! I'm Oktane"
    name = raw_input("What's your name? ")
    if name.lower() in peopleImet:
        print "Hey man!"
    else:
        print "So nice to meet you %s" % (name)

def speak(message):
    speaker.say(message)
    speaker.runAndWait()

    pass
def train(message):
    Yes = ['yes','yea','yup','yeah','ehe','hongu','always','sure']
    No = ['no','nope','nada','never','ayewa','ayehwa','not']
    print "I'm sorry, I don't understand what you mean by %s" % (message)
    response = raw_input("how should I respond? ")
    accepted = False
    while not accepted:
        print ("So if someone says '%s' I should respond '%s'") % (message,response)
        answer = raw_input('right? ')
        if answer.lower() in Yes:
            print 'Okei!'
            accepted = True
            pass
        elif answer.lower() in No:
            response = raw_input('What should I say then? ')
            pass
        else:
            print "Now you're just confusing me :("

    bot.set_trainer(ListTrainer)
    bot.train([
        message,
        response
    ])
    print random.choice(learnt)
    chat()

    pass
def rep(message):
    if message in repList:
        return True
    else:
        return False
    pass
def chat():
    messeges = ['']
    while True:
        try:
            repList.insert(0,raw_input('me: '))
            message = repList[0]
            #if rep(message) and (annoyance > 3):
            #    print random.choice(repList)
            #    pass
            #elif rep(message):
            #    print "I told you that already"
            #    pass
            if message == "you don't respond that way":
                train(repList[1])
            response = str(bot.get_response(message))
            if response == "I'm sorry, I do not understand.":
                train(message)
            else:
                sys.stdout.write("Oktane: ")
                typeOut(response)
                print ""

            if len(repList) > 10:
                repList.pop()
                pass

        except(KeyboardInterrupt, EOFError, SystemExit):
            break

greet()
chat()