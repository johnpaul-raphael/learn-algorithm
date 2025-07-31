list = list()
list.append('a')
# list.append(1)
list.append('z')
list.append('m')
print(f'{list}')
print(f'{list.index('m')=}')
print(f'{len(list)=}')
print(f'{list.pop(2)=}')
print(f'{len(list)=}')
list.insert(1, 'b')
print(f'{list=}')
list1 = ['d', 'h']
list.extend(list1)
print(f'{list=}')
list.reverse()
print(f'{list=}')
list.pop(2)
list.sort()
print(f'{list=}')

print('=========================================================================')
set1 = set()
set1.add('L')
set = set()
set.add('m')
set.add('d')
set.add('p')
print(f'{set=}')
# print(f'after pop {set.pop()=}')
print(f'{set=}')

print(f'after union {set.union(set1)=}')

# set.clear()
print(f'after cleat {set}')

set.remove('d')
print(f'after remove d {set=}')

set.update('z')
print(f'update p to P {set}')
print('=========================================================================')
dicts = dict()
dicts[1] = 'z'
dicts[2] = 't'
dicts[1] = 'g'
dicts[3] = 'a'

print(f'{dicts=}')
dicts.pop(1)
print(f'{dicts=}')
print(f'{dicts.get(3)=}')
print(f'{dicts.keys()=}')
print(f'{dicts.values()=}')
