begin = int(input('begin->'))
end = int(input('end->'))
for item in range(end, begin-1, -1):
    print(item, end='\t')