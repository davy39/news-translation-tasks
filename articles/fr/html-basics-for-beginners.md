---
title: Apprenez les bases du HTML pour les débutants en seulement 15 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-12T16:41:21.000Z'
originalURL: https://freecodecamp.org/news/html-basics-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Ep10_html.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Apprenez les bases du HTML pour les débutants en seulement 15 minutes
seo_desc: "By Thu Nghiem\nIf you want to build a website, the first language that\
  \ you need to learn is HTML. \nIn this article, we are going to go through the basics\
  \ of HTML. At the end, we are going to build a basic website using only HTML. \n\
  Here's a video you c..."
---

Par Thu Nghiem

Si vous voulez créer un site web, le premier langage que vous devez apprendre est le HTML. 

Dans cet article, nous allons passer en revue les bases du HTML. À la fin, nous construirons un site web basique en utilisant uniquement le HTML. 

Voici une vidéo que vous pouvez regarder pour compléter cet article :  


%[https://youtu.be/pMJ0NI3OkYA]

## Qu'est-ce que le HTML ?

Le HTML, qui signifie Hypertext Markup Language, est un langage assez simple. Il se compose de différents éléments que nous utilisons pour structurer une page web.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-11-at-1.16.17-PM.png)
_Qu'est-ce que le HTML ?_

## Que sont les éléments HTML ?

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-11-at-1.16.34-PM.png)
_Éléments HTML_

L'élément commence généralement par une balise d'ouverture, qui contient le nom de l'élément. Elle est entourée de chevrons ouvrant et fermant. La balise d'ouverture indique où l'élément commence.

Semblable à la balise d'ouverture, la balise de fermeture est également entourée de chevrons. Mais elle inclut aussi une barre oblique avant le nom de l'élément.

Tout ce qui se trouve à l'intérieur des balises d'ouverture et de fermeture est le contenu.

Mais tous les éléments ne suivent pas ce modèle. Nous appelons ceux qui ne le font pas des éléments vides. Ils ne consistent qu'en une seule balise ou une balise d'ouverture qui ne peut pas avoir de contenu. Ces éléments sont généralement utilisés pour insérer ou intégrer quelque chose dans le document.

Par exemple, l'élément `<img>` est utilisé pour intégrer un fichier image, ou l'élément `<input>` est utilisé pour insérer un champ de saisie sur la page.

```html
<img src="https://images.unsplash.com/photo-1610447847416-40bac442fbe6" width="50">
```

Dans l'exemple ci-dessus, l'élément `<img>` ne consiste qu'en une seule balise qui n'a pas de contenu. Cet élément est utilisé pour insérer un fichier image depuis [Unsplash](https://unsplash/) dans le document.

## Comment imbriquer les éléments HTML

```html
<div class="my-list">
  <h4>Ma liste :</h4>

  <ul>
     <li>Pomme</li>
     <li>Orange</li>
     <li>Banane</li>
  </ul>
</div>

```

Les éléments peuvent être placés à l'intérieur d'autres éléments. C'est ce qu'on appelle l'imbrication. Dans l'exemple ci-dessus, à l'intérieur de l'élément `<div>`, nous avons un élément `<h4>` et un élément `<ul>` ou élément de liste non ordonnée. Et de même, à l'intérieur de l'élément `<ul>`, il y a 3 éléments `<li>` ou éléments de liste.

L'imbrication de base est assez simple à comprendre. Mais quand la page s'agrandit, l'imbrication peut devenir compliquée. 

Par conséquent, avant de travailler avec le HTML, réfléchissez à la structure de mise en page que vous aimeriez avoir. Vous pouvez la dessiner sur un morceau de papier ou dans votre esprit. Cela aidera beaucoup.

![Comment imbriquer les éléments HTML](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-12-at-10.45.05-AM.png)

## Que sont les attributs HTML ?

Les éléments ont également des attributs, qui contiennent des informations supplémentaires sur l'élément qui n'apparaîtront pas dans le contenu.

```html
<img src="https://images.unsplash.com/photo" width="50">
```

Dans l'exemple ci-dessus, l'élément `<img>` possède 2 attributs : `src` ou source pour spécifier le chemin de l'image, et `width` pour spécifier la largeur de l'image en pixels.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-12-at-10.45.17-AM.png)

Avec cet exemple, vous pouvez voir les caractéristiques suivantes des attributs :

* Il y a un espace entre les attributs et le nom de l'élément
* Les attributs sont ajoutés dans la balise d'ouverture
* Les éléments peuvent avoir plusieurs attributs
* Les attributs ont généralement un nom et une valeur : nom=“valeur”

Mais tous les attributs n'ont pas le même modèle. Certains peuvent exister sans valeurs, et nous les appelons attributs booléens. 

```html
<button onclick=“alert('Envoyer')" disabled>Bouton</button>
```

Dans cet exemple, si nous voulons désactiver le bouton, tout ce que nous avons à faire est de passer un attribut `disabled` sans aucune valeur. Cela signifie que la présence de l'attribut représente la valeur vraie, sinon, l'absence représente la valeur fausse.

### Éléments HTML courants

Il existe au total plus de 100 éléments. Mais 90 % du temps, vous n'en utiliserez qu'environ 20 parmi les plus courants. Je les ai classés en 5 groupes :

#### Éléments de section

```html
  <div>, <span>, <header>, <footer>, <nav>, <main>, <section> 

```

Ces éléments sont utilisés pour organiser le contenu en différentes sections. Ils sont généralement explicites, par exemple, `<header>` représente généralement un groupe de la section d'introduction et de navigation, `<nav>` représente la section qui contient les liens de navigation, et ainsi de suite.

#### Contenu textuel

```html
  <h1> à <h6>, <p>, <div>, <span>, <ul>, <ol>, <li>

```

Ces éléments sont utilisés pour organiser le contenu ou les blocs de texte. Ils sont importants pour l'accessibilité et le SEO. Ils indiquent au navigateur le but ou la structure du contenu.

#### Formulaires

```html
  <form>, <input>, <button>, <label>, <textarea>

```

Ces éléments peuvent être utilisés ensemble pour créer des formulaires que les utilisateurs peuvent remplir et soumettre. Les formulaires sont peut-être la partie la plus délicate du HTML.

#### Images et Liens

```html
  <img>, <a>

```

Ces éléments sont utilisés pour insérer une image ou créer un lien hypertexte.

#### Autres

```html
  <br>, <hr>

```

Ces éléments sont utilisés pour ajouter un saut de ligne ou une ligne de séparation à la page web.

Vous pouvez trouver tous les éléments sur [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/HTML/Element). Mais pour les débutants, vous avez juste besoin de connaître les plus courants.

## Éléments HTML de niveau bloc vs en ligne

Par défaut, un élément peut être soit de niveau bloc, soit un élément en ligne.

Les éléments de niveau bloc sont les éléments qui commencent toujours sur une nouvelle ligne et occupent toute la largeur disponible.

Les éléments en ligne sont les éléments qui ne commencent pas sur une nouvelle ligne et n'occupent que la largeur nécessaire.  


![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screen-Shot-2021-01-11-at-1.17.22-PM.png)
_Éléments HTML de niveau bloc vs en ligne_

Deux éléments qui représentent respectivement les éléments de niveau bloc et en ligne sont `<div>` et `<span>`. Dans cet exemple, vous pouvez voir que les éléments `<div>` occupent 3 lignes, tandis que l'élément `<span>` n'occupe qu'une seule ligne.

Mais la question est : comment savoir lesquels sont des éléments de niveau bloc et lesquels sont des éléments en ligne ? Eh bien, malheureusement, vous devez les mémoriser. Le moyen le plus simple est de se rappeler quels sont les éléments en ligne – et le reste sont des éléments de bloc.

Si nous regardons à nouveau les éléments HTML les plus courants, les éléments en ligne incluent : `<span>, <input>, <button>, <label>, <textarea>, <img>, <a>, <br>`.

## Comment commenter en HTML

```html
<p>Ceci est un paragraphe.</p>

<!-- <p>Je ne m'affiche pas.</p> -->

```

Le but des commentaires est d'inclure des notes dans le code pour expliquer votre logique ou simplement pour organiser votre code. 

Les commentaires HTML sont entourés de marqueurs spéciaux : `<!-- et -->` et ils sont ignorés par le navigateur.

## Comment utiliser les entités HTML

Et si vous voulez afficher le texte : `la balise <p> définit un paragraphe.`, mais que le navigateur interprète `<p>` comme une balise d'ouverture pour un nouvel élément ? Dans ce cas, nous pouvons utiliser des entités HTML comme dans l'exemple suivant :

```html
<p>la balise <p> définit un paragraphe.</p>

<p>la balise &lt;p&gt; définit un paragraphe.</p>

```

## Comment utiliser les emojis en HTML

Sur le web moderne, nous pouvons afficher des emojis en HTML assez facilement, comme ceci : 👻

```html
<p>😀 Visage souriant.</p>

<p>🎂 Anniversaire</p>

```

## Erreurs courantes de débutant en HTML

### 1. Noms des balises/éléments

Les noms des balises/éléments sont insensibles à la casse. Cela signifie qu'ils peuvent être écrits en minuscules ou en majuscules, mais il est recommandé de tout écrire en minuscules : `<button>` et non `<ButTon>`.

### 2. Balise de fermeture

Oublier d'inclure une balise de fermeture est une erreur courante de débutant. Par conséquent, chaque fois que vous créez une balise d'ouverture, insérez immédiatement une balise de fermeture.

### 3. Imbrication

Ceci est incorrect :

```html
<div>Div 1 <span> Span 2 </div></span>

```

Les balises doivent s'ouvrir et se fermer de manière à être à l'intérieur ou à l'extérieur les unes des autres.

### 4. Guillemets simples et guillemets doubles

Ceci est incorrect :

```html
<img src="https://images.unsplash.com/'>

```

Vous ne pouvez pas mélanger les guillemets simples et les guillemets doubles. Vous devriez toujours utiliser des guillemets doubles et utiliser des entités HTML si nécessaire.

## Comment construire un site web simple avec HTML

Les éléments HTML individuels ne suffisent pas pour créer un site web. Voyons donc ce dont nous avons besoin de plus pour construire un site web simple à partir de zéro.

### Comment créer un document HTML

Tout d'abord, ouvrons [Visual Studio Code](https://code.visualstudio.com/) (ou votre éditeur de code préféré). Dans le dossier de votre choix, créez un nouveau fichier et nommez-le index.html.

Dans le fichier index.html, tapez ! (point d'exclamation) et appuyez sur entrée. Vous verrez quelque chose comme ceci :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>

```

C'est le code minimal qu'un document HTML devrait avoir pour constituer un site web. Et ici nous avons :

1. `<!DOCTYPE html>` : D'abord, nous avons le Doctype. Pour une raison historique étrange en HTML, nous devons inclure le doctype pour que tout fonctionne correctement.
2. `<html lang="fr"></html>` : L'élément `<html>` enveloppe tout le contenu de la page, également connu sous le nom d'élément racine. Et nous devrions toujours inclure l'attribut `lang` pour déclarer la langue de la page.
3. `<head></head>` : L'élément `<head>` est un conteneur pour tout ce que vous voulez inclure, mais pas le contenu que vous montrez à vos utilisateurs.
4. `<meta charset="UTF-8" />` : Le premier élément meta est utilisé pour définir le jeu de caractères sur UTF-8, qui inclut la plupart des caractères des langues écrites.
5. `<meta name="viewport" content="width=device-width, initial-scale=1.0" />` : Le deuxième élément meta spécifie le viewport du navigateur. Ce paramètre est destiné à un site optimisé pour les mobiles.
6. `<title>Document</title>` : C'est l'élément `<title>`. Il définit le titre de la page.
7.  `<body></body>` : L'élément `<body>` contient tout le contenu de la page.

### Comment construire une page de recette de pancakes

Très bien, maintenant que nous avons le code de départ, construisons une page de recette de pancakes. Nous allons utiliser le contenu de cette [page AllRecipes](https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/).

Tout d'abord, donnons à l'élément `<title>` le contenu de la recette de pancakes. Vous verrez le texte sur l'onglet de la page web changer. Dans l'élément `<body>`, créons 3 éléments : `<header>`, `<main>` et `<footer>` représentant 3 sections.

#### 1. Construire la section d'en-tête

Dans l'en-tête, nous voulons avoir le logo et la navigation. Par conséquent, créons un `div` avec le contenu `TOUTES LES RECETTES` pour le logo.

Pour la navigation, utilisons l'élément `<nav>`. À l'intérieur de l'élément `<nav>`, nous pouvons utiliser `<ul>` pour créer une liste non ordonnée. Nous voulons avoir 3 éléments `<li>` pour 3 liens : Ingrédients, Étapes et S'abonner. Le code de l'en-tête ressemble à ceci :

```html
...
    <header>
      <div>TOUTES LES RECETTES</div>
      <nav>
        <ul>
          <li><a href="#ingredients">Ingrédients</a></li>
          <li><a href="#etapes">Étapes</a></li>
          <li><a href="#sabonner">S'abonner</a></li>
        </ul>
      </nav>
    </header>
...

```

#### 2. Construire la section principale

Dans la section principale, nous voulons d'abord avoir un titre et une image. Nous pouvons utiliser `h1` pour le titre et `<img>` pour l'image (nous pouvons utiliser gratuitement une image d' [Unsplash](https://images.unsplash.com/)) :

```html
...
    <main>
      <h1>Pancakes classiques à l'ancienne</h1>
      <img
        src="https://images.unsplash.com/photo-1575853121743-60c24f0a7502"
        alt="pancake"
        width="250"
      />
    </main>
...

```

Ensuite, nous voulons lister tous les ingrédients. Nous pouvons utiliser `<ol>` pour créer une liste ordonnée et `<input type="checkbox" />` pour créer une case à cocher.

Mais avant cela, nous pouvons utiliser `<h2>` pour commencer un nouveau bloc de contenu. Nous voulons également ajouter l'attribut `id` pour `<h2>` afin que le lien dans la navigation sache où aller :

```html
...
    <main>
    ...
      <h2 id="ingredients">Ingrédients</h2>
      <ol>
        <li><input type="checkbox" /> 1 ½ tasses de farine tout usage</li>
        <li><input type="checkbox" /> 3 ½ cuillères à café de levure chimique</li>
        <li><input type="checkbox" /> 1 cuillère à café de sel</li>
        <li><input type="checkbox" /> 1 cuillère à soupe de sucre blanc</li>
        <li><input type="checkbox" /> 1 ¼ tasse de lait</li>
        <li><input type="checkbox" /> 1 œuf</li>
      </ol>
    </main>
...

```

Après les ingrédients, nous voulons lister toutes les étapes. Nous pouvons utiliser `<h4>` pour le titre de l'étape et `<p>` pour le contenu de l'étape :

```html
...
    <main>
    ...
      <h2 id="etapes">Étapes</h2>
      
      <h4>Étape 1</h4>
      <p>
        Dans un grand bol, tamisez ensemble la farine, la levure chimique, le sel et le sucre.
        Faites un puits au centre et versez-y le lait, l'œuf et le beurre fondu ;
        mélangez jusqu'à l'obtention d'une pâte lisse.
      </p>
      
      <h4>Étape 2</h4>
      <p>
        Faites chauffer une plaque chauffante ou une poêle légèrement huilée à feu moyen-vif. Versez
        ou déposez la pâte sur la plaque, en utilisant environ 1/4 de tasse pour
        chaque pancake. Faites dorer des deux côtés et servez chaud.
      </p>
    </main>
...

```

Très bien, maintenant que nous en avons terminé avec la section principale, passons à la section du pied de page.

#### 3. Construire la section de pied de page

Dans le pied de page, nous voulons avoir un formulaire d'abonnement et un texte de copyright.

Pour le formulaire d'abonnement, nous pouvons utiliser l'élément `<form>`. À l'intérieur, nous pouvons avoir un `<input type="text">` pour la saisie de texte et un `<button>` pour le bouton d'envoi.

Pour le texte de copyright, nous pouvons simplement utiliser un `<div>`. Notez qu'ici, nous pouvons utiliser l'entité HTML `&copy;` pour le symbole du copyright.

Nous pouvons ajouter `<br>` pour ajouter de l'espace entre le formulaire d'abonnement et le texte du copyright :

```html
...
    <footer>
      <h6 id="sabonner">S'abonner</h6>
      <form onsubmit="alert('Inscrit')">
        <input type="text" placeholder="Entrez votre adresse e-mail" />
        <button>Envoyer</button>
      </form>
      <br />
      <div>&copy; dakota kelly sur Allrecipe.com</div>
    </footer>
...

```

Très bien, maintenant nous avons terminé ! Voici le code complet pour référence :

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Recette de pancakes</title>
  </head>
  <body>
    <header>
      <div>TOUTES LES RECETTES</div>
      <nav>
        <ul>
          <li><a href="#ingredients">Ingrédients</a></li>
          <li><a href="#etapes">Étapes</a></li>
          <li><a href="#sabonner">S'abonner</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <h1>Pancakes classiques à l'ancienne</h1>
      <img
        src="https://images.unsplash.com/photo-1575853121743-60c24f0a7502?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8cGFuY2FrZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=60"
        alt="pancake"
        width="250"
      />
      <h2 id="ingredients">Ingrédients</h2>
      <ol>
        <li><input type="checkbox" /> 1 ½ tasses de farine tout usage</li>
        <li><input type="checkbox" /> 3 ½ cuillères à café de levure chimique</li>
        <li><input type="checkbox" /> 1 cuillère à café de sel</li>
        <li><input type="checkbox" /> 1 cuillère à soupe de sucre blanc</li>
        <li><input type="checkbox" /> 1 ¼ tasse de lait</li>
        <li><input type="checkbox" /> 1 œuf</li>
      </ol>
      <h2 id="etapes">Étapes</h2>
      <h4>Étape 1</h4>
      <p>
        Dans un grand bol, tamisez ensemble la farine, la levure chimique, le sel et le sucre.
        Faites un puits au centre et versez-y le lait, l'œuf et le beurre fondu ;
        mélangez jusqu'à l'obtention d'une pâte lisse.
      </p>
      <h4>Étape 2</h4>
      <p>
        Faites chauffer une plaque chauffante ou une poêle légèrement huilée à feu moyen-vif. Versez
        ou déposez la pâte sur la plaque, en utilisant environ 1/4 de tasse pour
        chaque pancake. Faites dorer des deux côtés et servez chaud.
      </p>
    </main>
    <hr />
    <footer>
      <h6 id="sabonner">S'abonner</h6>
      <form onsubmit="alert('Inscrit')">
        <input type="text" placeholder="Entrez votre adresse e-mail" />
        <button>Envoyer</button>
      </form>
      <br />
      <div>&copy; dakota kelly sur Allrecipe.com</div>
    </footer>
  </body>
</html>

```

## Conclusion

Vous pouvez construire un site web simple avec juste du HTML. Mais pour être capable de construire des sites web beaux et fonctionnels, vous devez étudier le CSS et le JavaScript. 

Vous pouvez me suivre sur les réseaux sociaux ou sur YouTube pour les futures mises à jour sur ces sujets. Mais en attendant, vous pouvez consulter le [programme freeCodeCamp](https://www.freecodecamp.org/learn) pour pratiquer le HTML en résolvant de petites tâches. 

Sinon, bon codage à tous et à bientôt dans de futurs articles 👋.  
  
__________ 🐣 À propos de moi __________

* Je suis le fondateur de [DevChallenges](https://devchallenges.io/)
* Abonnez-vous à [ma chaîne](https://www.youtube.com/c/thunghiem)
* Suivez [mon Twitter](https://twitter.com/thunghiemdinh)
* Rejoignez [Discord](https://discord.com/invite/3R6vFeM)