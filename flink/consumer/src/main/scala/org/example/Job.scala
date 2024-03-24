package org.example

import org.apache.flink.streaming.api.scala.StreamExecutionEnvironment
import org.apache.flink.table.api.bridge.scala.StreamTableEnvironment

object Job {

  def main(args: Array[String]): Unit = {

    val env = StreamExecutionEnvironment.getExecutionEnvironment
    val tableEnv = StreamTableEnvironment.create(env)

    tableEnv.executeSql(
      """
        | CREATE TABLE source (
        |   word VARCHAR
        | ) WITH (
        |   'connector' = 'kafka',
        |   'topic' = 'input.flink.dev',
        |   'properties.bootstrap.servers' = 'kafka:9094',
        |   'format' = 'json''
        | )
        |""".stripMargin
    )

    tableEnv.executeSql(
      """
        | CREATE TABLE sink (
        |   word VARCHAR
        | ) WITH (
        |   'connector' = 'kafka',
        |   'topic' = 'output.flink.dev',
        |   'properties.bootstrap.servers' = 'kafka:9094',
        |   'format' = 'json''
        | )
        |""".stripMargin
    )

    tableEnv
      .sqlQuery("SELECT lower(word) AS word FROM source")
      .executeInsert("sink")
      .wait()
  }
}
