---
title: Conseils CodePen et meilleures pratiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-08T04:12:17.000Z'
originalURL: https://freecodecamp.org/news/codepen-tips-and-best-practice-cf926ebd0b11
coverImage: https://cdn-media-1.freecodecamp.org/images/1*v9Er_3fscyNz8LhhdJXQ4Q.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Conseils CodePen et meilleures pratiques
seo_desc: 'By Michael Henderson

  When working in FCC there are going to be times when you create your own projects
  with CodePen. Campers like to share these projects on the Free Code Camp Forum to
  receive feedback from other Campers.

  Today, I am going to show yo...'
---

Par Michael Henderson

Lorsque vous travaillez dans [FCC](https://www.freecodecamp.com), il y aura des moments où vous créerez vos propres projets avec [CodePen](https://codepen.io/). Les campeurs aiment partager ces projets sur le [Forum Free Code Camp](http://forum.freecodecamp.com) pour recevoir des commentaires d'autres campeurs.

Aujourd'hui, je vais vous montrer comment tirer le meilleur parti de CodePen et comment maximiser vos commentaires dans le Forum FCC.

Préparez votre sac de couchage et vos guimauves. Oh, et n'oubliez pas de récupérer votre glacière Yeti de ce ours qui l'a volée pendant que vous dormiez ! Nous partons en randonnée pour apprendre quelques choses.

#### Organiser votre code dans CodePen

Lorsque j'ai travaillé avec CodePen pour la première fois, je me souviens avoir tout mon code dans la section HTML de mon Pen. Tout comme l'image ci-dessous, j'avais mon HTML, CSS et le contenu de <head> tout au même endroit.

![Image](https://cdn-media-1.freecodecamp.org/images/Pnn8Fy-edz-6KRoRVbk07eOESGIfThundWDt)

Il n'y a absolument rien de mal à construire votre site web comme cela. Mais dans CodePen, il existe des moyens de nettoyer votre code pour le rendre plus organisé et lisible par les autres qui vous aident ou qui consultent simplement votre projet génial.

Vous pouvez ouvrir ce pen dans un autre onglet en cliquant [ici](http://codepen.io/michaelhenderson/pen/JKYYWz). Cela vous permettra de jouer avec le code et de suivre.

#### Supprimons quelques éléments

```
<!-- Supprimer les lignes de code suivantes de la section Html --> 
```

```
<!DOCTYPE html>
```

```
<html lang="en">
```

```
</html>
```

Nous n'avons pas besoin de ces morceaux de code car CodePen les injecte automatiquement dans notre projet.

#### Suivez ces étapes pour placer correctement le contenu de votre head là où il doit aller dans CodePen.

Déplaçons notre contenu meta et les liens de polices Google vers la partie Stuff For <head> de CodePen.

Voici un aperçu du code entre les balises head. Vous ne devez déplacer que le code que j'ai en gras.

```
<head>  <! — Theme Made By www.w3schools.com — No Copyright --> <title>Bootstrap Theme Company Page</title> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1"> <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"> <link href="http://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css"> <link href="http://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css"> <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script> <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script> <style> body { font: 400 15px Lato, sans-serif; line-height: 1.8; color: #818181; } h2 { font-size: 24px; text-transform: uppercase; color: #303030; font-weight: 600; margin-bottom: 30px; } h4 { font-size: 19px; line-height: 1.375em; color: #303030; font-weight: 400; margin-bottom: 30px; }  .jumbotron { background-color: #f4511e; color: #fff; padding: 100px 25px; font-family: Montserrat, sans-serif; } .container-fluid { padding: 60px 50px; } .bg-grey { background-color: #f6f6f6; } .logo-small { color: #f4511e; font-size: 50px; } .logo { color: #f4511e; font-size: 200px; } .thumbnail { padding: 0 0 15px 0; border: none; border-radius: 0; } .thumbnail img { width: 100%; height: 100%; margin-bottom: 10px; } .carousel-control.right, .carousel-control.left { background-image: none; color: #f4511e; } .carousel-indicators li { border-color: #f4511e; } .carousel-indicators li.active { background-color: #f4511e; } .item h4 { font-size: 19px; line-height: 1.375em; font-weight: 400; font-style: italic; margin: 70px 0; } .item span { font-style: normal; } .panel { border: 1px solid #f4511e;  border-radius:0 !important; transition: box-shadow 0.5s; } .panel:hover { box-shadow: 5px 0px 40px rgba(0,0,0, .2); } .panel-footer .btn:hover { border: 1px solid #f4511e; background-color: #fff !important; color: #f4511e; } .panel-heading { color: #fff !important; background-color: #f4511e !important; padding: 25px; border-bottom: 1px solid transparent; border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px; } .panel-footer { background-color: white !important; } .panel-footer h3 { font-size: 32px; } .panel-footer h4 { color: #aaa; font-size: 14px; } .panel-footer .btn { margin: 15px 0; background-color: #f4511e; color: #fff; } .navbar { margin-bottom: 0; background-color: #f4511e; z-index: 9999; border: 0; font-size: 12px !important; line-height: 1.42857143 !important; letter-spacing: 4px; border-radius: 0; font-family: Montserrat, sans-serif; } .navbar li a, .navbar .navbar-brand { color: #fff !important; } .navbar-nav li a:hover, .navbar-nav li.active a { color: #f4511e !important; background-color: #fff !important; } .navbar-default .navbar-toggle { border-color: transparent; color: #fff !important; } footer .glyphicon { font-size: 20px; margin-bottom: 20px; color: #f4511e; } .slideanim {visibility:hidden;} .slide { animation-name: slide; -webkit-animation-name: slide; animation-duration: 1s; -webkit-animation-duration: 1s; visibility: visible; } @keyframes slide { 0% { opacity: 0; -webkit-transform: translateY(70%); }  100% { opacity: 1; -webkit-transform: translateY(0%); } } @-webkit-keyframes slide { 0% { opacity: 0; -webkit-transform: translateY(70%); }  100% { opacity: 1; -webkit-transform: translateY(0%); } } @media screen and (max-width: 768px) { .col-sm-4 { text-align: center; margin: 25px 0; } .btn-lg { width: 100%; margin-bottom: 35px; } } @media screen and (max-width: 480px) { .logo { font-size: 150px; } } </style></head> 
```

1. Cliquez sur le bouton des paramètres.

![Image](https://cdn-media-1.freecodecamp.org/images/J-dNXpP4nW5KdDylY44TOoninHli-w2zWpqN)

2. Cliquez sur HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/QDaEwufhU6YL-RGbiM29u2b1-rBWL-mv0M0d)

3. Collez le contenu dans **Stuff for <head>**. Une fois terminé, cliquez sur Enregistrer et Fermer.

![Image](https://cdn-media-1.freecodecamp.org/images/WcGiL7cAL-kTnSPzSs52kKRo7l6FvV4PJu6Z)

#### Maintenant, déplaçons notre CSS là où il doit être

1. Copiez tout ce qui se trouve entre vos balises d'ouverture et de fermeture de style et collez-le dans la section CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/2xQkav2jsa4YESpLd8Nypuh3gxT5Yt3O8JvL)

Votre HTML et CSS sont maintenant séparés. Cela crée un environnement de travail organisé et efficace. Veuillez noter : Vous n'avez pas besoin de mettre de balises <styles> dans votre section CSS.

#### Ajout de la feuille de style [Bootstrap](http://getbootstrap.com/) à votre projet

1. Cliquez sur Paramètres.
2. Cliquez sur **CSS**.

![Image](https://cdn-media-1.freecodecamp.org/images/Yq9cSbJf5zXZhjOq12cqL0Sc9se0eBj08fnt)

3. Cliquez sur la flèche déroulante en bas où il est écrit « Quick-add » et sélectionnez bootstrap. Il l'ajoutera à vos liens CSS externes.

![Image](https://cdn-media-1.freecodecamp.org/images/SHf7jB9EkftdjwJiUZiN9PweMmQlkJELV3Zv)

**Astuce rapide :** Vous pouvez également ajouter Font Awesome comme feuille de style externe. Lisez le contenu sous **Add External CSS**.

#### **Ajout de JavaScript**

1. Toujours dans les paramètres, cliquez sur **JavaScript**.

![Image](https://cdn-media-1.freecodecamp.org/images/jcY8YK1XjUMoDDRXGevFnosAeXkZzSPtGZOl)

2. Cliquez sur le menu déroulant « Quick-add » et ajoutez jQuery et Bootstrap.

3. Cliquez sur Enregistrer et Fermer.

#### Déplacement de notre JavaScript de la section HTML

1. Faites défiler vers le bas et copiez le code javascript entre vos balises de script.

```
<script>$(document).ready(function(){ // Ajouter un défilement fluide à tous les liens dans la barre de navigation + lien de pied de page $(".navbar a, footer a[href=\'#myPage\']").on('click', function(event) { // Assurez-vous que this.hash a une valeur avant de remplacer le comportement par défaut if (this.hash !== "") { // Empêcher le comportement de clic d'ancre par défaut event.preventDefault();
```

```
// Stocker le hash var hash = this.hash;
```

```
// Utilisation de la méthode animate() de jQuery pour ajouter un défilement de page fluide // Le nombre optionnel (900) spécifie le nombre de millisecondes nécessaires pour faire défiler jusqu'à la zone spécifiée $('html, body').animate({ scrollTop: $(hash).offset().top }, 900, function(){  // Ajouter le hash (#) à l'URL une fois le défilement terminé (comportement de clic par défaut) window.location.hash = hash; }); } // Fin si });  $(window).scroll(function() { $(".slideanim").each(function(){ var pos = $(this).offset().top;
```

```
var winTop = $(window).scrollTop(); if (pos < winTop + 600) { $(this).addClass("slide"); } }); });})</script>
```

2. Collez-le dans la section JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/jUa76cLdstSRJbQ3Zus9kJ92ZACT34YANJeQ)

#### Finalisation

Maintenant que votre HTML, CSS et JavaScript sont séparés, vous avez un environnement de travail plus organisé dans CodePen. Cela facilite également l'aide des autres dans le Forum Free Code Camp, car ils peuvent localiser votre code et diagnostiquer facilement les erreurs. Jouez avec les paramètres de CodePen et voyez ce que vous pouvez faire d'autre.

La prochaine fois que vous construirez un projet dans CodePen, vous saurez comment ajouter des feuilles de style, où placer correctement le contenu <head>, comment ajouter une bibliothèque JavaScript et comment séparer votre HTML, CSS et JavaScript. J'espère que cela aide !

J'ai également une [vidéo](http://forum.freecodecamp.com/t/codepen-tips-for-building-your-projects/5824) expliquant comment faire certaines de ces choses aussi.

Bon codage mes amis !

Si vous avez aimé cet article, faites-le nous savoir dans les commentaires.

N'hésitez pas à consulter ma [chaîne YouTube](https://www.youtube.com/channel/UC_Dn6rTbbVggWONZtgzVHIQ) où je fais des choses cool comme passer en revue des projets et partager ma vie en tant qu'ingénieur logiciel.