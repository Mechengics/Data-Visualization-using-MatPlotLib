#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline #First execute this statement.')


# In[2]:


#Data visualization will done this series with the help of matplotlib library.


# In[13]:


#first import the matplot library:
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[14]:


data1=np.arange(10)
data1


# In[15]:


#in order to use the matplot library 
plt.plot(data1)


# In[16]:


#The in built seaborn and pandas built in library will deal with many mundane details of making plots, but if you have to advanced plotting with minor details highlighted matplotlib is more preffered.


# In[24]:


#lets create a scatter plot from this.
x_data1=np.random.random(1000)
y_data1=np.random.random(1000)
#to plot the scatter diagram you can use the command
plt.scatter(x_data1,y_data1, c="red", marker="*", s=150, alpha=0.3)
#adjust the color using c 
#adjust the marker using marker
#adjust the size using s
#since the data is too much, so there are overlapping
#you use the transparency using the alpha. Those that have overlapped will seem darker in his case.


# In[30]:


#Plotting Lines:
#you want to see your progress in life in years than you can use the concept
years=[2010+x for x in range(8)]
lifeon=[1,2,1,3,0,2,0,1]
plt.plot(years, lifeon, c="g", lw=3, linestyle="--")
#c specifies for color
#lw specifies for the line width
#linestyle means the type of the line that you want to have
#this process can also be simply done as
plt.plot(years, lifeon, "g--")


# In[31]:


#you can see the line graph in this case. This is a line chart where the points are interconnected.
#next thing you can observe is what is written first in plt.plot(x,y) is considered as x and the second specification is the y.


# In[38]:


#Bar Plots:
x=["python", "c++","java","Go"]
y=[100,50,40,1]
plt.bar(x,y, color="g", align="edge", width=0.3, edgecolor="red", lw=6)
#align indicates where text indicating each bar is placed in the bar graph below it is placed in the edge of the bar.
#width indicates the maximum width the bar can have
#edge color indicates the color that is present at the edge of the bar graph
#line width indicates the maximum width of the given line.


# In[39]:


#histograms looks like a bargraph but the difference is that histogram doesnot have spaces, its a different way of data representtion.


# In[55]:


#Histogram
data3=np.random.normal(20, 1.5, 1000) # this means the mean of the given data is 20, its standard deviation is 1.5 and the total number of points here is 100
plt.hist(data3, color='r', lw=4, edgecolor='g', bins=100)


# In[59]:


plt.hist(data3, color='r', lw=4, edgecolor='g', bins=100, cumulative=True)


# In[60]:


#You can also specify the range of the bins
#in this method you can use
# bins=data1.min(), 18, 21, data1.max()


# In[63]:


plt.pie(y, labels=x)


# In[73]:


#want to pick some data a little bit out
x=["python", "c++","java","Go"]
y=[100,50,40,1]
explodes=[0,0,0,0.5]
plt.pie(y, labels=x, explode=explodes, autopct="%.2f", pctdistance=1.3, startangle=90)
#explodes: gets a certain segment out of the pie chart, it brings that segment out highlights it kind of
#autopct: this specifies to calculate the percentage by itself, .2f at last of the text mentions that the percentage should maximum contain 2 decimal places
#pctdistance: this helps to spread the text from the centre. 
#startangel: the data starts from 90 degrees.


# In[76]:


#Boxplots: 
heights=np.random.normal(172, 8, 308)
print(heights)


# In[78]:


plt.boxplot(heights)


# In[32]:


#Plot Customization:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
years=[2010+x for x in range(8)]
lifeon=[1,2,1,3,0,2,0,1]
plt.plot(years, lifeon)
#Want to set the title of the function than we can continue as 
plt.title("Life Graph", fontsize=20)
#You can also put the x axis labels and y axis labels. 
plt.xlabel("Years")
plt.ylabel("Score")
#You want to add the yrs in the numerical data, for this you can continue as
plt.xticks(years, [f'{x} yrs' for x in years])
#wrting another line graph with different data will present you the line graph in the same field.
years2=[2013+x for x in range(8)]
lifeon2=[1,2,1,4,0,2,0,2]
plt.plot(years,lifeon2)
#you can also specify legend to the plot. You can do this using the command
plt.legend(["Person1","Person2"], loc="upper right")


# In[56]:


#we can also use different style for example say gg plot.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")#can also try gg plot.
years=[2010+x for x in range(8)]
lifeon=[1,2,1,3,0,2,0,1]
plt.plot(years, lifeon, color='green')
#Want to set the title of the function than we can continue as 
plt.title("Life Graph", fontsize=20, color="blue")
#You can also put the x axis labels and y axis labels. 
plt.xlabel("Years")
plt.ylabel("Score")
#You want to add the yrs in the numerical data, for this you can continue as
plt.xticks(years, [f'{x} yrs' for x in years], color="white")
#wrting another line graph with different data will present you the line graph in the same field.
years2=[2013+x for x in range(8)]
lifeon2=[1,2,1,4,0,2,0,2]
plt.plot(years,lifeon2, color="red")
#you can also specify legend to the plot. You can do this using the command
plt.legend(["Person1","Person2"], loc="upper right")


# In[57]:


#you can create your own customized style sheet. You can view the documentation of matplot lib.


# In[76]:


#Sometimes you want different figures in the same window. 
#for this you can use the subplots in the code
x=np.arange(100)
fig, axis=plt.subplots(2,2)
axis[0,0].plot(x, np.sin(x))#sinx function
axis[0,0].set_title("Sine Curve")
axis[0,1].plot(x, np.cos(x))#cosx function
axis[0,1].set_title("Cos Curve")
axis[1,0].plot(x, np.arange(100))#tanx function
axis[1,0].set_title("Line")
axis[1,1].plot(x, np.tan(x))#cosec function
axis[1,1].set_title("tan")
plt.tight_layout()#this removes the overlapping of the data.
#how can we export these functions. 
plt.savefig("output", dpi=300)#dpi for the quality of the picture. 


# In[79]:


#Now we move into 3 d plot and animations
axis1=plt.axes(projection="3d")
x=np.random.rand(100)
y=np.random.rand(100)
z=np.random.rand(100)
axis1.scatter(x,y,z)


# In[81]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")
axis1=plt.axes(projection="3d")
x=np.arange(-4,4,0.1)
y=np.arange(-4,4,0.1)
X,Y= np.meshgrid(x,y)
Z=np.cos(X)*np.sin(Y)
axis1.plot_surface(X,Y,Z, cmap="Spectral")#spectral is used to define the color.
plt.show()


# In[ ]:


#Want to create some cool looking animation
#Animation. 
import numpy as np 
import random 
import matplotlib.pyplot as plt 
from matplotlib import style
head_tails=[0,0]
for _ in range(1000):
    head_tails[random.randint(0,1)]+=1
    plt.bar(["Heads", "Tails"], head_tails, color=["red","blue"])
    plt.pause(0.001)
plt.show() #operate this in vs code.


# In[ ]:


#Thanks for today, we will be learning the matplot lib when the time demands. The basics of this will be enough for now
#Regards 
#Mechengics

