---
title: How to Setup DNS for a Website Using Kubernetes, EKS, and NGINX
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-07T11:30:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-dns-for-a-website-using-kubernetes-eks-and-nginx
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/nyc.png
tags:
- name: Devops
  slug: devops
- name: dns
  slug: dns
- name: Kubernetes
  slug: kubernetes
- name: nginx
  slug: nginx
seo_title: null
seo_desc: 'By Adam Henson

  As the creator of Foo, a platform for website quality monitoring, I recently endeavored
  in a migration to Kubernetes and EKS (an AWS service).

  Kubernetes provides a robust level of DNS support. Luckily for us, within a cluster,
  we can ...'
---

By Adam Henson

As the creator of [Foo, a platform for website quality monitoring](https://www.foo.software/), I recently endeavored in a migration to Kubernetes and EKS (an AWS service).

Kubernetes provides a robust level of DNS support. Luckily for us, within a cluster, we can reference pods by host name as defined in a spec. 

But what if we want to expose an app to the outside world as a website under a static domain? I thought this would be a common, well documented case, but boy was I wrong.

> Assume a Service named `foo` in the Kubernetes namespace `bar`. A Pod running in namespace `bar` can look up this service by simply doing a DNS query for `foo`. A Pod running in namespace `quux` can look up this service by doing a DNS query for `foo.bar` ~ [DNS for Services and Pods - Kubernetes](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)

Yes, that's great ❤️ But this still leads to many unsolved mysteries. Let's take this one step at a time shall we?! This post will address the following items.

1. **How to define services**
2. **How to expose multiple services under one NGINX server**. No fancy schmancy "[Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)" needed **?**
3. **How to create an external DNS and connect to a domain** you've acquired through any qualified registry like GoDaddy or Google Domains, for example. We'll use [Route 53](https://aws.amazon.com/route53/) and [ExternalDNS](https://github.com/kubernetes-sigs/external-dns) to do the heavy lifting.

This post assumes a setup with EKS and `eksctl` as documented in "[Getting started with `eksctl`](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html)", but many of the concepts and examples in this post could be applicable in a variety of configurations.

## Step 1: Define Services

[Connecting Applications with Services](https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/) explains how to expose an NGINX application by defining a `Deployment` and `Service`. Let's go ahead and create 3 applications in the same manner: a user facing web app, an API and a reverse proxy NGINX server to expose the two apps under one host.

> web-deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        # etc, etc
```

> web-service.yaml

```
apiVersion: v1
kind: Service
metadata:
  name: web
  labels:
    app: web
spec:
  ports:
  - name: "3000"
    port: 3000
    targetPort: 3000
  selector:
    app: web
```

> api-deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
      - name: api
        # etc, etc
```

> api-service.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api
  labels:
    app: api
spec:
  ports:
  - name: "3000"
    port: 3000
    targetPort: 3000
  selector:
    app: api
```

Fair enough, let's move on!

## Step 2: Expose Multiple Services Under One NGINX Server

NGINX is a reverse proxy in that it proxies a request by sending it to a specified origin, fetches the response, and sends it back to the client. 

Going back to the bit about service names being accessible to other pods in a cluster, we can setup an NGINX configuration to look something like this.

> sites-enabled/www.example.com.conf

```
upstream api {
  server api:3000;
}

upstream web {
  server web:3000;
}

server {
  listen 80;

  server_name www.example.com;

  location / {
    proxy_pass http://web;
  }

  location /api {
    proxy_pass http://api;
  }
}
```

Note how we can reference origin hosts like `web:3000` and `api:300`. Niiiice!

> nginx-deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80

```

> nginx-service.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
  annotations:
    # this part will make more sense later
    external-dns.alpha.kubernetes.io/hostname: www.example.com
  labels:
    app: nginx
spec:
  type: LoadBalancer
  ports:
  - name: "80"
    port: 80
    targetPort: 80
  selector:
    app: nginx
```

...and, we're done! Right? In my experience, initially I thought so. The `[LoadBalancer](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/)` provides an externally-accessible IP. You can confirm by running `kubectl get svc` and sure enough you'll find a host name listed in the `EXTERNAL-IP` column. 

Assuming you've acquired a domain from a provider that offers an interface to manage DNS settings, you could simply add this URL as a `CNAME` and you're good, right? Well, kinda... but not so much.

Kubernetes Pods are considered to be relatively ephemeral (rather than durable) entities. Find more on this in "[Pod Lifecycle - Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)". 

With that said, anytime a significant change has been made in the lifecycle of a service, in our case the NGINX app, we will have a different IP address which will in turn cause significant downtime in our app which defeats a main purpose of Kubernetes - to help establish a "highly available" application. 

Okay, don't panic - we'll get through this ?

## Step 3: Create an External DNS Service to Dynamically Point NGINX

In the previous step, with our `LoadBalancer` spec coupled with EKS we actually created an [Elastic Load Balancer](https://aws.amazon.com/elasticloadbalancing/) (for better or worse). 

In this section we'll create a DNS service that points our load balancer via "ALIAS record". This ALIAS record is essentially dynamic in that a new one is created whenever our service changes. The stability is established in the name server records.

The tl;dr for the remaining portion is simply follow the [documentation for using ExternalDNS with Route 53](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md). Route 53 is "[cloud Domain Name System (DNS) web service](https://aws.amazon.com/route53/)". 

Below were things I had to do that weren't obvious from the documentation. Hold on to your horses, this gets a little scrappy.

* `eksctl utils associate-iam-oidc-provider --cluster=your-cluster-name` per [`eksctl` service accounts documentation](https://eksctl.io/usage/iamserviceaccounts/).
* When creating the IAM policy document per the [ExternalDNS documentation](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md#iam-policy), I actually had to do it via CLI vs online in my account. I kept getting this error: `WebIdentityErr: failed to retrieve credentials\ncaused by: AccessDenied: Not authorized to perform sts:AssumeRoleWithWebIdentity\n\tstatus code: 403`. When I created the policy via CLI the issue went away. Below is the full command you should be able to literally copy and execute if you have the [AWS CLI](https://aws.amazon.com/cli/) installed.

```
aws iam create-policy \
  --policy-name AllowExternalDNSUpdates \
  --policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":["route53:ChangeResourceRecordSets"],"Resource":["arn:aws:route53:::hostedzone/*"]},{"Effect":"Allow","Action":["route53:ListHostedZones","route53:ListResourceRecordSets"],"Resource":["*"]}]}'
```

* Use the policy ARN output above to create an IAM role bound to the ExternalDNS service account with a command that will look something like `eksctl create iamserviceaccount --cluster=your-cluster-name --name=external-dns --namespace=default --attach-policy-arn=arn:aws:iam::123456789:policy/AllowExternalDNSUpdates`.
* We should now have a new role from the above that we can see in the [IAM console](https://console.aws.amazon.com/iam) which will have a name of something like `eksctl-foo-addon-iamserviceaccount-Role1-abcdefg`. Click on the role from the list and at the top of the next screen make note of the "Role ARN" as something like `arn:aws:iam::123456789:role/eksctl-foo-addon-iamserviceaccount-Role1-abcdefg`.
* Follow [these steps](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md#set-up-a-hosted-zone) to create a "hosted zone" in Route 53.
* You can confirm things in the [Route 53 console](https://console.aws.amazon.com/route53).
* If your domain provider allows you to manage DNS settings, add the 4 name server records from the output of the command you ran to create a "hosted zone".
* Deploy ExternalDNS by following [the instructions](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md#deploy-externaldns). Afterwards, you can tail the logs with `kubectl logs -f name-of-external-dns-pod`. You should see a line like this at the end: `time="2020-05-05T02:57:31Z" level=info msg="All records are already up to date"`

Easy, right?! Okay, maybe not... but at least you didn't have to figure all of that out alone ? There could be some gaps above, but hopefully it helps guide you through your process.

## Conclusion

Although this post may have some grey areas, if it helps you establish dynamic DNS resolution as part of a highly available application, you've got something really special ?

Please add comments if I can help clear up anything or correct my terminology!

