---
title: Comment utiliser les variables dans Figma – Un guide pour débutants
subtitle: ''
author: Faith Olohijere
co_authors: []
series: null
date: '2023-12-15T22:11:10.000Z'
originalURL: https://freecodecamp.org/news/variables-in-figma-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/How-to-Use-Variables-in-Figma-cover--1-.png
tags:
- name: Design
  slug: design
- name: figma
  slug: figma
- name: handbook
  slug: handbook
- name: Web Design
  slug: web-design
seo_title: Comment utiliser les variables dans Figma – Un guide pour débutants
seo_desc: "At Figma Config 2023, the Figma team unveiled a lot of new features – including\
  \ variables. The launch of variables in Figma offers designers a new approach that\
  \ helps them make their designs more flexible and adaptable. \nIn this tutorial,\
  \ you'll lear..."
---

Lors de la Figma Config 2023, l'équipe Figma a dévoilé de nombreuses nouvelles fonctionnalités, y compris les variables. Le lancement des variables dans Figma offre aux designers une nouvelle approche qui les aide à rendre leurs designs plus flexibles et adaptables.

Dans ce tutoriel, vous apprendrez ce que sont les variables dans Figma, et comment créer et implémenter différents types de variables lors de la conception dans Figma.

## Prérequis :

Pour tirer le meilleur parti de ce guide, il sera utile d'avoir des connaissances de base sur l'utilisation de Figma et de ses fonctionnalités. Mais notez que cela n'est pas nécessaire, car j'ai écrit ce guide pour tout le monde, indépendamment de leur niveau de connaissance individuel.

Ce guide est destiné à tous ceux qui souhaitent en savoir plus sur les variables, Figma et le design en général.

## Table des matières :

- [Qu'est-ce que les variables ?](#heading-quest-ce-que-les-variables)
- [Différences entre les variables et les styles dans Figma](#heading-differences-entre-les-variables-et-les-styles-dans-figma)
- [Pourquoi les variables sont-elles importantes pour le processus de design ?](#heading-pourquoi-les-variables-sont-elles-importantes-pour-le-processus-de-design)
- [Comment créer des variables dans Figma](#heading-comment-creer-des-variables-dans-figma)
    - [Comment créer des variables de couleur dans Figma](#heading-comment-creer-des-variables-de-couleur-dans-figma)
        - [Comment créer des variables de couleur pour les tokens](#heading-comment-creer-des-variables-de-couleur-pour-les-tokens)
        - [Comment implémenter des variables de couleur dans vos designs](#heading-comment-implementer-des-variables-de-couleur-dans-vos-designs)
        - [Comment créer différents modes avec des variables](#heading-comment-creer-differents-modes-avec-des-variables)
    - [Comment créer des variables numériques dans Figma](#heading-comment-creer-des-variables-numeriques-dans-figma)
    - [Comment créer des variables de chaîne dans Figma](#heading-comment-creer-des-variables-de-chaine-dans-figma)
    - [Comment créer des variables booléennes dans Figma](#heading-comment-creer-des-variables-booleennes-dans-figma)
- [Comment utiliser les variables pour le prototypage avancé](#heading-comment-utiliser-les-variables-pour-le-prototypage-avance)
   - [Prototypage avancé avec des variables numériques](#heading-prototypage-avance-avec-des-variables-numeriques)
   - [Prototypage avancé avec des variables booléennes](#heading-prototypage-avance-avec-des-variables-booleennes)
- [Comment utiliser les variables pour les développeurs - Utilisation des API](#heading-comment-utiliser-les-variables-pour-les-developpeurs-utilisation-des-api) 
- [Conclusion](#heading-conclusion)

# Qu'est-ce que les variables ?

Le mot « variable » a de nombreuses définitions. Le dictionnaire Oxford définit le mot variable comme « non constant ou n'ayant pas de motif fixe ; susceptible de changer. » Une autre définition dit « un élément, une caractéristique ou un facteur susceptible de varier ou de changer. »

Les définitions ci-dessus nous disent simplement que les variables sont des éléments dynamiques et sujets à changement. Avec ces définitions, nous pouvons maintenant définir ce qu'est une variable dans Figma.

Dans Figma, une variable stocke des valeurs réutilisables comme les couleurs et les valeurs de texte que vous pouvez appliquer à différentes propriétés de design et prototypes.

## Différences entre les variables et les styles dans Figma

Étant donné la définition des variables ci-dessus, vous avez peut-être commencé à voir certaines similitudes entre les variables et les guides de style. Bien que les deux fonctionnalités existent pour améliorer votre travail, il y a quelques différences clés à garder à l'esprit :

* Les variables sont une fonctionnalité plus avancée, et elles vous permettent de définir et de réutiliser des valeurs comme les couleurs, le texte et l'espacement dans vos designs. D'autre part, les styles sont des ensembles prédéfinis de propriétés de design telles que les styles de texte, les styles de couleur et les styles d'effet.
* Les variables permettent aux designs de changer lorsqu'elles sont utilisées dans divers contextes, en raison de leur nature dynamique, contrairement aux styles. Par exemple, vous pouvez changer vos designs du mode clair au mode sombre ou avoir des valeurs de remplissage qui changent lors de la conception pour différents appareils. Cela rend les variables utiles pour créer des systèmes de design avec des composants adaptables.
* Les variables offrent un processus de design plus flexible dans la création de composants de design flexibles, surtout lorsque vous souhaitez changer des valeurs comme le texte ou la couleur des boutons sur différentes instances du même composant. Les styles sont généralement utilisés pour maintenir des éléments de design cohérents comme les styles de boutons, les titres de texte ou les palettes de couleurs.
* Les variables peuvent stocker des valeurs brutes et uniques, tandis que les styles stockent des ensembles de valeurs.

## Pourquoi les variables sont-elles importantes pour le processus de design ?

L'utilisation des variables est assez importante pour un certain nombre de raisons.

Premièrement, les variables aident à maintenir la **cohérence** dans un système de design. En définissant des variables pour les couleurs, la typographie, l'espacement et d'autres éléments de design, vous garantissez que ces éléments ont une apparence uniforme dans tout votre projet. Cette cohérence est cruciale pour le branding et l'expérience utilisateur.

Les variables rendent également les designs **adaptables**. Les designers peuvent rapidement expérimenter avec différentes valeurs telles que les schémas de couleurs ou les tailles de police en ajustant les variables. Cette adaptabilité est précieuse lors de la création de designs pour différentes plateformes ou appareils.

Les variables sont également assez **efficaces**. Lorsqu'une variable est mise à jour, toutes les instances de cette variable dans le design sont mises à jour automatiquement. Cela permet de gagner du temps et des efforts, et élimine le besoin de mettre à jour manuellement chaque instance d'un élément spécifique.

Les variables sont particulièrement utiles dans les grands projets ou les systèmes de design en raison de leur **évolutivité** et de leur **facilité de maintenance**. Elles permettent aux designers de faire évoluer leurs designs sans perdre le contrôle.

Puisque les projets évoluent et que les systèmes de design se développent au fil du temps, les variables peuvent être ajustées globalement pour répondre à de nouvelles exigences. Les variables fournissent également un endroit central pour mettre à jour ces changements, garantissant que tous les éléments de design sont modifiés de manière cohérente.

Et enfin, les variables peuvent être bénéfiques pour les développeurs lors du **processus de transfert**. Les designers peuvent fournir aux développeurs des valeurs précises pour les éléments de design, réduisant ainsi les risques de mauvaise interprétation et simplifiant le processus de mise en œuvre.

# Comment créer des variables dans Figma

Les variables sont assez faciles à créer dans Figma. Ci-dessous, je vais vous guider à travers les étapes pour créer différents types de variables dans Figma.

Pour l'instant, nous avons quatre types de variables dans Figma :

* Couleur : utilisée pour les remplissages de couleur.
* Nombre : utilisée pour les dimensions, le rayon des coins et les propriétés de disposition automatique.
* Chaîne : utilisée pour les calques de texte et les propriétés de variante.
* Booléen : utilisée pour basculer la visibilité des calques.

Nous allons créer et implémenter chacune de ces variables dans Figma, et les utiliser également pour le prototypage avancé.

## Comment créer des variables de couleur dans Figma

Le premier type de variable que nous allons créer est une variable de couleur. En tant que designer ou développeur, vous avez probablement utilisé des couleurs dans vos projets. Ainsi, le concept de couleur ne devrait pas vous être étranger d'un point de vue design.

### Étape 1 : Ouvrir un nouveau fichier Figma

Supposons que vous souhaitez créer des variables de couleur pour un nouveau projet de design sur lequel vous allez commencer à travailler, comme un site web de magazine par exemple. La première chose que vous devez faire est d'ouvrir un nouveau fichier Figma.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Variable-1.png)
_Fichier Figma vierge_

### Étape 2 : Choisir une palette de couleurs

L'étape suivante consiste à choisir une palette de couleurs pour le projet. Chaque projet de design a un ensemble de couleurs utilisées de manière répétée pour établir la cohérence – par exemple, pour les en-têtes et les arrière-plans, pour attirer l'attention sur un bouton principal, et ainsi de suite.

Vous voudrez choisir des couleurs qui se complètent pour votre design. Si vous avez besoin d'aide ici, vous pouvez lire mon article sur la [règle 60-30-10 en design](https://www.freecodecamp.org/news/the-60-30-10-rule-in-design/).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Variable-3.png)
_Création d'une palette de couleurs_

### Étape 3 : Créer des variables pour chaque couleur

Ensuite, nous allons créer des variables pour chaque code de couleur de la palette. Allez dans le panneau sur le côté droit et cliquez sur _variables locales_.

Les variables locales signifient toutes les variables situées dans le fichier de design.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-4.png)
_Cliquez sur les variables locales_

Cliquez sur _créer une variable_ pour créer la première variable dans le fichier.

Une liste déroulante apparaîtra contenant les quatre types de variables que j'ai expliqués précédemment. Puisque nous essayons de créer des variables de couleur dans cette section, nous choisirons _couleur_.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-5.png)
_Créer une variable de couleur_

Une section de variable créée apparaîtra, avec deux colonnes : le titre de la variable (_Couleur_), et la valeur de la variable (le code couleur-FFFFFF).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Variable-6.png)
_Choisir des variables de couleur_

Donnez un nom à votre nouvelle variable – vous pouvez utiliser le rôle de la couleur, par exemple, arrière-plan principal. Dans la colonne suivante, tapez le code couleur ou utilisez un sélecteur de couleur.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-7.png)
_Renommer la variable et taper le code couleur_

Et voilà – vous venez de créer votre première variable de couleur !

Pour voir plus d'options d'édition, survolez la ligne de la variable. Une icône _modifier la variable_ apparaîtra.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-141.png)
_Modifier la variable_

Cliquez dessus pour modifier la variable de couleur à votre goût.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-8.png)
_Modifier la variable de couleur/ajouter une description_

Dans la section d'édition, vous pouvez ajouter une description sur la façon d'utiliser la variable, la masquer de la publication, et ainsi de suite.

Ayant fait cela, suivez les étapes ci-dessus pour créer des variables pour les couleurs restantes de la palette de couleurs.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-10.png)
_Créer des variables pour d'autres couleurs_

Vous pouvez également organiser vos variables en groupes. Pour ce faire, sélectionnez les variables de couleur que vous souhaitez regrouper (maintenez la touche SHIFT enfoncée), et faites un clic droit.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-11.png)
_Grouper les variables de couleur_

Cela fera apparaître quelques options :

* Nouveau groupe avec sélection
* Modifier les variables
* Dupliquer les variables
* Supprimer les variables

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-12.png)
_Nouveau groupe avec sélection_

Choisissez _Nouveau groupe avec sélection_, double-cliquez sur le nom du groupe, et renommez-le en _couleur/bleu_.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-14-1.png)
_Renommer le groupe_

Vous pouvez regrouper vos variables de couleur comme vous le souhaitez – par exemple, couleurs d'arrière-plan, couleurs d'en-tête, différentes nuances d'une couleur particulière, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-15.png)
_Variables de couleur bleue regroupées._

Violà ! Vous venez de créer un groupe de variables de couleur dans Figma. Cliquez sur la liste déroulante de la collection et choisissez _renommer la collection_.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-16.png)
_Renommer la collection_

Vous pouvez renommer cette collection _primitives_.

_Primitives_ signifie basique. Vous pouvez également décider de renommer vos collections ou non. Le choix vous appartient.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-39.png)
_Collection primitives renommée_

### Comment créer des variables de couleur pour les tokens

Maintenant, nous allons créer des variables de couleur pour le texte, les surfaces (comme les arrière-plans) et les bordures dont nous avons besoin pour le projet. Nous voulons attribuer différentes fonctions à la palette de couleurs (variables) que nous avons créée précédemment.

Cliquez sur les variables locales et créez une nouvelle collection. Vous pouvez la nommer _tokens_.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-21.png)
_Nouvelle collection_

Créez une nouvelle variable de couleur et renommez-la "texte principal".

Pour gagner du temps et regrouper vos variables au fur et à mesure que vous les nommez, renommez la variable en _texte/principal_. Cela formera automatiquement un groupe.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-24.png)
_Création et regroupement des variables de texte_

Cliquez sur la boîte de remplissage et allez dans _Bibliothèques_ pour voir toutes les variables de couleur créées.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-26.png)
_Attribution de couleur à partir des bibliothèques_

Nous choisirons _Noir Principal_ qui se trouve sous _couleur/gris_.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-27.png)
_Choix de la couleur noire_

Nous pouvons continuer et attribuer d'autres variables de couleur pour différentes fonctions de texte, autant que nous le souhaitons. N'oubliez pas d'ajouter _texte/_ avant le nom réel de la variable, afin qu'elle forme automatiquement un groupe.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-28.png)
_Attribution de variables de couleur pour le texte_

Ensuite, nous allons créer des variables de couleur pour les surfaces telles que les arrière-plans, et pour les bordures également.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-29.png)
_Variables de couleur pour les surfaces et les bordures_

Certaines des variables de couleur peuvent avoir le même code couleur, mais elles ont des fonctions différentes, donc c'est tout à fait normal. Par exemple, le code couleur pour le texte du bouton est le même que le code couleur pour l'arrière-plan principal.

### Comment implémenter des variables de couleur dans vos designs

Ensuite, nous allons implémenter ces variables de couleur dans notre design.

Dans l'image ci-dessous, il y a quatre maquettes mobiles sans couleur ni images (je les ai créées précédemment).

Vous pouvez lire comment créer des maquettes dans cet article : [Qu'est-ce que le wireframing ? Comment passer des croquis papier aux maquettes haute fidélité](https://www.freecodecamp.org/news/what-is-wireframing/).

Nous allons utiliser les variables de couleur que nous avons créées pour ajouter de la couleur aux boutons et au texte, en veillant à ce que tous les éléments soient cohérents.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-30.png)
_Maquettes basse fidélité_

En commençant par le premier écran, ajoutons de la couleur au bouton. Cliquez sur le bouton, et allez dans _Remplissage_ sur le côté droit de votre écran.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-32-1.png)
_Cliquez sur le bouton_

Dans la section _Remplissage_, cliquez sur _style_ (l'icône à quatre points sur le côté). La sélection de _style_ fera apparaître une liste de couleurs dans vos bibliothèques. Sélectionnez la couleur que vous avez attribuée pour le bouton principal afin de l'implémenter.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-33-1.png)
_Sélectionnez une couleur de remplissage parmi les variables de couleur dans les bibliothèques_

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-34-1.png)
_Couleur de bouton implémentée_

Ensuite, donnez au texte du bouton une couleur blanche en suivant les mêmes étapes.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-35-3.png)
_Implémentation de la variable de couleur pour le texte du bouton_

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-36-1.png)
_Couleur de texte de bouton implémentée_

Vous pouvez continuer et faire de même pour les autres écrans, en suivant les étapes ci-dessus. N'oubliez pas de mettre à jour le texte et les couleurs également.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-37-1.png)
_Mise à jour des variables de couleur pour les autres écrans_

Vous pouvez également ajouter des images ou des illustrations pour compléter l'apparence.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/variable-38-1.png)
_Ajout d'illustrations au design mis à jour_

Remarque : Vous pouvez obtenir vos illustrations à partir de plugins dans Figma comme Storyset by Freepik, Artify Illustrations, et ainsi de suite, ainsi qu'à partir de bibliothèques d'illustrations comme [Freepik](https://www.freepik.com/), [Lapa Ninja](https://www.lapa.ninja/blog/free-illustrations-library-for-your-project/), et d'autres.

### Comment créer différents modes avec des variables

Ensuite, nous allons créer différents modes pour notre design. Par exemple, si vous travaillez sur un projet qui nécessite des modes clair et sombre, au lieu de changer manuellement tous les éléments de design pour accommoder les modes, vous pouvez simplement utiliser des variables pour implémenter cela.

Pour commencer, cliquez sur _Variables locales_ pour créer une nouvelle variable. Une liste de toutes les variables dans le fichier et leurs groupes apparaîtra :

couleur/bleu :

* Bouton Principal
* Bleu Principal

couleur/gris :

* Noir Principal
* Arrière-plan Principal

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-142.png)
_Ouvrir "Variables locales"_

Ensuite, je vais créer une nouvelle collection afin de me concentrer uniquement sur les modes que je suis sur le point de créer. Pour créer une nouvelle collection, cliquez simplement sur l'icône de menu dans l'en-tête des variables.

Notez que la création d'une nouvelle collection n'est pas obligatoire. C'est juste pour vous aider à vous concentrer sur d'autres variables que vous avez déjà créées.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-143.png)
_Création d'une nouvelle collection_

Ensuite, je vais renommer la collection en _Modes_. Pour renommer une collection, double-cliquez simplement sur le titre et entrez votre titre préféré.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-144.png)
_Renommer une collection_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-145.png)
_Collection renommée "Modes"_

Ensuite, cliquez sur _Créer une variable_ pour créer une nouvelle variable. Je vais choisir _Couleur_ car c'est la variable avec laquelle nous travaillons.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-146.png)
_Création d'une variable appelée Couleur_

La variable de couleur créée apparaîtra avec un code couleur par défaut : FFFFFF.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-147.png)
_Variable de couleur créée avec le code couleur par défaut : FFFFFF_

Ensuite, je vais renommer la variable _Arrière-plan_ car j'essaie de définir les couleurs d'arrière-plan pour chaque mode (clair et sombre).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-148.png)
_Variable de couleur renommée : Arrière-plan_

Maintenant, nous avons travaillé uniquement avec le nom et la valeur des variables que nous avons créées, mais nous pouvons ajouter une autre colonne lorsque nous voulons créer des modes. Pour ce faire, cliquez simplement sur l'icône plus dans l'en-tête pour ajouter un nouveau mode de variable.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-149.png)
_Cliquer sur l'icône plus_

Le nouveau mode comportera trois colonnes :

* Colonne 1 (le titre de la variable – Arrière-plan)
* Mode 1 (la première valeur de la variable – code couleur FFFFFF)
* Mode 2 (la première valeur de la variable – code couleur FFFFFF)

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-150.png)
_Nouveau mode créé_

Ensuite, je vais renommer les modes en clair et sombre. Pour ce faire, double-cliquez simplement sur le titre et modifiez le nom.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-151.png)
_Modes renommés : Clair et Sombre_

Maintenant, nous allons attribuer une valeur à l'arrière-plan pour le mode sombre. Pour ce faire, entrez simplement le code/valeur de couleur que vous préférez pour l'arrière-plan. J'utiliserai #0C3272 comme couleur d'arrière-plan pour le mode sombre.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-152.png)
_Valeur modifiée pour l'arrière-plan du mode sombre_

Ensuite, nous allons créer d'autres variables de couleur pour d'autres éléments comme le texte, la couleur du bouton, la couleur du texte du bouton, et ainsi de suite pour les deux modes. Je vais lister les spécifications pour faciliter les choses :

**Clair/Sombre :**

* Texte du corps : 1A1A1A/FFFFFF
* Bouton : 0C3272/FFFFFF
* Texte du bouton : FFFFFF/0C3272
* En-tête de l'iPhone : 1A1A1A/FFFFFF

Ensuite, nous allons créer les variables. Suivez simplement les étapes que nous avons suivies précédemment pour créer les variables et attribuer des valeurs pour chacun des modes.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-154.png)
_Variables créées pour d'autres éléments_

Ensuite, nous nous assurons que le design est connecté aux variables que nous avons créées. Pour ce faire, maintenez simplement l'élément et utilisez _Remplissage_ pour le lier à la variable de couleur.

Pour le texte du bouton par exemple, sélectionnez le texte et cliquez sur l'icône de style dans _Remplissage_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-155.png)
_Cliquer sur l'icône de style dans la section "Remplissage"_

Ensuite, faites défiler la liste qui apparaît jusqu'à la variable spécifique à laquelle vous souhaitez lier la variable (dans ce cas, Texte du corps).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-156.png)
_Sélection de la variable Texte du corps._

Faites de même pour les autres éléments du design, y compris l'arrière-plan.

Notez que je vais laisser les illustrations telles qu'elles sont.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-157.png)
_Écrans connectés aux modes de variable._

Pour vérifier si les modes fonctionnent réellement, cliquez sur l'icône _changer de mode de variable_ dans la section _Calque_ sur le panneau droit de votre écran.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-158.png)
_Cliquer sur l'icône "changer de mode de variable"_

Une liste de tous les modes (Clair et Sombre) apparaîtra et vous pourrez basculer l'écran vers le mode de votre choix.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-159.png)
_Changement de modes_

Une section nommée _Modes_ apparaîtra dans la section _Calque_, indiquant que l'un des écrans est en mode sombre.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-160.png)
_Un écran en mode sombre et un en mode clair._

## Comment créer des variables numériques dans Figma

Ensuite, je vais vous montrer comment créer des variables numériques dans Figma.

Les variables numériques sont définies par des valeurs numériques, et elles peuvent être appliquées au rayon des coins, au remplissage de la largeur ou de la hauteur, et ainsi de suite. Voici les étapes à suivre pour créer les vôtres :

### Étape 1 : Choisir une variable

Tout comme nous l'avons fait lors de la création de variables de couleur, cliquez sur le panneau des variables locales pour sélectionner le type de variable que vous essayez de créer. Ici, vous sélectionnerez _nombre_.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/variable-40.png)
_Choisir une variable à créer_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Variable-41.png)
_Sélection de "nombre"_

Lorsque vous sélectionnez _nombre_, il apparaît dans la liste des variables avec une valeur, dans ce cas 0.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-43.png)
_Variable numérique montrant Nombre avec une valeur par défaut de 0_

Maintenant, vous pouvez renommer la variable numérique comme vous le souhaitez. Pour renommer la variable, double-cliquez sur _nombre_, et changez-le en n'importe quel nom que vous voulez.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-44.png)
_Renommer la variable numérique_

Je vais renommer la mienne en _OrderCount_, car j'essaie d'implémenter une fonction qui permet à un utilisateur d'augmenter le nombre de portions de nourriture qu'il essaie de commander.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-45.png)
_Variable numérique renommée_

Ensuite, nous allons définir la valeur numérique par défaut à _1_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-46.png)
_Définit la valeur numérique par défaut_

Maintenant, nous allons lier le nombre dans le design à la variable numérique (_OrderCount_). Pour ce faire, cliquez sur le nombre dans le design.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-47.png)
_Implémentation de la variable numérique_

Ensuite, allez dans _Texte_ sur le côté gauche de votre écran. Cliquez sur l'icône _Appliquer la variable_ pour appliquer la variable.

Remarque : L'icône _appliquer la variable_ n'apparaîtra dans la section _Texte_ que lorsqu'une variable aura été créée.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-49.png)
_Cliquer sur l'icône "appliquer la variable"_

En cliquant sur l'icône, une liste de toutes les variables numériques disponibles dans le fichier apparaîtra. Ensuite, vous sélectionnerez la variable que vous essayez d'implémenter. Je vais choisir _OrderCount_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-50.png)
_Sélection d'une variable numérique_

Lorsque la variable aura été implémentée (liée au nombre), elle apparaîtra dans la section de texte, indiquant qu'une variable numérique a été implémentée.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-51.png)
_Variable numérique implémentée_

Maintenant, nous aurons également besoin de deux autres variables numériques pour les autres valeurs numériques dans le design (coût de la nourriture et coût total). Cela permet à ces valeurs de changer également lorsqu'un utilisateur augmente le nombre de portions qu'il commande.

Nous n'inclurons pas les frais de livraison, car ils restent les mêmes quelle que soit le nombre de portions qu'un utilisateur commande.

Ensuite, nous allons suivre le même processus que précédemment pour créer des variables numériques pour celles-ci.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-52.png)
_Création d'autres variables numériques_

Ensuite, nous allons lier les nombres dans le design à leurs variables numériques respectives, comme nous l'avons également fait précédemment.

Remarque : Dans le design principal, j'ai donné au nombre réel (25) un cadre différent du signe dollar (qui est en texte). Cela est dû au fait que lors de la création de la variable numérique, le signe dollar ne sera pas attaché, car c'est un mot, pas un nombre.

Par conséquent, lorsque je lie la variable numérique au design, je l'appliquerai au cadre contenant le nombre seul.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-53.png)
_Donner au nombre un cadre différent du signe dollar_

Ainsi, lorsque j'ai lié le premier nombre à la variable numérique que j'ai créée (Coût-Portion), quelque chose d'intéressant s'est produit. Le nombre dans le design a pris la valeur de la variable. Au lieu de 25,00 qui était sur l'écran précédemment, il est passé à 25 car c'est ce que la variable numérique était définie.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-55.png)
_La variable numérique change le nombre dans le design_

Maintenant, pour éviter tout désagrément, je vais changer les valeurs des autres nombres et les réaligner.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-56.png)
_Valeurs numériques modifiées et réalignées dans le design_

Nous venons de créer des variables numériques pour notre design. Dans la section de prototypage avancé, nous vérifierons si ces variables numériques fonctionnent réellement.

## Comment créer des variables de chaîne dans Figma

Ensuite, vous apprendrez à créer des variables de chaîne dans Figma.

Comme je l'ai écrit précédemment, les variables de chaîne sont utilisées pour les calques de texte et les propriétés de variante. Avec les variables de chaîne, vous pouvez changer les titres dans votre design, inverser le texte sur différents écrans, changer les modes de langue, et ainsi de suite.

Pour cet article, nous utiliserons des variables de chaîne pour changer les titres sur les écrans pour chaque mode que nous avons créé précédemment (clair et sombre).

Comme d'habitude, notre première étape consiste à cliquer sur _Variables locales_ et à sélectionner le type de variable que nous voulons créer.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-161.png)
_Aller aux variables locales pour créer une nouvelle variable_

Je vais choisir _Chaîne_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-163.png)
_Choisir "Chaîne" parmi une liste de toutes les variables_

Lorsque je fais cela, la variable de chaîne que je viens de créer apparaîtra dans la liste des variables.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-164.png)
_Variable de chaîne créée_

Si vous l'avez remarqué, la variable de chaîne a deux colonnes pour "valeur de chaîne", car j'ai créé la variable dans la collection _Modes_. Suite à cela, voyons si nous pouvons changer les titres pour chaque mode.

Remarque : La valeur de chaîne est le texte réel que vous essayez de changer.

Ainsi, pour le premier écran dont le titre est "Transactions Made Easy", je veux qu'il change en "Easy Transactions, Less Stress" pour le mode sombre. Pour le deuxième écran dont le titre est "Pay Bills with Ease", je veux qu'il change en "Paid Bills, Easier Life" pour le mode sombre.

Puisque nous changeons les titres pour deux écrans différents, nous allons créer une autre variable de chaîne.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-165-1.png)
_Création d'une autre variable de chaîne_

Ensuite, nous allons entrer les différentes valeurs pour les différents modes. Pour ce faire, entrez simplement les différents textes pour les deux écrans dans les deux modes.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-166-1.png)
_Entrée de la valeur de chaîne_

Ensuite, nous allons lier les titres aux variables de chaîne que nous venons de créer. Pour ce faire, cliquez sur le titre particulier et allez à l'icône _Appliquer la variable_ dans la section _Texte_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-167-3.png)
_Application de la variable de chaîne_

Ensuite, faites défiler vers le bas et choisissez la chaîne à laquelle vous l'appliquez.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-168-1.png)
_Choix de la variable de chaîne_

Une fois que vous avez terminé, une icône de chaîne apparaîtra, indiquant qu'une variable de chaîne a été appliquée au texte.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-169-1.png)
_Variable de chaîne appliquée_

Faites de même pour la deuxième chaîne :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-170-1.png)
_Application de la variable de chaîne au deuxième écran_

Ensuite, testons pour voir si la variable de chaîne fonctionne. Sélectionnez les écrans qui ont la variable appliquée, allez dans _Calques_, et changez le mode de clair à sombre.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-171-1.png)
_Sélection des écrans qui ont les variables appliquées_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-172-1.png)
_Sélection du mode sombre_

Le mien fonctionne :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-173-1.png)
_Écrans changés en mode sombre_

## Comment créer des variables booléennes dans Figma

Ensuite, nous allons apprendre à créer des variables booléennes.

Généralement, les variables booléennes sont des variables qui ne peuvent avoir que deux valeurs possibles – vrai ou faux. Dans Figma, les variables booléennes ont la même fonction : elles sont utilisées pour les propriétés de variante ou les composants avec deux valeurs : vrai ou faux.

Vous vous souvenez du basculeur dans le design ci-dessus ?

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-110.png)
_Basculeur dans le design utilisé pour implémenter les variables numériques_

Je vais le changer en une case à cocher et utiliser des variables booléennes pour le faire fonctionner.

Pour ce faire, je vais copier le composant et le coller sur un autre cadre. Je vais ensuite ajouter la case à cocher (et la remplacer dans l'écran de design principal plus tard).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-111.png)
_Case à cocher sur un cadre vide._

Ensuite, nous allons faire de la sélection une variante. Pour ce faire, double-cliquez sur l'icône _Créer un composant_ dans l'en-tête de votre fichier Figma.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-113.png)
_Double-cliquez sur l'icône "créer un composant"_

Une variante apparaîtra automatiquement :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-114.png)
_Variante du composant_

Ensuite, je vais créer différents états pour les cases à cocher : par défaut, survol et rempli.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-116.png)
_Différents états pour les cases à cocher : Par défaut, survol et rempli._

Maintenant, nous allons créer la variable booléenne.

Pour ce faire, allez dans _Variables locales_ comme d'habitude et sélectionnez _Booléen_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-118.png)
_Ouvrir les variables locales_

Cliquez sur _Créer une variable_.

Ensuite, nous allons choisir _Booléen_ dans la liste.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-117.png)
_Choisir "booléen" dans la liste_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-119.png)
_Variable booléenne créée_

Ensuite, nous allons renommer la variable booléenne _SaveFood_ puisque nous essayons de créer une fonction pour enregistrer un choix de nourriture pour les commandes ultérieures.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-120.png)
_Variable booléenne renommée_

Ensuite, nous allons rendre la variable _True_ par défaut. Pour ce faire, cliquez simplement sur l'icône de bascule à côté de la variable.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-121.png)

Vous avez créé une variable booléenne !

Nous allons créer une interaction pour cette variable booléenne dans la section de prototypage avancé et vérifier si elle fonctionne.

## Comment utiliser les variables pour le prototypage avancé

Dans cette section, nous allons apprendre à utiliser les variables pour le prototypage avancé dans Figma, en utilisant les variables de couleur, de nombre, de chaîne et booléennes que nous avons implémentées précédemment dans le design.

N.B : Vous ne pouvez utiliser les fonctionnalités de prototypage avancé sur Figma que si votre fichier est sur un fichier d'équipe payant. Si vous n'avez pas de version d'équipe payante, vous pouvez demander le plan _[Figma pour l'éducation](https://www.figma.com/education/)_. C'est une façon pour Figma d'aider les apprenants et les éducateurs en leur donnant accès à des ressources, et à tous les avantages d'une version payante, gratuitement.

Vous pouvez utiliser le prototypage avancé lorsque vous avez beaucoup d'écrans à travailler, et pour simplifier le prototypage.

### Prototypage avancé avec des variables numériques

En commençant par les variables numériques que nous avons créées ci-dessus, essayons de vérifier si elles fonctionnent réellement. Mais avant de faire cela, nous devons réellement prototyper le design.

Notez que vous pouvez prototyper des variables numériques pour des designs où votre utilisateur peut augmenter ou diminuer le nombre d'un élément à l'écran. Le prototypage aide à montrer la fonctionnalité et comment cette fonctionnalité particulière fonctionnerait.

Pour commencer, je vais faire du cadre où se trouve le compteur de commandes un composant. Pour ce faire, sélectionnez le cadre et cliquez sur l'icône de composant dans l'en-tête de votre fichier Figma.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-57.png)
_Sélection du cadre du compteur de commandes_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-58.png)
_Cliquer sur l'icône de composant_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-59.png)
_Le composant du compteur de commandes_

Cliquez à nouveau sur l'icône de composant pour en faire une variante.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-60.png)
_Faire du composant du compteur de commandes une variante_

Je vais créer un cadre en dehors de l'écran et y glisser la variante, afin de pouvoir bien travailler sur les interactions.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-61.png)
_Création d'un cadre en dehors de l'écran_

Rappelez-vous que nous voulons implémenter une fonction où le nombre de portions augmente lorsque l'utilisateur clique sur l'icône plus.

Nous allons commencer le prototypage à partir d'ici.

Maintenant, cliquez sur l'icône plus dans la variante par défaut et passez à l'onglet prototype.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-62.png)
_Cliquer sur l'icône plus dans la variante par défaut_

Ensuite, cliquez sur l'icône plus dans la zone des interactions pour ajouter une interaction.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-63.png)
_Ajout d'une interaction_

Un onglet apparaîtra montrant les interactions. Dans ce cas, il est défini par défaut sur _On click_, et aucune interaction n'a encore été ajoutée (None).

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-64.png)
_Ajout d'une interaction_

Maintenant, cliquez sur l'icône de la liste déroulante qui dit _None_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-65.png)
_Cliquer sur l'icône de la liste déroulante_

Cela fera apparaître une liste :

* Naviguer vers
* Changer pour
* Retour
* Définir la variable
* Conditionnel
* Faire défiler vers
* Ouvrir le lien
* Ouvrir le calque
* Échanger le calque
* Fermer le calque

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-66.png)
_Liste suivant la liste déroulante_

Choisissez _Définir la variable_.

Une liste de toutes les variables dans le fichier apparaîtra, et vous pourrez alors sélectionner la variable particulière que vous souhaitez implémenter. Je vais cliquer sur _OrderCount_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-67.png)
_Choisir "définir la variable"_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-68.png)
_Cliquer sur Order Count (la première fois)_

Ensuite, je vais cliquer à nouveau sur _OrderCount_ pour écrire une expression mathématique, et toutes les expressions mathématiques disponibles apparaîtront :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-69.png)
_Cliquer sur Order Count (la deuxième fois) et montrer toutes les expressions mathématiques_

Je vais sélectionner _Addition_, car c'est ce que nous essayons de faire.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-70.png)
_Choisir l'expression "addition"_

Vous remarquerez qu'une icône d'addition est apparue pour signifier que l'expression d'addition a été donnée.

Ensuite, je vais entrer _1_ à côté de l'icône d'addition pour montrer que c'est plus 1.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-71.png)
_Ajout du nombre 1 à l'expression_

Terminé !

Maintenant, nous allons suivre les mêmes étapes pour faire de même pour l'icône moins, en faisant de l'expression une soustraction au lieu d'une addition.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-72.png)
_Interactions ajoutées pour l'icône moins_

Terminé !

Remarque : Nous n'avons pas vraiment besoin de la variante que nous avons créée précédemment. Vous pourriez n'utiliser la variante que dans les cas où vous souhaitez créer un état de survol. Je voulais simplement vous montrer à quel point il serait facile de créer une variante en faisant cela.

Ensuite, nous allons simplement copier le composant prototypé et le remettre dans le design principal.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-73.png)
_Cadre contenant la variable prototypée_

Pour mettre le composant prototypé dans le design principal, cliquez sur _Assets_ en haut du panneau de gauche.

Cette section affichera tous les actifs de la page sur laquelle vous vous trouvez actuellement.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-74.png)
_Affichage de tous les actifs de la page_

Ensuite, je vais glisser le cadre vers le design.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-75.png)
_Actif glissé vers le design principal_

Remarque : Si vous ne souhaitez pas suivre le processus ci-dessus pour placer le composant prototypé dans le design, copiez simplement le composant (CTRL + C) et _collez pour remplacer_ le cadre sur le design principal.

Maintenant, vérifions notre prototype. Pour ce faire, vous n'avez pas besoin d'ouvrir le prototype dans un autre onglet. Vous pouvez simplement cliquer sur l'actif et appuyer sur SHIFT + barre d'espace.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-76.png)
_Actif cliqué_

Un autre cadre apparaîtra sur votre écran. Il est interactif et vous pouvez tester votre prototype dessus.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-77.png)
_Cadre interactif sur votre écran Figma._

Essayez de cliquer sur les icônes moins et plus sur le cadre pour voir si elles remplissent leur fonction.

Après avoir vérifié le prototype, j'aimerais implémenter une logique.

Nous ne voulons pas d'un scénario où le clic sur l'icône moins continue jusqu'à ce qu'elle donne un signe négatif comme -1 comme vous pouvez le voir dans l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-78.png)
_Icône moins nous donnant des valeurs négatives_

Cela n'aurait pas de sens, donc nous allons ajouter une _condition_.

Une condition est simplement une condition qui définit des règles sur la façon dont l'interaction doit fonctionner.

Pour ce faire, je vais me rendre au cadre contenant le composant que j'ai créé précédemment.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-79.png)
_Cadre contenant le composant prototypé_

Je vais ajouter la condition à l'icône moins puisque c'est la zone qui nous donnerait des valeurs négatives. Donc, je veux que les valeurs s'arrêtent à 1 puisque c'est le minimum qu'un utilisateur peut commander (ils ne peuvent pas commander la moitié ou 0, par exemple).

Donc, nous allons simplement zoomer sur le composant pour ajouter notre condition. Assurez-vous d'être également dans l'onglet prototype.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/variable-80.png)
_Passer à l'onglet prototype et zoomer sur le composant prototypé_

Je vais cliquer sur l'icône de variable à côté du cadre moins.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-81.png)
_Sélection de l'icône de variable proche du cadre de l'icône moins_

Cela fera apparaître les interactions déjà définies :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-82.png)
_Interactions déjà faites sur le cadre moins_

Ensuite, je vais cliquer sur l'icône plus à côté du 'x' dans l'en-tête des interactions.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-83.png)
_Cliquer sur l'icône plus dans l'en-tête de l'interaction_

Je vais choisir _conditionnel_ dans la liste des options qui apparaîtra :

* Naviguer vers
* Changer pour
* Retour
* Définir la variable
* Conditionnel
* Faire défiler vers
* Ouvrir le lien
* Ouvrir le calque
* Échanger le calque
* Fermer le calque

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-84.png)
_Choisir conditionnel dans la liste des options_

Nous allons ensuite écrire la condition. Pour ce faire, cliquez sur _Écrire une condition_ à côté de l'instruction _if else_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-86.png)
_Écrire une condition pour l'interaction_

Lorsque nous cliquons sur _Écrire une condition_, une liste de toutes les variables numériques apparaîtra. Je vais choisir _OrderCount_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-87.png)
_Sélection de ordercount_

Cela fera apparaître une liste de toutes les conditions disponibles :

* Égal à
* Différent de
* Supérieur à
* Supérieur ou égal à
* Inférieur à
* Inférieur ou égal à

Je vais choisir _Différent de_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-88.png)
_Choisir la condition "Différent de"_

Ensuite, l'icône de la condition que j'ai choisie apparaîtra dans le champ de saisie pour écrire la condition.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-89.png)
_Condition apparaissant dans le champ de saisie_

Ensuite, je vais entrer 0, ce qui signifie que l'interaction n'est pas égale à 0.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-90.png)
_Entrée de 0 (zéro)_

Ensuite, je vais fermer le cadre et essayer de déplacer la section _Définir la variable_ sous la section _conditionnelle_ dans l'interaction. Pour fermer la section Définir la variable, cliquez sur la petite icône de liste déroulante.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-91.png)
_Cliquer sur l'icône de liste déroulante pour fermer définir la variable_

Lorsque vous cliquez sur la petite icône de liste déroulante, la section _Définir la variable_ sera minimisée, vous permettant de déplacer la section sous la section _Conditionnelle_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-92.png)
_Section définir la variable fermée_

Ensuite, je vais glisser la section _définir la variable_ sous la section _conditionnelle_. Pour ce faire, survolez simplement la section _définir la variable_ et utilisez votre pavé tactile ou votre souris pour la glisser.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-93.png)
_Glisser définir la variable sous conditionnelle_

Nous venons d'ajouter une condition à notre interaction ! L'icône du cadre moins changera en une icône de condition, montrant qu'une condition a été ajoutée.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-94.png)
_Ajout d'une condition à l'interaction moins_

Maintenant, vous pouvez tester cette nouvelle interaction pour voir comment elle fonctionne.

La mienne fonctionne certainement ! Elle ne descend plus en dessous de 0.

### Comment implémenter la variable de coût par portion

Maintenant, nous voulons que les autres valeurs numériques (coût par portion et coût total) augmentent en réponse au nombre de portions qu'un utilisateur commande.

Nous allons commencer par le cadre de l'icône Plus :

En revenant au composant sur lequel nous avons travaillé...

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-95.png)
_Cadre avec le composant prototypé_

Je vais cliquer sur le cadre plus et passer à _définir la variable_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-96.png)
_Ouvrir les interactions pour le cadre plus_

Je vais cliquer sur l'icône plus dans l'en-tête des interactions.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-97.png)
_Cliquer sur l'icône plus dans l'en-tête des interactions_

Ensuite, je vais sélectionner _définir la variable_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-98.png)
_Sélection de définir la variable_

Une liste de toutes les variables qui ont été créées dans le fichier apparaîtra :

* Les variables de couleur pour le texte, les boutons, les titres, et ainsi de suite.
* Variables numériques – _OrderCount_, _Cost-Portion_, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-99.png)
_Une liste de toutes les variables dans le fichier_

Je vais faire défiler vers le bas pour choisir _cost-portion_, qui est le coût par portion de nourriture qu'un utilisateur commande.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-100.png)
_Choisir "Cost-portion" (la première fois)_

Un champ de saisie pour écrire une expression pour la variable apparaîtra.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-101.png)
_Champ de saisie pour écrire une expression_

Pour écrire une expression, cliquez à nouveau sur Cost-Portion et sélectionnez _Addition_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-102.png)
_Choisir cost-portion (la deuxième fois) et sélectionner addition_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-104.png)
_Icône d'addition apparaissant dans le champ de saisie_

Ensuite, je vais entrer 25, ce qui signifie que +25 doit être ajouté pour chaque portion de nourriture qu'un utilisateur commande.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-103.png)
_Entrée de 25_

Ayant ajouté l'interaction pour le cadre plus, nous allons suivre le même processus pour le cadre moins. Lorsque vous avez terminé, la section _Définir la variable_ doit être sous la section _Conditionnelle_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-105.png)
_Ajout d'interaction pour le cadre moins_

Rappelez-vous qu'il y a une condition pour le cadre moins, donc je vais simplement glisser la nouvelle interaction à l'intérieur de la condition.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-106.png)
_Glisser la nouvelle interaction "définir la variable" à l'intérieur de la conditionnelle ;_

Maintenant, essayez de tester la nouvelle interaction que vous venez d'ajouter. La mienne fonctionne certainement !

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-107.png)
_Test de la nouvelle interaction_

Ensuite, nous avons encore une dernière variable à ajouter (Coût Total).

Suivez les étapes ci-dessus pour recréer cette interaction. En commençant par le cadre plus, implémentez la variable pour vous assurer que 25 $ s'ajoute lorsque la commande augmente. Il devrait montrer un espace réservé – _Coût Total + 25_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-108.png)
_Implémentation de la variable Coût Total_

Maintenant, faites de même pour le cadre moins et testez l'interaction. N'oubliez pas d'ajouter la nouvelle interaction à l'intérieur de la condition.

La mienne fonctionne !

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-109.png)
_Test des interactions_

Vous venez d'apprendre à implémenter des variables numériques avec le prototypage avancé dans Figma. Félicitations !

### Prototypage avancé avec des variables booléennes

Ensuite, nous allons créer une interaction pour la variable booléenne que nous avons créée précédemment dans l'article.

Notez que vous pouvez prototyper vos variables booléennes dans des designs où vous avez des fonctionnalités comme des cases à cocher et des basculeurs. Le prototype montrerait comment la case à cocher est censée fonctionner.

Pour créer l'interaction, passez à l'onglet prototype et concentrez-vous sur le cadre contenant les composants booléens.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-122.png)
_Cadre contenant les composants booléens_

Maintenant, notre interaction principale commencerà partir de l'état de survol car c'est à ce moment-là qu'un utilisateur essaie de cliquer sur la case à cocher. Mais nous devons toujours ajouter une action qui amènera l'utilisateur de l'état par défaut à l'état de survol.

Pour ce faire, je vais simplement cliquer sur la première variante et la faire glisser vers la deuxième variante.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-132.png)
_Connexion de la première variante à la deuxième variante_

Je vais changer _On-click_ en _While Hovering_. Pour ce faire, cliquez simplement sur la liste déroulante _On-click_ et sélectionnez dans la liste qui apparaît :

* On click
* On drag
* While hovering
* While pressing
* Key/Gamepad
* Mouse enter
* Mouse leave
* Mouse down
* Mouse up
* After delay

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-133.png)
_Cliquer sur la liste déroulante on-click_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-134.png)
_Sélection de "while hovering" dans la liste_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-135.png)
_Sélectionné "while hovering"_

Je veux également changer _Instant_ en _Smart Animate_, donc je vais cliquer sur l'icône de liste déroulante à côté de _Instant_, et sélectionner dans la liste qui apparaît :

* Instant
* Dissolve
* Smart animate

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-136.png)
_Changer "Instant" en "Smart Animate"_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-137.png)
_À quoi ressemble l'interaction_

Donc, nous avons terminé la première interaction et nous allons commencer à connecter la deuxième variante à la troisième variante (Survol - Rempli).

Tout comme nous l'avons fait précédemment, nous allons simplement faire glisser la deuxième variante vers la troisième variante.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-124.png)
_Connexion de la deuxième à la troisième variante_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-125-1.png)
_À quoi ressemble l'interaction_

Comme je l'ai dit précédemment, l'interaction principale commence à partir de la deuxième variante, donc nous ne suivrons pas les mêmes étapes que nous avons prises pour ajouter la première interaction.

Pour continuer, je vais cliquer sur l'icône plus dans l'en-tête de l'interaction pour ajouter une action, et sélectionner _Définir la variable_ dans la liste qui apparaît :

* Naviguer vers
* Changer pour
* Retour
* Définir la variable
* Conditionnel
* Faire défiler vers
* Ouvrir le lien
* Ouvrir le calque
* Échanger le calque
* Fermer le calque

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-126.png)
_Cliquer sur l'icône plus dans l'interaction_

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-127.png)
_Choisir "définir la variable" dans la liste_

Ensuite, je vais cliquer sur _Sélectionner la variable cible_ pour sélectionner la variable booléenne.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-128.png)
_Cliquer sur "sélectionner la variable cible"_

Je vais faire défiler la liste des variables pour choisir la variable que je veux : SaveFood.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-129.png)
_Sélection de la variable "SaveFood"_

Maintenant, pour écrire l'expression pour cette variable, nous allons dire que la valeur sera égale à vrai. Donc, je vais sélectionner _Vrai_.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-130.png)
_Écrire l'expression et sélectionner "vrai"_

Ayant sélectionné _Vrai_, l'expression (_vrai_) ira sous la variable _SaveFood_, indiquant qu'une expression a été appliquée.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-131.png)
_À quoi ressemble l'interaction_

Ensuite, nous allons simplement copier le composant original et le coller dans notre design afin qu'il se synchronise lorsque nous vérifions le prototype.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-138.png)
_Coller le composant par défaut dans le design principal_

Pour vérifier le prototype directement sur votre page Figma, cliquez sur Shift + barre d'espace.

Le mien fonctionne !

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-139.png)

Mais j'ai remarqué quelque chose ; je ne peux pas décocher la case à cocher. Aucune interaction n'a été prévue pour cela. Maintenant, nous allons rapidement ajouter cette interaction pour que notre composant fonctionne parfaitement.

Pour ce faire, nous allons revenir à nos composants, en nous assurant d'être en mode prototype, et faire glisser la connexion de rempli jusqu'à par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Variable-140.png)
_Faire glisser la connexion de l'état rempli à l'état par défaut_

Maintenant, cela fonctionne parfaitement !

## Comment utiliser les variables pour les développeurs – Utilisation des API

Les variables sont très utiles pour les équipes composées de développeurs et/ou de designers.

> Les variables sont désormais prises en charge dans l'API de plugins de Figma – pour la création de plugins et de widgets – et dans l'API REST. Comme les variables sont actuellement en bêta ouverte, les fonctionnalités et les fonctions peuvent changer en réponse aux commentaires. – Documentation de Figma

Il existe trois documentations qui contiennent un support pour les variables pour les développeurs sur Figma :

* Pour l'[API REST](https://www.figma.com/developers/api#variables) :

> Cette API inclut des points de terminaison pour interroger, créer, mettre à jour et supprimer des variables. – Documentation de Figma

Pour pouvoir utiliser cette API, vous devez être membre d'une entreprise.

* Pour l'[API de plugins](https://www.figma.com/plugin-docs/working-with-variables/) :

> Cette API fournit un support pour la création et la lecture de variables, et la liaison de variables à des composants. – Documentation de Figma

* Pour l'[API de widgets](https://www.figma.com/widget-docs/working-with-variables/) : Cette API est connectée à l'API de plugins. Elle est disponible pour les widgets en utilisant l'API de plugins que le widget contient.

Les widgets sont des éléments interactifs qui peuvent être utilisés pour créer des prototypes interactifs. Les widgets étendent la fonctionnalité des fichiers de design et des tableaux FigJam et font souvent partie du système de design plus large, qui est une collection de composants réutilisables.

## Conclusion

Les variables existent dans Figma pour améliorer vos designs. Elles sont faciles à utiliser et à créer, et sont utiles dans chaque projet de design. Afin de gagner du temps, assurez-vous d'incorporer des variables dans votre processus de design.

La clé est de pratiquer et d'explorer, et vous vous améliorerez au fur et à mesure.

Merci d'avoir lu cet article, j'espère que vous l'avez apprécié !