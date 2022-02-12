from bs4 import BeautifulSoup
import requests


def data():
    content = requests.get('https://www.bmkg.go.id/')
    soup = BeautifulSoup(content.text, 'html.parser')
    main = soup.find('div', {'class': 'col-md-4 artikel-pengumuman-home md-margin-bottom-20'})

    dat = []
    news = main.findChildren('h3')
    for i in news:
        dat.append(i.text)

    datt = []
    date = main.findChildren('li')
    for j in date:
        datt.append(j.text)

    print('berikut artikel terakhir pada web BMKG:')
    print(f"{dat[0]}, terbit pada tanggal {datt[0]}")
    print(f"{dat[1]}, terbit pada tanggal {datt[1]}")
    print(f"{dat[2]}, terbit pada tanggal {datt[2]}")
    print(f"{dat[3]}, terbit pada tanggal {datt[3]}")


if __name__ == '__main__':
    data()
