---
title: Une brève introduction aux Web Components
subtitle: ''
author: Mark Mahoney
co_authors: []
series: null
date: '2025-05-08T15:32:15.694Z'
originalURL: https://freecodecamp.org/news/a-brief-introduction-to-web-components
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746625674217/902b1ac1-f7c2-42cd-b12f-d9803e58739d.png
tags:
- name: Web Components
  slug: web-components
- name: Web Development
  slug: web-development
- name: React
  slug: reactjs
seo_title: Une brève introduction aux Web Components
seo_desc: In a previous article, I gave a brief introduction to React. This tutorial
  introduces an alternative approach to building a component-based frontend. It covers
  the fundamentals of Web Components to build modular, reusable elements for your
  web applic...
---

Dans un article précédent, j'ai donné une [brève introduction à React](https://www.freecodecamp.org/news/a-brief-introduction-to-react/). Ce tutoriel présente une approche alternative pour construire une interface frontend basée sur des composants. Il couvre les fondamentaux des [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) pour créer des éléments modulaires et réutilisables pour vos applications web.

Les Web Components sont un ensemble d'APIs standardisées du navigateur qui vous permettent de créer des éléments HTML personnalisés et réutilisables avec des fonctionnalités encapsulées. Ils aident les développeurs à créer des composants autonomes qui peuvent être utilisés avec différents frameworks ou même sans aucun framework.

Ce tutoriel suppose que vous avez une certaine expérience en programmation et que vous êtes à l'aise avec la lecture et l'écriture de JavaScript. Vous devriez comprendre les variables, les fonctions, les boucles, les objets, les classes et comment JavaScript fonctionne dans le navigateur. Vous n'avez pas besoin de connaître les Web Components pour commencer.

Les quatre leçons présentées ici sont tirées de mon livre gratuit de playbacks de code :

> [Une introduction au développement web de A à Z](https://playbackpress.com/books/webdevbook/)  
> Par Mark Mahoney

Ce livre est disponible gratuitement sur [Playback Press](https://playbackpress.com/books/). Le livre est un guide pratique du développement web moderne, couvrant tout, des fonctionnalités principales de JavaScript à la construction d'applications full-stack avec divers outils et technologies.

Chaque leçon est présentée sous forme de [code playback](https://markm208.github.io/), qui est une visite interactive du code montrant comment un programme évolue au fil du temps, accompagnée de mes explications sur ce qui se passe. Ce format vous aide à vous concentrer sur la logique derrière les modifications du code.

Pour visualiser un playback, cliquez sur les commentaires dans le panneau de gauche. Chaque commentaire met à jour le code dans l'éditeur et met en évidence le changement. Lisez l'explication, étudiez le code et utilisez le tuteur IA intégré si vous avez des questions. Voici une courte vidéo montrant comment utiliser un code playback :

%[https://youtu.be/uYbHqCNjVDM] 

Après cette introduction, vous pourriez vouloir explorer les ressources officielles sur les Web Components : [Guide MDN sur les Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components).

## **Table des matières**

* [Web Components Partie 1 : Votre premier élément personnalisé](#heading-web-components-partie-1-votre-premier-element-personnalise)
    
* [Web Components Partie 2 : Communication de données](#heading-web-components-partie-2-communication-de-donnees)
    
* [Web Components Partie 3 : Événements personnalisés](#heading-web-components-partie-3-evenements-personnalises)
    
* [Web Components Partie 4 : Construction d'une application complète](#heading-web-components-partie-4-construction-dune-application-complete)
    
* [Comparaison React vs Web Components](#heading-react-vs-web-components-comparaison)
    

## **Web Components Partie 1 : Votre premier élément personnalisé**

Cette première leçon introduit la construction d'interfaces utilisateur en utilisant les Web Components, qui vous permettent de regrouper HTML, CSS et JavaScript en un seul élément réutilisable.

Ces éléments peuvent être traités comme des éléments HTML intégrés tels que `h1`, `div` et `img`. Ils sont particulièrement utiles lorsque vous souhaitez diviser une page en parties plus petites, autonomes et réutilisables comme des en-têtes, des tableaux ou des formulaires, tout en gardant le code de chaque partie organisé et isolé.

Dans ce playback, vous apprendrez :

* Comment créer une classe JavaScript qui représente un élément HTML personnalisé
    
* Comment accéder aux attributs du web component
    
* Comment créer et utiliser un web component en HTML
    

La leçon se concentre sur la création d'un composant `LegendHeader` qui peut être réutilisé dans une application web. Vous verrez comment les éléments personnalisés peuvent avoir des attributs comme les éléments HTML réguliers (comme `src` dans une balise `img`), et comment ces attributs peuvent être modifiés à partir du code JavaScript, déclenchant des méthodes en réponse.

**Visualisez le playback ici :** [**Web Components Partie 1 - LegendHeader**](https://playbackpress.com/books/webdevbook/chapter/3/8)

## **Web Components Partie 2 : Communication de données**

En s'appuyant sur la leçon précédente, ce playback démontre comment créer plusieurs composants qui partagent des données. J'améliorerai le composant `LegendHeader` pour afficher le nombre de légendes suivies, et j'ajouterai un nouveau composant `LegendTable` qui affiche toutes les légendes CS dans une base de données en utilisant un tableau HTML.

Un concept clé introduit dans cette leçon est d'avoir un élément de niveau supérieur qui détient les données de l'application web et qui communique les changements aux composants qui en dépendent. Cette approche rend la gestion des composants plus organisée et maintenable.

Dans ce playback, vous apprendrez :

* Comment créer et travailler avec plusieurs composants
    
* Comment configurer et utiliser des 'attributs observables' dans un web component
    
* Comment un élément de niveau supérieur peut gérer les données et informer les composants lorsque les données changent
    

**Visualisez le playback ici :** [**Web Components Partie 2 - LegendTable**](https://playbackpress.com/books/webdevbook/chapter/3/9)

## **Web Components Partie 3 : Événements personnalisés**

Cette leçon étend l'application en ajoutant un composant `NewLegendForm` qui permet aux utilisateurs d'ajouter de nouvelles légendes à la base de données. Le playback introduit le concept d'événements personnalisés qui 'remontent' à travers le DOM, permettant aux éléments de niveau supérieur de contrôler les demandes de données.

Vous apprendrez pourquoi il est souvent préférable que les composants ne gèrent pas eux-mêmes les données de l'application. Avoir un élément de niveau supérieur gérer toutes les données de l'application web rend les composants plus simples et plus réutilisables, car ils n'ont pas besoin de se connaître ou de communiquer directement.

Dans ce playback, vous apprendrez :

* Comment les composants peuvent générer des événements personnalisés pour demander des données au lieu de les gérer eux-mêmes
    
* Comment un élément de niveau supérieur peut écouter les événements et les traiter
    
* Comment un élément de niveau supérieur accède aux données et les transmet aux composants qui en ont besoin
    

**Visualisez le playback ici :** [**Web Components Partie 3 - NewLegendForm**](https://playbackpress.com/books/webdevbook/chapter/3/10)

## **Web Components Partie 4 : Construction d'une application complète**

Dans cette dernière leçon, je rassemble tout pour créer une application complète avec authentification. J'ajouterai un nouveau composant `AuthBox` et implémenterai un système d'authentification léger afin que seuls les utilisateurs enregistrés et connectés puissent ajouter de nouvelles légendes à la base de données.

Le playback utilise des sessions sur le serveur pour contrôler l'accès des utilisateurs et renforce l'importance de la gestion centralisée des données dans une architecture basée sur des composants.

Dans ce playback, vous apprendrez :

* Comment implémenter l'authentification des utilisateurs avec un web component
    
* Comment intégrer tous les composants dans une application complète et fonctionnelle
    
* Les meilleures pratiques pour la gestion des données dans les applications web basées sur des composants
    

**Visualisez le playback ici :** [**Web Components Partie 4 - AuthBox**](https://playbackpress.com/books/webdevbook/chapter/3/11)

## **Comparaison React vs Web Components**

Certaines des principales différences entre React et les Web Components peuvent être résumées comme suit :

| Propriété clé | React | Web Components |
| --- | --- | --- |
| **Définition des composants** | Utilise des fonctions (généralement) pour définir les composants | Utilise des classes JavaScript qui étendent HTMLElement |
| **Exigences d'outillage** | Nécessite des outils pour l'installation, la transpilation, le bundling (npm, webpack, babel, etc.) | Support natif du navigateur sans outils de build ou installation requise |
| **Syntaxe des templates** | Utilise JSX, une syntaxe similaire à HTML dans JavaScript | Utilise HTML standard dans des chaînes ou des templates HTML |
| **Mises à jour du DOM** | Utilise le Virtual DOM pour regrouper et minimiser efficacement les manipulations réelles du DOM | Manipule directement le DOM, généralement moins optimisé pour les mises à jour fréquentes |
| **Types de propriétés** | Accepte divers types de données comme props (chaînes, tableaux, objets, fonctions) | N'accepte que les chaînes comme attributs en HTML |
| **Modèle de rendu** | Déclaratif : décrit à quoi l'UI devrait ressembler, React gère les mises à jour | Plus impératif : manipule directement le DOM en réponse aux changements |
| **Encapsulation des styles** | Pas d'encapsulation des styles intégrée (nécessite CSS-in-JS ou CSS Modules) | Encapsulation des styles intégrée avec Shadow DOM |
| **Support des navigateurs** | Fonctionne dans tous les navigateurs via des polyfills | Navigateurs modernes uniquement (peut nécessiter des polyfills pour les anciens navigateurs) |
| **Écosystème** | Grand écosystème avec de nombreuses bibliothèques et outils | Écosystème plus petit, mais en croissance |

## Conclusion

Ces quatre leçons couvrent les fondamentaux des Web Components, mais il y a beaucoup plus à explorer. Les Web Components offrent une manière standardisée de créer des éléments réutilisables sans avoir besoin de bibliothèques ou de frameworks externes, ce qui les rend particulièrement précieux pour construire un code maintenable et portable.

Si vous avez trouvé ce format utile, explorez le reste du livre pour voir comment des applications web complètes sont construites à partir de zéro en utilisant des outils et des approches modernes.

Les Web Components représentent une approche du développement web basé sur des composants. Continuez à construire, continuez à lire et essayez les autres playbacks lorsque vous êtes prêt à aller plus loin.

Si vous avez des commentaires sur les playbacks, j'aimerais avoir de vos nouvelles. Vous pouvez me contacter ici [mark@playbackpress.com](mailto:mark@playbackpress.com).

Si vous souhaitez soutenir mon travail et aider à garder Playback Press gratuit pour tous, envisagez de faire un don via [GitHub Sponsors](https://github.com/sponsors/markm208). J'utilise toutes les donations pour couvrir les coûts d'hébergement. Votre soutien m'aide à continuer à créer du contenu éducatif comme celui-ci. Merci !