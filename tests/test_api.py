import pytest
import requests

'''
另一个接口测试网站
https://jsonplaceholder.typicode.com/

'''
# pytest 初始化base_url网址
@pytest.fixture
def base_url():
    return 'https://jsonplaceholder.typicode.com/posts'

# 测试 GET 请求
def test_get_posts(base_url):
    # url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(base_url)

    # 验证响应状态码为200
    assert response.status_code == 200
    # 验证返回数据是否是列表
    assert isinstance(response.json(), list)


# 测试 POST 请求
def test_create_post(base_url):
    # url = 'https://jsonplaceholder.typicode.com/posts'
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(base_url, json=payload)

    # 验证响应状态码为201（创建成功）
    assert response.status_code == 201
    # 验证返回的内容是否包含正确的标题
    assert response.json().get("title") == "foo"


# pytest 传参 "post_id"=[1, 2, 3, 4]
@pytest.mark.parametrize("post_id", [1, 2, 3, 4])
def test_get_post_by_id(base_url, post_id):
    url = f'{base_url}/{post_id}'
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json().get('id') == post_id
