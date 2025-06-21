temperature = int(input("Enter the temperature (*C): "))
if temperature >= 40:
    print("Extremely Hot!")
elif temperature < 40 and temperature >=30:
    print("Moderate Weather")
elif temperature < 30 and temperature>=10:
    print("Cold Outside")
else:
    print("Freezing Cold!")