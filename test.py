import sh

text_filenames = [i for i in sh.ls('.').split() if i.endswith('.txt')]

for filename in text_filenames:
	with open(filename) as f:
		assert 'test' in f.read()
		print('FILE {} IS OK'.format(filename))
