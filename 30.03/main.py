__author__ = 'Дмитрий'
class leo():
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


    def dialog(self):
        rez = self.inp()
        while rez != 'exit':
            #Если не надо менять статус, меняем только действие
            if self.diff[rez][self.data['status']]['status'] == 'null':
                self.data.update({'action' : self.diff[rez][self.data['status']]['action']})
            else:
            #Иначе меняем и статус и действие
                self.data.update(self.diff[rez][self.data['status']])
            print ('Новые значения:', self.data)
            rez = self.inp()

l = leo()
l.dialog()


