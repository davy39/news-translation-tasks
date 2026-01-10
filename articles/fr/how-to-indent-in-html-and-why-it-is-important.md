---
title: Comment indenté le code HTML – Et pourquoi c'est important
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-06-01T15:40:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-indent-in-html-and-why-it-is-important
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/irvan-smith-ymn_TY_MBn8-unsplash.jpg
tags:
- name: freeCodeCamp Curriculum Guide
  slug: freecodecamp-curriculum-guide
- name: best practices
  slug: best-practices
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Comment indenté le code HTML – Et pourquoi c'est important
seo_desc: 'When you are building out HTML files, it''s really important to indent
  your code. But how do you do that in HTML and why is it important?

  In this article, I will show you how to properly indent your HTML files and explain
  why it is important to proper...'
---

Lorsque vous construisez des fichiers HTML, il est vraiment important d'indenter votre code. Mais comment faire cela en HTML et pourquoi est-ce important ?

Dans cet article, je vais vous montrer comment indenter correctement vos fichiers HTML et expliquer pourquoi il est important de formater correctement votre code.

## Comment indenter votre code en HTML

Chaque fois que vous avez des éléments HTML imbriqués dans d'autres éléments HTML, il est préférable d'utiliser l'indentation. Les éléments imbriqués sont connus comme les enfants de leur élément parent.

Dans cet exemple, j'ai un élément `p` imbriqué dans un élément `div`. Pour indenter l'élément `p`, je vais le déplacer de deux espaces vers la droite.

```html
<div>
  <p>Voici à quoi ressemble l'indentation pour le HTML</p>
</div>
```

Cela est considéré comme une bonne pratique et rendra votre code plus lisible par d'autres développeurs. Maintenant, nous pouvons voir que l'élément `p` est imbriqué dans son élément parent qui est le `div`.

Dans cet exemple suivant, j'ai un élément `h2` et `p` imbriqués dans un élément `main` **sans** indentation.

```html
<main>
<h2>Apprenons l'indentation</h2>
<p>Il n'y a pas d'indentation ici</p>
</main>
```

Mais si j'édite le code en déplaçant les éléments `h2` et `p` de deux espaces vers la droite, maintenant nous avons une indentation correcte.

```html
<main>
  <h2>Apprenons l'indentation</h2>
  <p>Voici l'indentation</p>
</main>
```

Les éléments `h2` et `p` sont des enfants de l'élément `main`.

## Exemples couramment utilisés d'indentation en HTML

### Listes non ordonnées

Les éléments `li` sont indentés de deux espaces vers la droite et imbriqués dans l'élément `ul`. L'élément `ul` est le parent des éléments `li`.

```html
<ul>
  <li>Gâteau</li>
  <li>Pizza</li>
  <li>Salade</li>
  <li>Pomme</li>
</ul>
```

### Listes ordonnées

Les éléments `li` sont indentés de deux espaces vers la droite et imbriqués dans l'élément `ol`. L'élément `ol` est le parent des éléments `li`.

```html
<ol>
  <li>Conduisez 1,2 miles et tournez à gauche sur Cherry Lane</li>
  <li>Conduisez 4,5 miles et tournez à droite sur Sycamore Rd.</li>
  <li>Conduisez 400 pieds et arrêtez-vous au feu</li>
  <li>Tournez à gauche au feu</li>
  <li>Arrivez à la destination sur votre droite</li>
</ol>
```

## Pourquoi l'indentation est-elle importante ?

Lorsque vous écrivez du code, il est important d'écrire du code lisible par d'autres développeurs. Une grande partie de la lisibilité consiste à indenter correctement votre HTML.

Dans cet exemple, j'ai copié tout le code du projet [Learn HTML by Building a Cat Photo App](https://www.freecodecamp.org/learn/2022/responsive-web-design/#learn-html-by-building-a-cat-photo-app) et supprimé toute l'indentation pour vous montrer à quoi ressemble un mauvais formatage de code.

```html
<html lang="en">
<head>
<title>CatPhotoApp</title>
</head>
<body>
<h1>CatPhotoApp</h1>
<main>
<section>
<h2>Cat Photos</h2>
<!-- TODO: Add link to cat photos -->
<p>
Click here to view more
<a target="_blank" href="https://freecatphotoapp.com">cat photos</a>.
</p>
<a href="https://freecatphotoapp.com"
><img
src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
alt="A cute orange cat lying on its back."
/></a>
</section>
<section>
<h2>Cat Lists</h2>
<h3>Things cats love:</h3>
<ul>
<li>cat nip</li>
<li>laser pointers</li>
<li>lasagna</li>
</ul>
<figure>
<img
src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg"
alt="A slice of lasagna on a plate."
/>
<figcaption>Cats <em>love</em> lasagna.</figcaption>
</figure>
<h3>Top 3 things cats hate:</h3>
<ol>
<li>flea treatment</li>
<li>thunder</li>
<li>other cats</li>
</ol>
<figure>
<img
src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"
alt="Five cats looking around a field."
/>
<figcaption>Cats <strong>hate</strong> other cats.</figcaption>
</figure>
</section>
<section>
<h2>Cat Form</h2>
<form action="https://freecatphotoapp.com/submit-cat-photo">
<fieldset>
<legend>Is your cat an indoor or outdoor cat?</legend>
<label
><input
id="indoor"
type="radio"
name="indoor-outdoor"
value="indoor"
checked
/>
Indoor</label
>
<label
><input
id="outdoor"
type="radio"
name="indoor-outdoor"
value="outdoor"
/>
Outdoor</label
>
</fieldset>
<fieldset>
<legend>What's your cat's personality?</legend>
<input
id="loving"
type="checkbox"
name="personality"
value="loving"
checked
/>
<label for="loving">Loving</label>
<input id="lazy" type="checkbox" name="personality" value="lazy" />
<label for="lazy">Lazy</label>
<input
id="energetic"
type="checkbox"
name="personality"
value="energetic"
/>
<label for="energetic">Energetic</label>
</fieldset>
<input
type="text"
name="catphotourl"
placeholder="cat photo URL"
required
/>
<button type="submit">Submit</button>
</form>
</section>
</main>
<footer>
<p>
No Copyright -
<a href="https://www.freecodecamp.org">freeCodeCamp.org</a>
</p>
</footer>
</body>
</html>

```

Ce n'est pas une bonne pratique HTML du tout car il est vraiment difficile de lire et de comprendre ce que fait le code. Si vous essayiez de soumettre quelque chose comme cela dans un cadre professionnel de développement, votre équipe ne serait pas du tout contente de vous.

Maintenant, je vais prendre ce même code et l'indenter correctement pour vous montrer la différence.

```html
<html lang="en">
  <head>
    <title>CatPhotoApp</title>
  </head>
  <body>
    <h1>CatPhotoApp</h1>
    <main>
      <section>
        <h2>Cat Photos</h2>
        <!-- TODO: Add link to cat photos -->
        <p>
          Click here to view more
          <a target="_blank" href="https://freecatphotoapp.com">cat photos</a>.
        </p>
        <a href="https://freecatphotoapp.com"
          ><img
            src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
            alt="A cute orange cat lying on its back."
        /></a>
      </section>
      <section>
        <h2>Cat Lists</h2>
        <h3>Things cats love:</h3>
        <ul>
          <li>cat nip</li>
          <li>laser pointers</li>
          <li>lasagna</li>
        </ul>
        <figure>
          <img
            src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg"
            alt="A slice of lasagna on a plate."
          />
          <figcaption>Cats <em>love</em> lasagna.</figcaption>
        </figure>
        <h3>Top 3 things cats hate:</h3>
        <ol>
          <li>flea treatment</li>
          <li>thunder</li>
          <li>other cats</li>
        </ol>
        <figure>
          <img
            src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"
            alt="Five cats looking around a field."
          />
          <figcaption>Cats <strong>hate</strong> other cats.</figcaption>
        </figure>
      </section>
      <section>
        <h2>Cat Form</h2>
        <form action="https://freecatphotoapp.com/submit-cat-photo">
          <fieldset>
            <legend>Is your cat an indoor or outdoor cat?</legend>
            <label
              ><input
                id="indoor"
                type="radio"
                name="indoor-outdoor"
                value="indoor"
                checked
              />
              Indoor</label
            >
            <label
              ><input
                id="outdoor"
                type="radio"
                name="indoor-outdoor"
                value="outdoor"
              />
              Outdoor</label
            >
          </fieldset>
          <fieldset>
            <legend>What's your cat's personality?</legend>
            <input
              id="loving"
              type="checkbox"
              name="personality"
              value="loving"
              checked
            />
            <label for="loving">Loving</label>
            <input id="lazy" type="checkbox" name="personality" value="lazy" />
            <label for="lazy">Lazy</label>
            <input
              id="energetic"
              type="checkbox"
              name="personality"
              value="energetic"
            />
            <label for="energetic">Energetic</label>
          </fieldset>
          <input
            type="text"
            name="catphotourl"
            placeholder="cat photo URL"
            required
          />
          <button type="submit">Submit</button>
        </form>
      </section>
    </main>
    <footer>
      <p>
        No Copyright -
        <a href="https://www.freecodecamp.org">freeCodeCamp.org</a>
      </p>
    </footer>
  </body>
</html>

```

Cela est beaucoup plus facile à lire et maintenant nous pouvons voir tous les éléments enfants imbriqués dans leurs éléments parents et comprendre ce que fait le code.

## Conclusion

Lorsque vous écrivez du HTML, il est important de formater correctement votre code en utilisant une bonne indentation. Vous pouvez indenter les éléments en les déplaçant de deux espaces vers la droite.

```html
<main>
  <h2>Apprenons l'indentation</h2>
  <p>Voici l'indentation</p>
</main>
```

Cela rendra votre code plus lisible par d'autres développeurs et montre la relation entre les éléments enfants et parents HTML.

J'espère que vous avez apprécié cet article et bonne chance dans votre parcours de développeur.