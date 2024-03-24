// package org.example

// import java.util.concurrent.TimeUnit

// import org.apache.flink.api.scala._
// import org.apache.flink.streaming.api.scala.StreamExecutionEnvironment
// import org.apache.flink.streaming.api.windowing.time.Time
// import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer.{FetcherType, OffsetStore}
// import org.apache.flink.streaming.connectors.kafka.{FlinkKafkaConsumer, FlinkKafkaProducer}
// import org.apache.flink.streaming.util.serialization.{DeserializationSchema, SerializationSchema}
// import org.apache.flink.streaming.api.scala.DataStream
// import org.apache.flink.streaming.api.windowing.time.Time


// object KafkaExample {

//   type WordCount = (String, Int)

//   def countWords(lines: DataStream[String], stopWords: Set[String], window: Time): DataStream[WordCount] = {
//     lines
//       .flatMap(line => line.split(" "))
//       .filter(word => !word.isEmpty)
//       .map(word => word.toLowerCase)
//       .filter(word => !stopWords.contains(word))
//       .map(word => (word, 1))
//       .keyBy(0)
//       .timeWindow(window)
//       .sum(1)
//   }

//   val stopWords = Set("a", "an", "the")
//   val window = Time.of(10, TimeUnit.SECONDS)

//   def main(args: Array[String]): Unit = {
//     val env = StreamExecutionEnvironment.createLocalEnvironment()

//     val kafkaConsumerProperties = Map(
//       "group.id" -> "flink",
//       "bootstrap.servers" -> "localhost:9094"
//     )

//     val kafkaConsumer = new FlinkKafkaConsumer[String](
//       "input",
//       KafkaStringSchema,
//       kafkaConsumerProperties,
//     )

//     val kafkaProducer = new FlinkKafkaProducer[String](
//       "localhost:9094",
//       "output",
//       KafkaStringSchema
//     )

//     val lines = env.addSource(kafkaConsumer)

//     val wordCounts = countWords(lines, stopWords, window)

//     wordCounts
//       .map(_.toString)
//       .addSink(kafkaProducer)

//     env.execute()
//   }

//   implicit def map2Properties(map: Map[String, String]): java.util.Properties = {
//     (new java.util.Properties /: map) { case (props, (k, v)) => props.put(k, v); props }
//   }

//   object KafkaStringSchema extends SerializationSchema[String, Array[Byte]] with DeserializationSchema[String] {

//     import org.apache.flink.api.common.typeinfo.TypeInformation
//     import org.apache.flink.api.java.typeutils.TypeExtractor

//     override def serialize(t: String): Array[Byte] = t.getBytes("UTF-8")

//     override def isEndOfStream(t: String): Boolean = false

//     override def deserialize(bytes: Array[Byte]): String = new String(bytes, "UTF-8")

//     override def getProducedType: TypeInformation[String] = TypeExtractor.getForClass(classOf[String])
//   }

// }