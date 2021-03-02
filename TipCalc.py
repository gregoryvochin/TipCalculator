#!C:\Users\gvoch\Desktop\TipCalculator\TipCalc.py

"""
TipCalc.py: Used to calculate a 10, 12, or 15 percent portion of a user entered
               float,adding that portion to the initial float and then splitting
               it over an integer provided by the User.
"""

__author__ = "Gregory Vochin"
__maintainer__ = "Gregory Vochin"
__email__ = "gvochin3@gmail.com"
__status__ = "Development"

print("Welcome to the tip calculator.")

totalBill = input("What was the total bill? ")
peoplePaying = input("How many people to split the bill? ")

tipPercentages = {"10": 1.10, "12": 1.12, "15": 1.15}
selectedTip = None

while selectedTip not in tipPercentages:
    selectedTip = input("What percentage tip would you like to give? 10, 12, or 15? ")
    print(f"You have selected {selectedTip}%.")
    if selectedTip in tipPercentages:
        selectedTip = tipPercentages[selectedTip]
        break
    else:
        print("Whoops! Please choose form the provided values.")
        continue

tippedBill = float(totalBill) * float(selectedTip)
roundedTotalBill = round(tippedBill, 2)
print("The total bill is ${:.2f}".format(roundedTotalBill))

splitBill = float(roundedTotalBill) / int(peoplePaying)
roundedSplitBill = round(splitBill, 2)
print("Each patron is due to pay ${:.2f}".format(roundedSplitBill))
