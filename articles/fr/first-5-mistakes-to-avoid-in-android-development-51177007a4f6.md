---
title: Erreurs critiques à éviter dans le développement Android
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-13T18:42:52.000Z'
originalURL: https://freecodecamp.org/news/first-5-mistakes-to-avoid-in-android-development-51177007a4f6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*M1tlcxNZnpB2-npa.
tags:
- name: Android
  slug: android
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Erreurs critiques à éviter dans le développement Android
seo_desc: 'By Varun Barad

  As many pioneers and leaders in different fields have paraphrased:


  In any endeavor, it is important to know what are the top few things that need to
  be done right. But, it is equally important, if not more, to know the top few things
  ...'
---

Par Varun Barad

Comme de nombreux pionniers et leaders dans différents domaines l'ont paraphrasé :

> Dans toute entreprise, il est important de savoir quelles sont les quelques choses principales à faire correctement. Mais il est tout aussi important, sinon plus, de connaître les quelques choses principales que les gens doivent éviter à tout prix.

Mes publications jusqu'à présent ont porté sur la manière d'effectuer une tâche particulière sur Android. En tenant compte de la citation ci-dessus, aujourd'hui, je vais écrire sur les cinq premières erreurs que, selon moi, les développeurs Android devraient éviter.

#### Ne pas mettre toutes les chaînes à afficher dans `strings.xml`

Cela offre une mauvaise expérience d'internationalisation, car vous devrez concevoir vos propres moyens d'afficher la version correcte d'un message en fonction de la locale de l'utilisateur.

Si les messages sont dans strings.xml, ils peuvent facilement être traduits et intégrés dans l'application. Le système d'exploitation Android gère alors de manière transparente quelle ressource de chaîne utiliser en fonction de la locale que l'utilisateur a définie sur son appareil.

Voici quelques-unes des raisons données par les utilisateurs pour ne pas utiliser les ressources de chaînes :

* **Besoin de contexte pour accéder :** si vous souhaitez afficher cette chaîne dans l'UI, vous aurez inévitablement besoin/disposerez d'un certain type de contexte là aussi. Utilisez simplement ce même contexte pour récupérer la chaîne.
* **Mais je n'en ai besoin qu'à cet endroit :** Il est impossible de savoir quand demain vous pourriez avoir besoin d'avoir cette même chaîne dans un autre fichier. Il est préférable d'investir une minute supplémentaire pour se prémunir contre les problèmes futurs.
* **Chaîne complexe avec des données d'exécution :** Mes amis, Android vous couvre. Il existe des chaînes paramétrées prises en charge par la plateforme avec une syntaxe similaire à celle utilisée dans `String.format()` de Java. De plus, les chaînes pluriels (utilisant différentes chaînes en fonction de la quantité de quelque chose) sont également prises en charge. Consultez [ce post StackOverflow](https://stackoverflow.com/questions/2397613/are-parameters-in-strings-xml-possible) pour les chaînes paramétrées et la [documentation officielle](https://developer.android.com/guide/topics/resources/string-resource.html) pour les chaînes pluriels.

#### Ne pas utiliser la liaison de données

Qui aime écrire des appels `findViewById` fastidieux et maintenir ensuite la référence à ces vues dans leur espace de noms actuel ? De plus, dans ce cas, nous devons garder nos identifiants de vue afin d'être sûrs de l'identifiant de vue que nous utilisons dans `findViewById`. Cela est dû au fait que l'autocomplétion dans Android Studio suggérera chaque identifiant (de toutes les mises en page), mais seuls ceux présents dans l'arborescence de mise en page actuelle seront disponibles pour `findViewById`. Ceux qui n'existent pas retourneront `null` (provoquant probablement une `NullPointerException`).

Google a rendu extrêmement facile l'intégration de la liaison de données dans n'importe quelle application (nouvelle/existante) et l'élimination de toutes ces références de vue fastidieuses.

Voici quelques-uns des avantages de l'utilisation de la liaison de données (par rapport à ne pas l'utiliser) :

* Références uniquement aux vues présentes (essayer de se référer à un composant absent affichera une erreur lors de l'édition du fichier dans AS. Cela générera également une erreur de compilation au lieu de vous mordre à l'exécution.).
* Un peu plus rapide car il doit parcourir tout l'arborescence de mise en page une seule fois, contrairement à chaque fois que `findViewById` est appelé.
* Votre espace de noms de travail (classe/fonction) reste propre, et vous n'avez pas à garder une référence à toutes les vues.
* Vous pouvez utiliser aussi peu de fonctionnalités dans la liaison de données que simplement l'utiliser pour éliminer les appels `findViewById` à des fonctionnalités beaucoup plus avancées (comme dans [ce post](https://medium.com/google-developers/android-data-binding-recyclerview-db7c40d9f0e4), George Mount de Google essaie d'écrire un seul adaptateur pour toutes les recycler-views dans une application).

#### Ne pas cacher les clés API

Ceci est un problème courant qui est spécifique au domaine et fait principalement par les développeurs juniors dans presque tous les domaines. Une fois que vous validez un morceau de code dans le contrôle de version, il y reste pour toujours. Même si vous supprimez cette clé API dans les validations futures, toute personne ayant accès à ce dépôt peut consulter la clé à partir de son historique et toutes sortes de problèmes peuvent suivre.

Vous pouvez consulter [ce post](https://medium.com/code-better/hiding-api-keys-from-your-android-repository-b23f5598b906) pour savoir comment cacher vos clés API de votre dépôt tout en les incluant dans le processus de construction et en les rendant disponibles dans votre code.

#### Ne pas prendre en compte le cycle de vie de l'activité

Tout type de changement de configuration entraînera la destruction de l'activité actuelle et sa recréation. Pour s'assurer que la transition est transparente pour l'utilisateur, nous devons stocker l'état dans lequel se trouvait notre application juste avant le changement de configuration. Ensuite, nous pouvons le recréer tel que l'utilisateur s'y attend en utilisant l'état après que notre activité ait été recréée suite au changement de configuration.

En parlant de cela, nous devons également stocker l'état de l'application lorsque notre activité actuelle passe à l'état arrêté. Après cela, notre application peut être tuée selon les besoins du système en ressources.

#### Ne pas apprendre les raccourcis clavier dans Android Studio

Cela peut ne pas être quelque chose qui se reflète dans le code que vous écrivez, mais cela affecte grandement votre flux de travail global. Android Studio est construit sur la base d'IntelliJ Idea (un IDE célèbre pour sa convivialité avec le clavier). Cela signifie qu'il y a beaucoup à gagner en productivité des développeurs en investissant simplement un peu de temps dans l'apprentissage des différents raccourcis clavier. Voici quelques-unes de mes ressources préférées pour vous aider :

* **KeyPromoter** — Il s'agit d'un plugin IntelliJ (disponible dans AS) qui affichera une boîte de dialogue géante et laide, montrant la commande de raccourci pour l'action que vous venez d'effectuer, chaque fois que vous utilisez votre souris pour faire quelque chose. Faites-moi confiance, celui-ci vous énervera et vous forcera en quelque sorte à apprendre ces raccourcis. Vous pouvez le trouver et le télécharger dans la section des plugins des paramètres d'Android Studio.
* **Cheat-sheet** — [Ceci est une feuille de triche imprimable officielle](https://resources.jetbrains.com/storage/products/intellij-idea/docs/IntelliJIDEA_ReferenceCard.pdf) pour les raccourcis clavier de Jetbrains (la société derrière IntelliJ). Des versions pour Windows et Mac sont disponibles.
* **Guide officiel** — [Ceci est le guide officiel](https://www.jetbrains.com/help/idea/mastering-intellij-idea-keyboard-shortcuts.html) fourni par Jetbrains pour maîtriser les raccourcis clavier sur la plateforme IntelliJ.
* Consultez également [ces](https://www.youtube.com/watch?v=hdrAlhRI5vM) [deux](https://www.youtube.com/watch?v=eOV2owswDkE) vidéos

#### C'est tout pour aujourd'hui

Ce sont les cinq choses sur lesquelles, selon moi, toute personne travaillant dans le développement Android devrait se concentrer en premier. Si vous avez d'autres suggestions concernant ces sujets ou tout autre sujet, n'hésitez pas à me contacter sur Twitter à l'adresse [@varun_barad](https://twitter.com/varun_barad).