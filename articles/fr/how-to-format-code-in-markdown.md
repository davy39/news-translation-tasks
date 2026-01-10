---
title: Comment formater du code en Markdown
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-format-code-in-markdown
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d0f740569d1a4ca35a8.jpg
tags:
- name: markdown
  slug: markdown
- name: toothbrush
  slug: toothbrush
seo_title: Comment formater du code en Markdown
seo_desc: 'There are two ways to format code in Markdown. You can either use inline
  code, by putting backticks (`) around parts of a line, or you can use a code block,
  which some renderers will apply syntax highlighting to.

  Inline Code

  You can use inline code f...'
---

Il existe deux façons de formater du code en Markdown. Vous pouvez soit utiliser du code en ligne, en plaçant des backticks (`) autour de parties d'une ligne, soit utiliser un bloc de code, auquel certains renderers appliqueront une coloration syntaxique.

## **Code en ligne**

Vous pouvez utiliser le formatage de code en ligne pour mettre en évidence une petite commande ou un morceau de syntaxe dans une ligne que vous écrivez.

Par exemple, vous pouvez souhaiter mentionner la méthode `Array.protoype.map()` de JavaScript. En utilisant le formatage de code en ligne, il est clair que ceci est un morceau de code. Vous pouvez également l'utiliser pour illustrer une commande terminal, comme `yarn install`.

Pour utiliser le formatage de code en ligne, il suffit d'encadrer le code que vous souhaitez formater avec des backticks. Sur un clavier QWERTY standard US, cela se trouve à gauche du '1', et au-dessus de la touche Tab. Plus d'informations sur l'emplacement du backtick sur les claviers internationaux sont fournies ci-dessous.

Par exemple, écrire `Array.prototype.map()` en markdown sera rendu comme `Array.prototype.map()`.

## **Blocs de code**

Pour écrire des extraits de code plus longs ou plus détaillés, il est souvent préférable de les placer dans un bloc de code. Les blocs de code vous permettent d'utiliser plusieurs lignes, et markdown les rendra dans leur propre boîte et avec une police de type code.

Pour ce faire, commencez votre bloc par une ligne de trois backticks. Cela signale à markdown que vous créez un bloc de code. Vous devrez terminer par une autre ligne de trois backticks. Par exemple :

```  
var add2 = function(number) {  
   return number + 2;  
}  
```

sera rendu en markdown comme :

```text
var add2 = function(number) {
  return number + 2;
}
```

### Colorisation syntaxique

Bien que ce ne soit pas supporté nativement par markdown, de nombreux moteurs markdown, y compris celui utilisé par GitHub, supporteront la colorisation syntaxique. Cela signifie qu'en indiquant à markdown le langage que vous utilisez dans le bloc de code, il ajoutera des couleurs comme le ferait un IDE.

Vous pouvez faire cela en ajoutant le nom du langage sur la même ligne que vos trois backticks d'ouverture. Dans l'exemple ci-dessus, si au lieu de la première ligne étant ``` vous écrivez ```js, alors la colorisation JavaScript sera appliquée au bloc.

```js
var add2 = function(number) {
	return number + 2;
}
```

La colorisation syntaxique peut être appliquée à plus que juste JavaScript, cependant. Vous pouvez utiliser ```html :

```html
<div class="row">
  <div class="col-md-6 col-md-offset-3">
    <h1>Hello World</h1>
  </div>
</div>
```

```ruby :

```ruby
"Hello World".split('').each do |letter|
  puts letter
end
```

ou ```python :

```python
a, b = 0, 1
while b < 10:
    print(b)
    a, b = a, a + b
```

Rappelez-vous simplement que tous les moteurs markdown n'appliqueront pas la colorisation syntaxique.

## Backticks sur les claviers internationaux

L'emplacement de la touche backtick peut être différent sur différents claviers, et si vous n'utilisez pas un clavier QWERTY standard US, il peut être difficile à trouver. [Ce](http://superuser.com/a/254077/122424) guide utile liste certaines des façons de trouver votre touche backtick, que nous avons rassemblées ici ci-dessous :

### QWERTY et QWERTZ :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/a7daf1d707e12e207d47f0eb70ba01d97ffd1924_1_690x327.png)

### AZERTY :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/8f65c339ce4eefd9d79841f3dc54f4c37cab2e77.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/de291f0895b0fed992726a62d654f4e1f0e421f3.png)