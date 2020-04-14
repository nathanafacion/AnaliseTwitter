
import matplotlib.pyplot as plt 

class Graph:

    def __init__(self,xlabel, ylabel, title, figurename):
        self.xlabel = xlabel
        self.ylabel = ylabel 
        self.title = title
        self.figurename = figurename

    def plot_graph( self,x,y, color, markerfacecolor, legend, save = False):
        # plotting the points  
        plt.plot(x, y, label= legend,color=color, linestyle='dashed', linewidth = 3, marker='o', markerfacecolor=markerfacecolor, markersize=12) 
        plt.ylim(1, len(y) + 5) 
        plt.xlim(1, len(x) + 5) 
        plt.xlabel(self.xlabel) 
        plt.ylabel(self.ylabel) 
        plt.title(self.title) 
        #plt.show()
        if save == True: 
        	plt.legend()
        	plt.savefig(self.figurename)
        	plt.clf()