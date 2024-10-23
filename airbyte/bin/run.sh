## brew install helm

helm repo add airbyte https://airbytehq.github.io/helm-charts
helm repo update

helm install airbyte-local airbyte/airbyte
## helm install --values ../values.yaml airbyte-local airbyte/airbyte

## kubectl apply -f airbyte-logs-secrets.yaml -n <NAMESPACE>


# kubectl --namespace airbyte port-forward airbyte-local-webapp-5b66d8c784-qwm2c 8080:8080

# helm install airbyte-nginx oci://ghcr.io/nginxinc/charts/nginx-ingress --version 1.4.0 --namespace airbyte

helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace