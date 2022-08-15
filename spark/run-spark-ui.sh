LOG_DIR="s3://your-bucket/uri-prefix"
PROFILE_NAME="default"

docker run -itd -v ~/.aws:/root/.aws \
 -e AWS_PROFILE=$PROFILE_NAME \
 -e SPARK_HISTORY_OPTS="$SPARK_HISTORY_OPTS -Dspark.history.fs.logDirectory=$LOG_DIR  -Dspark.hadoop.fs.s3a.aws.credentials.provider=com.amazonaws.auth.DefaultAWSCredentialsProviderChain" \
 -p 18080:18080 glue/sparkui:latest "/opt/spark/bin/spark-class org.apache.spark.deploy.history.HistoryServer"