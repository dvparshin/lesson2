"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
goods_list = [
      {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
      {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
      {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

def sales(goods_list):
    total_sales_all_products = 0
    total_items_sold_all_products = 0

    for product_value in goods_list:
        product = product_value['product']
        items_sold_value = product_value['items_sold']
        total_sales = sum(items_sold_value)
        print(f"{product}:")
        print(f"  Суммарное количество продаж: {total_sales}")
        avg_product_sales = int(total_sales / len(items_sold_value))
        print(f"  Среднее количество продаж: {avg_product_sales}")
        total_sales_all_products += total_sales
        total_items_sold_all_products += int(len(items_sold_value))
    
    print(f"\nСуммарное количество продаж всех товаров: {total_sales_all_products}")

    average_sales_all_products = int(total_sales_all_products / total_items_sold_all_products)
    print(f"Среднее количество продаж всех товаров: {average_sales_all_products}")

def main():
    result = sales(goods_list)
    
if __name__ == "__main__":
    main()
