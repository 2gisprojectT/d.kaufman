__author__ = 'Дмитрий'
import unittest
from main import leo
class testLeo(unittest.TestCase):
    def setUp(self):
        self.test_data = {'status': 'status1', 'action': 'action1'}
        self.l = leo(self.test_data, {})
        self.test_object = 'test_object'
        # Переменная добавляется в словарь, хранящий соответствия входного объекта
        # и изменений status и action. Создана с целью избавления зависимости по данным. В тестах, мы используем
        # данную переменную, а не ее значение

    # Тестируем конструктор
    def test_constructor(self):
        diff_table = {self.test_object : {'status1': {'action': 'action_diff', 'status': 'null'}}}
        self.l.set_diff_table(diff_table)
        self.assertEqual(self.l.get_status(), self.test_data['status'])# Сравниваем статусы теста и статусы словаря data
        self.assertEqual(self.l.get_action(), self.test_data['action'])# Сравниваем действия теста и действия словаря data
        self.assertEqual(self.l.get_diff_table(), diff_table)# Сравниваем таблицу изменений



    # Тестируем ситуацию, когда не надо менять статус:
    # Если в diff словаре поле status имеет значение null,
    # то поле status не меняем
    def test_diff_status_null(self):
        diff_table = {self.test_object : {'status1': {'action': 'action_diff', 'status': 'null'}}}
        self.l.set_diff_table(diff_table)
        old_status = self.l.get_status()
        self.l.diff_data(self.test_object)
        self.assertEqual(old_status, self.l.get_status())

    #Проверяем корректность изменения l.data
    def test_diff_data(self):
        action_diff = 'action_diff'
        status_diff = 'status_diff'
        diff_table = {self.test_object: {'status1': {'action': action_diff, 'status': status_diff}}}
        self.l.set_diff_table(diff_table)
        self.l.diff_data(self.test_object)
        #Проверяем что значения изменились
        self.assertEqual(self.l.get_status(), status_diff)
        self.assertEqual(self.l.get_action(), action_diff)

if __name__ == '__main__':
    unittest.main()

