package org.example

import org.apache.flink.api.common.eventtime.WatermarkStrategy
import org.apache.flink.api.common.serialization.SimpleStringSchema
import org.apache.flink.connector.base.DeliveryGuarantee
import org.apache.flink.connector.kafka.sink.{KafkaRecordSerializationSchema, KafkaSink}
import org.apache.flink.connector.kafka.source.KafkaSource
import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment


object Job {
  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment

    val kafkaSource = KafkaSource.builder()
      .setBootstrapServers("kafka:9092")
      .setTopics("input.flink.dev")
      .setGroupId("flink-consumer-group")
      .setStartingOffsets(OffsetsInitializer.latest())
      .setValueOnlyDeserializer(
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
