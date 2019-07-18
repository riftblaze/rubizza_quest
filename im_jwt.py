#!/usr/bin/env python encoding='utf-8'
import json
import jwt

key = 'yours_mail@abc.de'
data = '''{        "age": 32,
         "english": "intermediate",
         "full_name": "Taisiia Alekseevna Ialovaia",
         "goal": "improve ruby skills",
         "education": "SPbGUT,2021,applied cybersecurity",
         "have_a_job": "no",
         "hours_per_day": 13,
         "programming_languages": "Python",
         "laptop": "yes",
         "phone_number": 79500153410 }'''

#print(json.dumps(data,sort_keys=True,indent=4,separators=('\n', ':')))
#print('~')
#print("data " + str(type(data))) - класс строка
print('~ this will create a token for rubizza quest')
print(data)
print('~')
payload = open('payload.json', 'w')
payload.write(data)
payload.close()
print("~")
#payload = open('payload.json', 'r')
#print ('~')
#readdata = payload.read()
#print(readdata)
#payload.close()

encoded = jwt.encode(json.load(open('payload.json', 'r')), key, algorithm='HS256')
print(encoded)

token = open('token', 'wb')
token.write(encoded)
token.close()


