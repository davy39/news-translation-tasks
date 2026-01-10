---
title: Comment ajouter la localisation (l10n) à votre application React avec react-i18next
subtitle: ''
author: Tom Mondloch
co_authors: []
series: null
date: '2021-03-29T22:40:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-localization-to-your-react-app
coverImage: https://cdn-media-2.freecodecamp.org/w1280/605df42a9618b008528a7ca8.jpg
tags:
- name: localization
  slug: localization
- name: React
  slug: react
seo_title: Comment ajouter la localisation (l10n) à votre application React avec react-i18next
seo_desc: 'When you add localization to a website you''re making it available in multiple
  languages. This tutorial aims to teach you how to do that to a small react app using
  react-i18next.

  The way it works is simple. Instead of putting the text you want to disp...'
---

Lorsque vous ajoutez la localisation à un site web, vous le rendez disponible dans plusieurs langues. Ce tutoriel vise à vous apprendre comment faire cela pour une petite application React en utilisant `react-i18next`.

Le fonctionnement est simple. Au lieu de mettre le texte que vous souhaitez afficher dans les composants, tout va dans un fichier JSON. 

Vous utilisez ensuite les clés du fichier dans les composants pour obtenir le texte. Vous pouvez ajouter des fichiers JSON supplémentaires avec les mêmes clés et des valeurs traduites pour chaque langue souhaitée. La langue définie déterminera quel fichier JSON est utilisé comme texte pour l'application.

Suivez les étapes ci-dessous pour apprendre comment ajouter cette fonctionnalité à une application React.


## Cloner le boilerplate

Si vous souhaitez coder en suivant, vous pouvez [cloner le boilerplate depuis GitHub](https://github.com/moT01/react-i18next-demo) ou [ouvrir le boilerplate sur replit](https://repl.it/github/moT01/react-i18next-demo). Il s'agit d'une petite application React avec deux pages et quelques composants :

![les deux pages de l'application](https://raw.githubusercontent.com/moT01/moT01/master/i18n-demo.png)

Le but est de rendre l'application disponible en anglais et en espagnol. 

Si vous suivez ce tutoriel, je vous recommande de jeter un rapide coup d'œil aux composants et à la structure des fichiers pour vous familiariser avec le code. Les fichiers JS dans le dossier `src` sont ceux que vous allez modifier. Les composants `Nav`, `Home` et `Page2` contiennent tout le texte qui doit être traduit.


## Ajouter les dépendances

`react-i18next` est basé sur `i18next`, vous aurez donc besoin des deux packages comme dépendances pour traduire l'application. Vous pouvez les ajouter avec :

```sh
npm install --save react-i18next i18next
```

Si vous suivez ce tutoriel, démarrez l'application avec `npm start` pour que vous puissiez jeter un coup d'œil aux deux pages.


## Créer la structure des fichiers

Dans le dossier `src`, créez un dossier `i18n` pour contenir toutes les informations liées à la traduction de l'application. Voici la structure que j'ai utilisée et qui est assez courante :

```
src
+-- i18n
    +-- locales
    |    +-- en
    |        +-- translations.json
    |    +-- es
    |        +-- translations.json
    +-- config.js
```

Le fichier `config.js` contient la configuration de l'instance `i18n`. Les deux fichiers JSON contiendront le texte qui va dans l'application. `en` pour l'anglais et `es` pour l'espagnol. Si vous suivez ce tutoriel, créez la structure des fichiers dans le boilerplate.


## Configurer l'instance i18n

L'instance `i18n` contiendra toutes vos traductions, la langue actuelle et d'autres informations et méthodes nécessaires. Vous pouvez la configurer dans le fichier `config.js` comme ceci :

```js
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

i18n.use(initReactI18next).init({
  fallbackLng: 'en',
  lng: 'en',
  resources: {
    en: {
      translations: require('./locales/en/translations.json')
    },
    es: {
      translations: require('./locales/es/translations.json')
    }
  },
  ns: ['translations'],
  defaultNS: 'translations'
});

i18n.languages = ['en', 'es'];

export default i18n;
```

En haut, importez les dépendances nécessaires. Ensuite, `use(initReactI18next)` liera `react-i18next` à l'instance `i18n`. 

Les deux premières propriétés de l'objet paramètre `init` sont une langue de secours (`fallbackLng`) et une langue par défaut (`lng`). J'ai défini les deux en anglais (`en`). 

Les `resources` sont les fichiers JSON avec les traductions que vous avez créés à l'étape précédente. Les espaces de noms (`ns`) et l'espace de noms par défaut (`defaultNS`) sont les clés de l'objet `resources`. 

Vous pouvez diviser vos traductions en plusieurs fichiers (espaces de noms) si vous avez une grande application pour simplifier les fichiers. Dans ce cas, vous ajouteriez plus qu'un seul fichier dans l'objet `resources` et l'ajouteriez au tableau des espaces de noms. Cette application est petite, donc toutes les traductions peuvent aller dans un seul fichier.


## Ajouter l'instance i18n à votre application

Dans le fichier `index.js` du boilerplate, qui contient toute l'application, importez l'instance `i18n` que vous avez créée comme ceci :

```js
import './i18n/config';
```

Ensuite, ajoutez un objet vide à vos deux fichiers `translations.json` pour éviter toute erreur. Vous remplirez les clés plus tard.


## Traduire un composant fonctionnel avec le hook useTranslation

Le fichier `Nav.js` est le premier composant à traduire. C'est un composant fonctionnel, vous pouvez donc utiliser le hook `useTranslation`. Importez-le en haut avec `import { useTranslation } from 'react-i18next'`. 

Ensuite, au lieu d'utiliser le retour implicite avec le composant, ajoutez des accolades et l'instruction return pour que vous puissiez déclarer une variable. Obtenez la fonction `t` du hook avec `const { t } = useTranslation();`. 

Ensemble, cela devrait ressembler à quelque chose comme ceci :

```js
import { useTranslation } from 'react-i18next';

const Nav = () => {
  const { t } = useTranslation();

  return (
    
  );
}
```

Le texte que vous souhaitez traduire dans ce composant est `Home` et `Page 2`. Dans votre fichier `translations.json` anglais, ajoutez deux propriétés à l'objet :

```json
{
  "home": "Home",
  "page2": "Page 2"
}
```

Maintenant, vous pouvez passer ces clés à la fonction `t` pour obtenir le texte. Dans le composant `Nav.js`, utilisez la fonction `t` pour traduire `Home` et `Page 2` en texte anglais comme ceci : `t('key-from-json-file')`. 

Voici à quoi ces lignes devraient ressembler :

```js
import { useTranslation } from 'react-i18next';

const Nav = () => {
  const { t } = useTranslation();

  return (
    

    <Link to="/">{t('home')}</Link>
    <Link to="/page2">{t('page2')}</Link>
  );
}
```

## Aperçu en espagnol

Les deux boutons de navigation devraient fonctionner pour l'anglais. Ajoutez les deux mêmes clés au fichier JSON espagnol pour voir à quoi cela ressemblera en espagnol. Voici les traductions :

```json
{
  "home": "Casa",
  "page2": "Página 2"
}
```

Après cela, allez dans le fichier `config.js`, définissez le `lng` (langue par défaut) sur `es` et rechargez la page. Les liens de navigation devraient s'afficher en espagnol. Lorsque vous avez terminé, vous pouvez définir la langue par défaut sur `en`.


## Traduire un composant de classe en utilisant withTranslation

Dans le fichier `Home.js`, il y a trois phrases et un bouton à traduire. Vous pouvez utiliser la fonction `t` à nouveau pour la plupart d'entre eux, mais celui-ci est un composant de classe, vous devez donc utiliser le composant d'ordre supérieur (HOC) `withTranslation`. Importez-le en haut avec `import { withTranslation } from 'react-i18next';`. 

Ensuite, en bas du fichier, exportez-le avec `export default withTranslation()(Home);`. Maintenant, la fonction `t` sera passée dans les props du composant pour être utilisée. 

Dans la méthode render, obtenez la fonction avec `const { t } = this.props`. Le code devrait ressembler à quelque chose comme ceci :

```js
import { withTranslation } from 'react-i18next';

class Home extends Component {
  

  render() {
    const { t } = this.props;

    
  }
}

export default withTranslation()(Home);
```

La première ligne à traduire, `Welcome, {username}`, contient une variable. Vous pouvez passer un objet à la fonction `t` avec votre variable comme ceci : `t('key-from-json-file', { variable: value })`. Cela ressemblerait à ceci dans le composant :

```js
<p>{t('welcome', { username: username })}</p>
```

Ajoutez cela à la place de la ligne "welcome". Ensuite, dans le fichier JSON anglais, ajoutez la nouvelle clé : `"welcome": "Welcome, {{username}}"`. La variable `username` passée à la fonction `t` sera placée dans la chaîne pour vous.

Ajoutez également la propriété au fichier espagnol : `"welcome": "Bienvenido {{username}}"`. Suivez les instructions précédentes si vous souhaitez le prévisualiser en espagnol.


### Défi

Vous devriez maintenant être capable de traduire quelques éléments par vous-même. Essayez de faire les deux lignes suivantes, `Change your username:` et `Submit`, comme les autres.

Voici les propriétés pour le fichier JSON anglais :

```json
"change-username": "Change your username:",
"submit": "Submit"
```

Et les traductions espagnoles :

```json
"change-username": "Cambia tu nombre de usuario:",
"submit": "Enviar"
```

Ajoutez ce qui précède dans les deux fichiers JSON. Ensuite, traduisez le texte du `label` et du `button` avec la fonction `t`.

Lorsque vous avez terminé, la partie render de `Home.js` devrait ressembler à ceci :

```js
render() {
  const { username } = this.state;
  const { t } = this.props;

  return (
    <div className='body'>
      <p>{t('welcome', {username: username})}</p>

      <div>
        <label>{t('change-username')}</label>
        <input type='text' onChange={this.updateUsername.bind(this)} />
        <button onClick={this.setUsername.bind(this)}>
          {t('submit')}
        </button>
      </div>

      <p>Click <Link to='/page2'>here</Link> to go to page 2, {username}</p>
    </div>
  );
}
```

Changez le `lng` dans `config.js` en `en` ou `es` et rechargez l'application pour tester les langues.


## Traduire des éléments imbriqués de base avec le composant Trans

Laissez la dernière ligne de la page d'accueil pour l'instant et passez au fichier `Page2.js`. Les deux phrases à traduire contiennent d'autres éléments - une balise `strong` et un composant `Link`. 

La règle générale est d'utiliser la fonction `t` des exemples précédents lorsque vous le pouvez, mais si vous avez des éléments ou d'autres composants dans le texte, vous devrez utiliser le composant `Trans`. 

Tout d'abord, importez `Trans` et `withTranslation` depuis `react-i18next`. Ensuite, exportez le composant en utilisant à nouveau `withTranslation`. Cela devrait ressembler à ceci :

```js
import { Trans, withTranslation } from 'react-i18next';

const Page2 = () => (
  
);

export default withTranslation()(Page2);
```

Si vous avez des balises HTML *de base* dans votre texte, vous pouvez envelopper le composant `Trans` autour de la clé de votre fichier JSON, et les balises seront ajoutées au texte.

Changez le premier `<p>` dans le composant en ceci :

```js
<p><Trans>this-is-page2</Trans></p>
```

Ensuite, ajoutez la clé aux deux fichiers `translation.json`. Pour l'anglais :

```json
"this-is-page2": "This is <strong>page 2</strong>"
```

Et le JSON espagnol :

```json
"this-is-page2": "Esta es la <strong>página 2</strong>"
```

Ce qui précède traduira la première ligne de `Page2.js`. Les balises de base par défaut que vous pouvez utiliser avec cette méthode sont `br`, `strong`, `i` et `p`, mais cette liste peut être étendue dans la configuration. Définissez la langue dans la configuration sur l'espagnol pour vous assurer que cela fonctionne.


## Traduire des éléments imbriqués complexes avec Trans

La ligne suivante contient un composant `Link` imbriqué, donc c'est un peu plus compliqué. Vous devez utiliser à nouveau `Trans`, mais passer la clé dans ses props comme `i18nKey` et garder le `Link` comme son enfant. Le `Link` n'a pas besoin d'avoir de texte. Voici à quoi cela ressemble :

```js
<Trans i18nKey='go-to-home'>
  <Link to='/'></Link>
</Trans>
``` 

Assurez-vous de garder les balises `<p>`. Ajoutez la propriété associée au JSON anglais :

```json
"go-to-home": "Go to <0>the home page</0>"
```

Et la version espagnole :

```json
"go-to-home": "Ir a la <0>pagina principal</0>"
```

Les balises `<0>` représentent le premier enfant du composant `Trans`, dans ce cas, `Link`. S'il y avait un autre enfant, il utiliserait les balises `<1>`, et ainsi de suite.

Changez la langue dans la configuration si vous souhaitez voir les deux locales différentes.


## Traduire des éléments imbriqués complexes avec une variable

Une dernière ligne à traduire. La dernière ligne du fichier `Home.js` contient un élément `Link` imbriqué et une variable. Vous devez utiliser à nouveau `Trans`, alors ajoutez-le à l'importation existante en haut.

Si vous devez utiliser une variable avec `Trans`, elle peut être placée à l'intérieur de l'élément. Donc la dernière ligne :

```js
<p>Click <Link to='/page2'>here</Link> to go to page 2, {username}</p>
```

Peut être traduite comme ceci :

```js
<Trans i18nKey='go-to-page2'>
  <Link to='/page2'></Link>
  {{username}}
</Trans>
```

La clé est passée à `Trans` comme une prop comme avant. L'élément `Link` imbriqué et la variable `{{ username }}` doivent être quelque part dans le composant, peu importe où.

Assurez-vous d'ajouter les valeurs aux fichiers JSON. Pour l'anglais :

```json
"go-to-page2": "Click <0>here</0> to go to page 2, {{username}}"
```

Et l'espagnol :
```json
"go-to-page2": "Haga clic <0>aquí</0> para ir a la página 2, {{username}}"
```


## Comment changer de langue

Tout le texte souhaité devrait maintenant être disponible en anglais et en espagnol. La dernière chose à faire est de faciliter le passage d'une langue à l'autre. 

Le fichier `Footer.js` contient quelques boutons et une fonction `changeLanguage`. Importez le hook `useTranslation` depuis `react-i18next` en haut du fichier. En haut du composant `Footer`, obtenez l'instance `i18n` comme ceci : `const { i18n } = useTranslation();`. 

Enfin, dans la fonction `changeLanguage`, utilisez la méthode `i18n.changeLanguage()`, en lui passant `e.target.value`, pour changer la langue.

Ensemble, cela ressemble à ceci :

```js
import { useTranslation } from 'react-i18next';

const Footer = () => {
  const { i18n } = useTranslation();

  function changeLanguage(e) {
    i18n.changeLanguage(e.target.value);
  }

  return(
    <div className='footer'>
      <button onClick={changeLanguage} value='en'>English</button>
      <button onClick={changeLanguage} value='es'>Español</button>
    </div>
  )
}
```

Maintenant, vous devriez pouvoir changer de langue en cliquant sur les boutons de chaque page.


## Comment ajouter des langues

À partir de là, l'application est prête à être traduite dans n'importe quelle langue assez facilement. Vous devez simplement ajouter une autre langue à la configuration, et le fichier JSON avec le texte traduit pour l'accompagner.


## Conclusion

Espérons que cela vous a donné un aperçu de la manière de développer rapidement une application React dans de nombreuses langues du monde. 

Il existe de nombreuses autres fonctionnalités et détails avec ces outils. Voir les liens ci-dessous pour plus d'informations. 


### Liens utiles

- Voir une [démo du projet terminé](https://react-i18next-demo.mot01.repl.co/)
- Voir le [code source du projet terminé](https://github.com/moT01/react-i18next-demo/tree/solution)
- La [documentation react-i18next](https://react.i18next.com) entre dans plus de détails sur certaines des méthodes de traduction, le rendu côté serveur, les tests et les utilisations supplémentaires avec React.
- La [documentation i18next](https://www.i18next.com/) contient des informations utiles sur la configuration supplémentaire, l'API, la traduction de texte complexe et les fonctionnalités supplémentaires.