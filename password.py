password = 'a123456'

x = input('請輸入密碼:')

if x == 'a123456':
	print("登錄成功!")
else:
	j = 1 
	while j<3:
		print("密碼錯誤，請再輸入一次密碼，還有%s次機會" %(3-j))
		j = j + 1
	print("錯誤太多次，已拒絕登錄")