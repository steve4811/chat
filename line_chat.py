import os
def read_file(filename):
	if os.path.isfile(filename):
		message = []
		with open(filename ,'r' ,encoding = 'utf-8-sig') as f:
			for line in f:
				message.append(line.strip())
		return message
	else :
		print('檔案未找到')


def convert(lines):
	newline = []
	for line in lines:
		if line[:4] == '2019':
			continue
		else:
			newline.append(line.split(' '))
	return newline


def count_word(lines):
	steve_wc = 0
	Jason_wc = 0
	for line in lines:
		if line[1] == '蕭國珍':
			if len(line) > 2:
				steve_wc += len(line[2])
		else:
			if len(line) > 2:
				Jason_wc += len(line[2])
	print(steve_wc)
	print(Jason_wc)


def main():
	message = []
	lines = read_file('[LINE]Jason.txt')
	message = convert(lines)
	count_word(message)

main()