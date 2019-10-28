# List
countriesList = ["Spain", "France", "Germany"]
countriesList.append("Italy")
countriesList.remove("France")
countriesList.insert(1, "Japan")

countriesSet = {"Spain", "France", "Germany"}
#Inserted randomly
countriesSet.update(["Italy"])
countriesSet.remove("France")
#Insert in the middle not allowed
print(countriesSet)