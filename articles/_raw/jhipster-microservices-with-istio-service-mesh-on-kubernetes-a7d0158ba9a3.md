---
title: How to set up JHipster microservices with Istio service mesh on Kubernetes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-17T16:01:37.000Z'
originalURL: https://freecodecamp.org/news/jhipster-microservices-with-istio-service-mesh-on-kubernetes-a7d0158ba9a3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sed7vszGYvi40oa1F7iVzg.png
tags:
- name: Azure
  slug: azure
- name: Google Cloud Platform
  slug: google-cloud-platform
- name: Kubernetes
  slug: kubernetes
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Deepu K Sasidharan

  You can find a more up to date version of this post that uses JHipster 6 and latest
  Istio & Kubernetes versions here.


  Istio is the coolest kid on the DevOps and Cloud block now. For those of you who
  aren’t following close enoug...'
---

By Deepu K Sasidharan

You can find a more up to date version of this post that uses JHipster 6 and latest Istio & Kubernetes versions [here](https://dev.to/deepu105/how-to-set-up-java-microservices-with-istio-service-mesh-on-kubernetes-5bkn).

---

Istio is the coolest kid on the DevOps and Cloud block now. For those of you who aren’t following close enough — [Istio is a service mesh](https://istio.io/docs/concepts/what-is-istio/) for distributed application architectures, especially the ones that you run on the cloud with Kubernetes. Istio plays extremely nice with Kubernetes, so nice that you might think that it’s part of Kubernetes.

If you are still wondering, what the heck is a service mesh or Istio? then let's have an overview of Istio.

Istio provides the following functionality in a distributed application architecture:

* Service discovery — Traditionally provided by platforms like [Netflix Eureka](https://github.com/Netflix/eureka/wiki) or [Consul](https://www.consul.io/).
* Automatic load balancing — You might have used [Netflix Zuul](https://github.com/Netflix/zuul/wiki) for this.
* Routing, circuit breaking, retries, fail-overs, fault injection — Think of [Netflix Ribbon](https://github.com/Netflix/ribbon/wiki), [Hytrix](https://github.com/Netflix/Hystrix) and so on.
* Policy enforcement for access control, rate limiting, A/B testing, traffic splits, and quotas — Again you might have used Zuul to do some of these.
* Metrics, logs, and traces — Think of [ELK](https://www.elastic.co/elk-stack) or [Stack driver](https://cloud.google.com/stackdriver/)
* Secure service-to-service communication

Below is the architecture of Istio.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_STCerKXb4L3Hutyn4P5Gw.png)
_Istio architecture_

It can be classified into 2 distinct planes.

**Data plane**: Is made of [Envoy](https://www.envoyproxy.io/) proxies deployed as sidecars to the application containers. They control all the incoming and outgoing traffic to the container.

**Control plane**: It uses Pilot to manages and configure the proxies to route traffic. It also configures Mixer to enforce policies and to collect telemetry. It also has other components like Citadel, to manage security, and Galley, to manage configurations.

Istio also configures an instance of [Grafana](https://grafana.com/), [Prometheus](https://prometheus.io/) and [Jaeger](https://www.jaegertracing.io/) for Monitoring and Observability. You can use this or use your existing monitoring stack as well.

I hope this provides an overview of Istio, now let's focus on the goal of this article.

### Devoxx 2018

I did a talk at [Devoxx 2018](https://dvbe18.confinabox.com/talk/XCM-6395/JHipster_5_-_What's_new_and_noteworthy) along with [Julien Dubois](https://www.julien-dubois.com/) doing the same demo and promised that I’d write a detailed blog about it.

%[https://twitter.com/deepu105/status/1063010906777497600?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fdeepu105%2Fstatus%2F1063010906777497600%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F1056590953132244993%25252F0FGRfVeQ_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

You can watch the video to see JHipster + Istio in action.

%[https://www.youtube.com/watch?v=NPToZd0PxbI]

You can watch the slides on Speaker Deck as well.

%[https://speakerdeck.com/deepu105/jhipster-5-whats-new-and-noteworthy]

### Preparing the Kubernetes cluster

First, let us prepare a Kubernetes cluster to deploy Istio and our application containers. Follow the instructions for any one of the platforms you prefer.

#### Prerequisites

[**kubectl**](https://kubernetes.io/docs/tasks/tools/install-kubectl/): The command line tool to interact with Kubernetes. Install and configure it.

#### Create a cluster on Azure Kubernetes Service(AKS)

If you are going to use Azure, then install [**Azure CLI**](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) to interact with Azure. Install and log in with your Azure account (you can create a [free account](https://azure.microsoft.com/en-us/free/) if you don’t have one already).

First let us create a resource group. You can use any region you like here instead of East US.

```bash
$ az group create --name eCommerceCluster --location eastus
```

Create the Kubernetes cluster:

```bash
$ az aks create \
--resource-group eCommerceCluster \
--name eCommerceCluster \
--node-count 4 \
--kubernetes-version 1.11.4 \
--enable-addons monitoring \
--generate-ssh-keys
```

The `node-count` flag is important as the setup requires at least four nodes with the default CPU to run everything. You can try to use a higher `kubernetes-version` if it is supported, else stick to 1.11.4

The cluster creation could take while so sit back and relax. ?

Once the cluster is created, fetch its credentials to be used from `kubectl` by running the below command. It automatically injects the credentials to your `kubectl` configuration under **_~/.kube/config_**

```bash
$ az aks get-credentials \
--resource-group eCommerceCluster \
--name eCommerceCluster
```

You can view the created cluster in the Azure portal:

![Image](https://cdn-media-1.freecodecamp.org/images/1*yfLnHHc_N7VCkEY9vjNciQ.png)
_Kubernetes cluster in AKS_

Run `kubectl get nodes` to see it in the command line and to verify that kubectl can connect to your cluster.

![Image](https://cdn-media-1.freecodecamp.org/images/1*k8xsRqQsvnquUhGPAh9TsA.png)
_Cluster Nodes_

Proceed to the **Install and setup Istio** section.

#### Create a cluster on Google Kubernetes Engine(GKE)

If you are going to use Google Cloud Platform(GCP) then install [**Gcloud CLI**](https://cloud.google.com/sdk/docs/)to interact with GCP. Install and log in with your GCP account (you can create a [free account](https://console.cloud.google.com/freetrial) if you don’t have one already).

First, we need a GCP project, you can either use an existing project that you have or create a new one using GCloud CLI with below command:

```bash
$ gcloud projects create jhipster-demo-deepu
```

Set the project you want to use as the default project:

```bash
$ gcloud config set project jhipster-demo-deepu
```

Now let us create a cluster for our application with the below command:

```bash
$ gcloud container clusters create hello-hipster \

   --cluster-version 1.10 \
   
   --num-nodes 4 \
   
   --machine-type n1-standard-2
```

The `num-nodes` and `machine-type` flags are important as the setup requires at least four nodes with a bigger CPU to run everything. You can try to use a higher `cluster-version` if it is supported, else stick to 1.10.

The cluster creation could take while so sit back and relax.

Once the cluster is created, fetch its credentials to be used from `kubectl` by running the below command. It automatically injects the credentials to your `kubectl` configuration under **_~/.kube/config_**

```bash
$ gcloud container clusters get-credentials hello-hipster
```

You can view the created cluster in the GCP GUI.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZxNbIG4vqWJymTLweJpPyQ.png)
_Kubernetes cluster on GKE_

Run `kubectl get nodes` to see it in the command line and to verify that kubectl can connect to your cluster.

![Image](https://cdn-media-1.freecodecamp.org/images/1*F5Qcd_GS_GSuA1PsJE7gvA.png)
_Cluster Nodes_

### Install and setup Istio

Install Istio on your machine by following these steps:

```bash
$ cd ~/

$ export ISTIO_VERSION=1.0.2

$ curl -L https://git.io/getLatestIstio | sh -

$ ln -sf istio-$ISTIO_VERSION istio

$ export PATH=~/istio/bin:$PATH
```

Make sure to use version **1.0.2** since the latest version seems to have issues connecting to the MySQL database containers.

Now let us install Istio on our Kubernetes cluster by applying the provided Kubernetes manifests and helm templates from Istio.

```bash
$ kubectl apply -f ~/istio/install/kubernetes/helm/istio/templates/crds.yaml
$ kubectl apply -f ~/istio/install/kubernetes/istio-demo.yaml \
    --as=admin --as-group=system:masters
```

Wait for the pods to run, these will be deployed to the `istio-system` namespace.

```bash
$ watch kubectl get pods -n istio-system
```

Once the pods are in running status, exit the watch loop and run the below to get the Ingress gateway service details. This is the only service that is exposed to an external IP.

```bash
$ kubectl get svc istio-ingressgateway -n istio-system

NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP
istio-ingressgateway   LoadBalancer   10.27.249.83   35.195.81.130
```

The external IP is very important here, let us save this to an environment variable so that we can use it in further commands.

```bash
$ export \
  INGRESS_IP=$(kubectl -n istio-system get svc \
  istio-ingressgateway \
  -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
```

Now our Kubernetes cluster is ready for Istio. ?

_For advanced Istio setup options refer to_ [_https://istio.io/docs/setup/kubernetes/_](https://istio.io/docs/setup/kubernetes/)

### Creating the microservice application stack

In one of my [previous posts](https://medium.com/@deepu105/create-full-microservice-stack-using-jhipster-domain-language-under-30-minutes-ecc6e7fc3f77), I showcased how to create a full stack microservice architecture using **JHipster** and **JDL**. You can read the post [here](https://medium.com/@deepu105/create-full-microservice-stack-using-jhipster-domain-language-under-30-minutes-ecc6e7fc3f77) if you want to learn more details about it. For this exercise, we will use the same application but we will not use the Eureka service discovery option we used earlier. Also, note that the store application is further split into Gateway and Product applications.

#### Architecture

Here is the architecture of the microservice that we are going to create and deploy today.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UmNJ-Ue362-OltPOxt-OFQ.png)
_Microservice architecture with Istio_

It has a gateway application and three microservice applications. Each of them has its own database. You can see that each application has an Envoy proxy attached to the pod as a sidecar. Istio control plane components are also deployed to the same cluster along with Prometheus, Grafana, and Jaeger.

The Ingress gateway from Istio is the only entry point for traffic and it routes traffic to all microservices accordingly. Telemetry is collected from all the containers running in the cluster, including the applications, databases, and Istio components.

Compared to the architecture of the original application [here](https://medium.com/@deepu105/deploying-jhipster-microservices-on-azure-kubernetes-service-aks-fb46991746ba), you can clearly see that we replaced the JHipster registry and Netflix OSS components with Istio. The ELK monitoring stack is replaced with Prometheus, Grafana and Jaeger configured by Istio. Here is the original architecture diagram without Istio for a quick visual comparison.

![Image](https://cdn-media-1.freecodecamp.org/images/1*H-6_dz1-aYXQ-fzWEuJcRw.png)
_Microservice architecture with Netflix OSS_

#### Application JDL

Let’s take a look at the modified JDL declaration. You can see that we have declared `serviceDiscoveryType no` here since we will be using Istio for that.

```

application {
  config {
    baseName store
    applicationType gateway
    packageName com.jhipster.demo.store
    serviceDiscoveryType no
    authenticationType jwt
    prodDatabaseType mysql
    cacheProvider hazelcast
    buildTool gradle
    clientFramework react
    useSass true
    testFrameworks [protractor]
  }
  entities *
}


application {
  config {
    baseName product
    applicationType microservice
    packageName com.jhipster.demo.product
    serviceDiscoveryType no
    authenticationType jwt
    prodDatabaseType mysql
    cacheProvider hazelcast
    buildTool gradle
    serverPort 8081
  }
  entities Product, ProductCategory, ProductOrder, OrderItem
}

application {
  config {
    baseName invoice
    applicationType microservice
    packageName com.jhipster.demo.invoice
    serviceDiscoveryType no
    authenticationType jwt
    prodDatabaseType mysql
    buildTool gradle
    serverPort 8082
  }
  entities Invoice, Shipment
}

application {
  config {
    baseName notification
    applicationType microservice
    packageName com.jhipster.demo.notification
    serviceDiscoveryType no
    authenticationType jwt
    databaseType mongodb
    cacheProvider no
    enableHibernateCache false
    buildTool gradle
    serverPort 8083
  }
  entities Notification
}

/**
 * Entities for Store Gateway
 */

// Customer for the store
entity Customer {
    firstName String required
    lastName String required
    gender Gender required
    email String required pattern(/^[^@\s]+@[^@\s]+\.[^@\s]+$/)
    phone String required
    addressLine1 String required
    addressLine2 String
    city String required
    country String required
}

enum Gender {
    MALE, FEMALE, OTHER
}

relationship OneToOne {
    Customer{user(login) required} to User
}

service Customer with serviceClass
paginate Customer with pagination


/**
 * Entities for product microservice
 */


// Product sold by the Online store 
entity Product {
    name String required
    description String
    price BigDecimal required min(0)
    size Size required
    image ImageBlob
}

enum Size {
    S, M, L, XL, XXL
}

entity ProductCategory {
    name String required
    description String
}

entity ProductOrder {
    placedDate Instant required
    status OrderStatus required
    code String required
    invoiceId Long
    customer String required
}

enum OrderStatus {
    COMPLETED, PENDING, CANCELLED
}

entity OrderItem {
    quantity Integer required min(0)
    totalPrice BigDecimal required min(0)
    status OrderItemStatus required
}

enum OrderItemStatus {
    AVAILABLE, OUT_OF_STOCK, BACK_ORDER
}

relationship ManyToOne {
	OrderItem{product(name) required} to Product
}

relationship OneToMany {
   ProductOrder{orderItem} to OrderItem{order(code) required} ,
   ProductCategory{product} to Product{productCategory(name)}
}

service Product, ProductCategory, ProductOrder, OrderItem with serviceClass
paginate Product, ProductOrder, OrderItem with pagination
microservice Product, ProductOrder, ProductCategory, OrderItem with product


/**
 * Entities for Invoice microservice
 */


// Invoice for sales
entity Invoice {
    code String required
    date Instant required
    details String
    status InvoiceStatus required
    paymentMethod PaymentMethod required
    paymentDate Instant required
    paymentAmount BigDecimal required
}

enum InvoiceStatus {
    PAID, ISSUED, CANCELLED
}

entity Shipment {
    trackingCode String
    date Instant required
    details String
}

enum PaymentMethod {
    CREDIT_CARD, CASH_ON_DELIVERY, PAYPAL
}

relationship OneToMany {
    Invoice{shipment} to Shipment{invoice(code) required}
}

service Invoice, Shipment with serviceClass
paginate Invoice, Shipment with pagination
microservice Invoice, Shipment with invoice


/**
 * Entities for notification microservice
 */


entity Notification {
    date Instant required
    details String
    sentDate Instant required
    format NotificationType required
    userId Long required
    productId Long required
}

enum NotificationType {
    EMAIL, SMS, PARCEL
}

microservice Notification with notification

/**
 * Deployments
 */

deployment {
  deploymentType kubernetes
  appsFolders [store, invoice, notification, product]
  dockerRepositoryName "deepu105"
  serviceDiscoveryType no
  istio true
  kubernetesServiceType Ingress
  kubernetesNamespace jhipster
  ingressDomain "34.90.236.124.nip.io"
}
```

#### Deployment JDL

JHipster version 5.7.0 introduced support for deployment declaration straight in the JDL

%[https://twitter.com/deepu105/status/1056588722769195018?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fdeepu105%2Fstatus%2F1056588722769195018%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F1056590953132244993%25252F0FGRfVeQ_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

We have the below in our JDL which declares our Kubernetes deployment:

```
deployment {
  deploymentType kubernetes
  appsFolders [store, invoice, notification, product]
  dockerRepositoryName "deepu105"
  serviceDiscoveryType no
  istio autoInjection
  istioRoute true
  kubernetesServiceType Ingress
  kubernetesNamespace jhipster
  ingressDomain "35.195.81.130.nip.io"
}
```

The `serviceDiscoveryType` is disabled and we have enabled Istio with `autoInjection` support — the Envoy sidecars are injected automatically for the selected applications. Istio routes are also generated for the applications by enabling `istioRoute` option.

The `kubernetesServiceType` is set as `Ingress`, which is very important as Istio can only work with an Ingress controller service type. For Ingress, we need to set the domain DNS and this is where the Istio ingress gateway IP is needed. Now we need a DNS for our IP. For real usecases, you should map a DNS for the IP, but for testing and demo purposes we can use a wildcard DNS service like [**nip.io**](http://nip.io/) to resolve our IP. Just append `nip.io` to our IP and use that as the ingress domain.

#### Generate the applications and deployment manifests

Now that our JDL is ready, let us scaffold our applications and Kubernetes manifests. Create a new directory and save the above JDL in the directory. Let us name it **_app-istio.jdl_** and then run the import-jdl command.

```bash
$ mkdir istio-demo && cd istio-demo
$ jhipster import-jdl app-istio.jdl
```

This will generate all the applications and install the required NPM dependencies in each of them. Once the applications are generated the deployment manifests will be generated and some useful instruction will be printed to the console.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ROg2XrRkHVHA4Xib)
_Generation output_

Open the generated code in your favorite IDE/Editor and explore the code.

### Deploy to Kubernetes cluster using Kubectl

Now let us build and deploy our applications. Run the `./gradlew bootWar -Pprod jibDockerBuild` command in the store, product, invoice, and notification folders to build the docker images. Once the images are built, push them to the docker repo with these commands:

```bash
$ docker image tag store deepu105/store

$ docker push deepu105/store

$ docker image tag invoice deepu105/invoice

$ docker push deepu105/invoice

$ docker image tag notification deepu105/notification

$ docker push deepu105/notification

$ docker image tag product deepu105/product

$ docker push deepu105/product
```

Once the images are pushed, navigate into the generated Kubernetes directory and run the provided startup script. (If you are on windows you can run the steps in **_kubectl-apply.sh_** manually one by one.)

```bash
$ cd kubernetes
$ ./kubectl-apply.sh
```

Run `watch kubectl get pods -n jhipster` to monitor the status.

### Deployed applications

Once all the pods are in running status we can explore the deployed applications

#### Application gateway

The store gateway application is the entry point for our microservices. Get the URL for the store app by running `echo store.$INGRESS_IP.nip.io`, we already stored the INGRESS_IP to environment variables while creating the Istio setup. Visit the URL in your favorite browser and explore the application. Try creating some entities for the microservices:

![Image](https://cdn-media-1.freecodecamp.org/images/0*Qd6y_H-ObCeorQkg)
_Store gateway application_

#### Monitoring

Istio setup includes Grafana and Prometheus configured to collect and show metrics from our containers. Let's take a look.

By default, only the Ingress gateway is exposed to external IP and hence we will use kubectl port forwarding to set up a secure tunnel to the required services

Let us create a tunnel for Grafana:

```bash
$ kubectl -n istio-system \
port-forward $(kubectl -n istio-system get pod \

-l app=grafana -o jsonpath='{.items[0].metadata.name}') 3000:3000
```

Open [localhost:3000](localhost:3000) to view the Grafana dashboard.

![Image](https://cdn-media-1.freecodecamp.org/images/0*zaX0S8relpT4q__T)
_Grafana dashboard for the Store application_

Grafana uses the metrics scrapped by Prometheus. We can look at Prometheus directly by creating a tunnel for it and opening [localhost:9090](localhost:9090):

```bash
$ kubectl -n istio-system \
port-forward $(kubectl -n istio-system get pod -l \

app=prometheus -o jsonpath='{.items[0].metadata.name}') 9090:9090
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*W4obHNne_wQJfAuU)
_Prometheus dashboard_

#### Observability

Istio configures Jaeger for distributed tracing and service graph for service observability. Let us take a look at them.

Create a tunnel for Jaeger and open [localhost:16686](localhost:16686)

```bash
$ kubectl -n istio-system \
port-forward $(kubectl -n istio-system get pod -l \

app=jaeger -o jsonpath='{.items[0].metadata.name}') 16686:16686
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*cyhS1_B0LFO54e48)
_Jaeger tracing dashboard_

You can make some requests in the application and find it in the tracing dashboard by querying for the service. Click on the request to see tracing details:

![Image](https://cdn-media-1.freecodecamp.org/images/1*X4XtKtIeMapPEyt_nfvftA.png)
_Tracing for product category listing request_

Let us now create a tunnel for the service graph and open it in [localhost:8080/force/forcegraph.html](localhost:8080/force/forcegraph.html):

```bash
$ kubectl -n istio-system \
port-forward $(kubectl -n istio-system get pod -l \

app=servicegraph -o jsonpath='{.items[0].metadata.name}') 8088:8088
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*4nQUsagF6TVupK-5)
_Istio service graph_

### Conclusion

Istio provides building blocks to build distributed microservices in a more Kubernetes-native way and takes the complexity and responsibility of maintaining those blocks away from you. This means you do not have to worry about maintaining the code or deployments for service discovery, tracing and so on.

Istio documentation says

> Deploying a microservice-based application in an Istio service mesh allows one to externally control service monitoring and tracing, request (version) routing, resiliency testing, security and policy enforcement, etc., in a consistent way across the services, for the application as a whole.

Werner Vogels (CTO of AWS) quoted at AWS Re:Invent

> “In the future, all the code you ever write will be business logic.”

Istio Service mesh helps with that statement. This lets you worry only about the applications that you are developing and with JHipster that future is truly here and you just need to worry about writing your business logic.

While this is great, it is not a silver bullet. Keep in mind that Istio is fairly new compared to other stable and battle-tested solutions like JHipster Registry (Eureka) or Consul.

Also, another thing to keep in mind is the resource requirements. The same microservices with JHipster Registry or Consul can be deployed to a 2 node cluster with 1 vCPU and 3.75 GB of memory per node in GCP while you need a 4 node cluster with 2 vCPUs and 7.5 GB of memory per node for Istio enabled deployments. The default Kubernetes manifest from Istio doesn’t apply any request limits for resources, and by adding and tuning those, the minimum requirement could be reduced. But still I don’t think you can get it as low as that is needed for the JHipster registry option.

In a real-world use case, the advantages of not having to maintain the complex parts of your infra vs having to pay for more resources might be a decision that has to be taken based on your priorities and goals.

A huge shout out to [Ray Tsang](https://twitter.com/saturnism) for helping me figure out an optimal cluster size for this application. Also a huge thank you from myself and the community to both Ray and [Srinivasa Vasu](https://twitter.com/humourmind) for adding the Istio support to JHipster.

JHipster provides a great Kubernetes setup to start with which you can further tweak as per your needs and platform. The Istio support is recent and will improve further over time, but it's still a great starting point especially to learn.

To learn more about JHipster and Full stack development, check out my book “_Full Stack Development with JHipster_” on [Amazon](https://www.amazon.com/Stack-Development-JHipster-Deepu-Sasidharan/dp/178847631X) and [Packt](https://www.packtpub.com/application-development/full-stack-development-jhipster).

There is a great Istio tutorial from Ray Tsang [here](https://docs.google.com/document/d/1Qo8o5C4UpGwMF7Mg02kLTaU4-xCSfJjLcnIFNveMEEA).

If you like JHipster don’t forget to give it a star on [Github](https://github.com/jhipster/generator-jhipster).

If you like this article, please leave some claps (Did you know that you can clap multiple times in Medium? ?) I hope to write more about Istio in the near future.

You can follow me on [Twitter](https://twitter.com/deepu105) and [LinkedIn](https://www.linkedin.com/in/deepu05/).

My other related posts:

1. [Create full Microservice stack using JHipster Domain Language under 30 minutes](https://medium.com/@deepu105/create-full-microservice-stack-using-jhipster-domain-language-under-30-minutes-ecc6e7fc3f77)
2. [Deploying JHipster Microservices on Azure Kubernetes Service (AKS)](https://medium.com/@deepu105/deploying-jhipster-microservices-on-azure-kubernetes-service-aks-fb46991746ba)

