__author__ = 'Дмитрий'
import unittest
from main import leo
class testLeo(unittest.TestCase):
    #Проверяем ситуацию, когда не надо менять статус
    def test_constructor(self):
        test_data = {'status' : 'status1', 'action' : 'action1'}
        test_diff = {'obj1' : {'status1' : {'action' : 'action_diff', 'status' : 'null'}}}
        self.l = leo(test_data, test_diff)
        self.assertEqual(test_data, self.l.data)
        self.assertEqual(test_diff, self.l.diff)

    #Тестируем ситуацию, когда не надо менять статус:
    #Если в diff словаре поле status имеет значение null,
    #то поле status не меняем
    def test_diff_status_null(self):
        test_object = 'test_object'
        test_data = {'status' : 'status1', 'action' : 'action1'}
        test_diff = {test_object : {'status1' : {'action' : 'action_diff', 'status' : 'null'}}}
        self.l = leo(test_data, test_diff)
        old_status = self.l.data['status']
        self.l.diff_data(test_object)
        self.assertEqual(old_status, self.l.data['status'])

    #Проверяем корректность изменения l.data
    def test_diff_data(self):
        test_object = 'test_object'
        test_data = {'status' : 'status1', 'action' : 'action1'}
        test_diff = {test_object : {'status1' : {'action' : 'action_diff', 'status' : 'diff_status'}}}
        self.l = leo(test_data, test_diff)
        old_data = self.l.data
        self.l.diff_data(test_object)
        self.assertEqual(old_data, test_data[test_object])

if __name__ == '__main__':
    unittest.main()
