ThisBuild / resolvers ++= Seq(
  "Apache Development Snapshot Repository" at "https://repository.apache.org/content/repositories/snapshots/",
  Resolver.mavenLocal
)

name := "flink-dev"

ThisBuild / version := "0.1-SNAPSHOT"
ThisBuild / scalaVersion := "2.12.19"
ThisBuild / organization := "ivoryRabbit"

ThisBuild / scalacOptions ++= Seq("-unchecked", "-deprecation")
ThisBuild / scalacOptions ++= Seq("-unchecked", "-feature")

val flinkVersion = "1.18.1"

lazy val root = (project in file("."))
  .settings(
    libraryDependencies ++= Seq(
      "org.apache.flink" %% "flink-scala" % flinkVersion,
      "org.apache.flink" % "flink-streaming-java" % flinkVersion % "provided",
      "org.apache.flink" % "flink-table-api-java" % flinkVersion,
      "org.apache.flink" % "flink-table-api-java-bridge" % flinkVersion % "provided",
      "org.apache.flink" % "flink-table" % flinkVersion % "provided" pomOnly(),
      "org.apache.flink" % "flink-connector-kafka" % "1.17.2" % "provided",
      "org.apache.flink" % "flink-shaded-guava" % "30.1.1-jre-16.1"
    )
  )

assembly / mainClass := Some("org.example.TableAPIJob")
assembly / logLevel := Level.Warn

// make run command include the provided dependencies
Compile / run  := Defaults.runTask(Compile / fullClasspath,
  Compile / run / mainClass,
  Compile / run / runner
).evaluated

// stays inside the sbt console when we press "ctrl-c" while a Flink programme executes with "run" or "runMain"
Compile / run / fork := true
Global / cancelable := true
