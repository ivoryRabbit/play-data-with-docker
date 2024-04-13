package org.example

import org.apache.flink.api.common.eventtime.WatermarkStrategy
import org.apache.flink.api.common.serialization.{DeserializationSchema, SimpleStringSchema}
import org.apache.flink.connector.base.DeliveryGuarantee
import org.apache.flink.connector.kafka.sink.{KafkaRecordSerializationSchema, KafkaSink}
import org.apache.flink.connector.kafka.source.KafkaSource
import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment
import org.apache.flink.table.api.bridge.java.StreamTableEnvironment


object Job {
  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment

    val kafkaSource = KafkaSource.builder()
      .setBootstrapServers("kafka:9092")
      .setTopics("input.flink.dev")
      .setGroupId("flink-consumer-group")
      .setStartingOffsets(OffsetsInitializer.latest())
      .setValueOnlyDeserializer(
        //        new JsonRowDeserializationSchema(false) //[Rating]()
        new SimpleStringSchema()
      )
      .setProperty("enable.auto.commit", "true")
      .setProperty("auto.commit.interval.ms", "1")
      .build()

    val kafkaSink = KafkaSink.builder()
      .setBootstrapServers("kafka:9092")
      .setRecordSerializer(
        KafkaRecordSerializationSchema.builder()
          .setTopic("output.flink.dev")
          .setValueSerializationSchema(new SimpleStringSchema())
          .build()
      )
      .setDeliveryGuarantee(DeliveryGuarantee.AT_LEAST_ONCE)
      .build()

    val streamLines = env.fromSource(kafkaSource, WatermarkStrategy.noWatermarks(), "Kafka Sink")
    streamLines.print()
    streamLines.sinkTo(kafkaSink)

    env.execute("Flink Streaming Scala Example")
  }
}

object Job {
  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    val tableEnv: StreamTableEnvironment = StreamTableEnvironment.create(env)

     tableEnv.executeSql(
       """
         | CREATE TABLE ratings (
         |   user_id INT
         |   movie_id INT
         |   rating FLOAT
         |   timestamp LONG
         | ) WITH (
         |   'connector' = 'kafka',
         |   'topic' = 'input.flink.dev',
         |   'properties.bootstrap.servers' = 'kafka:9094',
         |   'format' = 'json'
         | )
         |""".stripMargin
     )

     tableEnv.executeSql(
       """
         | CREATE TABLE populars (
         |   movie_id INT
         |   rating FLOAT
         | ) WITH (
         |   'connector' = 'kafka',
         |   'topic' = 'output.flink.dev',
         |   'properties.bootstrap.servers' = 'kafka:9094',
         |   'format' = 'json'
         | )
         |""".stripMargin
     )

     tableEnv
       .sqlQuery("SELECT movie_id, avg(rating) AS word FROM ratings GROUP BY movie_id")
       .executeInsert("populars")
       .wait()
  }
}