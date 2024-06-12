import requests
import json

print("="*10, 'Задание № 1', "="*10)
url = "https://fakestoreapi.com/products/categories"

response = requests.get(url).json()
cat = json.dumps(response)
categories = (''.join(x for x in cat if x not in '["]')).split(sep=', ')

print(f'В интернет-магазине представлены категории товаров:\n \
 = {categories[0]}\n  = {categories[1]}\n  = {categories[2]}\n  = {categories[3]}\n')

choice_user = (input('Какая категория товаров Вас интересуют?:  ')).strip()
if choice_user in categories:
    print(f'\nВыбор покупателя: {choice_user.capitalize()}\n\n')
else:
    print(f'Такой категории товаров нет в интернет-магазине\n\n')

print("="*10, 'Задание № 2', "="*10)
url_1 = "https://fakestoreapi.com/carts"
url_2 = "https://fakestoreapi.com/users"

id_user = int(input(f'Сообщите свой id и узнаете о своих корзинах заказов:  '))
response_carts = requests.get(url_1).json()
response_users = requests.get(url_2).json()
carts = json.dumps(response_carts, indent=2)

flag = False
for user in response_users:
    if int(user["id"]) == id_user:
        flag = True
        for cart in response_carts:
            if int(cart["id"]) == id_user:
                print(f'Покупатель {user["name"]["firstname"].capitalize()} {user["name"]["lastname"].capitalize()}')
                print(f'{cart["date"].split(sep="T")[0]} купил в интернет-магазине\n{json.dumps(cart["products"], indent=2)}')
if not flag:
    print(f'Нет покупателя с id = {id_user}')