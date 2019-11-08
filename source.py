from timeit import Timer
class Car():
    def __init__(self, the_model, available_qty, sold_qty):
        self.the_model = the_model
        self.available_qty = available_qty
        self.sold_qty = sold_qty

car1 = Car(the_model = "Nissan", available_qty=45,sold_qty= 25)
car2 = Car(the_model="Toyota", available_qty = 25,sold_qty= 40)
car3 = Car(the_model="BMW", available_qty=50,sold_qty=70)

def list_structure():
    data = []
    data.append(car1)
    data.append(car2)
    data.append(car3)

    output = 0

    for item in data:
        if item.the_model == "BMW":
            output = item.sold_qty
            break
    #print(output)

list_structure()

def dict_structure():
    data = {}
    data[car1.the_model] = car1
    data[car2.the_model] = car2
    data[car3.the_model] = car3

    output = data["BMW"].sold_qty
    #print(output)

dict_structure()

t1 = Timer("""list_structure()""", """from __main__ import list_structure""")
t2 = Timer("""dict_structure()""", """from __main__ import dict_structure""")

print(t1.timeit(10000))
print(t2.timeit(10000))

