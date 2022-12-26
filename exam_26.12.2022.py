# encoding=utf-8
# задача № 5

capitals = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington')
a = 'Russia'

def reverseLookup(capitals, a):
        print(capitals.get(a))


print(reverseLookup(capitals, a))