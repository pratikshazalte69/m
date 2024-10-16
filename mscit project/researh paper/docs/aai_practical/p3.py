P_A = float(input("Enter the Percentage of  patients having liver Disease: ")) 
P_B = float(input("Enter the Percentage of  patients are Alcoholic: ")) 
P_B_Given_A = float(input("Enter the Percentage of  patients who are Alcoholic if they have liver Disease: ")) 
P_A_Given_B = (P_B_Given_A*P_A)/P_B 
print("There are %.2f %% chances that the patients have liver Disease if they have alcoholic"%(P_A_Given_B))
