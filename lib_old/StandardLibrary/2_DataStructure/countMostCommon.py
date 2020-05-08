import collections

c = collections.Counter()
with open('/usr/share/dict/words', 'r') as wordsfile:
	for line in wordsfile:
		c.update(line.strip().lower())

print('The most common words: ')
for letter, count in c.most_common(5):
	print('word {} appear {} times'.format(letter, count))

