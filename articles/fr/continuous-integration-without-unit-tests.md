---
title: Comment configurer l'intégration continue sans tests unitaires
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-03T09:51:00.000Z'
originalURL: https://freecodecamp.org/news/continuous-integration-without-unit-tests
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/continuous-integration-without-unit-tests.jpg
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Productivity
  slug: productivity
seo_title: Comment configurer l'intégration continue sans tests unitaires
seo_desc: 'By Jean-Paul Delimat

  Do you think continuous integration is not for you because you have no automated
  tests? Or no unit tests at all? Not true. Tests are important. But there are many
  more aspects to continuous integration than just testing. Let''s se...'
---

Par Jean-Paul Delimat

Pensez-vous que l'intégration continue n'est pas pour vous parce que vous n'avez pas de tests automatisés ? Ou pas de tests unitaires du tout ? Ce n'est pas vrai. Les tests sont importants. Mais il y a bien plus d'aspects à l'intégration continue que simplement les tests. Voyons ce qu'ils sont.

## **1. Construction de la base de code**

C'est le problème le plus critique que l'intégration continue devrait résoudre. La branche principale de votre base de code devrait toujours se construire/compiler. Cela semble idiot de même le mentionner. 

Prenez une équipe de 12 personnes. Disons qu'un commit défectueux se retrouve dans la branche principale. Tout le monde fait un pull. Commence alors le processus de découverte de ce qui ne va pas et de coordination pour savoir qui devrait ou va le corriger. La confusion met votre équipe entière hors de ses objectifs pendant environ 30 minutes. De plus, cela cause de la frustration.

Disons que cela arrive une fois par semaine (tout le monde fait des erreurs éventuellement). 30 minutes x 12 personnes équivaut à 8 heures perdues par semaine.

Si vous êtes d'accord avec cela, vous pourriez aussi bien :

* configurer un processus CI empêchant les builds défectueux d'atteindre la branche principale
* offrir un jour de congé à un développeur chaque semaine

Même résultat, équipe plus heureuse :)

Configurer un processus CI qui garantit que votre base de code se compile prend moins d'une demi-journée de travail. Cela en vaut l'effort.

## **2. Analyse statique du code**

Cela est gratuit dans presque tous les langages et est une ligne de commande à exécuter contre un ensemble prédéfini de règles :

* Javascript : [eslint](https://eslint.org/), [tslint](https://palantir.github.io/tslint/)
* Java : [sonarlint](https://www.sonarlint.org/)
* Python : [pylint](https://www.pylint.org/)
* Go : [golint](https://github.com/golang/lint)

Configurer l'analyse statique du code (ou linting) prend environ 1 heure. Quels sont donc les avantages ? Vous avez un code bien formaté et "conforme aux règles" dans votre branche principale. C'est une augmentation claire de la qualité pour votre base de code.

Si c'est le moindre de vos problèmes parce que votre équipe est toujours pressée de respecter les délais, voyez les choses ainsi. Votre processus de revue de code sera plus rapide. Tout ce qui relève de la structure du code, des meilleures pratiques, etc., est déjà vérifié par votre processus CI. Pas besoin de le revoir ou d'en discuter. Vos développeurs peuvent se concentrer sur le contenu métier des revues de code.

Super bonus : les développeurs apprennent automatiquement les conventions de code. L'outil d'analyse statique vous montre la règle violée et explique pourquoi il est incorrect de faire cette chose.

Un obstacle avec les conventions est que les développeurs sont dogmatiques à propos, par exemple, des tabulations versus des espaces ou ce genre de choses. À la fin de la journée, de bonnes conventions sont celles qui sont suivies par tous. Choisissez un ensemble de conventions standard et suivez-les.

## **3. Changement de culture**

L'intégration continue n'est pas un problème technique. C'est un processus d'équipe. Vous voulez travailler par petites incréments et intégrer le code à la branche principale souvent. Voir [Comment commencer avec l'intégration continue](https://fire.ci/blog/how-to-get-started-with-continuous-integration/) pour une discussion plus large sur ce que l'objectif culturel est réellement.

Après que l'équipe maîtrise les premiers éléments critiques, un autre changement devrait se produire. Les gens réaliseront que travailler par petites incréments est plus efficace. Les vérifications automatisées des erreurs de base augmenteront votre confiance afin que vous puissiez fusionner le code plus rapidement. 

En conséquence, la durée de vie d'une branche diminuera. La revue de code sera plus rapide. Tout le monde travaillera avec presque le dernier code. Cela préviendra les dérives et les conflits de fusion dus aux personnes travaillant séparément. Voir [Pourquoi vous ne devriez pas utiliser de branches de fonctionnalités](https://fire.ci/blog/why-you-should-not-use-feature-branches/) pour une liste complète des avantages.

À la fin de la journée, l'intégration continue aide notre fierté et notre ego. Tout le monde devrait être heureux d'avoir un outil pour attraper leurs erreurs avant qu'elles n'atteignent le monde. 

## **Comment commencer ?**

Voici un processus très simple et actionnable pour commencer. Il fonctionne indépendamment de votre fournisseur git : GitHub, Bitbucket, Gitlab, Azure DevOps, et tous les autres.

### **1. Activer un processus de Pull Request (PR)**

Verrouillez votre branche principale contre les pushes directs. Tout devrait passer par des PR. Voici des liens sur la façon de faire cela pour [Github](https://help.github.com/en/github/administering-a-repository/enabling-branch-restrictions), [Bitbucket](https://confluence.atlassian.com/bitbucketserver/using-branch-permissions-776639807.html#Usingbranchpermissions-Addbranchpermissionsforasinglerepository), [GitLab](https://docs.gitlab.com/ee/user/project/protected_branches.html), et [Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops).

### **2. Choisir une plateforme CI**

Tous les fournisseurs git vous permettent de définir des pipelines de build pour vos PR. Les builds s'exécuteront lorsque la PR sera créée et pour chaque nouveau push vers la branche que la PR porte. Une précondition pour compléter votre PR (= fusionner votre branche) sera un build réussi.

Les grands acteurs CI sont CircleCI, Codeship et Travis CI. Je recommande bien sûr [Fire CI](https://fire.ci/) puisque c'est la plateforme que j'ai construite. Mais je ne prétends pas qu'elle est meilleure que les autres pour chaque cas d'utilisation.

Choisissez-en une et commencez.

### **3. Définir un build en 2 lignes**

Le build le plus basique que nous voulons atteindre est build + analyse statique du code. Y parvenir prend 2 ou 3 commandes dans un shell.

Toutes les plateformes CI optent pour "la configuration en tant que code". Vous définissez votre build dans un fichier *.yml à la racine de votre dépôt et la plateforme le prend en charge.

Avec Fire CI, par exemple, vous devriez ajouter un fichier .fire.yml à la racine de votre dépôt qui ressemblerait à ceci :

```yaml
pipeline:   
  dockerfile: Dockerfile
```

Ensuite, vous ajoutez un fichier nommé "Dockerfile" pour construire votre application. Voici quelques exemples de Dockerfiles simples.

Toute technologie basée sur yarn/npm comme React/Angular/Vue/Node :

```docker
FROM python:3 
WORKDIR /app  
COPY . . 
RUN yarn
RUN yarn lint 
RUN yarn build
```

Python :

```docker
FROM python:3
WORKDIR /app 
COPY . .
RUN pip install all_your_dependencies
RUN pylint all_your_python_files.py
```

Go :

```docker
FROM golang:latest
WORKDIR /app
COPY . .
RUN go build -o main .
```

Je pourrais continuer avec beaucoup d'autres exemples. Ces exemples sont simplistes et pourraient être améliorés avec quelques commandes supplémentaires. Mais vous voyez le point : c'est facile.

### **Optionnel : Activer les revues de code**

Maintenant que chaque contribution de code passe par une PR, les revues de code sont faciles à faire. Chaque fournisseur git dispose d'une interface utilisateur géniale pour présenter les différences et vous permettre de commenter le code.

Si vous êtes nouveau dans le processus, ne définissez pas un ensemble obligatoire de relecteurs car cela ralentira votre équipe. Commencez un processus de bonne volonté pour revoir le code des autres. Et construisez sur cela.

## **Et ensuite ?**

Comme pour tout, pensez grand mais commencez petit. Avoir un processus CI en place ouvre un monde d'opportunités.

### **Tests**

Une fois que vous avez le processus de base en place, il devient un jeu d'enfant d'ajouter votre premier test automatisé. Et puis quelques autres. Un effort faible mais continu peut vous apporter une couverture de test géniale avant que vous ne vous en rendiez compte.

Je vous recommande de rester lean et de ne pas investir d'efforts dans l'écriture de tests. Vérifiez ce qui se casse souvent ou nécessite beaucoup d'efforts pour être testé manuellement. Automatisez cela.   
Gardez toujours la productivité à l'esprit. Avoir une tonne de tests juste parce que cela ne vaut rien.

### **Autres avantages**

Il existe de nombreux outils que vous pouvez intégrer à votre processus CI. Ils ne sont pas clés mais l'effort versus les avantages pourraient en valoir la peine.

Voici quelques exemples ci-dessous. Les liens sont pour le marketplace GitHub mais d'autres fournisseurs git s'intègrent aussi facilement.

* Mise à jour automatique des dépendances : [Depfu](https://github.com/marketplace/depfu) vous suggère des dépendances à mettre à jour automatiquement. Ainsi, vous restez à jour en faisant de petites incréments. Cela est toujours mieux qu'une stratégie "bousculons tout" une fois par an.
* Sécurité open source : [Snyk](https://github.com/marketplace/snyk) vous avertit des menaces de sécurité dans les bibliothèques open source.
* Optimisation des images : [ImgBot](https://github.com/marketplace/snyk) détecte les grandes images dans votre dépôt et soumet une PR avec une version optimisée en taille. Pertinent pour les projets front-end, mais toujours sympa.

Il y en a beaucoup d'autres. Parcourez le marketplace pour des choses qui pourraient résoudre un problème pour vous.

Attention cependant ! Résistez à l'envie d'utiliser tout ce qui vous passe par la tête. Choisissez ceux qui offrent vraiment un gain de productivité. Les métriques ou outils gratuits que vous ne considérez pas soigneusement sont nuisibles car les gens ne sont pas sûrs de ce qu'ils doivent en faire.

## **Conclusion**

Vous n'avez pas besoin de suites de tests sophistiquées pour commencer avec l'intégration continue. 

Littéralement 2 heures d'effort peuvent vous faire avancer. Et cela permettra un cercle vertueux pour la productivité de votre équipe.

Plus votre équipe et vos projets sont grands, plus les avantages sont importants. En 2020, il n'y a pas de bonne raison de ne pas avoir un processus CI.

N'hésitez pas à [me contacter](https://twitter.com/jpdelimat) si vous avez besoin d'aide pour configurer un processus CI pour votre équipe. Je serai heureux de vous aider si je le peux.

Merci d'avoir lu et bonne chance !  
  
_Originalement publié sur The Fire CI Blog._