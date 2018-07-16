print("歡迎")
a = input("猜猜看:")
guess = int(a)
while guess != 5:
	a = input("再猜猜看:")
	guess = int(a)
print("猜對了")
print("遊戲結束")