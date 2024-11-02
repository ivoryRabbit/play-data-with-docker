helm repo add airbyte https://airbytehq.github.io/helm-charts

helm repo update

kubectl create namespace airbyte

helm --namespace airbyte install airbyte-local airbyte/airbyte
helm --namespace airbyte install airbyte-nginx oci://ghcr.io/nginxinc/charts/nginx-ingress

kubectl --namespace airbyte apply -f ingress/nginx.yaml