library(plotrix)
library(genalg)
library(FNN)
x<-c(1,2,3,4,5)
y<-c(5,4,3,2,1)
r<-c(0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5)
colors<-c(1:9)
gridarea=16
circlex<<-c()
circley<<-c()
rectax=c()
exists<<-c()
rectay=c()
rectbx=c()
rectby=c()
rectcx=c()
rectcy=c()
rectx<-c()
recty<-c()
circles<<-data.frame(1:9,2)


areaofintersection<- function (x0, y0, r0, x1, y1, r1){
  rr0 = r0*r0;
  rr1 = r1*r1;
   c = sqrt((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0));
   phi = (acos((rr0+(c*c)-rr1) / (2*r0*c)))*2;
	if((rr0+(c*c)-rr1) / (2*r0*c) < -1 ){
	phi=-1;	
}
	if((rr0+(c*c)-rr1) / (2*r0*c) > 1 ){
	phi=1;	
}

   theta = (acos((rr1+(c*c)-rr0) / (2*r1*c)))*2;
	if((rr1+(c*c)-rr0) / (2*r1*c) < -1 ){
	theta=-1;	
}
	if((rr1+(c*c)-rr0) / (2*r1*c) > 1 ){
	theta=1;	
}

   area1 = 0.5*theta*rr1 - 0.5*rr1*sin(theta);
   area2 = 0.5*phi*rr0 - 0.5*rr0*sin(phi);
  return (area1 + area2)
}



#####################################################################
finalplotcircles<-function(obj){
i=1
#xy=obj$population[length(obj$population[,1]),]
#xy=obj$population[which.min(obj$evaluations),]
small<-which(obj$evaluations == min(obj$evaluations))
xy=obj$population[small[length(small)],]


plot(xy[1:9],xy[10:18],xlim=c(0,10),ylim=c(0,10))

while(i<=9){

circlex<<-c(circlex,xy[i])
circley<<-c(circley,xy[i+9])
draw.circle(xy[i],xy[i+9],r[i],col=colors[i])

i=i+1
points(xy[i],xy[i+9])

rect(1, 1, 3, 3) # transparent
rect(4, 2, 6,4) # transparent
rect(6, 6,8, 8) # transparent
a1=(1+3)/2
b1=(1+3)/2
a2=(4+6)/2
b2=(2+4)/2
a3=(6+8)/2
b3=(6+8)/2
points(a1,b1)
points(a2,b2)
points(a3,b3)
#rectax<-c(rectax,a1)
#rectay<-c(rectay,b1)
#rectbx<-c(rectbx,a2)
#rectby<-c(rectby,b2)
#rectcx<-c(rectcx,a3)
#rectcy<-c(rectcy,b3)
rectx<-c(a1,a2,a3)
recty<-c(b1,b2,b3)
d1<-sqrt((a1-a2)^2+(b1-b2)^2) 


}
circlex<<-c(circlex,a1,a2,a3)
circley<<-c(circley,b1,b2,b3)

circles<<-data.frame(circlex,circley)
print(circles)
knnop<-get.knn(circles,k=11)
print(knnop)
rec=10
while(rec<=12){
i=1
while(i<=3){
index=knnop$nn.index[rec,][i]
k=i

while(index>9 || any(exists==index)){
k=k+1
index=knnop$nn.index[rec,][k]
}
exists<-c(exists,index)
print(index)
####################################################################
j=1
circlex[index]<<-rectx[i]+i/5
circley[index]<<-recty[i]+i/5
plot(circlex,circley,xlim=c(0,10),ylim=c(0,10))
while(j<=9){
draw.circle(circlex[j],circley[j],r[j],col=colors[j])
j=j+1
points(circlex[j],circley[j])
rect(1, 1, 3, 3) # transparent
rect(4, 2, 6,4) # transparent
rect(6, 6,8, 8) # transparent
a1=(1+3)/2
b1=(1+3)/2
a2=(4+6)/2
b2=(2+4)/2
a3=(6+8)/2
b3=(6+8)/2
points(a1,b1)
points(a2,b2)
points(a3,b3)
}
#####################################################################
i=i+1
}
rec=rec+1
}
}

######################################################################






chkintersect<-function(x,y,i){
flag=0

j=1
while(j<=9){
if(i==j){
j=j+1
next
}
if(  sqrt((x[i]-x[j])^2 + (y[i]-y[j])^2) < r[i]+r[j]   ){
flag=flag+areaofintersection(x[i],y[i],r[i],x[j],y[j],r[j])
}
j=j+1
}


return (flag)
}





evalfunc<-function(x){


i=1
totalcirclearea<-0
while(i<=9){
totalcirclearea=totalcirclearea+(3.14*r[i]*r[i])-chkintersect(x[1:9],x[10:18],i)
i<-i+1
coverage <- gridarea-totalcirclearea
}
return (coverage)
}


plotcircles<-function(obj){
i=1
#xy=obj$population[length(obj$population[,1]),]
#xy=obj$population[which.min(obj$evaluations),]
small<-which(obj$evaluations == min(obj$evaluations))
xy=obj$population[small[length(small)],]


plot(xy[1:9],xy[10:18],xlim=c(0,10),ylim=c(0,10))

while(i<=9){
#print("jj")
#print(xy[i])
#print(xy[i+9])
circlex<<-c(circlex,xy[i])
circley<<-c(circley,xy[i+9])
draw.circle(xy[i],xy[i+9],r[i],col=colors[i])

i=i+1
points(xy[i],xy[i+9])

rect(1, 1, 3, 3) # transparent
rect(4, 2, 6,4) # transparent
rect(6, 6,8, 8) # transparent
a1=(1+3)/2
b1=(1+3)/2
a2=(4+6)/2
b2=(2+4)/2
a3=(6+8)/2
b3=(6+8)/2
points(a1,b1)
points(a2,b2)
points(a3,b3)
#rectax<-c(rectax,a1)
#rectay<-c(rectay,b1)
#rectbx<-c(rectbx,a2)
#rectby<-c(rectby,b2)
#rectcx<-c(rectcx,a3)
#rectcy<-c(rectcy,b3)
rectx<-c(a1,a2,a3)
recty<-c(b1,b2,b3)
d1<-sqrt((a1-a2)^2+(b1-b2)^2) 


}

}

rbga.results = rbga(c(rep(1,18)), c(rep(6,18)),monitorFunc=plotcircles,
evalFunc=evalfunc, mutationChance=1,iters=1)
gridarea=16
circlex<<-c()
circley<<-c()
rectax=c()
exists<<-c()
rectay=c()
rectbx=c()
rectby=c()
rectcx=c()
rectcy=c()
rectx<-c()
recty<-c()
circles<<-data.frame(1:9,2)
Sys.sleep(3)
rbga.results = rbga(c(rep(1,18)), c(rep(6,18)),monitorFunc=finalplotcircles,
evalFunc=evalfunc, mutationChance=1,iters=1)

Sys.sleep(3)
rbga.results = rbga(c(1.5,1.5,1.5,4.5,4.5,4.5,6.5,6.5,6.5,1.5,1.5,1.5,2.5,2.5,2.5,6.5,6.5,6.5), c(2.5,2.5,2.5,5.5,5.5,5.5,7.5,7.5,7.5,2.5,2.5,2.5,3.5,3.5,3.5,7.5,7.5,7.5),monitorFunc=plotcircles,
evalFunc=evalfunc, mutationChance=1,iters=10)

