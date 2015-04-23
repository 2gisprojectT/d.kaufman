__author__ = 'Дмитрий'

data = {'action' : 'default',
        'status' : 'hungry'}

diff = {
    'antelope' : {'full' : {'action' : 'sleep',
                            'status' : 'hungry'},
                  'hungry':{'action' : 'eat',
                            'status' : 'full'}},

    'hunter'    :{'full' :  {'action' : 'run',
                             'status' : 'hungry'},
                  'hungry': {'action' : 'run',
                             'status' : 'null'}},

    'tree'      :{'full' : { 'action' : 'see',
                             'status' : 'hungry'},
                  'hungry' :{'action' : 'sleep',
                             'status' : 'null'}}
}

class leo():

    data = {}
    diff = {}
    def __init__(self, data, diff):
        self.data = data
        self.diff = diff
    def inp(self):
        #Продолжаем цикл, пока не введен корректо номер
        while True:
            for key in diff.keys():
                print(key)
            rez = input("Your selection? (exit for end)\n")
            #Если ничего не введено
            if len(rez) == 0:
                 print("You don't select\n")
            else:
                #Проверяем, верно ли ввели данные
                if diff.get(rez) != None or rez == 'exit':
                    return rez
                else:
                    print('You data is incorrect\n')

    def diff_data(self, object):
        #Если не надо менять статус, меняем только действие
        if self.diff[object][self.data['status']]['status'] == 'null':
            self.data.update({'action' : self.diff[object][self.data['status']]['action']})
        else:
        #Иначе меняем и статус и действие
            self.data.update(self.diff[object][self.data['status']])
        return self.data

    def dialog(self):
        rez = self.inp()
        while rez != 'exit':
            self.diff_data(rez)
            print ('New data:', self.data, '\n')
            rez = self.inp()

    def get_status(self):           #Получение статуса
        return self.data['status']

    def get_action(self):           #Получение действия
        return self.data['action']

    def set_diff_table(self, d):    #Установить таблицу изменений
        self.diff = d

    def get_diff_table(self):       #Получить таблицу изменений
        return self.diff



#l = leo(data, diff)
#l.dialog()
