password = 'a123456'
j = 0
while j < 3:
	j = j + 1
	pwd = input('請輸入密碼:')
	if pwd == password:
		print("登錄成功!")
		break
	elif j == 3:
		print("錯誤太多次，已拒絕登錄")
	else:
		print("密碼錯誤，請再輸入一次密碼，還有%s次機會" %(3-j))