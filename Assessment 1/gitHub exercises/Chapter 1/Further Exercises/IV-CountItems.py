#EXERCISE IV: COUNT ITEMS
staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]
staff_dict = {}
for name in staff:
    if name not in staff_dict:
        staff_dict[name] = 1
    else:
        staff_dict[name] += 1

for key, value in staff_dict.items():
    if value > 1:
        print(f"{key} was repeated {value} times!")
    else:
        print(f"{key} was only mentioned once!")