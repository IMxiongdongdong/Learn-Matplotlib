import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)
# plt.title("Square numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of value", fontsize=14)
# plt.tick_params(axis='both',which='major', labelsize=14)
# plt.show()

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=100)
# plt.show()

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
plt.axis([0, 1100, 0, 1100000])
plt.savefig('scatter_test.png', bbox_inches='tight')