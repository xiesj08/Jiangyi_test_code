import requests
import json
class Api:

    def __init__(self):
        self.host = 'https://reqres.in/api/'

    def hello(self):
        print('hello world!')

    def users(self):

        url = self.host + 'users'
        print(f'url: {url}')
        params = {'page': 99999}
        res = requests.get(url, params=params)
        print(res.text)

    def create(self):
        url = self.host + 'users'
        json = {'name': 'jiangyi', 'job': 'leader'}

        '''接口'''
        res = requests.post(url, json=json)


        resp_data = res.json()

        name = resp_data['name']
        job = resp_data['job']

        if name == 'jiangyi':
            print(f'pass')
        if name != 'jiangyi':
            print(f'fail')
        if job == 'leader':
            print(f'pass')
        if job != 'leader':
            print(f'fail')


    def register(self):
        url = self.host + 'register'
        json = {'email': 'eve.holt@reqres.in', 'password': '123456'}
        # json = {'email': 'xieshangji.work@gmail.com', 'password': '123456'}

        res = requests.post(url, json = json)
        res_data = res.json()
        print(f'res_data: \n{res_data}')





'''pytest'''







'''pytest'''

if __name__ == '__main__':
    api = Api()
    # api.users()
    # api.create()
    api.register()
