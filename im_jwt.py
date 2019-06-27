#!/usr/bin/env python encoding='utf-8'
#это не работает. но общий смысл такой)
import jwt
#воспользуемся либой, которую умные люди сделали до нас
import os
key = "yours_mail@abc.de"
#по условию задачи
payload_file = open('payload.json','r')
#в нагрузке данные сиви
encoded = jwt.encode(payload_file, key, algorithm='HS256')
print(encoded)
#отсюда мы получим нужный нам "токен"
payload_file.close()
#закрыть процесс с файлом
