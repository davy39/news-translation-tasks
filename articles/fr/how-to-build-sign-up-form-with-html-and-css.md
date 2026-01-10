---
title: Comment créer un formulaire d'inscription avec des étiquettes flottantes et
  des transitions en utilisant HTML et CSS simples
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-09-13T21:15:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-sign-up-form-with-html-and-css
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/floating-label.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: transitions
  slug: transitions
seo_title: Comment créer un formulaire d'inscription avec des étiquettes flottantes
  et des transitions en utilisant HTML et CSS simples
seo_desc: 'In this tutorial we are going to build a modern sign up form with floating
  labels and smooth transitions using plain HTML and CSS.


  A view

  As you can see in the above image, when an input within the form gains focus, its
  label floats to the top and a...'
---

Dans ce tutoriel, nous allons créer un formulaire d'inscription moderne avec des étiquettes flottantes et des transitions fluides en utilisant HTML et CSS simples.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/ezgif.com-gif-maker--9--2.gif align="left")

*Une vue*

Comme vous pouvez le voir dans l'image ci-dessus, lorsqu'un champ de saisie dans le formulaire reçoit le focus, son étiquette flotte vers le haut et une bordure semi-épaisse apparaît autour du champ. Si du texte est saisi dans le champ et que le champ perd le focus, l'étiquette reste en haut. Sinon, l'étiquette redescend dans le champ.

De nombreux formulaires modernes ont une sorte de transition appliquée. Non seulement ces transitions rendent le formulaire plus dynamique, mais elles aident également à guider l'utilisateur sur l'état du champ (c'est-à-dire s'il a le focus ou non) et quel type de données chaque champ est censé gérer.

Dans ce tutoriel, vous apprendrez quelques fonctionnalités CSS intéressantes comme les transitions, les sélecteurs comme `:placeholder_focus`, et bien d'autres propriétés CSS que vous devriez connaître.

Commençons !

## Le balisage HTML

Nous allons définir le balisage pour notre formulaire d'inscription. Mais avant cela, nous devons configurer notre modèle HTML de base et correctement lier notre feuille de style depuis la balise `head`. Vous pouvez facilement le faire avec le [plugin Emmet](https://emmet.io/) en tapant `!` puis tab dans votre IDE/éditeur de code.

Vous pouvez également copier ce modèle et le coller dans votre fichier `index.html` :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>

</body>
</html>
```

Dans la balise body, nous définissons le balisage pour notre formulaire d'inscription :

```html
<div class="signupFrm">
    <form action="" class="form">
      <h1 class="title">Inscription</h1>

      <div class="inputContainer">
        <input type="text" class="input" placeholder="a">
        <label for="" class="label">Email</label>
      </div>

      <div class="inputContainer">
        <input type="text" class="input" placeholder="a">
        <label for="" class="label">Nom d'utilisateur</label>
      </div>

      <div class="inputContainer">
        <input type="text" class="input" placeholder="a">
        <label for="" class="label">Mot de passe</label>
      </div>

      <div class="inputContainer">
        <input type="text" class="input" placeholder="a">
        <label for="" class="label">Confirmer le mot de passe</label>
      </div>

      <input type="submit" class="submitBtn" value="Inscription">
    </form>
  </div>
```

Nous créons un conteneur `div` pour contenir l'élément formulaire. Chacun des champs de saisie du formulaire, ainsi que son étiquette de texte, sont enveloppés dans un conteneur div. Les étiquettes servent à informer l'utilisateur des informations que chaque champ doit contenir.

Et notre page ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/noCSS.png align="left")

*Formulaire HTML avec quatre champs de saisie et quatre étiquettes*

Vous avez peut-être remarqué que la valeur de l'espace réservé que nous avons attribuée à tous les champs de saisie est "a". Cela sera utile plus tard dans le tutoriel lorsque nous commencerons à appliquer une logique dynamique.

## Comment styliser le formulaire

Notre formulaire est assez basique, alors ajoutons quelques styles pour le rendre plus joli.

Tout d'abord, nous devons effectuer quelques réinitialisations et définir la couleur de fond :

```css
@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');

/* Supprimer toutes les marges/padding par défaut. Définir la police */
body {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  background-color: white;
  font-family: "lato", sans-serif;
}
```

Voici à quoi ressemblera notre page :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/reset-lato.png align="left")

*Sans aucun style pour l'instant*

Après avoir stylisé le `body`, nous allons définir le mode d'affichage du contenu sur `flex`. Cela garantit que tous les enfants directs à l'intérieur d'un élément conteneur `div` sont affichés côte à côte par défaut.

Dans notre cas, il n'y a qu'un seul enfant à l'intérieur du conteneur `signupFrm`. La seule raison pour laquelle nous utilisons `display: flex` ici est d'utiliser les propriétés `align-items` et `justify-content` pour aider à centrer tout verticalement et horizontalement :

```css
/* Place le formulaire au centre à la fois horizontalement et verticalement. Définit sa hauteur à 100% de la hauteur de la fenêtre */

.signupFrm {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
```

La propriété `vh`, qui signifie hauteur de la fenêtre, garantit que le formulaire prend 100% de la hauteur de la fenêtre du navigateur, quelle que soit la taille ou l'orientation de l'écran. Cela le rendra plus réactif.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/middle.png align="left")

*Notre formulaire est maintenant aligné au centre*

Maintenant, nous allons styliser un peu le formulaire :

```css
.form {
  background-color: white;
  width: 400px;
  border-radius: 8px;
  padding: 20px 40px;
  box-shadow: 0 10px 25px rgba(92, 99, 105, .2);
}

.title {
  font-size: 50px;
  margin-bottom: 50px;
}
```

Dans le premier style ciblé sur le formulaire, nous définissons le fond en blanc, nous lui donnons une largeur de 400px, nous ajoutons une courbe autour du formulaire, et enfin nous définissons une ombre autour de la boîte. Nous définissons également la taille de la police du titre et un espace en dessous de l'élément.

Et le résultat devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/with-card.png align="left")

*Le formulaire est maintenant dans une carte, avec une ombre de boîte*

Ensuite, nous allons styliser le `div` qui contient les champs de saisie du formulaire et les étiquettes du formulaire.

```css
.inputContainer {
  position: relative;
  height: 45px;
  width: 90%;
  margin-bottom: 17px;
}
```

Nous définissons la propriété de position de notre conteneur `div` de saisie sur relative. Cela nous permettra de positionner les enfants `input` et `label` comme nous le souhaitons. Nous définissons également la largeur pour qu'elle occupe 90 pour cent de la largeur totale du conteneur.

Voici comment notre formulaire sera rendu dans le navigateur web.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/margin-added.png align="left")

*Cela semble mieux*

Maintenant, nous devons styliser nos champs de saisie.

Nous définissons d'abord la `position` sur `absolute`. Cela nous permettra de déplacer chacun d'eux vers la partie supérieure gauche du parent conteneur positionné de manière relative.

Nous devons également masquer notre texte de remplissage arbitraire (les caractères "a" mentionnés précédemment), afin qu'ils ne se chevauchent pas avec le texte dans chaque étiquette. Le texte de remplissage sera nécessaire lorsque nous implémenterons la transition :

```css
/* Styliser les champs de saisie */

.input {
  position: absolute;
  top: 0px;
  left: 0px;
  height: 100%;
  width: 100%;
  border: 1px solid #DADCE0;
  border-radius: 7px;
  font-size: 16px;
  padding: 0 20px;
  outline: none;
  background: none;
  z-index: 1;
}

/* Masquer les textes de remplissage (a) */

::placeholder {
  color: transparent;
}
```

Avec les styles appliqués, notre formulaire devrait maintenant ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/absolute.png align="left")

*Le remplissage "a" n'est plus visible*

Ensuite, nous stylisons les étiquettes de texte :

```css
/* Styliser les étiquettes de texte */

.label {
  position: absolute;
  top: 15px;
  left: 15px;
  padding: 0 4px;
  background-color: white;
  color: #DADCE0;
  font-size: 16px;
  transition: 0.5s;
  z-index: 0;
}
```

L'étiquette affiche le texte qui indique quelles informations sont attendues dans le champ de saisie. Nous commençons par définir sa position sur absolue. Et en définissant les propriétés `top` et `left`, nous pouvons déplacer le texte vers le haut par rapport à son conteneur.

Ensuite, nous définissons une transition de 0,5 seconde. C'est le temps qu'il faudra au texte pour monter lorsqu'il est survolé.

Enfin, nous définissons également un z-index de 0. Le faible z-index garantit que l'étiquette est positionnée derrière d'autres éléments "mieux placés" s'ils se chevauchent jamais.

Voici ce qui est rendu sur la page :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/labels-1.png align="left")

*Le résultat*

Maintenant, nous allons nous concentrer sur les boutons.

Nous allons ajouter quelques animations fluides avec la propriété CSS `transform`, qui déplace le bouton un peu vers le haut et change la couleur une fois qu'il est survolé :

```css
.submitBtn {
  display: block;
  margin-left: auto;
  padding: 15px 30px;
  border: none;
  background-color: purple;
  color: white;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 30px;
}

.submitBtn:hover {
  background-color: #9867C5;
  transform: translateY(-2px);
}
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/ezgif.com-gif-maker--6-.gif align="left")

*Le bouton s'agrandit et change de couleur lorsqu'il est survolé*

Ensuite, nous devons effectuer quelques changements d'état.

Lorsque un champ de saisie reçoit le focus, nous voulons positionner son étiquette au-delà du haut du conteneur (-7px), à 3 pixels de la gauche, réduire la taille de la police à 14, et changer la couleur en violet :

```css
.input:focus + .label {
  top: -7px;
  left: 3px;
  z-index: 10;
  font-size: 14px;
  font-weight: 600;
  color: purple;
}
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/ezgif.com-gif-maker--5-.gif align="left")

*Les étiquettes montent lorsque le champ de saisie reçoit le focus*

Nous devons également ajouter une bordure violette autour du champ de saisie lorsqu'il reçoit le focus.

```css
.input:focus {
  border: 2px solid purple;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/ezgif.com-gif-maker--7--3.gif align="left")

*Bordure violette ajoutée*

Enfin, nous devons faire quelque chose de très important.

Actuellement, lorsque vous tapez du texte dans le formulaire et que vous déplacez le focus (votre souris) loin de celui-ci, le texte de l'étiquette et le texte dans le champ de saisie entrent en collision :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/ezgif.com-gif-maker--8--3.gif align="left")

*Collision entre l'étiquette et la valeur du champ de saisie*

Avec le CSS suivant, nous allons spécifier que, lorsque nous tapons une valeur dans le champ de saisie et que nous changeons de focus, nous voulons que l'étiquette reste flottante. De plus, nous spécifierons que nous voulons que le texte de l'étiquette perde sa couleur violette :

```css
.input:not(:placeholder-shown)+ .label {
  top: -7px;
  left: 3px;
  z-index: 10;
  font-size: 14px;
  font-weight: 600;
}
```

Et avec cela, voici l'apparence finale de notre page d'inscription.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/ezgif.com-gif-maker--9--1.gif align="left")

*Apparence finale*

## Conclusion

J'espère que vous avez appris de nouvelles choses sur CSS grâce à ce tutoriel. Les transitions CSS donnent vie à votre site web, et dans ce guide, nous avons rendu notre formulaire beaucoup plus vivant avec elles.

Vous pouvez obtenir tout le code de ce tutoriel depuis ce [dépôt GitHub](https://github.com/KingsleyUbah/Sign-Up-CSS).

J'ai récemment créé une newsletter où je fournis des conseils pratiques et des ressources sur l'apprentissage du développement web. Abonnez-vous à ma [newsletter](https://www.getrevue.co/profile/ubahthebuilder) et recevez des conseils directement dans votre boîte de réception.

Merci d'avoir suivi.

> **P/S** : Si vous apprenez JavaScript, j'ai créé un eBook qui enseigne 50 sujets en JavaScript avec des notes numériques dessinées à la main. [Découvrez-le ici](https://ubahthebuilder.gumroad.com/l/js-50).