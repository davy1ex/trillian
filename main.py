import modules.say_shutdown as shutdown


class Start:
    def __init__(self):
#         print("""
# █───█─███─█───████─████─█───█─███
# █───█─█───█───█──█─█──█─██─██─█
# █─█─█─███─█───█────█──█─█─█─█─███
# █████─█───█───█──█─█──█─█───█─█───█
# ─█─█──███─███─████─████─█───█─███─█
#
#
# ████─█───███─██─██─███─███─██─██
# █──█─█───█────███──█───█────███
# ████─█───███───█───███─███───█
# █──█─█───█────███────█─█─────█
# █──█─███─███─██─██─███─███───█""")
        print("""
████─████─█──█─████──███─███─████─███─████──█─█─█──██
█──█─█──█─█──█─█──██─█────█──█──█──█──█──██─█─█─█─█──█
█──█─████─█─██─████──███──█──█─────█──████──███─████─█
█──█─█────██─█─█──██─█────█──█──█──█──█──██───█─█─█──█─█
█──█─█────█──█─████──███──█──████──█──████──███─█──██──█

─────────────────────────────██
████───██─███─█──█─████─███─█──█
█──█──█─█─█───█─█──█──█─█───█──█
████─█──█─███─██───█────███─█─██
█──█─█──█─█───█─█──█──█─█───██─█
█──█─█──█─███─█──█─████─███─█──█\n""")
        # self.threads = [self.parse_user_input()]
        # while True:
        #     self.parse_user_input()
        #     if len(self.threads) > 0:
        #         self.multithread()

        # это надо будет пихнуть в отдельный поток (попытка сделана выше)
        while True:
            self.parse_user_input()


    def parse_user_input(self):
        user_input = input(">: ")

        if "выключи" in user_input:

            user_time_input = user_input[10:]

            if user_time_input[2] == ":":
                a = shutdown.TurnOff_By_Time
                # self.threads.append(threading.Thread(target=a, args=(user_time_input,)))
                a.start(user_time_input)    # кажись, ахилесова пята здесь

            else:
                print("Вывод имеет вид 00:00, сер")

    # def multithread(self):
    #     for thread in self.threads:
    #         thread.start()
    #     for thread in self.threads:
    #         thread.join()
    #
    # def start(self):
    #     pass


if __name__ == "__main__":
    Start()