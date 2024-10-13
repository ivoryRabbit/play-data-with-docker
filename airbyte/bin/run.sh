## brew install helm

helm repo add airbyte https://airbytehq.github.io/helm-charts
helm repo update

helm install airbyte-local airbyte/airbyte
## helm install --values ../values.yaml airbyte-local airbyte/airbyte

## kubectl apply -f airbyte-logs-secrets.yaml -n <NAMESPACE>