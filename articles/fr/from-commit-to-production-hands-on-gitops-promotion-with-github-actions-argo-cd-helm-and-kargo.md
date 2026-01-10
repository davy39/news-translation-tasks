---
title: 'Du Commit à la Production : Promotion GitOps Pratique avec GitHub Actions,
  Argo CD, Helm et Kargo'
subtitle: ''
author: Nitheesh Poojary
co_authors: []
series: null
date: '2025-06-05T19:34:08.997Z'
originalURL: https://freecodecamp.org/news/from-commit-to-production-hands-on-gitops-promotion-with-github-actions-argo-cd-helm-and-kargo
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1749151777327/ece5b0b7-4a9a-4f95-8ebb-32e3768b678f.png
tags:
- name: gitops
  slug: gitops
- name: GitHub
  slug: github
- name: GitHub Actions
  slug: github-actions
seo_title: 'Du Commit à la Production : Promotion GitOps Pratique avec GitHub Actions,
  Argo CD, Helm et Kargo'
seo_desc: 'Have you ever wanted to go beyond ‘hello world’ and build a real, production-style
  CI/CD pipeline – starting from scratch?

  Let’s pause for a moment: what are you trying to learn from your DevOps journey?
  Are you focusing on GitOps-style deployments, ...'
---

Avez-vous déjà voulu aller au-delà du "hello world" et construire un pipeline CI/CD réel, de style production, à partir de zéro ?

Faisons une pause un instant : que cherchez-vous à apprendre de votre parcours DevOps ? Vous concentrez-vous sur les déploiements de style GitOps ou sur les promotions ? Ce guide vous aidera à tout aborder, une étape à la fois.

En tant qu'ingénieur DevOps intéressé par la création d'un pipeline CI/CD complet, je voulais plus qu'un microservice "hello world" de base. Je cherchais un projet où je pourrais partir de zéro, en commençant par le code source brut, en écrivant mes propres fichiers Docker Compose et Kubernetes, en déployant localement, puis en ajoutant l'automatisation, la promotion des environnements et les pratiques GitOps étape par étape.

Dans ma recherche, j'ai trouvé plusieurs dépôts GitHub. La plupart étaient soit trop simples pour être utiles, soit trop compliqués et déjà configurés, ne laissant aucune place à l'apprentissage. Ils incluaient souvent des fichiers Docker Compose et des manifests Kubernetes prêts à l'emploi, ce qui n'aidait pas à apprendre par l'expérience pratique.

C'est alors que j'ai découvert **Craftista**, un projet maintenu par [Gourav Shah](https://www.linkedin.com/in/gouravshah/). Ce n'était pas juste un autre dépôt de formation. Comme décrit dans sa documentation :

> *"Craftista n'est pas votre application hello world typique ou une application WordPress prête à l'emploi utilisée dans la plupart des formations DevOps. C'est le vrai truc."*

![Craftista](https://cdn.hashnode.com/res/hashnode/image/upload/v1748210412834/5ef3f2b6-029d-4967-b6a9-825888b44706.png align="left")

Craftista s'est distingué pour plusieurs raisons :

* C'est une **application de microservices polyglottes**, conçue pour ressembler à une plateforme réelle.

* Chaque service utilise sa propre pile technologique, exactement comme dans les entreprises modernes.

* Il inclut les éléments essentiels d'un système de commerce électronique réel :

  * Une interface utilisateur moderne construite en Node.js

  * Un service de catalogue de produits

  * Un moteur de recommandation

  * Un service de vote/avis

À la fin de ce guide, vous n'aurez pas seulement une démonstration "hello world", vous aurez un pipeline CI/CD/GitOps entièrement fonctionnel, modélisé sur une pile de microservices réelle. Vous comprendrez comment les pièces s'emboîtent, pourquoi chaque outil existe et comment adapter ce flux de travail à vos propres projets.

Prêt à aller au-delà de "hello world" et à construire un pipeline de style production à partir de zéro ? Plongeons-nous.

## [Table des matières](#heading-table-des-matieres)

* [Prérequis et ce que vous apprendrez](#heading-prerequis-et-ce-que-vous-apprendrez)

* [Sujets hors du cadre de ce guide](#heading-sujets-hors-du-cadre-de-ce-guide)

* [Qu'est-ce que GitOps ?](#heading-quest-ce-que-gitops)

  * [Principes de base de GitOps](#heading-principes-de-base-de-gitops)

* [Outils que nous utilisons dans ce guide](#heading-outils-que-nous-utilisons-dans-ce-guide)

  * [GitHub Actions](#heading-github-actions)

  * [Minikube](#heading-minikube)

  * [Argo CD](#heading-argo-cd)

  * [Kargo](#heading-kargo)

* [Comment structurer les dépôts pour les applications de microservices](#heading-comment-structurer-les-depots-pour-les-applications-de-microservices)

  * [Pourquoi un Polyrepo convient à mon application de microservices](#heading-pourquoi-un-polyrepo-convient-a-mon-application-de-microservices)

  * [Le branchement Git est un anti-pattern pour les principes GitOps](#heading-le-branchement-git-est-un-anti-pattern-pour-les-principes-gitops)

* [Comment organiser les manifests Kubernetes pour GitOps](#heading-comment-organiser-les-manifests-kubernetes-pour-gitops)

  * [Dossiers Argo CD](#heading-dossiers-argo-cd)

  * [2. Manifests d'application Argo CD (par environnement)](#heading-2-manifests-dapplication-argo-cd-par-environnement)

  * [Dossiers Env](#heading-dossiers-env)

  * [Dossiers Kargo](#heading-dossiers-kargo)

* [Comment déployer et promouvoir votre application de microservices Craftista](#heading-comment-deployer-et-promouvoir-votre-application-de-microservices-craftista)

  * [Prérequis](#heading-prerequis)

  * [1. Démarrer Minikube](#heading-1-demarrer-minikube)

  * [2. Installer Argo CD](#heading-2-installer-argo-cd)

  * [3. Accéder à l'interface utilisateur d'Argo CD](#heading-3-acceder-a-linterface-utilisateur-dargo-cd)

  * [4. Définir un projet Argo CD "Craftista"](#heading-4-definir-un-projet-argo-cd-craftista)

  * [5. Déployer l'environnement de développement](#heading-5-deployer-lenvironnement-de-developpement)

  * [6. Promotion manuelle (Staging & Prod)](#heading-6-promotion-manuelle-staging-amp-prod)

  * [7. Promotion automatisée avec Kargo](#heading-7-promotion-automatisee-avec-kargo)

* [Lectures et ressources supplémentaires](#heading-lectures-et-ressources-supplementaires)

* [Conclusion](#heading-conclusion)

## Prérequis et ce que vous apprendrez :

Avant de progresser dans ce guide, demandez-vous :

* Comprends-je comment le marquage sémantique améliore la traçabilité entre les environnements ?

* Puis-je reproduire une configuration GitOps multi-environnements en utilisant Helm et Kubernetes ?

* Suis-je confiant dans l'organisation des charts Helm et des manifests pour des déploiements scalables ?

* Sais-je comment Kargo et Argo CD fonctionnent ensemble pour automatiser les promotions et les approbations ?

Ce guide vous aidera à répondre à ces questions en vous guidant à travers :

* ✅ Une stratégie de branchement Git optimisée : utilisation de branches de fonctionnalités et d'une seule branche principale

* ✅ Le marquage sémantique des images Docker pour un suivi propre des versions

* ✅ La structuration des charts Helm et des manifests Kubernetes pour GitOps multi-environnements

* ✅ Les pipelines CI utilisant GitHub Actions pour l'automatisation de la construction → test → marquage

* ✅ Les flux de travail GitOps complets avec Kargo et Argo CD pour une promotion et une livraison transparentes

### **Sujets hors du cadre de ce guide**

* Le déploiement sur des services gérés comme EKS, AKS ou GKE n'est pas inclus. Nous utiliserons Minikube pour le développement local.

* Je suppose que vous êtes déjà familiarisé avec l'écriture de manifests Kubernetes de base. Je n'expliquerai pas les Pods, Services, Déploiements et leurs structures YAML ici.

* Je ne discuterai pas non plus des sujets comme la journalisation, les métriques, le traçage et le durcissement de la sécurité.

* Ce guide ne couvre pas la gestion des secrets et des ConfigMaps et la mise en œuvre de la découverte de services.

* Enfin, nous n'aborderons pas l'installation d'ArgoCD et de Kargo.

## **Qu'est-ce que GitOps ?**

GitOps est une méthode moderne pour gérer les applications et l'infrastructure en utilisant Git comme principale source de vérité. Les développeurs utilisent Git depuis longtemps pour gérer et collaborer sur le code. GitOps va plus loin en incluant la configuration de l'infrastructure, les processus de déploiement et l'automatisation.

En gardant tout, des fichiers Kubernetes et des charts Helm au code d'infrastructure et aux paramètres d'application, dans Git, les équipes disposent d'un système centralisé et versionné qui peut être suivi. Les changements dans Git sont automatiquement mis à jour et synchronisés avec les environnements cibles par des outils GitOps comme Argo CD ou Flux.

### **Principes de base de GitOps**

* Git comme seule source de vérité

* Systèmes déclaratifs

* Déploiements immuables

* Audit centralisé des changements

## **Outils que nous utilisons dans ce guide**

![Outils](https://cdn.hashnode.com/res/hashnode/image/upload/v1748886977153/8d7eb087-8161-431b-b48f-c67d724909b9.png align="center")

### **GitHub Actions**

GitHub Actions est une plateforme d'intégration et de livraison continues (CI/CD) qui aide à automatiser vos processus de construction, de test et de déploiement.

Dans notre projet, nous l'utiliserons pour stocker le code de notre application de microservices. Nous utiliserons les workflows GitHub Actions pour construire et pousser des images Docker vers Docker Hub en tant que registre Docker. Nous compterons sur GitHub Actions pour la livraison continue.

### **Minikube**

Nous déployons notre application et ArgoCD localement sur Minikube. Pour simuler la promotion entre différents environnements, j'utilise des namespaces.

### **Argo CD**

Argo CD est un outil de déploiement continu GitOps déclaratif pour Kubernetes qui automatise le déploiement et la synchronisation des applications de microservices avec les dépôts Git. Il suit les principes GitOps et utilise des configurations déclaratives avec une approche basée sur la pull.

![Flux ArgoCD](https://cdn.hashnode.com/res/hashnode/image/upload/v1748345707461/f7484475-8867-48af-a36e-e97d68683a45.png align="left")

Voici un résumé du flux représenté dans l'image ci-dessus :

1. Le développeur modifie le code de l'application et les changements sont poussés vers un dépôt Git.

2. Le pipeline CI est déclenché et construit une nouvelle image de conteneur et la pousse vers un registre de conteneurs.

3. La fusion déclenche un webhook pour notifier Argo CD des changements dans le dépôt Git.

4. Argo CD clone le dépôt Git mis à jour. Compare l'état souhaité (à partir de Git) avec l'état actuel dans le cluster Kubernetes.

5. Argo CD applique les changements nécessaires pour amener le cluster à l'état souhaité.

6. Les contrôleurs Kubernetes réconcilient les ressources jusqu'à ce que le cluster corresponde à la configuration souhaitée.

7. Argo CD surveille en continu l'état de l'application et du cluster.

8. Argo CD peut automatiquement ou manuellement revenir en arrière pour correspondre à la configuration Git, garantissant que Git reste la seule source de vérité.

### **Kargo**

Kargo gère la promotion en surveillant les dépôts (Git, Image, Helm) pour les changements et en effectuant les commits nécessaires dans votre dépôt Git, tandis qu'Argo CD s'occupe de la réconciliation. Kargo est conçu pour simplifier la promotion multi-étapes des applications en utilisant les principes GitOps, éliminant le besoin d'automatisation personnalisée ou de pipelines CI.

![Kargo (Source : Blog Akuity)](https://cdn.hashnode.com/res/hashnode/image/upload/v1748373053736/6c015e27-b47b-486a-bb6a-e581b0f29a30.webp align="left")

#### **Composants de Kargo**

1. **Warehouse** : Surveille les registres d'images et découvre de nouvelles images de conteneurs. Surveille DockerHub pour de nouvelles balises comme `v1.2.0`, `v1.2.1`, etc., et stocke les métadonnées sur les images découvertes.

2. **Stage** : Définit un environnement de déploiement (Dev, Stage, Prod). Lorsqu'une nouvelle image est trouvée par le warehouse, elle met à jour le manifest sous `env/dev/` avec la nouvelle balise d'image. Cela déclenche Argo CD pour synchroniser l'environnement `dev`.

3. **PromotionPolicy** : Définit comment la promotion doit se faire entre les stages (par exemple, auto ou manuel).

4. **Freight** : Une version d'artefact à promouvoir (par exemple, une image de conteneur ou un chart Helm spécifique). Lorsque `v1.2.1` est découvert par le warehouse, un nouveau **Freight** est créé.

![Composants de Kargo](https://cdn.hashnode.com/res/hashnode/image/upload/v1748373806449/00c7a2e5-48af-43b9-b9fc-9463b55c1abb.png align="left")

#### **Exemples pratiques**

* Une nouvelle image `v1.2.0` est poussée vers DockerHub.

* Kargo la détecte via un **warehouse** et met à jour l'environnement `dev`.

* Une fois vérifiée (par des tests ou des métriques), Kargo met automatiquement à jour les valeurs Helm dans le dépôt Git pour le staging.

* Argo CD voit le changement Git et synchronise la nouvelle version vers le staging.

* Une approbation manuelle (via Slack ou UI) est requise pour pousser vers la production.

#### **Pourquoi Kargo est le compagnon parfait d'Argo CD**

Avez-vous déjà dû promouvoir manuellement des versions entre les environnements et souhaité que cela soit automatisé ? Comment l'intégration de Kargo aurait-elle permis de gagner du temps ou d'éviter des erreurs dans votre dernier déploiement ?

Argo CD excelle dans le déploiement continu piloté par GitOps, synchronisant votre cluster Kubernetes avec l'état souhaité déclaré dans Git. Mais il manque de support natif pour les workflows de promotion entre les environnements (comme dev → staging → production) basés sur les métadonnées d'image, les résultats de tests ou les portes d'approbation. C'est là que Kargo devient le compagnon parfait.

![Comparaison Kargo et Argo CD](https://cdn.hashnode.com/res/hashnode/image/upload/v1748474195349/8e615222-067e-4958-aa8c-19a9f44e4d74.png align="left")

Kargo ne remplace pas Argo CD, il l'étend. Vous continuez à utiliser Argo CD pour la synchronisation et le déploiement des applications, mais Kargo ajoute l'intelligence et l'automatisation de la promotion.

## **Comment structurer les dépôts pour les applications de microservices**

Mon application exemple se compose de 4 microservices ([frontend](https://github.com/nitheeshp-irl/microservice-frontend), [recommendation](https://github.com/nitheeshp-irl/microservice-recommendation), [catalogues](https://github.com/nitheeshp-irl/microservice-catalogue), et [voting](https://github.com/nitheeshp-irl/microservice-voting)). Concevoir la structure de votre dépôt est très important pour démarrer votre projet. Il y a beaucoup de débats entre monorepo et multi-service repo.

Un **monorepo** est un dépôt unifié qui abrite tout le code pour un projet ou un ensemble de projets liés. Il consolide le code de divers services, bibliothèques et applications en un seul emplacement centralisé.

D'autre part, une architecture **polyrepo** comprend plusieurs dépôts, chacun contenant le code pour un service, une bibliothèque ou un composant d'application distinct.

### **Pourquoi un Polyrepo convient à mon application de microservices**

Imaginez que vous intégrez une nouvelle équipe à votre application. Préféreriez-vous leur donner accès à un monorepo entier ou seulement au dépôt du service pertinent ? Quels compromis êtes-vous prêt à accepter ?

Eh bien, en utilisant une approche polyrepo,

* Les équipes peuvent travailler indépendamment sur le frontend, les recommandations, les catalogues et le vote sans se marcher sur les pieds.

* Les services sensibles restent verrouillés sans règles complexes au niveau des répertoires.

* Les runners CI fonctionnent sur une base de code plus petite, accélérant les checkouts et réduisant la bande passante.

* Chaque service a son propre rythme de publication (par exemple, `catalogues` v2.1.0 et `voting` v1.7.3).

* À mesure que votre organisation grandit, de nouvelles équipes peuvent s'intégrer uniquement aux dépôts qui les intéressent.

* Les bibliothèques partagées peuvent être versionnées et publiées dans un registre de packages interne, puis consommées par chaque service.

### **Le branchement Git est un anti-pattern pour les principes GitOps**

![Git Branching AntiPattern](https://cdn.hashnode.com/res/hashnode/image/upload/v1748376156187/f1fb6cc6-c5d1-4001-a8a1-63353cc03cd7.png align="left")

De nombreuses équipes utilisent par défaut le style de branchement "[**GitFlow**](https://medium.com/novai-devops-101/understanding-gitflow-a-simple-guide-to-git-branching-strategy-4f079c12edb9)" – créant des branches à longue durée de vie pour `dev`, `staging`, `prod`, et plus. Mais dans un flux de travail GitOps véritable, **Git est votre plan de contrôle**, et les "environnements" ne devraient pas exister en tant que branches.

Au lieu de cela, vous pouvez garder les choses simples avec juste :

* Une branche `master` (ou `main`) à longue durée de vie

* Des branches de fonctionnalités à courte durée de vie pour le travail de code

## **Comment organiser les manifests Kubernetes pour GitOps**

[Ce dépôt](https://github.com/nitheeshp-irl/microservice-helmcharts) montre comment vous pouvez garder les manifests d'application ArgoCD, les valeurs spécifiques à l'environnement, les tâches de promotion Kargo, les charts Helm pour chaque microservice, et les workflows CI/CD tous au même endroit. Il est organisé de sorte que :

1. **Les manifests d'application ArgoCD** vivent sous `argocd/`, divisés par environnement (par exemple, `dev/`, `staging/`, `prod/`).

2. **Les remplacements spécifiques à l'environnement** (valeurs Helm ou correctifs Kustomize) vont sous `env/`.

3. **Les configurations de promotion Kargo** sont regroupées sous `kargo/`, définissant comment les nouvelles images passent entre les environnements.

4. **Les charts Helm de service** résident dans `service-charts/`, un chart par microservice.

```markdown
/microservice-helmcharts/
├── argocd/                # Manifests d'application ArgoCD
│   ├── application/       # Définitions d'application
│   │   ├── dev/           # Applications d'environnement de développement
│   │   │   ├── catalogue.yaml
│   │   │   ├── catalogue-db.yaml
│   │   │   ├── frontend.yaml
│   │   │   ├── recommendation.yaml
│   │   │   ├── voting.yaml
│   │   │   └── kustomization.yaml
│   │   ├── staging/       # Applications d'environnement de staging
│   │   │   └── [structure similaire à dev]
│   │   ├── prod/          # Applications d'environnement de production
│   │   │   └── [structure similaire à dev]
│   │   └── craftista-project.yaml
│   ├── blog-post.md
│   ├── deployment-guide-blog.md
│   └── repository-structure.md
├── env/                   # Configurations spécifiques à l'environnement
│   ├── dev/               # Valeurs d'environnement de développement
│   │   ├── catalogue/
│   │   │   └── catalogue-values.yaml
│   │   ├── catalogue-db/
│   │   │   └── catalogue-db-values.yaml
│   │   ├── frontend/
│   │   │   └── frontend-values.yaml
│   │   ├── recommendation/
│   │   │   └── recommendation-values.yaml
│   │   ├── voting/
│   │   │   └── voting-values.yaml
│   │   └── kustomization.yaml
│   ├── staging/           # Structure similaire à dev mais avec des fichiers d'image
│   └── prod/              # Structure similaire à staging
├── kargo/                 # Configuration de promotion Kargo
│   ├── catalogue-config/  # Promotion du service de catalogue
│   │   ├── catalogue-promotion-tasks.yaml
│   │   ├── catalogue-stages.yaml
│   │   └── catalogue-warehouse.yaml
│   ├── frontend-config/   # Promotion du service frontend
│   │   ├── frontend-promotion-tasks.yaml
│   │   ├── frontend-stages.yaml
│   │   └── frontend-warehouse.yaml
│   ├── recommendation-config/ # Promotion du service de recommandation
│   │   ├── recommendation-promotion-tasks.yaml
│   │   ├── recommendation-stages.yaml
│   │   └── recommendation-warehouse.yaml
│   ├── voting-config/     # Promotion du service de vote
│   │   ├── voting-promotion-tasks.yaml
│   │   ├── voting-stages.yaml
│   │   └── voting-warehouse.yaml
│   ├── kargo.yaml         # Application ArgoCD pour Kargo
│   ├── kustomization.yaml # Combine toutes les ressources
│   ├── project.yaml       # Définition du projet Kargo
│   └── projectconfig.yaml # Politiques de promotion à l'échelle du projet
├── service-charts/        # Charts Helm pour chaque microservice
│   ├── catalogue/         # Chart du service de catalogue
│   │   ├── templates/
│   │   │   ├── deployment.yaml
│   │   │   └── service.yaml
│   │   ├── Chart.yaml
│   │   └── values.yaml
│   ├── catalogue-db/      # Structure similaire à catalogue
│   ├── frontend/          # Structure similaire à catalogue
│   ├── recommendation/    # Structure similaire à catalogue
│   └── voting/            # Structure similaire à catalogue
├── .github/workflows/     # Workflows CI/CD
│   └── docker-ci.yml      # Construction et poussée de l'image Docker
└── README.md              # Documentation du dépôt
```

### **Dossiers Argo CD**

Le répertoire `argocd/` contient tous les manifests dont Argo CD a besoin pour suivre, regrouper et déployer vos microservices. Dans ce guide, nous divisons ce répertoire en deux parties principales :

1. **Définition du projet Argo CD**

2. **Manifests d'application Argo CD (organisés par environnement)**

#### [**Projets ArgoCD**](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/)

Avant de pouvoir donner à Argo CD un ensemble d'applications à gérer, il est souvent considéré comme une bonne pratique de définir un "Projet". Un Projet dans Argo CD sert de frontière logique autour d'un groupe d'applications. Il peut contrôler quels dépôts Git ces applications sont autorisées à référencer, quels clusters/namespaces Kubernetes elles peuvent cibler, et même quels types de ressources elles peuvent gérer.

Dans notre dépôt exemple, le fichier `craftisia-project.yaml` se trouve au sommet de `argocd/` :

```yaml
# argocd/craftisia-project.yaml
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: craftisia
  namespace: argocd
spec:
  # 1) Quels dépôts Git sommes-nous autorisés à tirer ?
  sourceRepos:
    - "https://github.com/nitheeshp-irl/microservice-helmcharts"
    # (Ou vous pourriez utiliser "*" pour permettre n'importe quel dépôt, mais c'est moins sécurisé.)

  # 2) Quels clusters/namespaces ces Apps peuvent-ils être déployés ?
  destinations:
    - namespace: "*"
      server: "*"    # Permettre le déploiement sur n'importe quel cluster (pour une démonstration locale Minikube, c'est bien).

  # 3) Quels types de ressources Kubernetes peuvent être créés/mis à jour ?
  #    (Par exemple, nous voulons des Pods, Services, Déploiements, Ingresses, etc.)
  #    Argo CD rejettera tout manifest contenant un type non autorisé.
  clusterResourceWhitelist:
    - group: ""            # groupe d'API core (Pods, Services, ConfigMaps, etc.)
      kind: Pod
    - group: "apps"        # déploiements, statefulsets, etc.
      kind: Deployment
    - group: "networking.k8s.io"
      kind: Ingress
    # (Vous pouvez lister des types de ressources supplémentaires si nécessaire.)

  # 4) Optionnel : définir le contrôle d'accès basé sur les rôles ou les politiques de synchronisation au niveau du projet.
  #    (Non montré ici, mais vous pourriez ajouter des rôles, des quotas de ressources de namespace, etc.)
```

### 2. Manifests d'application Argo CD (par environnement)

À l'intérieur de `argocd/`, il y a un sous-répertoire appelé `application/`. Nous l'utilisons pour garder tous nos YAML d'application Argo CD, divisés par environnement. La disposition de haut niveau ressemble à ceci :

```markdown
rCopyEditargocd/
└── application/
    ├── dev/            # Applications de l'environnement "Dev"
    │   ├── catalogue.yaml
    │   ├── catalogue-db.yaml
    │   ├── frontend.yaml
    │   ├── recommendation.yaml
    │   ├── voting.yaml
    │   └── kustomization.yaml
    ├── staging/        # Applications de l'environnement "Staging" (mêmes noms/structure que dev/)
    │   └── […]
    └── prod/           # Applications de l'environnement "Prod" (mêmes noms/structure que dev/)
        └── […]
```

Chacun de ces fichiers YAML est une **application Argo CD** autonome. Une application indique à Argo CD :

1. À quel projet elle appartient (dans notre cas, `craftisia`),

2. Où trouver ses manifests (un dépôt Git et un chemin),

3. Quel cluster Kubernetes et namespace déployer,

4. Comment se maintenir à jour (c'est-à-dire, les politiques de synchronisation).

Ci-dessous se trouve un exemple du fichier `frontend.yaml` pour l'environnement **dev** :

```markdown
yamlCopyEdit# argocd/application/dev/frontend.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: frontend-dev
  namespace: argocd
spec:
  project: craftisia

  # 1) Source : Où trouver le chart Helm et quel fichier de valeurs utiliser
  source:
    repoURL: https://github.com/nitheeshp-irl/microservice-helmcharts
    targetRevision: main
    path: service-charts/frontend       # Dossier du chart Helm pour le service frontend
    helm:
      valueFiles:
        - ../../env/dev/frontend/frontend-values.yaml

  # 2) Destination : Quel cluster & namespace déployer
  destination:
    server: https://kubernetes.default.svc    # (Suppose qu'Argo CD est en cours d'exécution dans le cluster)
    namespace: front-end-dev                   # Un namespace dédié pour le frontend "dev"

  # 3) Politique de synchronisation : Automatiser la synchronisation et activer l'auto-guérison
  syncPolicy:
    automated:
      prune: true          # Supprimer les ressources qui ne sont plus dans Git
      selfHeal: true       # Si quelqu'un modifie manuellement les ressources en direct, revenir à l'état Git
    syncOptions:
      - CreateNamespace=true  # Si le namespace n'existe pas, Argo CD le créera
```

Vous répéteriez un modèle similaire sous `argocd/application/staging/` et `argocd/application/prod/` – chaque environnement a son propre `frontend.yaml`, `catalogue.yaml`, etc., mais chacun pointera vers un fichier de valeurs différent sous `env/staging/…` ou `env/prod/…` et sera probablement déployé dans un namespace différent (par exemple, `front-end-staging`, `front-end-prod`).

### **Dossiers Env**

Le répertoire `/env` est une partie cruciale de notre implémentation GitOps, contenant toutes les configurations spécifiques à l'environnement pour nos microservices. Chaque environnement (dev, staging, prod) a son propre sous-répertoire contenant des configurations spécifiques au service. Celles-ci contiennent des valeurs générales de **chart Helm** comme les limites de ressources et les comptes de réplicas, ainsi que le dépôt et la balise de l'image du conteneur.

```yaml
image:
  repository: nitheesh86/microservice-frontend
  tag: 1.0.11

replicaCount: 2

resources:
  limits:
    memory: "512Mi"
  requests:
    cpu: "100m"
    memory: "128Mi"
```

### **Dossiers Kargo**

Notre configuration Kargo est organisée dans le répertoire `/kargo` avec plusieurs composants clés :

```markdown
/kargo/
├── catalogue-config/           # Configuration de promotion du service de catalogue
│   ├── catalogue-promotion-tasks.yaml  # Définit comment mettre à jour les images de catalogue
│   ├── catalogue-stages.yaml           # Étapes Dev, staging, prod pour le catalogue
│   └── catalogue-warehouse.yaml        # Surveille le dépôt d'images de catalogue
├── frontend-config/            # Configuration de promotion du service frontend
│   ├── frontend-promotion-tasks.yaml   # Définit comment mettre à jour les images frontend
│   ├── frontend-stages.yaml            # Étapes Dev, staging, prod pour le frontend
│   └── frontend-warehouse.yaml         # Surveille le dépôt d'images frontend
├── recommendation-config/      # Configuration de promotion du service de recommandation
│   ├── recommendation-promotion-tasks.yaml  # Workflow de mise à jour des images
│   ├── recommendation-stages.yaml           # Étapes d'environnement
│   └── recommendation-warehouse.yaml        # Surveillance des images
├── voting-config/              # Configuration de promotion du service de vote
│   ├── voting-promotion-tasks.yaml     # Workflow de mise à jour des images
│   ├── voting-stages.yaml              # Étapes d'environnement
│   └── voting-warehouse.yaml           # Surveillance des images
├── kargo.yaml                  # Application ArgoCD pour l'installation de Kargo
├── kustomization.yaml          # Ce fichier - combine toutes les ressources
├── project.yaml                # Définit le projet Kargo
└── projectconfig.yaml          # Politiques de promotion à l'échelle du projet
```

**Configurations de Stage** : Kargo utilise le concept de "stages" pour représenter nos environnements de déploiement. Chaque stage définit :

* Quel fret (images de conteneurs) déployer

* Le workflow de promotion à exécuter

* Les variables spécifiques à l'environnement

**Configuration de Warehouse** : Le warehouse surveille notre registre de conteneurs pour de nouvelles images.

**Tâches de Promotion** : Les tâches de promotion définissent le workflow réel pour la promotion entre les environnements.

## Comment déployer et promouvoir votre application de microservices Craftista

Maintenant, je vais expliquer comment déployer votre application de microservices Craftista en utilisant Argo CD.

![Tableau de bord ArgoCD](https://cdn.hashnode.com/res/hashnode/image/upload/v1748558624685/9f0d5725-cc8a-4e37-851c-d4ab2870bafc.png align="center")

### **Prérequis**

* **Un cluster Kubernetes local** : Nous utiliserons Minikube pour le développement local.

* **kubectl et helm** : Assurez-vous que les deux sont installés et configurés.

* **Clone Git du dépôt microservice-helmcharts** :

  ```bash
  git clone https://github.com/nitheeshp-irl/microservice-helmcharts.git
  cd microservice-helmcharts
  ```

### **1. Démarrer Minikube**

Démarrez Minikube avec les ressources spécifiées :

```bash
minikube start --memory=4096 --cpus=2
kubectl config use-context minikube
```

Ajustez `--memory` et `--cpus` selon les besoins de votre machine.

### **2. Installer Argo CD**

Créez un namespace :

```bash
kubectl create namespace argocd
```

Appliquez le manifest d'installation officiel :

```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### **3. Accéder à l'interface utilisateur d'Argo CD**

Port-forward le serveur :

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

**Connexion** :

* **Nom d'utilisateur** : admin

* **Mot de passe** :

  ```bash
  kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
  ```

Ouvrez votre navigateur à l'adresse [**http://localhost:8080**](http://localhost:8080/).

### **4. Définir un projet Argo CD "Craftista"**

Définir la portée des dépôts, des clusters et des namespaces :

```bash
kubectl apply -f argocd/application/craftista-project.yaml
```

Vous devriez voir :

```bash
project.argoproj.io/craftista created
```

### **5. Déployer l'environnement de développement**

Créez des applications Argo CD :

```bash
kubectl apply -f argocd/application/dev/
```

Argo CD va :

* Cloner le dépôt microservice-helmcharts.

* Rendre chaque chart Helm avec son `env/dev/*-values.yaml`.

* Créer Deployment, Service, etc. dans vos namespaces dev.

* Réconcilier en continu l'état souhaité vs l'état réel.

Surveillez votre progression :

```bash
argocd app list
argocd app get frontend-dev
```

### **6. Promotion manuelle (Staging & Prod)**

Modifiez la balise d'image ou d'autres valeurs :

* `env/staging/<service>/<service>-values.yaml`

* `env/prod/<service>/<service>-values.yaml`

Validez et poussez les changements :

```bash
git add env/staging env/prod
git commit -m "Promote v1.2.0 → staging & prod"
git push
```

Argo CD détectera le changement Git et synchronisera automatiquement vos applications staging et prod (si la synchronisation automatique est activée).

### **7. Promotion automatisée avec Kargo**

![Tableau de bord Kargo](https://cdn.hashnode.com/res/hashnode/image/upload/v1748689354529/3759ec0c-7db4-42a8-9f01-f0792dfec895.png align="center")

Tout d'abord, installez Kargo :

```bash
kubectl apply -f kargo/kargo.yaml
```

Configurez les tâches de promotion, les stages et le warehouse :

```bash
kubectl apply -k kargo/

apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
  - project.yaml
  - projectconfig.yaml
  - catalogue-config/catalogue-warehouse.yaml
  - catalogue-config/catalogue-stages.yaml
  - catalogue-config/catalogue-promotion-tasks.yaml
  - frontend-config/frontend-warehouse.yaml
  - frontend-config/frontend-stages.yaml
  - frontend-config/frontend-promotion-tasks.yaml
  - recommendation-config/recommendation-warehouse.yaml
  - recommendation-config/recommendation-stages.yaml
  - recommendation-config/recommendation-promotion-tasks.yaml
  - voting-config/voting-warehouse.yaml
  - voting-config/voting-stages.yaml
  - voting-config/voting-promotion-tasks.yaml
```

## Comment fonctionne le pipeline GitOps

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748885521249/285bcaed-447d-4a31-87cb-98b531d9cb0d.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1748557162526/f4716cfc-a71f-4ddc-bc58-7a42118c3190.png align="center")

1. **Le développeur ouvre une Pull Request** : Le parcours commence lorsque un développeur ouvre une pull request sur l'un des dépôts de microservices. Cela signale que du nouveau code (fonctionnalité, correction de bug, changement de configuration) est prêt à être intégré.

2. **CI (GitHub Actions)**

   * **CI : Lint → Test → Build & Tag** : Un seul travail de workflow lint le code, exécute des tests unitaires/intégration, construit l'image Docker et applique une balise sémantique (par exemple, v1.2.0).

   * **CI OK ? (Décision)** :

     * Si **Non**, le pipeline s'arrête et le développeur est notifié pour corriger les erreurs.

     * Si **Oui**, la nouvelle image construite est poussée vers le registre de conteneurs (DockerHub, ECR, etc.).

3. **Kargo**

   * **Warehouse découvre la nouvelle balise d'image** : Le composant Warehouse de Kargo surveille en continu votre registre. Dès qu'il voit la nouvelle balise, il enregistre les métadonnées de l'image.

   * **Mettre à jour les valeurs env/dev → Git** : Kargo effectue automatiquement un commit pour mettre à jour `env/dev/<service>/…-values.yaml`, pointant le fichier de valeurs Helm dev vers la nouvelle balise d'image. Ce commit Git entraînera l'étape suivante.

4. **GitOps (Argo CD)**

5. * **Argo CD sync dev** : Argo CD voit le changement Git dans le fichier de valeurs dev et le tire dans le cluster, réconciliant le namespace dev réel avec l'état souhaité.

   * **Le déploiement dev est-il sain ? (Décision)** :

     * Si **Non**, Argo CD peut éventuellement revenir en arrière et notifier l'équipe (via Slack, email, etc.) de l'échec du déploiement dev.

     * Si **Oui**, il est temps de promouvoir vers le staging.

   * **Mettre à jour les valeurs env/staging → Git** : Kargo (ou vous, si manuel) effectue un commit de la même balise d'image dans `env/staging/<service>/…-values.yaml`.

   * **Argo CD sync staging** : Argo CD déploie ce changement dans le namespace staging.

   * **L'approbation staging est-elle accordée ? (Décision)** :

     * Si **Non**, Kargo attend (et notifie éventuellement) jusqu'à ce qu'une porte manuelle soit levée.

     * Si **Oui**, le commit de promotion final est effectué : mise à jour de `env/prod/<service>/…-values.yaml`.

   * **Argo CD sync prod → Fin** : Argo CD applique le changement de production, complétant le pipeline du commit jusqu'au déploiement en production.

### **Résumé du pipeline**

1. Le développeur ouvre une PR → CI teste et construit → L'image Docker est poussée

2. Le Warehouse Kargo détecte la nouvelle balise → Commit Git vers `env/dev`

3. Argo CD synchronise dev → Vérification de santé → (si réussi) commit vers `env/staging`

4. Argo CD synchronise staging → Approbation → commit vers `env/prod`

5. Argo CD synchronise prod → Déploiement en direct terminé

Chaque étape doit passer sa vérification de santé ou d'approbation avant que la suivante ne commence, garantissant que seul le code soigneusement testé et validé arrive en production.

## Conclusion

Construire un pipeline CI/CD réel ne consiste pas seulement à faire passer du code de votre ordinateur portable à un cluster Kubernetes, mais à créer un système répétable, auditable et fiable qui évolue avec votre équipe et la complexité de votre application.

Dans ce guide, nous avons parcouru comment j'ai construit un pipeline de promotion basé sur GitOps complet en utilisant GitHub Actions, Argo CD et Kargo, le tout piloté par un projet de microservices pratique : Craftista. Du premier commit de code à la promotion automatisée des environnements, nous avons exploité les meilleures pratiques de l'industrie comme le versionnage sémantique, l'infrastructure déclarative et les répertoires GitOps basés sur l'environnement.

Ce qui rend cette approche puissante, ce ne sont pas seulement les outils, mais aussi les principes. En traitant Git comme la seule source de vérité et en utilisant Kargo pour automatiser ce qui était traditionnellement un processus de promotion manuel et fragile, nous gagnons en prévisibilité et en contrôle sur nos déploiements. Argo CD garantit que ce qui est dans Git est toujours ce qui s'exécute dans nos clusters, tandis que Kargo élimine les erreurs humaines dans les déploiements multi-étapes.

Si vous en avez assez des tutoriels DevOps trop abstraits "hello world" et que vous voulez vous salir les mains avec quelque chose qui semble **réel**, Craftista offre le bac à sable parfait. Ce pipeline reflète la manière dont les équipes opèrent en production – services polyglottes, déploiements indépendants, portes de promotion d'environnement et GitOps comme colonne vertébrale opérationnelle.

Que vous soyez un ingénieur DevOps perfectionnant vos compétences ou une équipe de plateforme établissant des normes pour le développement interne, j'espère que ce tutoriel vous a fourni la clarté et l'inspiration pour construire votre propre pipeline de commit à production – étape par étape, avec confiance.

### Lectures et ressources supplémentaires

* [Documentation Argo CD](https://argo-cd.readthedocs.io/)

* [Documentation Kargo](https://docs.kargo.io/)

* [Documentation GitHub Actions](https://docs.github.com/en/actions)

* [Comment modéliser vos environnements GitOps et promouvoir les versions entre eux](https://codefresh.io/blog/how-to-model-your-gitops-environments-and-promote-releases-between-them/)

* [Dépôt Craftista](https://github.com/craftista/craftista)