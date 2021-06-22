#!/usr/bin/env python
# coding: utf-8

# Arquivo pra Testes

# In[12]:


import pyautogui as ptg
import time
import pyperclip as pcp

ptg.PAUSE = 3

ptg.hotkey('ctrl', 't')
ptg.write('youtube.com')
ptg.press('enter')
time.sleep(5)
ptg.click(963, 97)
ptg.write('python')
ptg.press('enter')


# In[11]:


import time
import pyautogui

time.sleep(3)
print(pyautogui.position())


# In[15]:


import pyautogui
pyautogui.KEYBOARD_KEYS


# In[ ]:




