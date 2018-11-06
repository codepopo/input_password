#密碼重試程式




pw = 'a123456'                                  #先在程式碼中設定好密碼
x = 0
while x < 3 :                                   #讓使用者最多輸入三次密碼
	x = x + 1
	pw_in = input('請輸入正確密碼', ) 
	if pw_in == pw :                            #對的話
		print('密碼正確')                       
		break
	else :
		print('密碼錯誤,你還有 ',3 - x, '次機會')#不對的話
