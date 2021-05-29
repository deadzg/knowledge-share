# Istio Basics

- The `proxy-status` command allows you to get an overview of your mesh and identify the proxy causing the problem
- Then `proxy-config` can be used to inspect Envoy configuration and diagnose the issue.

https://istio.io/latest/docs/ops/diagnostic-tools/proxy-cmd/
## Commands
- Download: `curl -L https://istio.io/downloadIstio | sh -`
- Install: `istioctl manifest apply --set profile=demo`
    Make sure the minikube is already running
- Verfify all the services are up: `kubectl get svc -n istio-system`
- Verify all the pods are up: `kubectl get pods -n istio-system`    
- List istio profile: `istioctl profile list`
- Check profile configuration: `istioctl profile dump <profile_name>`
- Check All the Envoy Proxy Status: `istioctl proxy-status`
- Get envoy proxy config: `istioctl proxy-config cluster <pod-name> [flags]`

https://istio.io/latest/docs/ops/diagnostic-tools/istioctl/

## Kind Deployment
https://istio.io/latest/docs/setup/platform-setup/kind/

### Steps to Deploy
Deploy Istio: `istioctl install --set profile=default -y`
Enable Namespace for Istio: `kubectl label namespace <namespace-name> istio-injection=enabled`
Install Kiali: `kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.9/samples/addons/kiali.yaml`
Run Kiali: `istioctl dashboard kiali`

# References
- https://medium.com/faun/istio-step-by-step-part-10-installing-istio-1-4-in-minikube-ebce9a4e99c