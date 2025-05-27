from django.test import SimpleTestCase
from  cacl import calc
class cacl_test(SimpleTestCase):

    def test_calc_val(self):
        res = calc(5,6)

        self.assertEquals(res,11)


