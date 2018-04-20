import requests
import json
from threading import Thread
import time

class Picture(Thread):

    def __init__(self,url):
        super().__init__()
        self._url = url

    @property
    def url(self):
        return self._url

    def run(self):
        resp = requests.get(self._url)
        mydict = json.loads(resp.text)
        print(mydict)
        start1 = time.time()
        for tempdict in mydict['newslist']:
            pic_url = tempdict['picUrl']
            resp = requests.get(pic_url)
            filename = pic_url[pic_url.rfind('/') + 1:]
            try:
                with open(filename, 'wb') as fs:
                    fs.write(resp.content)
            except IOError as e:
                print(e)
        end1 = time.time()
        print('耗费了%f秒' % (end1 - start1))


def main():
    start = time.time()
    p1 = Picture('http://api.tianapi.com/meinv/?key=29bd63490eee88afd3f2b30fca8daab2&num=5')

    p2 = Picture('http://api.tianapi.com/meinv/?key=29bd63490eee88afd3f2b30fca8daab2&num=5')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print('总共耗费了%f秒' % (end - start))


if __name__ == '__main__':
    main()