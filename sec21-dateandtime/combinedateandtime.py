from datetime import *

# Create datetime by combining date and time

# One date
d = date(2018,7,21)

# One time
t = time(12,45)

# Combine date and time
dt = datetime.combine(d, t)
print(dt)