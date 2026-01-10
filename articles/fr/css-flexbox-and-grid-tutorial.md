---
title: Tutoriel CSS Flexbox et Grid – Comment créer une page de destination responsive
  avec HTML et CSS
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-09-08T17:16:00.000Z'
originalURL: https://freecodecamp.org/news/css-flexbox-and-grid-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/SkilllzLanding.png
tags:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: flexbox
  slug: flexbox
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Tutoriel CSS Flexbox et Grid – Comment créer une page de destination responsive
  avec HTML et CSS
seo_desc: 'In this tutorial, we are going to build a simple landing page for an online
  education platform called Skilllz.

  This tutorial will teach you how to use and implement CSS Flexbox and CSS Grid alignment.
  We''ll also cover many other CSS concepts. And fin...'
---

Dans ce tutoriel, nous allons créer une page de destination simple pour une plateforme d'éducation en ligne appelée **Skilllz**.

Ce tutoriel vous apprendra à utiliser et à implémenter l'alignement CSS Flexbox et CSS Grid. Nous aborderons également de nombreux autres concepts CSS. Et enfin, nous apprendrons à rendre la page responsive afin qu'elle fonctionne sur toutes les tailles d'écran.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/ezgif.com-gif-maker.gif align="left")

Le tutoriel est divisé en cinq parties :

* Comment créer la barre de navigation

* Comment créer la section de présentation

* Comment créer la section inférieure

* Comment créer la section de pied de page

* Comment rendre la page responsive

Chacune de ces sections vous apprendra de nouvelles compétences et outils en CSS et en développement web. Alors, plongeons directement dans le sujet.

## Comment créer le modèle HTML de base

Si vous avez emmet installé dans votre IDE, vous pouvez générer un modèle HTML de base pour votre projet en tapant `!` et en cliquant sur la touche `enter` ou `tab` de votre clavier.

Si ce n'est pas le cas, vous pouvez copier ce code de modèle et le coller dans votre éditeur de code :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" integrity="sha512-1ycn6IcaQQ40/MKBW2W4Rhis/DbILU74C1vSrLJxCq57o941Ym01SwNsOMqvEBFlcgUa6xLiPY/NS5R+E6ztJQ=="
  crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>
 
</body>
</html>
```

### Comment utiliser les icônes Font Awesome

Comme vous pouvez le voir dans l'une des captures, nous allons utiliser certaines icônes de police pour donner un meilleur échange à notre section de service.

Pour cela, nous allons utiliser Font Awesome depuis le CDN. Si vous avez créé un modèle HTML vous-même, copiez la balise `link` suivante et collez-la dans votre balise `head` :

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" integrity="sha512-1ycn6IcaQQ40/MKBW2W4Rhis/DbILU74C1vSrLJxCq57o941Ym01SwNsOMqvEBFlcgUa6xLiPY/NS5R+E6ztJQ=="
  crossorigin="anonymous" referrerpolicy="no-referrer" />
```

## Commençons

Tout d'abord, assurez-vous que votre fichier de feuille de style (.css) est correctement lié à votre page HTML.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/test.png align="left")

## Comment créer la barre de navigation

La section de la barre de navigation sera composée du nom de notre site ainsi que de deux liens de navigation : `Se connecter` et `Voir les cours`.

Voici le balisage pour notre navbar :

```js
<div class="navbar">
        <div class="container flex">
          <h1 class="logo">Skilllz</h1>
            <nav>
              <ul>
                <li class="nav"><a class="outline" href="">Se connecter</a></li>
                <li class="nav"><a href="" class="outline">Voir les cours</a 				</li>
              </ul>
            </nav>
        </div>
      </div>
```

Sur la div enveloppant les éléments à l'intérieur de cette section (la navbar), nous enregistrons les classes container et flex.

* `.container` : nous utiliserons cette classe utilitaire dans chaque section pour nous assurer que les éléments internes ne dépassent pas une certaine largeur que nous spécifierons en CSS

* `.flex` : nous utiliserons cette classe utilitaire pour afficher les éléments enfants de manière alignée horizontalement (côte à côte) en utilisant CSS Flexbox.

À l'intérieur de la `div`, nous avons un `h1` avec la classe `logo` et deux liens de navigation `li>a` avec les classes `outline`, respectivement.

À ce stade, notre page aura l'air toute simple et nue comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/navbarHTML1.png align="left")

*Aucun CSS pour l'instant*

### Comment appliquer le style CSS à notre page

Nous devons maintenant appliquer certaines règles CSS pour styliser notre section de navigation comme nous le souhaitons. Ce que nous voulons faire en premier, c'est définir le style de base pour notre page web avec le code suivant :

```css
/* Remplacer le style par défaut et définir le remplissage et la marge à rien */

* {
  box-sizing: border-box;
  padding: 0;
  margin: 0
}

/* Texte blanc partout */

body {
  font-family: "lato", sans-serif;
  color: white;
}

/* Rendre tout le texte des liens noir sans décoration de texte */
a {
  color: black;
  text-decoration: none;
}


h1 {
  font-size: 30px;
  font-weight: 600;
  margin: 10px 0;
  line-height: 1.2;
}


h2 {
  font-size: 25px;
  font-weight: 300;
  margin: 10px 0;
  line-height: 1.2;
}

p {
  font-size: 30px;
}

/* Toutes les images ne doivent pas être plus grandes que le conteneur parent */
img {
  width: 100%;
}

/* Aucun style sur les éléments de liste */
li {
  list-style-type: none;
}



p {
  font-size: 20px;
  margin: 10px 0;
}
```

Avec les styles par défaut appliqués, notre page ressemblera maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/navbarHTML2.png align="left")

Ensuite, nous devons définir le style pour notre classe container :

```css
/* Centre le contenu, définit une largeur maximale et assure que les éléments peuvent dépasser */

.container {
  margin: 0 auto;
  max-width: 1200px;
  overflow: visible;
}
```

Maintenant, notre contenu ne dépassera pas la largeur maximale spécifiée.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/navbarHTML3.png align="left")

Après cela, nous devons définir la couleur de fond de notre section de barre de navigation en violet :

```css
/* Définit la couleur de fond, la hauteur et le remplissage */

.navbar {
  background-color: purple;
  height: 70px;
  padding: 0 30px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/navbarHTML4.png align="left")

Ensuite, nous ciblons uniquement l'élément `h1` à l'intérieur de la `navbar` et spécifions les styles suivants :

```css
/* Définit la taille de la police, réduit le poids de la police, ajoute une marge et une hauteur de ligne */

.navbar h1 {
  font-size: 30px;
  font-weight: 300;
  margin: 10px 0;
  line-height: 1.2;
}
```

Avec ce style appliqué, notre titre `h1` ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/navbarH5.png align="left")

Maintenant, nous devons afficher les deux éléments enfants à l'intérieur du conteneur `h1` et `nav` côte à côte en utilisant Flexbox.

```css
.navbar .flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 100%;
}
```

Tout d'abord, nous définissons le mode d'affichage sur `flex`. Cela alignera les éléments côte à côte **par défaut**.

Nous justifions ensuite le contenu, en ajoutant un espace considérable entre chaque élément en utilisant la valeur `space-between`. Nous alignons les éléments pour qu'ils apparaissent au centre (milieu) du conteneur et définissons sa hauteur pour qu'elle occupe tout le conteneur.

Voici à quoi notre page devrait maintenant ressembler :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/navrbarH6.png align="left")

*Cool, non ?*

Cependant, nous ne voulons pas non plus que nos deux liens de navigation soient empilés l'un sur l'autre. Au lieu de cela, nous voulons qu'ils soient affichés côte à côte. Devinez comment nous faisons cela ? Avec Flexbox !

```css
.navbar ul {
  display: flex;
}

/* Change la couleur des deux liens en blanc, ajoute un remplissage entre eux et une marge également */

.navbar a {
  color: white;
  padding: 9px;
  margin: 0 10px;
}
```

Notre page ressemblera maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/navbarH7.png align="left")

*La puissance de CSS flexbox*

Si vous avez regardé la brève vidéo d'introduction, vous remarquerez que chaque fois que je survole l'un des liens, la couleur du texte change pour une teinte plus claire de violet et une bordure solide apparaît en dessous.

Nous pouvons implémenter cette transition en utilisant le pseudo-élément CSS `:hover` :

```css
.navbar a:hover {
  color: #9867C5;
  border-bottom: 3px solid #9867C5;
}
```

Maintenant, regardez ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/ezgif.com-gif-maker--1-.gif align="left")

*Effet de survol sur les liens*

Et avec cela, nous arrivons à la fin de la section de la barre de navigation.

## Comment créer la zone de présentation

La zone de présentation va contenir le texte du titre, le texte de soutien, un formulaire pour l'inscription de nouveaux utilisateurs, ainsi qu'une image de titre.

Cette section va être divisée en deux : le côté gauche et le côté droit. En d'autres termes, elle sera affichée sous forme de grille de deux unités.

Voici le balisage pour cette section :

```html
<section class="showcase">
        <div class="container">
            <div class="grid">
              <div class="grid-item-1">
                <div class="showcase-text">
                  <h1>Apprenez n'importe quelle compétence numérique de votre choix aujourd'hui</h1>
                  <p class="supporting-text"> Plus de 30 000 étudiants apprennent actuellement avec nous</p>
                </div>
                <div class="showcase-form">
                  <form action="">
                    <input type="email" placeholder="Entrez votre adresse e-mail">
                    <input type="submit" class="btn" value="Commencer l'apprentissage">
                  </form>
                  <p class="little-info">Essayez nos cours gratuits aujourd'hui. Aucun risque, aucune carte de crédit requise</p>
                </div>
              </div>

              <div class="grid-item-2">
                <div class="image">
                  <img src="./images/transparent.png" alt="">
                </div>
              </div>
           </div>

        </div>
      </section>
```

Actuellement, notre application va avoir l'air un peu désordonnée :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/showcaseH1.png align="left")

### Comment appliquer le style CSS à notre zone de présentation

Tout d'abord, nous définissons la hauteur de la section de présentation ainsi qu'une couleur de fond :

```css
.showcase {
  height: 300px;
  background-color: purple;
}
```

Notre application ressemblera maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/showcaseH2.png align="left")

*Toujours désordonné*

> REMARQUE : J'ai changé la couleur du `h1` en blanc

Ensuite, nous appliquons les styles suivants :

```css
/* Ajoute une marge sous le texte */
.showcase p {
  margin-bottom: 30px;
}

/* Ajoute une ombre sous l'image */
.showcase img {
  box-shadow: 7px 7px 7px rgba(0, 0, 0, 0.2);
}

/* Ajoute un peu de remplissage au contenu du formulaire */
.showcase-form {
  padding-left: 7px;
}
```

Cela nous amène à l'activité principale. Si vous vous souvenez, j'ai dit que nous allions créer deux sections (grilles) à l'intérieur du conteneur de présentation. Avec la classe de grille enregistrée sur ce conteneur, nous pouvons aligner son contenu en utilisant l'affichage de la grille CSS comme ceci :

```css
.grid {
  overflow: visible;
  display: grid;
  grid-template-columns: 60% 40%;
}
```

Cela créera deux colonnes à l'intérieur de notre conteneur de présentation. La première partie occupera 60 pour cent du conteneur, et la deuxième partie occupera les 40 pour cent restants du conteneur.

Le débordement visible garantira que l'image (si elle est plus grande que le conteneur) dépassera du conteneur.

Notre application ressemblera maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/showcaseH3.png align="left")

Ensuite, nous devons définir un espace entre la zone de navigation et la zone de présentation.

```css
.grid-item-1,
.grid-item-2 {
  position: relative;
  top: 50px;
}
```

En conséquence, il est maintenant un peu espacé :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/showcaseH4.png align="left")

Maintenant, nous devons styliser les deux entrées de notre formulaire car elles ne sont pas très belles. Nous sélectionnons la première entrée par son type (email) et sélectionnons la deuxième par son nom de classe, `btn`.

```css
.showcase input[type='email'] {
  padding: 10px 70px 10px 0;
  font-size: 14px;
  border: none;
  border-radius: 6px;
  padding-left: 6px;
}

.btn {
  border-radius: 6px;
  padding: 12px 20px;
  background: #9867C5;
  border: none;
  margin-left: 10px;
  color: white;
  font-size: 16px;
  cursor: pointer;
  box-shadow: 0 10px 10px rgba(0, 0, 0, 0.2);
}
```

Ce style transformera nos deux entrées de formulaire en ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/showcaseH5-1.png align="left")

*Entrée de formulaire mieux stylisée*

Peut-être aussi changer la police du texte de soutien :

```css
.showcase-form {
  margin: auto;
}

/* Changer la police et sa taille */
.little-info {
  font-size: 15px;
  font-family: "poppins", sans-serif;

}
```

Voici l'apparence finale de notre section de présentation :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/showcaseH7.png align="left")

*Apparence finale de la section de présentation*

C'est tout pour cette section !

## Comment construire la partie inférieure de la page

La partie inférieure de la page contiendra deux sections, la section **statistiques** et la section **témoignages**.

Le conteneur de statistiques, qui affiche les services offerts par **Skilllz**, sera composé de trois `div`, chacune contenant une icône Font Awesome, un `h3` de classe `title`, et un paragraphe `p` de classe `text`.

Le conteneur de témoignages contiendra les témoignages de trois personnes aléatoires qui ont appris en utilisant Skillz. J'ai pris les photos sur [unsplash](https://unsplash.com/s/photos/random-people).

### Comment construire la section des statistiques

Tout d'abord, nous allons travailler sur la section des statistiques. Le texte est simplement un texte factice 'lorem50' pour servir de remplissage pour cette démonstration.

Voici le balisage pour cela :

```html
<div class="lower-container container">
      <section class="stats">
        <div class="flex">
          <div class="stat">
            <i class="fa fa-folder-open fa-2x" aria-hidden="true"></i>
            <h3 class="title">Plus de 300 cours disponibles</h3>
            <p class="text">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
              Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
          </div>
          <div class="stat">
            <i class="fa fa-graduation-cap fa-2x" aria-hidden="true"></i>
            <h3 class="title">Certificat gratuit offert pour tous les cours</h3>
            <p class="text">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
              Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
          </div>
          <div class="stat">
            <i class="fa fa-credit-card-alt fa-2x" aria-hidden="true"></i>
            <h3 class="title">Réservez une session 1on1 pour seulement 5 $</h3>
            <p class="text">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
              Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
          </div>
        </div>
      </section>
```

Cette section sera affichée comme une page blanche. Cela est dû au fait que nous avions défini la couleur de notre texte dans tout le corps en blanc. Nous devons donc ajouter un peu de style.

### Comment appliquer le style CSS à la section des statistiques

Tout d'abord, nous devons appliquer les styles suivants :

```css
/* Centre le conteneur, définit une largeur maximale
.lower-container {
  margin: 120px auto;
  padding: 0;
  max-width: 1400px;
}


/* Cible tous les h3 avec la classe title */
.title {
  color: black;
  font-size: 20px;
  text-align: left;
  padding-left: 10px;
  padding-top: 10px;
}

/* Cible les paragraphes avec le nom de classe text */
.text {
  color: black;
  font-size: 19px;
  width: 100%;
  padding: 10px;
  margin: 0, 20px;
  text-align: justify;
}
```

Cela rendra maintenant notre texte visible :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/lower1.png align="left")

Remarquez que les icônes de police de Font Awesome ne sont pas visibles. Nous allons travailler là-dessus très bientôt.

Mais avant cela, nous devons faire quelque chose d'important. Nous avons l'intention que les trois div de statistiques soient alignées horizontalement (côte à côte). Pour y parvenir, nous allons à nouveau utiliser CSS Flexbox :

```css
/* Affichage horizontal, met un peu d'espace autour d'eux */
.flex {
  display: flex;
  justify-content: space-around;
}

/* Ajoute un peu de remplissage autour du conteneur. Aligne le texte de manière centrale */
.stats {
  padding: 45px 50px;
  text-align: center;
}

/* Définit la marge et la largeur */
.stat {
  margin: 0 30px;
  text-align: center;
  width: 800px;
}
```

Voici à quoi ressemblera notre application maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/lower2.png align="left")

Toujours pas d'icônes ? Il est temps de corriger cela !

```css
.stats .fa {
  color: purple;
}
```

et voilà !

![Image](https://www.freecodecamp.org/news/content/images/2021/09/lower4.png align="left")

### Comment construire la section des témoignages

La deuxième section à l'intérieur du conteneur inférieur `div` de la page est la section des témoignages. Cette section sera composée de trois cartes, chacune contenant l'image de la personne (découpée dans un cercle), son nom et le témoignage de la personne.

Voici le balisage pour cela :

```html
<section class="testimonials">
      <div class="container">
        <div class="testimonial grid-3">
          <div class="card">
            <div class="circle">
              <img src="./images/4.jpg" alt="">
            </div>
            <h3>Aston</h3>
            <p>J'ai appris le développement web en utilisant cette plateforme et je vais dire que c'est la meilleure plateforme pour apprendre. Absolument
            ça vaut l'investissement !</p>
          </div>
          <div class="card">
            <div class="circle">
              <img src="./images/5.jpg" alt="">
            </div>
            <h3>Beth</h3>
            <p>J'ai appris la rédaction publicitaire en utilisant cette plateforme et je vais dire que c'est la meilleure plateforme pour apprendre. Absolument
            ça vaut l'investissement !</p>
          </div>
          <div class="card">
            <div class="circle">
              <img src="./images/6.jpg" alt="">
            </div>
            <h3>Chris</h3>
            <p>J'ai appris le marketing d'affiliation en utilisant cette plateforme et je vais dire que c'est la meilleure plateforme pour apprendre. Absolument
            ça vaut l'investissement !</p>
          </div>
        </div>
      </div>
    </section>
```

### Comment appliquer le style CSS

Tout d'abord, nous définissons la couleur du texte en noir pour pouvoir le voir :

```css
.testimonial {
  color: black;
  padding: 40px;
}
```

Une fois appliqué, cela devrait rendre le texte visible et ajouter un peu de remplissage à la section :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/testi1.png align="left")

Ensuite, nous définissons l'image pour qu'elle prenne la hauteur de son conteneur parent :

```css

/* Enveloppe l'image dans une forme de cercle et définit la hauteur pour qu'elle prenne tout l'élément parent */

.testimonial img {
    height: 100%;
    clip-path: circle();
}

/* Aligne le texte de manière centrale */

.testimonial h3{
  text-align: center;
}
```

Si vous vérifiez la mise en page finale dans le gif, vous remarquerez que les trois cartes de témoignages sont alignées côte à côte sur la même ligne.

Nous devons donc créer une div de trois colonnes égales en utilisant l'arrangement de grille CSS.

```css
/* Crée une grille de trois colonnes égales. Définit un écart de 40 px entre elles */

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
}


/* Crée une carte blanche avec une ombre autour */
.card {
  padding: 10px;
  background-color: white;
  border-radius: 10px;
  box-shadow: -7px -7px 20px rgba(0, 0, 0, 0.2),
               7px  7px 20px rgba(0, 0, 0, 0.2)
}
```

Avec tous ces styles appliqués, la section des témoignages ressemblera maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/testi2.png align="left")

Enfin, nous stylisons la div du cercle et la positionnons par rapport à la bordure supérieure de la carte en utilisant CSS :

```css
.circle {
    background-color: transparent;
    border:3px solid purple;
    height:90px;
    position: relative;
    top: -30px;
    left: 120px;
    border-radius:50%;
    -moz-border-radius:50%;
    -webkit-border-radius:50%;
    width:90px;
}
```

Et voici à quoi tout ressemblera dans notre navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/testi4.png align="left")

*Apparence finale*

Très bien, nous sommes maintenant prêts à passer à la section du pied de page. Ensuite, nous apprendrons comment rendre le site responsive.

## Comment construire la section du pied de page

La dernière partie de notre processus de création de la page de destination consiste à créer la section du pied de page. La section du pied de page comprendra un texte de copyright, trois liens de navigation supplémentaires et un groupe d'icônes de médias sociaux de Font Awesome.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/ezgif.com-gif-maker--2-.gif align="left")

Voici le balisage HTML pour la section du pied de page de notre page de destination :

```html
<footer>
   <div class="container grid-3">
     <div class="copyright">
       <h1>Skilllz</h1>
       <p>Copyright &copy; 2021</p>
     </div>
     <nav class="links">
       <ul>
         <li><a href="" class="outline">Accueil</a></li>
         <li><a href="" class="outline">Tuteurs</a></li>
         <li><a href="" class="outline">Catégories</a></li>
       </ul>
     </nav>
     <div class="profiles">
       <a href=""><em class="fab fa-twitter fa-2x"></em></a>
       <a href=""><em class="fab fa-instagram fa-2x"></em></a>
       <a href=""><em class="fab fa-facebook fa-2x"></em></a>
       <a href=""><em class="fab fa-whatsapp fa-2x"></em></a>
     </div>
   </div>
 </footer>
```

La section du pied de page aura l'air peu attrayante sans aucun style :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/footer-1.png align="left")

*Aucun CSS pour l'instant*

Alors, changeons cela.

### Comment styliser le pied de page

Tout d'abord, nous devons définir la couleur de fond pour la section du pied de page (ainsi que la couleur pour tous les liens) en blanc, comme ceci :

```css
/* Ajoute un remplissage autour du pied de page également */

footer {
  background-color: purple;
  padding: 20px 10px;
}

/* Définit tous les textes de liens en blanc et met une marge à gauche et à droite */

footer a {
  color: white;
  margin: 0 10px;
}
```

Maintenant, le pied de page ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/footer3.png align="left")

*Pied de page*

Si vous vérifiez le premier gif, vous remarquerez que lorsque je survole l'un des liens à l'intérieur du pied de page, leur couleur change pour une teinte plus claire de violet et une bordure apparaît également en dessous.

Nous pouvons faire en sorte que cela se produise en utilisant un sélecteur `:hover` :

```css
footer a:hover {
  color: #9867C5;
  border-bottom: 2px solid #9867C5;
}
```

C'est tout pour le pied de page !

## Comment définir des requêtes média pour rendre la page responsive

Il est maintenant temps de rendre notre page de destination plus responsive. Lors de la création d'un site web, il est important de garder à l'esprit que les utilisateurs consulteront le site à partir de différents appareils. Il est donc impératif de rendre la mise en page du site responsive pour améliorer l'expérience utilisateur sur plusieurs appareils.

Dans notre CSS, nous définirons des requêtes média qui établissent des points d'arrêt pour les différentes largeurs d'écran des appareils et associent un ensemble de règles CSS pour chaque taille d'écran.

### Comment concevoir pour les tablettes et les écrans plus petits

Tout d'abord, nous allons optimiser la mise en page de notre site pour les utilisateurs consultant depuis une tablette. Dans notre CSS, nous définissons le style suivant :

```css
/* Tablettes et écrans plus petits */

@media(max-width: 768px) {
  .grid,
  .grid-3 {
    grid-template-columns: 1fr;
  }
```

Initialement, nous avions défini deux colonnes pour la classe `.grid` et 3 colonnes pour la classe `grid-3`. Maintenant, nous voulons nous assurer que tous les éléments de la grille prennent une seule ligne.

En conséquence, notre formulaire et notre image, qui étaient auparavant affichés côte à côte (horizontalement), seront maintenant affichés l'un après l'autre (verticalement), comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/resp1.png align="left")

Ensuite, nous appliquerons les styles suivants :

```css
/* Aligne tout le texte au centre. Cela déplacera tout le texte, y compris le formulaire, au centre */

.showcase {
    height: auto;
    text-align: center;
  }

/* Cela réinitialise la largeur du conteneur d'image et ajoute un espace de marge à gauche */ 

.image {
    width: 600px;
    margin-left: 80px;
  }

/* Change les sections de service de l'orientation côte à côte à chacune prenant sa propre ligne. Aligne le texte au centre */

.stats .flex {
    flex-direction: column;
  }

  .stats {
    text-align: center;
  }

/* Assure que chaque section de statistiques ne dépasse pas la largeur du parent */

.stat {
    width: 100%;
    padding-right: 80px;
  }

/* (ré)Déplace le cercle au centre de la carte */

.circle {
      background-color: transparent;
      border:3px solid purple;
      height:90px;
      position: relative;
      top: -30px;
      left: 270px;
      border-radius:50%;
      -moz-border-radius:50%;
      -webkit-border-radius:50%;
      width:90px;
  }
```

Et voilà ! Notre site fonctionne maintenant sur les tablettes et les écrans plus petits.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/ezgif.com-gif-maker--3--1.gif align="left")

*Le résultat*

### Comment concevoir pour les appareils mobiles

De nombreuses personnes peuvent consulter le site depuis un appareil mobile, qui a généralement la plus petite taille d'écran parmi tous les appareils. Pour cette raison, la création d'une mise en page pour les écrans de taille mobile est très importante.

```css
/* Appareils mobiles */
@media(max-width: 500px) {
  .navbar {
    height: 100px;
  }
```

Tout d'abord, nous augmentons la hauteur de notre zone de navigation. Puisqu'elle sera consultée depuis un écran plus petit, nous voulons que la zone soit plus accentuée pour l'utilisateur.

Ensuite, nous définissons les styles suivants :

```css
/* Change l'alignement. Le titre du logo reste en haut, les liens de navigation seront en dessous */

.navbar .flex {
    flex-direction: column;
  }


/* Lorsqu'on survole, conserve la couleur blanche et change la bordure en noir */

  .navbar a:hover {
    color: white;
    border-bottom: 2px solid black;
  }


/* Définit un fond violet clair sur les liens de navigation, le rend un peu arrondi et ajoute un peu d'espacement */

  .navbar ul {
    background: #9867C5;
    border-radius: 5px;
    padding: 10px 0;
  }


/* Aligne le texte au centre */

  .showcase {
    height: auto;
    text-align: center;
  }


/* Réduit la taille de la police */

.little-info {
    font-size: 13px;
  }


/* Réduit la largeur de l'image */

  .image {
    width: 350px;
    margin-left: 70px;
  }

  .stat {
    margin-bottom: 40px;
  }


/* Déplace le cercle une fois de plus */

.circle {
      background-color: transparent;
      border:3px solid purple;
      height:90px;
      position: relative;
      top: -30px;
      left: 150px;
      border-radius:50%;
      -moz-border-radius:50%;
      -webkit-border-radius:50%;
      width:90px;
  }
}
```

Et voilà !

![Image](https://www.freecodecamp.org/news/content/images/2021/09/ezgif.com-gif-maker--4--1.gif align="left")

## **Conclusion**

FlexBox et l'alignement Grid sont des outils très puissants pour disposer une page web comme vous le souhaitez.

Le design web responsive est sans doute l'un des principes de design les plus importants dans le développement web. Nous devons tenir compte du fait que notre site sera consulté à partir de divers types d'appareils avec différentes résolutions d'écran. Optimiser la mise en page de notre site pour différents écrans améliorera l'expérience utilisateur.

Dans ce tutoriel, nous avons conçu une page de destination simple en utilisant CSS Flexbox, Grid et de nombreuses autres propriétés CSS. Nous avons également rendu la page attrayante sur les tablettes et les écrans mobiles.

Le code complet de ce projet peut être obtenu à partir de ce [dépôt GitHub](https://github.com/KingsleyUbah/Skilllz).

J'espère que vous avez appris quelque chose d'utile dans ce tutoriel. Si vous avez des suggestions, contactez-moi sur [Twitter](https://twitter.com/UbahTheBuilder). Vous pouvez également visiter mon [blog](https://ubahthebuilder.tech/) pour des articles comme celui-ci.

Merci de m'avoir suivi et à bientôt.