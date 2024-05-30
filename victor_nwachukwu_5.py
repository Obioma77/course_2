brands = ["Hermes", "Gucci", "Chanel", "Gucci",
           "Louis Vuitton", "Hermes", "Chanel","hugo boss", 
           "Guess", "Gucci", "Louis Vuitton"]

brand_dict = {}
unique_brands = set(brands)
for brand in unique_brands:
       first_letter = brand[0].upper()
       if first_letter not in brand_dict:
            brand_dict[first_letter] = [brand] 
else:
            brand_dict[first_letter].append(brand)
print(brand_dict)
