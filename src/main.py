import threading
import os.path
from random import randint
from time import sleep


def inject():
    #Lee el fichero de nombres /files/People.txt
    file = open(os.path.dirname(__file__) + "/../files/People.txt", "r+")
    people = file.readlines()
    while 1:
        while len(people) == 0 :
            print("Waiting for more people...")
            sleep(3)
        index = randint(0, (len(people)-1))
        print(index)
        sleep(randint(0, 5))
        newPerson = people[index]
        print(newPerson + "Entered")
        people.remove(people[index])
        ###########################################
        # Insertar newPerson en la base de datos  #
        ###########################################

    file.close()
    print("Finished")



if __name__ == "__main__":
    #Para hacer la inyeción y extracción de personas desde el mismo script, lanzo las funciones en hilos diferentes
    th_Inject = threading.Thread(target=inject())
    th_Inject.start()
