country = input('請輸入國家: ')
age = input('請輸入年齡: ')
if country == '台灣':
	if int(age) >= 18:
		print('你可以考駕照!!')
	else:
		print('你尚未符合資格!!')
elif country == '美國':
	if int(age) >= 16:
		print('你可以考駕照!!')
	else:
		print('你尚未符合資格!!')
