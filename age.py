driving = input('請問你有開過車嗎?')
if driving != "有" and driving != "沒有":
	print('只能輸入 有/沒有')
	raise SystemExit

age = input('請問您的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('您通過測驗了')
	else:
		print('奇怪 您怎麼有開過車呢?')
elif driving == '沒有':
	if age >= 18:
		print('您可以考駕照拉，怎麼還沒考呢')
	else:
		print('很好, 再過幾年就可以考駕照了')