
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import glob
import os






PATH = "C:/Users/ncornejo/Desktop/Bot Python/IEDriverServer.exe"
driver = webdriver.Ie(PATH)
driver.get("http://ebs.andes.vtr.cl:8000/OA_HTML/AppsLocalLogin.jsp")

time.sleep(5)

search = driver.find_element_by_name("usernameField").send_keys("25-09-2022")

#INICIO DE SESION
pyautogui.moveTo(293,540,1)
pyautogui.leftClick()
pyautogui.write("gguerreroc")

pyautogui.moveTo(897,352,1)
pyautogui.leftClick()
pyautogui.write("Alan_1532")

pyautogui.moveTo(883,351,1)
pyautogui.leftClick()


pyautogui.moveTo(293,540,1)

pyautogui.leftClick()

pyautogui.moveTo(226,751,1)

pyautogui.leftClick()

pyautogui.moveTo(270,793,1)

pyautogui.leftClick()

pyautogui.moveTo(616,698,4)

pyautogui.leftClick()

pyautogui.moveTo(1156,702,4)

pyautogui.leftClick()

#SELECCION DE DIRECTA G40
pyautogui.moveTo(713,642,4)
pyautogui.leftClick()
##CIERRE DE POP UPS INICIALES
pyautogui.moveTo(909,140,2)
pyautogui.leftClick()
##CIERRE DE POP UPS INICIALES 2 
pyautogui.moveTo(1026,143,2)
pyautogui.leftClick()


pyautogui.moveTo(318,476,2)
pyautogui.doubleClick() 

#Seleccion Sub menu
pyautogui.moveTo(436,521,2)
pyautogui.doubleClick() 

#Seleccion Find 
pyautogui.moveTo(797,880,2)
pyautogui.doubleClick() 

#OPCION FILE
pyautogui.moveTo(33,69,12)
pyautogui.doubleClick() 

#OPCION EXPORT
pyautogui.moveTo(33,257,2)
pyautogui.doubleClick() 


#APROBAR + 100 REGISTROS 
pyautogui.moveTo(1127,610,3)
pyautogui.doubleClick() 

time.sleep(65)


#APROBAR LA DESCARGA
pyautogui.moveTo(940,374,3)
pyautogui.doubleClick() 

#CERRAR VENTANA DE DESCARGA
pyautogui.moveTo(1068,139,6)
pyautogui.doubleClick() 



## MOVER DESCARGA A CARPETA COMPARTIDA
list_of_files = glob.glob('C:/Users/ncornejo/Downloads/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

os.rename(latest_file,'C:\\Users\\ncornejo\\Dropbox\\SSIS_PY\\ORACLE\\G40.tsv')

#CAMBIAR RESPONSABLE
pyautogui.moveTo(263,110,5)
pyautogui.doubleClick() 






