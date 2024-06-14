import requests
import json

print("="*10, 'Задание № 1', "="*10)

url = "https://fakestoreapi.com/products/categories"
url_prod = "https://fakestoreapi.com/products/category/"

response = requests.get(url).json()
cat = json.dumps(response)
categories = (''.join(x for x in cat if x not in '["]')).split(sep=', ')

print(f'В интернет-магазине представлены категории товаров:\n \
 = {categories[0]}\n  = {categories[1]}\n  = {categories[2]}\n  = {categories[3]}\n')

choice_user = (input('Какая категория товаров Вас интересуют?:  ')).strip()
if choice_user in categories:
    print(f'\nВыбор покупателя: {choice_user.capitalize()}\n')
    r = requests.get(url_prod + choice_user).json()
    for product in r:
        print('* ', product['title'].capitalize())
else:
    print(f'Такой категории товаров нет в интернет-магазине\n\n')



print("="*10, 'Задание № 2', "="*10)

url_1 = "https://fakestoreapi.com/carts"
url_2 = "https://fakestoreapi.com/users"
url_3 = "https://fakestoreapi.com/products"

id_user = int(input(f'Сообщите свой id и узнаете о своих корзинах заказов:  '))
response_carts = requests.get(url_1).json()
response_users = requests.get(url_2).json()
response_products = requests.get(url_3).json()

flag = False
for user in response_users:
    if int(user["id"]) == id_user:
        flag = True
        for cart in response_carts:
            if int(cart["id"]) == id_user:
                print(f'Покупатель {user["name"]["firstname"].capitalize()} {user["name"]["lastname"].capitalize()}')
                print(f'{cart["date"].split(sep="T")[0]} купил в интернет-магазине:')
                cart_user = cart["products"]
                for i in cart_user:
                    for k in response_products:
                        if i['productId'] == k['id']:
                            print(f'=> {k["title"]} в количестве {i["quantity"]} штук(и)')
if not flag:
    print(f'Нет покупателя с id = {id_user}')



print("="*10, 'Задание № 3', "="*10)

id_user = int(input("Введите цифровой идентификатор аккаунта VK: ").strip())
base_url = "https://api.vk.com/method/"
method_api = "friends.get"
payload = {
    "user_id": id_user,
    "order": "name",
    "access_token": "068d17a3068d17a3068d17a3460595bafc0068d068d17a360e639740403fb356622506a",
    "v": 5.199
}
url_vk = f"{base_url}{method_api}"

response_vk = requests.post(url_vk, params=payload)
count = response_vk.json()["response"]["count"]
print(f'\nУ пользователя с id{id_user} {count} друзей')
