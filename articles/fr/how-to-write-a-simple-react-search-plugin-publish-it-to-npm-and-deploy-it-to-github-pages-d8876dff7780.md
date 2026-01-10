---
title: Comment écrire un plugin de recherche simple avec React, le publier sur npm
  et le déployer sur Github Pages
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-15T21:42:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-simple-react-search-plugin-publish-it-to-npm-and-deploy-it-to-github-pages-d8876dff7780
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UpNlBkE42X6JrNZ1bYqsOA.png
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment écrire un plugin de recherche simple avec React, le publier sur
  npm et le déployer sur Github Pages
seo_desc: 'By Nirmalya Ghosh

  In this article, we’re going to write a simple search plugin in React. Through this
  article, I hope to help fellow developers understand how to write plugins using
  React, publish them to npm and deploy a demo to Github pages.

  The so...'
---

Par Nirmalya Ghosh

Dans cet article, nous allons écrire un plugin de recherche simple avec [React](https://reactjs.org/). À travers cet article, j'espère aider les autres développeurs à comprendre comment écrire des plugins avec React, les publier sur [npm](https://www.npmjs.com/) et déployer une démonstration sur Github Pages.

Le code source du plugin est disponible sur [Github](https://github.com/ghoshnirmalya/react-search-box).

## Installation

Nous allons initialiser notre plugin en utilisant [create-react-library](https://github.com/transitive-bullshit/create-react-library/), qui est un CLI pour créer facilement des bibliothèques React réutilisables. Ce CLI possède de nombreuses [fonctionnalités](https://github.com/transitive-bullshit/create-react-library/#features) et nous aidera à générer un modèle de base pour notre plugin.

Pour utiliser create-react-library, nous devons l'installer globalement :

```
npm install -g create-react-library
```

La commande ci-dessus installera create-react-library globalement et nous pourrons générer un nouveau module depuis n'importe quel répertoire. Pour générer un nouveau répertoire, tapez la commande suivante dans le répertoire où vous souhaitez initialiser le plugin :

```
create-react-library
```

La commande ci-dessus posera quelques questions basiques sur votre module et, une fois que vous y aurez répondu, un modèle de base pour le plugin sera généré.

![Image](https://cdn-media-1.freecodecamp.org/images/PljaKvDkbnE20hvlTKH6UrGrv0nFNajUKnGx)
_Initialisation du projet avec [create-react-library](https://github.com/transitive-bullshit/create-react-library/" rel="noopener" target="_blank" title=")_

Maintenant, vous devez exécuter le plugin (pour surveiller les modifications que vous y apportez) et l'exemple. Dans un onglet, vous pouvez exécuter :

```
cd react-search-box && yarn start
```

Et, dans un autre onglet, vous devez exécuter l'application d'exemple :

```
cd react-search-box/example && yarn start
```

La dernière commande exécutera un projet [create-react-app](https://facebook.github.io/create-react-app/) qui importe votre plugin. Si vous apportez des modifications à votre plugin, elles seront reflétées dans l'application d'exemple. Vous pouvez voir l'état actuel de votre plugin en visitant [http://localhost:3000](http://localhost:3000/).

![Image](https://cdn-media-1.freecodecamp.org/images/daNJKly2eX8HNgjW9aDn5PI3um-Rx1JVlaYf)
_État initial du plugin après initialisation avec [create-react-library](https://github.com/transitive-bullshit/create-react-library/" rel="noopener" target="_blank" title=")_

## Conception de la zone de saisie

Ajoutons la première fonctionnalité de base : une zone de saisie qui permettra aux utilisateurs de taper dedans.

```
import React, { Component } from 'react'import PropTypes from 'prop-types'
```

```
import styles from './styles.css'
```

```
export default class ReactSearchBox extends Component {  static propTypes = {    /**     * value: La valeur par défaut pour la zone de saisie.     * placeholder: Le texte de l'espace réservé pour la zone de saisie.     */    value: PropTypes.string,    placeholder: PropTypes.string  }
```

```
  state = {    value: ''  }
```

```
  componentDidMount() {    const { value } = this.props
```

```
    this.setState({      value: value    })  }
```

```
  handleInputChange = e => {    const { value } = e.target
```

```
  this.setState({      value: value    })  }
```

```
  inputNode = () => {    /**     * Cette fonction est responsable de l'affichage de la zone de saisie.     * La zone de saisie sert de source d'entrée pour les données de l'utilisateur.     */    const { placeholder } = this.props    const { value } = this.state
```

```
    return (      <input        className={styles.input}        type='text'        placeholder={placeholder}        value={value}        onChange={this.handleInputChange}      />    )  }
```

```
  render() {    return <div className={styles.container}>{this.inputNode()}</div>  }}
```

Dans le code ci-dessus, nous créons un élément input qui a un attribut `className`, un attribut `type`, un attribut `placeholder`, un attribut `value` et un gestionnaire `onChange`. La plupart de ces attributs sont très basiques. Le seul attribut intéressant est l'attribut `onChange` qui est déclenché chaque fois que l'utilisateur tape dans la zone de saisie.

Chaque fois qu'il y a un changement dans la zone de saisie, nous appelons la fonction `handleInputChange`. La fonction `handleInputChange` reçoit l'événement comme argument. Nous utilisons ici une [fonction fléchée ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions). Ainsi, nous n'avons pas besoin de lier explicitement `this` avec la fonction `handleInputChange`. Vous pouvez lire [Quand devrais-je utiliser les fonctions fléchées avec React](https://frontarm.com/articles/when-to-use-arrow-functions/) par [James K Nelson](https://twitter.com/james_k_nelson).

Puisque nous avons un état `value` que nous passons à la zone de saisie comme attribut, nous mettons à jour cet état `value` chaque fois qu'il y a un changement dans la zone de saisie via la fonction `handleInputChange`.

```
handleInputChange = e => {  const { value } = e.target
```

```
  this.setState({    value  })}
```

Si vous visitez [http://localhost:3000](http://localhost:3000/), vous verrez une zone de saisie à l'écran. Vous pouvez taper dans la zone de saisie et la valeur sera mise à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/P5R0CV2siS1BaLpAvp3FW7c5Y8wAcMcs63fA)
_État initial de la zone de saisie_

Si vous vérifiez dans [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en), vous verrez que la valeur de la zone de saisie est mise à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/hB2qoFsdmF90pz-DdbiGWLVJ-GcBlmHlPsWP)

![Image](https://cdn-media-1.freecodecamp.org/images/RDdZ2Gk38kACwg6jmrL6sLQlUqtLUuQB1GiF)

C'est toute la fonctionnalité dont nous avons besoin pour la zone de saisie. Ensuite, nous allons concevoir une liste déroulante qui apparaîtra une fois que la chaîne que l'utilisateur tape dans la zone de saisie correspond à un enregistrement qui sera fourni à notre plugin via la propriété `data`.

## Conception de la liste déroulante

Dans cette section, nous allons implémenter une liste déroulante, qui apparaîtra avec un tableau d'enregistrements correspondant à la chaîne que l'utilisateur tape dans la zone de saisie. Le tableau initial des enregistrements sera fourni en utilisant la propriété `data` que nous allons implémenter en premier.

```
import React, { Component } from "react";import ReactSearchBox from "react-search-box";
```

```
export default class App extends Component {  data = [    {      key: "john",      value: "John Doe"    },    {      key: "jane",      value: "Jane Doe"    },    {      key: "mary",      value: "Mary Phillips"    },    {      key: "robert",      value: "Robert"    },    {      key: "karius",      value: "Karius"    }  ];
```

```
  render() {    return (      <div className="container">        <ReactSearchBox          placeholder="Placeholder"          value="Doe"          data={this.data}        />      </div>    );  }}
```

Notre plugin doit être importé et défini comme dans le bloc de code ci-dessus. Vous importez `ReactSearchBox` puis vous passez un tableau d'objets (le tableau `data` dans ce cas) à `ReactSearchBox`.

Pour l'instant, nous allons afficher la liste déroulante si une propriété `value` est passée à notre plugin. Plus tard, nous allons refactoriser notre composant pour afficher la liste déroulante si un enregistrement du tableau `data` correspond à la propriété `value` fournie.

Notre plugin ressemblerait maintenant à quelque chose comme ceci :

```
import React, { Component } from 'react'import PropTypes from 'prop-types'
```

```
import styles from './styles.css'
```

```
export default class ReactSearchBox extends Component {  static propTypes = {    /**     * value: La valeur par défaut pour la zone de saisie.     * placeholder: Le texte de l'espace réservé pour la zone de saisie.     * data: Un tableau d'objets qui sert de source de données pour la liste déroulante.     */    value: PropTypes.string,    placeholder: PropTypes.string,    data: PropTypes.array.isRequired  }
```

```
  static defaultProps = {    /**     * Définir la propriété data comme un tableau vide au cas où elle n'est pas passée.     */    data: []  }
```

```
  state = {    value: ''  }
```

```
  componentDidMount() {    /**     * Cette fonction est la même que précédemment     */    }
```

```
  handleInputChange = e => {    /**     * Cette fonction est la même que précédemment     */    }
```

```
  inputNode = () => {    /**     * Cette fonction est la même que précédemment     */  }
```

```
  dropdownNode = () => {    /**     * Cette fonction est responsable de l'affichage de la liste déroulante.     */    const { data } = this.props
```

```
    return (      <div className={`react-search-box-dropdown ${styles.dropdown}`}>        <ul className={styles.dropdownList}>          {data.map(record => {            return (              <li                key={record.key}                className={`react-search-box-dropdown-list-item ${                  styles.dropdownListItem                }`}              >                {record.value}              </li>            )          })}        </ul>      </div>    )  }
```

```
render() {    return (      <div className={styles.container}>        {this.inputNode()}        {this.dropdownNode()}      </div>    )  }}
```

Le code pour la liste déroulante est présent dans la fonction `dropdownNode`. En fonction de la propriété `data` fournie à notre plugin, nous créons une liste d'éléments `li` et les affichons dans la liste déroulante.

Si nous visitons [http://localhost:3000/](http://localhost:3000/), nous verrons une liste déroulante avec une zone de saisie.

![Image](https://cdn-media-1.freecodecamp.org/images/mGlZbD5-5b4zICli-oEy1trP5j5Z4HvJan73)

C'est toute la fonctionnalité dont nous avons besoin pour la liste déroulante. Ensuite, nous allons refactoriser notre plugin pour afficher la liste déroulante uniquement lorsque des enregistrements correspondent à la requête que l'utilisateur tape dans la zone de saisie.

## Refactorisation de notre plugin pour afficher la liste déroulante uniquement lorsque des enregistrements correspondent à la requête

C'est la dernière étape de notre processus de développement.

Tout d'abord, nous devons ajouter un package nommé [fuse.js](http://fusejs.io/) qui est une bibliothèque de recherche floue légère. Elle nous aidera à vérifier si la requête que l'utilisateur tape dans la zone de saisie correspond à des enregistrements de la propriété `data` fournie à notre plugin.

Ajoutons-le à notre liste de dépendances en utilisant la commande ci-dessous :

```
yarn add fuse.js
```

Maintenant, nous allons refactoriser notre plugin pour vérifier si la requête correspond à l'un des enregistrements.

```
import React, { Component } from 'react'import PropTypes from 'prop-types'import Fuse from 'fuse.js'
```

```
import styles from './styles.css'
```

```
export default class ReactSearchBox extends Component {  static propTypes = {    /**     * Ceci est identique à précédemment     */  }
```

```
  static defaultProps = {    /**     * Ceci est identique à précédemment     */  }
```

```
  state = {    /**     * 'matchedRecords' stocke les éléments lorsque la valeur de la zone de saisie     * correspond à un élément de la propriété 'data'.     */    value: '',    matchedRecords: []  }
```

```
  constructor(props) {    super(props)
```

```
    const { data } = props
```

```
    /**     * Ces options proviennent du plugin Fuse. Consultez http://fusejs.io/     * pour plus de détails.     */    const options = {      /**       * À quel point l'algorithme de correspondance abandonne-t-il. Un seuil de 0,0       * nécessite une correspondance parfaite (des lettres et de l'emplacement), un seuil       * de 1,0 correspondrait à n'importe quoi.       */      threshold: 0.05,      /**       * Détermine approximativement où dans le texte le motif est censé être trouvé.       */      location: 0,      /**       * Détermine à quel point la correspondance doit être proche de l'emplacement flou       * (spécifié par location). Une correspondance exacte de lettres qui est à distance       * de caractères de l'emplacement flou serait notée comme une non-correspondance complète. Une distance de 0 nécessite que la correspondance soit à l'emplacement exact spécifié, une distance de 1000 nécessiterait une correspondance parfaite dans les 800 caractères de l'emplacement à trouver       * en utilisant un seuil de 0,8.       */      distance: 100,      /**       * Lorsque défini pour inclure les correspondances, seules les correspondances dont la longueur dépasse cette       * valeur seront retournées. (Par exemple, si vous souhaitez ignorer les retours d'index de caractères uniques, définissez sur 2).       */      minMatchCharLength: 1,      /**       * Liste des propriétés qui seront recherchées. Cela prend en charge les propriétés imbriquées,       * la recherche pondérée, la recherche dans les tableaux de chaînes et d'objets.       */      keys: ['value']    }
```

```
    this.fuse = new Fuse(data, options)  }
```

```
  componentDidMount() {    const { value } = this.props
```

```
    /**     * Si une 'value' est passée en tant que prop, vérifiez si elle correspond à un élément     * de la prop 'data'. Si un enregistrement correspond à     * la requête, mettez à jour l'état 'matchedRecord' avec l'objet(s) correspondant(s).     *     * De plus, mettez à jour l'état 'value' avec la prop 'value'.     */    const matchedRecords = this.fuse.search(value)
```

```
    this.setState({      value: value.trim(),      matchedRecords,      /**       * Contrôle l'affichage et le masquage de la liste déroulante lorsqu'il y a une valeur       * dans la zone de saisie. Mais, fermez la liste déroulante une fois qu'un élément de la liste déroulante est       * cliqué.       */      showDropdown: !!value.trim()    })  }
```

```
  handleInputChange = e => {    /**     * Cette fonction est responsable de la vérification si des éléments de la valeur de la zone de saisie     * correspondent à un élément de la prop 'data'. Si un élément correspond,     * alors cet objet correspondant est poussé dans l'état 'matchedRecords'. Cet état     * est responsable du peuplement de la liste déroulante.     */
```

```
    const { value } = e.target
```

```
/**     * Vérifiez toutes les valeurs du tableau 'data' dont la 'value' correspond à     * 'value' en utilisant le plugin Fuse.     */    const matchedRecords = this.fuse.search(value)
```

```
/**     * Mettez à jour l'état 'value' avec la valeur de la zone de saisie     * Mettez à jour l'état 'matchedRecords' avec les enregistrements correspondants du tableau de données.     */    this.setState({      value: value.trim(),      matchedRecords,      /**       * Affichez la liste déroulante lors du changement de la saisie       */      showDropdown: true    })  }
```

```
  inputNode = () => {    /**     * Cette fonction est la même que précédemment     */  }
```

```
  handleDropdownItemClick = record => {    /**     * Cette fonction est responsable de la mise à jour de la valeur à l'intérieur de     * la zone de saisie lorsqu'un élément de la liste déroulante est cliqué.     *     * L'état 'value' est mis à jour avec la valeur de l'enregistrement cliqué.     */
```

```
  const { value } = record
```

```
  this.setState({      value,      /**       * Masquez la liste déroulante une fois qu'un élément de la liste déroulante est cliqué       */      showDropdown: false    })  }
```

```
  dropdownNode = () => {    /**     * Cette fonction est responsable de l'affichage de la liste déroulante.     * Lorsqu'une valeur de la zone de saisie correspond à une valeur de la     * prop 'data', cet objet correspondant du tableau 'data' apparaît     * dans le li de la liste déroulante. Les valeurs correspondantes sont stockées dans l'état     * 'matchedRecords'.     */    const { matchedRecords, showDropdown } = this.state
```

```
/**     * Si aucune valeur n'est présente dans la zone de saisie, alors la liste déroulante     * ne doit pas apparaître.     */    if (!showDropdown) return false
```

```
  return (      <div className={`react-search-box-dropdown ${styles.dropdown}`}>        <ul className={styles.dropdownList}>          {matchedRecords.map(record => {            return (              <li                key={record.key}                className={`react-search-box-dropdown-list-item ${                  styles.dropdownListItem                }`}                onClick={() => this.handleDropdownItemClick(record)}              >                {record.value}              </li>            )          })}        </ul>      </div>    )  }
```

```
  render() {    /**     * Cette fonction est la même que précédemment     */  }}
```

J'ai ajouté des commentaires à l'intérieur de chaque fonction qui indiquent ce que fait cette fonction particulière. La fonctionnalité de base que nous obtenons du code ci-dessus est la suivante :

1. L'utilisateur tape dans la zone de saisie (nous appellerons le texte que l'utilisateur tape comme `query`).
2. `onChange` de la zone de saisie, le plugin vérifie si la valeur actuelle de la zone de saisie correspond à un enregistrement fourni à notre plugin via la propriété `data`.
3. Si un enregistrement correspond à la requête, nous affichons une liste déroulante avec une liste des enregistrements correspondants.
4. Si aucun enregistrement ne correspond à la requête, nous n'affichons pas la liste déroulante.

Si vous visitez [http://localhost:3000](http://localhost:3000/), vous pouvez voir que la liste déroulante apparaît avec une liste d'enregistrements correspondants. La liste déroulante se masquera si la zone de saisie est vide.

![Image](https://cdn-media-1.freecodecamp.org/images/lqp6qofrsyKaZnVF23hCThbNrbg7P4Hes4pj)
_Les enregistrements correspondants apparaîtront maintenant dans la liste déroulante_

C'est tout le code dont nous avons besoin. Ensuite, nous allons pousser nos modifications vers un dépôt [Github](https://github.com).

## Pousser notre code vers Github

Dans cette section, nous allons créer un dépôt Github et pousser notre code vers Github.

Si vous êtes nouveau sur Github, vous pouvez suivre cet [article](https://help.github.com/articles/create-a-repo/) pour savoir comment créer un dépôt. Une fois que vous avez terminé la création d'un nouveau dépôt, vous devez [ajouter un remote à votre plugin](https://help.github.com/articles/adding-a-remote/).

```
git remote add origin https://github.com/ghoshnirmalya/react-search-box
```

Dans mon cas, j'ajoute `[https://github.com/ghoshnirmalya/react-search-box](https://github.com/ghoshnirmalya/react-search-box)` car je veux que mes modifications de code soient disponibles sur ce dépôt. Pour votre cas, ce sera une URL différente.

Une fois que c'est fait, vous pouvez pousser vos modifications vers le dépôt Github :

```
git push origin master
```

![Image](https://cdn-media-1.freecodecamp.org/images/cf0l9TRsqpn4NF4drOrVHmtFchSwBJh8Rs5Z)
_Dépôt Github ([https://github.com/ghoshnirmalya/react-search-box](https://github.com/ghoshnirmalya/react-search-box" rel="noopener" target="_blank" title="))_

Votre code est maintenant disponible sur votre dépôt Github.

## Publier notre plugin sur npm

Dans cette section, nous allons publier notre code sur [npm](https://www.npmjs.com/). npm est le gestionnaire de paquets pour JavaScript.

[create-react-library](https://github.com/transitive-bullshit/create-react-library/) a déjà une [fonctionnalité](https://github.com/transitive-bullshit/create-react-library/#publishing-to-npm) grâce à laquelle nous pouvons publier notre plugin sur le registre npm. Vous devez simplement exécuter la commande suivante :

```
yarn publish
```

![Image](https://cdn-media-1.freecodecamp.org/images/YaosMlCMfhq1GXSSk2ArFJzJe-mKzXPISnpw)
_[https://www.npmjs.com/package/react-search-box](https://www.npmjs.com/package/react-search-box" rel="noopener" target="_blank" title=")_

## Déployer une application d'exemple sur Github Pages

Dans cette section, nous allons déployer une application d'exemple qui utilisera notre plugin sur [Github Pages](https://pages.github.com/).

[create-react-library](https://github.com/transitive-bullshit/create-react-library/) a déjà une [fonctionnalité](https://github.com/transitive-bullshit/create-react-library/#deploying-to-github-pages) grâce à laquelle nous pouvons déployer le [dossier example](https://github.com/ghoshnirmalya/react-search-box/tree/master/example) sur Github Pages. Vous devez simplement exécuter la commande suivante :

```
yarn deploy
```

Maintenant, vous pouvez voir votre application disponible à l'adresse `https://votre-nom-dutilisateur.github.io/nom-de-votre-depot/`. Pour moi, c'est [https://ghoshnirmalya.github.io/react-search-box](https://ghoshnirmalya.github.io/react-search-box/) puisque l'URL de mon dépôt est [https://github.com/ghoshnirmalya/react-search-box](https://github.com/ghoshnirmalya/react-search-box).

![Image](https://cdn-media-1.freecodecamp.org/images/yd7TW2zIls4qOwuJDJgIoY1Xix13gq7ygVqn)
_Application de démonstration sur [https://ghoshnirmalya.github.io/react-search-box](https://ghoshnirmalya.github.io/react-search-box/" rel="noopener" target="_blank" title=")_

## Remarques finales

Une dernière chose que vous devez retenir est que j'ai apporté un tas de modifications à [React Search Box](https://github.com/ghoshnirmalya/react-search-box) en plus des modifications que j'ai mentionnées ici. Je voulais simplement créer un plugin React d'autocomplétion simple et j'ai pensé que mes apprentissages pourraient aider les autres qui veulent contribuer à React mais ne savent pas par où commencer.

J'espère que cet article aidera les autres. Je suis curieux de savoir quels grands plugins vous allez construire avec l'aide de cet article. Faites-le moi savoir dans les commentaires ci-dessous.