import requests
import json
from bs4 import BeautifulSoup

def json_parser(filename):
    return json.load(open(filename))

def login_integra(s):
    hal_login = 'https://integra.its.ac.id'

    s.post(hal_login, data=json_parser('credential.json'))

    res = s.get('http://integra.its.ac.id/dashboard.php')

    if res:
        print "Login sukses!"

def get_sim_gate(res):
    html = BeautifulSoup(res.text, "lxml")

    for tags in html.find_all('meta'):
        content = tags.get('content')

    return content.split('=', 1)[1]

def get_sim_akademik_cookie(s):
    res = s.get('https://integra.its.ac.id/dashboard.php?sim=AKADX__-__')
    
    sim_akademik_gate = get_sim_gate(res)

    s.get(sim_akademik_gate)

    res = s.get('http://akademik3.its.ac.id/home.php')

    if res:
        print 'Cookie SIM Akademik didapatkan'

def get_members_page(matkul, kelas):
    return "http://akademik3.its.ac.id/lv_peserta.php?mkJur=51100&mkID="+matkul+"&mkSem=2&mkThn=2017&mkKelas="+kelas

def go_stalk(s, nrp):
    classes = ['A','B','C','D','E','F',]

    subjects = json_parser('matkul.json')

    for matkul in subjects:
        for kelas in classes:
            list_peserta_page = get_members_page(matkul, kelas)
            result = s.get(list_peserta_page)

            if nrp in result.text:
                print subjects[matkul] + " " + kelas

s = requests.Session()
login_integra(s)
get_sim_akademik_cookie(s)

nrp = raw_input("Masukkan NRP yang akan di stalk (gunakan format baru): ")

go_stalk(s, nrp)