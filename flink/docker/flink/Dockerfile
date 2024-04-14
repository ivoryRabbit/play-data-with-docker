FROM flink:1.18.1-scala_2.12-java11

ENV FLINK_VERSION=1.18.1
ENV FLINK_CONNECTOR_VERSION=1.17.2
ENV KAFKA_VERSION=3.4.1

RUN curl -L https://repo1.maven.org/maven2/org/apache/flink/flink-streaming-java/${FLINK_VERSION}/flink-streaming-java-${FLINK_VERSION}.jar \
    -o ${FLINK_HOME}/lib/flink-streaming-java-${FLINK_VERSION}.jar
RUN curl -L https://repo1.maven.org/maven2/org/apache/flink/flink-connector-kafka/${FLINK_CONNECTOR_VERSION}/flink-connector-kafka-${FLINK_CONNECTOR_VERSION}.jar \
    -o ${FLINK_HOME}/lib/flink-connector-kafka-${FLINK_CONNECTOR_VERSION}.jar
RUN curl -L https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/${KAFKA_VERSION}/kafka-clients-${KAFKA_VERSION}.jar \
    -o ${FLINK_HOME}/lib/kafka-clients-${KAFKA_VERSION}.jar
RUN curl -L https://repo1.maven.org/maven2/org/apache/flink/flink-shaded-guava/30.1.1-jre-16.1/flink-shaded-guava-30.1.1-jre-16.1.jar \
    -o ${FLINK_HOME}/lib/flink-shaded-guava-30.1.1-jre-16.1.jar
