
basic_salary = 12000

hra = 0.09 * basic_salary

pf = 0.12 * basic_salary

da = 1.25 * basic_salary

incentives = 0.10 * basic_salary

net_salary = (basic_salary + da + incentives) - (hra + pf)

print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("PF:", pf)
print("DA:", da)
print("Other Incentives:", incentives)
print("Net Salary:", net_salary)
