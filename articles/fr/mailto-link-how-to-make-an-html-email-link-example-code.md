---
title: Lien Mailto – Comment créer un lien email HTML [Exemple de code]
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-11-16T22:58:22.000Z'
originalURL: https://freecodecamp.org/news/mailto-link-how-to-make-an-html-email-link-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/brett-jordan-LPZy4da9aRo-unsplash.jpg
tags:
- name: email
  slug: email
- name: HTML
  slug: html
seo_title: Lien Mailto – Comment créer un lien email HTML [Exemple de code]
seo_desc: 'A mailto link allows users to send emails straight from a website using
  the user''s default email client. But how do you create a mailto link in HTML?

  In this article, I will walk you through how to create a mailto link in HTML using
  example code.

  Bas...'
---

Un lien mailto permet aux utilisateurs d'envoyer des emails directement depuis un site web en utilisant le client email par défaut de l'utilisateur. Mais comment créer un lien mailto en HTML ?

Dans cet article, je vais vous expliquer comment créer un lien mailto en HTML en utilisant un exemple de code.

## Syntaxe de base du lien `mailto`

Voici la syntaxe de base pour le lien mailto :

```html
<a href="mailto:johndoe@fakeemail.com">Exemple de lien mailto</a>
```

Dans le navigateur, l'utilisateur peut cliquer sur le lien et cela ouvrira son client email par défaut.

Dans cet exemple, lorsque je clique sur le lien, cela ouvre mon application Mail et l'adresse email est déjà remplie dans le champ `à`.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.07.32-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.05.15-AM.png)

En utilisant cette méthode, je pourrais envoyer un email rapide et revenir sur le site web.

## Comment ajouter plusieurs adresses email au lien mailto

Vous pouvez ajouter plusieurs adresses email au lien mailto en utilisant cette syntaxe :

```html
<a href="mailto:johndoe@fakeemail.com, janedoe@fakeemail.com">
    Plusieurs adresses email
</a>
```

Il est important de séparer les multiples adresses email en utilisant des virgules.

Lorsque je clique sur le lien dans le navigateur, cela ouvre l'application `Mail` et remplit les adresses email dans le champ `à`.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.18.17-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.18.42-AM.png)

## Comment ajouter un sujet au lien mailto

Voici un exemple de code qui montre comment ajouter un sujet au lien mailto.

```html
<a href="mailto:johndoe@fakeemail.com, janedoe@fakeemail.com?subject=voici comment utiliser le lien mailto">
    Utilisation du paramètre subject
</a>
```

Après les adresses email, vous devez ajouter un `?` pour séparer les emails et le paramètre `subject`. Si vous omettez ce `?`, alors le lien du sujet ne fonctionnera pas.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.32.41-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.34.08-AM.png)

## Comment ajouter CC et BCC au lien mailto

Voici un exemple qui montre comment ajouter des destinataires en CC (copie carbone) et BCC (copie carbone invisible) au lien mailto.

```html
<a
    href="mailto:johndoe@fakeemail.com, janedoe@fakeemail.com?cc=jackdoe@fakeemail.com &bcc=jennydoe@fakeemail.com &subject=voici comment utiliser le lien mailto">
    Utilisation des paramètres CC et BCC
</a>
```

Après les adresses email, vous devez ajouter un `?` pour séparer les emails et le paramètre `CC`. Vous devez également ajouter un `&` avant les paramètres `BCC` et `subject`.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.44.29-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.45.03-AM.png)

## Comment ajouter le paramètre body au lien mailto

Voici un exemple qui montre comment utiliser le paramètre body avec le lien mailto. Cela permet d'ajouter du texte au corps de l'email.

```html
<a
   href="mailto:johndoe@fakeemail.com, janedoe@fakeemail.com?cc=jackdoe@fakeemail.com &bcc=jennydoe@fakeemail.com &subject=voici comment utiliser le lien mailto &body=voici un article sur comment utiliser le lien mailto">
    Utilisation du paramètre body
</a>
```

Vous devez ajouter un `&` avant le paramètre `body`.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.57.00-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.57.17-AM.png)

## Y a-t-il des inconvénients à utiliser les liens mailto ?

L'un des inconvénients de l'utilisation d'un lien mailto est qu'il est souvent perçu comme du spam par les utilisateurs. Malheureusement, beaucoup de spammers utilisent cette option pour envoyer des emails aux utilisateurs. Donc, gardez cela à l'esprit lorsque vous l'utilisez.

## Avantages de l'utilisation des liens mailto

Une bonne raison d'utiliser un lien mailto est si vous envoyez des emails à un groupe de personnes que vous connaissez. Si ce groupe entier utilise un client email par défaut, alors utiliser un lien mailto serait une bonne option par rapport à un formulaire de contact.