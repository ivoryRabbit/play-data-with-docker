# curl -X GET http://localhost:8081/v1/config
# curl -X GET http://localhost:8081/v1/jars
sbt clean assembly

jarId=$(curl -X POST -H "Expect:" -F "jarfile=@./target/scala-2.12/flink-dev-assembly-0.1-SNAPSHOT.jar" http://localhost:8081/v1/jars/upload | sed 's/.*"filename":"\{0,1\}\([^,"]*\)"\{0,1\}.*/\1/' | sed 's/.*\///')
curl -X POST http://localhost:8081/v1/jars/$jarId/run

