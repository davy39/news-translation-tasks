---
title: Comment travailler sur un projet multi-bibliothèques dans Android – Localement
  et à distance
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2024-04-27T22:37:15.000Z'
originalURL: https://freecodecamp.org/news/working-on-a-multiple-library-project-in-android
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/sandy-millar-5PCeHBkMCmk-unsplash.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
seo_title: Comment travailler sur un projet multi-bibliothèques dans Android – Localement
  et à distance
seo_desc: "In this article, we're going to talk about multi-library projects in Android.\
  \ It's not something ordinary, but not something out of the ordinary either. \n\
  You may have come across multi-library projects in your line of work, or you may\
  \ be looking into..."
---

Dans cet article, nous allons parler des projets multi-bibliothèques dans Android. Ce n'est pas quelque chose d'ordinaire, mais ce n'est pas non plus quelque chose d'extraordinaire.

Vous avez peut-être rencontré des projets multi-bibliothèques dans votre travail, ou vous envisagez peut-être de convertir votre bibliothèque en sous-modules pour une meilleure structure et organisation. Dans tous les cas, vous devez être bien conscient de ce qui vous attend avant de vous lancer.

Écrire votre propre bibliothèque dans Android est une bonne chose. Vous avez l'opportunité d'écrire du code qui peut aider d'autres développeurs (ou même vous-même).

Puisque les bibliothèques ne peuvent pas être un projet autonome par elles-mêmes, elles sont généralement toujours associées à un projet avec une application. Cela permet de développer la bibliothèque de manière simple où vous ajoutez une fonctionnalité/corrigé un bug et ensuite vous pouvez le tester directement avec l'application que vous avez dans le projet. Ainsi, en simulant (de manière locale) comment un développeur intégrera votre bibliothèque.

Mais, que se passe-t-il si votre bibliothèque dépend d'une autre bibliothèque que vous développez ?

Si vous n'en êtes pas conscient, vous devez savoir qu'une bibliothèque (lire aar) ne peut pas contenir une autre bibliothèque locale en son sein. Elle peut dépendre de bibliothèques à distance (via des dépendances), mais pas de quelque chose de local. 

Cela n'est pas supporté dans Android, et bien que certaines solutions aient émergé au fil des ans ([FatAar](https://github.com/kezong/fat-aar-android)), celles-ci n'ont pas toujours résolu le problème et ne sont pas à jour. Il existe même un [Google Issue Tracker](https://issuetracker.google.com/issues/62121508?pli=1) demandant cette fonctionnalité qui est ouvert depuis assez longtemps et reçoit beaucoup d'attention de la communauté. Mais identifions quels murs nous pouvons briser et lesquels nous ne pouvons pas.

Imaginez que votre hiérarchie de projet ressemble à ceci :

```
-- App
|
 -- OuterLib
   |
    --- InnerLib
```

Donc, puisque InnerLib ne peut pas faire partie de votre projet original, où peut-elle résider ? Et aussi, comment pourriez-vous travailler localement tout en développant des fonctionnalités à l'intérieur de InnerLib ?

Nous allons répondre à ces questions dans cet article.

## Git Submodule

Pour la plupart des problèmes techniques, il n'y a pas toujours une seule solution. Habituellement, il y en a plusieurs, mais chaque solution a ses inconvénients. Tout est une question de savoir quels inconvénients vous êtes plus à l'aise de vivre à la fin de la journée.

Pour répondre à notre première question, où InnerLib peut-elle résider, nous avons plusieurs options :

1. Faire de InnerLib un sous-module de notre projet original
2. Faire de InnerLib une dépendance distante à part entière

Si vous n'êtes pas familier avec les sous-modules dans Git, [la documentation de Git](https://git-scm.com/book/en/v2/Git-Tools-Submodules) est un bon endroit pour vous familiariser avec eux. En citant (le premier paragraphe) :

> Il arrive souvent que, tout en travaillant sur un projet, vous ayez besoin d'utiliser un autre projet à l'intérieur de celui-ci. 👉 Peut-être est-ce une bibliothèque développée par un tiers ou que vous développez séparément et utilisez dans plusieurs projets parents. 👈 Un problème courant se pose dans ces scénarios : vous voulez pouvoir traiter les deux projets comme séparés tout en étant capable d'utiliser l'un à l'intérieur de l'autre.

Ce paragraphe nous montre que c'est exactement notre cas d'utilisation. Utiliser un sous-module a ses avantages. Tout votre code est au même endroit, facile à gérer et facile à développer localement. 

Mais les sous-modules ont quelques faiblesses. L'une est le fait que vous devez toujours être conscient de la branche vers laquelle votre sous-module pointe. Imaginez un scénario où vous êtes sur une branche de release dans votre dépôt principal et votre sous-module est sur une branche de fonctionnalité. Si vous ne le remarquez pas, vous publiez une version de votre code avec quelque chose qui n'est pas prêt pour la production. Oups.

Maintenant, imaginez cela dans une équipe de développeurs. Une erreur négligente peut être coûteuse.

Si la première option semble problématique pour vous, alors héberger votre bibliothèque dans un autre dépôt est votre deuxième choix. Configurer le dépôt est assez simple, mais comment travaillez-vous localement maintenant ?

## Travailler localement

Maintenant que nous avons correctement configuré notre projet, nous aurons probablement une ligne similaire à celle-ci dans notre fichier build.gradle de OuterLib :

```
dependencies {
  implementation 'url_to_remote_inner_lib_repository'
} 
```

Comment pouvons-nous rendre le cycle de développement efficace et facile à utiliser ? Si nous développons une fonctionnalité dans InnerLib, comment testons-nous les choses dans OuterLib ? Ou dans notre application ?

Une solution qui pourrait venir à l'esprit est d'importer notre InnerLib localement dans notre projet OuterLib, tout en ayant InnerLib .gitignoré dans notre projet OuterLib. Vous pouvez le faire facilement en cliquant avec le bouton droit sur le nom du projet dans le menu de gauche dans Android Studio et en allant vers Nouveau → Module.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/1.jpg)
_Comment importer un module (Étape 1)_

Ensuite, dans la fenêtre qui s'ouvre, vous pouvez choisir l'option Importer en bas à gauche :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/1-1.jpg)
_Comment importer un module (Étape 2)_

Cela semble facile et simple jusqu'à présent, mais quel est le piège ?

Chaque fois que vous modifiez un fichier appartenant à InnerLib, les changements ne seront pas reflétés à l'intérieur de InnerLib puisqu'il est ignoré. Donc, chaque changement que vous souhaitez apporter doit se faire à l'intérieur de InnerLib et ensuite vous devez l'importer à nouveau à l'intérieur de OuterLib pour voir les changements.

Cela ne semble pas correct. Il doit y avoir une meilleure façon de faire cela.

Avec seulement quelques lignes dans notre fichier **settings.gradle**, nous pouvons nous assurer que nos fichiers restent synchronisés lorsque nous apportons des modifications à InnerLib. 

Lorsque nous avons importé InnerLib dans notre projet, Android Studio a fait une copie de InnerLib et l'a mise en cache. C'est pourquoi nous devions réimporter la bibliothèque pour chaque changement que nous avons fait à l'intérieur. Nous pouvons dire à Android Studio où référencer les fichiers en utilisant l'attribut **projectDir**. 

Notre settings.gradle pourrait ressembler à ceci :

```
include ':outerLib', ':innerLib', ':app'
```

Pour référencer notre InnerLib localement, nous devrions changer settings.gradle en ceci :

```
include ':outerLib', ':innerLib', ':app'
project('innerLib').projectDir = new File('PATH_TO_INNER_LIB')
```

En utilisant cette approche, nos fichiers InnerLib seront liés à notre répertoire de travail, donc chaque changement que nous apportons sera reflété immédiatement. 

Mais, nous aimerions avoir de la flexibilité lorsque nous travaillons localement sur OuterLib avec une version distante de InnerLib. Ce que nous avons écrit ci-dessus dans le fichier settings.gradle ne nous permettra de travailler que localement et sûrement nous ne voulons pas commiter cela tel quel.

## Maven Local

Si l'approche ci-dessus ne vous convient pas tout à fait, il y en a une autre que vous pouvez prendre. Tout comme vous publieriez votre bibliothèque publiquement avec maven, vous pouvez faire la même chose localement avec maven local. Maven local est un ensemble de dépôts qui résident localement sur votre machine.

Voici les chemins pour mavenLocal selon le système d'exploitation de votre machine :

* Mac → /Users/YOUR_USERNAME/.m2
* Linux → /home/YOUR_USERNAME/.m2
* Windows → C:\Users\YOUR_USERNAME\.m2

En essence, vous pouvez publier votre bibliothèque localement et ensuite la lier dans votre projet. En faisant cela, nous pouvons lier notre projet à InnerLib. 

Pour permettre cette configuration dans notre projet, nous devons faire les choses suivantes :

1. Ajouter **_mavenLocal()_** en tant que dépôt à l'intérieur de notre clause repositories. Cela permet à notre projet de rechercher des dépôts localement

```
buildscript {
    repositories {
        mavenLocal()
    }
}

...

allprojects { 
    repositories { 
        mavenLocal() 
    }
}
```

2.  Changer notre ligne d'implémentation à l'intérieur de notre clause de dépendances pour référencer notre InnerLib comme si nous la référencions à distance

3.  Pour publier InnerLib localement, nous allons créer un fichier appelé publishingLocally.gradle qui contiendra ce qui suit :

```
apply plugin: 'maven-publish' 

project.afterEvaluate {
    publishing { 
      publications {
            library(MavenPublication) { 
                    setGroupId groupId          //votre package de bibliothèque
                    setArtifactId artifactId              
                    version versionName         //I.E. 1.0

                    artifact bundleDebugAar

                    pom.withXml { 
                        def dependenciesNode = asNode().appendNode('dependencies')
                        def dependencyNode = dependenciesNode.appendNode('dependency')
                        dependencyNode.appendNode('groupId', 'your_group_id')
                        dependencyNode.appendNode('artifactId', 'your_artificat_id')
                        dependencyNode.appendNode('version', 'your_version')
                    } 
                }
            }
        }
}
```

4.  À l'intérieur de votre fichier build.gradle au niveau de l'application, ajoutez la ligne :

```
apply from: '/.publishingLocally.gradle
```

Si cette option semble un peu trop belle pour être vraie, **c'est le cas**. D'une part, nous pouvons développer des choses localement de manière transparente, comme si nous travaillions avec une bibliothèque distante. D'autre part, si nous apportons une modification à l'intérieur de InnerLib tout en travaillant localement, il est nécessaire de la publier à nouveau localement. Bien que ce ne soit pas une tâche coûteuse, cela crée un besoin d'effectuer des tâches fastidieuses encore et encore.

## Une solution pour travailler localement et à distance

Nous voulons éviter le besoin constant de republier notre package InnerLib chaque fois que nous apportons une modification localement. Nous devons trouver un moyen de faire en sorte que notre projet soit conscient de ces changements. 

Dans la section Travailler localement, nous avons découvert comment faire cela, mais nous avions un problème avec le commit du fichier settings.gradle. Pour résoudre ce problème afin que nous puissions travailler à la fois localement et à distance avec notre InnerLib, nous allons utiliser un paramètre que nous définirons dans notre fichier **_gradle.properties_**.

Le fichier gradle.properties est un endroit où vous pouvez stocker des paramètres au niveau du projet qui configurent votre environnement de développement. Cela aide à s'assurer que tous les développeurs d'une équipe ont un environnement de développement cohérent. 

Certains paramètres avec lesquels vous pourriez être familier et qui se trouvent à l'intérieur de ce fichier sont la prise en charge d'AndroidX (android.useAndroidX=true) ou les arguments JVM (org.gradle.jvmargs=-Xmx1536m). 

Pour nous aider à résoudre notre situation, nous pouvons ajouter un paramètre ici pour indiquer si nous voulons travailler localement ou non. Quelque chose comme :

```
workingLocally = false
```

Ce paramètre nous donnera la possibilité de distinguer entre les paramètres avec lesquels nous travaillons, soit localement, soit avec du code de production. Tout d'abord, modifions ce que nous avons dans notre fichier settings.gradle en l'enveloppant dans une condition qui vérifie si notre paramètre est vrai :

```
include ':outerLib', ':innerLib', ':app'
if (workingLocally.booleanValue()) {
  project('innerLib').projectDir = new File('PATH_TO_INNER_LIB')
}
```

De cette manière, nous indiquons au projet de récupérer les fichiers pour notre InnerLib localement depuis notre machine. 

Un autre endroit où nous devons changer notre logique est dans notre fichier build.gradle. Ici, au lieu de récupérer le code de notre bibliothèque à distance dans notre bloc de dépendances, nous pouvons indiquer si nous en dépendons localement ou non.

```
dependencies {
   if (workingLocally.booleanValue()) {
      implementation 'innerLib'
   } else {
     implementation 'url_to_remote_repository'
  }
}
```

> _⚠️ Avertissement : Vous ne devriez jamais commiter le fichier gradle.properties lorsque vous travaillez localement._

Le voyage a été long et a peut-être semblé assez épuisant. Mais maintenant nous avons une configuration à toute épreuve pour travailler localement et à distance sur un projet multi-bibliothèques.

Si vous rencontrez des problèmes ou si vous souhaitez donner votre avis sur ce sujet, n'hésitez pas à laisser un commentaire.