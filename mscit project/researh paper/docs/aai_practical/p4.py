Card_Colour= input('Enter the Colour of the card: ') 
Card_Number= input('Enter the Number of the card: ') 
# P(A) is the Probability of drawing a card with entered color 
P_A = 26/52 
# P(B) is the Probability of drawing a card with entered Number 
P_B = 4/52 
print("Probability of drawing a ",Card_Colour,' card is ',round(P_A,2)) 
print("Probability of drawing a card with number ",Card_Colour,' is ',round(P_B,2)) 
P_A_AND_B = round(P_A*P_B,2) 
print("Probability of drawing ", Card_Colour, ' card with the number ', Card_Number, 'from a normal deck of 52 playing card is ', P_A_AND_B)
