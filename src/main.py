import threading
import os.path
from random import randint
from time import sleep

#Lee el fichero de nombres /files/People.txt
file = open(os.path.dirname(__file__) + "/../files/People.txt", "r+")
people = file.readlines()
file.close()
#Mutex para People
lock = threading.Lock()


def inject():
    while 1:
        while len(people) == 0 :
            print("Waiting for more people...")
            sleep(3)
        lock.acquire()
        index = randint(0, (len(people)-1))
        print(index)
        sleep(randint(0, 5))
        personIN = people[index]
        people.remove(people[index])
        lock.release()
        print(personIN + "Entered")
        ###########################################
        # Insertar personIN en la base de datos   #
        ###########################################


def extract():

###########################################
#   Extraer Persona de la base de datos   #
###########################################
    lock.acquire()
    #people.append(personOUT)
    lock.release()



if __name__ == "__main__":
    #Para hacer la inyeción y extracción de personas desde el mismo script, lanzo las funciones en hilos diferentes
    th_Inject = threading.Thread(target=inject())
    th_Extract = threading.Thread(target=extract())
    th_Inject.start()
    th_Extract.start()
