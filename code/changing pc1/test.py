import matplotlib.pyplot as plt 

val1 = ["{:d}".format(i) for i in range(10)] 
val2 = ["Stayed C1", "Stayed C2", "Left Market", "Searching", "All Agents", "Houses C1", "Houses C2", "Ratio left", "Ratio C1", "Ratio C2", "W. Time T.", "W. Time C1", "W. Time C2"] 
val3 = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]] 
   
fig, ax = plt.subplots() 
ax.set_axis_off() 
table = ax.table( 
    cellText = val3,  
    rowLabels = val2,  
    colLabels = val1, 
    rowColours =["skyblue"] * 13,  
    colColours =["skyblue"] * 13, 
    cellLoc ='center',  
    loc ='upper left')         
   
ax.set_title("Average waiting times after 2000 iterations over λC1 in C2 \n λTenants = " , 
             fontweight ="bold") 

plt.show()