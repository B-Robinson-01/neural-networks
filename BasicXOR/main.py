# Exploring a very simple setup of the XOR solution using my own intuition
# <--Inputs are not modified using a linear regression so results are not 100% accurate-->

# This class is a simple declaration of a node 
#  in my XOR network
class Node:
    def __init__(self, bias):
        self.bias = bias
        self.value = 0
    
    def UnitValue(self, x1, x2, w1, w2):
        self.value += (x1 * w1) + (x2 * w2) + self.bias

    def getValue(self):
        return self.value

# Get input from user
x1 = int(input("Please input the first value (0,1): "))
x2 = int(input("Please input the second value (0,1): "))

# Create hidden nodes
h1 = Node(0)
h2 = Node(-1)

# Create final Node
y1 = Node(0)

# Calculate the values of each 
h1.UnitValue(x1, x2, 1, 1)
h2.UnitValue(x1, x2, 1, 1)
y1.UnitValue(h1.getValue(), h2.getValue(), 1, -2)

# Output result
print(y1.getValue())