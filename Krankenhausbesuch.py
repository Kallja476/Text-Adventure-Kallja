#Import in das System
import random
import os
import time
import sys

#Variablen
#BotX = "Player"
#Lebenspunkte_BotX = "Player"
Verrückter_Arzt = False
Hund = False
Rundenzähler = 0
Warteschlange = "<----Lädt---->"
Lebenspunkte_Verrückter_Arzt = 4.5
Hund = 3.5
Lebenspunkte_Player = 6
RED = "\033[31m"
BLAU = "\33[34m"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"
Möglichkeiten_in_Tasche = ["eine Pfeife","eine Feder", "nichts"]#oder weiteres

#Listen
Patient1 = ["Lennard",  "185"  , "braun","blau",       "Raum_NR:43"]
Patient2 = ["Markus",     "178", "schwarz","braun","Raum_NR:81"]
Patient3 = ["Nils",    "184"  ,  "rot", "grün",       "Raum_NR:12"]
Patient4 = ["Lennard", "185", "braun","blau","Raum_NR:31"]

BotX_Optionen = ["faust","tritt","tornadokick"]


data = {
    "Lennard":{ "Körpergröße": "185"  , "Haarfarbe": "braun","Augenfarbe":"blau","Raumnummer":    "43"     },
    "Markus":   { "Körpergröße": "178"  , "Haarfarbe": "schwarz","Augenfarbe":"dunkelbraun","Raumnummer":"81"},
    "Nils":  { "Körpergröße": "184"  , "Haarfarbe": "rot","Augenfarbe":"grün","Raumnummer":"12"           },
}


#Kampfoptionen für den Spieler
Spieler_faust = [
       ("effektiv",1.5),
       ("mäßig",1),
       ("mäßig",1),
       ("nicht effektiv",0.5)
       
]
Spieler_tritt = [
       ("Sehr effektiv",2),
       ("effektiv",1.5),
       ("mäßig",1),
       ("nicht effektiv",0.5),
       ("abgeruscht",0)
]
Spieler_tornadokick = [
       ("Knock-Out",4),
       ("Sehr schwer",1),
       ("mäßig",1),
       ("nicht effektiv",0.5),
       ("abgeruscht",0),
       ("daneben",0),
       ("daneben",0)
]


#Kampfoptionen für den aktuell kämpfenden Gegner
faust = [
       ("effektiv",1.5),
       ("mäßig",1),
       ("mäßig",1),
       ("nicht effektiv",0.5)
       
]
tritt = [
       ("Sehr effektiv",2),
       ("effektiv",1.5),
       ("mäßig",1),
       ("nicht effektiv",0.5),
       ("abgeruscht",0)
]
tornadokick = [
       ("Knock-Out",4),
       ("Sehr schwer",1),
       ("mäßig",1),
       ("nicht effektiv",0.5),
       ("abgeruscht",0),
       ("daneben",0),
       ("daneben",0)
]



#Definitionen 
def clear_screen():
    os.system("cls")

def langsam(Ausgabe):
    for c in Ausgabe:
        time.sleep(0.8)

def clean(text):
    for c in text:
        sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.000055)

def clean_schneller(text):
    for c in text:
        sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.0008)

def cleanschlange(Schnur):
    for c in Schnur:
        sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.65)

def cleanPause(Punkte):
    for c in Punkte:
        sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.65)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def Kampfsystem_ohne_Waffen():
    #mit Global sind die Variablen auch außerhalb der Definition nutzbar
    global Rundenzähler
    global Verrückter_Arzt
    global Lebenspunkte_Verrückter_Arzt
    global Lebenspunkte_Player
    global Lebenspunkte_BotX
    global BotX

    while Lebenspunkte_Player > 0 and Lebenspunkte_BotX > 0 and Rundenzähler != 7:

        Rundenzähler += 1
        print("\n",Rundenzähler,". Runde\n")
        KampfOhneWaffe2 = input("--->").lower()

        #Kampfbereich für den Spieler
        if KampfOhneWaffe2.lower() == "tritt":
            Random_Tritt = random.choice(Spieler_tritt)  #zufällig wird bei Auswahl "Tritt" die Trittstärke ermittelt
            treffer_name, schaden = Random_Tritt   #Treffer_name und schaden werden aus Random_Tritt extrahiert und gespeichert um anschließend definiert zu sein

            print(f"Dein Treffer war {treffer_name}!")
            print(f"Du verursachst {schaden} Schaden.")

            Lebenspunkte_BotX -= schaden  # Schaden abziehen
            if Lebenspunkte_BotX <= 0:
                print("Der Gegner ist jetzt besiegt")
                break
            print(f"Der Gegner hat noch {Lebenspunkte_BotX} HP übrig.")


        if KampfOhneWaffe2.lower() == "tornadokick":
            Random_Tornadokick = random.choice(Spieler_tornadokick) 
            treffer_name, schaden = Random_Tornadokick

            print(f"Dein Treffer war {treffer_name}!")
            print(f"Du verursachst {schaden} Schaden.")

            Lebenspunkte_BotX -= schaden  # Schaden abziehen
            if Lebenspunkte_BotX <= 0:
                    print("Der Gegner ist jetzt besiegt")
                    break
            elif Lebenspunkte_Player <= 0:
                print("Du bist jetzt leider besiegt.")
                break               
            print(f"Der Gegner hat noch {Lebenspunkte_BotX} HP übrig.")

        if KampfOhneWaffe2.lower() == "faust":
            Random_Faust = random.choice(Spieler_faust)  
            treffer_name, schaden = Random_Faust

            print(f"Dein Treffer war {treffer_name}!")
            print(f"Du verursachst {schaden} Schaden.")

            Lebenspunkte_BotX -= schaden  # Schaden abziehen
            if Lebenspunkte_BotX <= 0:
                    print("Der Gegner ist jetzt besiegt")
                    break               
            print(f"Der Gegner hat noch {Lebenspunkte_BotX} HP übrig.")


        #Kampfbereich für den Bot
        if BotX == True:
            BotX_Treffer = random.choice(BotX_Optionen)
            if BotX_Treffer == "faust":
                Random_Faust = random.choice(faust)  
                treffer_name, schaden = Random_Faust   

                print(f"\n\nDer Treffer von dem Gegner war {treffer_name} und die Art war",BotX_Treffer.upper(),"!")
                print(f"Du erhälst {schaden} Schaden.")           
                if Lebenspunkte_Player <= 0:
                    print("Du bist jetzt leider besiegt.")
                    break
                Lebenspunkte_Player -= schaden
                print(f"Du hast noch {Lebenspunkte_Player} HP übrig.")

            elif BotX_Treffer == "tornadokick":
                Random_Tornadokick = random.choice(tornadokick)  
                treffer_name, schaden = Random_Tornadokick   

                print(f"\n\nDer Treffer von dem Gegner war {treffer_name} und die Art war",BotX_Treffer.upper(),"!")
                print(f"Du erhälst {schaden} Schaden.")           
                if Lebenspunkte_Player <= 0:
                    print("Du bist jetzt leider besiegt.")
                    break
                Lebenspunkte_Player -= schaden
                print(f"Du hast noch {Lebenspunkte_Player} HP übrig.")


            elif BotX_Treffer == "tritt":
                Random_Tritt = random.choice(tritt)  
                treffer_name, schaden = Random_Tritt   

                print(f"\n\nDer Treffer von dem Gegner war {treffer_name} und die Art war",BotX_Treffer.upper(),"!")
                print(f"Du erhälst {schaden} Schaden.")           
                if Lebenspunkte_Player <= 0:
                    print("Du bist jetzt leider besiegt.")
                    break
                Lebenspunkte_Player -= schaden
                print(f"Du hast noch {Lebenspunkte_Player} HP übrig.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def Willkommen():
    Start="Willkommen in meinem Spiel. Hier wirst du eine Geschichte erleben, in der du auf deinen besten Freund Lennard triffst. \nAuf jenem Weg wirst du aber auch andere Figuren kennenlernen.\n\nAlso bist du bereit, dieses Abenteuer zu bestreiten??? Wenn dem so ist, so schreibe bitte 'Start'!"
    clean(Start)
    Startknopf = input("\n-->")
    while True:      #Iteration erst verlassen, wenn in irgendeiner Form "Start" verfasst wurde
        if Startknopf.lower() == "start":
            Warteschleife = "Sehr schön, viel Spaß und viel Erfolg!\n"
            clean(Warteschleife)
            break
        elif Startknopf.lower() != "start":
            Falsche_Eingabe=("Dies entsprach nicht der möglichen Eingabe, wenn du fortfahren möchtest, so schreibe bitte 'Start'.")
            clean(Falsche_Eingabe)
            Startknopf = input("\n-->")

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def Lennard_Suche():
    gefunden = False

    clean(Abfrage_Körpergröße)
    Antwort_Körpergröße=input().lower()
    clean(Abfrage_Haarfarbe)
    Antwort_Haarfarbe=input().lower()
    clean(Abfrage_Augenfarbe)
    Antwort_Augenfarbe = input().lower()

    while True:

        for name, info in data.items():#name greift auf dictionary name; info greift auf untergeordnete Kategorien von name zu;data.items greift auf alle Keys jener vorher genannten Kategorien
            if info["Haarfarbe"].lower() == Antwort_Haarfarbe and info["Augenfarbe"].lower() == Antwort_Augenfarbe and info["Körpergröße"] == Antwort_Körpergröße:  
                gefunden = True 
                break   #genutzt um aus der for Schleife auszubrechen

        if gefunden == True:    #genutzt um anschließend auch aus der while Schleife auszubrechen
            Lennard_gefunden = (""+BLAU+"Wir haben "+name+" gefunden und du kannst ihn auch besuchen. Seine Zimmernummer lautet "+(info["Raumnummer"])+(RESET)+".")
            clean(Lennard_gefunden)
            break
        else:
            Wiederholung = input(""+BLAU+"Lennard wurde hier nicht gefunden, möglicherweise habt ihr euch mit etwas vertan. Wollt Ihr es erneut ausprobieren?\nWenn dem so ist, so sage bitte 'Ja' andernfalls 'Nein'-->"+RESET+"")
            if Wiederholung.lower () == "ja":
                Antwort_Körpergröße = (''+BLAU+'Wie groß ist Lennard in CM gemessen?:'+RESET+'')
                Antwort_Haarfarbe =(''+BLAU+'Dann benötige ich die entsprechende Haarfarbe:'+RESET+'')
                Antwort_Augenfarbe = (''+BLAU+'Und zum Schluss die Augenfarbe des Patienten:'+RESET+'')
                clean(Antwort_Körpergröße)
                Antwort_Körpergröße = input().lower()
                clean(Antwort_Haarfarbe)
                Antwort_Haarfarbe = input().lower()
                clean(Antwort_Augenfarbe)
                Antwort_Augenfarbe = input().lower()
            elif Wiederholung.lower() == "nein":
                print(""+BLAU+"Dann wünsche ich Ihnen noch einen schönen Tag."+RESET+"")
                break
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------


def mehr_Listen():
    Weitere_Patienten = ('\n\nDu willst dich gerade auf dem Weg machen, da sagt die Krankenschwester mit einer verdächtigen Stimme:'+BLAU+'"\nIch habe hier eine Liste mit Leuten,\ndie Sie möglicherweise auch besuchen wollen. Wollen Sie sie sehen?"'+RESET+'(Ja/Nein)')
    clean(Weitere_Patienten)
    Antwort_auf_Liste=input()
    while True:
        if Antwort_auf_Liste.lower () == "ja":
            Antwort=(""+BLAU+"Gut, hier ist sie..\n"+RESET+"")
            clean(Antwort)
            print(Patient1)
            print(Patient2)
            print(Patient3)
            break

        elif Antwort_auf_Liste.lower() == "nein":
            Antwort2=(""+BLAU+"Dann wünsche ich Ihnen noch einen schönen Tag."+RESET+"")
            clean(Antwort2)
            break

        elif Antwort_auf_Liste.lower() != "ja" or Antwort_auf_Liste.lower() != "nein":
            Antwort_erneuern = (""+BLAU+"Leider entspricht deine Antwort nicht meinem Verständnis, antworten Sie bitte mit 'Ja', falls Sie sie sehen wollen, andernfalls mit 'Nein'."+RESET+"")
            clean(Antwort_erneuern)
            Antwort_auf_Liste=input()

    Krankenschwester_Abschluss=(BLAU+"Noch eine Sache, passen Sie auf sich auf.. die Phrenocomii ist kein Platz für Jeden."+RESET+"\n\n","Du weißt nicht genau, was du damit anfangen kannst, gehst aber dennoch weiter.")
    clean(Krankenschwester_Abschluss)
    Überbrückung =  clean(input("Drücke eine beliebige Taste, um fortzufahren:"))

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def Arzt_kämpft():
    global Lebenspunkte_BotX
    global Verrückter_Arzt
    global Lebenspunkte_Verrückter_Arzt
    global BotX

    #BotX ist der aktuelle Gegner 
    Verrückter_Arzt = True  #System aktiviert den gewählten Gegner
    BotX = Verrückter_Arzt  #Gewählter Gegner wird zum aktuellen Gegner und alle Kampfoptionen wirken 
    Lebenspunkte_BotX = Lebenspunkte_Verrückter_Arzt


#----------------------------------------------------------------------------------------------------------------------------------------------------------

def erster_Kampf():
    global Rundenzähler
    global Verrückter_Arzt
    global Lebenspunkte_Verrückter_Arzt
    global Lebenspunkte_Player
    global Lebenspunkte_BotX
    global BotX


    x = 0
    erste_Gefahr_Vorbereitung2 = ("Nichts…nur ein Doktor, der sich ruhig mit seinem Patienten unterhält. Die angespannte Stimmung, die dich noch vor wenigen Augenblicken erfasst hatte, löst sich sofort in Luft auf – völlig unbegründet. Dennoch schnappst du die Tür hastig zu, ein Hauch von Verlegenheit prickelt über deine Haut. Nach einer kurzen Atemübung bringst du zögerlich die Worte hervor:\n"+RED+"'Hat der Doktor gerade… mit einer Puppe gesprochen..?'" +RESET+"\n\nWeil dir dieser Gedanke komisch erscheint, gehst du unbeirrt weiter und tust so, als hättest du es nicht bemerkt. Kurz darauf triffst du im Flur einen Arzt und ergreifst sofort die Chance:\n"+RED+"'Entschuldigung, wo finde ich die Zimmernummer 43?'" +RESET+"\n\nDer Arzt starrt dich plötzlich an, seine Augen weiten sich, und er brüllt:\n"+BLAU+"'Du nervst mich schon wieder!'" +RESET+"\n\nEr stürmt auf dich zu, die Schritte hallen wie donnernde Trommeln im Flur.Bevor er dich erreicht, musst du dich entscheiden:\nGreifst du in die Hosentasche nach einem Gegenstand oder kämpfst du mit deinen Händen?\n"+RED+"''Ja' Hosentasche (Gegenstand nutzen)'\n''Nein' Hände (direkter Nahkampf)'" +RESET)
    clean(erste_Gefahr_Vorbereitung2)
    AuswahlWaffe = random.choice(Möglichkeiten_in_Tasche)

    erste_Gefahr_Reaktion = input("--->").lower()
    while True:
        if erste_Gefahr_Reaktion.lower() == "ja":
            clear_screen()
            Antwort_erste_Waffe = ("*Du hast ", AuswahlWaffe," erhalten!*")
            clean(Antwort_erste_Waffe)
            if AuswahlWaffe == "eine Pfeife":
                KampfPfeife = "Du greifst in deine Tasche und ziehst die KampfPfeife hervor — ein kleiner, abgenutzter Signalgeber, den du einst für Notfälle mitgenommen hast. Du pfeifst so laut du kannst, aber es kommt kein Ton heraus; die Pfeife bleibt stumm. Also wirfst du die Pfeife zur Seite und bereitest dich auf den Nahkampf vor.\nWillst du ihm einen 'Tritt (riskant)' verpassen oder eine 'Faust (mäßig)' landen?" 
                clean(KampfPfeife)

                #KampfnachPfeife = input()//////Forsetzung

            #elif AuswahlWaffe == "ein Messer"://////Forsetzung
            break  


        elif erste_Gefahr_Reaktion.lower() == "nein":
            KampfOhneWaffe1 = "Sieht so aus als wolltest du ihm richtig eine reinhauen. Dann sind folgende Dinge jetzt deine Optionen: 1. Tritt(effektiv) 2. Tornadokick(Schwer) 3.Faust ins Gesicht(mäßig)"
            clear_screen()
            clean(KampfOhneWaffe1)
            Arzt_kämpft()
            Kampfsystem_ohne_Waffen()
            break


        elif erste_Gefahr_Reaktion.lower() != "nein" or erste_Gefahr_Reaktion.lower() != "ja":
                clean("Bite gib eine gültige Eingabe ein.")
                erste_Gefahr_Reaktion = input("--->").lower()

#----------------------------------------------------------------------------------------------------------------------------------------------------------

def Karte_mitnehmen_Abfrage():
    global Lebenspunkte_Player
    Karte_Zustand = False
    while True:
        if Antwort_Karte_mitnehmen.lower() == "ja":
            Map_einstecken = "Kurz schaust du dich um, dann katapultierst du mit einem Faustschlag die Vitrine auseinander. Glas regnet auf den Boden."
            clean(Map_einstecken)
            print (""+RED+"\n\nDu hast einen Lebenspunkt verloren"+RESET+"")
            Lebenspunkte_Player -= 1
            print("\n Du hast noch ", Lebenspunkte_Player," übrig. Dein Leben ist kostbar und deine Handlungen beeinflussen es. Sei also vorsichtig.")
            Karte_Zustand = True
            break

        elif Antwort_Karte_mitnehmen.lower() == "nein":
            Map_liegen_lassen = "Du lässt die Karte liegen, merkst dir aber ganz genau, wo alles ist, das Hoffst du zumindest."
            break

#----------------------------------------------------------------------------------------------------------------------------------------------------------


#Story

Einleitung1 ="\n\nDu hast Lennard angerufen und ihn gefragt, wie es ihm geht.\nEr hat dir erzählt, dass er wieder mal zu viel getrunken hätte, weshalb er jetzt \nim Krankenhaus gelandet sei. Du sorgst dich um ihn und willst ihn dort auch besuchen. \n\n"
Einleitung1_2="\nAls du dort angekommen bist, ist dir aufgefallen, dass du ihn nicht gefragt hast, \nin welchem Zimmer er stationiert wurde. Das Gute ist, du weißt, dass er "+RED+"185cm" +RESET+" groß ist und "+RED+"braune"+RESET+" Haare, sowie "+RED+"blaue"+RESET+" Augen hat. \nAus diesem Grund suchst du eine Krankenschwester auf. \nDu siehst Eine, willst sie ansprechen..traust dich aber nicht..du denkst dir, \nwas mache ich eigentlich hier...aber dann nimmst du deinen ganzen Mut und gehst zu ihr hin...\n"
Pause= "--Auf dem Weg zu Lennard--\n"

Einleitung2=('\n'+BLAU+'"Guten Tag!'+RESET+'" sagt die Krankenschwester erfreut.')

#Begrüßung_im_Krankenhaus
Gruß = "\n\nWas antwortest du?\n\n-->"

Unterhaltung_mit_Krankenschwester1 = (''+BLAU+'"Hallo, wie kann ich Ihnen helfen?"'+RESET+' fragt sie freundlich und aufmerksam.\n\nDu senkst leicht den Blick, ein wenig verlegen, und antwortest,'+ORANGE+'"Ähm… ich wollte nur kurz nach meinem Freund Lennard sehen."'+RESET+'\n\n')
Unterhaltung_mit_Krankenschwester2=('\nSie sucht am Computer nach dem Namen und sagt:'+BLAU+'"Hmm, wir haben ganz viele Leute, die hier Lennard heißen. \nKönnen Sie ihn mir beschreiben, möglicherweise kann ich ihn anhand von seinen Merkmalen finden.'+RESET+'\n\n')
Unterhaltung_mit_Krankenschwester3=("Du denkst dir innerlich, dass es nur einen solchen Lennard gibt, den kannst du gar nicht mit Anderen auch nur vergleichen...\nAber du fragst zur Sicherheit dennoch nach:"+ORANGE+"'Was genau wollen Sie denn für Merkmale?'"+RESET+"")
Unterhaltung_mit_Krankenschwester4=('Die Krankenschwester sagt:'+BLAU+'"es gibt die Merkmale: Körpergröße in CM, dann die Haarfarbe und zum Schluss die Augenfarbe.\n\nAlso fangen wir an.'+RESET+'')

Abfrage_Körpergröße = (''+BLAU+'Wie groß ist denn Lennard in CM gemessen?:'+RESET+'')
Abfrage_Haarfarbe =(''+BLAU+'Dann benötige ich die entsprechende Haarfarbe:'+RESET+'')
Abfrage_Augenfarbe = (''+BLAU+'Und zum Schluss die Augenfarbe des Patienten:'+RESET+'')

erste_Gefahr_Vorbereitung1 = ("Du drehst dich nach links und gehst den Gang weiter. Die endlosen Reihen von Türen lassen dich kurz stocken – wie \nsollst du hier bloß Lennard finden? Dein Herz beginnt schneller zu schlagen. Du beschließt, an der nächsten Tür zu klopfen und nachzufragen, wo sich Lennards Raum befindet. Deine Hand zittert leicht, als du den Griff greifst – doch ein unheimlicher Schauer hält dich zurück…"+RED+'"Was meinte die Krankenschwester damit, dass dieser Ort nichts für Jeden ist..?"'+RESET+" Ein kalter Schauer läuft dir den Rücken hinunter, deine Augen kneifen sich zusammen. Mit zitternder Hand drückst du die Tür endlich auf und siehst......")
Überbrücker = ("  ")
#erste_Gefahr_vorbereitung2 in Erster_Kampf
erste_Gefahr_überlebt = "Du hast den Mann bewusstlos geschlagen. Die Luft steht — nicht ein Mensch ist zu hören. Das Krankenhaus wirkt wie ausgestorben; die Stille saugt dir den Atem aus der Brust.Wie kann es sein, dass bei diesem Tumult niemand herbeigeeilt ist? Ein kalter Schauer läuft dir über den Rücken. Etwas stimmt nicht. Sehr falsch.Du reisst dich zusammen. Jetzt gilt: Alles einpacken, was nützlich sein könnte. Zuerst der Stift — noch warm von der Hand des Arztes.Warum ist der Arzt ausgeflippt? Was hast du ihm angetan? Und Lennard — was hat er diesmal angestellt? Fragen, die keine Antworten liefern, aber dich vorwärts treiben.Du steckst den Stift ein und findest die nächste Krankenhauskarte. Auf ihr prangt ein großes X: Raumnummer X.Der Anblick löst einen kleinen, elektrischen Kick in dir aus — Motivation, nach vorn zu stürmen. \n\n Möchtest du sie mitnehmen? ('Ja'/'Nein')"

#----------------------------------------------------------------------------------------------------------------------------------------------------------

#Ausführbereich

clear_screen()
Willkommen()
clear_screen()
print("\n" * 15 + " " * 65, end="")
cleanschlange(Warteschlange)
clear_screen()
clean(Einleitung1)
cleanPause(Pause)
clean(Einleitung1_2)
clean(Einleitung2)
clean(Gruß)
Begrüßung = input()
clean(Unterhaltung_mit_Krankenschwester1)
clean(Unterhaltung_mit_Krankenschwester2)
clean(Unterhaltung_mit_Krankenschwester3)
clean(Unterhaltung_mit_Krankenschwester4)
print("\n")
Lennard_Suche()
mehr_Listen()
clear_screen()
clean(erste_Gefahr_Vorbereitung1)
langsam(Überbrücker)
clear_screen()
erster_Kampf()
clean (erste_Gefahr_überlebt)
clear_screen()
Antwort_Karte_mitnehmen = input("-->")
Karte_mitnehmen_Abfrage()
#Forsetzung




#----------------------------------------------------------------------------------------------------------------------------------------------------------
