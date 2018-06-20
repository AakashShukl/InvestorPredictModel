setwd("C:\\Users\\AAKASH\\Desktop\\Machine Learning A-Z\\Part 2 - Regression\\Section 5 - Multiple Linear Regression")
getwd()
dataset=read.csv('50_Startups.csv')

#Encoding
dataset$State=factor(dataset$State,levels=c("New York","California","Florida"),labels = c(1,2,3))


library(caTools)
set.seed(123)
split=sample.split(dataset$Profit,SplitRatio = 0.8)
trainingset=subset(dataset,split==TRUE)
testset=subset(dataset,split==FALSE)

regressor=lm(formula = Profit~.,data = trainingset)
y_pred=predict(regressor,newdata = testset)

summary(regressor)
#Backward Elimination

regressor=lm(formula = Profit~R.D.Spend+Administration+Marketing.Spend+State,data=trainingset)
y_pred1=predict(regressor,newdata = testset)
summary(regressor)

regressor=lm(formula = Profit~R.D.Spend,data=trainingset)
y_pred2=predict(regressor,newdata = testset)
