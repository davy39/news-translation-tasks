---
title: Comment créer un site portfolio avec HTML, CSS, JavaScript et Bootstrap 5
date: '2022-01-25T17:10:50.000Z'
author: freeCodeCamp
authorURL: https://www.freecodecamp.org/news/author/sampurna/
originalURL: https://freecodecamp.org/news/how-to-create-a-portfolio-website-using-html-css-javascript-and-bootstrap
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Untitled-design-6.png
tags:
- name: Bootstrap 5
  slug: bootstrap-5
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: portfolio
  slug: portfolio
- name: Web Development
  slug: web-development
seo_desc: 'By Sampurna Chapagain

  If you are a web developer or a web designer, it is essential for you to have a
  portfolio website. It lets you provide information about yourself and showcase your
  best work with your relevant skills and experience.

  In this blog...'
---


Si vous êtes un développeur web ou un concepteur web, il est essentiel pour vous d'avoir un site portfolio. Il vous permet de fournir des informations sur vous-même et de présenter vos meilleurs travaux avec vos compétences et votre expérience pertinentes.

<!-- more -->

Dans cet article de blog, je vais aborder certains des avantages de la création d'un site portfolio. Ensuite, je vous montrerai comment créer un magnifique site portfolio responsive pour vous-même en utilisant HTML, CSS, JavaScript et Bootstrap version 5.

### Voici un scrim interactif sur la façon de créer un site portfolio avec HTML, CSS, JS et Bootstrap 5 :

<iframe src="https://scrimba.com/scrim/co27f4302abab219aea652cf7?embed=freecodecamp,mini-header" width="100%" height="480" title="Embedded content" loading="lazy"></iframe>

## Table des matières

-   [Avantages d'avoir un site portfolio][1]
-   [Qu'est-ce que Bootstrap][2] ?
-   [Structure des dossiers][3]
-   [Comment ajouter un menu de navigation à votre portfolio][4]
-   [Comment ajouter un en-tête Hero au portfolio][5]
-   [Comment créer la section À propos][6]
-   [Comment créer la section Services][7]
-   [Comment ajouter une couleur d'arrière-plan sombre à la barre de navigation lors du défilement][8]
-   [Comment construire la section Portfolio][9]
-   [Comment construire la section Contact][10]
-   [Comment construire la section Pied de page][11]
-   [Touches finales][12]
-   [Conclusion][13]

## Avantages d'avoir un site portfolio

Avoir un site portfolio présente plusieurs avantages, notamment :

-   il fournit une plateforme pour présenter vos compétences et votre expérience pertinentes
-   il montre votre personnalité
-   il permet aux recruteurs de vous trouver au lieu que vous ne les contactiez
-   vous êtes facilement trouvable sur les moteurs de recherche comme Google

## Qu'est-ce que Bootstrap ?

Bootstrap est un framework CSS front-end populaire qui est utilisé pour développer des sites web responsive et adaptés aux mobiles. La dernière version de Bootstrap est la version 5. Vous pouvez trouver la documentation officielle de Bootstrap 5 [ici][14].

## Structure des dossiers

Nous allons maintenant commencer à travailler sur la création du site portfolio.

Tout d'abord, créons la structure des dossiers. Vous pouvez obtenir les fichiers de base du projet sur [GitHub][15]. De plus, vous pouvez vous rendre [ici][16] pour voir la démo en direct de ce projet.

![Capture-d-ecran-du-2022-01-22-19-10-25](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-from-2022-01-22-19-10-25.png)

Structure des dossiers du projet

La structure des dossiers se compose des fichiers index.html, style.css et script.js, ainsi que d'un dossier images. Nous écrirons tout le CSS dans le fichier style.css et le JavaScript dans le fichier script.js.

Dans le fichier index.html, vous pouvez voir le code boilerplate HTML avec le CDN Bootstrap, le [kit font awesome][17], et un lien vers la feuille de style externe et le JavaScript.

Ici, le fichier script.js est chargé après le chargement de tout le code HTML.

## Comment ajouter un menu de navigation à votre portfolio

Travaillons maintenant à l'ajout d'un menu de navigation dans notre projet. Cela aidera les visiteurs à trouver les informations pertinentes qu'ils recherchent.

Nous utiliserons la classe `fixed-top` de Bootstrap dans l'élément nav pour maintenir la navbar en haut de la page. La navbar possède également une classe `navbar-brand` où nous gardons le nom de la personne comme marque.

```html
<nav class="navbar navbar-expand-lg fixed-top navbarScroll">
        <div class="container">
            <a class="navbar-brand" href="#">Brad</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item active">
                        <a class="nav-link" href="#home">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#services">Services</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#portfolio">Portfolio</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#contact">Contact</a>
                    </li>
                </ul>
                
            </div>
        </div>
    </nav>
```

La navbar possède les fonctionnalités suivantes :

-   Elle a six liens : home, about, services, portfolio, contact et footer
-   Elle a un arrière-plan transparent. Nous ajouterons un arrière-plan sombre lors du défilement de la page plus tard.
-   Elle se réduit sur les petits appareils

Vous pouvez trouver plus de détails concernant les fonctionnalités de la navbar Bootstrap 5 [ici][18].

Cependant, la navbar a un problème lors du défilement. Elle est entièrement transparente sur toute la page, ce qui cause des problèmes de lisibilité. Nous corrigerons ce problème après avoir terminé la [section Services][19] pour vous faire comprendre le problème correctement.

## Comment ajouter un en-tête Hero au portfolio

Maintenant, nous allons ajouter une image hero avec du texte au centre. Une image hero est un terme de conception web qui fait référence à une image de haute qualité en pleine largeur qui affiche les objectifs principaux de l'entreprise ou de l'individu, une image représentative, une photo ou d'autres éléments accrocheurs. Elle aide à attirer les utilisateurs sur votre site.

```html
 <!-- main banner -->
    <section class="bgimage" id="home">
        <div class="container-fluid">
            <div class="row">
            <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12 hero-text">
                <h2 class="hero_title">Hi, it's me Brad</h2>
                <p class="hero_desc">I am a professional freelancer in New York City</p>
            </div>
            </div>
        </div>
    </section>
```

Ajoutons également le CSS pour le code ci-dessus dans le fichier style.css :

```css
/* hero background image */
.bgimage {
    height:100vh;
    background: url('images/heroImage.jpeg');
    background-size:cover;
    position:relative;
}
/* text css above hero image*/
.hero_title {
    font-size: 4.5rem;
}
.hero_desc {
    font-size: 2rem;
}
.hero-text {
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
}
```

Ici, nous pouvons voir que la section a un id nommé `bgimage` qui est responsable de l'affichage de l'image hero d'arrière-plan en pleine largeur. Elle affiche également du texte au centre au-dessus de l'image d'arrière-plan à l'aide du CSS ci-dessus.

Voici à quoi ressemble le site jusqu'à présent avec la navbar et la section hero :

![Capture-d-ecran-du-2022-01-25-10-13-25](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-from-2022-01-25-10-13-25.png)

Image Hero avec barre de navigation

## Comment créer la section À propos

La page À propos contient des informations importantes sur vous et votre parcours. Les visiteurs de votre site portfolio peuvent apprendre à vous connaître grâce aux informations que vous fournissez sur cette page.

Nous ajouterons une image sur le côté gauche de la ligne, et sur le côté droit, nous ajouterons notre introduction rapide dans cette section. Démonstration avec le code ci-dessous :

```html
<!-- about section-->
    <section id="about">
        <div class="container mt-4 pt-4">
            <h1 class="text-center">About Me</h1>
            <div class="row mt-4">
                <div class="col-lg-4">
                    <img src="images/about.jpeg" class= "imageAboutPage" alt="">
                </div>

                <div class="col-lg-8">
                    <p> Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged
                        
                    </p>
                    <div class="row mt-3">
                        <div class="col-md-6">
                            <ul>
                                <li>Name: David Parker</li>
                                <li>Age: 28</li>
                                <li>Occupation: Web Developer</li>

                            </ul>
                        </div>
                        <div class="col-md-6">
                            <ul>
                                <li>Name: David Parker</li>
                                <li>Age: 28</li>
                                <li>Occupation: Web Developer</li>

                            </ul>
                        </div>
                    </div>
                    <div class="row mt-3">
                        <p> Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
                            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
                        </p>
                    </div>
                </div>
            </div>
    </section>
```

Ajoutons un peu de CSS pour l'image de gauche :

```css
/* about section image css */
.imageAboutPage {
    width: 100%;
}
```

Cela créera une section à propos. Vous pouvez modifier le contenu en fonction de vos besoins. Nous avons ajouté des classes nommées `mt-4` et `pt-4` avec la classe container, ce qui définira la marge supérieure et le padding supérieur à 1.5 rem.

La ligne a deux colonnes. L'une a la classe `col-lg-4` pour afficher l'image qui occupera la colonne de gauche avec une grille de 4 parties pour les grands écrans.

La colonne suivante se voit attribuer une classe `col-lg-8` qui occupera la colonne de droite avec une grille de 8 parties pour les écrans plus larges. Pour les écrans moyens et petits, elles se superposeront, ce que nous pouvons voir dans le fichier GIF ci-dessous :

![a-propos](https://www.freecodecamp.org/news/content/images/2022/01/about.gif)

Section À propos

## Comment créer la section Services

Cette section aide à convertir les visiteurs du site en clients potentiels. C'est ici que vous expliquez quels services spécifiques vous proposez, et où vous [ciblez][20] vos services offerts.

Ajoutons le code pour cette section et décrivons-le ci-dessous :

```html
<!-- services section-->
    <section id="services">
        <div class="container">
            <h1 class="text-center">Services</h1>
            <div class="row">
                <div class="col-lg-4 mt-4">
                    <div class="card servicesText">
                        <div class="card-body">
                            <i class="fas servicesIcon fa-clock"></i>
                            <h4 class="card-title mt-3">Website Development</h4>
                            <p class="card-text mt-3">Some quick example text to build on the card title and make up the bulk of the card's content.
                                Some quick example text to build on the card title and make up the bulk of the card's content.
                            </p>
                        </div>
                    </div>  
                </div>
                <div class="col-lg-4 mt-4">
                    <div class="card servicesText">
                        <div class="card-body">
                            <i class='fas servicesIcon fa-layer-group'></i>
                            <h4 class="card-title mt-3">Website Design</h4>
                            <p class="card-text mt-3">Some quick example text to build on the card title and make up the bulk of the card's content.
                                Some quick example text to build on the card title and make up the bulk of the card's content.
                            </p>
                        </div>
                    </div>  
                </div>

                <div class="col-lg-4 mt-4">
                    <div class="card servicesText">
                        <div class="card-body">
                            <i class='far servicesIcon fa-check-circle'></i>
                            <h4 class="card-title mt-3">Website Deployment</h4>
                            <p class="card-text mt-3">Some quick example text to build on the card title and make up the bulk of the card's content.
                                Some quick example text to build on the card title and make up the bulk of the card's content.
                            </p>
                        </div>
                    </div>  
                </div>
            </div>

            <div class="row">
                <div class="col-lg-4 mt-4">
                    <div class="card servicesText">
                        <div class="card-body">
                            <i class='fas servicesIcon fa-search'></i>
                            <h4 class="card-title mt-3">SEO</h4>
                            <p class="card-text mt-3">Some quick example text to build on the card title and make up the bulk of the card's content.
                                Some quick example text to build on the card title and make up the bulk of the card's content.
                            </p>
                        </div>
                    </div>  
                </div>

                <div class="col-lg-4 mt-4">
                    <div class="card servicesText">
                        <div class="card-body">
                            <i class='fas servicesIcon fa-shield-alt'></i>
                            <h4 class="card-title mt-3">DevOps</h4>
                            <p class="card-text mt-3">Some quick example text to build on the card title and make up the bulk of the card's content.
                                Some quick example text to build on the card title and make up the bulk of the card's content.
                            </p>
                        </div>
                    </div>  
                </div>

                <div class="col-lg-4 mt-4">
                    <div class="card servicesText">
                        <div class="card-body">
                            <i class='fas servicesIcon fa-wrench'></i>
                            <h4 class="card-title mt-3">QA</h4>
                            <p class="card-text mt-3">Some quick example text to build on the card title and make up the bulk of the card's content.
                                Some quick example text to build on the card title and make up the bulk of the card's content.
                            </p>
                        </div>
                    </div>  
                </div>
            </div>
        </div>
    </section>
```

Comme ce site est destiné aux développeurs et concepteurs web, j'ai inclus certains des services qu'un développeur ou concepteur web pourrait proposer.

Nous avons utilisé des cartes Bootstrap pour afficher les services. Notre section services comporte 2 lignes et 3 colonnes chacune. Pour les grands écrans d'une largeur supérieure ou égale à 992px, trois cartes sont affichées par ligne. Pour les écrans de moins de 992px de large, une seule carte est affichée par ligne.

Vous pouvez en savoir plus sur les points de rupture (breakpoints) de Bootstrap [ici][21].

De plus, des polices d'icônes ont été ajoutées dans chaque carte pour les rendre plus attrayantes.

Sans CSS, la section services ressemblerait à ceci :

![Capture-d-ecran-du-2022-01-23-14-01-00](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-from-2022-01-23-14-01-00.png)

Ajoutons donc un peu de CSS pour augmenter la taille de la police des icônes et la hauteur des cartes, et ajouter une couleur supplémentaire lorsqu'un utilisateur survole une carte.

```css
/* services section css */
.servicesText.card {
    height: 280px;
    cursor: pointer;
  }
.servicesIcon {
    font-size: 36px;
    text-align: center;
    width: 100%;
}
.card-title {
    text-align: center;
}
.card:hover .servicesIcon {
    color: #008000;
}
.servicesText:hover {
    border: 1px solid #008000;
}
```

Voici à quoi ressemble notre section services maintenant :

![services](https://www.freecodecamp.org/news/content/images/2022/01/services.gif)

Services 

## Comment ajouter une couleur d'arrière-plan sombre à la barre de navigation lors du défilement

Si vous regardez attentivement le gif ci-dessus, vous verrez que la barre de navigation est transparente sur toute la page, ce qui cause des problèmes de lisibilité. Travaillons donc à la résolution de ce problème.

Nous allons écrire un peu de JavaScript et de CSS afin de résoudre ce problème. Nous ajouterons une classe `navbarDark` afin d'afficher une couleur d'arrière-plan sombre pour la barre de navigation lors du défilement de la page.

Pour cela, nous devons aller dans le fichier script.js et ajouter le code suivant :

```javascript
// add class navbarDark on navbar scroll
const header = document.querySelector('.navbar');

window.onscroll = function() {
    var top = window.scrollY;
    if(top >=100) {
        header.classList.add('navbarDark');
    }
    else {
        header.classList.remove('navbarDark');
    }
}
```

Décomposons maintenant le code ci-dessus :

-   `header` contient la valeur de l'élément nav puisque la méthode `querySelector` renvoie le premier élément qui correspond au sélecteur CSS (qui est `.navbar` dans ce cas).
-   `window.onscroll` se déclenche lorsque l'événement de défilement se produit.
-   `window.scrollY` renvoie le nombre de pixels dont le document a été défilé verticalement et sa valeur est assignée à une variable nommée `top`.
-   Si la valeur de `top` est supérieure ou égale à 100, cela ajoute une classe `navbarDark` au header.

Ajoutons rapidement le CSS pour la classe `navbarDark`. Pour cela, allez dans votre fichier style.css et ajoutez le code suivant :

```css
/* display background color black on navbar scroll */
.navbarScroll.navbarDark {
    background-color: black;
}
```

Voici à quoi ressemblera la barre de navigation maintenant :

![navbar](https://www.freecodecamp.org/news/content/images/2022/01/navbar.gif)

Couleur d'arrière-plan sombre sur la barre de navigation lors du défilement

## Comment construire la section Portfolio

Cette section inclut vos meilleurs travaux. Les gens peuvent voir de quoi vous êtes capable, et présenter des travaux passés solides attirera certainement plus de clients potentiels ou de recruteurs. N'ajoutez donc que vos meilleurs travaux dans cette section.

Nous utiliserons des cartes Bootstrap pour afficher les projets du portfolio. Il y aura 2 lignes et chaque ligne aura 3 colonnes de cartes.

Voici le code pour la section portfolio :

```html
<!-- portfolio section-->
    <section id="portfolio">
        <div class="container mt-3">
            <h1 class="text-center">Portfolio</h1>
            <div class="row">
                <div class="col-lg-4 mt-4">
                    <div class="card">
                        <img class="card-img-top" src="images/portfolioImage1.jpg" alt="Card image" style="width:100%">
                        <div class="card-body">
                            <h4 class="card-title">YouTube Clone</h4>
                            <p class="card-text">Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                            <div class="text-center">
                                <a href="#" class="btn btn-success">Link</a>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 mt-4">
                    <div class="card portfolioContent">
                        <img class="card-img-top" src="images/portfolioImage4.jpg" alt="Card image" style="width:100%">
                        <div class="card-body">
                            <h4 class="card-title">Quiz App</h4>
                            <p class="card-text">Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                            <div class="text-center">
                                <a href="#" class="btn btn-success">Link</a>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 mt-4">
                    <div class="card portfolioContent">
                        <img class="card-img-top" src="images/portfolioImage3.jpg" alt="Card image" style="width:100%">
                        <div class="card-body">
                            <h4 class="card-title">Product Landing Page</h4>
                            <p class="card-text">Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                            <div class="text-center">
                                <a href="#" class="btn btn-success">Link</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-lg-4 mt-4">
                    <div class="card portfolioContent">
                        <img class="card-img-top" src="images/portfolioImage4.jpg" alt="Card image" style="width:100%">
                        <div class="card-body">
                            <h4 class="card-title">Messaging Service</h4>
                            <p class="card-text">Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                            <div class="text-center">
                                <a href="#" class="btn btn-success">Link</a>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 mt-4">
                    <div class="card portfolioContent">
                        <img class="card-img-top" src="images/portfolioImage1.jpg" alt="Card image" style="width:100%">
                        <div class="card-body">
                            <h4 class="card-title">Twitter Clone</h4>
                            <p class="card-text">Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                            <div class="text-center">
                                <a href="#" class="btn btn-success">Link</a>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-4 mt-4">
                    <div class="card portfolioContent">
                        <img class="card-img-top" src="images/portfolioImage4.jpg" alt="Card image" style="width:100%">
                        <div class="card-body">
                            <h4 class="card-title">Blog App</h4>
                            <p class="card-text">Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                            <div class="text-center">
                                <a href="#" class="btn btn-success">Link</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    </section>
```

Chaque carte possède une image, un titre, une description et un lien vers les projets. Trois cartes sont affichées par ligne pour les grands écrans qui ont des points de rupture ≥ 992px de large, mais pour les écrans < 992px de large, une seule carte est affichée par ligne.

Le GIF ci-dessous montre à quoi ressemble la section portfolio maintenant :

![portfolio](https://www.freecodecamp.org/news/content/images/2022/01/portfolio.gif)

Portfolio

## Comment construire la section Contact

Vous devriez inclure vos coordonnées dans cette section afin que les visiteurs puissent vous contacter s'ils souhaitent vous embaucher.

Notre section contact comprendra 2 colonnes dans une seule ligne : Google Maps pour la localisation et un formulaire de contact.

Afin d'intégrer la carte Google, vous devez suivre ces étapes :

-   allez sur [https://www.embed-map.com][22]
-   entrez votre emplacement
-   cliquez sur le bouton **Generate HTML Code** qui vous fournira votre code HTML Google Map

Notre code ressemblera à ceci avec le formulaire de contact inclus :

```html
<!-- contact section-->
    <section id="contact">
        <div class="container mt-3 contactContent">
            <h1 class="text-center">Contact Me</h1>

            <div class="row mt-4">
                <div class="col-lg-6">
                    <!-- to edit google map goto https://www.embed-map.com type your location, generate html code and copy the html  -->
                    <div style="max-width:100%;overflow:hidden;color:red;width:500px;height:500px;">
                        <div id="embedmap-canvas" style="height:100%; width:100%;max-width:100%;">
                            <iframe style="height:100%;width:100%;border:0;" frameborder="0" src="https://www.google.com/maps/embed/v1/place?q=new+york&key=AIzaSyBFw0Qbyq9zTFTd-tUY6dZWTgaQzuU17R8">
                            </iframe>
                        </div>
                        <a class="googlemaps-html" href="https://www.embed-map.com" id="get-data-forembedmap">https://www.embed-map.com</a>
                        <style>#embedmap-canvas img{max-width:none!important;background:none!important;font-size: inherit;font-weight:inherit;}
                        </style>
                    </div>
                </div>

                <div class="col-lg-6">
                    <!-- form fields -->
                    <form>
                        <input type="text" class="form-control form-control-lg" placeholder="Name">
                        <input type="email" class="form-control mt-3" placeholder="Email">
                        <input type="text" class="form-control mt-3" placeholder="Subject">
                        <div class="mb-3 mt-3">
                            <textarea class="form-control" rows="5" id="comment" name="text" placeholder="Project Details"></textarea>
                        </div>
                    </form>
                    <button type="button" class="btn btn-success mt-3">Contact Me</button>
                    
                </div>

            </div>
        </div>
    </section>
```

La première colonne affichera la carte Google et la suivante affichera le formulaire de contact.

Le formulaire comporte quatre champs différents : nom, email, sujet et détails du projet. Le formulaire ne soumet pas la demande lui-même. Vous devrez le connecter à n'importe quel langage back-end. Ou, vous pouvez simplement utiliser [Netlify Form][23] ou [Formspree form][24] pour cela.

Voici comment apparaîtra la section contact :

![Capture-d-ecran-du-2022-01-25-11-31-56](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-from-2022-01-25-11-31-56.png)

Section Contact

## Comment construire la section Pied de page

Nous sommes maintenant arrivés à la dernière section de cet article, qui est le pied de page. Nous avons déjà ajouté un lien vers le CDN Font Awesome dans le fichier index.html.

Dans le pied de page, nous ajouterons des liens vers nos réseaux sociaux via des icônes Font Awesome.

```html
 <!-- footer section-->
    <footer id="footer">
        <div class="container-fluid">
            <!-- social media icons -->
            <div class="social-icons mt-4">
                <a href="https://www.facebook.com/" target="_blank"><i class="fab fa-facebook"></i></a>
                <a href="https://www.instagram.com/" target="_blank"><i class="fab fa-instagram"></i></a>
                <a href="https://www.twitter.com/" target="_blank"><i class="fab fa-twitter"></i></a>
                <a href="https://www.linkedin.com/" target="_blank"><i class="fab fa-linkedin"></i></a>
                <a href="https://www.twitch.tv/" target="_blank"><i class="fab fa-twitch"></i></a>
            </div>
        </div>
    </footer>
```

Sans le CSS, notre pied de page ressemblera à ceci :

![Capture-d-ecran-du-2022-01-23-17-56-37](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-from-2022-01-23-17-56-37.png)

pied de page sans style  

Ajoutons donc un peu de style au pied de page avec ce code :

```css
/* social media icons styling */
.social-icons {
    font-size: 36px;
    cursor: pointer;
}
.fa-facebook:hover,.fa-instagram:hover,.fa-twitter:hover,.fa-linkedin:hover, .fa-twitch:hover {
    color: #008000;
}
.fab {
    color: #000000;
}
/* footer styling */
#footer {
    background-color: #808080;
    text-align: center;
}
```

Les icônes sont maintenant affichées au centre avec un effet de survol que nous pouvons voir dans le fichier GIF ci-dessous.

![pied-de-page](https://www.freecodecamp.org/news/content/images/2022/01/footer.gif)

Pied de page

## Touches finales

Afin d'ajouter de l'espacement entre toutes les sections, ajoutons un peu plus de style :

```css
/* spacing on all sections */
#about, #services, #portfolio, #contact {
    margin-top: 4rem;
    padding-top: 4rem;
}
#contact {
    padding-bottom: 4rem;
}
```

Nous avons maintenant terminé la création de notre site portfolio complet.

Vous pouvez trouver le code source complet de ce projet [ici][25].

## Conclusion

C'est ainsi que vous pouvez créer un site portfolio complet et responsive en utilisant HTML, CSS, JavaScript et Bootstrap 5.

Dans cet article de blog, nous avons vu certains des avantages de la création d'un site portfolio pour les développeurs et concepteurs web. Nous avons divisé l'ensemble du site en différentes sections et discuté de chacune individuellement au fur et à mesure de sa construction.

Vous pouvez personnaliser ce site en fonction de vos propres besoins.

J'espère que vous avez trouvé cet article utile.

Bon codage !

Vous pouvez me trouver sur [Twitter][26] pour du contenu quotidien concernant le développement Web.

[1]: #heading-avantages-d-avoir-un-site-portfolio
[2]: #heading-qu-est-ce-que-bootstrap
[3]: #heading-structure-des-dossiers
[4]: #heading-comment-ajouter-un-menu-de-navigation-a-votre-portfolio
[5]: #heading-comment-ajouter-un-en-tete-hero-au-portfolio
[6]: #heading-comment-creer-la-section-a-propos
[7]: #heading-comment-creer-la-section-services
[8]: #heading-comment-ajouter-une-couleur-d-arriere-plan-sombre-a-la-barre-de-navigation-lors-du-defilement
[9]: #heading-comment-construire-la-section-portfolio
[10]: #heading-comment-construire-la-section-contact
[11]: #heading-comment-construire-la-section-pied-de-page
[12]: #heading-touches-finales
[13]: #heading-conclusion
[14]: https://getbootstrap.com/docs/5.0/getting-started/introduction/
[15]: https://github.com/SampurnaC/portfolio_website_fcc/tree/portfolio-starter-files
[16]: https://brad-portfolio.netlify.app/
[17]: https://fontawesome.com/
[18]: https://getbootstrap.com/docs/5.0/components/navbar/
[19]: #heading-comment-creer-la-section-services
[20]: https://www.freecodecamp.org/news/web-design-niche/
[21]: https://getbootstrap.com/docs/5.0/layout/breakpoints/
[22]: https://www.embed-map.com/
[23]: https://www.netlify.com/products/forms/
[24]: https://formspree.io/
[25]: https://github.com/SampurnaC/portfolio_website_fcc/tree/master
[26]: https://twitter.com/saam_codes