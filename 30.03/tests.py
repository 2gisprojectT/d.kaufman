__author__ = 'Дмитрий'
import unittest
import main
class testLeo(unittest.TestCase):
    def setUp(self):
        #Создадим льва и передадим ему таблицу изменений
        self.l = main.leo({}, main.diff)

    #Подаем на вход антилопу 2 раза: когда лев сыт и когда лев голоден
    def test_antelope(self):
        #Лев сыт, подаем антилопу
        self.l.data['status'] = 'full'
        self.assertEqual(self.l.diff_data('antelope'), {'action' : 'sleep', 'status' : 'hungry'})
        #Лев голоден, подаем антилопу
        self.l.data['status'] = 'hungry'
        self.assertEqual(self.l.diff_data('antelope'), {'action' : 'eat', 'status' : 'full'})

    #Тестируем действия льва при виде охотника
    def test_hunter(self):
        #Лев сыт подаем охотника
        self.l.data['status'] = 'full'
        self.assertEqual(self.l.diff_data('hunter'), {'action' : 'run', 'status' : 'hungry'})
        #Лев голоден, подаем охотника
        self.l.data['status'] = 'hungry'
        self.assertEqual(self.l.diff_data('hunter'), {'action' : 'run', 'status' : 'hungry'})

    #Действия льва при виде дерева
    def test_tree(self):
        #Лев сыт, подаем дерево
        self.l.data['status'] = 'full'
        self.assertEqual(self.l.diff_data('tree'), {'action' : 'see', 'status' : 'hungry'})
        self.l.data['status'] = 'hungry'
        self.assertEqual(self.l.diff_data('tree'), {'action' : 'sleep', 'status' : 'hungry'})

    #Тестируем input
    def test_input_1(self):
        self.l.inp()

if __name__ == '__main__':
    unittest.main()
