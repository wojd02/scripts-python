tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes',
    },
    'total':[534.50, 20.0, 5]
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

def reserve_table(table_number, name, vip_status=False, table_status = 'RESERVED', table_hour='00:00'):
  tables[table_number]['table_status'] = table_status
  tables[table_number]['table_hour'] = table_hour
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

def remove_table(table_number):
  tables[table_number].clear()

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

def remove_food(table_number):
    tables[table_number]['order']['food_items'] = ''

def remove_drinks(table_number):
    tables[table_number]['order']['drinks'] = ''

def total(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)

def calculate_price_per_person(table_number):
    lista = tables[table_number]['total']
    total(*lista)

reserve_table(3, 'Andy', False, table_hour='21:50')
print(tables)
assign_table(3, 'Andy', False)
print(tables)
remove_table(3)
print(tables)