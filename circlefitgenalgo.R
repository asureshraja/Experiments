library(plotrix)
library(genalg)
x<-c(1,2,3,4,5)
y<-c(5,4,3,2,1)
r<-c(0.5,0.5,0.75,0.85,0.85)
x
y
r
colors<-c("blue","blue","black","red","red")
gridarea<-3
circles<-5
plotcircles<-function(x,y,r){
i=1
plot(x,y,xlim=c(0,10),ylim=c(0,10))
while(i<=length(x)){
draw.circle(x[i],y[i],r[i],col=colors[i])
i=i+1
}
}
plotcircles(x,y,r)
grid()
iter = 100

gm= rbga(
evalFunc=evalfunc, verbose=TRUE, mutationChance=1)



evalfunc<-function(x,y){
i=1
totalcirclearea=0
while(i<=5){
totalcirclearea=totalcirclearea+(3.14*r[i]*r[i])
i<-i+1
}
coverage<-gridarea-totalcirclearea
return (coverage)
}


plotcircles(x,y,r)
x
y
r