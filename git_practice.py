# with open('cats.txt', 'w') as file:
#     file.write('Thomas, Varya, Foxya, Miya, Fenya')
# with open('dogs.txt', 'w') as file:
#     file.write('Cooper, Toby, Jack\n'
#                'Molly, Daisy, Sophie\n'
#                'Max, Duke')
# with open('mice.txt', 'w') as file:
#     file.write('Mickey')
# with open('films.txt', 'w') as file:
#     file.write('Intertstate 60 (2002)\n'
#                'Gone Girl (2014)\n'
#                'Anna Karenina (2012)')
# with open('series.txt', 'w') as file:
#     file.write('Planet Earth ||| (2023)')
# with open('numbers1.txt', 'w') as file:
#     file.write('25 42 37 1 29\n'
#                '58 211 5')
# with open('numbers2.txt', 'w') as file:
#     file.write('4 1 3310 5 7\n'
#                '96 412 233 1 0 37 6584 5\n'
#                '4 63 87 2 8')
# d = {}
# lst = []
# for i in range(int(input())):
#     with open(input()) as file:
#         d[file.name] = file.readlines()
# for k, v in d.items():
#     if k == 'films.txt':
#         e = (len(v) - 1) * 2
#         for i in v:
#             e += int(len(i))
#         lst.append([k, e])
#     elif len(v) > 1:
#         r = len(v) - 1
#         for i in v:
#             r += int(len(i))
#         lst.append([k, r])
#     else:
#         u = 0
#         for i in v:
#             u += int(len(i))
#         lst.append([k, u])
# sor_r = sorted(lst)
# res = sorted(sor_r, key=lambda x: int(x[1]), reverse=True)
# for i, j in res:
#     print(f'{i} {j}B')

with open('desyatochka.txt', 'w') as file_des, open('kubit.txt', 'w') as file_kub, open('polosa.txt', 'w') as file_pol:
    file_des.write('хлеб: 35\n'
                'банан: 210\n'
                'йогурт: 52\n'
                'киноа: 162\n'
                'курица: 320\n'
                'яблоко: 126\n'
                'молоко: 74\n'
                'кефир: 50\n'
                'шоколад: 198\n'
                'лимон: 120\n'
                'груша: 150')

    file_kub.write('хлеб: 34\n'
                'йогурт: 49\n'
                'киноа: 160\n'
                'курица: 330\n'
                'яблоко: 99\n'
                'молоко: 76\n'
                'кефир: 54\n'
                'шоколад: 183\n'
                'груша: 145')

    file_pol.write('хлеб: 52\n'
                'банан: 220\n'
                'йогурт: 51\n'
                'киноа: 190\n'
                'курица: 360\n'
                'яблоко: 118\n'
                'молоко: 75\n'
                'кефир: 49\n'
                'шоколад: 188\n'
                'томатная паста: 170')

with open('desyatochka.txt') as file_des, open('kubit.txt') as file_kub, open('polosa.txt') as file_pol:
    one = file_des.read()
    two = file_kub.read()
    three = file_pol.read()

enter = [input() for i in range(int(input()))]

def create_lst(my_lst):
    return dict([[name, int(price)] for name, price in [item.split(': ') for item in my_lst.split('\n')]])

def true_value(my_dict, res_dict):
    for key, value in my_dict.items():
        d = {}
        for item in enter:
            d[item] = value[item] if item in value else None
        res_dict[key] = d
    return res_dict

total_dict = {'Десяточка:': create_lst(one), 'Кубит:': create_lst(two), 'Полоса:': create_lst(three)}

res = {}

true_value(total_dict, res)

shops_order = ['Десяточка:', 'Кубит:', 'Полоса:']

answer = {shop: [] for shop in shops_order}

for product in enter:
    prices = {
        shop: res[shop][product]
        for shop in shops_order
        if res[shop].get(product) is not None
    }

    if not prices:
        continue

    min_price = min(prices.values())
    winners = [shop for shop, p in prices.items() if p == min_price]

    if len(winners) == 1:
        answer[winners[0]].append(product)

for shop in shops_order:
    print(f'{shop}')
    if answer[shop]:
        print(', '.join(answer[shop]))
    else:
        print('–')
























