---
title: Qu'est-ce que le Tabnabbing et comment l'éviter
subtitle: ''
author: Juanita Washington
co_authors: []
series: null
date: '2023-10-16T22:56:14.000Z'
originalURL: https://freecodecamp.org/news/what-is-tabnabbing
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Tab-pg-6.png
tags:
- name: HTML
  slug: html
- name: Web Security
  slug: web-security
seo_title: Qu'est-ce que le Tabnabbing et comment l'éviter
seo_desc: 'Sometimes when you''re building a website, you may need a link to open
  in a new tab. What you might not realize, though, is that doing so could leave your
  users vulnerable to malicious attacks via a practice called "tabnabbing".

  And while nothing is f...'
---

Parfois, lorsque vous construisez un site web, vous pouvez avoir besoin qu'un lien s'ouvre dans un nouvel onglet. Ce que vous ne réalisez peut-être pas, cependant, c'est que faire cela pourrait laisser vos utilisateurs vulnérables à des attaques malveillantes via une pratique appelée "tabnabbing".

Et bien que rien ne soit infaillible, il existe un moyen d'atténuer au moins les effets : utiliser les attributs `noopener` et `noreferrer`. Et c'est ce que vous apprendrez dans ce tutoriel rapide.

## Qu'est-ce que le Tabnabbing ?

Le tabnabbing est un type d'attaque de phishing qui cible les onglets inactifs de votre navigateur. Pendant que vous êtes concentré sur votre onglet actuel, le lien vers le précédent peut être détourné, et vous serez redirigé du site prévu vers un site malveillant ressemblant à la vraie chose.

Puisque le site malveillant ressemble beaucoup à l'original, l'utilisateur ne se rend généralement pas compte que la page sur laquelle il se trouve n'est pas légitime une fois qu'il revient à cet onglet. À cause de cela, l'utilisateur entre ses informations personnelles, sans savoir que quelqu'un de l'autre côté attend pour les voler.

Quelques façons dont les attaquants pourraient compromettre un site web bien connu incluent :

* publicités malveillantes

* widgets tiers que le site web a inclus, qui ont été compromis plus tard

* contenu généré par les utilisateurs malveillants (comme des posts de forum) contenant du JavaScript non assaini

### Un exemple rapide de Tabnabbing

Pensez à la façon dont un site web avec vos détails personnels vous déconnecte automatiquement lorsque vous êtes inactif trop longtemps. Puisque cela signifie que votre attention est ailleurs, l'attaquant peut remplacer la page réelle par un faux très convaincant.

Lorsque vous revenez à cet onglet, vous ne verriez pas la différence, donc vous vous reconnectez, et le phisher a maintenant accès à vos détails privés.

Comme c'est le cas pour les attaques de phishing, le but de cette action est de tromper l'utilisateur insoupçonné pour qu'il entre des informations sensibles (généralement des informations de connexion ou financières) sur le site factice.

C'est, bien sûr, un problème que vous voudrez éviter pour votre site lorsque les visiteurs arrivent ! Vous voudrez vous assurer que les gens sont en sécurité lorsqu'ils cliquent sur l'un de vos liens, n'est-ce pas ?

Alors maintenant, vous allez apprendre à rendre votre coin d'internet un peu plus sûr — en commençant par apprendre à ouvrir un nouvel onglet pour commencer.

## Comment ouvrir un lien dans un nouvel onglet en HTML

Pour ouvrir un lien dans un nouvel onglet, écrivez un lien comme vous le feriez en HTML, puis ajoutez simplement l'attribut target, en définissant la valeur sur blank, comme ceci : `target="_blank"` :

```html
<p>Apprenez à coder gratuitement sur <a href="https://www.freecodecamp.org/" target="_blank">freeCodeCamp.org !</a><p/>
```

Sur la page, cela ressemblerait à ceci :

Apprenez à coder gratuitement sur [freeCodeCamp.org !](https://www.freecodecamp.org/)

## Comment ajouter un attribut `Noopener`/`Noreferrer`

Malheureusement, plus vous avez d'onglets ouverts (qui ne fait pas de multitâche sur son navigateur ?), plus vous êtes susceptible au tabnabbing. Cela est dû au fait que plus un onglet reste inactif longtemps, plus les chances qu'un phisher puisse frapper sont élevées, remplaçant la page réelle par une fausse.

Alors, comment prévenir cela ? En ajoutant `rel="noopener noreferrer"` à votre ancre, comme ceci :

```html
<p>Apprenez à coder gratuitement sur <a href="https://www.freecodecamp.org/" target="_blank" rel="noopener noreferrer">freeCodeCamp.org !</a><p/>
```

### Pourquoi utiliser `noopener` et `noreferrer` ?

L'utilisation de `noopener` empêche les mauvais acteurs et les liens d'accéder à l'onglet ou à la fenêtre précédente qui a ouvert l'actuel. Cela est fait en définissant la propriété `Window.opener()` à null.

L'ajout de `noreferrer` empêche les sites externes de savoir que vous avez fait un lien vers eux, ce qui signifie que vos données de trafic ne seront pas envoyées dans leur direction.

## Conclusion

Vous devriez maintenant comprendre ce qu'est le tabnabbing et comment protéger vos liens (et vos utilisateurs) contre cela. J'espère que vous avez trouvé cela utile et bonne chance à vous !

Si vous avez effectivement trouvé cela utile, j'ai plus d'articles techniques sur mon [blog](https://jwashingtondev.hashnode.dev/). Si vous voulez vous connecter, je suis sur [linkedin](https://www.linkedin.com/in/juanita-washington-freelance-writer-web-developer-saas-tech/) !

Si vous voulez lire plus sur tout cela, voici quelques ressources :

1. [EASYDMARC - Qu'est-ce que le Tabnabbing et comment cela fonctionne](https://easydmarc.com/blog/what-is-tabnabbing-and-how-it-works/)

2. [Elegant Themes - Qu'est-ce que la balise "noopener noreferrer" et que signifie-t-elle ?](https://www.elegantthemes.com/blog/wordpress/rel-noopener-noreferrer-nofollow)

3. [MDN - la propriété Window.opener()](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)