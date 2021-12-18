"""
* Problem: You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
• numberOfBoxesi is the number of boxes of type i.
• numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
Return the maximum total number of units that can be put on the truck.
* Algorithm: Greedy
Sort the array of boxType decreasingly by the number of units per box
Choose maximum number of box for each type in the sorted list
* Time-complexity: O(nlogn) due to sorting the input
* Space-complexity: O(1)
"""

def maximumUnits(boxTypes, truckSize):
    unitCount = 0
    sortedBoxTypes = sorted(boxTypes, key=lambda x: -x[1])
    i = 0
    while i < len(sortedBoxTypes) and truckSize != 0:
        if sortedBoxTypes[i][0] <= truckSize:
            truckSize -= sortedBoxTypes[i][0]
            unitCount += sortedBoxTypes[i][0] * sortedBoxTypes[i][1]
        else:
            unitCount += truckSize * sortedBoxTypes[i][1]
            truckSize = 0
        i += 1
    return unitCount

