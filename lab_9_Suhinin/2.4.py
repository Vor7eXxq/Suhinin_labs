def calculate_weight_cost(weight):
    if weight < 5:
        return 50
    elif 5 <= weight <=10 :
        return 80
    else:
        return 80+((weight-10)*10)
def calculate_delivery(distance,weight,if_express = False):
    if if_express:
        print(distance*2+calculate_weight_cost(weight))
    else:
       print(distance+calculate_weight_cost(weight))
calculate_delivery(100,14)