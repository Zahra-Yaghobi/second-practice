# Programmer : Zahra Yaghubi
print("Enter the seconds:")
vorodi = int(input('seconds = '))
hour = vorodi // 3600
min = (vorodi - 3600 * hour) // 60
sec = (vorodi - 3600 * hour) - 60 * min
print("Show convert sec - time = ", hour,':', min,':', sec )