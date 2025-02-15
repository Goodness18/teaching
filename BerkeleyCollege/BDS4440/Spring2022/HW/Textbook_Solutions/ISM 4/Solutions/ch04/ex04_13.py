# Exercise 4.13

def product(*args):
    """Calculate product of the arguments."""
    if len(args) == 0:
        return 0

    product = 1
    
    for arg in args:
        product *= arg
        
    return product

product()

product(1)

product(1, 2, 3)

product(1, 2, 3)

product(1, 2, 3, 4, 5)

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
