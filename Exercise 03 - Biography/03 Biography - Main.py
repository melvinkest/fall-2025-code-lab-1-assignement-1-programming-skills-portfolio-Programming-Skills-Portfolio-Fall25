#Declaring Variables (Name, Hometown, Age)
name= ('Melvin Kest')
hometown= ('Beira, Mozambique')
age=(18)

biography={
    'Name': name,
    'Hometown': hometown,
    'Age': age
}
#Displaying the users response
for key, value in biography.items():
    print(f"{key}:{value}")