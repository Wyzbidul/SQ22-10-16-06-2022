#####################################################################################################################################
#	PROGRAM BY : MC IATRIDES
#	LAST UPDATE : 16-06-2022
#	TITLE : SQ22-10 - (16-06-2022)
#   SUBTITLE : Analytic Streamline
#	REDACTED FOR : ADV COURSE ON COMPUTER VISUALIZATION
#####################################################################################################################################

##### PACKAGES ######################################################################################################################
from numpy import *
from matplotlib.pyplot import *
#####################################################################################################################################

###### ANALYSIS PART ################################################################################################################
print('START TESTS')

def f(x,y):
    return (-y,x)

x1 = 1
y1 = 0
X,Y = [],[]
U,V = [],[]

#Calculations have been done by hand
for k in range(4):
    X.append(x1)
    Y.append(y1)
    x2,y2 = f(x1,y1)
    u = x2-x1
    v = y2-y1
    U.append(u)
    V.append(v)
    x1 = x2
    y1 = y2

#Plot Results
figure()
quiver(X,Y,U,V,angles='xy', scale_units='xy', scale=1)
xticks([1,0,-1,0],X)
yticks([0,1,0,-1],Y)
xlim(-1,1)
ylim(-1,1)
grid()
show()

w=2
Y2,X2 = mgrid[-w:w+1,-w:w+1]
U2,V2 = f(X2,Y2)[:][0],f(X2,Y2)[:][1]
seed = array([[1,0]])


figure()
streamplot(X2,Y2,U2,V2,start_points=seed)
xticks([1,0,-1,0],X)
yticks([0,1,0,-1],Y)
xlim(-1,1)
ylim(-1,1)
grid()
show()

print('END TESTS')
#####################################################################################################################################
