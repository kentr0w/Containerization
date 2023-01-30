eval $(minikube docker-env)

docker build -t flask-api service/
docker build -t react-app frontend/

kubectl delete deployments --all
kubectl delete svc --all
kubectl delete pvc --all
kubectl delete pv --all
kubectl delete secret --all
kubectl delete configmap --all
