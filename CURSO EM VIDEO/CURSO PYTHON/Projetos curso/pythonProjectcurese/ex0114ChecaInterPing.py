import urllib
import urllib.request
import requests

def check_internet():
    '''Checar conexão '''
    url ='https://www.google.com.br/'
    timout = 5
    try:
        requests.get(url,timeout=timout)
        return True
    except (Exception,ConnectionError):
        return False


def pudim():
    try:
        site = urllib.request.urlopen('http://www.google.com.br')
    except:
        print('Deu erro')
    else:
        print('Tudo OK')




if not check_internet():
    print('Internet fora do ar!')
else:
    print('Internet OK!')



pudim()