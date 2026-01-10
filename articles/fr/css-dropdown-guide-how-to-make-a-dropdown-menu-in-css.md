---
title: 'Guide CSS des menus déroulants : Comment créer un menu déroulant en CSS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-08T22:33:00.000Z'
originalURL: https://freecodecamp.org/news/css-dropdown-guide-how-to-make-a-dropdown-menu-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/99-films-t1tAOh-CaZ4-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: toothbrush
  slug: toothbrush
seo_title: 'Guide CSS des menus déroulants : Comment créer un menu déroulant en CSS'
seo_desc: "What are Dropdowns?\nDropdown menus are used in CSS to hide a predefined\
  \ list within a button.\nExamples:\n<div class=\"dropdown\">\n  <button class=\"\
  dropbtn\">Name</button>\n  <div class=\"dropdownContent\">\n    <a href=\"#\">One</a>\n\
  \    <a href=\"#\">Two</a>\n   ..."
---

## **Qu'est-ce qu'un menu déroulant ?**

Les menus déroulants sont utilisés en CSS pour masquer une liste prédéfinie dans un bouton.

Exemples :

```html
<div class="dropdown">
  <button class="dropbtn">Nom</button>
  <div class="dropdownContent">
    <a href="#">Un</a>
    <a href="#">Deux</a>
    <a href="#">Trois</a>
  </div>
</div>
```

Ensuite, vous devez personnaliser les classes en CSS comme ceci :

```css
.dropdown {
  position: relative;
  display: inline-block;
}

.dropbtn {
  background-color: red;
  padding: 10px;
}

.dropdown-content {
  display: none;
  position: absolute;
}

.dropdown:hover .dropdown-content {
  display:block;
}
```

Vous avez besoin des classes div séparées pour créer le bouton, et une autre div pour séparer la liste de ce que le bouton contient.

### Un exemple

```html
<div id="container">
  
        <div id="myNav1" class="overlay">
  
            <div class="overlay-content" id="myNav1-content">
  
                <div>
                    <a href="#" id="list1_obj1" class="list1" >Contenu 1</a>
                </div>
                <div>
                    <a href="#" id="list1_obj2" class="list1" >Contenu 2</a>
                </div>
  
            </div>
  
         </div>
  
         <div id="myNav2" class="overlay">
  
             <a href="javascript:void(10)" class="closebtn" onclick="closeNav()">&times</a>
            <div class="overlay-content" id="myNav2-content">
  
                <div>
                    <a href="#" id="list2_obj1" class="list2" >Contenu 3</a>
                </div>
                <div>
                   <a href="#" id="list2_obj2" class="list2" >Contenu 4</a>
                </div>
                <div>
                  <a href="#" id="list2_obj3" class="list2" >Contenu 5</a>
                </div>
  
            </div>
  
         </div>
  
 </div>
```

```css
#myNav1 {
    height: 0;
    width: 50%;
    position: fixed;
    z-index: 6;
    top: 0;
    left: 0;
    background-color: #ffff;
    overflow: hidden;
    transition: 0.3s;
    opacity: 0.85;
}

#myNav2 {
    height: 0;
    width: 50%;
    position: fixed;
    z-index: 6;
    bottom: 0;
    right: 0;
    background-color: #ffff;
    overflow: hidden;
    transition: 0.3s;
    opacity: 0.85;
}

.overlay-content {
    position: relative;
    width: 100%;
    text-align: center;
    margin-top: 30px;
}

#myNav1-content{
    top: 12%;
    left: 5%;
    display: none;
}

#myNav2-content{
    top: 12%;
    right: 10%;
    display: none;   
}
```

## Plus d'informations sur les menus déroulants CSS :

* [Comment créer un menu déroulant avec CSS et JavaScript](https://www.freecodecamp.org/news/how-to-create-a-dropdown-menu-with-css-and-javascript/)