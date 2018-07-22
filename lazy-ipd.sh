#!/bin/sh
echo Script ini masih eksperimental, selalu cek ulang kuesioner anda di Integra anda !!!!

echo Masukkan NRP :

read nrp

echo Masukkan Password, jangan khawatir, saya nggak nyimpen password anda:

read password

echo Ok, coba saya isikan

python auto-ipd/v2-auto-ipd.py $nrp $password