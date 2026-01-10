---
title: Comment créer un moteur de thèmes en utilisant les variables CSS et le contexte
  React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-29T07:23:32.000Z'
originalURL: https://freecodecamp.org/news/themes-using-css-variables-and-react-context
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/cover-3.png
tags:
- name: CSS
  slug: css
- name: React
  slug: reactjs
- name: themes
  slug: themes
- name: Web Development
  slug: web-development
seo_title: Comment créer un moteur de thèmes en utilisant les variables CSS et le
  contexte React
seo_desc: "By Dor Shinar\nCSS variables are really cool. You can use them for a lot\
  \ of things, like applying themes in your application with ease. \nIn this tutorial\
  \ I'll show you how to integrate them with React to create a ThemeComponent (with\
  \ context!).\nCSS Va..."
---

Par Dor Shinar

Les variables CSS sont vraiment géniales. Vous pouvez les utiliser pour beaucoup de choses, comme appliquer des thèmes dans votre application avec facilité. 

Dans ce tutoriel, je vais vous montrer comment les intégrer avec React pour créer un `ThemeComponent` (avec contexte !).

## Les variables CSS en bref

Tout d'abord, j'aimerais expliquer brièvement ce que sont les variables CSS (ou dans leur nom formel - propriétés personnalisées CSS), et comment les utiliser.

Les variables CSS sont un moyen pour nous de définir des variables qui seront appliquées dans toute notre application. La syntaxe est la suivante :

![Variables CSS](https://www.freecodecamp.org/news/content/images/2020/01/cover-2.png)

Que se passe-t-il ici ? 
En utilisant la notation `--{varName}`, nous pouvons dire à notre navigateur de stocker une variable unique appelée `varName` (ou dans l'exemple ci-dessus, `primary`), puis nous pouvons l'utiliser avec la notation `var(--{varName})` n'importe où dans nos fichiers `.css`.

Cela semble vraiment simple ? C'est parce que c'est le cas. Il n'y a pas grand-chose à comprendre. Selon [caniuse.com](https://caniuse.com/#feat=css-variables), plus de 92 % des utilisateurs dans le monde utilisent un navigateur qui supporte les variables CSS (sauf si vous avez vraiment besoin du support IE, auquel cas vous êtes malchanceux). Donc pour la plupart, elles sont complètement sûres à utiliser.

Si vous voulez en savoir plus, vous pouvez trouver plus d'informations sur la [page MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties).

## Définir les variables CSS à partir de JavaScript

Définir et utiliser les variables CSS à partir de JavaScript est aussi facile que de les définir et les utiliser en CSS. Pour obtenir une valeur définie sur un élément :

```js
const primary = getComputedStyle(element).getPropertyValue("--primary");
```

Cela nous donnera la valeur de la propriété CSS personnalisée `primary` définie pour l'`element`.

Définir une propriété CSS personnalisée fonctionne comme suit :

```js
element.style.setProperty("--light", "#5cd2b6");
```

Ou, si nous voulons définir la propriété pour toute l'application, nous pouvons faire :

```js
document.documentElement.style.setProperty("--light", "#5cd2b6");
```

Et maintenant la propriété `light` sera accessible à tout notre code.

## Le contexte React en bref

L'`API de contexte React` est le seul moyen fourni par React pour passer des props indirectement d'un composant à un composant descendant. 

Dans ce guide, j'utiliserai le hook `useContext`, que vous pouvez lire plus en détail [ici](https://reactjs.org/docs/hooks-reference.html#usecontext). Mais le principe est le même avec les composants de classe.

Tout d'abord, nous devons initialiser un objet de contexte :

```jsx
import React from "react";

export const ThemeSelectorContext = React.createContext({
  themeName: "dark"
});
```

Les paramètres passés à la fonction `React.createContext` sont les paramètres par défaut du contexte. Maintenant que nous avons un objet de contexte, nous pouvons l'utiliser pour "injecter" des props à nos descendants indirects :

```jsx
export default ({ children }) => (
  <ThemeSelectorContext.Provider value={{ themeName: "dark" }}>
    {children}
  </ThemeSelectorContext.Provider>
);
```

Et maintenant, quiconque veut lire les valeurs dans notre contexte peut le faire :

```jsx
import React, { useContext } from "react";

import { ThemeSelectorContext } from "./themer";

export default () => {
  const { themeName } = useContext(ThemeSelectorContext);

  return <div>Mon thème est {themeName}</div>;
};
```

Et voilà ! Peu importe où se trouve notre composant dans la hiérarchie des composants, il a accès à la variable `themeName`. Si nous voulons permettre la modification de la valeur dans notre contexte, nous pouvons passer une fonction comme suit :

```jsx
export default ({ children }) => {
  const [themeName, setThemeName] = useState("dark");

  const toggleTheme = () => {
    themeName === "dark" ? setThemeName("light") : setThemeName("dark");
  };

  return (
    <ThemeSelectorContext.Provider value={{ themeName, toggleTheme }}>
      {children}
    </ThemeSelectorContext.Provider>
  );
};
```

Et pour l'utiliser :

```jsx
import React, { useContext } from "react";

import { ThemeSelectorContext } from "./themer";

export default () => {
  const { themeName, toggleTheme } = useContext(ThemeSelectorContext);

  return (
    <>
      <div>Mon thème est {themeName}</div>
      <button onClick={toggleTheme}>Changer de thème !</button>
    </>
  );
};
```

Cela suffit pour nos besoins, mais si vous le souhaitez, vous pouvez lire davantage sur la [Documentation officielle du contexte React](https://reactjs.org/docs/context.html).

## Mettre tout ensemble

Maintenant que nous savons comment définir les propriétés personnalisées CSS à partir de JavaScript, et que nous pouvons passer des props dans notre arbre de composants, nous pouvons créer un "moteur de thèmes" vraiment sympa et simple pour notre application. Tout d'abord, nous allons définir nos thèmes :

```js
const themes = {
  dark: {
    primary: "#1ca086",
    separatorColor: "rgba(255,255,255,0.20)",
    textColor: "white",
    backgroundColor: "#121212",
    headerBackgroundColor: "rgba(255,255,255,0.05)",
    blockquoteColor: "rgba(255,255,255,0.20)",
    icon: "white"
  },
  light: {
    primary: "#1ca086",
    separatorColor: "rgba(0,0,0,0.08)",
    textColor: "black",
    backgroundColor: "white",
    headerBackgroundColor: "#f6f6f6",
    blockquoteColor: "rgba(0,0,0,0.80)",
    icon: "#121212"
  }
};
```

Cela se trouve être la palette de couleurs que j'utilise pour mon blog, mais vraiment, le ciel est la limite en matière de thèmes, alors n'hésitez pas à expérimenter.

Maintenant, nous créons notre `ThemeSelectorContext` :

```jsx
export const ThemeSelectorContext = React.createContext({
  themeName: "dark",
  toggleTheme: () => {}
});
```

Et notre composant de thème :

```jsx
export default ({ children }) => {
  const [themeName, setThemeName] = useState("dark");
  const [theme, setTheme] = useState(themes[themeName]);

  const toggleTheme = () => {
    if (theme === themes.dark) {
      setTheme(themes.light);
      setThemeName("light");
    } else {
      setTheme(themes.dark);
      setThemeName("dark");
    }
  };

  return (
    <ThemeSelectorContext.Provider value={{ toggleTheme, themeName }}>
      {children}
    </ThemeSelectorContext.Provider>
  );
};
```

Dans ce composant, nous stockons notre objet de thème sélectionné, et le nom du thème sélectionné, et nous avons défini une fonction pour basculer notre thème sélectionné.

Le dernier morceau restant est en fait la définition des propriétés personnalisées CSS à partir de notre thème. Nous pouvons facilement le faire en utilisant l'API `.style.setProperty` :

```js
const setCSSVariables = theme => {
  for (const value in theme) {
    document.documentElement.style.setProperty(`--${value}`, theme[value]);
  }
};
```

Maintenant, pour chaque valeur dans notre objet `theme`, nous pouvons accéder à une propriété CSS avec le même nom (préfixée avec `--` bien sûr). La dernière chose dont nous avons besoin est d'exécuter la fonction `setCSSVariables` chaque fois que le thème est basculé. Donc dans notre composant `Theme`, nous pouvons utiliser le hook `useEffect` comme suit :

```jsx
export default ({ children }) => {
  // code...

  useEffect(() => {
    setCSSVariables(theme);
  });

  // code...
};
```

Le code source complet peut être trouvé [sur github](https://github.com/dorshinar/blog/blob/master/src/components/themer/themer.jsx).

Utiliser notre thème est super pratique :

```css
.title {
  color: var(--primary);
}
```

Et mettre à jour notre thème est tout aussi facile :

```jsx
import Toggle from "react-toggle";

export default () => {
  const { toggleTheme, themeName } = useContext(ThemeSelectorContext);

  return <Toggle defaultChecked={themeName === "dark"} onClick={toggleTheme} />;
};
```

Pour cet exemple, j'utilise le composant `Toggle` de `react-toggle`, mais n'importe quel composant de bascule/bouton ferait l'affaire. Cliquer sur le `Toggle` appellera la fonction `toggleTheme`, et mettra à jour notre thème pour toute l'application, plus besoin de configuration.

C'est tout ! C'est tout ce que vous devez faire pour créer un moteur de thèmes super simple et super propre pour votre application. Si vous voulez voir un exemple réel, vous pouvez consulter le [code source](https://github.com/dorshinar/blog/blob/master/src/components/themer/themer.jsx) de mon blog.

Merci d'avoir lu !

Cet article a été précédemment publié sur mon blog : [dorshinar.me](https://dorshinar.me/themes-using-css-variables-and-react-context). Si vous voulez lire plus de contenu, vous pouvez consulter mon blog, cela me ferait très plaisir.

Si vous voulez me soutenir, vous pouvez <a href='https://ko-fi.com/L3L116P44' target='_blank'><img height='36' style='left:0;border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi4.png?v=2' border='0' alt='Offrez-moi un café sur ko-fi.com' /></a>