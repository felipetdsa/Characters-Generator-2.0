# Version 2.0
# Accepts any hashable seed
# use integer for compatible with older versions

## PS: Use x = gen(X, Y)
## then print x

import random

def gen(num_char, fixed = False):
    """ Generate random characters
    num_char = number of characters
    fixed = any hashable item (optional) """
    if fixed != False:
        random.seed(fixed)
    pw = ''
    for i in xrange(num_char):
        pw += chr(random.randrange(32, 127))
    return pw
