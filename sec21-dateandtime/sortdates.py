from datetime import date

# Mocked list of dates
ldates = []

d1=date(2019,7,21)
d2=date(2015,7,21)
d3=date(2016,7,21)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

# Sort dates
ldates.sort()

# Result
for d in ldates:
    print(d)