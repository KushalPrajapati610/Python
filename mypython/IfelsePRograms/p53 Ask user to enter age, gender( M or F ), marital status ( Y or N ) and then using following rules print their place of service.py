age = int(input("Enter the age="))
gender = input("Enter the gender(Male/Female)=")
marital = input("Enter the marital status(Yes/No)=")

if gender == 'Female':
    print("she will work only in urban areas")
elif gender == 'Male' and 20 < age < 40:
    print("he may work in anywhere")
elif gender == 'Male' and 40 < age < 60:
    print("he will work in urban areas only")
else:
    print("Sorry")
