with open('cats.txt', 'w') as file:
    file.write('Thomas, Varya, Foxya, Miya, Fenya')

with open('dogs.txt', 'w') as file:
    file.write('Cooper, Toby, Jack\n'
               'Molly, Daisy, Sophie\n'
               'Max, Duke')

with open('mice.txt', 'w') as file:
    file.write('Mickey')

with open('films.txt', 'w') as file:
    file.write('Intertstate 60 (2002)\n'
               'Gone Girl (2014)\n'
               'Anna Karenina (2012)')

with open('series.txt', 'w') as file:
    file.write('Planet Earth ||| (2023)')

with open('numbers1.txt', 'w') as file:
    file.write('25 42 37 1 29\n'
               '58 211 5')

with open('numbers2.txt', 'w') as file:
    file.write('4 1 3310 5 7\n'
               '96 412 233 1 0 37 6584 5\n'
               '4 63 87 2 8')

d = {}
lst = []

for i in range(int(input())):
    with open(input()) as file:
        d[file.name] = file.readlines()

for k, v in d.items():
    if k == 'films.txt':
        e = (len(v) - 1) * 2
        for i in v:
            e += int(len(i))
        lst.append([k, e])
    elif len(v) > 1:
        r = len(v) - 1
        for i in v:
            r += int(len(i))
        lst.append([k, r])
    else:
        u = 0
        for i in v:
            u += int(len(i))
        lst.append([k, u])

sor_r = sorted(lst)
res = sorted(sor_r, key=lambda x: int(x[1]), reverse=True)
for i, j in res:
    print(f'{i} {j}B')



























