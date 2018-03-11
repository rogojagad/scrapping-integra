import requests
import json
from bs4 import BeautifulSoup

def credential():
    return json.load(open('credential.json'))

def login_integra(s):
    hal_login = 'https://integra.its.ac.id'

    s.post(hal_login, data=credential())

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

def get_ipk_rank(s):
    get_sim_akademik_cookie(s)

    for page_num in range(1,41):
        scrap_ipk_rank(s, page_num)

def scrap_ipk_rank(s, page_num):
    ipk_rank_page = 'http://akademik3.its.ac.id/list_ipkrank.php'

    payload ={
        'page':page_num
    }

    res = s.post(ipk_rank_page, data=payload)

    data_ranking = BeautifulSoup(res.text, 'html.parser')
    
    tabel_mhs = data_ranking.find('table', class_='GridStyle')

    rows = tabel_mhs.find_all('tr')

    for row in rows:
        if row.get('height'):
            continue
        else:
            columns_in_a_row = row.find_all('td')
            row_data = ""
            for column in columns_in_a_row:
                row_data += column.get_text()
            print row_data
            
def isi_skem(s):
    get_sim_skem_cookie(s)

    form = 'http://akademik3.its.ac.id/skem/entry_realisasi.php'

    nrp = credential()['userid']

    payload = {
        "semester" : "21142",
        "kodekegiatan" : "1;35000",
        "partisipasi" : "Testing",
        "tglmulai" : "05-03-2018",
        "tglselesai" : "05-03-2018",
        "act" : "simpan",
        "submit" : "submit",
        "nrp" : nrp
    }

    res = s.post(form, data=payload)

    if res.status_code == 200:
        print "SKEM berhasil diisi"

s = requests.Session()
login_integra(s)
# get_sim_beasiswa_cookie(s)
# daftar_beasiswa(s)
get_ipk_rank(s)
# isi_skem(s)
