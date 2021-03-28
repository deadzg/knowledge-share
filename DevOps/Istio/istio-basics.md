# Istio Basics

## Commands
- Download: `curl -L https://istio.io/downloadIstio | sh -`
- Install: `istioctl manifest apply --set profile=demo`
    Make sure the minikube is already running
- Verfify all the services are up: `kubectl get svc -n istio-system`
- Verify all the pods are up: `kubectl get pods -n istio-system`    
- List istio profile: `istioctl profile list`
- Check profile configuration: `istioctl profile dump <profile_name>`

## Kind Deployment
https://istio.io/latest/docs/setup/platform-setup/kind/

### Steps to Deploy
Deploy Istio: `istioctl install --set profile=default -y`
Enable Namespace for Istio: `kubectl label namespace <namespace-name> istio-injection=enabled`
Install Kiali: `kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.9/samples/addons/kiali.yaml`
Run Kiali: `istioctl dashboard kiali`

# References
- https://medium.com/faun/istio-step-by-step-part-10-installing-istio-1-4-in-minikube-ebce9a4e99c