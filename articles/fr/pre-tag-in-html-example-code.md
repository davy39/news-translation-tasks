---
title: <pre> Balise en HTML – Exemple de code
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-05T21:33:51.000Z'
originalURL: https://freecodecamp.org/news/pre-tag-in-html-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pre-tag.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: <pre> Balise en HTML – Exemple de code
seo_desc: "The HTML <pre> tag defines a preformatted block of text. It comes in handy\
  \ when you want to display text where the typographical formatting affects the meaning\
  \ of the content, such as code snippets and poems. \nBy default, browsers ignore\
  \ white space ..."
---

La balise HTML `<pre>` définit un bloc de texte préformaté. Elle est utile lorsque vous souhaitez afficher du texte où la mise en forme typographique affecte le sens du contenu, comme des extraits de code et des poèmes. 

Par défaut, les navigateurs ignorent les espaces blancs de tout type – espaces supplémentaires, sauts de ligne, tabulations ou tout autre caractère de formatage – spécifiés dans le HTML. 

Mais avec la balise `<pre>`, vous pouvez préserver tous les espaces blancs que vous souhaitez. La famille de polices par défaut assignée à tout texte à l'intérieur de `<pre>` est `monospace`, mais vous pouvez la remplacer avec du CSS si vous le souhaitez. 

Dans ce tutoriel, nous allons examiner en détail la balise `<pre>`. Je vais vous montrer comment elle fonctionne en utilisant quelques extraits de code "avec et sans" afin que vous puissiez vous amuser davantage à écrire du HTML, car le HTML n'a jamais été conçu pour être ennuyeux.

### Syntaxe de base

Comme beaucoup d'autres éléments HTML, la balise `<pre>` nécessite également une balise de fermeture (`</pre>`).

```html
<pre>
            Bonjour le monde, 
            ce texte est à l'intérieur d'une balise pre, tous les espaces       blancs     sont 


        préservés
</pre>
```

Consultez la capture d'écran ci-dessous pour le résultat :
![basic](https://www.freecodecamp.org/news/content/images/2021/08/basic.png)

## Exemples de la balise `<pre>` en HTML

Voici quelques extraits de code et captures d'écran qui montrent comment fonctionne la balise `<pre>`. 

### Espaces blancs en HTML sans la balise `<pre>`
```html
<div>
     <p>Il y a des espaces blancs supplémentaires dans les deux mots suivants, mais ils sont ignorés        par le navigateur : Bonjour  
     Monde</p>
</div>
```

```css
body {
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100vh;
      }

p, pre {
          font-size: 1.2rem;
      }
```

![ss1-1](https://www.freecodecamp.org/news/content/images/2021/08/ss1-1.png)

### Espaces blancs en HTML avec la balise `pre`

```html
<div>
     <p>Il y a des espaces blancs supplémentaires dans les deux mots suivants, rendus visibles par la        balise <code>pre</code> 
     : <pre>Bonjour   Monde</pre> </p>
</div>
```
![ss2-1](https://www.freecodecamp.org/news/content/images/2021/08/ss2-1.png)

### Tabulation en HTML sans la balise `pre`

```html
<div>
     <p>Il y a des tabulations entre les mots suivants, mais elles sont ignorées par le navigateur :      Je suis   un   campeur</p>
</div>
```

![ss3-1](https://www.freecodecamp.org/news/content/images/2021/08/ss3-1.png)

### Tabulation en HTML avec la balise `pre` 

```html
<div>
     <p>Il y a des tabulations entre les mots suivants, rendues visibles avec la                    balise <code>pre</code> <pre> : Je suis   
     un   campeur</pre></p>
</div>
```

![ss4-1](https://www.freecodecamp.org/news/content/images/2021/08/ss4-1.png)

### Sauts de ligne en HTML sans la balise `<pre>` 

```html
<div>
<p>
        Il y a des sauts de ligne entre les mots suivants : 
        Je suis

        un

        campeur
    </p>
</div>
```

![ss5-1](https://www.freecodecamp.org/news/content/images/2021/08/ss5-1.png)

### Sauts de ligne en HTML avec la balise `<pre>`

```html
<div>
    <p>
    Il y a des sauts de ligne entre les mots suivants : 
   <pre>
   Je suis

   un

   campeur
   </pre>
    </p>
</div>
```

![ss6-1](https://www.freecodecamp.org/news/content/images/2021/08/ss6-1.png)

Comme vous pouvez probablement l'imaginer maintenant, la balise `<pre>` est super utile dans l'art CSS (et l'art HTML aussi), les illustrations, pour insérer des extraits de code dans le HTML, et bien plus encore.

## Comment insérer des extraits de code sans la balise `<pre>`

Souvent, vous devrez peut-être afficher des extraits de code sur des pages web à des fins académiques ou dans la documentation d'un langage de programmation ou d'un framework. Cela vous aide, ainsi que les mainteneurs, à communiquer correctement avec les apprenants. 

Et vous voudrez préserver les espaces blancs même après avoir utilisé la balise `<code>` pour le faire, et c'est exactement ce que fait la balise `<pre>`.

```html
<div> 
<h3>Quelques réinitialisations CSS</h3>
      <p>
        Saviez-vous que vous pouvez supprimer le remplissage et la marge par défaut que les navigateurs
        insèrent dans les pages web ?
      </p>
      <code> * { padding: 0; margin: 0; box-sizing: border-box; }</code>
</div>
```

```css
 body {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
```

![ss7-1](https://www.freecodecamp.org/news/content/images/2021/08/ss7-1.png)

## Comment insérer des extraits de code avec la balise `<pre>` en HTML

```html
<div>
<h3>Quelques réinitialisations CSS</h3>
      <p>
        Saviez-vous que vous pouvez supprimer le remplissage et la marge par défaut que les navigateurs
        insèrent dans les pages web ?
      </p>
      <pre>
    <code>
        * {
         padding: 0;
         margin: 0;
         box-sizing: border-box;
       }
    </code>
    </pre>
      <p>Maintenant vous le savez.</p>
</div>
```

![ss8](https://www.freecodecamp.org/news/content/images/2021/08/ss8.png)

### Un peu d'art sans la balise `<pre>`

```html
 <div><p>                     ^^^^^^^^^^^^^^^^^^^^^
                <><><>       ^ Je suis Kolade,        ^
               <>    <>     ^  Développeur web du ^
                <><><>  ^^^^   Nigeria.           ^          
                  <>        ^  Je suis fier d'être un  ^
                  <>         ^ Campeur.            ^  
               <> <> <>       ^^^^^^^^^^^^^^^^^^^^^  
             <>   <>   <>
            <>    <>     <>
                  <>    
                <>  <>  
               <>    <>
              <>      <>
             <>        <>
            <>          <>
           <>            <></p> </div>
```

```css
body {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
      }
```


![ss9](https://www.freecodecamp.org/news/content/images/2021/08/ss9.png)

### Un peu d'art avec la balise `<pre>`

```html
<div>
      <pre>
                              ^^^^^^^^^^^^^^^^^^^^^
                <><><>       ^ Je suis Kolade,        ^
               <>    <>     ^  Développeur web du ^
                <><><>  ^^^^   Nigeria.           ^          
                  <>        ^  Je suis fier d'être un  ^
                  <>         ^ Campeur.            ^  
               <> <> <>       ^^^^^^^^^^^^^^^^^^^^^  
             <>   <>   <>
            <>    <>     <>
                  <>    
                <>  <>  
               <>    <>
              <>      <>
             <>        <>
            <>          <>
           <>            <>
      </pre>
    </div>
```

![ss10](https://www.freecodecamp.org/news/content/images/2021/08/ss10.png)

## Comment corriger les barres de défilement inutiles

Parce que le texte à l'intérieur d'une balise `<pre>` est affiché dans le navigateur tel qu'il est dans le code, avoir un bloc ou une ligne de texte plus large que la largeur de l'écran disponible entraîne une barre de défilement horizontale. Vous pouvez également obtenir une barre de défilement verticale inutile. 

```html
    <div>
        <pre> Ce sont quelques textes lorem : Lorem ipsum 
            
 dolor sit                amet consectetur adipisicing elit. Amet rem nam ea nihil fuga doloribus voluptatem sed officiis iusto. Eveniet quaerat sit quisquam                consequatur necessitatibus 


 totam placeat, ut unde                  nesciunt.
        </pre>
    </div>
```

![problem](https://www.freecodecamp.org/news/content/images/2021/08/problem.png)

Pour vous en débarrasser, CSS fournit une propriété `white-space`. En définissant sa valeur sur `wrap`, vous supprimez les barres de défilement.

```css
pre {
      white-space: pre-wrap;
    }
```

![problemFix](https://www.freecodecamp.org/news/content/images/2021/08/problemFix.png)

## Conclusion
 
Au cours de ce tutoriel, vous avez vu comment fonctionne la balise `<pre>` en HTML. Maintenant, allez vous amuser avec elle dans votre prochain projet de codage. 

Merci d'avoir lu, et continuez à coder.