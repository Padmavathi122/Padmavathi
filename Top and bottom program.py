import pandas as pd
d1 = {
    "name": ['a', 'b', 'c', 'd'],
    "age": [10, 20, 30, 40]
}
d2 = pd.DataFrame(d1)
print(d2)
print(d2.head(1))
print("Top")
print(d2.head(2))
print("bottom")
print(d2.tail(2))