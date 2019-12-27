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
	name = None
	for line in lines:
		if line == 'Allen':
			name = 'Allen'
			continue
		elif line == 'Tom':
			name = 'Tom'
			continue
		if name :
			newline.append(name + ':' + line)
	return newline

def write_file(filename,message):
		with open(filename ,'w' ) as f:
			for line in message:
				f.write(line + '/n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt' ,lines)

main()

