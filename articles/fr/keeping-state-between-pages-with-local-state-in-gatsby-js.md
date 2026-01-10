---
title: Comment conserver l'état entre les pages avec l'état local dans Gatsby.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-14T14:56:02.000Z'
originalURL: https://freecodecamp.org/news/keeping-state-between-pages-with-local-state-in-gatsby-js
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/gatsby1.jpeg
tags:
- name: Gatsby
  slug: gatsby
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment conserver l'état entre les pages avec l'état local dans Gatsby.js
seo_desc: 'By Thomas Weibenfalk


  Cover Photo by Anas Alshanti on Unsplash


  The “problem”

  When using the static site generator Gatsby you don’t have a base “App” component
  to play with. That said, there’s no component that wraps around your whole application
  whe...'
---

Par Thomas Weibenfalk

> Photo de couverture par [Anas Alshanti](https://unsplash.com/photos/feXpdV001o4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/search/photos/development-code?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

## **Le "problème"**

Lorsque vous utilisez le générateur de site statique Gatsby, vous n'avez pas de composant de base "App" avec lequel jouer. Cela dit, il n'y a pas de composant qui enveloppe toute votre application où vous pouvez placer votre état qui doit être conservé entre les routes/pages. Gatsby.js crée automatiquement (ou automagiquement ?) des routes vers les pages que vous placez dans le dossier de pages de votre installation. Ou, vous créez des pages de manière programmatique à partir de votre fichier **gatsby-node.js**.

Cela nous posera des problèmes si nous avons besoin, par exemple, d'un menu qui doit être visible et disponible pour l'interaction sur toutes nos routes de pages. Dans mon cas, j'avais un menu de formulaire de courrier qui pouvait être affiché ou masqué dans le coin inférieur droit de mon application. Ce composant a un état local qui décidera si le composant est affiché ou non. L'image ci-dessous montre le menu fermé et ouvert.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/gatsby2.jpeg)

Donc... c'est notre problème. Comment pouvons-nous le résoudre ? Il existe plusieurs façons de traiter cela, mais une façon, et l'approche que j'ai prise, est décrite ci-dessous.

## **La Solution**

Je vais aller droit au but. Gatsby a un fichier qui s'appelle **gatsby-browser.js. Nous pouvons utiliser ce fichier pour faire en sorte que des composants enveloppent toute notre application et nos pages !**

C'est génial !

Ce fichier nous permet d'utiliser l'API **Browser** de Gatsby. Cette API contient plusieurs fonctions utiles, mais il y en a une en particulier qui répondra à nos besoins. Elle s'appelle **wrapPageElement**. Consultez le code ci-dessous. Il s'agit du code réel que j'ai utilisé pour l'application de mon client.

```js
// gatsby-browser.js
// Importer le composant en haut du fichier
import MailWidgetWrapper from './src/components/MailWidgetWrapper';

export const wrapPageElement = ({ element, props }) => (
  <MailWidgetWrapper {...props}>{element}</MailWidgetWrapper>
);
```

Ici, j'ai créé un composant wrapper qui sera disponible sur toutes les routes et pages de Gatsby. C'est génial ! Et exactement ce dont nous avons besoin. Le **composant wrapper** ressemble à ceci :

```js
// MailWidgetWrapper.js
import React from 'react';

import MailWidget from './MailWidget';

const MailWidgetWrapper = ({ children }) => (
  <>
    {children}
    <MailWidget />
  </>
);

export default MailWidgetWrapper;
```

Il s'agit d'un composant React vraiment simple dont la seule fonction est d'envelopper notre application et de lui fournir le composant MailWidget. Mais comment fonctionne **wrapPageElement** ?

## wrapPageElement

Tout d'abord, je recommande également vivement d'utiliser gatsbyjs.org autant que possible pour trouver des réponses à tout ce qui concerne Gatsby. Le site est excellent et regorge d'explications vraiment bonnes et approfondies pour la plupart des problèmes que vous rencontrerez.

Dans notre cas, si vous regardez le code ci-dessus, nous avons deux paramètres qui sont créés pour nous dans la fonction de rappel `wrapPageElement` : **element et props.**

Vous devriez être familier avec les props si vous utilisez React, donc ils n'ont besoin d'aucune introduction supplémentaire. Dans ce cas, les props sont utilisés par la page sur laquelle nous nous trouvons. Nous n'avons pas besoin d'utiliser aucun de ces props, car nous avons seulement besoin d'utiliser le prop children (automatiquement créé par React).

Le `MailWidgetWrapper` se contente de rendre les children et le `MailWidget`. Les children sont la page que nous envoyons dans le composant `MailWidgetWrapper` à partir du fichier **gatsby-browser.js**, comme montré ci-dessous. La page réelle vit dans le paramètre **element** et c'est celle que nous envoyons avec l'expression `{element}`.

```js
<MailWidgetWrapper {...props}>{element}</MailWidgetWrapper>
```

Donc, en résumé, les paramètres que nous obtenons de `wrapPageElement` peuvent être résumés comme suit :

**Le paramètre props sont les props de la page réelle sur laquelle nous nous trouvons. Et le paramètre element est la page réelle sur laquelle nous nous trouvons**

## Le composant MailWidget

Mon composant `MailWidget` réel est assez grand et contient beaucoup de code qui n'est pas pertinent ici. C'est pourquoi je ne vous montre qu'un exemple de version simple et échafaudée d'un composant `MailWidget` ci-dessous. Ce composant n'est pas réellement pertinent pour la tâche d'expliquer la fonction `wrapPageElement`.

Le composant peut virtuellement être n'importe quoi que vous aimez et n'a rien à voir avec la mise en œuvre ci-dessus. Dans mon cas, c'est un `MailWidget`. C'est à vous de décider et quels composants avec état vous avez besoin d'avoir disponibles sur toutes vos routes de pages.

```js
// MailWidget.js
import React, { useState } from 'react';

const MailWidget = () => {
  const [isVisible, setIsVisible] = useState(false);

  const toggleVisible = () => {
    setIsVisible(!isVisible);
  };

  return (
    <div className={isVisible ? 'visible' : ''}>
      <button type="button" onClick={toggleVisible}>
        Masquer/Afficher MailWidget
      </button>
      <h1>Bonjour, je suis votre mailwidget</h1>
    </div>
  );
};
export default MailWidget;
```

Au fait, je suis complètement accro aux Hooks. J'adore les Hooks et les utiliserai dans tout ce que je fais en React ! C'est pourquoi j'ai créé mon état avec le hook `useState` dans celui-ci. Le composant ci-dessus utilise simplement un état local pour décider s'il doit s'afficher ou non.

## Conclusion

Voilà ! Espérons que vous avez appris qu'il n'est pas difficile d'avoir un composant qui conserve son état entre les pages dans Gatsby. Et nous aimons tous Gatsby.js, n'est-ce pas ? 😊

De plus, merci d'avoir lu cet article. Je suis un développeur de Suède qui aime enseigner et coder. Je crée également des cours en ligne sur React et Gatsby. Vous pouvez me trouver sur Udemy. Il suffit de chercher Thomas Weibenfalk ou de me contacter sur Twitter **@weibenfalk**  
J'ai aussi une chaîne YouTube où j'enseigne des choses gratuites, vérifiez-la [**ici**](https://www.youtube.com/channel/UCnnnWy4UTYN258FfVGeXBbg)**.**