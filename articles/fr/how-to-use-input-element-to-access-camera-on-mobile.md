---
title: Comment utiliser l'élément <input> pour accéder à la caméra d'un appareil mobile
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-01-31T08:55:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-input-element-to-access-camera-on-mobile
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--5-.png
tags:
- name: HTML5
  slug: html5
seo_title: Comment utiliser l'élément <input> pour accéder à la caméra d'un appareil
  mobile
seo_desc: "Mobile devices have become common tools for communication, entertainment,\
  \ and productivity. \nWith the growth of smartphones and tablets, accessing features\
  \ like the camera directly from a web application has become increasingly important.\
  \ Fortunately..."
---

Les appareils mobiles sont devenus des outils courants pour la communication, les loisirs et la productivité. 

Avec la croissance des smartphones et des tablettes, l'accès à des fonctionnalités comme la caméra directement depuis une application web est devenu de plus en plus important. Heureusement, HTML5 offre un moyen simple et efficace de le faire en utilisant l'élément `<input>`.

Dans cet article, nous allons explorer comment utiliser l'élément `<input>` avec les attributs `type` et `capture` pour capturer de manière transparente la caméra d'un utilisateur sur les appareils mobiles. Nous discuterons de ces attributs, comprendrons leurs fonctionnalités et fournirons des exemples pratiques tout au long de cet article. Alors, plongeons-nous dans le sujet !

### Table des matières

1. [Comprendre l'élément `<input>`](#heading-comprendre-lelement)
2. [Utilisation de l'attribut `type`](#utilisation-de-lattribut-type)
3. [Présentation de l'attribut `capture`](#heading-presentation-de-lattribut-capture)  
3.1. [Capture depuis la caméra avant (`user`)](#1-capture-depuis-la-camera-avant-user-)  
3.2. [Capture depuis la caméra arrière (`environment`)](#2-capture-depuis-la-camera-arriere-environment-)

4.  [Limitations et considérations pour la capture vidéo](#heading-limitations-et-considerations-pour-la-capture-video)  
\t4.1. [Support des navigateurs et des appareils](#heading-1-support-des-navigateurs-et-des-appareils)  
\t4.2. [Approches alternatives](#heading-2-approches-alternatives)  
\t4.3. [Amélioration progressive](#heading-3-amelioration-progressive)

5.  [Implémentation pratique](#heading-implementation-pratique)

6.  [Conclusion](#heading-conclusion)

## Comprendre l'élément `<input>`

L'élément `<input>` est l'un des éléments de formulaire les plus polyvalents et largement utilisés en HTML. Il permet aux utilisateurs de saisir des données et d'interagir avec des applications web de diverses manières, telles que la saisie de texte, la sélection de fichiers, et plus encore. 

En ce qui concerne la capture de la caméra d'un utilisateur sur mobile, nous nous concentrerons sur l'utilisation de l'élément `<input>` avec des attributs spécifiques adaptés à cet usage.

## Comment utiliser l'attribut `type`

L'attribut `type` de l'élément `<input>` spécifie le type de contrôle de saisie à afficher. 

Pour capturer la caméra d'un utilisateur sur mobile, nous utiliserons l'attribut `type` avec la valeur `file`. Cette valeur indique que la saisie doit inviter l'utilisateur à sélectionner un fichier, qui dans notre cas, sera une image ou une vidéo directement depuis leur caméra.

```html
<input type="file" accept="image/*, video/*" capture>

```

En définissant l'attribut `type` sur `file`, nous informons le navigateur d'ouvrir la boîte de dialogue de sélection de fichiers lorsque l'entrée est cliquée, permettant à l'utilisateur de choisir un fichier image ou vidéo depuis leur appareil. L'attribut `accept` affine davantage la sélection pour n'accepter que les types de fichiers image et vidéo.

## Présentation de l'attribut `capture`

L'attribut `capture` est un attribut supplémentaire introduit dans HTML5, spécifiquement ciblant les appareils mobiles. Il améliore la fonctionnalité de l'élément `<input>` en permettant un accès direct à la caméra de l'appareil. L'attribut `capture` peut accepter deux valeurs : `user` et `environment`.

### 1. Capture depuis une caméra avant (`user`)

Définir l'attribut `capture` sur `user` indique au navigateur d'ouvrir la caméra avant lorsque l'entrée est activée. Cela est particulièrement utile pour des scénarios tels que la prise de selfies ou la capture d'appels vidéo directement dans une application web.

```html
<input type="file" accept="image/*, video/*" capture="user">

```

Avec cette configuration, les utilisateurs peuvent basculer de manière transparente vers la caméra avant de leur appareil et capturer des photos ou enregistrer des vidéos sans quitter la page web.

### 2. Capture depuis une caméra arrière (`environment`)

Alternativement, définir l'attribut `capture` sur `environment` dirige le navigateur pour accéder à la caméra arrière de l'appareil. Ce mode est adapté aux scénarios où les utilisateurs doivent capturer leur environnement, comme la numérisation de codes-barres, la documentation d'événements ou la prise de photos de paysages.

```html
<input type="file" accept="image/*, video/*" capture="environment">

```

En spécifiant `capture="environment"`, l'application web invite les utilisateurs à utiliser la qualité supérieure et la perspective plus large offertes par la caméra arrière de leur appareil mobile.

## Limitations et considérations pour la capture vidéo

L'attribut `capture` lui-même ne garantit pas la fonctionnalité de capture vidéo, car son objectif principal est de spécifier si l'on utilise la caméra avant ou arrière (valeurs `user` ou `environment`) lors de la capture de médias. 

De plus, la capacité à capturer directement des vidéos via l'élément `<input>` n'est pas universellement supportée et est soumise à des limitations et des incohérences selon les différentes plateformes et navigateurs.

### 1. Support des navigateurs et des appareils

Tous les navigateurs et appareils ne supportent pas la capture vidéo via l'élément `<input>`. Alors que certains navigateurs modernes peuvent permettre la capture vidéo, d'autres peuvent ne supporter que la capture d'images. De plus, le comportement peut varier en fonction du système d'exploitation et des capacités de l'appareil.

### 2. Approches alternatives

Pour les scénarios nécessitant une fonctionnalité de capture vidéo, vous pouvez envisager d'autres approches telles que :

**Utilisation de bibliothèques/API JavaScript :** Tirer parti de bibliothèques ou d'API JavaScript telles que l'API MediaDevices permet aux développeurs d'accéder à des fonctionnalités plus avancées pour la capture de médias, y compris les capacités d'enregistrement vidéo. Ces solutions offrent un meilleur contrôle et une plus grande cohérence sur différents appareils et plateformes.

**Applications mobiles natives :** Pour les applications fortement dépendantes de la capture vidéo, le développement d'applications mobiles natives adaptées à des plateformes spécifiques peut offrir la meilleure expérience utilisateur. Les applications natives peuvent tirer parti des API et optimisations spécifiques à la plateforme pour une capture et un traitement vidéo fluides.

### 3. Amélioration progressive

Lors de la mise en œuvre de la fonctionnalité de capture vidéo dans les applications web, il est essentiel d'employer des stratégies d'amélioration progressive. Cela implique de fournir une fonctionnalité de base en utilisant les fonctionnalités HTML standard et d'améliorer l'expérience pour les appareils et navigateurs capables en utilisant des techniques avancées telles que des solutions basées sur JavaScript ou l'intégration d'applications natives.

En adoptant une approche d'amélioration progressive, les développeurs peuvent s'assurer que les utilisateurs avec des appareils et navigateurs compatibles profitent d'une expérience de capture vidéo améliorée tout en maintenant une fonctionnalité de base pour les utilisateurs sur des plateformes moins capables.

## Implémentation pratique

Mettons nos connaissances en pratique en créant une simple page web qui utilise l'élément `<input>` pour capturer la caméra d'un utilisateur sur mobile.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Capture de caméra</title>
</head>
<body>
   <label for="selfie" class="capture-button">Prendre un selfie</label>
    <input type="file" id="selfie" capture="user" accept="image/*,video/*">
        
    <label for="photo" class="capture-button">Prendre une photo</label>
    <input type="file" id="photo" capture="environment" accept="image/*,video/*">   
 
</body>
</html>

```

Résultat :

<style>

        .capture-button {
            padding: 15px 30px;
            font-size: 18px;
            border: none;
            background-color: #007bff;
            color: #fff;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin: 10px;
        }

        .capture-button:hover {
            background-color: #0056b3;
        }

        input[type="file"] {
            display: none;
        }

        label {
            display: block;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <label for="selfie" class="capture-button">Prendre un selfie</label>
    <input type="file" id="selfie" capture="user">
        
    <label for="photo" class="capture-button">Prendre une photo</label>
    <input type="file" id="photo" capture="environment">
</body>
</html>


Dans cet exemple, l'élément `<input>` est configuré pour accepter à la fois les fichiers image et vidéo tout en utilisant l'attribut `capture` pour capturer depuis la caméra avant et la caméra arrière.

## Conclusion

Capturer la caméra d'un utilisateur sur les appareils mobiles est une fonctionnalité puissante qui améliore les fonctionnalités et l'interactivité des applications web. 

En tirant parti de l'élément `<input>` avec les attributs `type` et `capture`, les développeurs peuvent intégrer de manière transparente la fonctionnalité de la caméra dans leurs projets, offrant aux utilisateurs une expérience riche et immersive.

Dans ce guide, nous avons exploré les subtilités de l'utilisation de l'élément `<input>` pour capturer la caméra d'un utilisateur sur mobile. De la compréhension de l'objectif de chaque attribut aux exemples d'implémentation pratique, vous disposez maintenant des connaissances et des outils pour incorporer efficacement la fonctionnalité de la caméra dans vos applications web.

Bien que l'attribut `capture` combiné avec l'élément `<input>` puisse faciliter la capture d'images depuis la caméra sur les appareils mobiles, la capture de vidéos directement par cette méthode n'est pas universellement supportée. Vous pouvez envisager des approches alternatives et employer des stratégies d'amélioration progressive pour fournir une expérience de capture vidéo cohérente et optimale sur différentes plateformes et appareils.

Alors, n'hésitez pas, expérimentez avec l'élément `<input>`, et réalisez tout le potentiel de la capture de caméra mobile dans vos projets web.