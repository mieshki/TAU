import unittest
import requests
import json

class ApiTests(unittest.TestCase):
    def test_random_fact_verify_status_code(self):
        url = 'https://uselessfacts.jsph.pl/random.json?language=en'
        response = requests.request("GET", url)
        self.assertEqual(200, response.status_code)

    def test_random_fact_verify_payload_exist(self):
        url = 'https://uselessfacts.jsph.pl/random.json?language=en'
        response = requests.request("GET", url)
        print(f'Random useless fact: {json.loads(response.text)["text"]}')
        self.assertTrue(response.text != '')

    def test_random_fact_verify_payload_keys(self):
        url = 'https://uselessfacts.jsph.pl/random.json?language=en'
        response = requests.request("GET", url)
        json_output = json.loads(response.text)

        expected_keys = ['id', 'text', 'source', 'source_url', 'language', 'permalink']
        received_keys = []

        for key, value in json_output.items():
            received_keys.append(key)
        self.assertEqual(expected_keys, received_keys)

    def test_bad_request(self):
        url = 'https://uselessfacts.jsph.pl/random.json?language=badbadbad'
        response = requests.request("GET", url)
        self.assertEqual(400, response.status_code)

    def test_request_404(self):
        url = 'https://uselessfacts.jsph.pl/404040404'
        response = requests.request("GET", url)
        self.assertEqual(404, response.status_code)

    def test_httpbin_post_payload_verify(self):
        url = 'https://httpbin.org/post'
        post_payload = {'test': '123'}
        response = requests.request("POST", url, data=post_payload)
        json_output = json.loads(response.text)
        self.assertEqual(post_payload, json_output['form'])

    def test_httpbin_put(self):
        url = 'https://httpbin.org/put'
        put_payload = {'test': '123'}
        response = requests.request("PUT", url, data=put_payload)
        json_output = json.loads(response.text)
        self.assertEqual(put_payload, json_output['form'])

    def test_httpbin_delete(self):
        url = 'https://httpbin.org/delete'
        delete_payload = {'test': '123'}
        response = requests.request("DELETE", url, data=delete_payload)
        json_output = json.loads(response.text)
        self.assertEqual(delete_payload, json_output['form'])

    def test_post_request_to_put_method(self):
        url = 'https://httpbin.org/put'
        response = requests.request("POST", url)
        ''' POST method shouldn't be allowed to controller operating PUT requests '''
        self.assertEqual(405, response.status_code)

    def test_put_request_to_post_method(self):
        url = 'https://httpbin.org/post'
        response = requests.request("PUT", url)
        ''' PUT method shouldn't be allowed to controller operating POST requests '''
        self.assertEqual(405, response.status_code)

if __name__ == '__main__':
    unittest.main()
