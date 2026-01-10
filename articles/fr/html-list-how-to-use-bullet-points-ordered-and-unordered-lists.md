---
title: Liste HTML – Comment utiliser les puces, les listes ordonnées et non ordonnées
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-07-01T18:02:56.000Z'
originalURL: https://freecodecamp.org/news/html-list-how-to-use-bullet-points-ordered-and-unordered-lists
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/freeCodeCamp-Cover-1.png
tags:
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Liste HTML – Comment utiliser les puces, les listes ordonnées et non ordonnées
seo_desc: 'Listing items on a web page is a common task you''ll have to do as a web
  developer. You may have to list shopping cart items, the order of students based
  on their grades, dogs with the loudest bark – and so on.

  So you need to know the different ways y...'
---

Lister des éléments sur une page web est une tâche courante que vous devrez effectuer en tant que développeur web. Vous devrez peut-être lister des articles dans un panier, l'ordre des étudiants en fonction de leurs notes, des chiens avec l'aboiement le plus fort – et ainsi de suite.

Vous devez donc connaître les différentes façons de lister des éléments en utilisant HTML. Bien que vous puissiez penser que c'est une chose triviale à apprendre, c'est important. Et c'est l'une des fonctionnalités les plus couramment utilisées de HTML en développement web.

Dans cet article, vous apprendrez tout sur les éléments de liste HTML, leurs propriétés, leur style et comment les utiliser pour créer des listes soignées. J'espère que vous le trouverez utile.

# Comment créer des listes en HTML

En HTML, nous pouvons lister des éléments soit de manière ordonnée, soit non ordonnée.

Une liste ordonnée utilise des nombres ou une sorte de notation qui indique une série d'éléments.

Par exemple, une liste ordonnée peut commencer par le nombre 1, et continuer à travers 2, 3, 4, et ainsi de suite. Votre liste ordonnée peut également commencer par la lettre A et passer par B, C, D, et ainsi de suite.

Voici un exemple de liste ordonnée avec les noms et les notes des étudiants.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/ordered-1.png)
_Liste ordonnée d'étudiants_

D'autre part, nous avons des listes non ordonnées, comme une liste de choses à faire par exemple. Ici, je suis si passionné par le codage que j'ai sauté mon petit-déjeuner 🥱.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/unordered-1.png)
_Liste de choses à faire non ordonnée_

Il existe un autre type de liste appelé `liste de description` que nous apprendrons également ci-dessous.

Maintenant, plongeons un peu plus dans les détails et voyons comment créer chaque type de liste en HTML.

# Comment créer une liste ordonnée avec HTML

En HTML, nous pouvons créer une liste ordonnée en utilisant la balise `<ol>`. Le `ol` dans la balise signifie une liste **o**rdonnée. À l'intérieur de chaque élément de liste ordonnée `<ol>` et `<ol />`, nous devons définir les éléments de la liste. Nous pouvons définir les éléments de la liste en utilisant la balise `<li>`.

Voici la structure HTML complète pour une liste ordonnée :

```html
<ol>
  <li>Manger</li>
  <li>Coder</li>
  <li>Dormir</li>
</ol>
```

Le résultat de la liste ordonnée ci-dessus est :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image.png)

Nous avons donc la liste des éléments ordonnés avec un nombre commençant par 1 et incrémenté à 2 et 3. Essayez ce CodePen et voyez si vous pouvez changer et jouer avec l'utilisation de `ol-li`.

%[https://codepen.io/atapas/pen/gOWpbMK]

### Types de listes ordonnées en HTML

Que faire si vous ne souhaitez pas ordonner votre liste par nombre ? Au lieu de cela, vous souhaitez ordonner en utilisant l'alphabet comme A, B, C ou a, b, c. Vous pouvez le faire en spécifiant la valeur de l'attribut `type` de la balise `<ol>`.

Vous pouvez ordonner la liste en utilisant les lettres A, B, C en passant `A` comme valeur de type.

```html
<ol type="A">
  <li>Manger</li>
  <li>Coder</li>
  <li>Dormir</li>
</ol>
```

Le résultat ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-10.png)

De même, vous pouvez utiliser des lettres minuscules comme `a` comme valeur de type pour lister les éléments avec a, b, c, et ainsi de suite.

```html
<ol type="a">
  <li>Manger</li>
  <li>Coder</li>
  <li>Dormir</li>
</ol>
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-2.png)

Si vous souhaitez utiliser des chiffres romains, utilisez la valeur `I` pour une liste ordonnée avec des chiffres romains :

```html
<ol type="I">
  <li>Manger</li>
  <li>Coder</li>
  <li>Dormir</li>
</ol>
```

Le résultat ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-3.png)

Consultez le CodePen ci-dessous pour essayer d'autres types :

%[https://codepen.io/atapas/pen/LYyVEbL]

## Comment utiliser l'attribut Start dans les listes HTML

L'élément `<ol>` possède un attribut intéressant appelé `start`. Vous pouvez spécifier une valeur à l'attribut start pour commencer la liste ordonnée à partir d'un nombre spécifique.

Supposons que vous souhaitez commencer la liste avec le nombre `30` au lieu de `1`. Vous pouvez spécifier le nombre `30` comme valeur de l'attribut `start` comme ceci :

```html
<ol start="30">
  <li>Trente</li>
  <li>Trente et un</li>
  <li>Trente-deux</li>
</ol>
```

Le résultat ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-4.png)

N'hésitez pas à jouer avec l'attribut `start` en utilisant ce CodePen :

%[https://codepen.io/atapas/pen/VwbLYzQ]

D'ailleurs, j'ai partagé les mêmes conseils sur Twitter récemment. Vous pourriez y trouver une discussion intéressante également :

%[https://twitter.com/tapasadhikary/status/1410508936344588289]

# Comment créer une liste non ordonnée en HTML

Passons maintenant aux listes non ordonnées. Nous utilisons la balise `<ul>` pour créer une liste non ordonnée. Comme d'habitude, nous devons utiliser les balises `<li>` à l'intérieur de `<ul>` et `<ul/>` pour créer les éléments de la liste.

Les éléments de la liste (`li`) à l'intérieur de la liste non ordonnée (`ul`) viennent avec le style par défaut des puces – chaque élément de la liste est précédé d'un point noir.

Créons une liste de mes ressources en ligne préférées pour apprendre la programmation web :

```html
Mes sites préférés pour apprendre le développement web
<div>
  <ul>
    <li>freeCodeCamp</li>
    <li>CSS-Tricks</li>
    <li>Traversy Media</li>
  </ul>
</div>
```

Le résultat ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-5.png)

Vous pouvez voir les puces pour chaque élément de la liste ci-dessus, mais vous pouvez les personnaliser. Nous apprendrons cela également.

Mais avant cela, n'hésitez pas à utiliser ce CodePen pour changer et exécuter le code.

%[https://codepen.io/atapas/pen/zYwxgJw]

## Comment utiliser les puces avec des liens dans les listes HTML

Nous pouvons utiliser les liens (balise d'ancrage `<a>`) dans les éléments de la liste (`<li>`) pour lier chaque élément à des pages web internes ou externes.

Voici un exemple qui vous montre comment lier chaque ressource de programmation web à leurs sites respectifs :

```html
Mes sites préférés pour apprendre le développement web
<div>
  <ul>
    <li>
      <a href="https://www.freecodecamp.org/" target="_blank">freeCodeCamp</a>
    </li>
    <li>
      <a href="https://css-tricks.com/" target="_blank">CSS-Tricks</a>
    </li>
    <li>
      <a href="https://www.traversymedia.com/" target="_blank">Traversy Media</a>
    </li>
  </ul>
</div>
```

Le résultat ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-6.png)

Vous pouvez utiliser le CodePen ci-dessous pour essayer la même chose. N'hésitez pas à le modifier comme vous le souhaitez :

%[https://codepen.io/atapas/pen/yLbNBmj]

## Types de listes non ordonnées en HTML

Comme nous l'avons brièvement discuté, nous pouvons personnaliser le style des puces d'une liste non ordonnée, ce que nous allons voir en action maintenant. Nous pouvons le faire en utilisant la propriété de style CSS appelée `list-style`.

Il existe quatre valeurs principales de la propriété `list-style` qui nous aident à cette personnalisation :

| list-style      | Effet  |
| -------------   | -----:|
| none            | Il n'y aura pas de puces apparaissant devant l'élément de la liste |
| circle          | Une puce circulaire (creuse) apparaît devant l'élément de la liste   |
| disc            | C'est la puce circulaire remplie par défaut     |
| square          | Une puce carrée remplie apparaît devant l'élément de la liste |

%[https://codepen.io/atapas/pen/vYmOYyK]

Vous pouvez utiliser le CodePen ci-dessus pour essayer différentes options de `list-style`.

# Le saviez-vous – Il existe également une liste de description ?

Il existe un autre type de liste HTML, mais il n'est pas utilisé aussi souvent. Il s'agit de la `liste de description`.

Nous pouvons définir une liste de description en utilisant l'élément de balise `<dl>`. À l'intérieur de `<dl>..</dl>`, nous devons définir un terme de description en utilisant la balise `<dt>`. Le terme est généralement un petit texte sur quelque chose. Ensuite, nous pouvons définir le descripteur de description pour décrire davantage le terme en utilisant la balise `<dd>`.

Trop à digérer ? Voyons comment cela fonctionne avec un exemple de code.

Supposons que nous voulons décrire certaines informations sur le codage, les commérages et le sommeil sur notre page web. Nous pouvons d'abord définir une balise `<dl>`. Maintenant, nous définissons trois paires de balises `<dt>` et `<dd>` pour décrire respectivement le codage, les commérages et le sommeil.

```html
<dl>
  <dt>Codage</dt>
  <dd>Une activité pour vous garder heureux, même en dormant.</dd>
  <dt>Commérages</dt>
  <dd>On ne peut pas vivre sans.</dd>
  <dt>Sommeil</dt>
  <dd>Mon préféré de tous les temps.</dd>
</dl>
```

Le résultat ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-7.png)

Essayez ce CodePen pour expérimenter davantage avec les listes de description :

%[https://codepen.io/atapas/pen/xxdGbzL]

Vous devez vous demander, pourquoi n'utilisons-nous pas ce type de liste beaucoup ? Eh bien, vous pouvez créer cette structure en utilisant la liste non ordonnée (ul), les éléments de liste (li) et les styles CSS.

Mais si vous considérez la sémantique HTML, vous devriez donner une place aux listes de description dans votre code lorsque vous avez un bon cas d'utilisation pour cela.

# Comment créer un en-tête de page avec des éléments de liste HTML

Nous sommes presque à la fin de ce tutoriel. Mais j'ai l'impression qu'il est incomplet sans au moins un exemple de cas d'utilisation des listes et balises HTML. Mon préféré est de lister les éléments dans l'en-tête d'une page web.

Créons un en-tête très basique avec un logo d'exemple et trois liens : `Accueil`, `Produits` et `À propos`. Nous allons d'abord créer la structure HTML comme ceci :

```html
<nav>
  <span class="logo">Logo</span>
  
  <ul>
    <li><a href="#/accueil">Accueil</a></li>
    <li><a href="#/produits">Produits</a></li>
    <li><a href="#/apropos">À propos</a></li>
  </ul>  
</nav>
```

Ici, nous avons pris une liste non ordonnée avec trois éléments de liste pour définir les liens Accueil, Produits et À propos. Vous remarquerez également un élément span avec le texte Logo qui indique qu'il s'agit d'un logo. Nous pouvons utiliser une image appropriée là, en fonction de nos besoins plus tard.

Jusqu'à présent, l'en-tête devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-8.png)

Eh bien, ce n'est pas ce que nous voulons. Nous allons donc écrire quelques règles et propriétés CSS pour lui donner l'apparence d'un en-tête de page (au moins proche de cela).

```css
nav{
  background-color: #273032;
  color: #FFF;
  padding: 10px;
  display: flex;
}

.logo {
  background-color: blue
}

ul {
  margin: 0px;
}

li {
  list-style: none;
  display: inline;
  margin-right: 0.2rem;
}

a {
  color: pink;
}
```

Maintenant, c'est beaucoup mieux et cela ressemble davantage à un en-tête de page réaliste.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-9.png)

Encore une fois, vous pouvez utiliser ce CodePen pour changer et essayer des choses avec l'en-tête.

%[https://codepen.io/atapas/pen/OJmVPGe]

# Avant de terminer...

C'est tout pour l'instant. J'espère que vous avez trouvé cet article perspicace et qu'il vous aide à comprendre les listes HTML plus clairement. Vous pouvez trouver tous les exemples ensemble dans cette [Collection CodePen](https://codepen.io/collection/jbOYRo?sort_by=item_created_at&grid_type=list).

Restons en contact. Vous me trouverez actif sur [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary). N'hésitez pas à me suivre. J'ai également commencé à partager des connaissances en utilisant ma [chaîne YouTube](https://youtube.com/c/TapasAdhikary?sub_confirmation=1), alors n'hésitez pas à la consulter également.

Vous pourriez également aimer ces articles :

* [10 astuces DevTools pour vous aider avec CSS et la conception UX](https://blog.greenroots.info/10-devtools-tricks-to-help-you-with-css-and-ux-design-ckpp7mtnu04u6whs143e7huwx)
* [10 faits HTML triviaux mais puissants que vous devez connaître](https://blog.greenroots.info/10-trivial-yet-powerful-html-facts-you-must-know-ckmx0d7q30346c1s125iydcsa)
* [10 fonctionnalités HTML5 utiles que vous n'utilisez peut-être pas](https://blog.greenroots.info/10-useful-html5-features-you-may-not-be-using-ckdua7ql300l1m3s1ez7teshc)