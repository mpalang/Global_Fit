
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit
from string import ascii_lowercase as alphabet
alphabet=list(alphabet)



class Global_Fit:
    
    def __init__(self,x,y,f,p0=None,plot=True,**p):
        
        self.x=x
        self.y=y
        self.f=f
        self.p0=p0
        
        self.p=p
        
        self.fit()
        
        
        if plot:
            self.plot()
            
#######Functions#######            
            
    def fit(self):
                   
        self.popt, self.pcov = curve_fit(self.f, self.x, self.y,p0=self.p0,**self.p)
            

    def plot(self):
        
        smallticks={"length":5,
               "width":2,
               "which": "minor",
               "direction": "in"
               }

        bigticks={"length":10,
               "width":2,
               "labelsize":12,
               "which": "major",
               "direction": "in"}

        Params={
            'lines.linewidth': 5,
            'lines.markersize': 1.5,
            'font.size': 12,
            'axes.linewidth':2,
            'axes.titlepad':20,  
            'axes.titlesize':5,
            'xtick.major.pad': 8,
            'ytick.major.pad': 8
            }
        
        residuum=plt.Figure()
        plt.scatter(self.x,self.f(self.x,*self.popt)-self.y)
        plt.ylim([-1,1])
        plt.show()
        
        
        result=plt.Figure()
        plt.plot(self.x, self.f(self.x,*self.popt),color='r',zorder=0)
        plt.scatter(self.x,self.y,edgecolors='k',facecolors='none',s=12,linewidths=0.8,zorder=1)
        title=''
        for n,i in enumerate(self.popt):
            title+=alphabet[n]+'='+str(round(i,2))+', '
        plt.title(title)
        plt.show()
        
    
        
    
    # y = [y]
    
    # def f(x, a, b):
    #     return 1/(1+x)
    
    # # single fits to each dataset
    # for y_i in y:
    #     popt, pcov = curve_fit(f, x, y_i)
    #     plt.plot(x, y_i, linestyle="", marker="x")
    #     plt.plot(x, f(x, *popt), color=plt.gca().lines[-1].get_color())
    
    # # global fit to concatenated dataset
    # popt, pcov = curve_fit(lambda x, a, b: np.tile(f(x, a, b), len(y)), x, y.ravel())
    # plt.plot(x, f(x, *popt), linestyle="--", color="black")
    
    # plt.show()
