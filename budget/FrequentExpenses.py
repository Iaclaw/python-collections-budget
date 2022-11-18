import matplotlib.pyplot as plt
import collections
from . import Expense

expanses = Expense.Expenses()
expanses.read_expenses('data/spending_data.csv')
spending_categories = []
for expanse in expanses.list:
    spending_categories.append(expanse.category)
spending_counter = collections.Counter(spending_categories)
top5 = spending_counter.most_common(5)
categories, count = zip(*top5)
fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

plt.show()
