# Author: Jay Oliver
# Date Created: 13/05/2022
# Date Last Modified: 14/05/2022
# Purpose: Visualisation of fractions
# Comments:

import argparse
import matplotlib.pyplot as plt
from fractions import Fraction

import frac_plot


parser = argparse.ArgumentParser(description="Provide a visual representation"
                                 " of the proper fractions passed on the"
                                 " command line.")
parser.add_argument('fraction', type=str,
                    help="The fraction to create a visual for. Eg: '3/4'.")

parser.add_argument('-color', type=str, default='b',
                    help="The color the segments representing the fractions"
                         " will be. This will be passed straight into"
                         " matplotlib.")
args = parser.parse_args()

frac = Fraction(args.fraction, _normalize=False)

fig = frac_plot.pie_plot(frac, args.color)
plt.show()
