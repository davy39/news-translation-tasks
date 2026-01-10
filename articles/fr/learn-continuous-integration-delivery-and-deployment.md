---
title: 'Le guide du CI/CD : Apprendre l''Intégration et la Livraison Continues avec
  GitHub Actions, Docker et Google Cloud Run'
date: '2024-12-05T16:21:12.535Z'
author: Prince Onukwili
authorURL: https://www.freecodecamp.org/news/author/onukwilip/
originalURL: https://freecodecamp.org/news/learn-continuous-integration-delivery-and-deployment
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1734119999570/cfbf3375-1e95-41df-b5b0-8fbb8b827f59.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: continuous delivery
  slug: continuous-delivery
- name: continuous deployment
  slug: continuous-deployment
- name: GitHub Actions
  slug: github-actions
- name: CI/CD
  slug: cicd
seo_desc: Hey everyone! 🌟 If you’re in the tech space, chances are you’ve come across
  terms like Continuous Integration (CI), Continuous Delivery (CD), and Continuous
  Deployment. You’ve probably also heard about automation pipelines, staging environments,
  pro...
---


Salut à tous ! 🌟 Si vous évoluez dans le secteur de la tech, il y a de fortes chances que vous ayez rencontré des termes comme **Intégration Continue (CI)**, **Livraison Continue (CD)** et **Déploiement Continu**. Vous avez probablement aussi entendu parler de pipelines d'automatisation, d'environnements de staging, d'environnements de production et de concepts tels que les workflows de test.

<!-- more -->

Ces termes peuvent sembler complexes ou interchangeables au premier abord, vous laissant perplexe : que signifient-ils réellement ? En quoi diffèrent-ils les uns des autres ? 🤔

Dans ce guide, je vais décomposer ces concepts de manière claire et accessible, en m'appuyant sur des analogies parlantes pour rendre chaque terme plus facile à comprendre. 🧠💡 Au-delà de la théorie, nous plongerons dans un tutoriel pratique où vous apprendrez à configurer un workflow CI/CD étape par étape.

Ensemble, nous allons :

-   Configurer un projet Node.js. ✨
    
-   Implémenter des tests automatisés à l'aide de Jest et Supertest. 🛠️
    
-   Configurer un workflow CI/CD utilisant GitHub Actions, déclenché lors d'un push, de pull requests ou après une nouvelle release. ⚙️
    
-   Construire et publier une image Docker de votre application sur Docker Hub. 📦
    
-   Déployer votre application dans un environnement de staging pour les tests. 🚀
    
-   Enfin, la déployer dans un environnement de production pour la mettre en ligne ! 🌐
    

À la fin de ce guide, non seulement vous comprendrez la différence entre les concepts CI/CD, mais vous aurez également une expérience pratique de la construction de votre propre pipeline automatisé. 😃

### Table des matières

1.  [**Qu'est-ce que l'intégration, le déploiement et la livraison continues ?**][1]
    
2.  [**Différences entre l'intégration continue, la livraison continue et le déploiement continu**][2]
    
3.  [**Comment configurer un projet Node.js avec un serveur web et des tests automatisés**][3]
    
4.  [**Comment créer un dépôt GitHub pour héberger votre code**][4]
    
5.  [**Comment configurer les workflows CI et CD dans votre projet**][5]
    
6.  [**Configurer un dépôt Docker Hub pour l'image du projet et générer un jeton d'accès pour publier l'image**][6]
    
7.  [**Créer un compte Google Cloud, un projet et un compte de facturation**][7]
    
8.  [**Créer un compte de service Google Cloud pour permettre le déploiement de l'application Node.js sur Google Cloud Run via le pipeline CD**][8]
    
9.  [**Créer la branche staging et y fusionner la branche feature (Intégration Continue et Livraison Continue)**][9]
    
10.  [**Fusionner la branche staging dans la branche main (Intégration Continue et Déploiement Continu)**][10]
    
11.  [**Conclusion**][11]
    

## **Qu'est-ce que l'intégration, le déploiement et la livraison continues ?** 🤔

### **Intégration Continue (CI)**

Imaginez que vous fassiez partie d'une équipe de six développeurs travaillant tous sur le même projet. Sans un système approprié, ce serait le chaos.

Disons que M. A construit une nouvelle fonctionnalité de connexion, Mme B corrige un bug dans la barre de recherche et M. C ajuste l'interface du tableau de bord — tout cela en même temps. Si tout le monde modifie directement le même "dossier" ou la même base de code, les choses pourraient très mal tourner : _"Hé ! Qui vient de casser l'application ?!"_ 😱

Pour maintenir l'ordre, les équipes utilisent des **systèmes de contrôle de version (VCS)** comme GitHub, GitLab ou BitBucket. Considérez cela comme un espace de travail numérique où tout le monde peut collaborer en toute sécurité sans se marcher sur les pieds. 🗂️✨

Voici comment l'Intégration Continue s'inscrit dans ce processus, étape par étape :

#### 1\. **La branche Main : Le dossier général** ✨

Au cœur de chaque projet se trouve la **branche main** — la source ultime de vérité. Elle contient la base de code stable qui alimente votre application en direct. C'est là que chaque membre de l'équipe apporte son travail, mais avec une règle importante : seul le code testé et approuvé y est fusionné. 🚀

#### 2\. **Branches Feature : Espaces de travail personnels** 🔨

Quand quelqu'un comme M. A veut travailler sur une nouvelle fonctionnalité, il crée une **branche feature**. Cette branche est essentiellement une copie personnelle de la branche main où il peut bricoler, écrire du code et tester sans affecter les autres. Mme B et M. C travaillent également sur leurs propres branches. Les expérimentations de chacun restent soigneusement organisées. 🧪💡

#### 3\. **Fusion des modifications : Le workflow CI** 🎉

Lorsque M. A est satisfait de sa fonctionnalité, il ne se contente pas de l'injecter dans la branche main — la CI garantit que cela est fait en toute sécurité :

-   **Tests automatisés** : Avant la fusion, les outils de CI exécutent automatiquement des tests sur le code de M. A pour vérifier les bugs ou les erreurs. Considérez cela comme un videur gardant la branche main, s'assurant qu'aucun mauvais code n'entre. 🕵️‍♂️
    
-   **Vérification du Build** : Le code de la branche feature est également "construit" (converti en une version déployable de l'application) pour confirmer qu'il fonctionne comme prévu.
    

Une fois ces vérifications passées, la branche feature de M. A est fusionnée dans la branche main. Cette fusion fréquente des modifications est ce que nous appelons l'**Intégration Continue**.

### Livraison Continue (CD)

La Livraison Continue (Continuous Delivery) est souvent confondue avec le Déploiement Continu, et bien qu'ils partagent des similitudes, ils servent des objectifs distincts dans le cycle de vie du développement. Décomposons cela ! 🧐

#### Le besoin d'une zone de `Staging` 🌉

Dans le processus d'Intégration Continue (CI) dont nous avons discuté plus haut, nous avons principalement traité des **branches feature** et de la **branche main**. Mais fusionner directement les modifications des branches feature vers la branche main (qui alimente le produit en direct) peut être risqué. Pourquoi ? 🛑

Bien que les tests et les builds automatisés capturent de nombreuses erreurs, ils ne sont pas infaillibles. Certains cas limites ou bugs pourraient passer inaperçus. C'est là que la **branche staging** et l'**environnement de staging** entrent en jeu ! 🎭

Considérez la branche staging comme un "essai à blanc". Avant de diffuser les modifications aux vrais clients, la base de code des branches feature est fusionnée dans la branche staging et déployée dans un **environnement de staging**. Cet environnement est une réplique exacte de l'environnement de production, mais il est utilisé exclusivement par l'équipe d'**Assurance Qualité (QA)** pour les tests.

L'équipe QA joue le rôle de "pilote d'essai", testant la plateforme exactement comme le ferait un utilisateur réel. Ils vérifient les problèmes d'utilisabilité, les cas limites ou les bugs que les tests automatisés pourraient manquer, et fournissent des retours aux développeurs pour les corrections. 🚦 Si tout passe, la base de code est autorisée pour le déploiement en production.

#### La Livraison Continue en action 📦

Le processus de fusion des modifications dans la branche staging et de leur déploiement dans l'**environnement de staging** est ce que nous appelons la **Livraison Continue**. 🛠️ Elle garantit que l'application est toujours dans un état déployable, prête pour l'étape suivante du pipeline.

Contrairement au Déploiement Continu (que nous verrons plus tard), la Livraison Continue ne pousse pas automatiquement les modifications en production (plateforme en direct). Au lieu de cela, elle marque une pause pour laisser les humains — à savoir l'équipe QA ou les parties prenantes — décider quand procéder. Cela ajoute une couche supplémentaire d'assurance qualité, réduisant les chances que des erreurs atteignent le produit final. 🕵️‍♂️

### Déploiement Continu (CD)

Le Déploiement Continu (Continuous Deployment) pousse l'automatisation à son paroxysme. Bien qu'il partage des similitudes avec la Livraison Continue, la différence clé réside dans la **dernière étape** : aucune approbation manuelle n'est requise. Le processus final — fusionner la base de code et la déployer en direct pour les utilisateurs finaux (les testeurs QA ou le chef d'équipe pourraient le faire).

Explorons ce qui rend le Déploiement Continu si puissant (et un peu effrayant) ! 😅

#### Le dernier kilomètre du pipeline CI/CD 🛣️

Imaginez que vous ayez suivi le processus rigoureux de l'Intégration Continue : les coéquipiers ont fusionné leurs branches feature, les tests automatisés ont été exécutés et la base de code a été déployée avec succès dans l'environnement de staging lors de la Livraison Continue.

Maintenant, vous êtes convaincu que l'application est exempte de bugs et prête à briller dans l'environnement de production — la version en direct de votre plateforme utilisée par de vrais clients.

Dans le **Déploiement Continu**, cette étape finale de déploiement des modifications dans l'environnement réel se produit **automatiquement**. Le pipeline se déclenche dès que des événements spécifiques surviennent, tels que :

-   Une **Pull Request (PR)** est fusionnée dans la **branche main**.
    
-   Une nouvelle **version de release** est créée.
    
-   Un **commit** est poussé directement sur la branche de production (bien que cela soit rare pour la plupart des équipes).
    

Une fois déclenché, le pipeline entre en action, construit, teste et déploie enfin la base de code mise à jour dans l'environnement de production. 📡

## **Différences entre l'intégration continue, la livraison continue et le déploiement continu** 🔍

| Aspect | Intégration Continue (CI) | Livraison Continue (CD) | Déploiement Continu (CD) |
| --- | --- | --- | --- |
| Objectif principal | Fusionner les branches feature dans la base de code main/générale OU vers la base de code de staging. | Déployer le code testé dans un environnement de staging pour les tests QA et l'approbation. | Déployer automatiquement le code dans l'environnement de production en direct. |
| **Niveau d'automatisation** | Automatise les processus de test et de build pour les branches feature. | Automatise le déploiement vers les environnements de staging/test après des tests réussis. | Automatise entièrement le déploiement en production sans approbation manuelle. |
| **Portée des tests** | Tests automatisés exécutés sur les branches feature pour garantir la qualité du code avant la fusion. | Inclut des tests automatisés avant le déploiement en staging et permet aux testeurs QA d'effectuer des tests manuels. | Peut inclure des tests automatisés comme vérification finale, garantissant la stabilité de la production. |
| **Branche impliquée** | Branches feature fusionnant dans la branche main/générale ou staging. | Branche staging utilisée comme étape intermédiaire avant la fusion dans la branche main. | Branche main/générale déployée directement en production. |
| **Environnement cible** | Garantit l'intégration et les tests dans un environnement local ou un pipeline de build. | Déploie vers des environnements de staging/test où les testeurs QA valident les fonctionnalités. | Déploie vers l'environnement de production/live accédé par les utilisateurs finaux. |
| **Objectif clé** | Prévenir les conflits d'intégration et s'assurer que les changements ne cassent pas le code existant. | Fournir un environnement stable proche de la production pour des tests QA approfondis. | Garantir que les nouvelles fonctionnalités atteignent les utilisateurs le plus rapidement possible. |
| **Processus d'approbation** | Aucune approbation nécessaire. Les branches sont testées et fusionnées selon les critères. | L'équipe QA ou le lead donne son feedback/approbation avant la fusion vers main pour la production. | Aucune approbation manuelle. Le déploiement est entièrement automatisé. |
| **Exemple de déclencheur** | Un développeur fusionne une branche feature dans la branche main. | La branche staging passe les tests automatisés (pendant la PR) et est prête pour le déploiement. | Une nouvelle release est créée ou une pull request est fusionnée dans main, déclenchant le déploiement. |

Maintenant que nous avons démêlé les mystères de l'Intégration Continue, de la Livraison Continue et du Déploiement Continu, il est temps de retrousser nos manches et de passer de la théorie à la pratique 😁.

## **Comment configurer un projet Node.js avec un serveur web et des tests automatisés** ✨

Dans cette section pratique, nous allons construire un serveur web Node.js avec des tests automatisés utilisant Jest. À partir de là, nous créerons un pipeline CI/CD avec GitHub Actions qui automatise les tests pour chaque **pull request vers les branches staging et main**. Enfin, nous publierons une image de notre application sur DockerHub et déploierons l'image sur **Google Cloud Run**, d'abord dans un environnement de staging pour les tests, puis plus tard dans l'environnement de production pour l'utilisation réelle.

Prêt à donner vie à votre projet ? C'est parti ! 🚀✨

### Étape 1 : Installer Node.js 📥

Pour commencer, vous devrez avoir **Node.js** installé sur votre machine. Node.js fournit l'environnement d'exécution JavaScript que nous utiliserons pour créer notre serveur web.

1.  Visitez [https://nodejs.org/en/download/package-manager][12]
    
2.  Choisissez votre système d'exploitation (Windows, macOS ou Linux) et téléchargez l'installateur.
    
3.  Suivez les instructions d'installation pour terminer la configuration.
    

Pour vérifier que Node.js a été installé avec succès, ouvrez votre terminal et exécutez `node -v`. Cela devrait afficher la version installée de Node.js.

### Étape 2 : Cloner le dépôt de démarrage 📂

L'étape suivante consiste à récupérer le code de démarrage sur GitHub. Si vous n'avez pas Git installé, vous pouvez le télécharger sur [https://git-scm.com/downloads][13]. Choisissez votre OS et suivez les instructions. Une fois prêt, il est temps de cloner le dépôt.

Exécutez la commande suivante dans votre terminal pour cloner le code de base :

```
git clone --single-branch --branch initial https://github.com/onukwilip/ci-cd-tutorial
```

Cela téléchargera les fichiers du projet depuis la branche `initial`, qui contient le template de départ pour notre serveur web Node.js.

Naviguez dans le répertoire du projet :

```
cd ci-cd-tutorial
```

### Étape 3 : Installer les dépendances 📦

Une fois dans le répertoire du projet, installez les dépendances requises pour le projet Node.js. Ce sont les packages qui alimentent l'application :

```
npm install --force
```

Cela téléchargera et configurera toutes les bibliothèques spécifiées dans le projet. Très bien, les dépendances sont installées ? Vous avez fait un pas de plus !

### Étape 4 : Exécuter les tests automatisés ✅

Avant de plonger dans le code, confirmons que les tests automatisés fonctionnent correctement. Exécutez :

```
npm test
```

Vous devriez voir deux résultats de test réussis dans votre terminal. Cela indique que le projet de démarrage est correctement configuré avec des tests automatisés fonctionnels.

![Exécution de test réussie](https://cdn.hashnode.com/res/hashnode/image/upload/v1733074280408/93b4ea86-1dfa-42eb-a163-b97c19c2a053.png)

### Étape 5 : Démarrer le serveur web 🌐

Enfin, démarrons le serveur web et voyons-le en action. Exécutez la commande suivante :

```
npm start
```

Attendez que l'application commence à s'exécuter. Ouvrez votre navigateur et visitez [http://localhost:5000][14]. 🎉 Vous devriez voir le serveur web de démarrage opérationnel, prêt pour votre magie CI/CD :

![Exécution réussie du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1733074667521/7b80bb21-1f43-430e-8a56-2bff8b81ddad.png)

## **How to Create a GitHub Repository to Host Your Codebase 📂**

### Étape 1 : Se connecter à GitHub

1.  **Allez sur GitHub** : Ouvrez votre navigateur et visitez GitHub - [https://github.com][15].
    
2.  **Se connecter** : Cliquez sur le bouton **Sign In** dans le coin supérieur droit et entrez vos identifiants, OU créez un compte si vous n'en avez pas en cliquant sur le bouton **Sign up**.
    

### Étape 2 : Créer un nouveau dépôt

Une fois connecté, sur la page principale de GitHub, vous verrez un signe "+" dans le coin supérieur droit à côté de votre photo de profil. Cliquez dessus et sélectionnez **“New repository”** dans le menu déroulant.

![Nouveau dépôt GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1733130465203/dac28dee-74da-4fd4-8a96-bc90aef01207.png)

Il est maintenant temps de définir les détails du dépôt. Vous inclurez :

-   **Repository Name** : Choisissez un nom pour votre dépôt. Par exemple, vous pouvez l'appeler `ci-cd-tutorial`.
    
-   **Description** (Optionnel) : Vous pouvez ajouter une courte description, comme “Un projet tutoriel pour CI/CD avec Docker et GitHub Actions.”
    
-   **Visibility** : Choisissez si vous voulez que votre dépôt soit **public** (accessible par tous) ou **private** (accessible uniquement par vous et ceux que vous invitez). Pour ce tutoriel, rendez-le **public**.
    
-   **Ne cochez pas la case Add a README File** : **Important** : Assurez-vous de **ne pas cocher** l'option **Add a README file**. Cela créerait automatiquement un fichier `README.md` dans votre dépôt, ce qui pourrait causer des conflits plus tard lors du push de vos fichiers locaux. Nous ajouterons le fichier README manuellement si nécessaire plus tard.
    

Après avoir rempli les détails, cliquez sur **“Create repository”**.

![Créer un dépôt GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1733130890582/04e09ac8-0ee6-4d26-a9f2-007c0e6ca08f.png)

### Étape 3 : Changer la destination distante et pousser vers votre nouveau dépôt

#### **Mettre à jour l'URL du dépôt distant** :

Comme vous avez déjà cloné la base de code depuis mon dépôt, vous devez mettre à jour la destination distante pour pointer vers votre dépôt GitHub nouvellement créé.

Copiez l'URL de votre dépôt (l'URL de la page vers laquelle vous avez été redirigé après la création du dépôt). Elle devrait ressembler à ceci : `https://github.com/<username>/<repo-name>`.

Ouvrez votre terminal dans le répertoire du projet et exécutez les commandes suivantes :

```
git remote set-url origin <your-repo-url>
```

Remplacez `<your-repo-url>` par l'URL de votre dépôt GitHub que vous avez copiée précédemment.

#### **Renommer la branche actuelle en** `main` :

Si votre branche porte un nom autre que `main`, vous pouvez la renommer en `main` en utilisant :

```
git branch -M main
```

#### **Pousser vers votre nouveau dépôt** :

Enfin, committez toutes les modifications que vous avez apportées et poussez votre dépôt local vers le nouveau dépôt distant GitHub en exécutant :

```
git add .
git commit -m 'Created boilerplate'
git push -u origin main
```

Maintenant, votre base de code locale est liée à votre nouveau dépôt GitHub, et les fichiers y sont poussés avec succès. Vous pouvez vérifier en visitant votre dépôt sur GitHub.

## Comment configurer les workflows CI et CD dans votre projet ⚙️

Il est maintenant temps de créer les **workflows CI et CD** pour notre projet ! Ces workflows ne s'exécuteront pas sur votre PC local mais seront automatiquement déclenchés et exécutés dans le cloud une fois que vous aurez poussé vos modifications vers le dépôt distant. GitHub Actions détectera ces workflows et les exécutera en fonction des déclencheurs que vous définirez.

### Étape 1 : Préparer le répertoire des workflows 📂

Avant d'ajouter les pipelines CI/CD, il est recommandé de créer d'abord une branche feature. Cette étape reflète le workflow couramment utilisé en équipe, où les nouvelles fonctionnalités ou modifications sont effectuées dans des branches séparées avant d'être fusionnées dans la base de code principale.

Pour créer et basculer vers une nouvelle branche, exécutez la commande suivante :

```
git checkout -b feature/ci-cd-pipeline
```

Cela créera une nouvelle branche appelée `feature/ci-cd-pipeline` et y basculera. Maintenant, vous pouvez ajouter et tester les workflows CI/CD en toute sécurité sans affecter la branche main.

Une fois terminé, vous pourrez fusionner cette branche feature dans `main` ou `staging` dans le cadre du processus de pull request.

Dans le répertoire racine du projet, créez un dossier nommé `.github`. À l'intérieur de `.github`, créez un autre dossier appelé `workflows`.

Tout fichier YAML placé dans le répertoire `.github/workflows` est automatiquement reconnu comme un workflow GitHub Actions. Ces workflows s'exécuteront en fonction de déclencheurs spécifiques, tels que des pull requests, des pushes ou des releases.

### Étape 2 : Créer le workflow d'Intégration Continue 🚀

Nous allons maintenant créer un workflow CI qui teste automatiquement l'application chaque fois qu'une pull request est effectuée vers les branches `main` ou `staging`.

Tout d'abord, à l'intérieur du répertoire `workflows`, créez un fichier nommé `ci-pipeline.yml`.

Collez le code suivant dans le fichier :

```
name: CI Pipeline to staging/production environment
on:
  pull_request:
    branches:
      - staging
      - main
jobs:
  test:
    runs-on: ubuntu-latest
    name: Setup, test, and build project
    env:
      PORT: 5001
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Install dependencies
        run: npm ci

      - name: Test application
        run: npm test

      - name: Build application
        run: |
          echo "Run command to build the application if present"
          npm run build --if-present
```

#### Explication du workflow CI

Voici une décomposition de chaque section du workflow :

1.  `name: CI Pipeline to staging/production environment` : C'est le titre de votre workflow. Il vous aide à identifier ce pipeline dans GitHub Actions.
    
2.  `on` : Le paramètre `on` détermine les événements qui déclenchent votre workflow. Lorsque le fichier YAML du workflow est poussé vers le dépôt GitHub distant, GitHub Actions enregistre automatiquement le workflow en utilisant les déclencheurs configurés dans le champ `on`. Ces déclencheurs agissent comme des écouteurs d'événements qui indiquent à GitHub quand exécuter le workflow.
    
    **Par exemple :**
    
    Si nous définissons `pull_request` comme valeur pour le paramètre `on` et spécifions les branches que nous voulons surveiller à l'aide de la clé `branches`, GitHub configure des écouteurs d'événements pour les pull requests vers ces branches.
    
    ```
     on:
       pull_request:
         branches:
           - main
           - staging
    ```
    
    Cette configuration signifie que GitHub déclenchera le workflow chaque fois qu'une pull request est effectuée vers les branches `main` ou `staging`.
    
    **Déclencheurs multiples** :  
    Vous pouvez définir plusieurs écouteurs d'événements dans le paramètre `on`. Par exemple, en plus des pull requests, vous pouvez ajouter un écouteur pour les événements push.
    
    ```
     on:
       pull_request:
         branches:
           - main
           - staging
       push:
         branches:
           - main
    ```
    
    Cette configuration garantit que le workflow est déclenché quand :
    
    -   Une pull request est effectuée vers la branche `main` ou `staging`.
        
    -   Un push est effectué directement sur la branche `main`.
        

📘 **En savoir plus sur les déclencheurs :** Consultez la [documentation officielle de GitHub ici][16].

3.  `jobs` : La section `jobs` décrit les tâches spécifiques (ou jobs) que le workflow exécutera. Chaque job est une unité de travail indépendante qui s'exécute sur une machine virtuelle (VM) distincte. Cette isolation garantit un environnement propre et unique pour chaque job, évitant les conflits potentiels entre les tâches.
    
    **Points clés sur les Jobs :**
    
    1.  **VM propre pour chaque Job** : Lorsque GitHub Actions exécute un workflow, il assigne une instance de VM dédiée à chaque job. Cela signifie que l'environnement est réinitialisé pour chaque job.
        
    2.  **Jobs multiples** : Les workflows peuvent avoir plusieurs jobs, chacun responsable d'une tâche spécifique. Par exemple :
        
        -   Un job **Test** pour installer les dépendances et exécuter les tests automatisés.
            
        -   Un job **Build** pour compiler l'application.
            
    3.  **Organisation des Jobs** : Les jobs peuvent être organisés pour s'exécuter :
        
        -   **Séquentiellement** : Garantit qu'un job est terminé avant que le suivant ne commence. Ce flux séquentiel imite la structure de "pipeline".
            
        -   **Simultanément** : Plusieurs jobs peuvent s'exécuter en parallèle pour gagner du temps.
            
    4.  **Job unique dans ce workflow** : Dans notre workflow actuel, il n'y a qu'un seul job, `test`, qui :
        
        -   Installe les dépendances.
            
        -   Exécute les tests automatisés.
            
        -   Construit l'application.
            

📘 **En savoir plus sur les jobs :** Plongez dans la [documentation des jobs GitHub Actions ici][17].

4.  `runs-on: ubuntu-latest` : Spécifie le système d'exploitation sur lequel le job s'exécutera. GitHub fournit des environnements virtuels préconfigurés, et nous utilisons la dernière image Ubuntu.
    
5.  `env` : Définit les variables d'environnement pour le job. Ici, nous définissons la variable **PORT** utilisée par notre application.
    
6.  **Steps** : Les étapes définissent les actions individuelles à exécuter au sein d'un job :
    
    -   `Checkout` : Utilise l'action `actions/checkout` pour cloner le dépôt contenant la base de code de la branche feature dans l'environnement de l'instance de machine virtuelle. Cette étape garantit que le pipeline a accès aux fichiers du projet.
        
    -   `Install dependencies` : Exécute `npm ci` pour installer les packages Node.js requis.
        
    -   `Test application` : Exécute les tests automatisés à l'aide de la commande `npm test`. Cela valide la base de code pour les erreurs ou les cas de test échoués.
        
    -   `Build application` : Construit l'application si un script de build est défini dans le `package.json`. Le drapeau `--if-present` garantit que cette étape n'échoue pas si aucun script de build n'est présent.
        

Maintenant que nous avons terminé le pipeline CI, qui s'exécute sur les pull requests vers les branches `main` ou `staging`, passons à la configuration des pipelines de **Livraison Continue (CD)** et de **Déploiement Continu**. 🚀

### Étape 3 : Le workflow de Livraison et de Déploiement Continus

**Tout d'abord, créez le fichier du pipeline** :  
Dans le dossier `.github/workflows`, créez un nouveau fichier appelé `cd-pipeline.yml`. Ce fichier définira les workflows pour automatiser la livraison et le déploiement.

**Ensuite, collez la configuration** :  
Copiez et collez la configuration suivante dans le fichier `cd-pipeline.yml` :

```
name: CD Pipeline to Google Cloud Run (staging and production)
on:
  push:
    branches:
      - staging
  workflow_dispatch: {}
  release:
    types: published

env:
  PORT: 5001
  IMAGE: ${{vars.IMAGE}}:${{github.sha}}
jobs:
  test:
    runs-on: ubuntu-latest
    name: Setup, test, and build project
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Install dependencies
        run: npm ci

      - name: Test application
        run: npm test
  build:
    needs: test
    runs-on: ubuntu-latest
    name: Setup project, Authorize GitHub Actions to GCP and Docker Hub, and deploy
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Authenticate for GCP
        id: gcp-auth
        uses: google-github-actions/auth@v0
        with:
          credentials_json: ${{ secrets.GCP_SERVICE_ACCOUNT }}

      - name: Set up Cloud SDK
        uses: google-github-actions/setup-gcloud@v0

      - name: Authenticate for Docker Hub
        id: docker-auth
        env:
          D_USER: ${{secrets.DOCKER_USER}}
          D_PASS: ${{secrets.DOCKER_PASSWORD}}
        run: |
          docker login -u $D_USER -p $D_PASS
      - name: Build and tag Image
        run: |
          docker build -t ${{env.IMAGE}} .
      - name: Push the image to Docker hub
        run: |
          docker push ${{env.IMAGE}}
      - name: Enable the Billing API
        run: |
          gcloud services enable cloudbilling.googleapis.com --project=${{secrets.GCP_PROJECT_ID}}
      - name: Deploy to GCP Run - Production environment (If a new release was published from the master branch)
        if: github.event_name == 'release' && github.event.action == 'published' && github.event.release.target_commitish == 'main'
        run: |
          gcloud run deploy ${{vars.GCR_PROJECT_NAME}} \
          --region ${{vars.GCR_REGION}} \
          --image ${{env.IMAGE}} \
          --platform "managed" \
          --allow-unauthenticated \
          --tag production \
      - name: Deploy to GCP Run - Staging environment
        if: github.ref != 'refs/heads/main'
        run: |
          echo "Deploying to staging environment"
          # Deploy service with to staging environment
          gcloud run deploy ${{vars.GCR_STAGING_PROJECT_NAME}} \
          --region ${{vars.GCR_REGION}} \
          --image ${{env.IMAGE}} \
          --platform "managed" \
          --allow-unauthenticated \
          --tag staging \
```

La configuration du **pipeline CD** combine les workflows de Livraison Continue et de Déploiement Continu dans un seul fichier par souci de simplicité. Elle s'appuie sur les concepts de CI/CD dont nous avons discuté précédemment, automatisant les tests, la construction et le déploiement de l'application sur Google Cloud Run.

#### Explication du pipeline CD :

1.  #### Déclencheurs du workflow (`on`)
    

-   `push` : Le workflow se déclenche lors des pushes vers la branche `staging`.
    
-   `workflow_dispatch` : Permet l'exécution manuelle du workflow via l'interface GitHub Actions.
    
-   `release` : Se déclenche lorsqu'une nouvelle release est publiée.  
    Exemple : Lorsqu'une release est publiée depuis la branche `main`, l'application se déploie dans l'environnement de production.
    

2.  **Job 1 – Tester la base de code :** Le premier job du pipeline, Test, garantit que la base de code est fonctionnelle et sans erreur avant de procéder à la livraison ou au déploiement.
    
3.  **Job 2 – Construire et déployer l'application :** Moment Eurêka ✨ : Ces jobs s'exécutent séquentiellement. 😃 Le job **Build** ne commence qu'après que le job **Test** s'est terminé avec succès. Il prépare l'application pour le déploiement et gère le processus de déploiement effectif.
    
    Voici ce qui se passe :
    
    -   **Autorisation pour GCP et Docker Hub** : Le workflow s'authentifie auprès de Google Cloud Platform (GCP) et de Docker Hub. Pour GCP, il utilise l'action `google-github-actions/auth@v0` pour gérer les identifiants du compte de service stockés en tant que secrets. De même, il se connecte à Docker Hub avec les identifiants stockés pour permettre le téléchargement d'images.
        
    -   **Construire et pousser l'image Docker** : L'application est construite dans une image Docker et taguée avec un identifiant unique (`${{env.IMAGE}}`). Cette image est ensuite poussée vers Docker Hub, la rendant accessible pour le déploiement.
        
    -   **Déployer sur Google Cloud Run** : En fonction de l'événement qui a déclenché le workflow, l'application est **déployée soit dans l'environnement de staging, soit dans l'environnement de production** sur Google Cloud Run. Un **push** vers la branche `staging` déploie vers l'environnement de staging (Livraison Continue), tandis qu'une **release** depuis la branche `main` déploie vers la production (Déploiement Continu).
        

Pour garantir la sécurité et la flexibilité de notre pipeline, nous nous appuyons sur des variables et des secrets externes plutôt que de coder en dur des informations sensibles directement dans le fichier du workflow.

Pourquoi ? Les fichiers de configuration de workflow font partie de votre dépôt et sont accessibles à toute personne ayant accès à la base de code. Si des données sensibles, comme des clés API ou des mots de passe, sont exposées ici, elles peuvent être facilement compromises. 😨

Au lieu de cela, nous utilisons les **Secrets** de GitHub pour stocker et accéder à ces informations en toute sécurité. Les secrets nous permettent de définir des variables chiffrées et accessibles uniquement par nos workflows. Par exemple :

-   **Identifiants DockerHub** : Nous ajouterons un nom d'utilisateur Docker et un jeton d'accès aux secrets du dépôt. Ceux-ci sont essentiels pour s'authentifier auprès de DockerHub afin de télécharger les images Docker construites.
    
-   **Clé du compte de service Google Cloud** : Cette clé accordera au pipeline les permissions nécessaires pour déployer l'application sur **Google Cloud Run** en toute sécurité.
    

Nous configurerons ces variables et secrets progressivement au fur et à mesure, en nous assurant que chaque étape est totalement sécurisée et fonctionnelle. 🎯

## **Configurer un dépôt Docker Hub pour l'image du projet et générer un jeton d'accès pour publier l'image** 📦

Avant de plonger dans les étapes, passons rapidement en revue ce que nous allons faire. Dans cette section, vous apprendrez à créer un dépôt Docker Hub, qui agit comme un espace de stockage en ligne pour l'image conteneur de votre application.

Considérez une image conteneur comme un instantané de votre application, prêt à être déployé n'importe où. Pour garantir un accès fluide et sécurisé, nous générerons également un jeton d'accès spécial, sorte de mot de passe révocable que notre pipeline CI/CD pourra utiliser pour télécharger l'image de votre application sur Docker Hub. C'est parti ! 🚀

### Étape 1 : S'inscrire sur Docker Hub

Voici les étapes à suivre pour s'inscrire sur Docker Hub :

1.  **Allez sur le site de Docker Hub** : Ouvrez votre navigateur web et visitez Docker Hub - [https://hub.docker.com/][18].
    
2.  **Créer un compte** : Sur la page d'accueil de Docker Hub, vous verrez un bouton intitulé **"Sign Up"** dans le coin supérieur droit. Cliquez dessus.
    
3.  **Remplissez vos coordonnées** : Il vous sera demandé de fournir quelques détails comme votre nom d'utilisateur, votre adresse e-mail et votre mot de passe. Choisissez un mot de passe fort dont vous pourrez vous souvenir.
    
4.  **Accepter les conditions** : Vous devrez cocher une case pour accepter les conditions de service de Docker. Après cela, cliquez sur **“Sign Up”** pour créer votre compte.
    
5.  **Vérifier votre e-mail** : Docker Hub vous enverra un e-mail pour vérifier votre compte. Ouvrez cet e-mail et cliquez sur le lien de vérification pour terminer la création de votre compte.
    

### Étape 2 : Se connecter à Docker Hub

Après avoir vérifié votre e-mail, retournez sur Docker Hub et cliquez sur **"Sign In"** en haut à droite. Vous pourrez ensuite utiliser les identifiants que vous venez de créer pour vous connecter.

### Étape 3 : Générer un jeton d'accès (pour le pipeline CI/CD)

Maintenant que vous avez un compte, vous pouvez créer un jeton d'accès (access token). Ce jeton permettra à votre workflow GitHub Actions de se connecter en toute sécurité à Docker Hub et de télécharger des images Docker.

Une fois connecté à Docker Hub, cliquez sur votre photo de profil (ou avatar) dans le coin supérieur droit. Cela ouvrira un menu. Dans le menu, cliquez sur “Account Settings”.

Ensuite, dans le menu de gauche de vos paramètres de compte, faites défiler jusqu'à l'onglet **"Security"**. Cette section est l'endroit où vous gérez vos jetons et mots de passe.

Vous devrez maintenant créer un nouveau jeton d'accès. Dans l'onglet Security, vous verrez un lien intitulé **“Personal access tokens”** – cliquez dessus. Cliquez sur le bouton intitulé **“Generate new token”**.

Il vous sera demandé de donner une description à votre jeton. Vous pouvez le nommer par exemple "GitHub Actions CI/CD" afin de savoir à quoi il sert.

Après avoir donné une description, cliquez sur le menu déroulant “**Access permissions**“ et sélectionnez **“Read & Write“,** ou **“Read, Write, Delete“**. Cliquez sur “**Generate**“.

![Créer un jeton d'accès Docker](https://cdn.hashnode.com/res/hashnode/image/upload/v1733129374816/c725f041-c0ef-49a0-b8ef-ca62acafc1ee.png)

Maintenant, vous devez copier les identifiants. Après avoir cliqué sur le bouton de génération, Docker Hub créera un jeton d'accès. **Copiez immédiatement ce jeton ainsi que votre nom d'utilisateur** et enregistrez-les dans un endroit sûr (ne vous inquiétez pas, nous les ajouterons à nos secrets GitHub). Vous ne pourrez plus revoir ce jeton, alors assurez-vous de le sauvegarder !

![Copier le nom d'utilisateur Docker + le jeton d'accès](https://cdn.hashnode.com/res/hashnode/image/upload/v1733133363382/33dbf334-a7ec-4151-8639-5368c3ccaedb.png)

### Étape 4 : Ajouter le jeton à GitHub en tant que Secret

Pour ce faire, ouvrez votre dépôt GitHub où la base de code est hébergée. Dans le dépôt GitHub, cliquez sur l'onglet **Settings** (situé près du haut de la page de votre dépôt).

Ensuite, dans la barre latérale gauche, faites défiler vers le bas et cliquez sur **“Secrets and Variables”**, puis choisissez **“Actions”**.

1.  ![Ouvrir les Secrets GitHub Actions](https://cdn.hashnode.com/res/hashnode/image/upload/v1733133003023/75c3bd35-1a5b-46fa-845a-0f4fd8305d53.png)

Voici les étapes pour créer et gérer votre nouveau secret :

1.  **Ajouter un nouveau secret** : Cliquez sur le bouton **“New repository secret”**.
    
2.  **Configurer le secret** :
    
    -   Dans le champ **Name**, tapez `DOCKER_PASSWORD`.
        
    -   Dans le champ **Value**, collez le jeton d'accès que vous avez copié précédemment.
        
3.  **Enregistrer le secret** : Enfin, cliquez sur **Add secret** pour enregistrer votre jeton d'accès Docker en toute sécurité dans GitHub.
    

Répétez ensuite le processus pour votre nom d'utilisateur Docker. Créez un nouveau secret appelé `DOCKER_USER` et ajoutez votre nom d'utilisateur Docker que vous avez copié précédemment.

Et voilà ! Maintenant, votre pipeline CI/CD peut utiliser ce jeton pour se connecter en toute sécurité à Docker Hub et télécharger des images automatiquement lorsqu'il est déclenché. 🎉

### **Étape 5 : Création du Dockerfile pour le projet**

Avant de pouvoir construire et publier l'image Docker sur Docker Hub, vous devez créer un `Dockerfile` contenant les instructions nécessaires pour construire votre application.

Suivez les étapes ci-dessous pour créer le `Dockerfile` dans le dossier racine de votre projet :

1.  Naviguez vers le dossier racine de votre projet.
    
2.  Créez un nouveau fichier nommé `Dockerfile`.
    
3.  Ouvrez le **Dockerfile** dans un éditeur de texte et collez-y le contenu suivant :
    

```
FROM node:18-slim

WORKDIR /app

COPY package.json .

RUN npm install -f

COPY . .

# EXPOSE 5001
EXPOSE 5001

CMD ["npm", "start"]
```

#### Explication du Dockerfile :

-   `FROM node:18-slim` : Définit l'image de base pour le conteneur Docker, qui est une version allégée de l'image officielle Node.js basée sur la version 18.
    
-   `WORKDIR /app` : Définit le répertoire de travail pour l'application à l'intérieur du conteneur sur `/app`.
    
-   `COPY package.json .` : Copie le fichier `package.json` dans le répertoire de travail.
    
-   `RUN npm install -f` : Installe les dépendances du projet à l'aide de `npm`.
    
-   `COPY . .` : Copie le reste des fichiers du projet dans le conteneur.
    
-   `EXPOSE 5001` : Indique à Docker d'exposer le port `5001`, qui est le port sur lequel notre application s'exécutera à l'intérieur du conteneur.
    
-   `CMD ["npm", "start"]` : Définit la commande par défaut pour démarrer l'application lorsque le conteneur est lancé, en utilisant `npm start`.
    

## **Créer un compte Google Cloud, un projet et un compte de facturation** ☁️

Dans cette section, nous posons les bases du déploiement de notre application sur Google Cloud. Tout d'abord, nous allons configurer un compte Google Cloud (ne vous inquiétez pas, c'est gratuit pour commencer !). Ensuite, nous créerons un nouveau projet où résideront toutes les ressources de votre application.

Enfin, nous activerons la facturation afin que vous puissiez débloquer les services cloud nécessaires au déploiement. Considérez cela comme la configuration de votre espace de travail dans le cloud — organisé, prêt et sécurisé ! Plongeons-y ! ☁️

### Étape 1 : Créer ou se connecter à un compte Google Cloud 🌐

Tout d'abord, allez sur la [Console Google Cloud][19]. Si vous n'avez pas de compte Google Cloud, vous devrez en créer un.

Pour ce faire, cliquez sur **Get Started for Free** et suivez les étapes pour configurer votre compte (vous devrez fournir des informations de paiement, mais Google offre 300 $ de crédits gratuits pour commencer). Si vous avez déjà un compte Google, connectez-vous simplement.

Une fois connecté, vous serez dirigé vers votre tableau de bord Google Cloud. C'est ici que vous pouvez gérer tous vos projets et ressources cloud.

### Étape 2 : Créer un nouveau projet Google Cloud 🏗️

En haut à gauche de la Console Google Cloud, vous verrez un menu déroulant à côté du logo Google Cloud. Cliquez sur ce menu pour afficher vos projets actuels.

Il est maintenant temps de créer un nouveau projet. Dans le coin supérieur gauche de la fenêtre contextuelle, cliquez sur le bouton **New Project**.

![Créer un projet Google Cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1733134260252/6769909a-cf9c-4c91-9d79-7676500f3981.webp)

Vous serez redirigé vers une page où vous devrez fournir quelques détails de base pour votre nouveau projet. Entrez les informations suivantes :

-   **Project Name :** Entrez le nom de votre choix pour le projet (par exemple, `gcr-ci-cd-project`).
    
-   **Location :** Sélectionnez un emplacement pour votre projet. Vous pouvez laisser la valeur par défaut "No organization" si vous débutez.
    

Une fois que vous avez entré le nom du projet, cliquez sur le bouton **Create**. Google Cloud va maintenant commencer à créer votre nouveau projet. Cela peut prendre quelques secondes.

### Étape 3 : Accéder à votre nouveau projet 🛠️

Après quelques secondes, vous serez redirigé vers votre **tableau de bord Google Cloud**.

Cliquez à nouveau sur le menu déroulant à côté du logo Google Cloud, et vous devriez maintenant voir votre projet nouvellement créé répertorié dans la fenêtre modale où vous pouvez le sélectionner.

Cliquez ensuite sur le nom du projet (par exemple, `gcr-ci-cd-project`) pour accéder au tableau de bord de votre projet.

### Étape 4 : Lier un compte de facturation à votre projet 💳

Pour accéder à la page de facturation, dans la Console Google Cloud, trouvez le **Menu de Navigation** (les trois lignes horizontales) en haut à gauche de l'écran. Cliquez dessus pour ouvrir une liste d'options. Faites défiler vers le bas et cliquez sur **Billing**. Cela vous mènera à la section de facturation de votre compte Google Cloud.

![Naviguer vers le tableau de bord de facturation Google Cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1733134747962/745c8a0e-13c5-4dde-849b-303c1200f495.png)

Si vous n'avez pas encore configuré de compte de facturation, vous serez invité à le faire. Cliquez sur le bouton **"Link a billing account"** pour lancer le processus.

Vous pouvez maintenant créer un nouveau compte de facturation (si vous n'en avez pas). Vous serez redirigé vers une page où vous pourrez soit sélectionner un compte de facturation existant, soit en créer un nouveau. Si vous n'avez pas encore de compte de facturation, cliquez sur **"Create a billing account"**.

Fournissez les détails nécessaires, notamment :

-   **Account name** (par exemple, "Compte de facturation personnel" ou le nom de votre entreprise).
    
-   **Country** : Choisissez le pays où votre entreprise ou votre compte est basé.
    
-   **Currency** : Choisissez la devise dans laquelle vous souhaitez être facturé.
    
    ![Créer un compte de facturation Google Cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1733135153425/1287ab53-e9c5-45b5-a09d-3d3a13840ca4.png)
    

Ensuite, entrez vos informations de paiement (carte de crédit ou coordonnées bancaires). Google Cloud vérifiera votre mode de paiement, assurez-vous donc que les informations sont correctes.

Lisez et acceptez les Conditions d'utilisation de Google Cloud et les Conditions du compte de facturation. Une fois cela fait, cliquez sur **"Start billing"** pour terminer la configuration de votre compte de facturation.

Après avoir configuré votre compte de facturation, vous serez dirigé vers une page vous demandant de le **lier** à votre projet. Sélectionnez le compte de facturation que vous venez de créer ou un compte existant que vous souhaitez utiliser. Cliquez sur Set Account pour lier le compte de facturation à votre projet.

![Lier le compte de facturation Google Cloud au projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1733337276189/b80702dd-2ff6-42db-a325-c2082e8059e5.png)

Une fois que vous avez lié votre compte de facturation à votre projet, vous devriez voir un message de confirmation indiquant que la facturation a été activée avec succès pour votre projet.

Vous pouvez toujours vérifier cela en retournant à la section Billing de la Console Google Cloud, où vous verrez votre compte de facturation répertorié.

## **Créer un compte de service Google Cloud pour permettre le déploiement de l'application Node.js sur Google Cloud Run via le pipeline CD** 🚀

### Pourquoi avons-nous besoin d'un compte de service et d'une clé ? 🤔

Un **compte de service** permet à notre pipeline CI/CD de s'authentifier et d'interagir avec les services Google Cloud par programmation. En attribuant des rôles spécifiques (permissions), nous garantissons que le compte de service ne peut effectuer que des tâches liées au déploiement, comme la gestion de Google Cloud Run.

La **clé du compte de service** est un fichier JSON contenant les identifiants utilisés pour l'authentification. Nous stockons cette clé en toute sécurité en tant que secret GitHub pour protéger les informations sensibles.

### Étape 1 : Ouvrir la page des comptes de service

Voici les étapes à suivre pour configurer votre compte de service et obtenir votre clé :

Tout d'abord, visitez la Console Google Cloud sur [https://console.cloud.google.com/][20]. Assurez-vous d'avoir sélectionné le bon projet (par exemple, `gcr-ci-cd-project`). Pour changer de projet, cliquez sur le menu déroulant à côté du logo Google Cloud dans le coin supérieur gauche et sélectionnez votre projet.

Ensuite, accédez au Menu de Navigation (trois lignes horizontales dans le coin supérieur gauche) et cliquez sur **IAM & Admin > Service Accounts**.

![Naviguer vers Google Cloud IAM - Service Account](https://cdn.hashnode.com/res/hashnode/image/upload/v1733147553088/e3647442-ca8e-4197-ab5f-91cee5a6d6b0.png)

### Étape 2 : Créer un nouveau compte de service

Cliquez sur le bouton "Create Service Account". Cela ouvrira un formulaire où vous définirez les détails de votre compte de service.

Ensuite, entrez les détails du compte de service :

-   **Name** : Entrez un nom descriptif (par exemple, `ci-cd-sa`).
    
-   **ID** : Il se remplira automatiquement en fonction du nom.
    
-   **Description** : Ajoutez une description pour aider à identifier son but, comme “Utilisé pour déployer l'application Node.js sur Cloud Run.”
    
-   Cliquez sur **Create and Continue** pour procéder.
    

### Étape 3 : Attribuer les rôles nécessaires (Permissions)

Sur l'écran suivant, vous attribuerez des rôles au compte de service. Ajoutez les rôles suivants un par un :

-   **Cloud Run Admin** : Permet la gestion des services Cloud Run.
    
-   **Service Account User** : Accorde la capacité d'utiliser des comptes de service.
    
-   **Service Usage Admin** : Permet de contrôler l'activation des API.
    
-   **Viewer** : Fournit un accès en lecture seule pour visualiser les ressources.
    

Pour ajouter un rôle :

-   Cliquez sur **"Select a Role"**.
    
-   Utilisez la barre de recherche pour taper le nom du rôle (par exemple, "Cloud Run Admin") et sélectionnez-le.
    
-   Répétez l'opération pour les quatre rôles.
    

![Créer un compte de service Google Cloud - Ajouter un rôle](https://cdn.hashnode.com/res/hashnode/image/upload/v1733147870701/393833c9-c320-49e3-8743-dbc0d739b99b.png)

Votre écran devrait ressembler à ceci :

![Créer un compte de service Google Cloud (SA) - Rôles attribués](https://cdn.hashnode.com/res/hashnode/image/upload/v1733147949148/c509c810-767d-4900-aa44-a737cc1c8dc1.png)

Après avoir attribué les rôles, cliquez sur **Continue**.

### Étape 4 : Ignorer l'octroi d'accès aux utilisateurs au compte de service

Sur l'écran suivant, vous verrez une option pour accorder l'accès à d'autres utilisateurs à ce compte de service. Cliquez sur **Done** pour terminer le processus de création.

### Étape 5 : Générer une clé de compte de service 🔑

Vous devriez maintenant voir votre compte de service nouvellement créé dans la liste. Trouvez la ligne correspondant à votre compte de service (par exemple, `ci-cd-sa`) et cliquez sur les trois points verticaux sous la colonne “Actions”. Sélectionnez **"Manage Keys"** dans le menu déroulant.

Pour ajouter une nouvelle clé :

-   Cliquez sur **"Add Key" > "Create New Key"**.
    
-   Dans la boîte de dialogue contextuelle, sélectionnez **JSON** comme type de clé.
    
-   Cliquez sur **Create**.
    
    ![Créer une clé de compte de service Google Cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1733148120618/c7014982-ae7d-40ed-bbfb-0c8f5c4b8090.png)
    

Maintenant, téléchargez le fichier de clé. Un fichier JSON sera automatiquement téléchargé sur votre ordinateur. Ce fichier contient les identifiants nécessaires pour s'authentifier auprès de Google Cloud.

Assurez-vous de garder la clé en sécurité et de la stocker dans un endroit sûr. Ne la partagez pas — traitez-la comme une information sensible.

### Étape 6 : Ajouter la clé du compte de service aux secrets GitHub 🔒

Commencez par ouvrir le fichier JSON téléchargé à l'aide d'un éditeur de texte (comme Notepad ou VS Code). Sélectionnez ensuite et copiez tout le contenu du fichier.

Naviguez ensuite vers le dépôt que vous avez créé pour ce projet sur GitHub. Cliquez sur l'onglet **Settings** en haut du dépôt. Faites défiler vers le bas et trouvez la section **Secrets and variables > Actions**.

Vous devez maintenant ajouter un nouveau secret. Cliquez sur le bouton **"New repository secret"**. Dans le champ **Name**, entrez `GCP_SERVICE_ACCOUNT`. Dans le champ **Value**, collez le contenu JSON que vous avez copié précédemment. Cliquez sur **Add secret** pour l'enregistrer.

Faites de même pour le secret `GCP_PROJECT_ID`, mais ajoutez cette fois votre ID de projet Google comme valeur. Pour obtenir votre ID de projet, suivez ces étapes :

1.  **Naviguez vers la Console Google Cloud** : Ouvrez la Console Google Cloud sur [https://console.cloud.google.com/][21].
    
2.  **Localisez le menu déroulant des projets** : En haut à gauche de l'écran, à côté du **logo Google Cloud**, vous verrez un menu déroulant affichant le nom de votre projet actuel.
    
3.  **Visualisez l'ID du projet** : Cliquez sur le menu déroulant, et vous verrez une liste de tous vos projets. Votre **Project ID** sera affiché à côté du nom du projet. C'est un identifiant unique utilisé par Google Cloud.
    
4.  **Copiez l'ID du projet** : Copiez le **Project ID** affiché et ajoutez-le comme valeur du secret `GCP_PROJECT_ID`.
    

### Étape 7 : Ajouter des variables externes au dépôt GitHub 🔧

Avant de procéder au déploiement, nous devons définir certaines variables externes qui ont été référencées dans le workflow CD. Ces variables garantissent que le pipeline connaît les détails critiques sur vos services Google Cloud Run et votre registre de conteneurs Docker.

Voici les étapes à suivre pour ce faire :

1.  Tout d'abord, allez sur votre dépôt sur GitHub.
    
2.  Cliquez sur l'onglet **Settings** en haut du dépôt. Faites défiler jusqu'à **Secrets and variables > Actions**.
    
3.  Cliquez sur l'onglet **Variables** à côté de **Secrets**. Cliquez sur **"New repository variable"** pour chaque variable. Vous devrez ensuite définir ces variables :
    
    -   `GCR_PROJECT_NAME` : Définissez-le comme le nom de votre service Cloud Run pour l'environnement de production/live. Par exemple, `gcr-ci-cd-app`.
        
    -   `GCR_STAGING_PROJECT_NAME` : Définissez-le comme le nom de votre service Cloud Run pour l'environnement de staging/test. Par exemple, `gcr-ci-cd-staging`.
        
    -   `GCR_REGION` : Entrez la région où vous souhaitez déployer les services. Pour ce tutoriel, définissez-la sur `us-central1`.
        
    -   `IMAGE` : Spécifiez le nom du registre d'images Docker/conteneurs où l'image publiée sera téléchargée. Par exemple, `<dockerhub-username>/ci-cd-tutorial-app`.
        
4.  Après avoir entré chaque nom de variable et sa valeur, cliquez sur **Add variable**.
    

### Activation de l'API Service Usage sur le projet Google Cloud 🌐

Pour déployer votre application, l'**API Service Usage** doit être activée dans votre projet Google Cloud. Cette API vous permet de gérer les services Google Cloud par programmation, y compris l'activation/désactivation des API et la surveillance de leur utilisation.

Suivez ces étapes pour l'activer :

1.  Tout d'abord, visitez la Console Google Cloud sur [https://console.cloud.google.com/][22].
    
2.  Assurez-vous ensuite d'être dans le bon projet. Cliquez sur le menu déroulant des projets près du **logo Google Cloud** dans le coin supérieur gauche. Sélectionnez `gcr-ci-cd-project`, ou le nom que vous avez donné à votre projet dans la liste.
    
3.  Ensuite, vous devrez accéder à la bibliothèque d'API. Ouvrez le **Menu de Navigation** (trois lignes horizontales dans le coin supérieur gauche). Sélectionnez **APIs & Services > Library** dans le menu.
    
4.  Dans la bibliothèque d'API, utilisez la barre de recherche pour rechercher **"Service Usage API"**.
    
5.  Cliquez sur **Service Usage API** dans les résultats de recherche. Sur la page de détails de l'API, cliquez sur **Enable**.
    
6.  Pour vérifier, allez dans **APIs & Services > Enabled APIs & Services** dans la Console Google Cloud. Confirmez que la **Service Usage API** apparaît dans la liste des API activées.
    
    ![Activer l'API Google Cloud "Service Usage" dans le projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1733150269757/00a4e20b-72ac-4bd4-b05f-af6e61600e09.png)
    

## **Créer la branche staging et y fusionner la branche feature (Intégration Continue et Livraison Continue) 🌟**

Lorsque les modifications de la branche `feature/ci-cd-pipeline` sont fusionnées dans la branche `staging`, nous complétons le processus d'**Intégration Continue (CI)**, et le workflow `ci-pipeline.yml` s'exécute. Cela garantit que les modifications apportées dans la branche feature sont testées et intégrées dans une branche partagée.

Une fois que la pull request (PR) est fusionnée dans `staging`, le pipeline de **Livraison Continue (CD)** se déclenche automatiquement, déployant l'application dans l'environnement de staging. Cela simule la façon dont les mises à jour sont testées dans un environnement sûr avant d'être poussées en production.

### Créer la branche `staging` sur le dépôt distant

Pour activer le pipeline CI/CD, nous allons d'abord créer une branche `staging` sur le dépôt GitHub distant. Cette branche servira d'environnement de test où les modifications sont déployées avant d'atteindre l'environnement de production.

Pour créer la branche `staging` directement sur GitHub, suivez ces étapes :

1.  Tout d'abord, naviguez vers votre dépôt sur GitHub. Ouvrez votre navigateur web et allez sur le dépôt GitHub où vous souhaitez créer la nouvelle branche `staging`.
    
2.  Ensuite, basculez vers la branche `main`. En haut de la page du dépôt, localisez le menu déroulant **Branch** (généralement étiqueté `main` ou le nom de la branche actuelle). Cliquez sur le menu déroulant et assurez-vous d'être sur la branche `main`.
    
3.  Ensuite, créez la branche `staging`. Dans le même menu déroulant où vous voyez la branche `main`, tapez `staging` dans la zone de texte. Une fois que vous commencez à taper, GitHub vous proposera de créer une nouvelle branche appelée `staging`. Sélectionnez l'option **Create branch: staging** dans le menu déroulant.
    
4.  Enfin, vérifiez la branche. Après avoir créé la branche `staging`, GitHub basculera automatiquement vers elle. Vous devriez maintenant voir `staging` dans le menu déroulant des branches, confirmant que la nouvelle branche a été créée.
    
    ![Créer une nouvelle branche Staging dans le dépôt GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1733152232155/e6215137-5e3b-474b-88f8-af03269eccc2.png)
    

### **Fusionner votre branche feature dans la branche staging via une Pull Request (PR)**

Ce processus combine à la fois l'Intégration Continue (CI) et la Livraison Continue (CD). Vous allez committer les modifications de votre branche feature, les pousser vers la branche feature distante, puis ouvrir une PR pour fusionner ces modifications dans la branche `staging`. Voici comment faire :

#### **Étape 1 : Committer les modifications locales sur votre branche feature**

Tout d'abord, assurez-vous d'être sur la bonne branche (la branche feature) en exécutant :

```
git status
```

Si vous n'êtes pas sur la branche `feature/ci-cd-pipeline`, basculez vers elle en exécutant :

```
git checkout feature/ci-cd-pipeline
```

Maintenant, il est temps d'ajouter vos modifications pour le commit :

```
git add .
```

Cela prépare toutes les modifications, y compris les nouveaux fichiers, les fichiers modifiés et les fichiers supprimés.

Ensuite, committez vos modifications avec un message clair et descriptif :

```
git commit -m "Set up CI/CD pipelines for the project"
```

Vous pouvez ensuite vérifier votre commit en exécutant :

```
git log
```

Cela affichera vos commits les plus récents, et vous devriez voir le message de commit que vous venez d'ajouter.

#### **Étape 2 : Pousser les modifications de votre branche feature vers le dépôt distant**

Après avoir committé vos modifications, poussez-les vers le dépôt distant :

```
git push origin feature/ci-cd-pipeline
```

Cela pousse vos modifications locales de la branche `feature/ci-cd-pipeline` vers le dépôt GitHub distant.

Une fois le push réussi, visitez votre dépôt GitHub dans un navigateur web et confirmez que la branche `feature/ci-cd-pipeline` est mise à jour avec votre nouveau commit.

#### **Étape 3 : Créer une Pull Request pour fusionner la branche feature dans staging**

Allez sur votre dépôt sur GitHub et assurez-vous d'être sur la page principale du dépôt.

Vous devriez voir une alerte en haut de la page suggérant de créer une pull request pour la branche récemment poussée (`feature/ci-cd-pipeline`). Cliquez sur le bouton **Compare & Pull Request** à côté de l'alerte.

Maintenant, il est temps de choisir les branches de base et de comparaison. Sur la page de création de PR, assurez-vous que la branche **base** est définie sur `staging` (c'est la branche dans laquelle vous voulez fusionner vos modifications). La branche **compare** devrait déjà être définie sur `feature/ci-cd-pipeline` (la branche que vous venez de pousser). Si elles ne sont pas sélectionnées correctement, utilisez les menus déroulants pour les changer.

Donnez une bonne description à cette PR. Écrivez un titre et une description clairs pour la pull request, expliquant quelles modifications vous fusionnez et pourquoi. Par exemple :

-   **Titre** : "Merge CI/CD setup changes from feature branch"
    
-   **Description** : "Cette pull request ajoute les pipelines CI/CD pour GitHub Actions et l'intégration de Docker Hub au projet. Elle inclut les configurations pour les workflows CI et CD."
    

GitHub affichera alors une liste de toutes les modifications qui seront fusionnées. Prenez un moment pour les examiner et vous assurer que tout semble correct.

Si tout semble correct après examen, cliquez sur le bouton **Create pull request**. Cela créera la PR et informera les membres de l'équipe (le cas échéant) que les modifications sont prêtes à être examinées et fusionnées.

Attendez quelques secondes, et vous devriez voir un message indiquant que toutes les vérifications ont été passées. Cliquez sur le lien avec la description "**CI Pipeline to staging/production environment...**". Cela devrait vous diriger vers le workflow d'Intégration Continue, où vous pouvez visualiser les étapes qui ont été exécutées.

![Créer une nouvelle pull request (PR) de la branche feature vers staging](https://cdn.hashnode.com/res/hashnode/image/upload/v1733153444873/6ecdb277-0a45-44ec-981c-c7ee671cd2f0.png)

![Exécution du workflow CI depuis la PR (branche feature vers staging)](https://cdn.hashnode.com/res/hashnode/image/upload/v1733153637817/e12fefde-9259-41a3-9bd1-63b5da1d88ea.png)

#### Le processus d'Intégration Continue (CI)

Le processus CI commence lorsqu'une Pull Request est effectuée vers la branche `staging`. Il déclenche le workflow GitHub Actions défini dans le fichier `.github/workflows/ci-pipeline.yml`. Le workflow exécute les étapes nécessaires pour configurer l'environnement, installer les dépendances et construire l'application Node.js.

Il exécute ensuite des tests automatisés (en utilisant `npm test`) pour s'assurer que les modifications ne cassent aucune fonctionnalité dans la base de code. Si toutes ces étapes sont terminées avec succès, le pipeline CI confirme que la branche feature est stable et prête à être fusionnée dans la branche `staging` pour des tests et un déploiement ultérieurs.

#### **Étape 4 : Fusionner la Pull Request**

Si votre équipe ou des collaborateurs font partie du projet, ils peuvent examiner votre PR. Cette étape peut impliquer de discuter de tout changement ou amélioration. Si tout semble correct, un examinateur fusionnera la PR.

Une fois que la PR a été examinée et approuvée, vous pouvez fusionner la PR. Pour ce faire, cliquez simplement sur le bouton **Merge pull request**. Choisissez **Confirm merge** lorsque vous y êtes invité.

Après la fusion, vous pouvez aller sur la branche `staging` pour vérifier que les modifications ont été fusionnées avec succès.

### **Naviguer vers la page Actions après la fusion de la PR**

Une fois que vous avez fusionné avec succès votre pull request de la branche `feature/ci-cd-pipeline` vers la branche `staging`, le pipeline de Livraison Continue (CD) sera déclenché. Pour voir la progression du pipeline CD, naviguez vers l'onglet **Actions** de votre dépôt GitHub. Voici comment faire :

1.  Allez sur votre dépôt GitHub.
    
2.  En haut de la page, vous verrez l'onglet **Actions** à côté de l'onglet **Code**. Cliquez dessus.
    
3.  Sur la page Actions, vous verrez une liste des workflows qui ont été déclenchés. Recherchez celui intitulé **CD Pipeline to Google Cloud Run (staging and production)**. Il devrait apparaître comme une nouvelle exécution après la fusion de la PR.
    
4.  Cliquez sur l'exécution du workflow pour voir sa progression et consulter les logs détaillés de chaque étape.
    

![Workflow de Livraison Continue depuis la fusion vers staging](https://cdn.hashnode.com/res/hashnode/image/upload/v1733154575368/96e236a2-ae66-494b-b544-f96955a18ac9.png)

![Jobs du workflow de Livraison Continue depuis la fusion vers staging](https://cdn.hashnode.com/res/hashnode/image/upload/v1733159329441/cb7e26a9-7a20-4b1b-9869-e00facc695c1.png)

![Étapes du workflow de Livraison Continue depuis la fusion vers staging](https://cdn.hashnode.com/res/hashnode/image/upload/v1733160506355/4682afe3-bb04-405d-af4e-fd9bd3494659.png)

Cela vous permettra de surveiller l'état du pipeline CD et de vérifier s'il y a des problèmes pendant le déploiement.

Si vous regardez les étapes et le workflow CD, vous verrez que l'étape de déploiement de l'application dans l'environnement de **production** a été ignorée, tandis que l'étape de déploiement vers l'environnement de **staging** a été exécutée.

#### **Le pipeline de Livraison Continue (CD) – ce qui se passe :**

Le **Pipeline de Livraison Continue (CD)** automatise le processus de déploiement de l'application sur Google Cloud Run (environnement de test). Ce workflow est déclenché par un push vers la branche `staging`, qui se produit après que les modifications de la branche feature sont fusionnées dans `staging`. Il peut également être déclenché manuellement via `workflow_dispatch` ou lors de la publication d'une nouvelle release.

Le pipeline se compose de plusieurs étapes :

1.  **Test Job :** Le pipeline commence par configurer l'environnement et exécuter les tests à l'aide de la commande `npm test`. Si les tests passent, le processus avance.
    
2.  **Build Job :** L'étape suivante construit l'image Docker de l'application Node.js, la tague, puis la pousse vers Docker Hub.
    
3.  **Déploiement sur GCP :** Une fois l'image poussée, le workflow s'authentifie auprès de Google Cloud et déploie l'application. Si l'événement est une release (c'est-à-dire un push vers la branche `main`), l'application est déployée dans l'environnement de production. Si l'événement est un push vers `staging`, l'application est déployée dans l'environnement de staging.
    

Le processus CD garantit que toutes les modifications apportées à la branche `staging` sont automatiquement testées, construites et déployées dans l'environnement de staging, prêtes pour une validation ultérieure. Lorsqu'une release est publiée, elle déclenchera le déploiement en production, garantissant que votre application est toujours à jour.

### Accéder à l'application déployée dans l'environnement de Staging sur Google Cloud Run 🌐

Une fois que le déploiement sur Google Cloud Run est terminé avec succès, vous voudrez accéder à votre application s'exécutant dans l'environnement de **staging**. Suivez ces étapes pour trouver et visiter votre application déployée :

#### 1\. **Naviguer vers la Console Google Cloud**

Ouvrez la Console Google Cloud dans votre navigateur en visitant [https://console.cloud.google.com][23]. Si vous n'êtes pas déjà connecté, assurez-vous de vous connecter avec votre compte Google.

#### 2\. **Aller au tableau de bord Cloud Run**

Dans la Console Google Cloud, utilisez la barre de recherche en haut ou naviguez via le menu de gauche : Allez à **Cloud Run** (vous pouvez taper cela dans la barre de recherche, ou le trouver sous **Products & services** > **Compute** > **Cloud Run**). Cliquez sur **Cloud Run** pour ouvrir le tableau de bord Cloud Run.

#### 3\. **Sélectionner votre service de Staging**

Dans le **tableau de bord Cloud Run**, vous devriez voir une liste de tous vos services déployés dans divers environnements. Trouvez le service associé à l'environnement de staging. Le nom devrait être similaire à ce que vous avez défini dans votre workflow (par exemple, `gcr-ci-cd-staging`).

![Service Google Cloud Run pour l'environnement de staging](https://cdn.hashnode.com/res/hashnode/image/upload/v1733159635861/4ac895d2-5071-4d3f-9ed1-5af2bcca8835.png)

#### 4\. **Accéder à l'URL du service**

Une fois que vous avez sélectionné votre service de staging, vous serez dirigé vers la **page des détails du service**. Cette page fournit toutes les informations importantes sur votre service déployé.  
Sur cette page, recherchez la section **URL** sous l'en-tête **Service URL**. L'URL ressemblera à ceci : `https://gcr-ci-cd-staging-<unique-id>.run.app`.

#### 5\. **Visiter l'application**

Cliquez sur l'**URL du service**, et cela ouvrira votre environnement de staging dans un nouvel onglet de votre navigateur. Vous pouvez maintenant interagir avec votre application comme si elle était en direct, mais dans l'**environnement de staging**.

![URL du service Google Cloud Run pour l'environnement de staging](https://cdn.hashnode.com/res/hashnode/image/upload/v1733160050763/b097e647-bf6d-442e-87df-fc7d82d3585c.png)

## **Fusionner la branche staging dans la branche main (Intégration Continue et Déploiement Continu) 🌐**

Dans cette section, nous allons prendre les mises à jour de la branche staging, les fusionner dans la branche main et déclencher le pipeline CI/CD. Ce processus garantit non seulement que vos modifications sont prêtes pour la production, mais les déploie également dans l'environnement de production/live. 🚀

### Étape 1 : Pousser les modifications locales et ouvrir une Pull Request

**Pourquoi ?** La première étape consiste à fusionner la branche staging dans la branche main. Tout comme dans le processus précédent de Livraison Continue, cela garantit l'intégration de mises à jour minutieusement testées.

Voici comment faire :

Tout d'abord, visitez le dépôt GitHub où votre projet est hébergé.

Allez ensuite dans l'onglet **Pull Requests**. Cliquez sur **New Pull Request**. Choisissez **staging** comme branche source (base branch) et **main** comme branche cible. Ajoutez un titre et une description clairs pour la Pull Request, expliquant pourquoi ces mises à jour sont prêtes pour le déploiement en production.

### Étape 2 : Exécution du pipeline d'Intégration Continue (CI)

Après la fusion de la pull request, le pipeline d'**Intégration Continue (CI)** s'exécutera automatiquement pour valider que les modifications sont toujours stables lorsqu'elles sont intégrées dans la **branche main**.

#### Étapes du pipeline :

-   **Code Checkout** : Le workflow récupère le code le plus récent de la **branche main**.
    
-   **Dependency Installation** : Le pipeline installe toutes les dépendances requises.
    
-   **Testing** : Des tests automatisés sont exécutés pour valider la stabilité de l'application.
    

### Étape 3 : Créer une nouvelle Release

Le workflow de Déploiement Continu (CD) pour déployer dans l'environnement de production est déclenché par la création d'une nouvelle release à partir de la branche main.

Passons en revue les étapes pour créer une release.

Sur la page de votre dépôt GitHub, cliquez sur la section **Releases** (située sous l'onglet **Code**).

![Naviguer vers la page Release dans le dépôt GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1733338781623/c21e7f03-5381-47f9-8807-b5a3360245ad.png)

Ensuite, cliquez sur **Draft a new release**. Définissez la branche **Target** sur **main**. Entrez une **Tag version** (par exemple, `v1.0.0`) en suivant le versionnage sémantique. Ajoutez un **Release title** et une description facultative des changements.

Ensuite, cliquez sur **Publish Release** pour finaliser.

![Créer une nouvelle release dans le dépôt GitHub](https://cdn.hashnode.com/res/hashnode/image/upload/v1733161473858/6e14214c-31fb-49b3-9dff-a719b9ec1d40.png)

#### Pourquoi exécuter le pipeline de Déploiement Continu lors d'une release plutôt que lors d'un push ? 🤔

Dans notre configuration, nous avons décidé de ne pas déclencher le pipeline de Déploiement Continu (CD) à chaque fois que des modifications sont poussées vers la branche main. Au lieu de cela, nous le déclenchons uniquement lorsqu'une nouvelle release est créée. Cela donne à l'équipe plus de contrôle sur le moment où les mises à jour sont déployées dans l'environnement de production.

Imaginez un scénario où les développeurs travaillent sur de nouvelles fonctionnalités — ils peuvent pousser des modifications vers la branche main dans le cadre de leur workflow régulier, mais ces fonctionnalités pourraient ne pas être terminées ou prêtes pour les utilisateurs. Déployer automatiquement chaque push pourrait accidentellement exposer des fonctionnalités inachevées à vos utilisateurs, ce qui peut être déroutant ou perturbateur.

En exigeant une release pour déclencher le déploiement, l'équipe a la possibilité de finaliser et de peaufiner toutes les modifications avant qu'elles ne soient mises en ligne.

Par exemple, les développeurs peuvent tester de nouvelles fonctionnalités dans l'environnement de staging, corriger les problèmes éventuels et fusionner ces modifications dans la branche main sans s'inquiéter de les voir apparaître immédiatement en production. Ce workflow garantit que seules les fonctionnalités bien testées et complètes parviennent à vos utilisateurs finaux.

En fin de compte, cette approche aide à maintenir une expérience utilisateur fluide. Au lieu de voir des fonctionnalités à moitié construites ou des changements inattendus, les utilisateurs ne voient que des mises à jour prêtes et fonctionnelles. Cela donne également à l'équipe la flexibilité de pousser fréquemment des modifications vers la branche main — évitant les conflits de fusion et facilitant la collaboration — tout en gardant le contrôle sur ce qui est déployé en direct. 🚀

### Étape 4 : Naviguer vers la page Actions

Une fois la release publiée, le pipeline CD pour l'environnement de production est déclenché. Pour surveiller cela, répétez le processus suivi pour le workflow de Livraison Continue :

1.  **Allez dans l'onglet GitHub Actions** : Dans votre dépôt GitHub, cliquez sur l'onglet **Actions**.
    
2.  **Localisez le workflow de déploiement** : Recherchez le workflow **CD Pipeline to Google Cloud Run (staging and production)**. Vous remarquerez que le workflow a été déclenché sur la **branche main** en raison de l'événement push.
    
3.  **Ouvrir les détails du workflow** : Cliquez sur le workflow pour afficher les étapes détaillées, les logs et les états de chaque partie du processus de déploiement.
    

Cette fois, le workflow de Livraison Continue déploie l'application dans l'environnement de **production**/**live**.

![Workflow de Déploiement Continu depuis la fusion vers main](https://cdn.hashnode.com/res/hashnode/image/upload/v1733164741827/303cd415-5bb9-4149-aa5d-7088d0eab582.png)

### Étape 5 : Accéder à l'application en direct

Une fois le déploiement terminé, allez sur la Console Google Cloud sur [https://console.cloud.google.com][24].

Naviguez vers **Cloud Run** depuis le menu. Sélectionnez le service correspondant à l'**environnement de production** (par exemple, `gcr-ci-cd-app`).

Localisez l'**URL du service** sur la page de détails du service. Ouvrez l'URL dans votre navigateur pour accéder à l'application en direct.

Et maintenant, félicitations – vous avez terminé !

## Conclusion 🌟

Dans cet article, nous avons exploré comment construire et automatiser un pipeline CI/CD pour une application Node.js, en utilisant GitHub Actions, Docker Hub et Google Cloud Run.

Nous avons configuré des workflows pour gérer l'Intégration Continue en testant et en intégrant les modifications de code, et la Livraison Continue pour déployer ces modifications dans un environnement de staging. Nous avons également conteneurisé notre application à l'aide de Docker et l'avons déployée de manière transparente sur Google Cloud Run.

Enfin, nous avons implémenté le Déploiement Continu, garantissant que les mises à jour de l'environnement de production ne se produisent que lorsqu'une release est créée à partir de la branche main.

Cette approche donne aux équipes la flexibilité de pousser et de tester des fonctionnalités incomplètes sans impact sur les utilisateurs finaux. En suivant ces étapes, vous avez construit un pipeline robuste qui rend le déploiement de votre application plus fluide, plus rapide et plus fiable.

### Approfondir 📚

Si vous souhaitez en savoir plus sur l'Intégration, la Livraison et le Déploiement Continus, vous pouvez consulter les cours ci-dessous :

-   [**Continuous Integration and Continuous Delivery (CI/CD) (d'IBM sur Coursera**][25]**)**
    
-   [**GitHub Actions - The Complete Guide (sur Udemy**][26]**)**
    
-   [**Learn CI/CD by building a project (tutoriel freeCodeCamp)**][27]
    

### À propos de l'auteur 👨‍💻

Salut, je suis Prince ! Je suis un ingénieur logiciel passionné par la construction d'applications scalables et le partage de connaissances avec la communauté tech.

Si vous avez apprécié cet article, vous pouvez en apprendre plus sur moi en explorant mes autres blogs et projets sur mon [profil LinkedIn][28]. Vous pouvez trouver mes [articles LinkedIn ici][29]. Et vous pouvez [visiter mon site web][30] pour lire également d'autres de mes articles. Connectons-nous et progressons ensemble ! 😊

[1]: #heading-qu-est-ce-que-l-integration-le-deploiement-et-la-livraison-continues
[2]: #heading-differences-entre-l-integration-continue-la-livraison-continue-et-le-deploiement-continu
[3]: #heading-comment-configurer-un-projet-node-js-avec-un-serveur-web-et-des-tests-automatises
[4]: #heading-comment-creer-un-depot-github-pour-heberger-votre-code
[5]: #heading-comment-configurer-les-workflows-ci-et-cd-dans-votre-projet
[6]: #heading-configurer-un-depot-docker-hub-pour-l-image-du-projet-et-generer-un-jeton-d-acces-pour-publier-l-image
[7]: #heading-creer-un-compte-google-cloud-un-projet-et-un-compte-de-facturation
[8]: #heading-creer-un-compte-de-service-google-cloud-pour-permettre-le-deploiement-de-l-application-node-js-sur-google-cloud-run-via-le-pipeline-cd
[9]: #heading-creer-la-branche-staging-et-y-fusionner-la-branche-feature-integration-continue-et-livraison-continue
[10]: #heading-fusionner-la-branche-staging-dans-la-branche-main-integration-continue-et-deploiement-continu
[11]: #heading-conclusion
[12]: https://nodejs.org/en/download/package-manager
[13]: https://git-scm.com/downloads
[14]: http://localhost:5000/
[15]: https://github.com/
[16]: https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows
[17]: https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow
[18]: https://hub.docker.com/
[19]: https://console.cloud.google.com
[20]: https://console.cloud.google.com/
[21]: https://console.cloud.google.com/
[22]: https://console.cloud.google.com/
[23]: https://console.cloud.google.com
[24]: https://console.cloud.google.com
[25]: https://www.coursera.org/learn/continuous-integration-and-continuous-delivery-ci-cd
[26]: https://www.udemy.com/course/github-actions-the-complete-guide/?couponCode=CMCPSALE24
[27]: https://www.freecodecamp.org/news/what-is-ci-cd/
[28]: https://www.linkedin.com/in/prince-onukwili-a82143233/
[29]: https://www.linkedin.com/in/prince-onukwili-a82143233/details/publications/
[30]: https://prince-onuk.vercel.app/achievements#articles