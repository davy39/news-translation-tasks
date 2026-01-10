---
title: Apprendre Kubernetes et EKS pour le déploiement
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2025-02-20T15:01:53.755Z'
originalURL: https://freecodecamp.org/news/learn-kubernetes-and-eks-for-deployment
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1740063597212/95295b26-4334-4875-ba73-c71218c47b67.png
tags:
- name: Kubernetes
  slug: kubernetes
- name: youtube
  slug: youtube
seo_title: Apprendre Kubernetes et EKS pour le déploiement
seo_desc: Kubernetes has become the de facto standard for container orchestration,
  allowing developers to efficiently deploy, manage, and scale applications. But deploying
  Kubernetes clusters in the cloud can be complex. That’s where Amazon Elastic Kubernetes
  ...
---

Kubernetes est devenu la norme de facto pour l'orchestration de conteneurs, permettant aux développeurs de déployer, gérer et mettre à l'échelle des applications de manière efficace. Mais le déploiement de clusters Kubernetes dans le cloud peut être complexe. C'est là qu'intervient Amazon Elastic Kubernetes Service (EKS), simplifiant la gestion de Kubernetes sur AWS. De plus, des outils d'Infrastructure as Code (IaC) comme Pulumi aident à automatiser et à rationaliser les déploiements cloud.

Nous venons de publier un cours sur la chaîne YouTube [freeCodeCamp.org](http://freeCodeCamp.org) qui vous apprendra tout sur Kubernetes, EKS et Pulumi. J'ai créé ce cours ! Il couvre les bases de Kubernetes, passe en revue un projet Kubernetes simple et explique des concepts clés comme les Pods, les Deployments, les Services et les ConfigMaps. Ensuite, vous plongerez dans Kubernetes dans des applications réelles et apprendrez à déployer des charges de travail Kubernetes sur AWS en utilisant EKS. Enfin, vous explorerez Pulumi, un outil d'Infrastructure as Code, et verrez comment il peut être utilisé pour automatiser les déploiements Kubernetes. Pulumi a fourni une subvention pour rendre ce cours possible.

### Ce que vous apprendrez

#### **Les bases de Kubernetes**

Kubernetes est une plateforme open-source conçue pour automatiser le déploiement, la mise à l'échelle et l'exploitation de conteneurs d'applications. Elle abstrait les détails de l'infrastructure et fournit un moyen déclaratif de gérer les applications. Le cours commence par une introduction à Kubernetes, couvrant des concepts clés tels que :

* **Pods** – L'unité la plus petite déployable dans Kubernetes, qui peut contenir un ou plusieurs conteneurs.

* **Deployments** – Un objet de niveau supérieur qui gère le déploiement et la mise à l'échelle des pods.

* **Services** – Utilisés pour exposer les applications au réseau, garantissant que les utilisateurs et autres services peuvent les atteindre.

* **ConfigMaps et Secrets** – Des outils pour gérer les variables d'environnement et les données sensibles séparément du code de l'application.

#### **Amazon Elastic Kubernetes Service (EKS)**

EKS est un service Kubernetes géré fourni par AWS. Il élimine une grande partie de la complexité liée à la configuration et à la maintenance des clusters Kubernetes. Le cours couvre :

* Comment EKS simplifie la gestion des clusters Kubernetes.

* La configuration et le déploiement d'applications sur EKS.

* La mise à l'échelle et la gestion des charges de travail dans un environnement de production.

#### **Infrastructure as Code avec Pulumi**

Pulumi est un outil moderne d'Infrastructure as Code (IaC) qui permet de définir des ressources cloud à l'aide de langages de programmation comme TypeScript, Python et Go. Contrairement aux outils IaC traditionnels tels que Terraform et CloudFormation, Pulumi permet aux développeurs d'utiliser des paradigmes de programmation familiers pour gérer l'infrastructure. Ce cours couvre :

* Pourquoi Pulumi est une alternative puissante aux solutions IaC traditionnelles.

* Comment créer un projet Pulumi simple.

* Déployer une application réelle (Zephyr App) sur EKS en utilisant Pulumi.

* Utiliser Pulumi Copilot et Pulumi Insights pour améliorer les déploiements cloud.

### Pourquoi suivre ce cours ?

Que vous soyez nouveau dans Kubernetes ou que vous cherchiez à rationaliser vos déploiements AWS avec l'Infrastructure as Code, ce cours offre un guide pratique et concret des stratégies modernes de déploiement cloud. À la fin, vous aurez une solide compréhension des fondamentaux de Kubernetes, de la manière de déployer des charges de travail sur AWS avec EKS, et de l'automatisation de la gestion de l'infrastructure avec Pulumi.

Consultez le cours complet sur la chaîne YouTube [freeCodeCamp.org](https://youtu.be/hK8wf18SasY) et faites passer vos compétences Kubernetes au niveau supérieur !

%[https://youtu.be/hK8wf18SasY]