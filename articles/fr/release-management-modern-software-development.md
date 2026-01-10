---
title: Gestion des versions pour le développement logiciel moderne – Comment gérer
  les dépendances, SemVer et les systèmes de build pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-31T17:00:00.000Z'
originalURL: https://freecodecamp.org/news/release-management-modern-software-development
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/xavi-cabrera-kn-UmDZQDjM-unsplash.jpg
tags:
- name: dependency management
  slug: dependency-management
- name: deployment
  slug: deployment
- name: software development
  slug: software-development
- name: versioning
  slug: versioning
seo_title: Gestion des versions pour le développement logiciel moderne – Comment gérer
  les dépendances, SemVer et les systèmes de build pour débutants
seo_desc: 'By Nabil Tharwat

  Releasing modern software might seem daunting and complicated. In this article,
  I''ll expand on the concepts involved in the process, from managing dependencies
  to building in the cloud.

  Articles and tutorials usually cover a specific...'
---

Par Nabil Tharwat

Publier un logiciel moderne peut sembler intimidant et compliqué. Dans cet article, je vais approfondir les concepts impliqués dans le processus, de la gestion des dépendances à la construction dans le cloud.

Les articles et tutoriels couvrent généralement un outil spécifique et plongent directement dedans sans poser les bases. Dans cet article, je vais fournir ces bases en introduisant les concepts qui sous-tendent ces outils.

Les sujets que je vais aborder incluent la gestion des dépendances (et ce que sont vraiment les dépendances !), les systèmes de build et les systèmes d'intégration continue avec un peu de glaçage sur le gâteau. Avoir cette base vous aidera à vous préparer pour ce qui va suivre.

## Qu'est-ce que les bibliothèques ?

Imaginez que vous travaillez consciencieusement sur vos tâches. Vous créez une collection d'utilitaires qui facilitent votre travail. On vous attribue ensuite un projet différent dans lequel vous avez besoin des mêmes utilitaires, et vous les copiez. Félicitations, vous venez de créer une bibliothèque et de l'utiliser dans deux projets ! 😁

Les bibliothèques sont des collections de code pré-écrit que les développeurs utilisent pour optimiser les tâches. Elles améliorent notre productivité en abstraant les tâches ennuyeuses et répétitives. Numpy, Matplotlib, Lodash, jQuery et React sont tous des exemples de bibliothèques populaires et open-source.

Vous avez probablement remarqué que chacune de ces bibliothèques (ou toute autre bibliothèque) a un numéro de version. Il est généralement constitué de quelques champs numériques séparés par des points : `v1.0.0` ou simplement `1.0.0`. Ces nombres ne sont pas aléatoires ! Il existe de nombreux schémas pour définir une version d'un produit.

Certains produits utilisent le numéro de build généré par un compilateur ou un outil CI/CD (nous allons examiner ceux-ci dans un instant). D'autres produits utilisent la date de la build au lieu du numéro de build. D'autres utilisent un hash de build ([hash](https://www.freecodecamp.org/news/p/70791fa1-2b5b-4ebc-9927-0e1c06895d4c/[<https://en.wikipedia.org/wiki/Hash_function>](<https://en.wikipedia.org/wiki/Hash_function>))).

Le schéma de versionnement le plus prominent est appelé _Versionnage Sémantique_. C'est ce que la plupart (sinon toutes) des bibliothèques de code utilisent.

## Qu'est-ce que le Versionnage Sémantique (Semver) ?

Le versionnage sémantique est un schéma de versionnement dans lequel vous avez 3 champs, chacun séparé par un point. Pour l'instant, nous appellerons le premier champ (à gauche) _Majeur_, celui du milieu _Mineur_, et le dernier _Patch_. Il ressemble exactement à ceci, avec quelques dérivations : `Majeur.Mineur.Patch`.

Selon la norme Semver, tous les champs doivent être incrémentés uniquement. Vous ne pouvez pas décrémenter aucun d'entre eux. Lorsqu'une version parente est incrémentée, tous les enfants sont réinitialisés. Donc incrémenter _Majeur_ réinitialise _Mineur_ et _Patch_ à 0.

### La version patch

La version _Patch_ est le nombre qui change le plus fréquemment. Lorsque ce nombre est incrémenté, il indique un changement qui n'ajoute pas de nouvelles fonctionnalités ou ne casse pas la fonctionnalité existante. Il peut s'agir de correctifs de sécurité, d'optimisations de performance, de corrections de bugs, etc. 

Les changements de la version _Patch_ sont toujours compatibles dans les deux sens, tant que les versions parentales sont les mêmes. Le code écrit sur `v1.0.1` fonctionnera sur `v1.0.0` et `v1.0.2`.

### La version mineure

La version _Mineur_ est le deuxième nombre qui change le plus fréquemment. Un changement de ce nombre indique une mise à jour de fonctionnalité qui ne casse pas la fonctionnalité existante. 

Les changements de la version Mineure sont toujours compatibles vers l'avant, tant que la version Majeure est la même. 

Le code écrit avec `v1.1.0` _fonctionnera_ avec `v1.2.0` mais _peut_ ne pas fonctionner avec `v1.0.0`, car vous pouvez utiliser des fonctionnalités ajoutées dans la version plus récente.

### La version majeure

La version _Majeur_ est la priorité la plus élevée et le champ le plus "dangereux" des trois. Lorsque ce nombre est incrémenté, il indique des changements cassants. Il s'agit généralement de changements d'API/interface et/ou de renommage et de suppression d'entités. 

Une nouvelle version Majeure n'est pas censée être compatible avec une autre version Majeure, donc ne vous attendez pas à ce que `v1.0.0` fonctionne avec `v2.0.0` ou vice versa. Votre code _peut_ compiler après une mise à jour, mais ce n'est que de la pure chance. 

Il existe des cas où les auteurs de bibliothèques cassent la logique sous-jacente sans affecter l'API publique que vous utilisez, donc cela ne casse pas votre code. Mais ce sont des exceptions.

Python 2 et Python 3 sont des exemples de changements cassants. Les instructions print de Python 2 ne fonctionnent pas sur l'interpréteur Python 3, et vice versa. Certaines parties peuvent fonctionner, comme les boucles for et autres structures de base, mais c'est à peu près tout.

Il est recommandé de rester à jour autant que possible avec la version _Patch_. Si vous avez besoin des nouvelles fonctionnalités, mettez à jour votre version _Mineur_. Un changement dans _Majeur_ indique des changements énormes. Soyez donc prudent lorsque vous mettez à jour. 

Il y a généralement un guide de migration avec chaque version majeure que vous devriez suivre. Vous pouvez en savoir plus sur Semver dans la [documentation officielle](https://www.freecodecamp.org/news/p/70791fa1-2b5b-4ebc-9927-0e1c06895d4c/[<https://semver.org/>](<https://semver.org/>)).

Alors... comment installons-nous et utilisons-nous des bibliothèques externes écrites par d'autres personnes en premier lieu ?

## Comment gérer les dépendances de votre projet

Dans le passé, le mieux que nous pouvions faire était de copier le code source des bibliothèques que nous utilisions dans nos projets. Nous appliquions des changements au code de la bibliothèque, corrigeions des bugs avant qu'ils ne soient publiés, et avions le contrôle sur le code. 

Mais cette pratique, communément appelée _vendoring_, est tombée en désuétude pour plusieurs raisons.

Si vous aviez appliqué des changements et qu'une nouvelle version était publiée, vous deviez réappliquer tous ces changements à nouveau. C'est un processus manuel qui doit se produire chaque fois que vous mettez à jour ou téléchargez une bibliothèque. C'est fastidieux, prend beaucoup de temps et peut casser des fonctionnalités supplémentaires que vous avez ajoutées.

Cela devient rapidement ingérable lorsque la complexité et l'échelle du projet augmentent, ce qui nous laisse avec la meilleure option : les _Gestionnaires de Dépendances_.

### Qu'est-ce qu'un gestionnaire de dépendances ?

Une dépendance est une bibliothèque ou un utilitaire dont votre projet a besoin pour fonctionner. En termes simples, si le Programme A nécessite le Programme B pour compiler et/ou s'exécuter, le Programme A dépend du Programme B. Un programme peut dépendre de plusieurs autres programmes. 

Un gestionnaire de dépendances est un outil qui suit automatiquement les dépendances d'un projet. Il vous permet d'exécuter des commandes simples dans le terminal pour installer, mettre à jour et supprimer des dépendances. NPM, Yarn, Composer, Gradle et Bundler sont tous des exemples de gestionnaires de dépendances.

Ne les confondez pas avec les gestionnaires de paquets, car ceux-ci sont des outils qui gèrent les paquets à l'échelle du système. apt-get, yum, Homebrew et Chocolatey sont des gestionnaires de paquets.

Certains gestionnaires de paquets peuvent gérer les paquets à l'échelle du système et les dépendances de projet. NPM et Yarn sont des exemples de cela.

### Comment fonctionne un gestionnaire de dépendances ?

Un gestionnaire de dépendances utilise deux fichiers principaux : un manifeste et un fichier de verrouillage. 

Le manifeste est une liste des dépendances directes de votre projet. Il liste les dépendances que vous avez directement spécifiées lors de l'installation de quelque chose. Donc lorsque vous exécutez `npm install jsdom`, il ajoute le paquet `jsdom` à la liste des dépendances dans le manifeste du projet.

Mais le manifeste ne suffit pas. Une dépendance peut avoir des dépendances, et celles-ci peuvent avoir des dépendances également, et ainsi de suite, formant un _graphe de dépendances_. Un manifeste inclut uniquement les dépendances _directes_. 

Par conséquent, lorsque vous exécutez `npm install jsdom`, le manifeste ne listera que `jsdom` malgré le fait que jsdom ait d'autres dépendances propres. Alors, comment les gestionnaires de dépendances suivent-ils l'ensemble du graphe de dépendances ?

### Qu'est-ce que les fichiers de verrouillage ?

Un fichier de verrouillage est un journal qui liste _toutes_ les dépendances du projet. Cela inclut les dépendances directes (listées dans le manifeste) et l'ensemble du graphe de dépendances. Il liste chaque dépendance avec une version spécifique, le dépôt à partir duquel elle a été récupérée, et d'autres détails.

Cette image montre une comparaison entre le graphe de dépendances (listé dans le fichier de verrouillage) et la liste des dépendances directes (listées dans le manifeste) de `jsdom`, une implémentation JavaScript de nombreuses normes web pour les tests.

![lock vs manifest.png](https://www.freecodecamp.org/news/content/images/2021/08/lock-vs-manifest.png)

D'accord, nous connaissons le graphe de dépendances exact, mais alors ? Alors tout ! Nous avons souvent plusieurs développeurs travaillant sur le même projet. Un gestionnaire de dépendances peut installer différentes versions d'une bibliothèque si plusieurs développeurs installent les dépendances du projet en utilisant uniquement le manifeste.

Un fichier de verrouillage verrouille chaque dépendance dans le graphe à une version spécifique, nous permettant d'avoir des _builds reproductibles sur différentes machines_. Cela signifie que chaque fois que quelqu'un exécute `npm install`, le code _est garanti de_ fonctionner. Cela facilite également le signalement des bugs en incluant un fichier de verrouillage dans le rapport.

Les fichiers de verrouillage permettent également aux gestionnaires de dépendances de réutiliser les paquets mis en cache au lieu de télécharger la dernière version à chaque fois que vous construisez votre projet.

Nous avons donc appris ce que sont les bibliothèques, le versionnage sémantique et les gestionnaires de dépendances. Il est maintenant temps de construire notre projet. 

## Qu'est-ce que les systèmes de build ?

Chaque processus de build est un système de build d'une manière ou d'une autre. Un système de build est un ensemble de transformations qui transforment une source en un artefact. Il peut s'agir d'une simple commande qui démarre un compilateur, d'un script pour générer un pdf à partir de fichiers texte, ou même d'une solution GUI qui construit votre projet et génère un binaire.

Un système de build se compose généralement de 3 composants : 

* Cibles
* Dépendances
* Règles 

Une cible est la sortie souhaitée. Si vous voulez un binaire appelé "test.exe", alors votre cible est exactement cela. Les dépendances sont les dépendances du projet et peuvent inclure des utilitaires d'environnement comme avoir le compilateur C++ installé, npm disponible, etc. Les règles définissent comment vous passez de la source à la cible. Elles peuvent également être les commandes utilisées.

Un système de build peut être configuré pour tester votre application, générer des rapports de couverture et lint les sources avant la construction dans le cadre de ses règles. Mais un système de build est manuel et local par défaut. Vous devez le démarrer vous-même, et il ne produit une sortie que sur votre machine locale. 

Alors... que faire si vous voulez que plusieurs développeurs puissent publier des versions de votre application de manière incrémentielle ? C'est là que le CI/CD entre en jeu !

## Systèmes d'intégration continue

En bref, l'intégration continue (CI) est un paradigme dans lequel vous validez continuellement les changements apportés à un produit. Un système CI construit et teste automatiquement chaque changement pour éviter les problèmes qui peuvent survenir en attendant une version.

La livraison continue (CD) est la pratique consistant à automatiser le processus de publication. Les versions majeures sont automatiquement déployées en staging et en production, fournissant un processus de publication automatisé.

Le déploiement continu (CD) est une étape au-dessus de la livraison continue. Il s'agit de la pratique consistant à déployer automatiquement chaque changement s'il passe toutes les étapes de votre pipeline de production, sans attendre d'approbation explicite. Cette pratique met l'accent sur l'automatisation des tests et les retours des utilisateurs, conduisant souvent à plusieurs mises à jour logicielles par mois, semaine, voire par jour !

C'est un concept large que vous pouvez lire plus en détail dans [cet article](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment). Pour l'instant, nous désignerons collectivement les systèmes qui hébergent ces pratiques sous le nom de Systèmes d'Intégration Continue.

Un système d'intégration continue (CI en abrégé) est un système de build dans le cloud qui active le système de build d'un projet à la demande et automatiquement. C'est une pierre angulaire du succès des équipes agiles. 

Les CI se composent de trois composants principaux :

* Déclencheurs
* Actions
* Recettes

Les déclencheurs sont des événements auxquels le CI écoute pour démarrer le système de build. Ces événements peuvent être un commit sur la branche principale, une pull request pour des prévisualisations de fonctionnalités, ou l'un des nombreux autres. Chaque plateforme prend en charge plusieurs événements.

Les actions sont des commandes et des scripts qui sont démarrés lors des déclencheurs. Vous pouvez dire : "Construire le projet lors d'un commit sur la branche principale" dans le langage du système.

Les recettes sont des configurations qui spécifient les déclencheurs et les actions, la configuration de l'environnement, les variables d'environnement, les systèmes de build et les dépendances du système. Elles sont le langage du système. 

> Notez que vous pouvez avoir plusieurs systèmes de build sur le même CI, chacun avec des cibles et des règles différentes.

TravisCI, Jenkins, CircleCI, GitHub Actions et GitLab CI/CD sont des exemples de CI que nous rencontrons tous les jours. Voici un exemple de recette GitHub Actions pour publier de nouvelles versions d'un programme et les envoyer à GitHub Releases :

```yaml
on:
  push:
    branches:
      - main // démarrera le CI lorsqu'un push vers la branche main est effectué

jobs:
  release_linux:
    runs-on: ubuntu-latest // doit être exécuté sur ubuntu@latest

    steps:
      - name: vérifier le dépôt git
        uses: actions/checkout@v1

      - name: installer Node.js, npm et yarn // outils d'environnement requis
        uses: actions/setup-node@v1

      - name: installer les paquets deb // dépendances d'environnement requises
        run: sudo apt-get install fakeroot dpkg rpm

      - name: construire et publier l'application
        uses: kl13nt/action-electron-forge@master
        with:
          // publier vers les releases github après une construction réussie
          release: ${{ startsWith(github.ref, 'refs/tags/v') }}
```

J'ai omis beaucoup de choses de configuration là-dedans, mais vous voyez l'idée. J'ai spécifié le déclencheur comme un commit sur la branche "main" et les actions pour cloner le dépôt du projet, installer NodeJS, npm, yarn et d'autres dépendances d'environnement. 

L'étape de build exécutera un système de build [npm-scripts](https://docs.npmjs.com/cli/v7/commands/npm-run-script/) qui lint et testera le code avant la construction. Le CI enverra ensuite les binaires de sortie à la page GitHub Releases du projet.

Un fichier de verrouillage entre également en jeu lors de l'envoi à un CI ! Si le CI installe différentes versions de dépendances de celles que vous avez localement, il peut échouer. C'est pourquoi un fichier de verrouillage est aussi nécessaire pour les CI que pour les développeurs, afin que vous puissiez être assuré que le code qui fonctionnait sur votre machine fonctionnera de la même manière sur le CI.

## Conclusion

Si vous êtes arrivé jusqu'ici, j'espère vraiment que cela a été une expérience d'apprentissage inspirante (et douce !). Vous pouvez trouver plus de mon contenu sur mon [site web](https://iamnabil.netlify.app/). Merci pour la lecture !

## Lectures complémentaires

* [Qu'est-ce que Package Lock](https://snyk.io/blog/what-is-package-lock-json)
* [The Missing Semester of Your CS Education - Metaprogramming](https://missing.csail.mit.edu/2020/metaprogramming)
* [The Simple Magic of Package Manifests and Lockfiles](https://blog.tidelift.com/the-simple-magic-of-package-manifests-and-lockfiles)