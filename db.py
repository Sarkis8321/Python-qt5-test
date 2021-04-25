class Database:
    def __init__(self, filename):
        self.f = open(filename,'rt')
    def readDb(self):
        l = self.f.readlines()
        l = [line.rstrip('\n') for line in l]
        self.f.close()
        return l
    def readDbNameList(self,lis):
        nameList = []
        for elem in lis:
            try:
                with open('db/list/'+elem+'.txt', 'rt') as fin:
                    nameList.append(fin.readlines())
                fin.close()
            except Exception:
                print('ошибка подключения к базе данных')
            else: 
                print('данные успешно добавлены')
        return nameList
    def readDbNames(self, lists):
        lists = [l[0].rstrip('\n') for l in lists]
        return lists

        
            

