library(tree)
library(randomForest)

Starbucks = read.csv("Starbucks.csv", header=TRUE)

set.seed(1)
train = sample(1:nrow(Starbucks, nrow(Starbucks)/2))
tree.starbucks = tree(avg_stars~.-starbucks_business_id, Starbucks, subset=train)
bag.starbucks = randomForest(avg_stars~.-starbucks_business_id, data=Starbucks, subset=train, mtry=13, importance=TRUE)

