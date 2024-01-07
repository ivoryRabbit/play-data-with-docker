FROM openjdk:17-jdk-slim

WORKDIR /etc/trino-gateway

RUN apt-get -y update && apt-get -y install curl

ENV VERSION=4

RUN curl https://repo1.maven.org/maven2/io/trino/gateway/gateway-ha/${VERSION}/gateway-ha-${VERSION}-jar-with-dependencies.jar -o gateway-ha.jar