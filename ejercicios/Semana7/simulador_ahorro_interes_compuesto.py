# Compound interest savings simulator

MAX_MONTHS = 120

initial_savings = float(input("Ahorro inicial (₡): "))
monthly_contribution = float(input("Aporte mensual (₡): "))
monthly_rate_percent = float(input("Tasa de interés mensual (%): "))
savings_goal = float(input("Meta de ahorro (₡): "))

# Convert percentage (e.g. 1.5) to decimal (0.015)
monthly_rate = monthly_rate_percent / 100
balance = initial_savings
months = 0

while balance < savings_goal and months < MAX_MONTHS:
    balance = balance + balance * monthly_rate
    balance = balance + monthly_contribution
    months = months + 1
    print("Meses de Ahorro:", months)
    print(f"Balance de Ahorro: ₡{balance:.2f}")

if balance >= savings_goal:
    print("Se alcanzó la meta de ahorro en el mes", months)
else:
    shortfall = savings_goal - balance
    print(f"Para alcanzar la meta de ahorro falta: ₡{shortfall:.2f}")

print(f"Balance Final: ₡{balance:.2f}")