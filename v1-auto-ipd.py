from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from utils import json_parser
from random import randint
import time
import sys

visited = []

def login(driver):
    driver.get("https://integra.its.ac.id")

    nrp = json_parser('credential')['userid']
    password = json_parser('credential')['password']

    nrp_input = driver.find_element_by_id('userid')
    nrp_input.send_keys(nrp)

    password_input = driver.find_element_by_id('password')
    password_input.send_keys(password)

    login_form = driver.find_element_by_id('login_form')
    login_form.submit()

def go_to_siakad(driver):
    options = driver.find_elements_by_tag_name("option")

    for option in options:
        if option.get_attribute("value") == './dashboard.php?sim=AKADX__-__':
            option.click()
            break

    hyperlink = driver.find_element_by_partial_link_text("Kuesioner")
    hyperlink.click()

def get_first_unfilled(matkul_options):
    for option in matkul_options:
        if "SELESAI" not in option.text and option.text != '' and option.get_attribute('value') not in visited:
            visited.append(option.get_attribute('value'))
            return option

def refresh_matkul_dropdown(driver):
    matkul_dropdown = Select(driver.find_element_by_id('mk_kuesioner'))
    return matkul_dropdown.options

def go_to_matkul_kuesioner_page(driver, matkul):
    matkul.click()

    print "Kuesioner untuk : " + driver.find_element_by_tag_name('h3').text

    fill_matkul_kuesioner(driver)

    print "Kuesioner matkul sukses terisi !!!!"

    go_to_dosen_kuesioner_page(driver)

    print "Kuesioner dosen sukses terisi !!!!"

def fill_matkul_kuesioner(driver):
    for i in xrange(1, 11):
        score = randint(1,4)

        selected_option_id = "MK" + str(i) + str(score)

        print selected_option_id

        # driver.find_element_by_id(selected_option_id).click

        target_label = '//label[@for="' + selected_option_id + '"]' 

        driver.find_element_by_xpath(target_label).click()

    driver.find_element_by_id("txtKomentar").send_keys("mantap")

    driver.find_element_by_id("chkPermanent").click()

    submit_kuesioner_form(driver)

def submit_kuesioner_form(driver):
    elements = driver.find_elements_by_tag_name("input")

    for element in elements:
        if element.get_attribute("value") == "SIMPAN":
            element.click()
            break

def go_to_dosen_kuesioner_page(driver):
    hyperlink = driver.find_element_by_link_text("Isi Kuesioner")

    hyperlink.click()

    print driver.find_element_by_class_name("FilterBox").text

    fill_dosen_kuesioner(driver)

def fill_dosen_kuesioner(driver):
    for i in xrange(1, 11):
        score = randint(1,4)

        selected_option_id = "DO" + str(i) + str(score)

        print selected_option_id

        # driver.find_element_by_id(selected_option_id).click

        target_label = '//label[@for="' + selected_option_id + '"]' 

        driver.find_element_by_xpath(target_label).click()

    driver.find_element_by_id("txtKomentar").send_keys("mantap")

    driver.find_element_by_id("chkPermanent").click()

    driver.find_element_by_id("form2").submit()

    driver.find_element_by_partial_link_text("Kembali ke Kuesioner Mata Kuliah").click()
    

def count_matkul_target(driver):
    matkul_dropdown = Select(driver.find_element_by_id('mk_kuesioner'))
    return len(matkul_dropdown.options)

def list_matkul(driver):
    target_count  = count_matkul_target(driver)

    while True:
        matkul_list = refresh_matkul_dropdown(driver)
        
        matkul = get_first_unfilled(matkul_list)
        
        if matkul != None: 
            go_to_matkul_kuesioner_page(driver, matkul)

            # got_to_dosen_kuesioner_page(driver)

        if len(visited) == target_count - 1: break

if __name__ == "__main__":
    driver = webdriver.PhantomJS(executable_path='/usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
    # driver = webdriver.Firefox()
    login(driver)

    go_to_siakad(driver)

    list_matkul(driver)

    driver.close()