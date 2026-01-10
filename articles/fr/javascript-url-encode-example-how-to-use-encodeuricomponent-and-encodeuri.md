---
title: Exemple d'encodage d'URL en JavaScript – Comment utiliser encodeURIComponent()
  et encodeURI()
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-08-04T22:39:13.000Z'
originalURL: https://freecodecamp.org/news/javascript-url-encode-example-how-to-use-encodeuricomponent-and-encodeuri
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/richy-great-MAYEkmn7G6E-unsplash.jpg
tags:
- name: browser
  slug: browser
- name: JavaScript
  slug: javascript
seo_title: Exemple d'encodage d'URL en JavaScript – Comment utiliser encodeURIComponent()
  et encodeURI()
seo_desc: "You might think that encodeURI and encodeURIComponent do the same thing,\
  \ at least from their names. And you might be confused which one to use and when.\n\
  In this article, I will demystify the difference between encodeURI and encodeURIComponent.\
  \ \nWhat ..."
---

Vous pourriez penser que `encodeURI` et `encodeURIComponent` font la même chose, du moins d'après leurs noms. Et vous pourriez être confus quant à celui à utiliser et quand.

Dans cet article, je vais démystifier la différence entre `encodeURI` et `encodeURIComponent`.


### Qu'est-ce qu'un URI et en quoi est-il différent d'une URL ?

**URI** signifie Uniform Resource Identifier.
**URL** signifie Uniform Resource Locator.

Tout ce qui identifie de manière unique une ressource est son URI, comme un identifiant, un nom ou un numéro ISBN. Une URL spécifie une ressource et comment elle peut être accessible (le protocole). Toutes les URL sont des URI, mais tous les URI ne sont pas des URL.


### Pourquoi devons-nous encoder ?

Les URL ne peuvent contenir que certains caractères de l'ensemble standard de 128 caractères ASCII. Les caractères réservés qui n'appartiennent pas à cet ensemble doivent être encodés.

Cela signifie que nous devons encoder ces caractères lorsqu'ils sont passés dans une URL. Les caractères spéciaux tels que `&`, `espace`, `!` lorsqu'ils sont saisis dans une URL doivent être échappés, sinon ils peuvent causer des situations imprévisibles.

Cas d'utilisation :
1. L'utilisateur a soumis des valeurs dans un formulaire qui peuvent être au format chaîne et doivent être passées, comme des champs d'URL.
2. Besoin d'accepter des paramètres de chaîne de requête afin de faire des requêtes GET.


### Quelle est la différence entre encodeURI et encodeURIComponent ?

`encodeURI` et `encodeURIComponent` sont utilisés pour encoder des identifiants de ressource uniforme (URI) en remplaçant certains caractères par une, deux, trois ou quatre séquences d'échappement représentant l'encodage UTF-8 du caractère.

`encodeURIComponent` doit être utilisé pour encoder un **composant URI** - une chaîne qui est censée faire partie d'une URL.

`encodeURI` doit être utilisé pour encoder un **URI** ou une URL existante.

[Voici un tableau pratique de la différence d'encodage des caractères](https://stackoverflow.com/a/23842171)



### Quels caractères sont encodés ?

`encodeURI()` n'encoderas pas : `~!@#$&*()=:/,;?+'`

`encodeURIComponent()` n'encoderas pas : `~!*()'`

Les caractères `A-Z a-z 0-9 - _ . ! ~ * ' ( )` ne sont pas échappés.


### Exemples

```JS
const url = 'https://www.twitter.com'

console.log(encodeURI(url))             //https://www.twitter.com
console.log(encodeURIComponent(url))    //https%3A%2F%2Fwww.twitter.com


const paramComponent = '?q=search'
console.log(encodeURIComponent(paramComponent)) //"%3Fq%3Dsearch"
console.log(url + encodeURIComponent(paramComponent)) //https://www.twitter.com%3Fq%3Dsearch

```

### Quand encoder
1. Lorsque vous acceptez une entrée qui peut contenir des espaces.
    ```JS 
    encodeURI("http://www.mysite.com/a file with spaces.html") //http://www.mysite.com/a%20file%20with%20spaces.html
    ```
2. Lorsque vous construisez une URL à partir de paramètres de chaîne de requête.
   ```JS
    let param = encodeURIComponent('mango')
    let url = "http://mysite.com/?search=" + param + "&length=99"; //http://mysite.com/?search=mango&length=99

   ```
   
3. Lorsque vous acceptez des paramètres de requête qui peuvent contenir des caractères réservés.
 ```JS
    let params = encodeURIComponent('mango & pineapple')
    let url = "http://mysite.com/?search=" + params; //http://mysite.com/?search=mango%20%26%20pineapple


   ```

### Résumé

Si vous avez une URL complète, utilisez `encodeURI`. Mais si vous avez une partie d'une URL, utilisez `encodeURIComponent`.

---

Intéressé par plus de tutoriels et de JSBytes de ma part ? [Inscrivez-vous à ma newsletter.](https://tinyletter.com/shrutikapoor) ou [suivez-moi sur Twitter](https://twitter.com/shrutikapoor08)

###