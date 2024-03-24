# curl -X GET http://localhost:8081/v1/config
# curl -X GET http://localhost:8081/v1/jars
sbt clean assembly
curl -X POST http://localhost:8081/v1/jars/upload -H "Expect:" -F "jarfile=@./target/scala-2.12/flink-dev-assembly-0.1-SNAPSHOT.jar"