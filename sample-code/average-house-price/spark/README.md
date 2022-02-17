brew install scala@2.12
brew install sbt


sbt package


spark-submit --master local target/scala-2.12/avgprice_2.12-0.1.jar