import bs4
from pprint import pprint


def main():
    # html = requests.get('https://ssau.ru/rasp?group=6161-110501D', verify=False).text
    html = open('Расписание - Самарский университет.html').read()
    soup = bs4.BeautifulSoup(html, 'lxml')
    week = int(soup.find('p', {'class': 'nav-link pl-1 mb-0'}).text.split()[0])
    print('Неделя: ', end = '')
    if week % 2 == 0:
        print('чётная ', end='')
        table = (soup.find('div', {'id': 'content2'})).find('table')
    else:
        print('не чётная ', end='')
        table = (soup.find('div', {'id': 'content1'})).find('table')
    print('({})'.format(week))

    rasp = {}

    for tr in table.find_all('tr'):
        pari = []
        for td in tr.find_all('td'):
            pari.append(td.text)
        if tr.find('td') != None:
            rasp[tr.find('td').text] = pari[1:]
    print(rasp)

    day_to_pc = {
        'понедельник': 0,
        'вторник': 1,
        'среда': 2,
        'четверг': 3,
        'пятница': 4,
        'суббота': 5,
    }

    # составляю расписание каждого дня
    n = 0
    rasp2 = []
    for day in day_to_pc:
        rasp2.append({day : []})
        for key in rasp:
            lesson = rasp[key][n]
            if lesson != '':
                rasp2[n][day].append(lesson)
        n += 1
    pprint(rasp2)

    # while True:
    #     number_of_day = day_to_pc[input('День: ')]
    #     n = 0
    #     for key in rasp:
    #         lesson = rasp[key][number_of_day]
    #         if lesson != '':
    #             print(key, lesson, '\n')


if __name__ == '__main__':
    main()