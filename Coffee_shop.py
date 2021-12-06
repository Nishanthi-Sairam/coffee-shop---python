size = input("enter cup size small , medium , large \n")
if size == "small":
     a=2.00
if size == "medium":
     a=3.00
if size == "large":
     a=4.00

coffee_type = input("enter coffee type brewed coffee , espresso , cold brew \n")
if coffee_type == "brewed coffee":
     b=0.00
if coffee_type == "espresso":
     b=0.15
if coffee_type == "cold brew":
     b=1.00

flavour = input("enter coffee type hazelnut , vanilla , caramel , none \n")
if flavour == "hazelnut":
     c=0.50
if flavour == "vanilla":
     c=0.50
if flavour == "caramel":
     c=0.50  
if flavour == "none":
     c=0.00 

cost = 0.00
cost= sum([a,b,c])

total_cost=(cost*1.15)
 
    
print("you asked for "+size+ " cup of "+coffee_type+ " coffee with "+flavour+ " syrup")

print("your cup of coffee cost "+str(cost))

print("The price with tip is " +str(total_cost))
