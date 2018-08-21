import json
import requests
from bs4 import BeautifulSoup


def json_parser(payload_name):
    return json.load(open(payload_name + '.json'))


def login_integra(s):
    hal_login = 'https://integra.its.ac.id'

    s.post(hal_login, data=json_parser('credential'))

    res = s.get('http://integra.its.ac.id/dashboard.php')

    if res:
        print "Login sukses!"


def get_sim_akademik_cookie(s):
    res = s.get('https://integra.its.ac.id/dashboard.php?sim=AKADX__-__')

    sim_akademik_gate = get_sim_gate(res)

    s.get(sim_akademik_gate)

    res = s.get('http://akademik3.its.ac.id/home.php')

    if res:
        print 'Cookie SIM Akademik didapatkan'


def get_sim_beasiswa_cookie(s):
    res = s.get('https://integra.its.ac.id//dashboard.php?sim=BEA__10__')

    sim_akademik_gate = get_sim_gate(res)

    s.get(sim_akademik_gate)

    res = s.get('http://beasiswa.its.ac.id/data/home.php')

    if res:
        print 'Cookie SIM Beasiswa didapatkan'


def get_sim_skem_cookie(s):
    res = s.get('https://integra.its.ac.id/dashboard.php?sim=SKEM__10__')

    sim_akademik_gate = get_sim_gate(res)

    s.get(sim_akademik_gate)

    res = s.get('http://akademik3.its.ac.id/skem/petunjukskemmhs.php')

    if res:
        print 'Cookie SIM SKEM didapatkan'


def get_sim_gate(res):
    html = BeautifulSoup(res.text, "lxml")

    for tags in html.find_all('meta'):
        content = tags.get('content')

    return content.split('=', 1)[1]
