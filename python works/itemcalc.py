# def kgcalculaor(x):
#     onionkg = x / 20
#     tomatokg = x / 10.5
#     onion_tomato = 10.5 / (onionkg - x)
#     print("onion:{} Tomato:{} onion & tomato :{}".format(onionkg,tomatokg,onion_tomato))

# kgcalculaor(float(input("Enter the budjet :")))

def kgcalculator(budget):
    # Define the prices of onion and tomato per kilogram
    onion_price_per_kg = 20
    tomato_price_per_kg = 10.5
    
    # Calculate how many kilograms of onion and tomato the customer can buy
    onion_kg = budget / onion_price_per_kg
    tomato_kg = budget / tomato_price_per_kg
    
    # Calculate how many kilograms of onion and tomato combined the customer can buy
    onion_tomato_kg = (budget / onion_price_per_kg) + (budget / tomato_price_per_kg)
    
    # Print the result
    print("Onion: {:.2f} kg Tomato: {:.2f} kg Onion & Tomato: {:.2f} kg".format(onion_kg, tomato_kg, onion_tomato_kg))

budget = float(input("Enter the budget: "))
kgcalculator(budget)
