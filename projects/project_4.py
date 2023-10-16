
height_decimal = float(input("Enter the height in feet and inches (e.g., 5.7 for 5 feet 7 inches): "))


feet = int(height_decimal)
inches = int((height_decimal - feet) * 10)

print(f"Feet = {feet}, Inches = {inches:.1f}")
