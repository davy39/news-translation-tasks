---
title: Vous êtes dans l'enfer des if/else — voici comment en sortir
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-25T16:34:57.000Z'
originalURL: https://freecodecamp.org/news/so-youre-in-if-else-hell-here-s-how-to-get-out-of-it-fc6407fec0e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hEbJvltnslRrdEzjWQ7Img.jpeg
tags:
- name: design patterns
  slug: design-patterns
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Vous êtes dans l'enfer des if/else — voici comment en sortir
seo_desc: 'By Adeel Imran


  _Photo by [Unsplash](https://unsplash.com/@markusspiske?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Markus
  Spiske / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  What is ...'
---

Par Adeel Imran

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-245.png)
_Photo par [Unsplash](https://unsplash.com/@markusspiske?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Markus Spiske</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

### De quoi parle ce sujet ?

Si vous venez d'un milieu `javascript`, vous avez peut-être entendu les termes `callback hell` ou `async/await hell`. Cela ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*13tInwUptNwGlHemJrxTig.png)
_L'horreur._

Il existe une situation similaire avec l'utilisation de `if/else`. Vous pourriez qualifier cela d'obsession des développeurs, ou l'ignorer en pensant que c'est acceptable dans certaines situations.

Je ne suis pas d'accord. Comme le dit le proverbe... imaginez simplement que la personne qui maintiendra votre code ensuite sait où vous travaillez et peut venir vous crier dessus.

Pour les besoins de cet article, je vais démontrer un exemple en utilisant ReactJS. Le principe lui-même peut être appliqué en JavaScript ou dans n'importe quelle langue, d'ailleurs.

**Avant de commencer**, l'exemple `_<MyButton_` /> n'est peut-être pas le meilleur exemple pour expliquer le problème des if/else imbriqués. Mais espérons qu'il vous donnera une bonne ligne directrice quant à ce qu'est le problème et comment l'éviter.

Dessinons un tableau. On vous donne un bouton à implémenter en `React` et le bouton a 2 options pour un thème, soit `default` soit `primary`. Vous pensez que c'est simple et vous écrivez votre composant `<MyButton` /> :

```jsx
const MyButton = ({ theme, content }) => {
  let className = '';                
  if (theme === 'default') {
    className = 'default-btn';
  } else if (theme === 'primary') {
    className = 'primary-btn';
  }
                   
  return (
    <button className={className}>{content}</button>
  );
}
```

Un certain temps passe et un autre développeur reçoit la tâche d'ajouter une fonctionnalité pour les coins arrondis du bouton pour les deux thèmes, default et primary. Le développeur qui prend la tâche est très adepte des opérateurs ternaires. Ils finissent par faire quelque chose comme ci-dessous :

```jsx
const MyButton = ({ theme, rounded, content }) => {
  let className = '';                
  if (theme === 'default') {
    className = rounded ? 'default-btn rounded' : 'default-btn';
  } else if (theme === 'primary') {
    className = rounded ? 'primary-btn rounded' : 'primary-btn';
  }
                   
  return (
    <button className={className}>{content}</button>
  );
}
```

Le temps passe et un autre développeur reçoit la tâche d'ajouter un état `hover` pour les boutons `default` et `primary`. Maintenant, l'autre développeur ne veut pas faire de changements dans le code déjà implémenté, de peur de casser quelque chose.

Alors ils écrivent une instruction if séparée :

```jsx
const MyButton = ({ theme, rounded, hover, content }) => {
  let className = '';                
  if (theme === 'default') {
    className = rounded ? 'default-btn rounded' : 'default-btn';
  } else if (theme === 'primary') {
    className = rounded ? 'primary-btn rounded' : 'primary-btn';
  }
  
  if (hover) {
    className = className + ' hover';
  }
                   
  return (
    <button className={className}>{content}</button>
  );
}
```

Jusqu'à présent, tout va bien...

#### C'est là que cela devient intéressant

Plus tard, une exigence finale arrive des mois plus tard pour ajouter une animation lorsque l'utilisateur **survole** un bouton qui a un thème **primary** et est de type **rounded**.

Maintenant, sur la base de cette exigence, toute la structure de l'API change le composant `<MyButto`n/> . Le développeur travaillant sur le code se retrouve avec une logique comme celle-ci :

```jsx
const MyButton = ({ theme, rounded, hover, animation, content }) => {
  let className = '';                
  if (theme === 'default') {
    className = rounded ? 'default-btn rounded' : 'default-btn';
    if (hover) {
      className = className + ' hover';
    }
  } else if (theme === 'primary') {
    if (rounded) {
      if (hover) {
        if (animation) {
           className = 'primary-btn rounded hover my-custom-animation';
        } else {
          className = 'primary-btn rounded hover';
        }
      } else {
        className = 'primary-btn rounded';
      }
    } else {
      if (hover) {
        className = 'primary-btn hover';
      } else {
        className = 'primary-btn';
      }
    }
  }

  return (
    <button className={className}>{content}</button>
  );
}
```

Cela a dégénéré beaucoup trop vite... n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*XwM0kI6bX9utPF0VwT20Gg.gif)
_et vous vous dites à vous-même, il n'y avait rien que vous auriez pu faire :(_

Pour rendre ce code plus simple, nous devons comprendre tous les états possibles que ce code peut avoir. J'ai fait un tableau de toutes les combinaisons possibles à un moment donné pour le bouton.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mnWn59gP2Lwb7f3huo783A.png)
_Toutes les combinaisons possibles de valeurs que le composant &lt;MyButton /&gt; peut avoir à un moment donné_

Si cela semble un peu compliqué, vous pouvez essayer de regarder ce tableau suivant pour mieux comprendre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*H5yLaIar39mkoVbzwJlLlQ.png)
_Ceci est le même que le précédent, les valeurs FALSE sont omises ici pour simplifier_

**La chose clé lors de l'écriture de code est de comprendre le flux de données de votre code. Une fois que vous en avez une compréhension complète, tout devient plus simple.**

#### Solution

Sur la base des critères donnés ci-dessus, je peux écrire mon code comme ceci pour le simplifier.

```jsx
const MyButton = ({ theme, rounded, hover, animation, content }) => {
  const isThemeDefault = theme === 'default'
  const isThemePrimary = theme === 'primary';
  const isRounded = rounded === true;
  const isHover = hover === true;
  const isAnimated = animation === true;
  
  const isPrimaryAnimated = isThemePrimary && isAnimated;
  
  let className = isThemePrimary ? 'primary-btn' : 'default-btn';

  if (isRounded) {
    className = `${className} rounded`;
  }
  if (isHover) {
    className = `${className} hover`;
  }
  if (isPrimaryAnimated) {
    className = `${className} animated`;
  }
 
  return (
    <button className={className}>{content}</button>
  );
}
```

Ce code est maintenant beaucoup plus lisible. Tout développeur qui travaille sur ce code peut facilement étendre sa fonctionnalité et continuer sa vie, en sachant qu'il a fait un travail merveilleux avec le code.

Vous pouvez essayer de jouer avec le code si vous le souhaitez, pour voir s'il correspond à tous les cas d'utilisation.

%[https://codesandbox.io/s/0pl6xvqrnw?from-embed]

Avec l'approche de codage de type automates (machines à états finis) :

* Le code est plus lisible maintenant
* Le code est plus maintenable

N'hésitez pas à partager vos pensées. Merci d'avoir lu.

Vous pouvez également me contacter sur Twitter [**@adeelibr**](https://twitter.com/adeelibr)

> Référence et Inspiration : [Stack Exchange Forum](https://softwareengineering.stackexchange.com/questions/205803/how-to-tackle-a-branched-arrow-head-anti-pattern)