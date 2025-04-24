print("Paramjeetsinh Jadeja")
print("24BEE138")
num_words = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", 
    "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]
num = int(input("Enter a number between 0 and 19: "))
if 0 <= num <= 19:
    print(f"The number {num} in words is: {num_words[num]}")
else:
    print("Please enter a number between 0 and 19.")
