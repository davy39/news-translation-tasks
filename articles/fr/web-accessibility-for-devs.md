---
title: Conseils d'accessibilité web pour les développeurs – Principes A11y expliqués
subtitle: ''
author: Adeola Ajiboso
co_authors: []
series: null
date: '2023-11-02T14:17:51.000Z'
originalURL: https://freecodecamp.org/news/web-accessibility-for-devs
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/51314.jpg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: Web Development
  slug: web-development
seo_title: Conseils d'accessibilité web pour les développeurs – Principes A11y expliqués
seo_desc: "Accessibility isn't just something you check off as done when you're building\
  \ websites and web apps. It's a basic part of making the online world a better and\
  \ fairer place for everyone. \nIn this article, you'll learn what accessibility\
  \ means, and why..."
---

L'accessibilité n'est pas simplement une case à cocher lorsque vous construisez des sites web et des applications web. C'est une partie fondamentale pour rendre le monde en ligne meilleur et plus équitable pour tous.

Dans cet article, vous apprendrez ce que signifie l'accessibilité et pourquoi il est important d'en faire une partie de votre flux de travail régulier. Je vous donnerai également des conseils pratiques avec des exemples pour rendre vos sites web plus accessibles.

Explorons ensemble les éléments clés de l'accessibilité web et aidons-vous à créer un site web qui inclut tout le monde.

## Qu'est-ce que l'accessibilité web ?

L'[accessibilité web](https://www.freecodecamp.org/news/accessibility-best-practices-to-make-web-apps-accessible/) fait référence à la pratique de concevoir et de développer des sites web, des applications et du contenu numérique de manière à ce que les personnes handicapées puissent les percevoir, les comprendre, les naviguer et interagir avec eux efficacement.

## Principes de l'accessibilité web

Pour améliorer efficacement l'accessibilité de vos sites web et applications, vous devrez suivre ces principes fondamentaux décrits par les Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0)) :

### Est-ce perceptible ?

Le contenu doit être affiché de manière à ce que tous les utilisateurs puissent le comprendre, quelles que soient leurs capacités sensorielles. Voici quelques moyens de rendre votre contenu plus perceptible :

Tout d'abord, vous pouvez fournir des sous-titres pour les matériaux audio et vidéo. L'ajout de sous-titres à votre site web ou application permet aux personnes souffrant de handicaps auditifs de comprendre les informations partagées et rend le contenu plus accessible à tous.

Vous pouvez voir un exemple d'ajout de sous-titres à une vidéo dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/img.jpg)
_Image d'une vidéo illustrant l'utilisation de sous-titres._

Ensuite, assurez-vous d'utiliser un contraste de couleurs approprié pour les éléments de texte et d'arrière-plan.

Les couleurs sont une partie importante d'un site web, et nous pouvons les décrire en termes de teinte, de luminosité et de saturation.

Il existe plusieurs catégories de couleurs qui incluent les couleurs chaudes, les couleurs froides et les couleurs neutres.

**Couleurs chaudes :** Les couleurs chaudes incluent le rouge, l'orange et le jaune, ainsi que les variations de ces trois couleurs. Ce sont les couleurs du feu, des feuilles d'automne, des couchers et levers de soleil, et sont généralement énergisantes, passionnées et positives.

**Couleurs froides :** Les couleurs froides incluent le vert, le bleu et le violet, et sont souvent plus discrètes que les couleurs chaudes. Ce sont les couleurs de la nuit, de l'eau, de la nature, et sont généralement apaisantes, relaxantes et quelque peu réservées.

**Couleurs neutres :** Les couleurs neutres servent souvent de toile de fond dans la conception. Elles sont généralement combinées avec des couleurs d'accentuation plus vives. Mais elles peuvent également être utilisées seules dans les conceptions et peuvent créer des mises en page très sophistiquées. Les couleurs neutres incluent le noir, le blanc, le gris, le crème et le beige.

Des exemples de couleurs qui offrent un bon contraste sont le blanc et le bleu, le violet et le blanc, le jaune et le blanc, le violet clair et le noir, le vert et le blanc, le noir et le blanc, et ainsi de suite – essentiellement toutes les couleurs qui sont suffisamment différentes les unes des autres pour créer ce contraste.

Des exemples de couleurs qui offrent un mauvais contraste sont le gris et le blanc, le marron et l'orange, le rouge et le violet, et ainsi de suite.

Voici un exemple qui montre un bon contraste de couleurs facile à lire :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/1.png)
_Image illustrant un bon contraste utilisant un fond bleu foncé avec du texte blanc_

Et voici une image avec un mauvais contraste de couleurs difficile à lire :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/2.png)
_Image illustrant un mauvais contraste utilisant un fond blanc avec du texte gris clair_

De plus, il est bon d'inclure un texte alternatif descriptif (alt text) pour les images, expliquant ce qu'elles représentent et leur but.

Par exemple, lorsque vous souhaitez ajouter une image à votre site web, vous pouvez ajouter un texte alternatif expliquant ce qu'elle représente.

Voici une description de balisage de la manière d'ajouter un texte alternatif à une image :

```HTML
    <img src="Dog.png" alt="Image d'un chien">
```

Voici un exemple qui montre une image de deux (2) chiens :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/dog.jpg)
_Image de deux chiens_

Et voici un exemple d'une image qui illustre l'utilisation du texte alternatif :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/dog1-1.jpg)
_Image de chien avec le texte alternatif affiché_

Vous devriez également décrire vos boutons d'icônes.

Les icônes peuvent être facilement comprises la plupart du temps. Il est largement reconnu qu'un symbole x, comme ceci ✖, ferme généralement une fenêtre, une coche ✓ signifie achèvement, une flèche avant ▶ signifie envoyer (ou jouer), et un signe plus ➕ représente l'addition.

Mais cela n'est clair que pour les individus ayant des capacités visuelles. Pour les personnes qui ne peuvent pas voir les boutons, vous devrez fournir une description afin qu'elles sachent ce que ce bouton fait.

Examinons ce code HTML et CSS qui montre comment rendre les boutons accessibles :

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css"
     integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA==" 
     crossorigin="anonymous" referrerpolicy="no-referrer" />
    <title>Document</title>
</head>

<style>
    button{
        border: none;
        outline: none;
        color: #fff;
        padding: 12px 12px;
        margin: 10px;
        border-radius: 10px;
        background-color: red;
        cursor: pointer;
    }
</style>
<body>
    <button><i class="fa-solid fa-trash"> Supprimer </i></button>
    <button style="background-color:green;"><i class="fa-solid fa-check"> Vérifier </i></button>
    <button style="background-color:green;"><i class="fa-solid fa-play"> Envoyer</i></button>
    <button style="background-color:blue;"><i class="fa-solid fa-plus"> Ajouter</i></button>
</body>
</html>

Voici le résultat du code implémenté ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/code1.jpg)

### Est-ce utilisable ?

Les utilisateurs doivent pouvoir naviguer et interagir avec l'interface rapidement. Prenez en compte les facteurs suivants :

Tout d'abord, assurez-vous d'utiliser des titres clairs et cohérents.

Voici à quoi ressemblent des titres clairs et cohérents :

# Je suis un Titre

## Je suis un Sous-titre

### Ceci est le titre 3

#### Ceci est le Titre 4

##### Ceci est le Titre 5

###### Ceci est le titre 6

Comme vous pouvez le voir, ces titres vont du plus grand au plus petit dans l'ordre. Nous avons un titre H1 en premier, suivi de H2, H3, et ainsi de suite.

Voici quelques titres qui ne suivent pas la hiérarchie appropriée :

###### Ceci est le titre 6

##### Ceci est le Titre 5

#### Ceci est le Titre 4

### Ceci est le titre 3

## Je suis un Sous-titre

# Je suis un Titre

Dans cet exemple, les titres vont dans l'ordre inverse, commençant par H6 et remontant à travers H5, H4, et ainsi de suite.

Rappelez-vous simplement d'utiliser une hiérarchie de titres appropriée – n'utilisez pas un H2 puis passez directement à H4 pour un sous-titre, par exemple, car cela est visuellement déroutant et ne transmet pas l'importance ou la hiérarchie appropriée du texte.

Voici pourquoi la hiérarchie des titres est importante :

* Une hiérarchie de titres claire aide les lecteurs à naviguer et à comprendre facilement le contenu d'un document.
* La hiérarchie des titres est cruciale pour l'accessibilité, car elle aide les lecteurs d'écran et les technologies d'assistance à interpréter la structure du contenu. Cela est important pour les personnes souffrant de handicaps visuels qui dépendent de tels outils pour accéder à l'information.
* Une hiérarchie de titres bien organisée met en œuvre un flux logique d'informations, garantissant que les sujets sont présentés dans un ordre cohérent.

De plus, évitez d'utiliser des éléments qui pourraient déclencher un inconfort physique, comme des lumières clignotantes vives.

Et assurez-vous de penser à l'[accessibilité au clavier](https://www.freecodecamp.org/news/designing-keyboard-accessibility-for-complex-react-experiences/) afin que les utilisateurs puissent naviguer et communiquer en utilisant le clavier, et pas exclusivement une souris.

### Est-ce compréhensible ?

Le contenu et la fonctionnalité doivent être présentés clairement et de manière compréhensible. Prenez en compte les facteurs suivants :

* Organisez le contenu en utilisant des titres, des sous-titres et des puces pour améliorer la lisibilité.
* Fournissez des instructions et des messages d'erreur faciles à comprendre.
* Utilisez un langage simple et concis, évitez les termes complexes.

### Est-ce robuste ?

Les sites web doivent être construits en utilisant des technologies robustes et largement supportées pour permettre la compatibilité entre les appareils et les technologies d'assistance.

Vous devrez maximiser la compatibilité avec les agents utilisateurs actuels et futurs, y compris les technologies d'assistance.

Voici quelques moyens de maximiser la compatibilité avec les agents actuels et futurs, y compris les outils d'assistance :

* Utilisez des [éléments sémantiques HTML5](https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/) comme `<header>`, `<nav>`, `<main>`, et `<footer>` pour améliorer la structure du document.
* Assurez-vous que votre [code JavaScript est efficace](https://www.freecodecamp.org/news/javascript-performance-async-defer/) et ne bloque pas le processus de rendu.
* Utilisez les [outils de développement du navigateur](https://www.freecodecamp.org/news/learn-how-to-use-the-chrome-devtools-to-troubleshoot-websites/) et les services de test en ligne pour identifier et corriger les problèmes de compatibilité.
* Effectuez des [tests d'utilisabilité](https://www.freecodecamp.org/news/10-best-ux-testing-software-tools/) avec un groupe diversifié d'utilisateurs, y compris ceux qui dépendent des technologies d'assistance, pour recueillir des commentaires et apporter des améliorations.
* Optimisez votre site web pour des temps de chargement rapides et une faible utilisation de données en utilisant des techniques comme la [mise en cache](https://www.freecodecamp.org/news/a-detailed-guide-to-pre-caching/) et des [outils comme les CDN](https://www.freecodecamp.org/news/cdns-speed-up-performance-by-reducing-latency/) pour réduire la latence. Cela bénéficie à la fois à l'accessibilité et à l'expérience utilisateur.
* Documentez votre code et les fonctionnalités d'accessibilité pour les futurs mainteneurs.
* Testez la [compatibilité du site web sur divers navigateurs](https://www.freecodecamp.org/news/cross-browser-compatibility-testing-best-practices-for-web-developers/). Tester la compatibilité d'un site web implique de s'assurer que votre site web fonctionne correctement et a une bonne apparence sur une variété d'appareils, de navigateurs et de technologies d'assistance.

Voici les étapes que vous pouvez suivre pour tester efficacement la compatibilité d'un site web :

1. **Test des appareils** : Testez votre site web sur divers appareils, tels que des ordinateurs de bureau, des ordinateurs portables, des tablettes et des smartphones. Cela inclut les appareils iOS et Android.
2. **Test des navigateurs** : Vérifiez les performances et l'apparence de votre site web sur plusieurs navigateurs, y compris, mais sans s'y limiter, Google Chrome, Mozilla Firefox, Apple Safari et Microsoft Edge.
3. **Test utilisateur** : Effectuez des tests d'utilisabilité avec de vrais utilisateurs. Demandez-leur d'utiliser votre site web sur différents appareils et navigateurs et recueillez des commentaires sur les problèmes de compatibilité.
4. **Test de performance** : Évaluez les temps de chargement du site web et optimisez la vitesse en utilisant des outils comme Google PageSpeed Insights, GTmetrix ou Lighthouse. Vérifiez la compatibilité avec les connexions internet lentes.

## Conclusion

Comprendre l'accessibilité web peut améliorer l'expérience utilisateur en créant une interaction fluide et sans faille avec les sites web et les applications web.

La mise en œuvre de ces conseils peut améliorer la convivialité et la navigabilité globales de votre application. Cela aidera à créer une expérience plus agréable pour tous les utilisateurs et permettra également aux personnes handicapées de percevoir, comprendre, naviguer et interagir avec vos sites efficacement.