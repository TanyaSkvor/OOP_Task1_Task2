with open('Книга рецептов.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines.insert(0, "")
    cook_book = {}
    for i in range(len(lines)):
        lin_i = lines[i].strip()
        if lin_i == "":
            ingred_num = int(lines[i+2].strip())
            dish_name = lines[i+1].strip()
            list_ingr_for_dict = []
            for g in range (1, ingred_num + 1):
                ingredient_dict = {}
                line_ingr = str(lines[i+2+g].strip())
                ingr_list = line_ingr.split(' | ')
                ingredient_dict["ingredient_name"] = str(ingr_list[0])
                ingredient_dict["quantity"] = str(ingr_list[1])
                ingredient_dict["measure"] = str(ingr_list[2])
                list_ingr_for_dict.append(ingredient_dict)
            cook_book[dish_name] = list_ingr_for_dict

#   Функция для подсчета продуктов
def get_shop_list_by_dishes(dishes, person_count):
    ingred_dict_full = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredient in cook_book[dish]:
                ingred_dict = {}
                ingred = ingredient["ingredient_name"]
                ingred_dict["measure"] = ingredient["measure"]
                ingred_dict["quantity"] = int(ingredient["quantity"]) * person_count
                if ingred in  ingred_dict_full.keys():
                    numb_ingred = ingred_dict_full[ingred]["quantity"]
                    ingred_dict_full[ingred]["quantity"] = numb_ingred + int(ingredient["quantity"]) * person_count
                else:
                    ingred_dict_full[ingred] = ingred_dict
    return ingred_dict_full

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))