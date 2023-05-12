import random
import time 

def gen_proxy():
  f = open('./result/proxy.txt', 'a+')
  asking = str(input('How Many Proxy To Scrape: '))
  asks = 1
while asks <= asking:
  proxy = str(random.randint(10, 152)) + '.' + str(random.randint(10, 152)) + '.' + str(random.randint(10, 152)) + '.' + str(random.randint(10, 152))
  port = random.randint(22, 8080)
  f.write(f'\n{proxy}:{port})
  f.close()
  asks += 1

gen_proxy()
