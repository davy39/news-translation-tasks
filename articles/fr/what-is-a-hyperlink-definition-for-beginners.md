---
title: Qu'est-ce qu'un hyperlien ? Les liens HTML expliqués avec des exemples
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2021-08-16T23:33:49.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-hyperlink-definition-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/uide-to-writting-a-good-readme-file--3--1.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce qu'un hyperlien ? Les liens HTML expliqués avec des exemples
seo_desc: "Let's begin with a quick question: How did you land on this article and\
  \ this site today? \nWell, quite literally, by clicking or tapping on a link, right?\
  \ That's how powerful this element is – it will get you to any part of the Internet\
  \ just by clicki..."
---

Commençons par une question rapide : Comment êtes-vous arrivé sur cet article et ce site aujourd'hui ?

Eh bien, tout simplement, en cliquant ou en tapant sur un lien, n'est-ce pas ? C'est à quel point cet élément est puissant – il vous emmène à n'importe quelle partie d'Internet simplement en cliquant sur un lien.

Alors, que sont les liens et les hyperliens en HTML ?

## Que sont les liens et les hyperliens en HTML ?
Un lien est une chaîne qui connecte les pages à la fois au sein d'un site web et vers d'autres sites web. Sans liens, nous n'aurions aucun site web.

Par exemple, jetons un coup d'œil à cette URL, `https://www.freecodecamp.org/`. Lorsque vous la tapez dans la barre d'adresse, elle vous emmène sur le site officiel de freeCodeCamp.

En termes plus simples, nous pouvons dire que les liens sont simplement les adresses web des pages web qui vous permettent de vous connecter à différents serveurs.

Peut-être vous demandez-vous alors ce qu'est un hyperlien ? Eh bien, ils permettent de lier des documents à d'autres documents ou ressources via des références appelées <mark>balises d'ancrage</mark>. Ils sont un concept fondamental derrière le World Wide Web qui facilite la navigation entre les pages web via des liens.

Les hyperliens peuvent être présentés sous différentes formes, comme une image, une icône, un texte, ou tout type d'élément visible qui, lorsqu'on clique dessus, vous redirige vers une URL spécifiée.

Par exemple, si vous cliquez [ICI](https://www.freecodecamp.org/news/author/larymak/), vous arriverez sur mon profil avec une liste de mes autres articles. C'est un hyperlien.


## Comment créer des liens en HTML

### Comment utiliser les liens `<a>`
Vous pouvez créer un lien de base en enveloppant le texte (ou tout autre contenu lié) dans l'élément `<a></a>` et en utilisant l'attribut `href` qui contient l'adresse.

Voici un exemple en action :
```html
<a href="https://www.freecodecamp.org">Visitez : Freecode Camp !</a>
```

### Comment styliser les liens
Il y a généralement des liens insérés dans le fichier `.html` qui relient le principal au fichier de style et de fonctionnalité. Et ils sont généralement nommés avec les extensions de fichier `.css` et `.js`.

Voici comment lier un fichier CSS :

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

<h1>Ceci est un titre</h1>
<p>Ceci est un paragraphe.</p>

</body>
</html>
```

Et voici comment lier un fichier JS. Vous pouvez placer ce que vous voulez lier dans la balise head ou body.

```html
<!DOCTYPE html>
<html>
<head>
  <script src="myScript.js"></script>
</head>
<body>

<h1>Ceci est un titre</h1>
<p>Ceci est un paragraphe.</p>

</body>
</html>
```

## Comment lier au sein d'un site
### Liens vers différentes pages au sein d'un site
Vous utilisez ce type de lien pour diriger un utilisateur vers différentes pages du même site.

Prenons un cas où votre site a 5 pages. Vous voulez qu'un utilisateur puisse accéder à toutes les pages à partir d'un seul point, comme la barre de navigation.

D'abord, vous devrez créer toutes les pages puis les lier. Dans ce cas, nous le ferons comme ceci :

```html
<nav>
    <ul>
        <li><a href="home.html">Accueil</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="pricing.html">Tarifs</a></li>
        <li><a href="about.html">À propos</a></li>
        <li><a href="contact.html">Contact</a></li>
    </ul>
</nav>
```

L'exemple ci-dessus liera vers différentes parties du site – la page 'Accueil', 'Services', 'Tarifs', et 'À propos', dans cet ordre. Écrire uniquement le nom du fichier est suffisant car tout le travail est partagé dans le même dossier de travail.

### Comment lier vers une section spécifique d'un site

Supposons que, quelque part sur votre site, vous avez mentionné un sujet ou une page particulier. Et vous aimeriez que vos lecteurs ou visiteurs puissent sauter directement à cette section avec un clic.

D'abord, vous devrez ajouter l'attribut `id` à cette section de la page. Peut-être est-ce un paragraphe – si c'est le cas, voici à quoi cela ressemblerait :

```html
<p id="detailed-info"> Lire plus sur les événements à venir </p>
```
Après cela, dans votre lien, ajoutez l'`id` dans le `href` :
```html
<a href="#detailed-info"> Lire plus sur les événements à venir </a>
```

Ce code les emmènera directement à la section des événements à venir.

## Autres types de liens en HTML

### Comment lier vers un fichier téléchargeable

Lorsque vous voulez lier vers une ressource qu'un utilisateur doit télécharger plutôt que d'ouvrir dans le navigateur, vous pouvez utiliser l'attribut `download`. Cela fournit un nom de fichier d'enregistrement par défaut.

L'attribut de téléchargement est idéal pour les PDF, les fichiers image, les clips vidéo et audio, et autres contenus multimédias que vous souhaitez que les utilisateurs enregistrent sur leur ordinateur ou appareil mobile.

Voici un exemple avec un lien de téléchargement :
```html
<a href="https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US"
   download="firefox-latest-64bit-installer.exe">
  Télécharger le dernier Firefox pour Windows (64-bit) (Anglais, US)
</a>
```

### Comment ajouter des liens e-mail

Les liens e-mail nous permettent de créer des hyperliens vers une adresse e-mail. Vous pouvez créer ces liens en utilisant la balise HTML `<a></a>` – mais dans ce cas, au lieu de passer une URL, nous passons l'adresse e-mail du destinataire.

Vous utilisez l'attribut `mailto` pour spécifier l'adresse e-mail dans votre balise d'ancrage.

Par exemple :
```html
<a href="mailto:hillarynyk@gmail.com">Envoyer un e-mail à moi</a>
```

En plus de l'adresse e-mail, vous pouvez fournir d'autres informations. En fait, tout champ d'en-tête de mail standard peut être ajouté à l'URL `mailto` que vous fournissez. Les plus couramment utilisés sont "subject", "cc", et "body".

Voici un exemple qui inclut un cc, un bcc, un sujet et un corps :
```html
<a href="mailto:hillarynyk@gmail.com?cc=larymak4@gmail.com&bcc=larymak8@gmail.com&subject=Le%20sujet%20de%20l'email&body=Le%20corps%20de%20l'email">
  Envoyer un mail avec cc, bcc, sujet et corps
</a>
```

## Attributs des liens HTML

Les liens HTML ont divers attributs que vous pouvez utiliser pour fournir des informations plus spécifiques. En voici quelques-uns des plus couramment utilisés.

1. **Attribut href**
L'attribut `href` définit l'URL de destination pour un lien HTML. Il rend le mot ou la phrase marquée cliquable. L'attribut href crée un hyperlien vers une autre page web, et les liens HTML ne fonctionneraient pas comme prévu sans lui.

2. **Attribut target**
L'attribut `target` définit où le lien HTML sera ouvert. Vous êtes déjà allé sur un site web et lorsque vous cliquez sur un lien, il s'ouvre automatiquement dans un nouvel onglet ? Eh bien, c'est le travail de cet attribut.

Voici toutes les options possibles que vous pouvez utiliser avec l'attribut `target` :

* **_blank** => Ouvre le lien dans un nouvel onglet. Principalement utilisé pour éviter de perdre les visiteurs d'un site. Par défaut, lorsqu'un utilisateur clique sur un lien, il s'ouvre dans le même onglet – mais cela change cela.
```html
<a href="https://www.freecodecamp.org/" target="_blank"> freeCodeCamp</a>
```

* **_self** => Charge l'URL dans la même fenêtre ou l'onglet où il a été cliqué. C'est généralement le comportement par défaut et n'a pas besoin d'être spécifié.
```html
<a href="https://www.freecodecamp.org" target="_self">freeCodeCamp</a>
```

* **_parent** => Charge l'URL dans le cadre parent. Il n'est utilisé qu'avec les cadres.
```html
<a href="https://www.freecodecamp.org" target="_parent">freeCodeCamp</a>
```

* **_top** => Charge le document lié dans le corps complet de la fenêtre.
```html
<a href="https://www.freecodecamp.org" target="_top">freeCodeCamp</a>
```

3. **Attribut title**
L'attribut `title` décrit des informations supplémentaires sur le but du lien. Si un utilisateur survole le lien avec sa souris, une info-bulle apparaîtra qui décrit l'objectif, le titre, ou toute autre information sur le lien :

```html
<a href="https://www.freecodecamp.org" title="Lien vers des ressources d'apprentissage gratuites">Apprendre à coder</a>
```

## Conseils rapides sur les liens HTML et récapitulatif
Dans cet article, nous avons tout appris sur les liens et les hyperliens en HTML. Voici quelques conseils finaux pour vous aider à travailler avec les liens.

Premièrement, lorsque vous utilisez une image comme lien, il est toujours bon d'inclure la balise `alt` avec le texte. Cela fournit un texte alternatif qui est affiché au cas où l'image ne se charge pas.

Deuxièmement, vous devriez pratiquer la spécification de la langue du document vers lequel l'ancre est liée en utilisant l'attribut `hreflang`.
```html
<a href="https://www.freecodecamp.org" hreflang="en">Freecode Camp</a>
```

Le Web est vraiment juste une bibliothèque de documents hyperliés où les balises d'ancrage agissent comme des ponts entre les documents liés.

Nous avons vu comment utiliser les liens et comment les créer, et pourquoi ils sont importants dans le développement web.

Il est temps d'aller pratiquer et de perfectionner votre nouvelle compétence.

Bon codage ❤