import matplotlib.pyplot as plt
import random
import csv
import numpy as np
import sys


heights = []
for count in range(150):
    heights.append(round(random.uniform(40,90),3))



def basketball_skills(height,m,b):
    skill = round(m*height + b + np.random.normal(loc=0.0, scale=0.5,),3)
    return(skill)




skills = []

####################
# TRUE PARAMS

m = 0.1
b = -0.5

####################


for height in heights:
    skill = basketball_skills(height, m,b)
    skills.append(skill)


heights.append(72)

skills.append(1)



plt.scatter(heights,skills, s=10, color="black")
plt.xlabel("Height (inches)",fontsize=16)
plt.ylabel("Basketball Skills", fontsize=16)

# plt.show()
plt.savefig("example_plot.pdf")

# sys.exit()



f = open('basketball_skills.csv', "w")

f.write("height_inches,basketball_skills\n")

for i in range(len(heights)):
    f.write("%s,%s\n" % (heights[i],skills[i]))

f.close()
