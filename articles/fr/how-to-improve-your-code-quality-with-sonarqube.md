---
title: Comment utiliser SonarQube pour améliorer la qualité de votre code
subtitle: ''
author: Divya Valsala Saratchandran
co_authors: []
series: null
date: '2025-05-02T17:34:53.336Z'
originalURL: https://freecodecamp.org/news/how-to-improve-your-code-quality-with-sonarqube
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746207275407/7b0da6c9-9bd7-40ca-853e-b1f7957acf3b.png
tags:
- name: sonarqube
  slug: sonarqube
- name: Code Quality
  slug: code-quality
- name: ci-cd
  slug: ci-cd
seo_title: Comment utiliser SonarQube pour améliorer la qualité de votre code
seo_desc: 'SonarQube is a powerful open-source tool that helps you maintain code quality
  and security by analyzing your codebase for bugs and vulnerabilities. And it can
  play a major role when integrated into your CI/CD pipeline.

  In this tutorial, we will cover...'
---

SonarQube est un outil open-source puissant qui vous aide à maintenir la qualité et la sécurité du code en analysant votre base de code pour détecter les bugs et les vulnérabilités. Et il peut jouer un rôle majeur lorsqu'il est intégré à votre pipeline CI/CD.

Dans ce tutoriel, nous allons couvrir :

1. Qu'est-ce que SonarQube ?
   
2. Comment SonarQube améliore la qualité du code
   
3. Installation et configuration étape par étape
   
4. Comment exécuter votre première analyse de code
   

## Qu'est-ce que SonarQube ?

SonarQube est un outil open-source qui vérifie en continu la qualité du code. Il analyse le code pour trouver des problèmes comme les duplications, les mauvaises pratiques, les lacunes de couverture de test, les bugs et les vulnérabilités, en fournissant des rapports détaillés. Il fonctionne avec de nombreux langages de programmation comme Java, C#, JavaScript, Python, TypeScript et Kotlin.

Vous pouvez ajouter SonarQube à vos pipelines CI/CD, IDE et systèmes de contrôle de version comme GitHub, GitLab ou Bitbucket. Il fournit des tableaux de bord détaillés qui montrent les métriques, les tendances et les problèmes dans votre code.

Vous pouvez utiliser des règles personnalisées pour faire respecter les normes de codage et réduire la dette technique. SonarQube prend également en charge l'analyse de la couverture de code pour aider les équipes à améliorer leurs tests. Avec la fonctionnalité Quality Gate, les équipes peuvent s'assurer que seul un code propre et maintenable est mis en production.

SonarQube propose des versions gratuites et payantes pour s'adapter à toute taille d'équipe. Dans l'ensemble, il aide à améliorer la qualité des logiciels et encourage les bonnes pratiques de codage.

## Comment SonarQube améliore-t-il la qualité du code ?

Voici comment SonarQube aide à améliorer la qualité du code :

1. **Détection précoce des bugs** : Identifie les bugs avant qu'ils n'atteignent la production
   
2. **Amélioration de la maintenabilité** : Met en évidence les problèmes de code et de conception
   
3. **Analyse de sécurité** : Identifie les vulnérabilités et les risques de sécurité
   
4. **Couverture de code** : Intégration avec des outils de test pour surveiller la couverture des tests unitaires
   
5. **Règles personnalisables** : Permet aux équipes de définir des normes et des politiques de codage
   
6. **Collaboration d'équipe** : Assure une qualité de code cohérente au sein des équipes de développement
   

## Installation et configuration étape par étape

### **Prérequis :**

Voici les prérequis dont vous aurez besoin avant d'installer SonarQube

1. **Java Runtime Environment (JRE)** : Java 11 ou supérieur installé sur votre système.
   
2. **Configuration système** : 2 Go de RAM minimum (Recommandé : 4 Go+).
   
3. **MacOS** : Vous pouvez utiliser HomeBrew, qui est le gestionnaire de paquets pour MacOS qui simplifie l'installation des logiciels.
   

Voici les étapes pour installer SonarQube sur votre machine locale :

### **Télécharger SonarQube**

Téléchargez le logiciel depuis [sonarsource downloads](https://www.sonarsource.com/products/sonarqube/downloads/) et choisissez l'*Édition Communautaire* pour les projets open-source.

### **Extraire et configurer**

Pour installer SonarQube, vous devez exécuter la commande suivante pour décompresser le fichier :

```bash
unzip sonarqube-<version>.zip
cd sonarqube-<version>/bin/<votre-dossier-OS>
```

### **Démarrer SonarQube**

Sur Linux/Mac, vous devez exécuter la commande suivante :

```bash
./sonar.sh start
```

Sur Windows, vous devez exécuter celle-ci :

```plaintext
StartSonar.bat
```

### **Accéder à SonarQube**

Pour accéder à SonarQube, vous devez ouvrir un navigateur et aller à : [http://localhost:9000](http://localhost:9000)

Entrez les identifiants par défaut :

* **Nom d'utilisateur :** `admin`
   
* **Mot de passe :** `admin` (vous serez invité à le changer)
   

La page ressemblera à ceci :

![Page de création de projet SonarQube](https://cdn.hashnode.com/res/hashnode/image/upload/v1746152681985/0b1829cb-bd2a-4961-bc69-18f5d677d9dd.png align="center")

### Configurer SonarQube dans votre projet

Pour configurer SonarQube dans votre projet, commencez par ouvrir le projet Java sur votre machine. À la racine du projet, créez un fichier **sonar-project.properties**.

Ajoutez les paires clé-valeur suivantes dans le fichier :

```bash
sonar.projectKey=spring-myproject
sonar.projectName=Mon Projet
sonar.projectVersion=1.0
sonar.sources=.
sonar.host.url=http://localhost:9000
```

## Comment exécuter votre première analyse de code

### Configurer et exécuter SonarScanner

SonarScanner est l'outil qui envoie réellement votre code à SonarQube pour analyse. Voici les étapes détaillées à suivre pour l'utiliser :

#### Installer SonarScanner :

Sur Windows/Linux, téléchargez le logiciel depuis [SonarSource](https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/scanners/sonarscanner/) et décompressez-le :

```bash
unzip sonar-scanner-cli-<version>.zip
```

Sur MacOS, exécutez la commande suivante :

```plaintext
>brew install sonar-scanner
```

Pour Windows/Linux et MacOS, vérifiez l'installation en exécutant la commande suivante :

```plaintext
>sonar-scanner -v
```

#### Configurer SonarScanner

Après avoir installé SonarScanner, vous devrez le configurer en définissant l'URL du **serveur SonarQube** et le **jeton d'authentification**. Ensuite, allez dans votre profil SonarQube (coin supérieur droit > Mon Compte > Sécurité) et générez un jeton.

![Générer des jetons dans SolarQube](https://cdn.hashnode.com/res/hashnode/image/upload/v1746154994148/02ccf0cd-68ce-4447-bb1f-12ff04cd9e59.png align="center")

Donnez un nom au jeton et cliquez sur "Générer" :

![Nommer le jeton puis générer](https://cdn.hashnode.com/res/hashnode/image/upload/v1746155102747/834dcbac-070e-4958-9cb7-44a738059343.png align="center")

Dans le fichier `sonar-project.properties` de votre projet, ajoutez la propriété "sonar.login" et enregistrez.

```plaintext
sonar.projectKey=test-project
sonar.projectName=Test Project
sonar.host.url=http://localhost:9000
sonar.login=<VOTRE_JETON_ICI>
```

#### Exécuter l'analyse

Une fois SonarScanner configuré, vous pouvez commencer à analyser votre projet.

Dans un terminal ou une invite de commande, allez à la racine de votre projet (où se trouve sonar-project.properties).

Exécutez la commande suivante :

```plaintext
>sonar-scanner
```

SonarScanner analysera votre code et enverra les résultats à votre serveur SonarQube local. Visitez `http://localhost:9000`, et vous verrez votre projet listé sur le tableau de bord.

* ![Tableau de bord des résultats du scanner](https://cdn.hashnode.com/res/hashnode/image/upload/v1746151289131/d2794dc7-1a53-4787-8137-668849d50d2b.png align="center")
   

Pour voir le rapport d'analyse, allez à [http://localhost:9000/dashboard?id=java-sonar-demo](http://localhost:9000/dashboard?id=java-sonar-demo) :

![Résultats de l'analyse](https://cdn.hashnode.com/res/hashnode/image/upload/v1746151477685/931d1170-3c90-45d2-ab07-b60b551f3856.png align="center")

Si vous allez à l'onglet "Problèmes" en haut à gauche, vous pouvez voir différentes catégories de qualité logicielle, la gravité des problèmes et divers autres attributs dans votre code.

![Résultats détaillés](https://cdn.hashnode.com/res/hashnode/image/upload/v1746151632987/090c61d0-0a37-4bb1-82a1-76f149a4cc86.png align="center")

## Conclusion

Vous avez maintenant installé et configuré SonarQube et appris comment analyser votre code en utilisant SonarScanner. Vous pouvez facilement le configurer dans vos projets pour une analyse continue de la qualité du code.

C'est un outil fantastique pour garder votre base de code propre et maintenable. Comme prochaines étapes, vous pouvez envisager d'ajouter des rapports de couverture de test, de faire respecter les quality gates dans votre pipeline et d'explorer SonarCloud pour une analyse basée sur le cloud.