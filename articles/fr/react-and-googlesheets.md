---
title: Comment transformer Google Sheets en une API REST et l'utiliser avec une application
  React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-18T16:15:14.000Z'
originalURL: https://freecodecamp.org/news/react-and-googlesheets
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--28-.png
tags:
- name: google sheets
  slug: google-sheets
- name: React
  slug: react
- name: REST API
  slug: rest-api
- name: spreadsheets
  slug: spreadsheets
seo_title: Comment transformer Google Sheets en une API REST et l'utiliser avec une
  application React
seo_desc: 'By Nishant Kumar

  Posting data to API''s has never been easy. But have you ever used React to post
  form data to Google Sheets? If not, then this tutorial is for you.

  Today, we are going to talk about how to POST form data from React to Google Sheets
  li...'
---

Par Nishant Kumar

Publier des données sur des API n'a jamais été facile. Mais avez-vous déjà utilisé React pour publier des données de formulaire vers Google Sheets ? Si ce n'est pas le cas, alors ce tutoriel est fait pour vous.

Aujourd'hui, nous allons parler de la manière de publier des données de formulaire depuis React vers Google Sheets comme des API REST.

## Tout d'abord, créez votre application React.

Pour commencer, vous pouvez utiliser create-react-app pour configurer votre application React.

Tapez simplement `npx create-react-app react-googlesheets` pour configurer le répertoire du projet.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-15-01-00-55.png)
_La structure des dossiers_

## Comment installer Semantic UI

Semantic UI est un framework utilisé pour concevoir et développer des mises en page belles et réactives. Il dispose de composants pour les boutons, les conteneurs, les listes, les entrées et bien plus encore.

Pour installer Semantic UI dans votre application React, utilisez la commande suivante :

```bash
npm install semantic-ui-react semantic-ui-css
```

Après l'installation, ouvrez le fichier index.js et importez ce qui suit en haut :

```bash
import 'semantic-ui-css/semantic.min.css'
```

Maintenant, exécutez l'application en utilisant la commande **`npm start`**.

## Créons quelques champs de saisie

Créons un formulaire et des champs de saisie pour obtenir nos entrées comme le nom, l'âge, le salaire et les hobbies depuis notre application React.

Ici, nous importons les boutons, le formulaire, le conteneur et l'en-tête de la bibliothèque _semantic-ui-react_ et créons des champs de formulaire.

```react
import React, { Component } from 'react'
import { Button, Form, Container, Header } from 'semantic-ui-react'
import './App.css';

export default class App extends Component {
  render() {
    return (
      <Container fluid className="container">
        <Header as='h2'>React Google Sheets !</Header>
        <Form className="form">
          <Form.Field>
            <label>Nom</label>
            <input placeholder='Entrez votre nom' />
          </Form.Field>
          <Form.Field>
            <label>Âge</label>
            <input placeholder='Entrez votre âge' />
          </Form.Field>
          <Form.Field>
            <label>Salaire</label>
            <input placeholder='Entrez votre salaire' />
          </Form.Field>
          <Form.Field>
            <label>Hobby</label>
            <input placeholder='Entrez votre hobby' />
          </Form.Field>
          
          <Button color="blue" type='submit'>Soumettre</Button>
        </Form>
      </Container>
    )
  }
}

```

```css
.form{
  width: 500px;
}

.container{
  padding:20px
}
```

Voici à quoi cela ressemblera :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-15-01-23-55-1.png)
_Formulaire de sortie_

Maintenant, nous avons terminé avec l'interface utilisateur. Ajoutons quelques fonctionnalités.

Tout d'abord, créons des états pour nos quatre champs de formulaire dans le constructeur.

```react
import React, { Component } from 'react'
import { Button, Form, Container, Header } from 'semantic-ui-react'
import './App.css';

export default class App extends Component {
  constructor(props) {
    super(props)
  
    this.state = {
       name: '',
       age: '',
       salary: '',
       hobby: ''
    }
  }

  changeHandler = (e) => {
    this.setState({[e.target.name] : e.target.value})
  }

  submitHandler = e => {
    e.preventDefault();
    console.log(this.state);
  }
  
  render() {
    const { name, age, salary, hobby } = this.state;    (*)
    return (
      <Container fluid className="container">
        <Header as='h2'>React Google Sheets !</Header>
        <Form className="form" onSubmit={this.submitHandler}>
          <Form.Field>
            <label>Nom</label>
            <input placeholder='Entrez votre nom' type="text" name = "name" value = {name} onChange={this.changeHandler}/>
          </Form.Field>
          <Form.Field>
            <label>Âge</label>
            <input placeholder='Entrez votre âge' type="number" name = "age" value = {age} onChange={this.changeHandler}/>
          </Form.Field>
          <Form.Field>
            <label>Salaire</label>
            <input placeholder='Entrez votre salaire' type="number" name = "salary" value = {salary} onChange={this.changeHandler}/>
          </Form.Field>
          <Form.Field>
            <label>Hobby</label>
            <input placeholder='Entrez votre hobby' type="text" name = "hobby" value = {hobby} onChange={this.changeHandler}/>
          </Form.Field>
          
          <Button color="blue" type='submit'>Soumettre</Button>
        </Form>
      </Container>
    )
  }
}

```

Ici, nous avons quatre champs de formulaire et leurs états respectifs. Nous avons également une méthode changeHandler pour suivre les changements dans les valeurs de saisie.

Déstructurons les états dans la méthode render et ajoutons leurs valeurs dans l'attribut value des entrées (ligne *).

La dernière chose dont nous avons besoin est un gestionnaire onSubmit. Sur la balise form, ajoutez l'événement onSubmit et attribuez la méthode submitHandler.

Remplissez le formulaire et cliquez sur soumettre. Vous verrez les données saisies dans la console.

Et c'est tout — nous avons un formulaire qui prend le nom, l'âge, le salaire et le hobby et les enregistre dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-15-02-13-09.png)

## Comment publier les données vers Google Sheets

Transformons notre Google Sheets en une API REST.

Nous allons publier des données vers Google Sheets comme une API REST, et pour cela, nous devons installer Axios. C'est une bibliothèque que vous pouvez utiliser pour envoyer des requêtes à des API, tout comme _fetch_.

Ouvrez une nouvelle feuille de calcul en cliquant sur Fichier, puis Nouveau, puis Feuille de calcul.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-15-02-24-46.png)

Nommez la feuille avec le nom de votre choix et enregistrez.

Cliquez sur le bouton de partage en haut à droite de votre écran, et modifiez la permission en public.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-15-02-27-45.png)

Copiez le lien et allez sur [https://sheet.best/](https://sheet.best/) et créez votre compte gratuit.

Créez une nouvelle connexion et collez votre URL copiée depuis Google Sheets dans la boîte de connexion URL.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-15-02-30-51.png)

Cliquez sur connecter. Vous serez redirigé vers votre page de connexions. Ici, vous pouvez voir toutes vos connexions. Cliquez sur les détails de votre nouvelle connexion.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-15-02-33-25.png)

Copiez l'URL de connexion. Cette URL sera utilisée comme point de terminaison pour envoyer des requêtes POST.

Maintenant, installons Axios. Tapez `npm install axios` dans votre terminal pour installer le package.

Après l'installation, importez-le en haut de votre fichier. Nous allons faire la requête POST dans la fonction submitHandler.

```react
submitHandler = e => {
    e.preventDefault();
    console.log(this.state);

    axios.post('url', this.state)
    .then(response => {
      console.log(response);
    })
  }
```

Remplacez la fonction submitHandler par le code ci-dessus. Ici, nous utilisons Axios pour publier les données vers l'URL et obtenir la réponse dans la console en utilisant le mot-clé **.then**.

Collez l'URL de connexion copiée depuis **sheet.best** et remplacez-la par l'URL dans axios.post('url').

```react
submitHandler = e => {
    e.preventDefault();
    console.log(this.state);

    axios.post('https://sheet.best/api/sheets/a6e67deb-2f00-43c3-89d3-b331341d53ed', this.state)
    .then(response => {
      console.log(response);
    })
  }
```

Maintenant, ouvrez Google Sheets et remplissez les premières colonnes, c'est-à-dire nom, âge, salaire et hobby. Veuillez les remplir soigneusement, sinon cela ne fonctionnera pas. Cela doit être sensible à la casse.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-15-02-43-12.png)
_Ajoutez les champs nom, âge, salaire et hobby_

Maintenant, exécutez votre application React et remplissez les champs de saisie. Vous verrez que les données sont peuplées dans votre Google Sheets une par une.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-18-14-03-16.png)
_Formulaire React_

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-15-02-45-27.png)
_Champs d'exemple_

C'est tout, les amis. Maintenant, vous savez comment transformer Google Sheets en une API REST. Maintenant, vous pouvez stocker vos données dans Google Sheets avec une application React.

Alternativement, vous pouvez [trouver le code sur Github](https://github.com/nishant-666/React-GoogleSheets) pour expérimenter.

Vous pouvez également [regarder ce tutoriel sur ma chaîne YouTube](https://youtu.be/5Vp4RVLNo3c) si vous le souhaitez.

> _Bon apprentissage._