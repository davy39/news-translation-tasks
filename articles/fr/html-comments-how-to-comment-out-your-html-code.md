---
title: 'Commentaires HTML : Comment commenter votre code HTML'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-30T21:47:00.000Z'
originalURL: https://freecodecamp.org/news/html-comments-how-to-comment-out-your-html-code
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d42740569d1a4ca36c2.jpg
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: toothbrush
  slug: toothbrush
seo_title: 'Commentaires HTML : Comment commenter votre code HTML'
seo_desc: 'Comments in HTML

  The comment tag is an element used to leave notes, mostly related to the project
  or the website. This tag is frequently used to explain something in the code or
  leave some recommendations about the project. The comment tag also makes...'
---

## **Commentaires en HTML**

La balise de commentaire est un élément utilisé pour laisser des notes, généralement liées au projet ou au site web. Cette balise est fréquemment utilisée pour expliquer quelque chose dans le code ou laisser des recommandations sur le projet. La balise de commentaire facilite également le retour du développeur pour comprendre le code qu'il a écrit à une date ultérieure. Les commentaires peuvent également être utilisés pour commenter des lignes de code à des fins de débogage.

Il est bon de pratique d'ajouter des commentaires à votre code, surtout lorsque vous travaillez en équipe ou dans une entreprise.

Les commentaires commencent par `<!--` et se terminent par `-->`, et peuvent s'étendre sur plusieurs lignes. Ils peuvent contenir du code ou du texte, et n'apparaîtront pas sur le front-end du site web lorsqu'un utilisateur visite une page. Vous pouvez consulter les commentaires via la Console de l'Inspecteur ou en consultant le Code Source de la page.

### **Exemple**

```html
<!-- Vous pouvez commenter un grand nombre de lignes comme ceci.
Auteur : xyz
Date : xx/xx/xxxx
Objectif : abc
-->
En savoir plus : https://html.com/tags/comment-tag/#ixzz4vtZHu5uR
<!DOCTYPE html>
<html>
	<body>
		<h1>FreeCodeCamp web</h1>
		<!-- Laisser un espace entre le h1 et le p pour comprendre de quoi nous parlons -->
		<p>FreeCodeCamp est un projet open-source qui a besoin de votre aide</p>
	        <!-- Pour la lisibilité du code, utilisez une indentation appropriée -->
	</body>
</html>
```

## **Commentaires conditionnels**

Les commentaires conditionnels définissent certaines balises HTML à exécuter lorsqu'une certaine condition est remplie.

Les commentaires conditionnels ne sont reconnus que par Internet Explorer des versions 5 à 9 - IE5 à IE9.

### **Exemple**

```html
<!DOCTYPE html>
<html>
	<body>
		<!--[if IE 9]>
    			<h1>FreeCodeCamp web</h1>
			<p>FreeCodeCamp est un projet open-source qui a besoin de votre aide</p>	
		<![endif]-->
	</body>
</html>
```

### **Commentaires conditionnels IE**

Ces commentaires ne sont disponibles que dans Internet Explorer et peuvent être utilisés jusqu'à IE9. De nos jours, il est peu probable que vous les rencontriez, mais il est bon de connaître leur existence. Les commentaires conditionnels sont un moyen de proposer une expérience différente pour différents navigateurs clients. Par exemple :

```html
<!--[if lt IE 9]> <p>Votre navigateur est inférieur à IE9</p> <![endif]-->     
<!--[if IE 9]> <p>Votre navigateur est IE9</p> <![endif]-->
<!--[if gt IE 9]> <p>Votre navigateur est supérieur à IE9</p> <![endif]-->
```

## Plus d'informations sur HTML :

* [Guide du débutant en HTML](https://www.freecodecamp.org/news/p/1c7bd638-2e4d-48f7-aba2-29d97a02021b/)
* [Meilleurs tutoriels HTML et HTML5](https://www.freecodecamp.org/news/best-html-html5-tutorial/)
* [Le manuel HTML](https://www.freecodecamp.org/news/the-html-handbook/)