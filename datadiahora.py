from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

# Abaixo está como imprimir em formato br
# print('%s/%s/%s' % (now.day, now.month, now.year))   //DATA
# print('%s:%s:%s' % (now.hour, now.minute, now.second))   //HORA
