import os
import sys
import logic
import networkx as nx
import matplotlib.pyplot as plt
from simple_term_menu import TerminalMenu
a = sys.argv[1]
b = logic.lode_pandemic(a)
nx.draw(b)
plt.savefig("test1.png")
