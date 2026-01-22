"""
MATPLOTLIB CHEAT SHEET – BEGINNER FRIENDLY
-----------------------------------------
Matplotlib is used for plotting and visualizing data.

Core idea:
- You give Matplotlib numbers (lists, NumPy arrays, Pandas Series)
- It draws charts (line, bar, scatter, etc.)

Most common import:
import matplotlib.pyplot as plt
"""

import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------
# 1️⃣ Basic Data for Plotting
# --------------------------------------------------

# x and y should be:
# - same length
# - list, tuple, or NumPy array

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# --------------------------------------------------
# 2️⃣ Basic Line Plot
# --------------------------------------------------

plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# --------------------------------------------------
# 3️⃣ Line Plot with Customization
# --------------------------------------------------

plt.plot(
    x,
    y,
    linestyle="--",   # '-', '--', ':', '-.'
    marker="o",       # o, x, s, ^
    linewidth=2
)
plt.title("Customized Line Plot")
plt.show()

# --------------------------------------------------
# 4️⃣ Using NumPy for Continuous Data
# --------------------------------------------------

# np.linspace(start, stop, number_of_points)
x_np = np.linspace(0, 10, 100)
y_np = np.sin(x_np)

plt.plot(x_np, y_np)
plt.title("Sine Wave")
plt.show()

# --------------------------------------------------
# 5️⃣ Scatter Plot
# --------------------------------------------------

# Best for showing relationship between points
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# --------------------------------------------------
# 6️⃣ Bar Chart
# --------------------------------------------------

# Categories + values
categories = ["A", "B", "C", "D"]
values = [5, 7, 3, 8]

plt.bar(categories, values)
plt.title("Bar Chart Example")
plt.show()

# --------------------------------------------------
# 7️⃣ Horizontal Bar Chart
# --------------------------------------------------

plt.barh(categories, values)
plt.title("Horizontal Bar Chart")
plt.show()

# --------------------------------------------------
# 8️⃣ Histogram
# --------------------------------------------------

# Used to show distribution
data = np.random.randn(1000)  # 1000 random values

plt.hist(data, bins=30)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# --------------------------------------------------
# 9️⃣ Multiple Lines in One Plot
# --------------------------------------------------

y2 = [v * 1.5 for v in y]

plt.plot(x, y, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.legend()
plt.title("Multiple Lines")
plt.show()

# --------------------------------------------------
# 🔟 Subplots (Multiple Charts in One Figure)
# --------------------------------------------------

# 2 rows, 1 column
fig, ax = plt.subplots(2, 1)

ax[0].plot(x, y)
ax[0].set_title("Top Plot")

ax[1].plot(x, y2)
ax[1].set_title("Bottom Plot")

plt.tight_layout()
plt.show()

# --------------------------------------------------
# 11 Pie Chart
# --------------------------------------------------

"""
Pie charts are used to show proportions (parts of a whole).

Inputs:
- sizes: list or array of numbers (values)
- labels: names for each slice (same length as sizes)
"""

labels = ["Apples", "Bananas", "Cherries", "Dates"]
sizes = [40, 25, 20, 15]   # must add up to 100 (recommended, not required)

plt.figure(figsize=(6, 6))

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",   # show percentage on slices
    startangle=90        # rotate chart for better look
)

plt.title("Fruit Distribution")
plt.axis("equal")        # makes the pie a perfect circle
plt.show()


# --------------------------------------------------
# 1️⃣1️⃣ Figure Size
# --------------------------------------------------

plt.figure(figsize=(8, 4))  # width, height in inches
plt.plot(x, y)
plt.title("Custom Figure Size")
plt.show()

# --------------------------------------------------
# 1️⃣2️⃣ Grid
# --------------------------------------------------

plt.plot(x, y)
plt.grid(True)
plt.title("Plot with Grid")
plt.show()

# --------------------------------------------------
# 1️⃣3️⃣ Save Plot to File
# --------------------------------------------------

plt.plot(x, y)
plt.title("Saved Plot")
plt.savefig("my_plot.png")  # saves to current folder
plt.close()

# --------------------------------------------------
# ✅ QUICK REFERENCE
# --------------------------------------------------
"""
plt.plot(x, y)          → line plot
plt.scatter(x, y)       → scatter plot
plt.bar(x, y)           → bar chart
plt.hist(data)          → histogram
plt.title("title")      → chart title
plt.xlabel("x label")   → x-axis label
plt.ylabel("y label")   → y-axis label
plt.legend()            → show legend
plt.grid(True)          → grid on
plt.show()              → display plot
plt.savefig("file.png") → save plot
"""

print("--- End of Matplotlib Cheat Sheet ---")
