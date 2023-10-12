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
                ingr_list = line_ingr.split('|')
                ingredient_dict["ingredient_name"] = str(ingr_list[0])
                ingredient_dict["quantity"] = str(ingr_list[1])
                ingredient_dict["measure"] = str(ingr_list[2])
                list_ingr_for_dict.append(ingredient_dict)
            cook_book[dish_name] = list_ingr_for_dict
    print(cook_book)