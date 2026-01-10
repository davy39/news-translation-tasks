---
title: Comment utiliser les macros Babel avec React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-08T14:02:42.000Z'
originalURL: https://freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NIQACxrWjnCUOLogiOrW5Q.png
tags:
- name: Babel
  slug: babel
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment utiliser les macros Babel avec React Native
seo_desc: 'By Karan Thakkar

  A practical use case for solving an i18n problem using codegen.macro


  _Background Photo by [Unsplash](https://unsplash.com/photos/6PF6DaiWz48" rel="noopener"
  target="_blank" title="">Rayi Christian Wicaksono on <a href="https://unspl...'
---

Par Karan Thakkar

#### Un cas d'utilisation pratique pour résoudre un problème d'i18n en utilisant codegen.macro

![Image](https://cdn-media-1.freecodecamp.org/images/jfjrz1ddbDi4Zef64CpbkFH3aucozCj7VNNX)
_Photo de fond par [Unsplash](https://unsplash.com/photos/6PF6DaiWz48" rel="noopener" target="_blank" title="">Rayi Christian Wicaksono</a> sur <a href="https://unsplash.com" rel="noopener" target="_blank" title=")_

Si vous suivez [Kent C. Dodds](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) ou [Sunil Pai](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) sur Twitter, vous avez peut-être lu des tweets de temps en temps sur les macros babel. Moi aussi. Mais ce n'est que hier que j'ai enfin compris de quoi il s'agit. **Et c'est glorieux !**

Donc, en venant au problème : je voulais ajouter une utilité pour faire du formatage de nombres basé sur la locale dans React Native. Comme il n'y a pas de support cohérent pour l'[API d'internationalisation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl) dans React Native, j'ai utilisé un polyfill pour cela : [https://github.com/andyearnshaw/Intl.js](https://github.com/andyearnshaw/Intl.js). Maintenant, avec le polyfill, j'avais aussi besoin d'importer tous les fichiers de locale de support. Il y a deux options ici :

1. **Charger toutes les locales** : C'est simple, car je peux simplement importer un fichier. Cela devrait généralement être évité, car cela peut inutilement alourdir la taille de votre bundle si vous avez juste besoin de supporter certaines locales.

![Image](https://cdn-media-1.freecodecamp.org/images/m8Pk2rDXI2f6OfOEECt99XwbiR0pw5OxzXXf)
_Charger toutes les locales fournies par Intl.js_

2. **Charger uniquement les locales nécessaires** : Avec cela, je ne charge que les locales que mon application supporte.

![Image](https://cdn-media-1.freecodecamp.org/images/LzitpUOexDJoOucbHFAbe7kkPP8nOVs2F7k5)
_Charger uniquement les locales nécessaires depuis Intl.js_

Par exemple, si l'application supporte 40 locales, je dois manuellement écrire 40 imports pour chaque locale. Cela devient beaucoup plus difficile et fastidieux à faire à mesure que la liste des locales que vous supportez augmente.

Je voulais automatiser cela de manière à ne nécessiter aucune modification manuelle. Cela est particulièrement utile pour nous car nous avons des tâches en arrière-plan qui s'exécutent sur le CI et qui mettent automatiquement à jour notre fichier de locales chaque fois que nous ajoutons le support pour une nouvelle langue.

Comment puis-je importer dynamiquement plusieurs fichiers tout en permettant à l'emballeur React Native d'avoir tous les chemins de fichiers au moment de la compilation ? [**babel-plugin-macros**](https://github.com/kentcdodds/babel-plugin-macros) et [**codegen.macro**](https://github.com/kentcdodds/codegen.macro) ?

### Qu'est-ce que ces... choses babel ?

[Cet](https://babeljs.io/blog/2017/09/11/zero-config-with-babel-macros) article de blog de [Kent C. Dodds](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) décrit parfaitement ce qu'est [**babel-plugin-macros**](https://github.com/kentcdodds/babel-plugin-macros) :

> C'est une approche "nouvelle" de la transformation de code. Elle vous permet d'avoir des transformations de code importables avec une configuration zéro.

[**codegen.macro**](https://github.com/kentcdodds/codegen.macro) est une telle transformation que vous pouvez utiliser pour "générer du code" au moment de la construction.

### Comment le configurer ?

React Native vous permet de configurer vos propres paramètres babel. Vous pouvez créer votre propre fichier ".babelrc" à la racine de votre projet. Pour vous assurer que vous utilisez la configuration babel par défaut qui vient avec React Native, installez [**babel-preset-react-native**](https://github.com/facebook/react-native/tree/master/babel-preset).

En plus de cela, vous devez installer un autre module : [**codegen.macro**](https://github.com/kentcdodds/codegen.macro). Le plugin codegen utilise [**babel-plugin-macros**](https://github.com/kentcdodds/babel-plugin-macros) sous le capot pour faire son travail. Nous verrons dans un instant ce que c'est.

![Image](https://cdn-media-1.freecodecamp.org/images/9yAnzljqibKRoDn7rKe5AkGMQ63pPWfp4354)
_f4c6fe0ffe0fVoici à quoi votre fichier **.babelrc** devrait ressembler_

### Que fait codegen.macro ?

Il prend un morceau de code, l'exécute et se remplace par la chaîne `export-ed`. Cela aura beaucoup plus de sens une fois que vous verrez l'exemple ci-dessous. Étant donné une liste de locales et une macro codegen, il génère une liste d'imports au moment de la construction !

![Image](https://cdn-media-1.freecodecamp.org/images/1WKwUJ0aFROJGwvTQNckj87aOJOTvadtYTuv)

![Image](https://cdn-media-1.freecodecamp.org/images/yj8t50UemnN-BaJUUy0q1XAgggZgMDPgelZz)
_GAUCHE : macro codegen pour construire les imports pour toutes les locales · DROITE : Liste des locales supportées_

![Image](https://cdn-media-1.freecodecamp.org/images/yPXysDYsOX2BytVUIzJKeY7pMK9CblD8oMeH)
_Sortie de babel après la transpilation_

### Mais, que faire si j'ai besoin de la coloration syntaxique ?

Puisque nous écrivons tout notre code dans une chaîne de modèle, il est vraiment difficile d'obtenir une coloration syntaxique appropriée. Vous pourriez finir par passer beaucoup de temps à essayer de comprendre pourquoi votre macro donne une erreur lors de la transpilation.

Heureusement, les macros babel supportent [plusieurs façons différentes](https://github.com/kentcdodds/babel-plugin-codegen#usage) de les utiliser. Ma préférée est d'utiliser un **codegen.require**. Avec cela, vous pouvez déplacer le corps de votre macro dans un fichier séparé et l'importer où vous voulez, comme montré ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1PuJiRDOV4A2YT6nx1SOTmeViF9XbpG1-L22)

![Image](https://cdn-media-1.freecodecamp.org/images/u1tVA9klTM1XTlJtK5Rj2PE5nxrzkUdtsh9F)
_Importer le codegen en utilisant un appel spécial **codegen.require**_

#### Avantages de l'utilisation de cette syntaxe :

* eh bien, la coloration syntaxique ??f44d
* pas besoin d'échapper les séquences d'échappement que vous devez utiliser comme **\n ?**

![Image](https://cdn-media-1.freecodecamp.org/images/EVMYOZ1LD-n8SHTuqvfwVNWXr6wghjIFiND3)

![Image](https://cdn-media-1.freecodecamp.org/images/zJD4HRaNxhHMHsHlhlINJf64K0B0vHin32jG)

* utiliser des littéraux de modèle à l'intérieur de votre codegen ?

![Image](https://cdn-media-1.freecodecamp.org/images/MVDROCDmMzE6MY8Osky7BpEJYlh-z5-QO-Ez)

![Image](https://cdn-media-1.freecodecamp.org/images/HXwx6D60GMfXD6DiiMmwqUI78dt4lowhLdrw)

### NOTE : mise à niveau de React Native

Si vous choisissez de remplacer la configuration babel, chaque fois que vous mettez à niveau react-native, vous devez également augmenter la version de babel-preset-react-native pour correspondre à celle utilisée dans cette version de react-native.

C'est tout, les gens ! Vous avez configuré les macros babel avec React Native ?? Consultez ces [autres macros disponibles](https://github.com/kentcdodds/babel-plugin-macros/blob/master/other/docs/macros.md) si vous voulez essayer quelque chose de différent.

PS : Merci à [Narendra N Shetty](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined), [Siddharth Kshetrapal](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) et [Kent C. Dodds](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) pour avoir révisé le brouillon et aidé à le façonner mieux ?

![Image](https://cdn-media-1.freecodecamp.org/images/NeELdCuvtLGOOP54bsUaMrsh3SDAd9cmI3FD)

Salut ! ?f44d Je suis K[aran Thakkar.](https://twitter.com/geekykaran) Je travaille sur l'infrastructure React Native chez S[kyscanner Engineering.](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) Auparavant, j'ai dirigé l'équipe web chez C[rowdfire.](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) J'aime essayer de nouvelles technologies pendant mon temps libre et j'ai construit T[weetify](https://karanjthakkar.com/projects/tweetify) (en utilisant React Native) et S[how My PRf44d's](https://showmyprs.com) (en utilisant Golang).

D'autres articles écrits par moi sont :

* [Un guide illustré pour configurer votre site web en utilisant GitHub et Cloudflare](https://medium.freecodecamp.org/an-illustrated-guide-for-setting-up-your-website-using-github-cloudflare-5a7a11ca9465)
* [Utilisation du Certbot Letf44d's Encrypt pour obtenir HTTPS sur votre boîte Amazon EC2 NGINX](https://medium.freecodecamp.org/going-https-on-amazon-ec2-ubuntu-14-04-with-lets-encrypt-certbot-on-nginx-696770649e76)