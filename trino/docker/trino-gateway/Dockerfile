FROM openjdk:17-jdk-slim

WORKDIR /etc/trino-gateway

RUN apt-get -y update && apt-get -y install curl

ARG VERSION
ARG JAR_FILE

RUN curl https://repo1.maven.org/maven2/io/trino/gateway/gateway-ha/${VERSION}/gateway-ha-${VERSION}-jar-with-dependencies.jar -o ${JAR_FILE}