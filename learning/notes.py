"Transforming Code into beautiful, idomatic python"
~14 minutes in


~18 minutes

def find(seq, target): 
	for i, value in enumerate(seq): 
		if value == tgt:
			break
	else:
		return -1
	return i

for k in d:
	print(d)

#for k, v in d.items():
#	print k, '-->', v

for k, v in d.iteritems():
	print k, '-->', v

for k in d.keys():
	if k.startswith('r'):
		del d[k]


~22:40
#have two lists we want to join together to make a dicitonary:
d = dict(izip(list1, list2))

#counting with dictionaries
d = {}
for color in colors:
	if color not in d:
		d[color] = 0
	d[color] += 1

d = {}
for color in colors:
	d[color] = d.get(color, 0) + 1

d = defaultdict(int)
for color in colors:
	d[color] += 1

#group two dictionaries together
d = {}
for name in names:
	key = len(name) #Grouping method
	if key not in d:
		d[key] = []
	d[key].append(name)

d = defaultdict(list)
for name in names:
	key = len(name)
	d[key].append(name)

~28:00
#popping items atomically
while d:
    key, value = d.popitem()
    print key, '-->' value


