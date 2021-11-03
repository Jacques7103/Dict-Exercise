my_dict = {
    "John": ["BRV", "HRV", "CRV"],
    "David": ["Civic", "CRZ", "Supra"],
    "Wilson": ["Fortuner", "Pajero", "Terra"],
    "Samuel": ["Mitsubishi 3000GT", "Honda S2000", "Nissan Skyline"],
    "Willard": ["Mitsubishi Evo VI", "Honda NSX", "Mazda RX-7"]
}

for key, value in my_dict.items():
    print(key,"likes these cars:")
    for car in value:
        print("- ", car)
    print()