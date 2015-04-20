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
        #Сопоставления числа и входного значения - список допустимых введенных чисел
        #К каждому входному параметру из второго поля соспоставлено число из первого, для удобства пользователя
        comprasion = {   1 : 'antelope',
                         2 : 'hunter',
                         3 : 'tree',
                         4 : 'exit'}
        #Продолжаем цикл, пока не введен корректо номер
        while True:
            rez = input('Введите номер входного параметра:\n'
                            '1) Антилопа\n'
                            '2) Охотник\n'
                            '3) Дерево\n'
                            '4) Выход\n')
            if len(rez) == 0:
                 print('Вы не ввели номер\n')
            else:
                rez = int(rez)
                r = comprasion.get(rez)
                if r != None:
                    return r
                else:
                    print('Вы ввели неверный номер\n')

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
            print ('Новые значения:', self.data, '\n')
            rez = self.inp()


#l = leo(data, diff)
#l.dialog()