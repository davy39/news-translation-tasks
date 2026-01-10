---
title: Comment créer un système de build iOS à la demande avec Jenkins et Fastlane
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-23T01:11:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-an-ios-on-demand-build-system-with-jenkins-and-fastlane-8eb1e02c73d1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RmcSmwPhUn8ljLiiwYxK0A.png
tags:
- name: automation
  slug: automation
- name: continuous delivery
  slug: continuous-delivery
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment créer un système de build iOS à la demande avec Jenkins et Fastlane
seo_desc: 'By Agam Mahajan

  This article is about creating iOS builds through Jenkins BOT, remotely, without
  the need of a developer.


  Before starting, I want to say that this is my first article. So feel free to leave
  a comment if something can be improved :)

  W...'
---

Par Agam Mahajan

Cet article traite de la création de builds iOS via un BOT Jenkins, à distance, sans avoir besoin d'un développeur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RmcSmwPhUn8ljLiiwYxK0A.png)

Avant de commencer, je tiens à dire que c'est mon premier article. N'hésitez donc pas à laisser un commentaire si quelque chose peut être amélioré :)

#### **Pourquoi est-ce une bonne idée ?**

Lorsque qu'un développeur crée une fonctionnalité, il la teste en assurance qualité avant de la pousser en production. Un build doit donc être partagé avec l'équipe QA avec certaines configurations de test.

Xcode (l'IDE) prend un temps significatif pour compiler et générer ce build. Cela signifie que toute personne ayant besoin du build devrait installer l'IDE, cloner le dépôt, créer une identité de signature et un certificat, puis créer le build elle-même. Ou dépendre du développeur pour qu'il le crée pour elle.

Pendant le processus de création du build, l'IDE est inutilisable. Cela impacte sévèrement la productivité du développeur. Dans mon entreprise, le temps moyen de build d'un .ipa est d'environ 20 minutes. En moyenne, un développeur crée 2 à 3 builds par jour. 
Cela signifie que 5 heures de travail par semaine sont perdues.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GFEYrijn6zJapmjaN2V4dA.jpeg)
_Combien de temps supplémentaire cela prendra-t-il pour construire ?_

Mais que se passerait-il s'il existait un système automatisé capable de générer les builds par lui-même ? Cela libérerait les développeurs de cette responsabilité. Cela permettrait également à n'importe qui d'obtenir facilement un build.

Jenkins est l'une des solutions à notre problème.

Rendre les builds facilement accessibles aux testeurs et aux développeurs garantit que les gens peuvent tester les fonctionnalités plus rapidement et les déployer en production plus facilement. Cela améliore la productivité des équipes de développement. Cela améliore également la qualité des produits poussés en production.

### **Commençons maintenant.**

#### **Prérequis**

Vous aurez besoin de :

* Une machine macOS (il est préférable de l'exécuter sur des produits Mac)
* 10 Go d'espace disque (pour Jenkins)
* Java 8 installé (un JRE ou un Java Development Kit (JDK) convient)  
[http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

**Plugins supplémentaires à installer**

* homebrew
* wget
* Plugin RVM  
[Guide d'installation](http://usabilityetc.com/articles/ruby-on-mac-os-x-with-rvm/)  
[https://rvm.io/rvm/security](https://rvm.io/rvm/security)

Créez une branche avec un fichier nommé `Jenkinsfile` contenant le code suivant :  
`_node {_`  
 `_sh 'echo HelloWorld'_`  
`_}_`  
Appelons-la **jenkins-integration**. Nous y reviendrons plus tard.

* Installez Xcode sur votre machine depuis l'App Store
* Installez Fastlane sur votre machine. Jenkins utilisera en interne les commandes fastlane pour générer les builds.

Maintenant, passons en revue les étapes une par une.

### **Étape 1. Installer Jenkins sur votre machine**

Vous pouvez l'installer sur un MacBook ou un mac-mini. Le mac-mini est préféré car il peut être laissé allumé.

Téléchargez Jenkins -&gt; https://jenkins.io/

Exécutez **java -jar jenkins.war --httpPort=8080** dans la ligne de commande. Si vous obtenez une erreur dans le terminal, essayez un autre port (par exemple, 9090) car parfois certains ports ne sont pas disponibles.

Accédez à [http://localhost:8080](http://localhost:8080) et suivez les instructions pour compléter l'installation.

Ajoutez ensuite les identifiants d'administrateur et ne les oubliez pas (comme je l'ai fait :P). Plus tard, vous pouvez aller dans **Jenkins > Manage Jenkins > Manager** Users et effectuer vos modifications si nécessaire.

### **Étape 2. Créer votre premier Pipeline**

Créez un nouveau job et choisissez **Pipeline Project**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cN7MqM8LaClcPg29kVGq_Q.png)

Pour vérifier votre projet, dans la section **Pipeline**, sous **Definition**, choisissez **Pipeline Script from SCM** et dans SCM, choisissez **Git**

Ajoutez ensuite l'URL de votre dépôt et ajoutez les identifiants si c'est un dépôt privé. Dans les branches à construire, ajoutez */**jenkins-integration**, la branche que nous avons créée précédemment.

Assurez-vous que le chemin du script est **Jenkinsfile** que nous avons créé dans notre nouvelle branche. Tous les scripts seront écrits dans ce Jenkinsfile.

![Image](https://cdn-media-1.freecodecamp.org/images/1*l6wpHeIHZZ5ZuoTjcdJoLA.png)

Cliquez sur Enregistrer et Jenkins analysera automatiquement votre dépôt avec la branche mentionnée et exécutera le script Jenkinsfile.

![Image](https://cdn-media-1.freecodecamp.org/images/1*v7QhFuQlGH9YhjEruS52nw.png)

Maintenant, nous sommes prêts à configurer notre Jenkinsfile pour créer des builds

### **Étape 3. Ajouter des paramètres au Job**

L'entrée utilisateur est requise pour

* la branche
* l'environnement (test ou prod)

Pour cela, nous devons configurer notre projet pour prendre des paramètres d'entrée pour un job.

Allez dans la section **Configure** et cochez **This project is parameterised**.
Ensuite, sélectionnez ajouter un paramètre et ajoutez-le en conséquence.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EfmwPbDPa-YwWAZ-rEU2cw.png)

Lorsque vous cliquez sur enregistrer, vous verrez une nouvelle section sur le côté gauche -&gt; **Build with Parameters**. Ce sera l'interface utilisateur pour créer des builds.

![Image](https://cdn-media-1.freecodecamp.org/images/1*msne-k6C4ksZdj8NpbGdrA.png)

Ces paramètres seront utilisés dans notre script Jenkins.

### **Étape 3. Configurer le script Jenkins**

Nous allons créer plusieurs étapes dans notre Jenkinsfile, chacune ayant une responsabilité, et cela créera une belle interface utilisateur lorsqu'il sera construit.

Allez dans votre Jenkinsfile et remplacez le script par ce qui suit :

Tout d'abord, vérifiez la branche via le paramètre que nous avons ajouté précédemment. Ajoutez votre dépôt et votre jeton GitHub.

Maintenant, le jeton GitHub ne doit pas être visible par les autres. Pour cela, allez dans **Manage Jenkins** -> **Configure System** -> **Global properties** et ajoutez **githubToken** comme variable d'environnement.

Ensuite, invoquez le script pour changer l'environnement.

Ensuite, invoquez fastlane pour nettoyer (supprimer les données dérivées, nettoyer, supprimer les fichiers .dsym, etc).

Si la signature de code est requise, faites-le ensuite en utilisant **ad-hoc**. Vous pouvez utiliser **development** ou **app store** en fonction de vos besoins.

Ensuite, créez des builds en utilisant la commande **gym** dans fastlane.

### **Étape 4. Exécuter le Job**

Maintenant, notre script est prêt. Allez dans Jenkins et ouvrez **Build with Parameters**.

Il commencera à exécuter le script et créera une belle interface utilisateur avec plusieurs étapes comme mentionné dans le Jenkinsfile.

![Image](https://cdn-media-1.freecodecamp.org/images/1*atL19HWAh9PkfnyxjfcsMg.png)

Lorsque le job est terminé, allez dans le projet **Users/agammahajan/.jenkins/workspace/iOS_Build_Systems**  
et vous verrez que le .ipa a été créé. Voilà !

Maintenant, vous pouvez partager ce build avec d'autres. Vous pouvez utiliser le plugin Slack pour télécharger les builds sur Slack si vous le souhaitez.

#### **Conclusion**

Pour conclure, nous pouvons voir à quel point il est facile de configurer un bot automatisé qui permet à n'importe qui de déclencher des builds en seulement 2 étapes : **Donner la branche -> Environnement de test ->** Terminé.

Cela m'a aidé, moi et mes collègues développeurs, à améliorer la productivité et à livrer plus rapidement. Cela a également aidé l'équipe QA, afin qu'ils n'aient pas à dépendre des développeurs chaque fois qu'ils doivent tester quelque chose. J'espère que cela vous bénéficiera, à vous et à votre entreprise également.

À partir de là, les **possibilités** sont infinies.

1. Vous pouvez créer des jobs planifiés pour générer des builds nocturnes.
2. Télécharger des builds directement sur l'App Store.
3. Mettre en cache les builds, afin que les builds avec la même configuration ne soient pas générés à nouveau.
4. Distribuer l'IPA en interne pour une installation OTA (Over the air).
5. Créer un pipeline CI-CD pour exécuter des tests automatisés à chaque commit et les rendre prêts pour la production.