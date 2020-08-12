from random import randint
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    while True:
        # it takes microphone input from user and returns string output
         r = sr.Recognizer()
         with sr.Microphone() as source:
             print("Listening...")
             sr.pause_threshold = 1
             audio = r.listen(source)

         try:
             print("Recognizing...")
             query = r.recognize_google(audio)
             print("Player Name: {}".format(query)) 
             query = r.recognize_google(audio)  
         except:
             print("Say that again please...")
             return str("None")
         return str(query)
game_running = True
def calculate_monster_attack():
    return randint(monster['attack_min'],monster['attack_max'])
def game_ends(winner_name):
    print(f'{winner_name} won the game')
    speak(f'{winner_name} won the game')
while game_running==True :  # this loop is for whole game print
    new_round=True    # this is for new round
    player={'name':'Siddhant','attack': 10,'heal': 20,'health': 100}  #player info
    monster={'name': 'VirusD','attack_min': 10,'attack_max': 20, 'health': 100}     # villain info
    print('---' * 7) 
    speak("enter player name")
    print('enter player name')
    player_name = player['name']=takeCommand()      
    speak(f'{player_name} is in the game')
    print('---' * 7)
    print(player['name'] + 'has' + str(player['health']) + 'health')
    speak(player['name'] + 'has' + str(player['health']) + 'health')
    print(monster['name'] + 'has' + str(monster['health']) + 'health')
    speak(monster['name'] + 'has' + str(monster['health']) + 'health')
    while new_round == True :  # ye game end krne ke liye hai 
       player_won=False   # starting conditions
       monster_won=False
       print('---' * 7)
       print('please speak what you want to do')
       speak("please speak what you want to do")
       print('1) Attack')
       print('2) Heal')
       print('3) Exit Game')
       player_choice=takeCommand()
       if player_choice=='attack':  # attack
           speak("Attacking")
           monster['health']=monster['health']-player['attack']
           if monster['health']<=0 :
               player_won=True 
           else :
               player['health']=player['health']-calculate_monster_attack()
               if player['health']<=0 :
                   monster_won=True
       elif player_choice=='heal':       #heal
           speak(f'{player_name} is healing ')
           player['health']=player['health']+player['heal']
           player['health']=player['health']- calculate_monster_attack()
           if player['health']<=0 :
               monster_won=True
       elif player_choice=='exit':       #exit
           speak("Exiting the game")
           new_round = False
           game_running = False
       else :
           print('invalid option')
           speak("invalid choice")
       if player_won==False and monster_won==False :
           print(player['name'] +  'has' + str(player['health']) + '  left')
           speak(player['name'] +  'has' + str(player['health']) + '  left')
           print(monster['name'] +  'has' + str(monster['health']) + '  left')
           speak(monster['name'] +  'has' + str(monster['health']) + '  left')
       elif player_won :
           game_ends(player['name'])
           new_round = False
       elif monster_won :
           game_ends(monster['name'])
           new_round = False