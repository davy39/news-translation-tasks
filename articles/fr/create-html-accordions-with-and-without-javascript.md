---
title: Comment créer des éléments HTML Accordion avec et sans JavaScript
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-11-30T19:10:31.000Z'
originalURL: https://freecodecamp.org/news/create-html-accordions-with-and-without-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/accordion-1.png
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment créer des éléments HTML Accordion avec et sans JavaScript
seo_desc: 'Accordion elements are very handy for displaying topic titles and expandable
  details below them when you click the title.

  In this article, I''ll walk you through creating an FAQ section with some expandable
  accordion elements.

  I''ll show you how to do ...'
---

Les éléments accordéon sont très pratiques pour afficher les titres des sujets et les détails extensibles en dessous lorsqu'on clique sur le titre.

Dans cet article, je vais vous guider à travers la création d'une section FAQ avec quelques éléments accordéon extensibles.

Je vais vous montrer comment faire cela sans aucun JavaScript, puis nous ajouterons un peu de JavaScript pour le rendre encore meilleur.

J'ai également réalisé un tutoriel vidéo de tout le processus ici :

%[https://youtu.be/NYleh6wzDRE]

## Comment créer un accordéon en utilisant <details>

HTML possède un élément de divulgation appelé `<details>` qui peut être dans l'un des deux états : ouvert et fermé. Lorsqu'il est ouvert, les informations contenues dans l'élément sont affichées. Lorsqu'il est fermé, seules les informations `<summary>` sont affichées.

Il s'agit d'une version extrêmement facile de l'"accordion", bien qu'on puisse dire qu'il ne s'agit pas d'un vrai accordéon à proprement parler. En utilisant `<details>`, plus d'un des panneaux peuvent être ouverts à la fois – et comme il n'y a pas encore de JavaScript, les panneaux resteront ouverts jusqu'à ce que vous cliquiez à nouveau pour les fermer.

Néanmoins, il s'agit d'un moyen rapide et facile d'obtenir un élément de type accordéon. Si vous n'en avez besoin que de quelques-uns et que vous n'êtes pas difficile sur la fonctionnalité, cela peut être tout ce que vous cherchez.

Voici à quoi ressemble un exemple de base. Le `<summary>` est visible jusqu'à ce qu'on clique dessus, moment auquel le reste du contenu est affiché en dessous.

```html
<!-- Avec juste <details> -->
<section>
    <h2>Accordéon utilisant details</h2>
    <details open>
        <summary>Qui est Eamonn ?</summary>
        Un gars du TN qui crée du contenu sur internet.
    </details>
    <details>
        <summary>Quel type de contenu crée-t-il ?</summary>
        Il se concentre sur des conseils de productivité utilisant la programmation et les tableurs. Il crée des vidéos <a href="https://youtube.com/@eamonncottrell">YouTube</a> et écrit des articles sur freeCodeCamp, <a href="https://www.linkedin.com/in/eamonncottrell/">LinkedIn</a> et sa <a href="https://got-sheet.beehiiv.com/">newsletter personnelle</a>.
    </details>
    <details>
        <summary>Que fait-il pour s'amuser ?</summary>
        Il passe du temps avec sa femme et ses quatre enfants, et court des ultramarathons.
    </details>
</section>
```

Nous pouvons également avoir le premier panneau de détails ouvert par défaut en incluant simplement la commande open : `<details open>`. 

Voici à quoi cela ressemblera avec seulement une touche de CSS :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/image-92.png)
_capture d'écran de l'accordéon HTML réalisé avec &lt;details&gt; uniquement_

C'est un excellent début, mais nous pouvons aller plus loin. Un peu de JavaScript ira loin 👍

## Comment ajouter JavaScript à un élément Accordion

Créons une autre section avec trois autres éléments `<details>`. Et ajoutons une `class = "withJS"` à chacun afin de pouvoir faire différentes choses pour comparaison.

```html
<!-- Avec JavaScript -->
<section>
    <h2>Accordéon avec un peu de JavaScript ajouté</h2>
    <details  open>
        <summary class="withJS">Quelle est la différence ?</summary>
        Nous ajoutons JavaScript à ces trois éléments.
    </details>
    <details >
        <summary class="withJS">Pourquoi ajouter JavaScript ?</summary>
        Nous pouvons faire en sorte qu'un seul panneau puisse être ouvert à la fois.
    </details>
    <details >
        <summary class="withJS">Essayez de cliquer sur chacun de ceux-ci</summary>
        Voyez comment un panneau se ferme dès qu'un autre s'ouvre ?.
    </details>
</section>
```

Pour garder les choses bien organisées et dans un seul fichier, nous pouvons ajouter une balise `<script>` en bas de notre `<body>`. 

Tout d'abord, sélectionnez tous les éléments summary avec la classe `.withJS` en utilisant `document.querySelectorAll()` :

```javascript
const summaries = document.querySelectorAll(".withJS")
```

Puis ajoutez un écouteur d'événement de clic à chacun d'eux :

```javascript
summaries.forEach(e=>{
    e.addEventListener('click',openCloseDetails)
})
```

Cela exécutera la fonction `openCloseDetails` chaque fois que l'un de ces éléments summary est cliqué.

Cela ne fera rien sauf nous donner une erreur jusqu'à ce que nous déclarions cette fonction, alors... faisons cela ensuite.

Dans le `<script>` après la boucle `forEach`, faisons en sorte que la fonction `openCloseDetails()` parcourt à nouveau ces résumés. Cette fois, nous voulons modifier le statut `open` sur l'élément `<details>`.

Rappelez-vous comment nous avons configuré cela : Le premier élément `<details>` est défini sur `open` par défaut, et les autres sont fermés.

Nous avons besoin d'un moyen pour basculer l'élément cliqué de ouvert à fermé, et fermer tout élément précédemment `open` lorsque nous cliquons sur un nouveau.

Pour ce faire, nous allons définir une variable pour l'élément `<details>` de chacun des éléments `<summary>` en la définissant égale à `e.parentNode` dans la boucle `forEach`. 

```javascript
let details = e.parentNode;
```

Le parentNode est l'élément directement précédent l'élément actuel. Puisque les éléments `<summary>` sont dans les éléments `<details>`, le `parentNode` pour les éléments `<summary>` sera le `<details>`.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/clearly.gif)
_gif d'une femme disant, "clairement"_

À partir de là, nous vérifions si ce `<details>` n'est PAS `this.parentNode`. Si ce n'est pas le cas, alors nous allons supprimer l'attribut `open`.

La fonctionnalité native des éléments `<details>` ouvrira celui qui est cliqué, nous devions simplement nous assurer que tous les autres se ferment.

Voici le code. Ce n'est pas compliqué, mais il peut prendre un moment pour comprendre la logique :

```javascript
summaries.forEach(e =>{
    let details = e.parentNode;
    if(details != this.parentNode){
        details.removeAttribute('open')
    }
```

Et c'est tout. Maintenant, lorsque nous cliquons sur chaque `<details>`, les autres se ferment automatiquement :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/accordion-gif.gif)
_gif de l'accordéon html en action_

Voici le fichier HTML complet pour référence :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accordéon</title>
</head>
<body>
    <style>
        body{
            background: rgb(255, 255, 230);
            color: #444;
        }
        details{
            font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            margin-bottom: 5px;
            padding: 0.5em 0.5em 0;
        }
        details[open]{
            padding: 0.5em;
        }
        summary{
            font-weight: bold;
            margin: -0.5em -0.5em 0;
            padding: 0.5em;
            cursor: pointer;
        }
        details[open] summary{
            margin-bottom: 0.5em;
        }
    </style>
    
    <h1>Accordéons</h1>

    <!-- Avec juste <details> -->

    <section>
        <h2>Accordéon utilisant details</h2>
        <details open>
            <summary>Qui est Eamonn ?</summary>
            Un gars du TN qui crée du contenu sur internet.
        </details>
        <details>
            <summary>Quel type de contenu crée-t-il ?</summary>
            Il se concentre sur des conseils de productivité utilisant la programmation et les tableurs. Il crée des vidéos <a href="https://youtube.com/@eamonncottrell">YouTube</a> et écrit des articles sur freeCodeCamp, <a href="https://www.linkedin.com/in/eamonncottrell/">LinkedIn</a> et sa <a href="https://got-sheet.beehiiv.com/">newsletter personnelle</a>.
        </details>
        <details>
            <summary>Que fait-il pour s'amuser ?</summary>
            Il passe du temps avec sa femme et ses quatre enfants, et court des ultramarathons.
        </details>
    </section>
    

    <!-- Avec JavaScript -->
    <section>
        <h2>Accordéon avec un peu de JavaScript ajouté</h2>
        <details  open>
            <summary class="withJS">Quelle est la différence ?</summary>
            Nous ajoutons JavaScript à ces trois éléments.
        </details>
        <details >
            <summary class="withJS">Pourquoi ajouter JavaScript ?</summary>
            Nous pouvons faire en sorte qu'un seul panneau puisse être ouvert à la fois.
        </details>
        <details >
            <summary class="withJS">Essayez de cliquer sur chacun de ceux-ci</summary>
            Voyez comment un panneau se ferme dès qu'un autre s'ouvre ?.
        </details>
    </section>
    
    <script>
        const summaries = document.querySelectorAll(`.withJS`)
        summaries.forEach(e=>{
            e.addEventListener('click',openCloseDetails)
        })

        function openCloseDetails(){
            summaries.forEach(e =>{
                let details = e.parentNode;
                if(details != this.parentNode){
                details.removeAttribute('open')
            }
            })
        }
    </script>
</body>
</html>
```

## Merci d'avoir lu

J'espère que cela a été utile pour vous !

Venez me suivre sur YouTube : [https://www.youtube.com/@eamonncottrell](https://www.youtube.com/@eamonncottrell) 

Et inscrivez-vous à ma newsletter sur la programmation et les tableurs : [https://got-sheet.beehiiv.com/](https://got-sheet.beehiiv.com/)

Passez une excellente journée !