library(plotrix)
library(genalg)
r<-c(2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3)*1.6
gridarea=20*20
mininput<-c(1:40)*0
maxinput<-c(1:40)*0+40

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










chkintersect<-function(x,y,i){
flag=0
j=1

while(j<=length(mininput)/2){

if(i==j){
j=j+1
next
}
print(j)
if(sqrt((x[i]-x[j])^2 +(y[i]-y[j])^2) < r[i]+r[j]   ){
flag=flag+(areaofintersection(x[i],y[i],r[i],x[j],y[j],r[j])*2)
}
j=j+1
}


return (flag)
}





evalfunc<-function(x){
i=1
totalcirclearea<-0
while(i<=length(mininput)/2){
totalcirclearea=totalcirclearea+(3.14*r[i]*r[i])-chkintersect(x[1:20],x[21:40],i)
i<-i+1
coverage <- totalcirclearea
}
return (-coverage)
}


plotcircles<-function(obj){
i=1
#xy=obj$population[length(obj$population[,1]),]
#xy=obj$population[which.min(obj$evaluations),]
small<-which(obj$evaluations == min(obj$evaluations))
xy=obj$population[small[length(small)],]


plot(xy[1:20],xy[21:40],xlim=c(0,40),ylim=c(0,40))

while(i<=length(mininput)/2){

draw.circle(xy[i],xy[i+20],r[i])

i=i+1
}
}




rbga.results = rbga(mininput, maxinput,monitorFunc=plotcircles,
evalFunc=evalfunc, mutationChance=1,iters=100,popSize=50)



