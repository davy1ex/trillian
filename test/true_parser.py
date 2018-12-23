import bs4
import requests
import re
import os
from pprint import pprint
from urllib3.connectionpool import InsecureRequestWarning


class Parser:
    def __init__(self):
        self.soup = bs4.BeautifulSoup(self.get_html(), 'lxml')      # заготовка для парсинга
        self.day_to_pc = {
                'понедельник': 0,
                'вторник': 1,
                'среда': 2,
                'четверг': 3,
                'пятница': 4,
                'суббота': 5,
            }

    def get_html(self):
        """
        пробует получить html код страницы, если на странице снова профилкатика,
        то чекает оффлайн версию,
        если нет и её, то сбрасывает программу нахуй
        :return: html код
        """
        # 'https://ssau.ru/rasp?group=6161-110501D'
        try:
            html = requests.get('https://ssau.ru/rasp?group=6161-110501D', verify=False).text
            re.search('tbody', html).group(0)       # проверяет, есть ли таблица в коде

            return html

        except AttributeError:
            try:
                print('Онлайн версия не работает.')
                f = open('test/index.html')
                html = f.read()
                f.close()
                print('Загрузил оффлайн версию.')

                return html

            except FileNotFoundError:
                print('Оффлайн версия расписание не найдена.')
                quit()

    def get_number_of_week(self):
        """
        парсит номер недели
        :return: номер недели
        """
        week = int(self.soup.find('p', {'class': 'nav-link pl-1 mb-0'}).text.split()[0])

        return week

    def get_table(self):
        """
        определяет чётная ли или не чётная неделя и возвращает таблицу с расписанием
        :return: таблицу с расписанием
        """
        self.week = self.get_number_of_week()
        if self.week % 2 == 0:
            table = (self.soup.find('div', {'id': 'content2'})).find('table')
        else:
            table = (self.soup.find('div', {'id': 'content1'})).find('table')

        return table

    def get_rasp(self):
        rasp = {}
        self.table = self.get_table()

        for tr in self.table.find_all('tr'):
            pari = []
            for td in tr.find_all('td'):
                pari.append(td.text)
            if tr.find('td') != None:
                rasp[tr.find('td').text] = pari[1:]

        n = 0
        rasp2 = []
        for day in self.day_to_pc:
            rasp2.append(
                {
                    'day': day,
                    'start': '',
                    'rasp': [],
                    'end': '',
                }
            )
            time = []
            for key in rasp:
                lesson = rasp[key][n]
                if lesson != '':
                    rasp2[n]['rasp'].append(lesson)
                    time.append(key)
            # print(time)
            if len(rasp2[n]['rasp']) > 0:
                rasp2[n]['start'] = time[0].split()[0]
                rasp2[n]['end'] = time[-1].split()[1]
            n += 1

        return rasp2

    def search_day(self, day, only_rasp=False):
        rasp = self.get_rasp()
        for d in rasp:
            if d['day'] == day:
                if only_rasp:
                    return d['rasp']
                else:
                    return d


if __name__ == '__main__':
    pass