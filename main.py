from typing import List, Dict

def creatList(file) -> List:
    '''Создаёт список строк из файла.txt'''
    return list(map(lambda x: x.strip(), file.readlines()))

def creatListPositonBook(listPosition: List) -> List:
    '''Создает список позиций'''
    count = listPosition.count('') + 1
    cook_list = []
    for _ in range(count):
        if '' in listPosition:
            cook_list.append(listPosition[0:listPosition.index('')])
            del listPosition[0:listPosition.index('') + 1]
        else:
            cook_list.append(listPosition[0:])
    return cook_list

def transformIngridient(cook_list: List) -> List:
    '''Проход по списку и преобразование ингридиентов в обычный список'''
    for i in cook_list:
        i[1] = int(i[1])
        for j in i[2:]:
            ls = j.split(' | ')
            i[i.index(j)] = ls
    return cook_list

def creatDictCookBook(cook_list: List) -> Dict:
    '''Создаем итоговый словарь'''
    cook_dict = {}
    for i in cook_list:
        cook_dict[i[0]] = [{'ingredient_name': j, 'quantity': int(n), 'measure': k} for j, n, k in i[2:]]

    return cook_dict

if __name__ == '__main__':
    with open('recipes.txt', 'r+') as f:
        listPosition = creatListPositonBook(creatList(f))
        mainDictCookBook = creatDictCookBook(transformIngridient(listPosition))

    def get_shop_list_by_dishes(dishes: List, person: int) -> Dict:
        dictMain = {}
        #Функция перебора словаря с ингридиентами для конкретного блюда
        def checkDish(dct: Dict, lst: List):
            for l in lst:
                if not dct.get(l['ingredient_name']):
                    dct[l['ingredient_name']] = {'measure': l['measure'], 'quantity': l['quantity']*person}
                else:
                    x = l['quantity']*person
                    dct[l['ingredient_name']]['quantity'] += x

        for dish in dishes:
            for k, v in mainDictCookBook.items():
                if dish == k:
                    checkDish(dictMain, v)
                else: continue

        return dictMain

    menu = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 1)

    #Вывод в читаемой форме итогового словаря
    for keyMenu in menu.keys():
        print(f'{keyMenu}:', end=' ')
        print(menu[keyMenu]['quantity'], menu[keyMenu]['measure'])
