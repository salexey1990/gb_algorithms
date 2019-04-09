import functools

company_count = int(input('count: '))
companies = {}
for i in range(company_count):
  company_name = input('name: ')
  company_profit = input('profit: ')
  companies[company_name] = {
    'profit': list(map(lambda x : int(x), company_profit.split(',')))
  }

total_average = 0

for key, value in companies.items():
  company_total = functools.reduce(lambda res, x : res + x, value['profit'], 0)
  company_average = company_total / len(value['profit'])
  companies[key] = {
    'average': company_average
  }
  total_average = total_average + company_average

average = total_average / 4

less = []
gte = []

for key, value in companies.items():
  if value['average'] > average:
    gte.append(key)
  else:
    less.append(key)

print(less, gte)