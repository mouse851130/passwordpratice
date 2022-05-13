password = 'a123456'  #正解
i = 3 #剩餘猜的次數
while True:
	pwd = input('請輸入密碼：') #左邊不能用password，不然跑出來的數值會蓋掉line 1的正解
	if pwd == password:  #password可以改a123456，但是不好，因為a123456已經存進password了
                         #這樣之後要改的話只要改line 1 的a123456		
		print('登入成功')
		break  #正解，所以逃出迴圈
	else:
		i = i - 1 #因為錯了，所以是3-1
		print('登入失敗，你還有', i, '次機會') #把一句話變成兩個字串跟一個變數
		if i == 0:
			break

