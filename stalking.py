from utils import *


def get_members_page(matkul, kelas):
    base_url = "http://akademik3.its.ac.id/lv_peserta.php?mkJur=51100&mkID="
    semester = "&mkSem=2&mkThn=2017&mkKelas="

    return base_url + matkul + semester + kelas


def go_stalk(s, nrp):
    classes = ['A', 'B', 'C', 'D', 'E', 'F', ]

    subjects = json_parser('matkul')

    for matkul in subjects:
        for kelas in classes:
            list_peserta_page = get_members_page(matkul, kelas)
            result = s.get(list_peserta_page)

            if nrp in result.text:
                print subjects[matkul] + " " + kelas


nrp = raw_input("Masukkan NRP yang akan di stalk (gunakan format baru): ")

s = requests.Session()

login_integra(s)

get_sim_akademik_cookie(s)

go_stalk(s, nrp)
