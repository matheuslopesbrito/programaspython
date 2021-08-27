# Terça
import pyautogui as ptg
import time as tm
import pyperclip as pcp
import datetime
import calendar
from tkinter import *
from tkinter import messagebox

bglive = ""
culto = ""

def cultodeensino():
    global culto
    culto="Culto de Ensino"
    global bglive
    bglive = "ensino1"
    return janela.destroy()

def cultodelibertacao():
    global culto
    culto="Culto de Libertação"
    global bglive
    bglive = "libertação1"
    return janela.destroy()

def ebd():
    global culto
    culto="Escola Bíblica Dominical"
    global bglive
    bglive = "ebd1"
    return janela.destroy()

def cultodafamilia():
    global culto
    culto="Culto da Família"
    global bglive
    bglive = "familia1"
    return janela.destroy()

def outroculto():
    global culto
    if cultoalternativo.get() == "":
        messagebox.showinfo(janela, title="ERRO", text="Por favor escolha ou digite um culto!")
        return
    culto = f"{cultoalternativo.get()}"
    return janela.destroy()

janela = Tk()
janela.title("Culto")
lb_orientacao = Label(janela, text="Escolha o Título do Culto apertando em um dos botões abaixo: ")
lb_orientacao.grid(column=0, row=0)
culto_de_ensino = Button(janela, text="Culto de Ensino", command=cultodeensino)
culto_de_ensino.grid(column=0, row=1)
culto_de_libertacao = Button(janela, text="Culto de Libertação", command=cultodelibertacao)
culto_de_libertacao.grid(column=0, row=2)
ebd = Button(janela, text="EBD", command=ebd)
ebd.grid(column=0, row=3)
culto_da_familia = Button(janela, text="Culto da Família", command=cultodafamilia)
culto_da_familia.grid(column=0, row=4)
outro = Label(janela, text="Outro: ")
outro.grid(column=0, row=5)
cultoalternativo = Entry(janela)
cultoalternativo.grid(column=1, row=5)
confirmar = Button(janela, text="Confirmar", command=outroculto)
confirmar.grid(column=2, row=5)
janela.mainloop()

ptg.PAUSE = 3


hora_do_dia = datetime.datetime.today().hour
ano = int(datetime.date.today().year)
mes = int(datetime.date.today().month)
dia = int(datetime.date.today().day)
dds = calendar.weekday(ano, mes, dia)
if mes < 10:
    mes = f"0{mes}"
if dia < 10:
    dia = f"0{dia}"
data = f" {dia}/{mes}/{ano}"
titulo = f"✝ {culto} ✝{data}"
# Abrindo Apps
ptg.hotkey('win', 'r')
local = r'C:\Users\Multimídia ADEV11\Desktop\Logitech Capture.lnk'
pcp.copy(local)
ptg.hotkey('ctrl', 'v')
ptg.press('enter')
tm.sleep(5)
ptg.hotkey('win', 'r')
local = r'C:\Users\Multimídia ADEV11\Desktop\ATEM.lnk'
pcp.copy(local)
ptg.hotkey('ctrl', 'v')
ptg.press('enter')
tm.sleep(5)
ptg.hotkey('win', 'r')
local = r'C:\Program Files\obs-studio\bin\64bit\obs64.exe'
pcp.copy(local)
ptg.hotkey('ctrl', 'v')
ptg.press('enter')
tm.sleep(5)
# Entrando no Google Chrome
ptg.hotkey('winRight')
ptg.write('Chrome')
ptg.press('enter')
tm.sleep(5)
# Configurando Youtube Studio
link = r"https://studio.youtube.com/video/QrBSuhX1D9g/livestreaming"
pcp.copy(link)
tm.sleep(1.5)
ptg.hotkey('ctrl', 'v')
ptg.press('enter')
tm.sleep(10)
ptg.click(595, 680)
tm.sleep(15)
ptg.click(1132, 28)
tm.sleep(3)
ptg.click(929, 223)
tm.sleep(3)
ptg.click(972, 256, clicks=3)
tm.sleep(0.5)
ptg.hotkey('backspace')
pcp.copy(titulo)
ptg.hotkey('ctrl', 'v')
tm.sleep(4)
ptg.moveTo(x=1104, y=230, duration=3)
tm.sleep(1)
ptg.dragTo(x=1104, y=350, duration=3)
tm.sleep(2)
ptg.moveTo(x=646, y=380, duration=2)
tm.sleep(1.5)
ptg.click(x=646, y=380)
tm.sleep(2)
ptg.click(x=646, y=380)
tm.sleep(5)
pcp.copy(bglive)
ptg.hotkey('ctrl', 'v')
tm.sleep(2)
ptg.press('enter')
ptg.moveTo(x=1065, y=658, duration=2)
tm.sleep(1.5)
ptg.click(x=1065, y=658)
