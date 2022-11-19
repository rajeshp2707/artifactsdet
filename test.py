import os

text_filenames = [i for i in os.listdir() if i.endswith('.txt')]

for filename in text_filenames:
    with open(filename) as f:
        data = f.read()
        assert 'begin' in data
        assert 'end' in data
        print('FILE {} IS COMPLETE'.format(filename))
