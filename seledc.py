
import random
from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://randomtodolistgenerator.herokuapp.com/library')

list_Task = driver.find_elements_by_xpath('//div[@class="taskCard card"]')
list_title = []
list_text = []
for tasks in list_Task:
	titleTask =  tasks.find_element_by_xpath('.//div[@class="flexbox task-title"]/div').text
	list_title.append(titleTask)
	textTask =  tasks.find_element_by_xpath('.//p[@class="card-text"]').text
	list_text.append(textTask)
print(list_title)
#driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://todoist.com/es') 
menu = driver.find_elements_by_xpath('//ul[@class="_3XsmI"]')

for men in menu:
	iniciar=men.find_element_by_xpath('.//li/a[@class="_2q_cf"]')
sleep(random.uniform(4.0, 8.0))
iniciar.click()

formulario = driver.find_elements(By.XPATH, '//form[@id="login_form"]')
for form in formulario:
	try:
		inputCorreo = form.find_element(By.XPATH, './/input[@class="input input_email"]')
		inputPssw = form.find_element(By.XPATH, '//input[@id="password"]')
		submit = form.find_element(By.XPATH, '//button[@class="submit_btn ist_button ist_button_red sel_login"]')
	except:
		break

correo = 'taskselenium20@gmail.com'
psww = 'taskselen20'

inputCorreo.send_keys(correo)
inputPssw.send_keys(psww)
submit.click()

sleep(random.uniform(3.0, 6.0))
addTask = driver.find_element(By.XPATH, '//button[@class="plus_add_button"]')
addTask.click()

for lis in range(len(list_title[1:6])):
	try:
		sleep(random.uniform(1.0, 2.0))
		area = driver.find_element(By.XPATH, '//br[@data-text="true"]')
		area.send_keys(list_title[lis])
		sleep(random.uniform(1.0, 2.0))
		driver.find_element(By.XPATH, '//button[@class="ist_button ist_button_red"]').click()
		sleep(random.uniform(1.0, 2.0))
	except:
		break
	

cerrar = driver.find_element(By.XPATH, '//button[@class="cancel"]')
cerrar.click()

	





