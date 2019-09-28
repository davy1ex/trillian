import os
from threading import Thread
import datetime
import time

import commands
from settings import CLEANED_FOLDERS


class Trillian:
    def __init__(self):
        print("Модуль периодической очистки запущен")
        Thread(target=self.time_removal).start()


    def run(self):
        # тут подрубаются команды
        while True:
            try:
                user_input = self.listen()
            except (EOFError, KeyboardInterrupt):
                quit()
            
            if "caf" in user_input:
                if len(user_input) == 1:
                    commands.clear_folders(folders=CLEANED_FOLDERS)                
                # else:
                #     try:
                #         for 
                #         clear_folders(folder)
            
            elif "ca" in user_input:
                if len(user_input.split()) == 1:
                    print(commands.clear_folders(folders=CLEANED_FOLDERS, force=False))

    
    def time_removal(self):        
        while True:
            # ниже ебанутый способ узнать сколько секунд до следующей даты очистки
            time_sleep = ((datetime.datetime.now() + datetime.timedelta(7 - (datetime.datetime.now().day % 7))) - datetime.datetime.now()).total_seconds() # количество секунд до момента очистки
            time.sleep(time_sleep) # усыпить поток
            
            # if check_choice("Совершить еженедельную очистку?"): # подтверждение
            commands.clear_folders(folders=CLEANED_FOLDERS, force=True)         


    def listen(self):
        return input(">: ")

    
    def check_choice(self, output=""):
        choice = input(output)
        
        if choice in ["y", "д"]:
            return True
        
        elif choice in ["n", "н"]:
            return False
        
        else:
            return "not choiced"
            