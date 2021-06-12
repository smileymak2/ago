driving = input('請問有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit 
	pass
ago = input('請問你的年齡?')
ago = int(ago)
if driving == '有':
	if ago >= 18:
		print('通過')
	elif ago <18:
		print('奇怪')
elif driving == '沒有':
	if ago >= 18:
		print('快d去考車牌')
	elif ago <18:
		print('很快可以考車牌')