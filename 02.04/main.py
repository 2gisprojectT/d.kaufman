from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class SeleniumTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait("5")

    def tearDown(self):
        self.driver.close()

    # Зайдем на сайт ngs.ru и проверим, нет ли пробок на дорогах
    #Тест заврешится успехом, если оценка пробок в баллах будет <=3
    #Данные о пробках находятся в верхем левом углу, справа от значка
    #"Нгс Новосибирск"
    def testTraffic(self):
        self.driver.get("http://www.ngs.ru")
        rez = self.driver.find_element_by_class_name("balls")  #На странице только один эллемент класса balls
        #Чтобы тест всегда проходил, поставил сравнение с 10
        self.assertLessEqual(int(rez.text[0]), 10)  #Проверяем что оценка пробок <= 3

    #Проверим, есть ли серьезные колебания курса доллара, относительно момента написания теста
    #Текущий курс = 50.8, тест завершится положительно, если курс будет находится на отрезке
    #[45; 55]
    def testDollar(self):
        a = 45  #Границы нормальных значений курса, при которых тест проходит успешно
        b = 55
        self.driver.get("http://www.google.com")
        q = self.driver.find_element_by_name("q")
        q.send_keys("курс доллара")
        q.send_keys(Keys.ENTER)
        #Получил с помощью XPath Helper
        info = self.driver.find_element_by_xpath("/html/body[@id='gsr']/div[@id='viewport']/div[@id='main']"
                                                 "/div[@id='cnt']/div[@class='mw'][3]/div[@id='rcnt']"
                                                 "/div[@class='col'][1]/div[@id='center_col']/div[@id='res']"
                                                 "/div[@id='topstuff']/g-card/div/div[@class='_srb vk_c vk_bk']"
                                                 "/div[@class='ct-cs']/div[@class='vk_ans vk_bk']")

        #info.text на момент написания теста, имеет значение: "50.8026824 российских рубля"
        rez = float((info.text.split(' '))[0])

        #Проверим, что полученное значение больше a
        self.assertGreaterEqual(rez, a)
        #Проверим, что полученное значение меньше b
        self.assertLessEqual(rez, b)

    #Проверим некоторые атрибуты рекламного банера на верху страницы ngs.ru
    def testBanner(self):
        self.driver.get("http://www.ngs.ru")
        obj = self.driver.find_element_by_id("ap54")
        self.assertEqual(obj.get_attribute("type"), "application/x-shockwave-flash")
        self.assertEqual(obj.get_attribute("scale"), "noscale")
if __name__ == '__main__':
    unittest.main()