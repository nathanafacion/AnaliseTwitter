
import matplotlib.pyplot as plt 
import createlog 
logger = createlog.logger

class Graph:

    def __init__(self,xlabel, ylabel, title, figurename):
        self.xlabel = xlabel
        self.ylabel = ylabel 
        self.title = title
        self.figurename = figurename

    def plot_graph( self,x,y, color, markerfacecolor, legend, save = False):
        # plotting the points  
        plt.bar(x, y, label= legend,color=color, linestyle='dotted', linewidth = 3) 
        plt.ylim(0, len(y) + 5) 
        plt.xlim(0, len(x) + 5) 
        plt.xlabel(self.xlabel) 
        plt.ylabel(self.ylabel) 
        plt.title(self.title) 
        #plt.show()
        if save == True: 
        	plt.legend()
        	plt.savefig(self.figurename)
        	plt.clf()
        	logger.info('Plot graph:'+self.figurename)