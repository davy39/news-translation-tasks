---
title: Comment utiliser les entrées contrôlées de React pour une validation instantanée
  des champs de formulaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-12T04:35:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-reacts-controlled-inputs-for-instant-form-field-validation-b1c7b033527e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*srCOOERJDBSNxm81z1mTBw.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les entrées contrôlées de React pour une validation instantanée
  des champs de formulaire
seo_desc: 'By Gosha Arinich

  Controlled inputs enable simple things, like disabling the Submit button when some
  fields are missing or invalid.

  But we’re not stopping there, of course.

  While a disabled button is nice, the user might not know why they can’t click ...'
---

Par Gosha Arinich

[Les entrées contrôlées](https://goshakkk.name/controlled-vs-uncontrolled-inputs-react/) permettent des choses simples, comme [désactiver le bouton Submit](https://goshakkk.name/form-recipe-disable-submit-button-react/) lorsque certains champs sont manquants ou invalides.

Mais nous ne nous arrêtons pas là, bien sûr.

Bien qu'un bouton désactivé soit bien, l'utilisateur ne sait peut-être pas pourquoi il ne peut pas cliquer sur ce bouton. Il ne sait peut-être pas quelle erreur il a commise qui l'a désactivé ou même quel champ en est la cause.

Et ce n'est pas joli. Nous devons absolument corriger cela.

### Les bases des entrées contrôlées

L'utilisation d'entrées contrôlées implique que nous stockons toutes les valeurs des entrées dans notre état. Nous pouvons ensuite évaluer une condition particulière à chaque changement de valeur, et faire quelque chose en fonction de celle-ci. Auparavant, tout ce que nous faisions était de désactiver le bouton.

![Image](https://cdn-media-1.freecodecamp.org/images/0*bQAjIj-YA2Lqonmw.png)

Nous avons utilisé une expression simple pour calculer si le bouton devait être désactivé (par exemple, lorsque le champ email ou mot de passe était vide) :

```
const { email, password } = this.state;const isEnabled =  email.length > 0 &&  password.length > 0;
```

```
<button disabled={!isEnabled}>Sign up</button>
```

Cela a fait le travail. Maintenant, pour marquer les mauvaises entrées, nous devons nous poser quelques questions.

### Comment les erreurs seront-elles affichées ?

C'est une question importante à se poser, car différentes exigences peuvent justifier différentes représentations d'erreurs.

Il existe de nombreuses façons d'afficher les erreurs de saisie. Par exemple, vous pourriez :

* Afficher un ❌

![Image](https://cdn-media-1.freecodecamp.org/images/0*GT0gLYLM8_ctEdq8.png)

* Marquer en rouge les entrées contenant des données incorrectes

![Image](https://cdn-media-1.freecodecamp.org/images/0*6iOVJGn0V8zSFfUl.png)

* Afficher les erreurs à côté des entrées pertinentes

![Image](https://cdn-media-1.freecodecamp.org/images/0*3velTmdOZkLfFERy.png)

* Afficher une liste d'erreurs en haut du formulaire
* Toute combinaison des éléments ci-dessus, ou autre chose !

![Image](https://cdn-media-1.freecodecamp.org/images/0*ij45gCEgGuaZ4FT-.png)

Laquelle devez-vous utiliser ? Eh bien, tout dépend de l'expérience que vous souhaitez offrir. Choisissez ce que vous voulez.

Pour les besoins de cet article, je vais utiliser la plus simple — marquer les mauvaises entrées en rouge, sans rien d'autre.

### Comment les erreurs seront-elles représentées ?

La façon dont vous souhaitez afficher les erreurs influence la manière dont vous pourriez les représenter.

Pour indiquer si une entrée particulière est valide, sans aucune information supplémentaire quant à la raison pour laquelle elle pourrait être invalide, quelque chose comme ceci suffira :

```
errors: {  name: false,  email: true,}
```

`false` signifie aucune erreur ou entièrement valide ; `true` signifie qu'un champ est invalide.

À l'avenir, si nous décidons que nous devons stocker la raison pour laquelle quelque chose était invalide, nous pouvons remplacer le vrai/faux par une chaîne contenant un message d'erreur.

### Mais comment cet objet d'erreur est-il créé ?

Maintenant que nous savons comment nous voulons afficher les erreurs ET savoir comment les représenter, il manque quelque chose de crucial.

Comment créer réellement des erreurs.

Ou, en d'autres termes : comment prenons-nous les entrées existantes, les validons et obtenons l'objet d'erreur dont nous avons besoin ?

Nous allons avoir besoin d'une **fonction de validation** pour cela. Elle acceptera les valeurs actuelles des champs et nous retournera l'objet `errors`.

Nous allons continuer avec l'exemple du formulaire d'inscription. Rappelez-vous que nous avions ceci :

```
const { email, password } = this.state;const isEnabled =  email.length > 0 &&  password.length > 0;
```

Nous pouvons, en fait, transformer cette logique en une fonction de validation qui aura :

* `email: true` si l'email est vide, et
* `password: true` si le mot de passe est vide

```
function validate(email, password) {  // true signifie invalide, donc nos conditions sont inversées  return {    email: email.length === 0,    password: password.length === 0,  };}
```

### La pièce manquante

Il reste une pièce du puzzle.

Nous avons une fonction de validation et nous savons comment nous voulons afficher les erreurs. Nous avons aussi un formulaire.

Il est maintenant temps de connecter les points.

**Étape 1 :** Exécuter le validateur dans `render`.

Il est inutile d'avoir la fonction `validate` si nous ne l'appelons jamais. Nous voulons valider les entrées à chaque fois (oui, à chaque fois) que le formulaire est réaffiché — peut-être qu'il y a un nouveau caractère dans l'entrée.

```
const errors = validate(this.state.email, this.state.password);
```

**Étape 2 :** Désactiver le bouton.

C'est simple. Le bouton doit être désactivé s'il y a des erreurs (c'est-à-dire si l'une des valeurs `errors` est `true`).

```
const isEnabled = !Object.keys(errors).some(x => errors[x]);
```

**Étape 3 :** Marquer les entrées comme erronées.

Cela peut être n'importe quoi. Dans notre cas, ajouter une classe `error` aux mauvaises entrées suffit.

```
<input  className={errors.email ? "error" : ""}  .../>
```

Nous pouvons également ajouter une règle CSS simple :

```
.error { border: 1px solid red; }
```

### Une dernière chose

Si vous regardez le JS Bin ci-dessus, vous remarquerez peut-être quelque chose d'étrange. Les champs sont marqués en rouge par défaut, car les champs vides sont invalides.

Mais nous n'avons même pas donné à l'utilisateur une chance de taper d'abord ! De plus, les champs sont rouges lorsqu'ils sont focalisés pour la première fois.

Ce n'est pas idéal pour l'UX.

Nous allons corriger cela en ajoutant la classe `error` si le champ a été focalisé au moins une fois mais a depuis été flouté. Cela garantit que la première fois qu'un utilisateur se concentre sur le champ, l'erreur n'apparaîtra pas immédiatement. Au lieu de cela, elle n'apparaîtra que lorsque le champ sera flouté. Lors des focalisations suivantes, cependant, l'erreur apparaîtrait.

Cela est facilement réalisable en utilisant l'événement `onBlur` et l'état pour suivre ce qui a été flouté.

```
class SignUpForm extends React.Component {  constructor() {    super();    this.state = {      email: '',      password: '',      touched: {        email: false,        password: false,      },    };  }
```

```
  // ...
```

```
  handleBlur = (field) => (evt) => {    this.setState({      touched: { ...this.state.touched, [field]: true },    });  }
```

```
  render()    const shouldMarkError = (field) => {      const hasError = errors[field];      const shouldShow = this.state.touched[field];
```

```
      return hasError ? shouldShow : false;    };
```

```
    // ...
```

```
    <input      className={shouldMarkError('email') ? "error" : ""}      onBlur={this.handleBlur('email')}
```

```
      type="text"      placeholder="Enter email"      value={this.state.email}      onChange={this.handleEmailChange}    />  }}
```

Pas si difficile, n'est-ce pas ?

### Dernières retouches

Notez que `shouldMarkError` n'affecte que la présentation du champ. L'état du bouton de soumission dépend toujours uniquement des erreurs de `validation`.

Vous voulez ajouter une belle touche finale ? Vous pourriez forcer l'affichage des erreurs dans tous les champs, indépendamment du fait qu'ils aient été focalisés ou non, lorsque l'utilisateur survole ou clique sur un bouton de soumission désactivé. Maintenant, allez essayer par vous-même.

J'ai initialement publié cela sur mon blog à l'adresse [goshakkk.name](https://goshakkk.name/instant-form-fields-validation-react/)

Si vous aimez cela, donnez-moi quelques applaudissements et consultez [ma série sur la gestion des formulaires avec React](http://goshakkk.name/on-forms-react/). Vous pouvez également [vous abonner](http://goshakkk.name/subscribe/) pour recevoir les nouveaux articles directement dans votre boîte de réception.