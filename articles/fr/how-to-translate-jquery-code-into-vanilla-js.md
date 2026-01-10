---
title: Comment traduire le code jQuery en Vanilla JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:15:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-translate-jquery-code-into-vanilla-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa7740569d1a4ca26e2.jpg
tags:
- name: JavaScript
  slug: javascript
- name: jQuery
  slug: jquery
- name: js
  slug: js
- name: toothbrush
  slug: toothbrush
seo_title: Comment traduire le code jQuery en Vanilla JS
seo_desc: 'jQuery was once one of the most popular JS libraries available. It solved
  a lot of problems, like making DOM manipulation and Ajax calls standard across all
  the different browsers, which all handled JavaScript slightly differently.

  A lot of jQuery''s ...'
---

jQuery était autrefois l'une des bibliothèques JS les plus populaires disponibles. Elle a résolu de nombreux problèmes, comme la standardisation de la manipulation du DOM et des appels Ajax sur tous les différents navigateurs, qui traitaient tous JavaScript légèrement différemment.

De nombreuses fonctionnalités autrefois innovantes de jQuery ont été intégrées dans JavaScript vanilla, il n'est donc plus nécessaire de charger une bibliothèque entière pour seulement quelques fonctionnalités. Étant donné cela, il n'est pas rare que l'une de vos tâches au travail consiste à réécrire jQuery en JavaScript vanilla.

### Comment réécrire jQuery en vanilla JS

Imaginez que vous avez le code suivant :

```html
<div class="m1 menu">
    <div id="menu-center">
        <ul>
            <li><a class="active" href="#home">Accueil</a>

            </li>
            <li><a href="#portfolio">Portfolio</a>

            </li>
            <li><a href="#about">À propos</a>

            </li>
            <li><a href="#contact">Contact</a>

            </li>
        </ul>
    </div>
</div>
<div id="home"></div>
<div id="portfolio"></div>
<div id="about"></div>
<div id="contact"></div>
```

```css
body, html {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
}
.menu {
    width: 100%;
    height: 75px;
    background-color: rgba(0, 0, 0, 1);
    position: fixed;
    background-color:rgba(4, 180, 49, 0.6);
    -webkit-transition: all 0.3s ease;
    -moz-transition: all 0.3s ease;
    -o-transition: all 0.3s ease;
    transition: all 0.3s ease;
}
.light-menu {
    width: 100%;
    height: 75px;
    background-color: rgba(255, 255, 255, 1);
    position: fixed;
    background-color:rgba(4, 180, 49, 0.6);
    -webkit-transition: all 0.3s ease;
    -moz-transition: all 0.3s ease;
    -o-transition: all 0.3s ease;
    transition: all 0.3s ease;
}
#menu-center {
    width: 980px;
    height: 75px;
    margin: 0 auto;
}
#menu-center ul {
    margin: 15px 0 0 0;
}
#menu-center ul li {
    list-style: none;
    margin: 0 30px 0 0;
    display: inline;
}
.active {
    font-family:'Droid Sans', serif;
    font-size: 14px;
    color: #fff;
    text-decoration: none;
    line-height: 50px;
}
a {
    font-family:'Droid Sans', serif;
    font-size: 14px;
    color: black;
    text-decoration: none;
    line-height: 50px;
}
#home {
    background-color: grey;
    height: 100%;
    width: 100%;
    overflow: hidden;
    background-image: url(images/home-bg2.png);
}
#portfolio {
    background-image: url(images/portfolio-bg.png);
    height: 100%;
    width: 100%;
}
#about {
    background-color: blue;
    height: 100%;
    width: 100%;
}
#contact {
    background-color: red;
    height: 100%;
    width: 100%;
}
```

```js
$(document).ready(function () {
    $(document).on("scroll", onScroll);
    
    //défilement fluide
    $('a[href^="#"]').on('click', function (e) {
        e.preventDefault();
        $(document).off("scroll");
        
        $('a').each(function () {
            $(this).removeClass('active');
        })
        $(this).addClass('active');
      
        var target = this.hash,
            menu = target;
        $target = $(target);
        $('html, body').stop().animate({
            'scrollTop': $target.offset().top+2
        }, 500, 'swing', function () {
            window.location.hash = target;
            $(document).on("scroll", onScroll);
        });
    });
});

function onScroll(event){
    var scrollPos = $(document).scrollTop();
    $('#menu-center a').each(function () {
        var currLink = $(this);
        var refElement = $(currLink.attr("href"));
        if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
            $('#menu-center ul li a').removeClass("active");
            currLink.addClass("active");
        }
        else{
            currLink.removeClass("active");
        }
    });
}
```

Lorsque vous faites défiler la page vers le bas, la barre de navigation doit changer de couleur lorsque vous atteignez différentes sections :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Peek-2020-05-25-18-44.gif)

La fonction qui gère cela est `onScroll` :

```js
function onScroll(event){
    var scrollPos = $(document).scrollTop();
    /* console.log(scrollPos); */
    $('#menu-center a').each(function () {
        var currLink = $(this);
        var refElement = $(currLink.attr("href"));
        if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
            $('#menu-center ul li a').removeClass("active");
            currLink.addClass("active");
        }
        else{
            currLink.removeClass("active");
        }
    });
}
```

Pour traduire `onScroll` en vanilla JS, vous avez plusieurs options.

### Option #1 : Utiliser un compilateur en ligne

Vous pouvez utiliser un outil en ligne comme le [Closure Compiler](https://closure-compiler.appspot.com/) de Google pour compresser le code et supprimer tout jQuery inutile.

Le problème est que vous avez toujours essentiellement du code jQuery, donc le navigateur devrait toujours charger la bibliothèque.

### Option #2 : Traduire manuellement le code

La meilleure option est de consulter des ressources comme [You Don't Need jQuery](https://github.com/nefe/You-Dont-Need-jQuery) et [You Might Not Need jQuery](http://youmightnotneedjquery.com/) avant de réécrire votre code jQuery. Vous pourrez trouver les versions natives JS des méthodes jQuery les plus populaires, dont certaines peuvent être utilisées dans votre propre code.

Voici la fonction `onScroll` en vanilla JS :

```js
function onScroll(event) {
  var sections = [...document.querySelectorAll('#menu-center a')];
  var scrollPos = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
  sections.forEach(function(currLink) {
    var val = currLink.getAttribute('href');
    var refElement = document.querySelector(val);
    if (refElement.offsetTop <= scrollPos && (refElement.offsetTop + refElement.offsetHeight > scrollPos)) {
      //document.querySelector('#menu-center ul li a').classList.remove('active');
      currLink.classList.add('active');
    } else {
      currLink.classList.remove('active');
    }
  });
}

document.addEventListener('scroll', onScroll);
```