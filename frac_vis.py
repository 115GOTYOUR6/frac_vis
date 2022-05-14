# Author: Jay Oliver
# Date Created: 14/05/2022
# Date Last Modified: 14/05/2022
# Purpose: Contains functions for plotting visualisations of fractions
# Comments:

import matplotlib.pyplot as plt
from fractions import Fraction
from math import ceil
from math import floor


def plot_colors(frac, col='k'):
    """
    Generate a list of colors representing the coloring of sections of a pie
    chart given the proper fraction.

    Input:
        - frac: a python fractions object. This must be a proper fraction!
        - col: a valid matplotlib color.
    Return:
        - list of matplotlib colors.
    Raise:
        None
    """
    return [col if i < frac.numerator else 'w'
            for i in range(frac.denominator)]


def pie_plot(frac, col):
    """
    Return a matplotlib object for a pie plot representing the given fraction.

    Input:
        - frac: A python Fraction object. Can be proper or improper.
        - col: a valid matplotlib color.
    Return:
        - fig: The matplotlib figure containing the plot(s)
    Raises:
        None
    """
    if frac.numerator == 0:
        n_sub = 1
    else:
        n_sub = ceil(frac)
    fig, ax = plt.subplots(n_sub)

    if n_sub == 1:
        colrs = plot_colors(frac, col=col)
        ax.pie([1 for j in range(frac.denominator)],
               colors=colrs, startangle=90,
               wedgeprops={"edgecolor": 'k'})
    else:
        for i in range(n_sub):
            if i < n_sub - 1:
                colrs = plot_colors(Fraction(frac.denominator,
                                             frac.denominator,
                                             _normalize=False), col=col)
            else:
                colrs = plot_colors(Fraction(frac.numerator
                                             - frac.denominator*floor(frac),
                                             frac.denominator,
                                             _normalize=False),
                                    col=col)

            ax[i].pie([1 for j in range(frac.denominator)],
                      colors=colrs, startangle=90,
                      wedgeprops={"edgecolor": 'k'})

    return fig
