#!/usr/bin/python

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

def getTCO(): 
    return 0

def get_current_cost(t_TCO=100.00, t_units=200.00, t_demand=400):
   print "TCO: $", t_TCO
   print "Total Capacity:",t_units
   print "Total Demand:", t_demand
   unit_cost = ((t_TCO * t_units) / t_demand)
   print "Cost/Unit", unit_cost
   return;

# Now you can call printme function
printme("Your Code has Started to Run")
get_current_cost()