import os

text_filenames = [i for i in os.listdir() if i.endswith('.txt')]

for filename in text_filenames:
	with open(filename) as f:
		assert 'test' in f.read()
		print('FILE {} IS OK'.format(filename))
