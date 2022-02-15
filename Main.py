from timeit import repeat
from wsgiref import headers
import requests
import json
from itertools import chain, permutations
import itertools
import enchant
import random
import os
from os.path import exists



d=enchant.Dict("en_US")
op=set()


def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


english_words = load_words()

autho = ""
channelid = ""

if (os.path.exists('auth.json')):
    f = open("auth.json","r")
    yo2 = json.load(f)
    autho = yo2['Auth']
    channelid = yo2['Channel']

else:
    f = open("auth.json","x")
    autho = input("Enter Discord Authorization (you can change this inside the TXT if you get it wrong.): \n")
    channelid = input("CHANNEL ID GOES HERE \n")
    ayto =  "{" + '"Auth": "{}" , "Channel" : "{}"'.format(autho, channelid) +"}"

    f.write(ayto)
    f.close()
    
urly = "https://discord.com/api/v9/channels/{}/messages".format(channelid)

header = {
    'authorization': autho
}

r = requests.get(urly, headers=header)

bruh = 'abcdefghijklmnopqrstuvwxyaz'
correctWords = []
 
        

def sendMsg(message):
    data = {"content": message}
    requests.post(urly, data=data, headers=header)





def Nigario(yeahy):
    for yeah in yeahy:
        author = yeah["author"]['username']
        content = yeah["content"]
        if author == "Mudae":
            if "Type the longest word containing:" in content:
                treelet = content[65:68]
                print("Word prefix is "+treelet)
                correctWords = []
                for x in english_words:
                    if treelet.casefold() in x:
                        if not "-" in x:
                            correctWords += [x]
                
                maxedlengthword = max(correctWords, key=len)
                print("MAX LENGTH WORD IS "+maxedlengthword)
                sendMsg(maxedlengthword)
    
                return
            else:
                print("Game has not started (Start a red tea!)")


                        


                    
                  

                        
                        
                




jsonvalue = json.loads(r.text)
Nigario(jsonvalue)

def fakeNigario():
    for value in jsonvalue:
        print(f'  {value["author"]["username"]} :{value["content"]}  ', '\n')




