f=open('/home/student/Downloads/vehicle.csv','r')
a=f.readlines()
b=[]
b1=[]
for row in a:
	row=row.strip()
	row=row.split(',')
	b.append(row)
	b1.append(row[2])
b1.pop(0)

def avg(x):
	s=0
	for i in x:
		
		a=int(i)
		s+=a	
	return s/len(x)
print("average count of new vehicles sold per month =",round(avg(b1),2))
c=[]
for i in b:
	c.append(i[3])
c.pop(0)
c.sort()
ind=c.index(max(c))
d=[]
e=[]
s=[]
for i in b:
	s.append(i[2])
s.pop(0)
x=max(s)
x1=s.index(x)
s.pop(x1)
y=max(s)
y1=s.index(y)
s.pop(y1)
z=max(s)
z1=s.index(z)
for i in b:
	d.append(i[1])
	e.append(i[0])
d.pop(0)
e.pop(0)
m,n=d[x1],e[x1]
o,p=d[y1],e[y1]
q,r=d[z1],e[z1]
print("the quarter where the sale of old car is maximum is:",x,"in",m,n,";",y,"in",o,p,";",z,"in",q,r)
new=[]
old=[]
for i in b:
	new.append(i[4])
new.pop(0)
for i in b:
	old.append(i[5])
old.pop(0)
yr=[]
l=0
se=list(set(e))
se.sort()

for i in se:
	t=0
	a=e.count(i)
	for j in range(l,l+a):
		t+=(int(new[j])+int(old[j]))
	l=l+a
	yr.append(t)
import matplotlib.pyplot as plt 
  
# x axis values 
x = se
# corresponding y axis values 
y = yr
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('years ') 
# naming the y axis 
plt.ylabel('toatal sales (old+new)') 
  
# giving a title to my graph 
plt.title('graph of sales of old and new cars on yearly basis') 
  
# function to show the plot 
plt.show() 
	
k=e.index('2019')
r=[]
g=[]
h=[]
p=e.count('2019')
for i in range(0,p):
	r.append(b1[k])
	h.append(c[k])
	g.append(d[k])
	k=k+1
#r is the list of new cars sold in 2019 per month
#h is the list of old cars sold in 2019 per month
#g is the list of months in 2019


import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = g
y1 = r 
# plotting the line 1 points  
plt.plot(x1, y1, label = "new cars soled ") 
  
# line 2 points 
x2 = g 
y2 = h 
# plotting the line 2 points  
plt.plot(x2, y2, label = "old cars soled") 
  
# naming the x axis 
plt.xlabel('months os 2019 of sales of cars') 
# naming the y axis 
plt.ylabel('number of cars sold') 
# giving a title to my graph 
plt.title('graph of number of new and old cars sold in months of 2019 ') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show() 
