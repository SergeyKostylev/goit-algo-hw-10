import pulp

model = pulp.LpProblem("ProductionOptimization", pulp.LpMaximize)

x = pulp.LpVariable("Lemonade", lowBound=0, cat="Continuous")  # Lemonade amount
y = pulp.LpVariable("FruitJuice", lowBound=0, cat="Continuous")  # FruitJuice amount

# Sources limitation
model += 2 * x + y <= 100, "Water"
model += 1 * x <= 50, "Sugar"
model += 1 * x <= 30, "LemonJuice"
model += 2 * y <= 40, "FruitPuree"

# Goal function (max)
model += x + y, "TotalProducts"
model.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade: {pulp.value(x)}")
print(f"FruitJuice: {pulp.value(y)}")
print(f"Products amount: {pulp.value(model.objective)}")
