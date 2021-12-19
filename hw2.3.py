import sys
file_names = ['1.txt', '2.txt', '3.txt']


class special_conctination:
    def __init__(self):
        self.fn_sn = list()
        self.finfo = dict()


    def build_file_structure(self):
        for fn in file_names:
            f = open(fn, 'r')
            i = 0
            while f.readline() != '':
                i = i + 1
            self.finfo[i] = fn
            self.fn_sn.append(i)
            f.close()
        return 0


    def concat_files(self, file_name):
        output_file = open(file_name, 'w')
        while len(self.fn_sn) > 0:
            mstr = sys.maxsize
            for i in self.fn_sn:
                if i < mstr:
                    mstr = i

            f = open(self.finfo.get(mstr), 'r')
            if len(self.fn_sn) == len(file_names):
                output_file.write(f'{self.finfo.get(mstr)}\n{mstr}\n')
            else:
                output_file.write(f'\n{self.finfo.get(mstr)}\n{mstr}\n')

            t = 0
            while t < mstr:
                output_file.write(f.readline())
                t = t + 1
            f.close()
            self.fn_sn.remove(mstr)
        output_file.close()
        return 0

    def execute(self, file_out):
        self.build_file_structure()
        self.concat_files(file_out)
        return 0


sc = special_conctination()
sc.execute("result.txt")
print("Результат работы находится в файле result.txt")