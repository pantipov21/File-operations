import sys
file_names = ['1.txt', '2.txt', '3.txt']

fn_sn = list()
finfo = dict()
for fn in file_names:
    f = open(fn, 'r')
    i = 0
    while f.readline() != '':
        i = i + 1
    finfo[i] = fn
    fn_sn.append(i)
    f.close()

output_file = open('result.txt', 'w')
while len(fn_sn) > 0:
    mstr = sys.maxsize
    for i in fn_sn:
        if i < mstr:
            mstr = i

    f = open(finfo.get(mstr), 'r')
    if len(fn_sn) == len(file_names):
        output_file.write(f'{finfo.get(mstr)}\n{mstr}\n')
    else:
        output_file.write(f'\n{finfo.get(mstr)}\n{mstr}\n')

    t = 0
    while t < mstr:
        output_file.write(f.readline())
        t = t + 1
    f.close()
    fn_sn.remove(mstr)
output_file.close()

print("Результат работы находится в файле result.txt")