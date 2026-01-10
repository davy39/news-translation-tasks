---
title: L'attribut HTML a href expliqué avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T19:25:00.000Z'
originalURL: https://freecodecamp.org/news/the-a-href-attribute-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d6a740569d1a4ca37a6.jpg
tags:
- name: HTML
  slug: html
seo_title: L'attribut HTML a href expliqué avec des exemples
seo_desc: "The <a href> attribute refers to a destination provided by a link. The\
  \ a (anchor) tag is dead without the <href> attribute. \nHow to use the  tag\nSometimes\
  \ in your workflow, you don’t want a live link or you won’t know the link destination\
  \ yet. In thi..."
---

L'attribut `<a href>` fait référence à une destination fournie par un lien. La balise `a` (ancre) est inutile sans l'attribut `<href>`. 

## Comment utiliser la balise <a href>

Parfois dans votre flux de travail, vous ne voulez pas d'un lien actif ou vous ne connaîtrez pas encore la destination du lien. Dans ce cas, il est utile de définir l'attribut `href` sur `"#"` pour créer un lien mort. 

L'attribut `href` peut être utilisé pour lier des fichiers locaux ou des fichiers sur Internet.

Par exemple :

```html
<html>
  <head>
    <title>Exemple d'attribut Href</title>
  </head>
  <body>
    <h1>Exemple d'attribut Href</h1>
      <p>
        <a href="https://www.freecodecamp.org/contribute/">La page de contribution de freeCodeCamp</a> vous montre comment et où vous pouvez contribuer à la communauté et à la croissance de freeCodeCamp.
      </p>
    </h1>
  </body>
</html>
```

L'attribut `<a href>` est supporté par tous les navigateurs.

## Plus d'attributs HTML :

`hreflang` : Spécifie la langue de la ressource liée. 

`target` : Spécifie le contexte dans lequel la ressource liée s'ouvrira. 

`title` : Définit le titre d'un lien, qui apparaît à l'utilisateur sous forme d'infobulle.

### **Exemples**

```html
<a href="#">Ceci est un lien mort</a>
<a href="https://www.freecodecamp.org">Ceci est un lien actif vers freeCodeCamp</a>
<a href="https://html.com/attributes/a-href/">plus sur l'attribut a href</a>
```

### **Ancres dans la page**

Il est également possible de définir une ancre à un endroit précis de la page. Pour cela, vous devez d'abord placer une ancre à l'emplacement sur la page avec la balise et l'attribut nécessaire "name" avec une description de mot-clé, comme ceci :

```html
<a name="top"></a>
```

Toute description entre les balises n'est pas requise. Après cela, vous pouvez placer un lien menant à cette ancre à n'importe quel endroit de la même page. Pour cela, vous devez utiliser la balise avec l'attribut nécessaire "href" avec le symbole # (dièse) et la description du mot-clé de l'ancre, comme ceci :

```html
<a href="#top">Aller en haut</a>
```

### **Liens d'images**

L'attribut `<a href="#">` peut également être appliqué aux images et à d'autres éléments HTML.

### **Exemple**

```html
<a href="#"><img itemprop="image" style="height: 90px;" src="http://www.chatbot.chat/assets/images/header-bg_y.jpg" alt="image">  </a>
```

### **Quelques exemples supplémentaires de href**

```html
<base href="https://www.freecodecamp.org/a-href/">Ceci donne une URL de base pour toutes les URL suivantes sur la page</a>
<link href="style.css">Ceci est un lien actif vers une feuille de style externe</a>
```

## Que pouvez-vous faire d'autre avec <a href> ? 

Plus de personnalisation ! Voyons un cas d'utilisation spécifique :

Un lien mailto est un type d'hyperlien (`<a href=""></a>`) avec des paramètres spéciaux qui vous permettent de spécifier des destinataires supplémentaires, une ligne d'objet et/ou un texte de corps.

### **La syntaxe de base avec un destinataire est :**

```html
<a href="mailto:ami@quelquechose.com">Un texte</a>
```

### Ajouter un sujet à cet email :

Si vous souhaitez ajouter un sujet spécifique à cet email, faites attention à ajouter `%20` ou `+` partout où il y a un espace dans la ligne de sujet. Une façon facile de s'assurer qu'il est correctement formaté est d'utiliser un [Encodeur / Décodeur d'URL](https://meyerweb.com/eric/tools/dencoder/).

### Ajouter un texte de corps :

De même, vous pouvez ajouter un message spécifique dans la partie corps de l'email : Encore une fois, les espaces doivent être remplacés par `%20` ou `+`. Après le paramètre de sujet, tout paramètre supplémentaire doit être précédé par `&`

Exemple : Supposons que vous souhaitiez que les utilisateurs envoient un email à leurs amis sur leurs progrès chez Free Code Camp :

Adresse : vide

Sujet : Bonne nouvelle

Corps : Je deviens développeur

Votre lien html maintenant :

```html
<a href="mailto:?subject=Bonne%20nouvelle&body=Je%20deviens%20développeur">Envoyer un email !</a>
```

Ici, nous avons laissé mailto vide (mailto:?). Cela ouvrira le client de messagerie de l'utilisateur et l'utilisateur ajoutera lui-même l'adresse du destinataire.

### Ajouter plus de destinataires :

De la même manière, vous pouvez ajouter des paramètres CC et Cci. Séparez chaque adresse par une virgule !

Les paramètres supplémentaires doivent être précédés par `&`.

```html
<a href="mailto:premierami@quelquechose.com?subject=Bonne%20nouvelle&cc=deuxiemeami@quelquechose.com,troisiemeami@quelquechose.com&bcc=quatriemeami@quelquechose.com">Envoyer un email !</a>
```

#### **Plus d'informations :**

[MDN - Liens email](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks#E-mail_links)