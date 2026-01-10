---
title: Comment maîtriser IntelliJ pour booster votre productivité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-05T15:54:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-master-intellij-to-boost-your-productivity-44b9da20c556
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MSm4kz4INUPevAEutrc80Q.jpeg
tags:
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment maîtriser IntelliJ pour booster votre productivité
seo_desc: 'By Jérémy Bardon

  DISCLAMER: This isn’t some free advertising for JetBrains, this is only about a
  developer sharing tips about IntelliJ.

  Without a doubt, the most important developer tool is the development environment
  (called IDE).

  My favourite and t...'
---

Par Jérémy Bardon

**DISCLAIMER : Ceci n'est pas de la publicité gratuite pour JetBrains, il s'agit simplement d'un développeur partageant des conseils sur IntelliJ.**

Sans aucun doute, l'outil de développement le plus important est l'environnement de développement (appelé [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)).

Mon préféré et celui que j'utilise tous les jours au travail est **IntelliJ** (version Ultimate). Dans cet article, je vais partager avec vous tous les conseils et astuces que j'ai recueillis grâce à mon expérience et à celle de mes collègues. Cela pourrait vous aider à maîtriser cet outil et à faciliter votre travail.

Ne partez pas si vous n'utilisez pas IntelliJ ou même si vous le détestez ! Je parie que vous pouvez appliquer beaucoup de ces astuces à votre IDE préféré.

### Table des matières

* [Convertir les microservices en modules](#convertir-les-microservices-en-modules)
* [Avoir des revues de code efficaces](#avoir-des-revues-de-code-efficaces)
* [Revenir sur plusieurs commits](#revenir-sur-plusieurs-commits)
* [Vérifications de sécurité pour les développeurs Java](#verifications-de-securite-pour-les-developpeurs-java)
* [Discuter avec votre base de données](#discuter-avec-votre-base-de-donnees)
* Derniers conseils : [tableau de bord d'exécution](#tableau-de-bord-dexecution), [répertoires marqués](#repertoires-marques), [fichiers temporaires](#fichiers-temporaires), [installer des plugins](#installer-des-plugins), [abuser des raccourcis](#abuser-des-raccourcis)

### Convertir les microservices en modules

Si vous travaillez sur de nombreux projets ou si votre projet met en œuvre une architecture de microservices, vous avez des projets indépendants dans de nombreux répertoires.

Cela signifie que vous devez créer un projet IntelliJ pour chaque répertoire de projet. Pourtant, vous ne pouvez pas avoir plus d'un projet dans une seule fenêtre IntelliJ.

![Image](https://cdn-media-1.freecodecamp.org/images/ixVdg6rwoneJfniiYDG-4n9hrd5mZ4wR8JGA)
_Invite si un projet est déjà chargé (Fichier > Ouvrir un projet)_

La création de modules est la solution. L'idée est de créer un projet IntelliJ avec des modules indépendants.

![Image](https://cdn-media-1.freecodecamp.org/images/ZIk1S4P-bVjvAXgo2TKCKDA70ve2hOMsgcO3)
_Créer un module à partir de votre répertoire de projet_

Vous pouvez gérer tous les modules dans la fenêtre Structure du projet (`Fichier > Structure du projet`). Ils sont également accessibles en cliquant avec le bouton droit sur un module unique et en choisissant `Ouvrir les paramètres du module`.

### Avoir des revues de code efficaces

J'espère que vous utilisez un système de contrôle de version tel que Git ou Subversion. Si ce n'est pas le cas, vous devriez envisager d'en apprendre davantage sur les systèmes de contrôle de version !

IntelliJ offre une bonne intégration pour les VCS, en particulier pour les revues de code. Si votre projet contient de nombreux dépôts dans vos modules, il est possible de visualiser chaque commit en un seul endroit.

Tout d'abord, vérifiez si le contrôle de version connaît vos répertoires :

![Image](https://cdn-media-1.freecodecamp.org/images/cLNiqaz8C2OnmPKTM-MXQ5B3Mz5rDWfESHeN)
_Fichier > Paramètres > Contrôle de version_

Ensuite, allez vérifier cette fenêtre d'outil :

![Image](https://cdn-media-1.freecodecamp.org/images/4FlaxyN9EhW8vWZEmCChmcJEVAdeKerwGeEv)
_Fenêtre d'outil de contrôle de version (onglet Journal)_

Vous devez simplement activer l'option `Afficher les noms des racines` pour voir les noms des modules à gauche. Le filtre **Chemins** vous permet de filtrer en utilisant les noms des modules. Utile lorsque vous travaillez sur des projets avec une architecture de microservices !

Le côté droit de cette fenêtre montre chaque fichier modifié à partir du commit sélectionné. Vous pouvez cliquer sur `Afficher les différences` pour ouvrir une nouvelle fenêtre et visualiser les modifications pour chaque fichier.

![Image](https://cdn-media-1.freecodecamp.org/images/LOUR2-HUn1HlLJbMcOrgqvhEkXpuyfkaXAvR)
_Contenu du commit pour les revues de code_

> Si vous devez examiner plusieurs commits en même temps, sélectionnez les commits à examiner (maintenez la touche `ctrl` enfoncée) et cliquez sur `Afficher les différences`.

### Revenir sur plusieurs commits

Pour une raison quelconque, vous devrez peut-être revenir sur quelques commits dans votre projet. Si vous n'êtes pas habitué à le faire, vous pourriez avoir des problèmes.

Revenir sur un commit est assez simple : cliquez avec le bouton droit dessus et choisissez revenir. Une fois que vous avez éventuellement résolu les conflits, une fenêtre de commit apparaîtra. Si vous ne revenez que sur un seul commit, faites comme d'habitude sans cocher l'option `Amender le commit`.

![Image](https://cdn-media-1.freecodecamp.org/images/dkiCWi7Tue6uRAkkpqW-shr8n4NOM0CcPLBw)
_Fenêtre des modifications de commit (ne pas cocher Amender pour le premier commit annulé)_

Mais si vous devez revenir sur plusieurs commits, vous devez être un peu plus malin. L'idée est de créer un commit qui annule tous les commits en une seule fois — commencez par le plus récent pour éviter les conflits.

Lorsque vous annulez un commit, vous devez valider les modifications. Cela signifie que vous ne pouvez pas effectuer plusieurs annulations et enfin valider le résultat. Ma solution est de valider la première annulation, puis de cocher l'option **Amender le commit** pour fusionner les autres annulations dans ce premier commit.

### Vérifications de sécurité pour les développeurs Java

IntelliJ est livré avec de nombreuses fonctionnalités pour Java, y compris l'intégration de Maven. Il est hautement configurable, mais avant d'explorer, vous devez vérifier certains paramètres.

* SDK du projet _(Fichier > Structure du projet)_
* Version du compilateur Java pour chaque module _(Fichier > Paramètres > Compilateur Java)_
* Configuration de Maven _(Fichier > Paramètres > Maven)_

Pour la configuration de Maven, envisagez de cocher `Toujours mettre à jour les snapshots` si vous travaillez sur des projets avec une architecture de microservices.

![Image](https://cdn-media-1.freecodecamp.org/images/X3A8LqHWqBqMxqp3kIbwfJadMdptfA21csHq)
_Vérifier la configuration de Maven_

N'oubliez pas de vérifier également la section **Fichiers ignorés** pour vous assurer qu'IntelliJ n'ignore pas votre module `pom.xml`. Si votre module n'est toujours pas reconnu comme un projet Maven, cliquez avec le bouton droit sur votre `pom.xml` et `Ajouter en tant que projet Maven`.

Parfois, vous pouvez compiler en utilisant le terminal, mais IntelliJ trouve des erreurs en raison des dépendances Maven. Pour corriger cela, cliquez avec le bouton droit sur le module `Maven > Recharger` puis cliquez à nouveau avec le bouton droit pour `Reconstruire` le module.

### Discuter avec votre base de données

J'ai essayé quelques clients pour gérer les bases de données, mais utiliser IntelliJ est bien meilleur lorsque vous écrivez également du code.

Vous pouvez explorer votre base de données sans écrire de code en utilisant l'explorateur d'arborescence. Ensuite, si vous double-cliquez sur une table, vous pouvez également filtrer les résultats, effectuer des opérations CRUD et même exporter les données dans de nombreux formats tels que SQL, CSV et HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/PeousZe3IFFleZP5Vt46oza2hXqQSb2sCy1m)
_Éditeur de table de base de données_

Comme vous pouvez le penser, les fichiers SQL supportent la [coloration syntaxique](https://en.wikipedia.org/wiki/Syntax_highlighting), l'autocomplétion et la possibilité d'exécuter des requêtes à partir du fichier. Le bon point est que vous pouvez écrire plusieurs requêtes dans votre fichier mais n'exécuter que les requêtes surlignées avec `Ctrl + Entrée`.

### Derniers conseils

#### Tableau de bord d'exécution

Il est possible d'exécuter vos applications à partir d'IntelliJ, mais vous devez d'abord créer une `Configuration d'exécution`. Une fois qu'un processus est en cours d'exécution, vous pourrez tous les lister sur un tableau de bord.

![Image](https://cdn-media-1.freecodecamp.org/images/dkbzaArlvNCv-3avb6m8zZvosKYhgmemMwCk)
_Paramètres de configuration d'exécution_

Pour activer le tableau de bord d'exécution, ouvrez la fenêtre de configuration d'exécution et sélectionnez `Par défaut`. Ensuite, vous pouvez ajouter quel type de configuration peut apparaître dans votre tableau de bord d'exécution.

#### Répertoires marqués

Lorsque vous faites un clic droit sur un répertoire, vous avez la possibilité de le marquer comme Source, Test, et même de l'exclure.

C'est utile, car vous pouvez masquer les fichiers exclus dans votre projet et également filtrer les résultats de recherche pour qu'ils n'affichent pas les tests _(dans la portée > Fichiers de production)_.

#### Fichiers temporaires

Créer des fichiers temporaires est très pratique pour tester quelque chose en dehors de votre projet. IntelliJ supporte cette fonctionnalité _(raccourci : Ctrl + Alt + Maj + Insert)_ avec de nombreux types de fichiers tels que JavaScript et SQL. Les plugins peuvent vous aider à exécuter ces fichiers. Je vous recommande d'essayer Quokka qui exécute les fichiers JS temporaires.

#### Installer des plugins

De nombreux plugins existent pour IntelliJ — presque tous les frameworks et langages populaires en ont un. Vous devriez installer ces plugins et vérifier s'ils vous aident dans votre travail quotidien.

Par exemple, consultez [Advanced Java Folding](https://medium.com/@andrey_cheptsov/making-java-code-easier-to-read-without-changing-it-adeebd5c36de) qui pourrait être intéressant pour les développeurs Java. Vous pouvez également configurer une police particulière pour distinguer facilement les caractères similaires tels que `l 1 I` et `O 0 o`. Je recommande [Source Code Pro](https://adobe-fonts.github.io/source-code-pro/) et [Hack](https://source-foundry.github.io/Hack/font-specimen.html) qui aident à éviter de confondre les caractères similaires.

#### Abuser des raccourcis

* `shift + shift` recherche partout pour un fichier
* `ctrl + shift + E` pour les fichiers récemment ouverts
* `ctrl + shift + F` recherche un texte dans le chemin (utilisez le filtre de module)
* `ctrl + clic` saute à la déclaration de variable/fonction
* `ctrl + f12` recherche une variable/fonction dans le fichier
* `alt + F7` liste les utilisations de variable/fonction

Merci d'avoir lu ! Il s'agissait d'une compilation de conseils et d'astuces que j'ai appris avec l'expérience et également avec l'aide de mes collègues. J'espère que vous avez trouvé quelque chose d'utile pour votre travail quotidien avec IntelliJ !

**Si vous avez trouvé cet article utile, veuillez cliquer sur le bouton** 💡 **plusieurs fois pour aider les autres à trouver l'article et pour montrer votre soutien ! 💡**

**N'oubliez pas de me suivre pour être informé de mes prochains articles** 💡

### Consultez mes [autres](https://medium.com/@jbardon/latest) articles

#### ➡ JavaScript

* [Série React pour débutants](https://medium.freecodecamp.org/a-quick-guide-to-learn-react-and-how-its-virtual-dom-works-c869d788cd44)
* [Comment améliorer vos compétences en JavaScript en écrivant votre propre framework de développement web](https://medium.freecodecamp.org/how-to-improve-your-javascript-skills-by-writing-your-own-web-development-framework-eed2226f190)
* [Erreurs courantes à éviter lors de l'utilisation de Vue.js](https://medium.freecodecamp.org/common-mistakes-to-avoid-while-working-with-vue-js-10e0b130925b)

#### ➡ Conseils et astuces

* [Arrêtez le débogage JavaScript douloureux et adoptez IntelliJ avec Source Map](https://medium.com/dailyjs/stop-painful-javascript-debug-and-embrace-intellij-with-source-map-6fe68eda8555)
* [Comment réduire les bundles JavaScript énormes sans effort](https://medium.com/dailyjs/how-to-reduce-enormous-javascript-bundle-without-efforts-59fe37dd4acd)