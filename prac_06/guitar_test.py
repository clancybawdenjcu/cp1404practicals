from prac_06.guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Air", 1986, 3)
guitar3 = Guitar("Old", 1970, 14.50)  # Test 50 y/o boundary condition for vintage.

print(f"Gibson L-5 CES get_age() - Expected 98. Got {guitar1.get_age()}.")
print(f"Gibson L-5 CES get_age() - Expected True. Got {guitar1.is_vintage()}.")
print(f"Air get_age() - Expected 34. Got {guitar2.get_age()}.")
print(f"Air is_vintage() - Expected False. Got {guitar2.is_vintage()}.")
print(f"Old get_age() - Expected 50. Got {guitar3.get_age()}.")
print(f"Old is_vintage() - Expected True. Got {guitar3.is_vintage()}.")
