# Write code below 💖

class city:
    def __init__(self,name,country,population,landmarks,mayor,founding_year):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks
        self.mayor = mayor
        self.founding_year = founding_year

LA = city('Los Angeles','United States', 40000000,['Venice Beach','Long Beach','Huntington Beach'], 'Karon Bass', 1781)
LV = city('Las Vegas', 'United States',2000000, ['MGM','Caesars Palace'], 'Shelley Berkley',1911)

print(vars(LA))
print(vars(LV))
