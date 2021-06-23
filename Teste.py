#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyautogui as ptg
import time
import pyperclip as pcp

ptg.PAUSE = 3

ptg.hotkey('ctrl', 't')
ptg.write('adev11')
ptg.press('enter')
# time.sleep(5)
# ptg.click(963, 97)
# ptg.write('python')
# ptg.press('enter')


# In[15]:


time.sleep(5)
print(ptg.position())
ptg.alert("Posição Registrada")


# In[3]:


import pyautogui as ptg
import time
import pyperclip as pcp

ptg.PAUSE = 3
contato = str(input('Pra qual contato a msg deve ser enviada? Digite a seguir: '))
ptg.hotkey('ctrl', 't')
ptg.write('w')
ptg.press('enter')
time.sleep(5)
ptg.click(519, 172)
pcp.copy(contato)
ptg.hotkey('ctrl', 'v')
ptg.press('enter')
ptg.write("Fala mano!")
ptg.hotkey('shiftleft', 'enter')
ptg.write("Eu programei essa msg!")
ptg.hotkey('shiftleft', 'enter')
ptg.write("Eu gostei bastante kkkk")
ptg.press('enter')


# In[16]:


contato = str(input('Pra qual contato a msg deve ser enviada? Digite a seguir: '))
ptg.hotkey('ctrl', 't')
ptg.write('w')
ptg.press('enter')
time.sleep(5)
ptg.click(519, 172)


# In[8]:


ptg.KEYBOARD_KEYS


# In[ ]:




