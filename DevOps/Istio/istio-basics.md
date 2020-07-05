# Istio Basics

## Commands
- Download: `curl -L https://istio.io/downloadIstio | sh -`
- Install: `istioctl manifest apply --set profile=demo`
    Make sure the minikube is already running
- Verfify all the services are up: `kubectl get svc -n istio-system`
- Verify all the pods are up: `kubectl get pods -n istio-system`    
- List istio profile: `istioctl profile list`
- Check profile configuration: `istioctl profile dump <profile_name>`



# References
- https://medium.com/faun/istio-step-by-step-part-10-installing-istio-1-4-in-minikube-ebce9a4e99c