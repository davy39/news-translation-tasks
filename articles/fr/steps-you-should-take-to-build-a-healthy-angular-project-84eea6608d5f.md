---
title: Étapes à suivre pour construire un projet Angular sain
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-16T22:53:15.000Z'
originalURL: https://freecodecamp.org/news/steps-you-should-take-to-build-a-healthy-angular-project-84eea6608d5f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q_Tuv1uGF5i5opPCuZrh0A.png
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: Jenkins
  slug: jenkins
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Étapes à suivre pour construire un projet Angular sain
seo_desc: 'By Ashish Gaikwad

  Create your “Angular Fitbit” with Jenkins + SonarQube


  Just like the recent introduction of wearables to track our health, the software
  industry has long followed the practice of monitoring the health of software projects.
  The most ...'
---

Par Ashish Gaikwad

#### Créez votre "Angular Fitbit" avec Jenkins + SonarQube

![Image](https://cdn-media-1.freecodecamp.org/images/wjMyKOsxM2Mcyv9WVWqsjKodQ0tksqkMMpGb)

Tout comme l'introduction récente des wearables pour suivre notre santé, l'industrie du logiciel suit depuis longtemps la pratique de surveillance de la santé des projets logiciels. Les processus les plus courants appliqués sont les tests unitaires, les tests d'intégration, l'intégration continue et la couverture de code.

J'ai récemment eu un peu de mal à configurer les processus mentionnés ci-dessus pour notre projet, alors j'ai écrit cet article pour documenter mon expérience. Puisque TypeScript est le langage par défaut pour les projets Angular 2, les configurations JS existantes ne fonctionnent pas.

### Pour commencer

Voici les étapes pour configurer un environnement Jenkins CI pour les projets Angular avec couverture de code en utilisant SonarQube sur un serveur Linux sans tête :

* Téléchargez [Jenkins](https://jenkins.io/) et installez-le sur votre serveur de build. Assurez-vous d'avoir Java installé sur celui-ci, car il est requis par Jenkins. **Note** : La configuration par défaut de Jenkins s'exécute avec l'utilisateur `jenkins`, vous devrez donc peut-être définir `JAVA_HOME` pour l'utilisateur `jenkins`.
* Une fois Jenkins configuré, installez ou assurez-vous d'avoir les plugins suivants installés à partir du menu de gestion des plugins :

![Image](https://cdn-media-1.freecodecamp.org/images/Z1fjqabmgmBITHEsZaWFDf1FOYOpZI-alnLR)
_[**Plugin Git**](http://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin" rel="noopener" target="_blank" title=") **pour la configuration du dépôt**_

![Image](https://cdn-media-1.freecodecamp.org/images/Ynn9vwg7yFFUHeRcH5IzcmcYLjb2lcnse8mY)
_[**Plugin NodeJs**](http://wiki.jenkins-ci.org/display/JENKINS/NodeJS+Plugin" rel="noopener" target="_blank" title=") **pour exécuter les commandes et scripts npm**_

![Image](https://cdn-media-1.freecodecamp.org/images/DqokQi13Q-TFB0a0VLSEKNP4je9sIdhFiu9e)
_[**Analyseur SonarQube**](http://redirect.sonarsource.com/plugins/jenkins.html" rel="noopener" target="_blank" title=") **pour l'analyse et la publication des rapports de test.**_

* Rendez Git, Node et l'analyseur SonarQube disponibles pour Jenkins. Cela peut être fait à partir du menu **Configuration des outils globaux** dans le menu **Gérer Jenkins**. Vous pouvez choisir d'installer automatiquement ou de fournir le chemin d'installation pour ces outils. Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/tE0Qjwua7ul3uwGOM-gYThmyhfJD82ASDDt3)
_Fournir le chemin pour l'installation locale._

* Enfin, faites connaître à Jenkins l'installation du serveur SonarQube à partir du menu **Configurer** dans **Gérer Jenkins**. Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/SAtVBrKnLxF4kfg2zHLxnQkjvEB3stLLLoXb)
_Configuration de l'URL du serveur SonarQube dans Jenkins_

Téléchargez [SonarQube](https://www.sonarqube.org/) et installez-le sur votre serveur. Il s'agit généralement d'une simple extraction de package sur toutes les plateformes.

Pour activer la prise en charge de TypeScript dans SonarQube, nous utiliserons le [**SonarTsPlugin**](https://github.com/Pablissimo/SonarTsPlugin) puisque SonarQube n'a pas encore de plugin par défaut pour TypeScript. Téléchargez simplement le jar depuis la [page des versions](https://github.com/Pablissimo/SonarTsPlugin/releases) du plugin et placez-le dans le dossier `**bin**` de votre installation SonarQube. Redémarrez Jenkins une fois. C'est tout.

Dans le fichier `**karma.conf.js**` des projets Angular, modifiez/ajoutez dans la section `browsers` `ChromeHeadless`.

Exemple : `**browsers:['ChromeHeadless']**`. À partir de la version 60, [Google Chrome supporte le mode headless](https://developers.google.com/web/updates/2017/04/headless-chrome) sur Windows également. Vous pouvez donc continuer à utiliser ce paramètre sur votre machine locale également, au cas où vous travailleriez sur une machine Windows dans un environnement d'entreprise (comme je le fais). Je préfère personnellement le mode headless uniquement pour les 1-2 secondes qu'il me fait gagner.

Ajoutez ce qui suit à la section `**scripts**` dans le fichier `**package.json**`.

![Image](https://cdn-media-1.freecodecamp.org/images/RXJqP0brv2WpNbxhjnmxG8522mLee71UonFR)
_Commande NPM pour le test suivie de la construction_

La commande ci-dessus garantit que la construction est **déclenchée uniquement si tous les tests sont réussis**. Le drapeau `**--cc**` est un code court pour `**--code-coverage**`. Ce drapeau produira le rapport de couverture du projet dans un nouveau dossier nommé `**coverage**` dans le répertoire du projet. Le fichier de rapport s'appelle `**lcov.info**`.

La configuration par défaut utilise le rapporteur Istanbul pour afficher le rapport de couverture de code. Pour publier ce rapport de couverture sur le serveur SonarQube, le plugin d'analyseur Jenkins SonarQube nécessite une configuration qui peut être ajoutée en tant que fichier `**sonar-project.properties**` au projet ou dans la configuration du projet Jenkins. Exemple de fichier de propriétés :

![Image](https://cdn-media-1.freecodecamp.org/images/WlS8OKVSTkUI6CcXgAn-crU-tpNVTWfHbLoS)
_Fichier sonar-project.properties exemple._

### Configuration

Avec les étapes ci-dessus terminées, la configuration du projet dans Jenkins est assez simple.

Tout d'abord, créez une nouvelle configuration en utilisant le menu **Nouvel élément**, puis un **Projet freestyle**.

Ensuite, dans la section **Gestion du code source**, activez **Git** et configurez l'URL du dépôt du projet :

![Image](https://cdn-media-1.freecodecamp.org/images/5gEgzqe6qCIPmd60CTD0XzzvlU7AGf3hisnz)
_Configuration du dépôt dans la configuration du projet Jenkins._

Dans la section **Environnement de construction**, activez la case à cocher pour fournir l'environnement node et npm à la configuration de construction.

![Image](https://cdn-media-1.freecodecamp.org/images/m2ioZHC6dtQwyNJq4uS260Xffyxne4oEVlHs)
_Fournir node et npm à la construction actuelle._

Ensuite, dans la section **Construction**, ajoutez deux étapes de construction. D'abord **Exécuter Shell** et ensuite **Exécuter l'analyseur SonarQube**.

L'étape shell est pour exécuter le script npm `**cibuild**` et cette dernière pour déclencher l'analyse du rapport de couverture. Comme mentionné ci-dessus, les propriétés sonar peuvent également être définies dans la configuration de construction. Exemple de configuration de construction :

![Image](https://cdn-media-1.freecodecamp.org/images/olqC-tt1a7qk6BgZxJjOH9iHiLejWRyE5vuD)
_Section de construction avec npm et analyse sonar_

C'est tout. Maintenant, une construction peut être déclenchée en utilisant le menu **Construire maintenant** sur la page d'accueil des projets.

> _Le journal de construction affichera les résultats des tests, les journaux de construction et le journal de publication sur le serveur SonarQube. Il est idéal de configurer des déclencheurs distants ou des webhooks pour déclencher la construction du projet. Cela garantira la stabilité du projet chaque fois qu'il y a un changement dans le dépôt._

Enfin, en visitant le serveur SonarQube, les détails du projet devraient être visibles avec toutes les métriques capturées à partir du rapport de couverture de code. Exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/v3aWz3iidRPk0KIDZRnI2A26a9uEFRaqSm3I)
_Tableau de bord des projets Sonar._

Ce n'est que la première étape vers la création d'une base de code plus saine. La construction Jenkins peut être encore améliorée pour créer une construction de pipeline pour un meilleur contrôle et des modifications granulaires.

_Publié à l'origine sur [medium.com](https://medium.com/@ashishgkwd/angular-fitbit-jenkins-sonarqube-829cc6201469) le 16 septembre 2017._