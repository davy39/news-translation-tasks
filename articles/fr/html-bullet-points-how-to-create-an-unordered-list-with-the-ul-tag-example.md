---
title: Points à puces HTML – Comment créer une liste non ordonnée avec l'exemple de
  la balise <ul>
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-09-30T17:31:40.000Z'
originalURL: https://freecodecamp.org/news/html-bullet-points-how-to-create-an-unordered-list-with-the-ul-tag-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-breakingpic-3243.jpg
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Points à puces HTML – Comment créer une liste non ordonnée avec l'exemple
  de la balise <ul>
seo_desc: 'We use lists all the time in our everyday lives.

  We create them to structure and organize our days, and we use them to make to-do
  lists. We use them in recipes so we don''t miss any of the steps. And we use them
  when we want to assemble a piece of fur...'
---

Nous utilisons des listes tout le temps dans notre vie quotidienne.

Nous les créons pour structurer et organiser nos journées, et nous les utilisons pour faire des listes de tâches. Nous les utilisons dans les recettes pour ne pas manquer d'étapes. Et nous les utilisons lorsque nous voulons assembler un meuble. 

Ce ne sont là que quelques exemples de la manière dont nous utilisons les listes pour nous aider à garder les choses organisées.

Il est donc logique qu'elles soient également une fonctionnalité si fréquemment utilisée et utile dans le développement web front-end.

Il existe trois types de listes en HTML : non ordonnées, ordonnées et listes de description.

Dans cet article, vous apprendrez à créer des listes non ordonnées. Vous verrez également quelques façons de modifier le style par défaut en utilisant seulement quelques lignes de CSS.

Commençons !

## Comment créer une liste non ordonnée en HTML

Les listes non ordonnées en HTML sont des collections d'éléments qui n'ont pas besoin d'être dans un ordre spécifique. Nous utilisons souvent de simples points pour lister ces éléments.

Vous créez une liste non ordonnée en utilisant la balise `ul`. Ensuite, vous utilisez la balise `li` pour lister chaque élément que vous souhaitez inclure dans votre liste.

La balise `ul`, qui signifie *unordered list* (liste non ordonnée), est le parent de la balise `li`. Cela signifie que la balise `li` est l'*enfant* de la balise `ul*.


```html
<ul>
    <li>Élément</li>
    <li>Un autre élément</li>
    <li>Encore un autre élément</li>
</ul>
```

Résultat :

![Screenshot-2021-09-30-at-4.43.47-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-30-at-4.43.47-PM.png)

Cela s'appelle une liste à puces car le style par défaut est que chaque élément de la liste a un point à côté.

Une chose à retenir et à garder à l'esprit est que `li` est le *seul* enfant direct de `ul`.

Cela signifie qu'après avoir créé les balises d'ouverture (`<ul>`) et de fermeture (`</ul>`) pour la liste non ordonnée, la première balise que vous inclurez sera la balise `li`.

Par exemple, **ne faites pas ceci** :

```html
<ul>
    <a href="#">Je suis un lien vers quelque chose sur le web !</a>
</ul>
```

Si vous voulez que les éléments de votre liste non ordonnée soient des liens, faites ceci à la place :

```html
<ul>
    <li>
        <a href="#">Je suis un lien vers quelque chose sur le web !</a>
    </li>
</ul>
```


La balise de lien (`a`) est l'enfant de la balise `li` et le petit-enfant (!) de la balise `ul`.


### Comment créer une liste non ordonnée imbriquée

Une liste imbriquée est une liste à l'intérieur d'une autre liste. 

Vous pouvez créer une liste non ordonnée imbriquée, ou une liste ordonnée imbriquée, ou même une liste ordonnée imbriquée à l'intérieur d'une liste non ordonnée.

Rappelez-vous que le *seul* enfant direct de la balise `ul` est `li`.

Voici comment vous créez une liste non ordonnée imbriquée :

```html
<ul><!-- début de la liste principale-->
  <li>HTML</li>
   <li>CSS</li>
    <li>JavaScript
            <ul><!-- début de la liste imbriquée-->
                <li>Angular</li>
                <li>React</li>
                <li>Vue</li>
            </ul><!--fin de la liste imbriquée-->
     </li>
 </ul><!--fin de la liste principale -->
```


Résultat :

![Screenshot-2021-09-30-at-5.33.53-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-30-at-5.33.53-PM.png)


Vous créez la liste non ordonnée imbriquée sous l'élément de la liste principale de votre choix.

Dans l'exemple ci-dessus, j'ai créé une liste imbriquée entre les balises d'ouverture et de fermeture `li` qui contient le nom 'JavaScript'. 

Assurez-vous d'inclure à la fois la balise de fermeture et les balises d'ouverture, car cela peut devenir rapidement confus. 

Une bonne pratique pour éviter toute confusion est de commenter votre code. Et gardez à l'esprit que vous devriez utiliser des listes imbriquées uniquement lorsque cela a du sens *sémantiquement*.

## Comment modifier le style par défaut des listes non ordonnées

Comme vous l'avez vu jusqu'à présent, le style par défaut des listes non ordonnées est des points à côté de chaque élément de la liste.

Mais vous pouvez modifier le style en utilisant la propriété `list-style-type` dans un fichier `.css` séparé.

La valeur par défaut de la propriété est `disc`.

### Comment styliser les éléments de liste avec des cercles

Vous pouvez créer des éléments de liste qui ont des cercles au lieu de points pleins comme style :

```html
<ul>
    <li>Élément</li>
    <li>Un autre élément</li>
    <li>Encore un autre élément</li>
</ul>
```

```css
ul {
    list-style-type: circle;
}
```

Résultat :

![Screenshot-2021-09-30-at-5.50.17-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-30-at-5.50.17-PM.png)

### Comment styliser les éléments de liste avec des carrés

Vous pouvez également créer des éléments de liste qui ont des carrés comme style :

```html
<ul>
    <li>Élément</li>
    <li>Un autre élément</li>
    <li>Encore un autre élément</li>
</ul>
```


```css
ul {
    list-style-type: square;
}
```

Résultat :

![Screenshot-2021-09-30-at-6.03.39-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-30-at-6.03.39-PM.png)

### Comment supprimer les styles des éléments de liste

Vous pouvez même supprimer le style complètement :

```html
<ul>
    <li>Élément</li>
    <li>Un autre élément</li>
    <li>Encore un autre élément</li>
</ul>
```


```css
ul {
    list-style-type: none;
}
```

Résultat :

![Screenshot-2021-09-30-at-6.05.01-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-30-at-6.05.01-PM.png)


Cela est particulièrement utile lorsque vous voulez styliser les éléments de liste horizontalement et créer une barre de navigation. Cela nécessitera un peu de style supplémentaire.

Les listes sont des éléments **block**. En changeant les éléments de liste en `inline` et en utilisant une règle Flexbox, vous pouvez faire en sorte que les éléments s'empilent les uns à côté des autres.

Le même HTML :
```html
<ul>
        <li>Élément</li>
        <li>Un autre élément</li>
        <li>Encore un autre élément</li>
    </ul>
```

Et en ajoutant quelques nouvelles règles CSS :

```css
ul {
    list-style-type: square;
    display:flex;
}

li{
    display:block;
    margin:10px;
}
```

Vous pouvez styliser les éléments de liste horizontalement :

![Screenshot-2021-09-30-at-6.15.40-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-30-at-6.15.40-PM.png)

### Comment styliser les éléments de liste avec des emojis

Vous n'avez pas autant de choix de style pour styliser les éléments dans une liste non ordonnée.

Pour rendre les listes plus intéressantes et amusantes, vous pouvez ajouter des emojis, en utilisant le pseudo-élément CSS `::before`.

Voici le HTML :

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

La première étape consiste à ajouter la règle `list-style-type:none;` à la balise parente `ul` et à supprimer le `padding` et la `margin` par défaut de la balise.

Vous ajoutez l'emoji à la balise `li` en utilisant le pseudo-élément `::before`. Vous pouvez choisir parmi une liste complète d'emojis dans [cet article](https://www.freecodecamp.org/news/all-emojis-emoji-list-for-copy-and-paste/).

```css
ul {
    list-style-type: none;
    padding:0;
    margin:0;
}

li::before{
    content: "💻";
}
```

Résultat :

![Screenshot-2021-09-30-at-6.28.49-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-30-at-6.28.49-PM.png)

Pour donner à chaque élément de liste un emoji différent, utilisez le sélecteur `:nth-child()` sur l'élément de liste *avant* le pseudo-élément `::before` :

```css
ul {
    list-style-type: none;
    padding:0;
    margin:0;
}

/*premier élément de liste*/
li:nth-child(1)::before{
    content: "✏️";
}

/*deuxième élément de liste*/
li:nth-child(2)::before{
    content: "🎨";
}

/*troisième élément de liste*/
li:nth-child(3)::before{
    content: "🔥";
}
```

Résultat :

![Screenshot-2021-09-30-at-6.38.15-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-30-at-6.38.15-PM.png)

## Conclusion

Et voilà ! Vous savez maintenant comment créer des listes non ordonnées en HTML et vous avez vu quelques façons de les styliser.

Pour continuer votre apprentissage du HTML, regardez les vidéos suivantes sur la chaîne YouTube de freeCodeCamp :

- [Tutoriel HTML - Cours intensif sur la création de sites web pour débutants](https://www.youtube.com/watch?v=916GWv2Qs08)
- [Cours complet de HTML - Tutoriel pour créer un site web](https://www.youtube.com/watch?v=pQN-pnXPaVg)

freeCodeCamp propose également une certification gratuite basée sur des projets sur le [Design Web Réactif](https://www.freecodecamp.org/learn/responsive-web-design/).

Elle est idéale pour les débutants complets et ne suppose aucune connaissance préalable. Vous commencerez par les bases nécessaires et développerez vos compétences au fur et à mesure. À la fin, vous complèterez cinq projets.

Merci d'avoir lu et bon apprentissage 😊