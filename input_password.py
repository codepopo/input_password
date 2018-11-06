#密碼重試程式




pw = 'a123456'                                  #先在程式碼中設定好密碼
x = 3                                           #次數計算方式改成用減的,比較直覺
while x > 0 :                                   #讓使用者最多輸入三次密碼
	x = x - 1
	pw_in = input('請輸入正確密碼', ) 
	if pw_in == pw :                            #對的話
		print('密碼正確')                       
		break
	else :
		print('密碼錯誤')#不對的話
		if x > 0 :
			print('你還有',x, '次機會')
		else :
			print("帳號已被鎖定")
