package org.example

import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment
import org.apache.flink.table.api.bridge.java.StreamTableEnvironment


object TableAPIJob {
  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    val tableEnv: StreamTableEnvironment = StreamTableEnvironment.create(env)

    tableEnv.executeSql(
      """
        | CREATE TABLE ratings (
        |   user_id INT,
        |   movie_id INT,
        |   rating FLOAT,
        |   `timestamp` BIGINT
        | ) WITH (
        |   'connector' = 'kafka',
        |   'topic' = 'input.flink.dev',
        |   'properties.bootstrap.servers' = 'kafka:9092',
        |   'properties.group.id' = 'flink',
        |   'properties.auto.offset.reset' = 'latest',
        |   'format' = 'json'
        | )
        |""".stripMargin
    )

    tableEnv.executeSql(
      """
        | CREATE TABLE ratings_clean (
        |   user_id INT,
        |   movie_id INT,
        |   rating FLOAT,
        |   created_at STRING
        | ) WITH (
        |   'connector' = 'kafka',
        |   'topic' = 'output.flink.dev',
        |   'properties.bootstrap.servers' = 'kafka:9092',
        |   'format' = 'json'
        | )
        |""".stripMargin
    )

    tableEnv
      .executeSql(
        """
          | INSERT INTO ratings_clean
          | SELECT
          |   user_id,
          |   movie_id,
          |   rating,
          |   FROM_UNIXTIME(`timestamp`) AS created_at
          | FROM ratings
          |""".stripMargin
      )
  }
}
