from utils import *
import time

userNrp = ""

def matkulList():
    listOfMatkul = [
#        'IF4954|_|2018|51100|0',
    ]

    return listOfMatkul

def setHeaders():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
    }

    return headers

def isiFrs(s):
    target = 'http://akademik3.its.ac.id/list_frs.php'

    headers = setHeaders()

    listOfMatkul = matkulList()

    count = 0

    while True:
        
        for matkul in listOfMatkul:
            payload = {
                'nrp':userNrp,
                'act':'ambil',
                'key':matkul,
            }

            s.post(target, data=payload, headers=headers)

        count += 1

        print "Percobaan ke " + str(count)

	time.sleep(5)

if __name__ == "__main__":
    s = requests.Session()

    userNrp = json_parser('credential')['userid']

    login_integra(s)

    get_sim_akademik_cookie(s)

    isiFrs(s)
