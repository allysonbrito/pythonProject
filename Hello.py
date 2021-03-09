import matplotlib.pyplot as plt
print("Hello World")
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
a = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
b = [10, 15, 10, 5, 100, 20, 30, 10, 4, 5, 9, 10]
print(a)
print(b)
plt.plot(a, b)
plt.xlabel('meses')
plt.ylabel('valores')
plt.title('my first graph in python')
plt.show()

