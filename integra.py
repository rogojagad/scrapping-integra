import re
from utils import *


def get_ipk_rank(s):
    get_sim_akademik_cookie(s)

    for page_num in range(1, 41):
        scrap_ipk_rank(s, page_num)


def cleanup(data):
    to_string = str(data)
    return re.sub('\s+', ' ', to_string)


def scrap_ipk_rank(s, page_num):
    ipk_rank_page = 'http://akademik3.its.ac.id/list_ipkrank.php'

    payload = {
        'page': page_num
        # ,'thnAngkatan':'2015'
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
                row_data += cleanup(column.get_text())
            print row_data


def isi_skem(s):
    get_sim_skem_cookie(s)

    form = 'http://akademik3.its.ac.id/skem/entry_realisasi.php'

    nrp = json_parser('credential')['userid']

    payload = {
        "semester": "21142",
        "kodekegiatan": "1;35000",
        "partisipasi": "Testing",
        "tglmulai": "05-03-2018",
        "tglselesai": "05-03-2018",
        "act": "simpan",
        "submit": "submit",
        "nrp": nrp
    }

    res = s.post(form, data=payload)

    if res.status_code == 200:
        print "SKEM berhasil diisi"


if __name__ = "__main__":
    s = requests.Session()
    login_integra(s)
    # get_sim_beasiswa_cookie(s)
    # daftar_beasiswa(s)
    get_ipk_rank(s)
    # isi_skem(s)
