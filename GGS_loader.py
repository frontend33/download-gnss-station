"""
comment
"""

#import fetch_data
import requests
import base64

spisok = [['vologodskya.txt', 28, '35'],['ivanovskay.txt', 29, '37'],['chuvashia.txt', 26, '21'],['mariyskiy.txt', 17, '12'],['tatarstan.txt', 56, '16'],['kirovskaya.txt', 44, '43'],['smolenskaya.txt', 27, '67'], ['leningradskaya.txt', 30, '47']]

for s in spisok:
# region_code='35'
# rayon_count=28
# filename='Vologodskaya.txt'
	try:
		link='http://pbprog.ru/webservices/oms/ajax_oms.php?type=fs&cn='+s[2]+'%3A'
#link_full='http://pbprog.ru/webservices/oms/ajax_oms.php?type=fs&cn=66%3A01' 

		headers = {'X-Requested-With':'XMLHttpRequest','Cookie':'_ym_uid=1508829202456486828; BX_USER_ID=345f53efb749c88b92c3744f1042df14; BITRIX_SM_LOGIN=wahha; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; last_visit=1508902955787::1508913755787; __utma=16333431.2118996432.1508829202.1508846067.1508913757.5; __utmc=16333431; __utmz=16333431.1508832650.2.2.utmcsr=yandex|utmccn=(organic)|utmcmd=organic; _ym_isad=2; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1508965140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; tmr_detect=0%7C1508913765891; PHPSESSID=5cc9cbedfac835b4bc9ae15acecc368e; BITRIX_SM_UIDH=c4c748dc20c1a16b16209a430e30a080; BITRIX_SM_UIDL=wahha; BITRIX_SM_SALE_UID=1937074'}
# построение списка текстов из 2х символов

		L=[str(i).rjust(2,'0') for i in range(1,s[1])]
		with open(s[0], 'wb') as fd:
			fd.write("FILENAME" + '\t' + "VERSION" + '\t' + "CAD_NUM" + '\t' + "PNmb" + '\t' + "PName" + '\t' + "PP" + '\t' + "OrdX" + '\t' + "OrdY" + '\t' + "X84" + '\t' + \
								   "Y84" + '\t' + "LON" + '\t' + "LAT" + '\t' + "TIMESTAMP_X" + '\t' + "FILEDATE" + '\t' + "NAME" + '\t' + "status" + '\t' + "Height" + '\n')
			for i in L:
				kvartal = i
				req_link=link+kvartal
				print('link:',req_link)
				print('ZAPROS!!!')
					#req = requests.Request('GET',req_link, auth=('user', 'pass'))
				#Запрос к сайту с пунктами
				req=requests.get(req_link,headers=headers)
				#Декодировка из бейза
				try:
					req_out=base64.b64decode(req.text)
				except:
					req_out='____________\n'

				req_out=req_out.replace('"omss": [','"omss": [\n')
				req_out=req_out.replace('}, {','},\n{')
				req_out=req_out.replace('"}]}','"}\n')
				req_out = req_out.replace('", "', '\t')
				req_out = req_out.replace('": "', '\t')
				req_out = req_out.replace('0\n', '')

				lines = req_out.split('\n')
				i = 0
				for line in lines:
					i += 1
					column = line.split('\t')
					try:
						line_new = column[3] + '\t' + column[5] + '\t' + column[7] + '\t' + column[17] + '\t' + column[
							19] + '\t' + column[21] + '\t' + column[23] + '\t' + column[25] + '\t' + column[27] + '\t' + \
								   column[29] + '\t' + column[31] + '\t' + column[33] + '\t' + column[35] + '\t' + column[
									   37] + '\t' + column[39] + '\t' + column[41] + '\t' + column[43] + '\n'
					except:
						print('игнорится строка № '+ str(i))
						line_new =""
					spisok.append(line_new)
					fd.write(line_new)
				print('ZAMENA')
	except:
		print("Вы вышли за предел")
	#    for chunk in r.iter_content(chunk_size=128):
	# запись в файл






#print out_text.decode('utf-8')
#print out_text_j.decode('utf-8')