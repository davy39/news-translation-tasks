---
title: What is a Helm Chart? A Tutorial for Kubernetes Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-09T18:44:46.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-helm-chart-tutorial-for-kubernetes-beginners
coverImage: https://cdn-media-2.freecodecamp.org/w1280/604640a8a7946308b768453d.jpg
tags:
- name: charts
  slug: charts
- name: containers
  slug: containers
- name: Helm
  slug: helm
- name: Kubernetes
  slug: kubernetes
seo_title: null
seo_desc: 'By Lucas Santos

  Kubernetes is a very helpful tool for cloud-native developers. But it doesn''t cover
  all the bases on its own – there are some things that Kubernetes cannot solve or
  that are outside its scope.

  This is one of the reasons why open sourc...'
---

By Lucas Santos

[Kubernetes](https://azure.microsoft.com/services/kubernetes-service/?WT.mc_id=containers-19838-ludossan) is a very helpful tool for cloud-native developers. But it doesn't cover all the bases on its own – there are some things that Kubernetes cannot solve or that are outside its scope.

This is one of the reasons why open source projects are so great. They help amazing tools become even more amazing when we combine them with other awesome open-source tools. And often these tools were developed for the sole purpose of filling the gaps. One of these tools is Helm.

## What is Helm?

[Helm](https://helm.sh) is widely known as "the package manager for [Kubernetes](https://azure.microsoft.com/services/kubernetes-service/?WT.mc_id=containers-19838-ludossan)". Although it presents itself like this, its scope goes way beyond that of a simple package manager. However, let's start at the beginning.

Helm is an open-source project which was originally created by [DeisLabs](https://deislabs.io/) and donated to [CNCF](https://azure.microsoft.com/blog/announcing-cncf/?WT.mc_id=containers-19838-ludossan), which now maintains it. The original goal of Helm was to provide users with a better way to manage all the [Kubernetes](https://azure.microsoft.com/services/kubernetes-service/?WT.mc_id=containers-19838-ludossan) YAML files we create on [Kubernetes](https://azure.microsoft.com/services/kubernetes-service/?WT.mc_id=containers-19838-ludossan) projects.

The path [Helm](https://docs.microsoft.com/azure/aks/kubernetes-helm?WT.mc_id=containers-19838-ludossan) took to solve this issue was to create Helm **[Charts](https://docs.microsoft.com/azure/aks/kubernetes-helm?WT.mc_id=containers-19838-ludossan)**. Each chart is a bundle with one or more [Kubernetes](https://azure.microsoft.com/services/kubernetes-service/?WT.mc_id=containers-19838-ludossan) manifests – a chart can have child charts and dependent charts as well. 

This means that Helm installs the whole dependency tree of a project if you run the install command for the top-level chart. You just a single command to install your entire application, instead of listing the files to install via `kubectl`.

[Charts](https://docs.microsoft.com/azure/aks/kubernetes-helm?WT.mc_id=containers-19838-ludossan) allow you to version your manifest files too, just like we do with Node.js or any other package. This lets you install specific chart versions, which means keeping specific configurations for your infrastructure in the form of code. 

Helm also keeps a release history of all deployed charts, so you can go back to a previous release if something went wrong.

[Helm](https://docs.microsoft.com/azure/aks/kubernetes-helm?WT.mc_id=containers-19838-ludossan) supports [Kubernetes](https://azure.microsoft.com/services/kubernetes-service/?WT.mc_id=containers-19838-ludossan) natively, which means you don't have to write any complex syntax files or anything to start using Helm. Just drop your template files into a new chart and you're good to go.

But why should we use it? Managing application manifests can be easily done with a few combinations of commands.

## Why Should You Use Helm?

Helm really shines where Kubernetes didn't go. For instance, templating. The scope of the Kubernetes project is to deal with your containers for you, not your template files. 

This makes it overly difficult to create truly generic files to be used across a large team or a large organization with many different parameters that need to be set for each file. 

And also, how do you version sensitive information using Git when template files are plain text?

The answer: Go templates. Helm allows you to add variables and use functions inside your template files. This makes it perfect for scalable applications that'll eventually need to have their parameters changed. Let's look at an example.

I have an open-source project called [Zaqar](https://github.com/khaosdoctor/zaqar/), a simple email microservice for Node.js which communicates with SendGrid. The project is basically composed of a service, a deployment and an autoscaler. 

Let's take the deployment file as the example. I'd have something like this:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: zaqar
  namespace: default
  labels:
    app: zaqar
    version: v1.0.0
    env: production
spec:
  replicas: 1
  selector:
    matchLabels:
      app: zaqar
      env: production
  template:
    metadata:
      labels:
        app: zaqar
        version: v1.0.0
        env: production
    spec:
      containers:
        - name: zaqar
          image: "khaosdoctor/zaqar:v1.0.0"
          imagePullPolicy: IfNotPresent
          env:
            - name: SENDGRID_APIKEY
              value: "MY_SECRET_KEY"
            - name: DEFAULT_FROM_ADDRESS
              value: "my@email.com"
            - name: DEFAULT_FROM_NAME
              value: "Lucas Santos"
          ports:
            - name: http
              containerPort: 3000
              protocol: TCP
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 250m
              memory: 256Mi
```

If I wanted to use this template on a [CI pipeline](https://docs.microsoft.com/learn/modules/aks-deployment-pipeline-github-actions/?WT.mc_id=containers-19838-ludossan), or publish it on my [GitHub](https://github.com/khaosdoctor), I'd need to replace the variable parts with placeholders. So we can replace these texts with the required information. 

In this case, both the version tag, the `env` label, and the environment variables would be replaced by placeholders, like this:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: zaqar
  namespace: default
  labels:
    app: zaqar
    version: #!VERSION!#
    env: #!ENV!#
spec:
  replicas: 1
  selector:
    matchLabels:
      app: zaqar
      env: #!ENV!#
  template:
    metadata:
      labels:
        app: zaqar
        version: #!VERSION!#
        env: #!ENV!#
    spec:
      containers:
        - name: zaqar
          image: "khaosdoctor/zaqar:#!VERSION!#"
          imagePullPolicy: IfNotPresent
          env:
            - name: SENDGRID_APIKEY
              value: "#!SENDGRID_KEY!#"
            - name: DEFAULT_FROM_ADDRESS
              value: "#!FROM_ADDR!#"
            - name: DEFAULT_FROM_NAME
              value: "#!FROM_NAME!#"
          ports:
            - name: http
              containerPort: 3000
              protocol: TCP
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 250m
              memory: 256Mi
```

We can now run our [CI pipeline](https://docs.microsoft.com/learn/modules/aks-deployment-pipeline-github-actions/?WT.mc_id=containers-19838-ludossan). But before we do that, we need to replace our placeholders with the actual values. 

For this we can use `sed` and its "super easy" syntax `sed 's/#!PLACEHOLDER!#/replacement/g'`, and pipe this down until we finish all the placeholders. The final command would be something like this:

```bash
cat deploy.yaml | \
    sed 's/#!ENV!#/production/g' | \
    sed 's/#!VERSION!#/v1.0.0/g' | \
    sed 's/#!SENDGRID_KEY!#/MyKey/g' | \
    sed 's/#!FROM_ADDR!#/my@email.com/g' | \
    sed 's/#!FROM_NAME!#/Lucas Santos/g'
```

By default, sed outputs everything to the `stdout`, so we can add another pipe to `kubectl -f`, like `<all the command from before> | kubectl -f -`. Then we'll have our deployment in place. The only problem is that we need to do the same for **all** the other files. 

Now imagine a larger project, with lots of other variables and placeholders. You'd probably write a script to do it for you, wouldn't you? That script is Helm.

When you create a Chart (more on this later on), we have a specific directory tree that we must follow so Helm understands what we want to do. Inside the `templates` directory, we can add our manifest files, **with native go templating,** like this:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Values.name }}
  namespace: {{ default .Release.Namespace .Values.namespace }}
  labels:
    app: {{ .Values.name }}
    version: {{ .Values.image.tag }}
    env: {{ .Values.env }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ .Values.name }}
      env: {{ .Values.env }}
  template:
    metadata:
      labels:
        app: {{ .Values.name }}
        version: {{ .Values.image.tag }}
        env: {{ .Values.env }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: "khaosdoctor/zaqar:{{ .Values.image.tag }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          env:
            - name: SENDGRID_APIKEY
              value: {{ required "You must set a valid Sendgrid API key" .Values.environment.SENDGRID_APIKEY | quote }}
            - name: DEFAULT_FROM_ADDRESS
              value: {{ required "You must set a default from address" .Values.environment.DEFAULT_FROM_ADDRESS | quote }}
            - name: DEFAULT_FROM_NAME
              value: {{ required "You must set a default from name" .Values.environment.DEFAULT_FROM_NAME | quote }}
          ports:
            - name: http
              containerPort: 3000
              protocol: TCP
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
```

All those values can be obtained from a `Values.yaml` file (for default values), or you can set them in the CLI using the `--set <path> value` flag. 

If we want to install our chart we can issue the following command:

```bash
helm upgrade --install --create-namespace myChart ./path/to/my/chart \
  --set image.tag=v1.0.0 \
  --set env=production \
  --set environment.SENDGRID_APIKEY=myKey \
  --set environment.DEFAULT_FROM_ADDRESS="my@email.com" \
  --set environment.DEFAULT_FROM_NAME="Lucas Santos"
```

Helm also allows us to use functions inside our deployments. So we can have `default` functions to fallback to default values if they're not filled, like the namespace. Or we can have `required` which displays a message and fails to install the chart if the value is not provided, which is the case of our environment variables.

There are a lot of other useful functions in their [docs](https://helm.sh/docs/chart_template_guide/) - check 'em out.

Now we are able to not only more efficiently manage our application's resources, but also to publish these resources in an open-source version system without any hassle or security issue.

## How to Create a Helm Chart

It's pretty easy to create a chart in Helm. First, you need to have [Helm installed](https://helm.sh/docs/intro/quickstart/). Then, just type in `helm create <chart name>` and it will create a directory filled with files and other directories. Those files are required for Helm to create a chart. 

Let's take a closer look at what this file tree looks like and what the files are within it:

* **chart.yaml:** This is where you'll put the information related to your chart. That includes the chart version, name, and description so you can find it if you publish it on an open repository. Also in this file you'll be able to set external [dependencies](https://helm.sh/docs/topics/charts/#chart-dependencies) using the `dependencies` key.
* **values.yaml**: Like we saw before, this is the file that contains defaults for variables.
* **templates (dir):** This is the place where you'll put all your manifest files. Everything in here will be passed on and created in Kubernetes.
* **charts:** If your chart depends on another chart you own, or if you don't want to rely on Helm's default library (the default registry where Helm pull charts from), you can bring this same structure inside this directory. Chart dependencies are installed from the bottom to the top, which means if chart A depends on chart B, and B depends on C, the installation order will be C ->B ->A.

There are other fields, but these are the most common, and they're the required ones. You can take a quick look at [Zaqar's repository](https://github.com/khaosdoctor/zaqar/tree/master/helm) to check on how we can publish open source charts.

A quick note: When installing Helm, make sure you're installing version 3. Version 2 still works, but it needs a server-side component called Tiller, which ties your helm installation to a single cluster. Helm 3 removed this need with the addition of several CRDs, but it's not supported in all Kubernetes versions.

## How to Host a Helm Chart

Ok, you created your chart, now what? Do we have to download the entire repository to install those charts? No! Helm has a [public library for the most used charts](https://artifacthub.io/), which kind of works like Docker Hub. 

You can also create your own chart repository and [host it online](https://helm.sh/docs/topics/chart_repository/). Helm drinks from the same fountain as HomeBrew, or Linux. You can tap these repositories to download charts contained in them. 

Since a chart repository is basically an `index.yaml` file served from a static web server, you can pretty much create a chart repository out of anywhere.

Take [Zaqar](https://github.com/khaosdoctor/zaqar/tree/master/helm), for example – it's hosted on GitHub Pages and is accessible through [my domain](https://lsantos.me/zaqar/helm/index.yaml). When Helm looks for an `index.yaml` file it's actually looking for the list of available versions of that chart, their SHA256 digests, and the location of the packaged `.tgz` file to download the chart itself. This is pretty much what NPM does under the hood (overly simplified).

This means you don't need to have your repository cloned forever, and your charts can be private as well. You only need to create a chart repository. 

You can even use [hosted services like Azure CR](https://docs.microsoft.com/azure/container-registry/container-registry-helm-repos?WT.mc_id=containers-19838-ludossan) to do the job, or you can have a full solution called [Chart Museum](https://github.com/helm/chartmuseum), which allows you to store your charts and provides you with a neat UI.

## Conclusion

Helm is here to stay. It has helped and will help a lot of Kubernetes developers out there for a long time. 

If you want to know how to use Helm, you can refer to their [docs](https://helm.sh), or you can take this [free learn module](https://docs.microsoft.com/learn/modules/aks-app-package-management-using-helm/?WT.mc_id=containers-19838-ludossan) on how to deploy your applications on Kubernetes the easy way with Helm.

