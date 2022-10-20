## AWS ALB Ingress Controller

### Annotations Reference: 
https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.2/guide/ingress/annotations/

### AWS Ref
https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html

https://aws.amazon.com/blogs/opensource/kubernetes-ingress-aws-alb-ingress-controller/

```yaml
# Annotations Reference: https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.2/guide/ingress/annotations/
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress-usermgmt-restapp-service
  labels:
    app: usermgmt-restapp
  annotations:
    # Ingress Core Settings
    kubernetes.io/ingress.class: "alb"
    alb.ingress.kubernetes.io/scheme: internet-facing
    # Health Check Settings
    alb.ingress.kubernetes.io/healthcheck-protocol: HTTP 
    alb.ingress.kubernetes.io/healthcheck-port: traffic-port
    alb.ingress.kubernetes.io/healthcheck-path: /usermgmt/health-status
    alb.ingress.kubernetes.io/healthcheck-interval-seconds: '15'
    alb.ingress.kubernetes.io/healthcheck-timeout-seconds: '5'
    alb.ingress.kubernetes.io/success-codes: '200'
    alb.ingress.kubernetes.io/healthy-threshold-count: '2'
    alb.ingress.kubernetes.io/unhealthy-threshold-count: '2'
spec:
  rules:
    - http:
        paths:
          - path: /*
            backend:
              serviceName: usermgmt-restapp-nodeport-service
              servicePort: 8095
```


```yaml
---
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: app2-ingress-service
  labels:
    app: cloudgeeks-app2
  namespace: cloudgeeks-app2
  annotations:
    # Single ALB Ingress Settings
    kubernetes.io/ingress.class: "alb"
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/group.name: cloudgeeksca
    # Health Check Settings
    alb.ingress.kubernetes.io/healthcheck-protocol: HTTP 
    alb.ingress.kubernetes.io/healthcheck-port: traffic-port
    alb.ingress.kubernetes.io/healthcheck-interval-seconds: '15'
    alb.ingress.kubernetes.io/healthcheck-timeout-seconds: '5'
    alb.ingress.kubernetes.io/success-codes: '200'
    alb.ingress.kubernetes.io/healthy-threshold-count: '2'
    alb.ingress.kubernetes.io/unhealthy-threshold-count: '2'
    ## SSL Settings
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTPS":443}, {"HTTP":80}]'
    alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:us-east-1:180056778330:certificate/83bb75f4-1d05-4267-a349-d692e007ffa5
    # SSL Redirect Setting
    alb.ingress.kubernetes.io/actions.ssl-redirect: '{"Type": "redirect", "RedirectConfig": { "Protocol": "HTTPS", "Port": "443", "StatusCode": "HTTP_301"}}'
spec:
  rules:
    - host: app2.saqlainmushtaq.com
      http:
        paths:
          - path: /green/index.html # SSL Redirect Setting
            backend:
              serviceName: ssl-redirect
              servicePort: use-annotation
          - path: /green/index.html
            backend:
              serviceName: cloudgeeks-app2-nodeport-service
              servicePort: 80
```