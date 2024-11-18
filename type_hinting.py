# Indication de Type ou Annotation de Type (Type Hinting en Anglais)

#def list_avg(sequence):
    #return sum(sequence) / len(sequence)

my_list = [1,2,3,4,5]
#print(list_avg(my_list))

#print(list_avg(1234))

from typing import List
def list_avg(sequence: List[float]) -> float:
    return sum(sequence) / len(sequence)

#print(list_avg(my_list))

print(list_avg([1.0, 2.5, 5.6]))