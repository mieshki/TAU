import unittest
import verify

from main import *
from mockito import when, mock, unstub


class TestGame2D(unittest.TestCase):
    def tearDown(self):
        unstub()

    def test_wrapper_api_call(self):
        response = mock({'status_code': 200, 'text': 'Ok'})
        when(RequestsWrapper).get(...).thenReturn(response)
        ans = RequestsWrapper.get('http://google.com/')
        verify.is_true(ans == response)

    def test_wrapper_api_cal_server_error(self):
        response = mock({'status_code': 500, 'text': 'Error'})
        when(RequestsWrapper).get(...).thenReturn(response)
        ans = RequestsWrapper.get('http://google.com/')
        verify.is_true(ans == response)

    def test_wrapper_invalid_api_call(self):
        response = mock({'status_code': 400, 'text': 'Invalid request'})
        when(RequestsWrapper).get('::das123').thenReturn(response)
        ans = RequestsWrapper.get('::das123')
        verify.is_true(ans == response)

    def test_stock_get_value(self):
        when(StockApi).get_current_value(...).thenReturn(500)
        output = StockApi.get_current_value()
        verify.IsTrue(500 == output)

    def test_stock_get_history(self):
        response = mock({'pos1':'val1', 'pos2':'val2'})
        when(StockApi).get_current_value(...).thenReturn(response)
        output = StockApi.get_current_value()
        verify.IsTrue(response == output)


if __name__ == '__main__':
    unittest.main()
