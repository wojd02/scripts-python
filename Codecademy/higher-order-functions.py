#High order functions are functions that accept other funtion as argument or returns a value that is a function

#function as a argument
def total_bill(func, price):
    print(func(price))
def tax_bill(price):
    tax = price * 0.07
    new_value = price + tax
    return new_value
def total_bills(func, list):
    new_bills = []
    for i in list:
        bill_w_tax = func(i)
        new_bills.append(bill_w_tax)
    return new_bills

#function as a return
bills = [100, 150, 300, 172]
resp = total_bills(tax_bill, bills)
for c in resp:
    print(f'Total amount owed is {c}.')

def make_box_volume_function(height):
    def volume(width, length):
        return width * length * height
    return volume
box_volume = make_box_volume_function(10)
print(box_volume(3,2))