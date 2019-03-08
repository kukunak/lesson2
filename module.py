import datetime, ephem
date = datetime.datetime.now()
print(date)

a = date.strftime('%a.%d.%m.%Y')
print(a)


mars = ephem.Mars('2016/09/23')
ephem.constellation(mars)

print(ephem.next_full_moon('2016/09/23'))

# необходимо запомнить:
# if __name__ =="__main_":
#   функция()
# необходимо прописать в коде для случая from .. import
# 