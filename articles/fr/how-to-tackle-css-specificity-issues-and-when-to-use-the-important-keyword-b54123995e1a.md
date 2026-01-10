---
title: Comment résoudre les problèmes de spécificité CSS et quand utiliser le mot-clé
  !important
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-09T18:27:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-tackle-css-specificity-issues-and-when-to-use-the-important-keyword-b54123995e1a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*O8s-GnxQPCyWNVc2WJyB5g.jpeg
tags:
- name: CSS
  slug: css
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment résoudre les problèmes de spécificité CSS et quand utiliser le
  mot-clé !important
seo_desc: 'By Muna Mohamed

  A Case Study


  Recently, there was a Twitter poll floating around where the user asked their followers
  a question about CSS specificity . Unfortunately, I was unable to find the original
  tweet (comment below if you happen to find it!) ...'
---

Par Muna Mohamed

#### Une étude de cas

![Image](https://cdn-media-1.freecodecamp.org/images/MzDK5rCsyUZQUDJtzNPCrrCVqob-ULXNImuE)

Récemment, un sondage Twitter circulant posait une question sur la spécificité CSS. Malheureusement, je n'ai pas pu retrouver le tweet original (laissez un commentaire si vous le trouvez !), mais en résumé, la majorité des gens ont eu tort.

Ce sondage Twitter (et ses conséquences) m'a amenée à me rafraîchir la mémoire sur le sujet de la spécificité et, à mon tour, à commencer à corriger les problèmes de spécificité dans mes propres projets — ce qui m'amène au but de cet article.

Dans cet article, nous allons refactoriser le code CSS d'un de mes projets qui présente des problèmes de spécificité CSS nécessitant des corrections.

### Spécificité CSS

#### Définition

La spécificité est décrite par [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity) comme :

> *le moyen par lequel les navigateurs décident quelles valeurs de propriétés CSS sont les plus pertinentes pour un élément et, par conséquent, appliquées.*

#### Règles

Lorsqu'il s'agit de décider quelles valeurs de propriétés CSS sont les plus pertinentes à appliquer à un élément, le navigateur utilise l'ordre source (c'est-à-dire la cascade) de la feuille de style CSS pour le déterminer. Mais cette règle s'applique lorsque les sélecteurs CSS ont une spécificité égale. Que se passe-t-il lorsque la spécificité d'un sélecteur CSS est plus élevée qu'un autre ?

![Image](https://cdn-media-1.freecodecamp.org/images/vS9jdbLJDgW1IWycyuIWGFlX9xPnJxekCte-)

Dans ce cas, les navigateurs utiliseront la spécificité d'un sélecteur CSS pour déterminer quelles déclarations CSS appliquer. Plus la spécificité d'un sélecteur CSS est élevée, plus il est probable que les navigateurs appliquent ses déclarations CSS plutôt qu'un autre.

```css
nav a {
  color: green;
}

a {
  color: red;
}
```

Par exemple, dans l'exemple ci-dessus, les deux sélecteurs CSS ciblent le même élément HTML, la balise d'ancrage. Pour déterminer quelle règle CSS appliquer à la balise d'ancrage, le navigateur calculera la valeur de spécificité et vérifiera laquelle est la plus élevée. Dans ce cas, le premier sélecteur a une valeur de spécificité plus élevée, donc le navigateur utilisera ses déclarations pour les appliquer à la balise d'ancrage.

Je voudrais souligner ici que bien que *!important* ne soit pas un sélecteur CSS, c'est un mot-clé utilisé pour forcer le remplacement d'une règle CSS indépendamment de la valeur de spécificité, de l'origine ou de l'ordre source d'un sélecteur CSS. Certains cas d'utilisation incluent :

* Corrections temporaires (un peu comme mettre du ruban adhésif sur un tuyau qui fuit)
* Remplacement du style en ligne
* Tests/débogage

Bien que l'utilisation du mot-clé *!important* puisse sembler utile, son utilisation peut être plus problématique qu'utile. Avec le temps, cela peut rendre difficile la maintenance de votre CSS et peut affecter négativement la lisibilité de votre feuille de style, en particulier pour toute autre personne qui travaille ou travaillera avec elle à l'avenir.

Ce qui nous amène à ce que nous allons faire aujourd'hui — corriger les problèmes de spécificité dans un projet.

### Le Projet

![Image](https://cdn-media-1.freecodecamp.org/images/jLPGiwbON7agN2c4M5yy0IPHIvvmpcmFFn75)

Un peu de contexte sur le projet que nous allons refactoriser — il s'agit d'une page d'accueil inspirée de Netflix utilisant l'API de MovieDB.

#### La feuille de style

L'objectif est de supprimer le mot-clé *"!important"* des règles CSS auxquelles il a été appliqué en refactorisant le code afin qu'il suive les règles de spécificité.

Ci-dessous, vous pouvez voir la feuille de style du projet.

```css
@import url("https://fonts.googleapis.com/css?family=Montserrat:400,400i,700");

body {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

.wrapper {
  width: 100%;
}

.wrapper #header {
  position: fixed;
  z-index: 300;
  padding: 15px;
  width: calc(100% - 30px);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: linear-gradient(to bottom, black 0%, transparent 100%);
}

.wrapper #header #brand-logo {
  color: #d32f2f;
  text-shadow: 1px 1px 2px black;
  letter-spacing: 5px;
  text-transform: uppercase;
  font-family: Montserrat;
  font-weight: bold;
  font-size: 22px;
}

.wrapper #header #menu-icon {
  display: none;
}

.wrapper #header .nav-link,
.wrapper #header .icon {
  color: #bdbdbd;
  cursor: pointer;
}

.wrapper #header .nav-menu {
  width: 400px;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.wrapper #header .nav-link {
  padding: 5px 10px;
  font-size: 15px;
  font-family: century gothic;
  text-decoration: none;
  transition: background-color 0.2s ease-in;
}

.wrapper #header .nav-link:hover {
  color: #c62828;
  background-color: rgba(0, 0, 0, 0.7);
}

.wrapper #header .icon {
  font-size: 16px;
}

.wrapper #header .icon:hover {
  color: #c62828;
}

.wrapper #site-banner,
.wrapper #categories {
  width: 100%;
}

.wrapper #site-banner {
  height: 550px;
  background-image: url("https://s1.gifyu.com/images/rampage_2018-1024x576.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

.wrapper #site-banner .main-movie-title,
.wrapper #site-banner .watch-btn,
.wrapper #site-banner .main-overview {
  position: absolute;
  z-index: 3;
}

.wrapper #site-banner .main-movie-title, .wrapper #site-banner .watch-btn {
  text-transform: uppercase;
}

.wrapper #site-banner .main-movie-title {
  top: 120px;
  left: 20px;
  background: -webkit-linear-gradient(#ff9100, #dd2c00);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: 55px;
  font-family: Montserrat;
  font-weight: bold;
}

.wrapper #site-banner .main-overview {
  width: 400px;
  top: 230px;
  left: 25px;
  color: #fafafa;
  line-height: 25px;
  font-family: helvetica;
}

.wrapper #site-banner .watch-btn {
  width: 150px;
  height: 35px;
  top: 350px;
  left: 25px;
  border: none;
  border-radius: 20px;
  color: #fafafa;
  cursor: pointer;
  transition: all 0.2s ease-in;
  background-color: #ff0000;
  box-shadow: 1px 5px 15px #940000;
}

.wrapper #site-banner .watch-btn:hover {
  color: #F5F5F5;
  background-color: #940000;
}

.wrapper .after {
  position: relative;
  top: 0;
  left: 0;
  z-index: 2;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.3);
}

.wrapper #categories {
  padding: 30px 0;
  display: flex;
  flex-direction: column;
  background: linear-gradient(to top, #090909 0%, #000000 100%);
  overflow: hidden;
}

.wrapper #categories .category {
  margin: 30px 0;
}

.wrapper #categories .category-header, .wrapper #categories .content {
  margin-left: 20px;
  color: #B0BEC5;
  font-family: helvetica;
}

.wrapper #categories .category-header {
  margin-bottom: 50px;
  font-weight: normal;
  letter-spacing: 5px;
}

.wrapper #categories .content {
  position: relative;
  right: 0;
  display: flex;
  justify-content: flex-start;
  transition: all 3s ease-in-out;
}

.wrapper #categories .movie {
  margin-right: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}

.wrapper #categories .movie-img {
  transition: all 0.2s ease-in;
}

.wrapper #categories .movie-img:hover {
  -webkit-filter: contrast(1.1);
          filter: contrast(1.1);
  -webkit-transform: scale(1.05);
          transform: scale(1.05);
  cursor: pointer;
}

.wrapper #footer {
  width: 100%;
  height: 120px;
  background-color: #090909;
  display: flex;
  align-items: flex-end;
  justify-content: flex-start;
}

.wrapper #footer #copyright-label {
  margin-left: 20px;
  padding: 10px;
  color: rgba(255, 255, 255, 0.3);
  opacity: 0.7;
  letter-spacing: 2px;
  font-family: helvetica;
  font-size: 12px;
}

//Media Query
@media (max-width: 750px) {
  .nav-menu {
    visibility: hidden;
  }
    
#menu-icon {
    display: block !important;
    font-size: 22px;
  }
    
.main-movie-title {
    font-size: 45px !important;
  }
    
.main-overview {
    width: 350px !important;
    font-size: 14px !important;
  }
    
.watch-btn {
    width: 130px !important;
    height: 25px !important;
    font-size: 13px;
  }
    
.movie-img {
    width: 170px;
  }
}
```

Nous pouvons voir dans la feuille de style que l'utilisation du mot-clé *!important* est principalement concentrée dans la section des requêtes média qui décrit les styles que le navigateur doit appliquer lorsque la largeur de l'écran est inférieure à 750 pixels.

Alors, que se passe-t-il lorsque nous supprimons le mot-clé *!important* des règles CSS auxquelles il a été appliqué ? Eh bien, nous n'avons plus de "carte joker" qui force le remplacement des règles CSS d'autres sélecteurs CSS qui ciblent le même élément HTML. Ainsi, le navigateur examinera la feuille de style pour voir s'il y a des règles CSS conflictuelles.

S'il y en a, alors pour déterminer quelles règles CSS appliquer plutôt qu'une autre, le navigateur utilisera l'ordre source, la spécificité et l'importance des sélecteurs CSS. Si les sélecteurs CSS avec des règles CSS conflictuelles ont une spécificité égale, alors le navigateur utilisera la règle de l'ordre source et appliquera les règles CSS du sélecteur CSS qui apparaît plus bas dans la feuille de style. En utilisant ces informations, nous pouvons voir que cette situation n'est pas le cas pour notre feuille de style.

Mais, si les sélecteurs CSS avec des règles CSS conflictuelles n'ont pas une spécificité égale, alors le navigateur appliquera les règles CSS du sélecteur CSS qui a une spécificité plus élevée. Nous pouvons voir dans notre feuille de style que c'est le cas ; les sélecteurs CSS dans notre requête média ont une spécificité plus faible que les sélecteurs CSS dans la partie principale de notre feuille de style.

Maintenant que nous avons identifié le problème, corrigeons-le !

Tout d'abord, nous devons localiser les sélecteurs CSS correspondants qui correspondent aux sélecteurs CSS dans notre requête média.

```css
.wrapper #header #menu-icon {
  display: none;
}

.wrapper #site-banner .main-movie-title {
  ...
  font-size: 55px;
  ...
}

.wrapper #site-banner .main-overview {
  width: 400px;
  ...
}

.wrapper #site-banner .watch-btn {
  width: 150px;
  height: 35px;
  ...
}

@media (max-width: 750px) {
#menu-icon {
    display: block !important;
    ...
  }
    
.main-movie-title {
    font-size: 45px !important;
  }
    
.main-overview {
    width: 350px !important;
    font-size: 14px !important;
  }
    
.watch-btn {
    width: 130px !important;
    height: 25px !important;
    ...
  }
}
```

Nous pouvons voir que les sélecteurs CSS dans la partie principale de la feuille de style ont une spécificité plus élevée que les sélecteurs CSS correspondants dans la requête média. Malgré le fait que les sélecteurs CSS dans la requête média apparaissent plus tard dans la feuille de style, en raison des règles de spécificité (qui priment sur les règles d'ordre source), le navigateur appliquera les règles CSS des sélecteurs CSS qui les précèdent.

Pour corriger cela, nous devons augmenter les valeurs de spécificité des sélecteurs CSS dans la requête média. Si nous faisons en sorte que les sélecteurs CSS qui ciblent les mêmes éléments HTML aient une spécificité égale, alors le navigateur suivra la règle de l'ordre source. Les règles CSS décrites dans la requête média (qui se trouve plus bas dans la feuille de style) seront appliquées lorsque la largeur de l'écran est inférieure à 750 pixels.

Le résultat final ressemblera à ceci :

```css
.wrapper #header #menu-icon {
  display: none;
}

.wrapper #site-banner .main-movie-title {
  ...
  font-size: 55px;
  ...
}

.wrapper #site-banner .main-overview {
  width: 400px;
  ...
}

.wrapper #site-banner .watch-btn {
  width: 150px;
  height: 35px;
  ...
}

@media (max-width: 750px) {
.wrapper #header #menu-icon {
    display: block;
    ...
  }
    
.wrapper #site-banner .main-movie-title {
    font-size: 45px;
  }
    
.wrapper #site-banner .main-overview {
    width: 350px;
    font-size: 14px;
  }
    
.wrapper #site-banner .watch-btn {
    width: 130px;
    height: 25px;
    font-size: 13px;
  }
}
```

Et voilà ! Nous avons supprimé toutes les traces du mot-clé *!important* de la feuille de style. Déjà, nous pouvons voir que la feuille de style est plus facile à lire, et vous pouvez imaginer que notre feuille de style refactorisée serait beaucoup plus facile à utiliser et à maintenir (surtout si d'autres personnes doivent également travailler dessus).

### Conclusion

Alors, qu'avons-nous appris ?

Nous avons appris comment les navigateurs déterminent quels styles CSS appliquer en utilisant l'ordre source, la spécificité et l'origine des sélecteurs. Nous avons également appris les problèmes qui peuvent survenir en utilisant *!important* dans votre CSS et pourquoi son utilisation doit être réduite au minimum.

Nous n'avons pas besoin de recourir à l'utilisation de *!important* pour corriger les choses — il existe des solutions bien meilleures.

Le concept de spécificité peut prendre un certain temps à comprendre, mais j'espère qu'en documentant le processus et en utilisant un projet réel, cela vous aidera à mieux comprendre le concept de spécificité et comment l'appliquer dans votre propre CSS.

**Ressources supplémentaires**

* [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)
* [Batficity](http://batificity.com/) par [Mandy Michael](https://twitter.com/Mandy_Kerr)
* [CSS Specificity Wars](https://stuffandnonsense.co.uk/archives/css_specificity_wars.html) par [Andy Clarke](https://twitter.com/malarkey)
* [Specificity Visualizer](https://isellsoap.github.io/specificity-visualizer/) par [Francesco Schwarz](https://twitter.com/isellsoap).
* [When using !important is the right choice](https://css-tricks.com/when-using-important-is-the-right-choice/) par [Chris Coyier](https://twitter.com/chriscoyier)

Vous pouvez trouver le projet sur lequel nous avons travaillé [ici](https://codepen.io/Munamohamed94/pen/LJWzGr).

#### J'espère que vous avez apprécié cet article ! Si c'est le cas, 💙, 🔖 et partagez ! À la prochaine ! ✌️