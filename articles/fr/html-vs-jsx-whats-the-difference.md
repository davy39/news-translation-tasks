---
title: HTML vs JSX – Quelle est la différence ?
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-05-17T21:11:58.000Z'
originalURL: https://freecodecamp.org/news/html-vs-jsx-whats-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/
seo_title: HTML vs JSX – Quelle est la différence ?
---

.png
tags:
- name: guide pour débutants
  slug: guide-pour-debutants
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: JSX
  slug: jsx
- name: React
  slug: react
seo_title: null
seo_desc: "HTML vs JSX\nL'Hypertext Markup Language (HTML) est le langage standard pour les documents qui déterminent la structure d'une page web. \nL'HTML est un langage très important dans le développement web. Votre code est soit écrit en HTML à l'origine, soit compilé vers celui-ci pour que les navigateurs..."
---

## HTML vs JSX

L'Hypertext Markup Language (HTML) est le langage standard pour les documents qui déterminent la structure d'une page web. 

L'HTML est un langage très important dans le développement web. Votre code est soit écrit en HTML à l'origine, soit compilé vers celui-ci pour que les navigateurs puissent le lire.

Le JSX, d'un autre côté, signifie JavaScript Syntax Extension ou JavaScript XML comme certains aiment l'appeler. 

Il a été créé comme un sucre syntaxique pour ```React.createElement()```. C'est une extension de JavaScript qui permet aux développeurs d'écrire du HTML directement au sein de JavaScript. Ainsi, lorsque vous écrivez du JSX, vous écrivez techniquement du JavaScript et du HTML ensemble. 

De plus, cela signifie que les mots-clés réservés de JavaScript doivent être conservés intacts. C'est pourquoi l'attribut « for » en HTML devient « htmlFor » en JSX, car « for » est l'un des mots-clés réservés les plus courants de JavaScript.

En termes de support par les navigateurs, l'HTML est supporté par tous. Le JSX, en revanche, n'a jamais vraiment été destiné à l'être, vous avez donc besoin d'un compilateur comme Babel ou Webpack pour transpiler le JSX en JavaScript que les navigateurs comprennent. 

## Les principales différences entre HTML et JSX

### Vous devez retourner un seul élément parent en JSX

L'une des différences majeures entre HTML et JSX est qu'en JSX, vous devez retourner un seul élément parent, sinon il ne compilera pas. 

Beaucoup de développeurs utilisent ```<div>...</div>```, mais une meilleure option que beaucoup de gens utilisent est le « fragment », ```<>...</>```, ce qui rend le code plus lisible. 

En HTML, vous êtes libre de faire ce que vous voulez car vous n'avez pas à retourner un seul élément parent.

![jsx1](https://www.freecodecamp.org/news/content/images/2021/05/jsx1.png)
Ici, vous pouvez voir que le JSX ne compile pas car il n'y a pas d'élément parent.

![jsx2](https://www.freecodecamp.org/news/content/images/2021/05/jsx2.png)
Et ici, le JSX compile car il y a un élément parent (fragment).

### Vous pouvez implémenter du JS directement dans le JSX

En JSX, il est possible d'écrire du JavaScript directement. Vous pouvez le faire en plaçant le JavaScript entre accolades ```{...}```. Alors qu'en HTML, vous avez besoin d'une balise script ou d'un fichier JavaScript externe pour implémenter du JavaScript :

```javascript
const Article = () => {
  return (
    <>
      <div>
        <p>Hi campers</p>
        <p>How's coding going</p>
        <p>What is up?</p>
        {new Date().toDateString()}
        <br />
        <br />
        {2 + 5} is seven in word
        <br />
      </div>
    </>
  );
};
export default Article;
```

### Toutes les balises s'auto-ferment en JSX 
Les balises peuvent s'auto-fermer en JSX. C'est-à-dire qu'il est possible d'avoir ```<div></div>``` sous la forme ```<div />``` et ```<span></span>``` sous la forme ```<span />```. Vous ne voudrez peut-être pas faire cela, mais c'est possible. 

Les balises auto-fermantes en HTML peuvent se fermer sans le slash avant le chevron fermant, c'est-à-dire que ```<br />``` pourrait fonctionner comme ```<br>```. Mais en JSX, vous devez inclure le slash. Cela devrait vous rappeler quelque chose – le JSX repose fortement sur la syntaxe HTML 4.


![jsx3](https://www.freecodecamp.org/news/content/images/2021/05/jsx3.png)
Ici, vous pouvez voir que le JSX ne compile pas car il n'y a pas de barre oblique avant le chevron fermant de la balise de saut de ligne.

![jsx4](https://www.freecodecamp.org/news/content/images/2021/05/jsx4.png)
Et ici, vous pouvez voir que le JSX compile car il y a une barre oblique dans la balise de saut de ligne.

### className et htmlFor, pas class et for en JSX
Pour définir les noms de classes et les attributs for en JSX, vous ne le faites pas avec `class` ou `for`, car les deux sont des mots-clés réservés en JavaScript. 

En fait, vous créez des composants de classe avec le mot-clé `class`. Ainsi, pour définir des noms de classes en JSX, vous utilisez « `className` » et pour les attributs des labels, vous écrivez « `htmlFor` » :

```javascript
const Article = () => {
  return (
    <>
      <div className="container">
        <p>Hi campers</p>
        <p>How's coding going</p>
        <p>What is up?</p>
        {new Date().toDateString()}
        <br />
        <br />
        {2 + 5} is seven in word
        <br />
        <form>
          <label htmlFor="name">Name</label>
          <input type="text" />
        </form>
      </div>
    </>
  );
};

export default Article;
```

### Écrivez tous les attributs HTML en camelCase en JSX 
Vous devez écrire tous les attributs HTML et les références d'événements en camelCase lorsque vous écrivez du JSX. Ainsi, `onclick` devient `onClick`, `onmouseover` devient `onMouseOver`, et ainsi de suite :

```javascript
const Article = () => {
  const sayHI = () => {
    alert("Hi Campers");
  };

  return (
    <>
      <div className="container">
        <p>Hi campers</p>
        <p>How's coding going</p>
        <p>What is up?</p>
        {new Date().toDateString()}
        <br />
        <br />
        {2 + 5} is seven in word
        <br />
        <button onClick={sayHI}>ALert Hi</button>
      </div>
    </>
  );
};
export default Article;
```

### Écrivez les styles en ligne sous forme d'objets en JSX 
Et enfin, pour définir des styles en ligne pour le JSX, vous l'écrivez sous forme d'objet, avec les propriétés en camelCase, les valeurs entre guillemets, puis vous le passez en ligne au JSX. 

Cela signifie que vous devez ouvrir un attribut style et utiliser des accolades au lieu de guillemets. Contrairement à l'HTML où vous êtes libre de définir des millions de styles directement à l'intérieur de la balise d'ouverture sans les écrire sous forme d'objets et les mettre entre guillemets :

```javascript
const Article = () => {
  const inlineStyle = {
    color: "#2ecc71",
    fontSize: "26px",
  };
  return (
    <>
      <div className="container">
        <p style={inlineStyle}>Hi campers</p>
        <p>How's coding going</p>
        <p>What is up?</p>
        {new Date().toDateString()}
        <br />
        <br />
        {2 + 5} is seven in word
        <br />
        <button onClick={sayHI}>ALert Hi</button>
      </div>
    </>
  );
};
export default Article;
```


Vous pouvez choisir d'écrire l'objet directement dans l'attribut style – c'est-à-dire en ouvrant deux paires d'accolades et en y plaçant les propriétés et les valeurs.

Mais une façon plus propre est de définir l'objet en dehors du JSX, puis de le passer dans la balise d'ouverture.

```javascript
const Article = () => {
  return (
    <>
      <div className="container">
        <p style={{ color: "#2ecc71", fontSize: "26px" }}>Hi campers</p>
        <p>How's coding going</p>
        <p>What is up?</p>
        {new Date().toDateString()}
        <br />
        <br />
        {2 + 5} is seven in word
        <br />
      </div>
    </>
  );
};

export default Article;
```
Notez que vous ne devriez pas utiliser de styles en ligne en HTML pur – vous ne voulez pas gâcher le SEO de votre site web.

## C'est tout !

Merci de m'avoir lu. Pour me contacter, consultez mon [portfolio](ksound22.github.io), ou suivez-moi sur [Twitter](https://twitter.com/koladechris), où je passe la majeure partie de mon temps à tweeter et à m'engager dans tout ce qui concerne le développement web.