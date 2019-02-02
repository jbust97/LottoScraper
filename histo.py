import matplotlib.pyplot as plt

array = []
with open("datosTrue.txt") as ins:
    for line in ins:
        array.append(int(line))
plt.hist(array)
plt.title("Histograma")
plt.show()
