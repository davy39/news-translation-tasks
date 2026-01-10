---
title: Comment fonctionne la propriété CSS Position – Expliqué avec des exemples de
  code
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-06-21T16:36:14.000Z'
originalURL: https://freecodecamp.org/news/css-position-property-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/FCC-Thumbnail--4-.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment fonctionne la propriété CSS Position – Expliqué avec des exemples
  de code
seo_desc: 'Today we''re gonna learn everything you need to know about the CSS position
  property along with examples. Let''s get started 🎖️

  Table of contents


  What is CSS Position Property?

  What is the Static Position in CSS?

  What are the Relative and Absolute Po...'
---

Aujourd'hui, nous allons tout apprendre sur la propriété CSS position avec des exemples. Commençons 🎖️

# Table des matières 

* [Qu'est-ce que la propriété CSS Position ?](#heading-quest-ce-que-la-propriete-position-en-css)
* [Qu'est-ce que la **position statique** en CSS ?](#heading-quest-ce-que-la-position-statique-en-css)
* [Quelles sont les positions **relative et absolue** en CSS ?](#heading-quelles-sont-les-positions-relative-et-absolue-en-css)
* [Qu'est-ce que la **position fixe** en CSS ?](#heading-quest-ce-que-la-position-fixe-en-css)
* [Qu'est-ce que la **position collante** en CSS ?](#heading-quest-ce-que-la-position-collante-en-css)

## **Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :**

%[https://youtu.be/yFXEur3SCGI]

# Qu'est-ce que la propriété position en CSS ? 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-3--6-.png)

Si vous souhaitez créer des **sites web époustouflants qui semblent artistiques, uniques et beaux**, vous devriez absolument apprendre à utiliser la propriété CSS position. Voyons comment cela fonctionne.

En utilisant **Flexbox ou Grid**, vous pouvez créer un **site web symétrique** comme ceci : 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-35--2-.png)
_**Site web créé avec Flexbox**_

Avec la **propriété position**, vous pouvez créer un **site web asymétrique** comme ceci : 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/A-1-1--2-.png)
_**Site web créé avec Grid et les propriétés de position**_

Vous ne pouvez pas placer votre contenu où vous le souhaitez en utilisant Flexbox et Grid. Vous êtes limité autour des **axes X et Y**. Regardez ce dessin pour voir ce que je veux dire : 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-1--6-.png)
_**Disposition symétrique du contenu montrant les éléments placés respectivement par rapport aux axes x et y**_

Vos boîtes suivront ces mesures exactes. 👋

Mais, en utilisant la **propriété position**, vous pouvez placer votre contenu où vous le souhaitez en **détachant** chaque élément des autres éléments.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-2--4-.png)
_**Disposition asymétrique du contenu montrant les éléments placés indépendamment des axes x et y.**_

Vous pouvez placer vos boîtes **n'importe où** vous le souhaitez avec ce type de disposition. 👋 En d'autres termes, vous aurez un **mouvement libre** autour de votre écran.

Voici un autre exemple de ce que vous pouvez faire en utilisant la propriété position :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-3--8-.png)
_**Un site web asymétrique**_

Vous pouvez placer ou déplacer ces petits motifs de points et de vagues et l'image de donut partout sur la page **☝** où vous le souhaitez en utilisant la propriété position.

# Installation du projet

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-4--7-.png)

Pour ce projet, vous pouvez utiliser n'importe quel éditeur de code qui a le **plugin emmet** installé. Je vais utiliser [CodePen.io](https://codepen.io).

### HTML 

À l'intérieur de la balise body, écrivez ce code : 👋

```html
<div class="box-1"> </div>
```

### CSS

Effacez vos paramètres par défaut du navigateur et ajoutez ce CSS : 👋

```css
*{
   margin: 0px;
   padding: 0px;
   box-sizing: border-box;
}
```

Stylez la classe box-1 comme ceci : 👋

```css
.box-1{
   width: 120px;
   height: 120px;
   background-color: skyblue;
   border: 2px solid black;
}
```

Notre propriété position a 5 valeurs :

1. relative
2. absolute
3. static
4. fixed
5. sticky

Pour déplacer notre boîte, nous utiliserons 4 propriétés :

* **Top, Bottom**
* **Left, Right**

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-12--1-.png)

# Qu'est-ce que la position statique en CSS ?

Cela n'a **aucun cas d'utilisation**. C'est la **valeur par défaut** de chaque élément.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-10--3-.png)
_Position par défaut de chaque élément_

# Quelles sont les positions relative et absolue en CSS ?

La **position relative** et la **position absolue** fonctionnent de la même manière, sauf dans un domaine. Nous utilisons `relative` pour identifier la classe parente. Et nous utilisons `absolute` pour identifier les classes enfants. 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-11--2-.png)
_**Position VS position relative**_

### Regardons 2 exemples 👋

Tout d'abord, expérimentons avec la valeur **`relative`**. Essayez ce code :

```css
.box-1{
/* Autres codes ici */

   position: relative;
   left: 100px;
}
```

Voici le résultat que vous obtiendrez : 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-13--1-.png)

Nous pouvons dupliquer le même résultat en utilisant la valeur **`absolute`** comme ceci : 👋

```css
.box-1{
/* Autres codes ici */

   position: absolute;
   left: 100px;
}
```

Examinons la principale différence entre les positions **relative et absolute**.

### Position relative vs absolue en CSS

![Image](https://www.freecodecamp.org/news/content/images/2021/06/BEM-1--1-.png)

### HTML

Écrivez ce code à l'intérieur de votre HTML : 👋

```html
<body>
   <div class="box-1">
    
       <div class="box-2"> </div>	
        
   </div>
</body>
```

### CSS

Stylez les boîtes avec le CSS suivant : 👋

```css
.box-1{
	width: 300px;
	height: 300px;
	background-color: skyblue;
	border: 2px solid black;
    margin: auto;
}

.box-2{
	width: 100px;
	height:100px;
	background-color: pink;
	border: 2px solid black;
}
```

Cela devrait ressembler à ceci : 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/dd-2.png)
_**Le résultat est une boîte bleue avec une petite boîte rose en haut à gauche**_

Maintenant, nous allons sélectionner nos classes comme ceci : 👋

```css
body{ }

.box-1{ }

.box-2{ }
```

Maintenant, écrivez ce code dans votre CSS : 👋

```css
body{
	
}

.box-1{
/* Ceci est le parent 👋 */
	position: relative;
}
.box-2{
/* Ceci est l'enfant 👋 */
	position: absolute;
	left: 100px;
}
```

Voici le résultat : 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-14.png)
_**Le résultat est que la boîte rose s'est déplacée de 100px vers la droite**_

Remarquez que .box-2 s'est déplacé de **100px** par rapport à .box-1.

C'est parce que .box-1 est le **parent** et .box-2 est l'**enfant**.

Changeons cela à nouveau. Écrivez ce code dans votre CSS :

```css
body{
/* Ceci est le parent 👋 */
   position: relative;	
}

.box-1{

}
.box-2{
/* Ceci est l'enfant 👋 */
   position: absolute;
    left: 100px;
}
```

Voici le résultat : 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-15.png)
_**Le résultat est que la boîte rose s'est déplacée de 100px par rapport au body**_

Remarquez que .box-2 s'est déplacé de **100px** par rapport à l'élément **body**.

C'est parce que le **body** est le **parent** et .box-2 est l'**enfant**.

# Qu'est-ce que la position fixe en CSS ?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-16--1-.png)

Cette valeur **fixera la position** de votre élément à l'écran même lorsque vous **faites défiler** dans le navigateur. Regardons quelques exemples pour voir comment cela fonctionne.

### Exemple de position fixe

Écrivez ce code dans votre HTML. 👋 Une fois que vous avez écrit `lorem200`, assurez-vous d'appuyer sur la touche **Tab** de votre clavier :

```html
<div class="container">
	
	<p>lorem200</p>
    
	<div class="box-1"> fixed </div>
    
	<p>lorem200</p>		

</div>
```

Et voici le CSS :

```css
.container{
	height: 3000px;
}

.box-1{
	height: 120px;
	width: 120px;
	background-color: skyblue;
	border: 2px solid black;
	
	display: grid;
	place-content: center;
}
```

Puis ajoutez ce CSS en bas :

```css
.box-1{

	position: fixed;
	top: 100px;
	left: 200px;
}

```

Voici le résultat : 👋

![](https://media.giphy.com/media/J6hbBulobEQz6HftRv/giphy.gif)

Vous pouvez voir que l'élément reste fixe même lorsque nous faisons défiler notre navigateur.

# Qu'est-ce que la position collante en CSS ?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-17.png)

Après avoir fait défiler jusqu'à un certain point sur notre écran, cette valeur **fixera la position** de notre élément à l'écran pour qu'il ne bouge pas.

### Exemple de position collante

Ne changez rien dans votre HTML et CSS actuels sauf cette valeur :

```css
.box-1{
/*  Jouez avec cette valeur 👋 */
   position: sticky;
   top: 30px;
   left: 200px;
}

```

Voici le résultat : 👋

![](https://media.giphy.com/media/175hkevbKC3yUfiLQc/giphy.gif)

Vous pouvez voir qu'après un **certain point de défilement**, l'élément reste fixe en haut de notre écran de navigateur.

Vous pouvez consulter ces sites web pour voir comment la position collante fonctionne sur des sites web réels.

* [AwakeBoards](https://awakeboards.com/)
* [Ferme](https://ferme.shop/)
* [LATORRE](https://www.ascensionlatorre.com/)

# Conclusion

Maintenant, vous pouvez créer des sites web magnifiques et résoudre des problèmes de disposition simples en utilisant la propriété position. 

Voici votre médaille pour avoir lu jusqu'à la fin. ❤️

### Suggestions et critiques sont grandement appréciées ❤️

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

**YouTube [/ Joy Shaheb](https://youtube.com/c/joyshaheb)**

**LinkedIn [/ JoyShaheb](https://www.linkedin.com/in/joyshaheb/)**

**Twitter [/ JoyShaheb](https://twitter.com/JoyShaheb)**

**Instagram [/ JoyShaheb](https://www.instagram.com/joyshaheb/)**

## Crédits 

* [Illustration de fille mignonne](https://www.freepik.com/free-vector/young-girl-holding-pile-papers-cartoon-illustration_12566300.htm)
* [Avatar de chaton](https://www.flaticon.com/packs/kitty-avatars-3)