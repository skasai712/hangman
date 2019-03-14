import re

text = """キリンは大昔から__職業__の興味対象でした。
キリンは__動物__の中で一番背が高いですが、科学者たちはそのような
長い__体の一部__をどうやって獲得したのか説明できません。
キリンの身長は__数値____単位__近くあり、その高さは
ほどんどは脚と__体の一部__によるものです。"""			 	 

def mad_libs(mls):
	"""
	:param mls: 文字列、 入力してもらいたい文字を　__hogehoge__ でスペルアウトする。
	"""

	hints = re.findall("__.*?__", mls)
	if hints is not None:
		for word in hints: 
			new = input("{} を入力してください:".format(word.replace("__","")))
			mls = mls.replace(word, new, 1)
		print('\n')
		mls = mls.replace("\n","")
		print(mls)



mad_libs(text)