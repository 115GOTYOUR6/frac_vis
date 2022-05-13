import matplotlib.pyplot as plt
from fractions import Fraction
import argparse


def plot_colors(frac, col='k'):
    """
    Generate a list of characters representing colors.
    """
    return [col if i < frac.numerator else 'w'
            for i in range(frac.denominator)]


parser = argparse.ArgumentParser(description="Provide a visual representation"
                                 " of the proper fractions passed on the"
                                 " command line.")
parser.add_argument('fraction', type=str,)

parser.add_argument('-color', type=str, default='b',
                    help="The color the segments representing the fractions"
                         " will be. This will be passed straight into"
                         " matplotlib.")
args = parser.parse_args()

frac = Fraction(args.fraction, _normalize=False)
cols = plot_colors(frac, col=args.color)


plt.figure()
plt.pie([1 for i in range(frac.denominator)], colors=cols,
        wedgeprops={"edgecolor": 'k'})
plt.show()
