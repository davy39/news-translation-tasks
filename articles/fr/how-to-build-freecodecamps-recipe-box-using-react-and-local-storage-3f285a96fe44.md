---
title: Comment construire la boîte à recettes de freeCodeCamp en utilisant React et
  le stockage local
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-15T20:28:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-freecodecamps-recipe-box-using-react-and-local-storage-3f285a96fe44
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4_uAp5H4Mm_w7RWz5Ivdfg.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment construire la boîte à recettes de freeCodeCamp en utilisant React
  et le stockage local
seo_desc: 'By Edward Njoroge

  I completed my first edition of the Free Code Camp recipe box project on May 3,
  2018. I put it up here for review. Then I didn’t check the reviews for a few weeks.
  When I returned, I was shocked to learn that I had overlooked an imp...'
---

Par Edward Njoroge

J'ai terminé ma première édition du projet de boîte à recettes de Free Code Camp le 3 mai 2018. Je l'ai mise en ligne [ici](https://forum.freecodecamp.org/t/check-out-my-recipe-box/177769/2) pour révision. Ensuite, je n'ai pas vérifié les avis pendant quelques semaines. À mon retour, j'ai été choqué d'apprendre que j'avais négligé une fonctionnalité importante dans les formulaires.

![Image](https://cdn-media-1.freecodecamp.org/images/GlNVp3au86v0MmkdMc-Qv-GH9KnVI88LeNFo)

Je sais. Terrible erreur. Mon formulaire permettait la création d'une recette vide. Cette négligence montre l'importance de permettre à d'autres personnes de réviser votre code.

Il s'avère que je n'étais pas le seul à avoir manqué cette fonctionnalité importante. J'ai vérifié le projet d'exemple de freeCodeCamp pour la boîte à recettes ([ici](https://codepen.io/FreeCodeCamp/full/xVXWag/)) et il manquait la même fonctionnalité. La validation n'est pas mentionnée dans les histoires utilisateur ([ici](https://www.freecodecamp.org/challenges/build-a-recipe-box)) non plus.

J'ai pensé que si j'incluais la validation dans mon projet, je pourrais essayer de convaincre freeCodeCamp de faire de ma boîte à recettes le projet d'exemple pour ce défi. J'ai donc redémarré le projet, et pendant ce processus, je me suis inspiré pour écrire cet article Medium.

### Construction de la boîte à recettes

Pour ce projet, nous utiliserons create-react-app, React bootstrap, et bootstrap CSS.

#### Étape 1 : Configurer l'environnement React et ajouter React bootstrap.

```
npx create-react-app recipe-box
npm install react-bootstrap --save
```

Nous allons créer une structure de fichiers qui ressemble à celle ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/66AzutgiMLsdMyNrX8WS7xaM-Q6XfL2RQZpb)

Nous supprimons favicon.ico et manifest.json du dossier public, et tout sauf index.js et index.css du dossier src. À l'intérieur du dossier SRC, créez un dossier components et un dossier CSS. Déplacez index.css dans le dossier CSS.

#### _Étape 2 : Configurer le html dans index.html._

Dans index.html :

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <title>Boîte à Recettes</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Ceci est un projet Free Code Camp appelé Boîte à Recettes">
    <meta name="keywords" content="HTML, CSS, JAVASCRIPT, REACTJS">
    <meta name="author" content="Votre Nom">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css?family=Mina" rel="stylesheet">
  </head>
  <body>
    <!--configurer une div où tout le code sera rendu-->
    <div class="container" id="app"></div>
  </body>
</html>
```

#### _Étape 3 : Configurer la première vue de la boîte à recettes._

Dans index.js, nous créons une liste initiale de recettes dans this.state et les affichons.

Dans index.js :

```js
//importer les fichiers nécessaires
import React from 'react';
import ReactDOM from 'react-dom';
import {PanelGroup,Panel,Button,ButtonToolbar,ListGroup,ListGroupItem} from 'react-bootstrap';
import './css/index.css';
//créer la classe principale pour afficher les recettes
class Recipe extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recipes: [
        {name: "Smoothie à la banane", ingredients: ["2 bananes", "1/2 tasse de yaourt à la vanille", "1/2 tasse de lait écrémé", "2 cuillères à café de miel", "une pincée de cannelle"]},
        {name: "Spaghetti", ingredients: ["Nouilles", "Sauce tomate", "Boulettes de viande"]},
        {name: "Soupe aux pois cassés", ingredients: ["1 livre de pois cassés", "1 oignon", "6 carottes", "4 onces de jambon"]}
      ]
    };
  }
  render() {
    const recipes = this.state.recipes;
    return(
      <div className="jumbotron">
        <h1>BOÎTE À RECETTES</h1>
        <PanelGroup accordion id="recipes">
          {recipes.map((recipe, index) => (
            <Panel eventKey={index} key={index}>
              <Panel.Heading>
                <Panel.Title className="title" toggle>{recipe.name}</Panel.Title>
              </Panel.Heading>
              <Panel.Body collapsible>
                <ListGroup>
                  {recipe.ingredients.map((ingredient, index) => (
                    <ListGroupItem key={index}>{ingredient}</ListGroupItem>
                  ))}
                </ListGroup>
                <ButtonToolbar>
                  <Button bsStyle="warning">Modifier</Button>
                  <Button bsStyle="danger">Supprimer</Button>
                </ButtonToolbar>
              </Panel.Body>
            </Panel>
          ))}
        </PanelGroup>
        <Button bsStyle="primary">Ajouter une Recette</Button>
      </div>
    );
  }
};

ReactDOM.render(<Recipe />, document.getElementById('app'));
```

Dans index.css :

```css
h1, li, .title {
  font-family: 'Mina';
}
h1, li {
  text-align: center;
}
.title {
  background-color: #D8BFD8;
  font-size: 20px;
}
li {
  list-style-type: none;
  font-size: 18px;
}
```

Résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/9wFXTAqnvx1TmKw-iuixpJkXOQTcpF-8xOLg)
_La boîte à recettes._

![Image](https://cdn-media-1.freecodecamp.org/images/KZ5eebS0feoWVzNArylgcBvs9IeO0McXWamW)
_La vue d'une recette lorsque son nom est cliqué._

#### _Étape 4 : Créer la fonction Ajouter une Recette._

Nous sommes maintenant prêts à ajouter des recettes. Nous créons un fichier appelé addrecipe.js à l'intérieur du dossier components.

Les recettes seront ajoutées via un formulaire modal. Nous devons d'abord pouvoir activer et désactiver le modal. Nous créons un état appelé showAdd et le définissons sur false. Ensuite, nous créons une fonction appelée showAddModal() qui change showAdd en true si elle est actuellement false et vice versa.

Lorsque le bouton "Ajouter une Recette" est cliqué, showAdd passera à true et le modal sera affiché. Par conséquent, showAdd et showAddModal() doivent être passés en tant que props à addrecipe.js.

Pour ajouter une recette, une fonction addRecipe() qui prend l'argument 'recipe' sera créée. Elle prend les détails de la nouvelle recette et les ajoute à la fin du tableau d'état des recettes. Cette fonction sera également passée en tant que prop à addrecipe.js.

Dans index.js :

```js
//importer les fichiers nécessaires
import React from 'react';
import ReactDOM from 'react-dom';
import {PanelGroup,Panel,Button,ButtonToolbar,ListGroup,ListGroupItem} from 'react-bootstrap';
import {AddRecipe} from './components/addrecipe';
import './css/index.css';
//créer la classe principale pour afficher les recettes
class Recipe extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recipes: [
        {name: "Smoothie à la banane", ingredients: ["2 bananes", "1/2 tasse de yaourt à la vanille", "1/2 tasse de lait écrémé", "2 cuillères à café de miel", "une pincée de cannelle"]},
        {name: "Spaghetti", ingredients: ["Nouilles", "Sauce tomate", "Boulettes de viande"]},
        {name: "Soupe aux pois cassés", ingredients: ["1 livre de pois cassés", "1 oignon", "6 carottes", "4 onces de jambon"]}
      ],
      showAdd: false
    };
    this.showAddModal = this.showAddModal.bind(this);
    this.addRecipe = this.addRecipe.bind(this);
  }
  showAddModal() {//afficher le modal de nouvelle recette
    this.setState({showAdd: !this.state.showAdd});
  }
  addRecipe(recipe) {//créer une nouvelle recette
    let recipes = this.state.recipes;
    recipes.push(recipe);
    this.setState({recipes: recipes});
    this.showAddModal();
  }
  render() {
    const recipes = this.state.recipes;
    return(
      <div className="jumbotron">
        <h1>BOÎTE À RECETTES</h1>
        <PanelGroup accordion id="recipes">
          {recipes.map((recipe, index) => (
            <Panel eventKey={index} key={index}>
              <Panel.Heading>
                <Panel.Title className="title" toggle>{recipe.name}</Panel.Title>
              </Panel.Heading>
              <Panel.Body collapsible>
                <ListGroup>
                  {recipe.ingredients.map((ingredient, index) => (
                    <ListGroupItem key={index}>{ingredient}</ListGroupItem>
                  ))}
                </ListGroup>
                <ButtonToolbar>
                  <Button bsStyle="warning">Modifier</Button>
                  <Button bsStyle="danger">Supprimer</Button>
                </ButtonToolbar>
              </Panel.Body>
            </Panel>
          ))}
        </PanelGroup>
        <Button bsStyle="primary" onClick={this.showAddModal}>Ajouter une Recette</Button>
        <AddRecipe onShow={this.state.showAdd} onAdd={this.addRecipe} onAddModal={this.showAddModal} />
      </div>
    );
  }
};

ReactDOM.render(<Recipe />, document.getElementById('app'));
```

```
ReactDOM.render(<Recipe />, document.getElementById('app'));
```

Dans addrecipe.js, nous créons un état qui contient le nom de la nouvelle recette et les ingrédients de la recette, et les valeurs initiales sont des chaînes vides. Nous allons ensuite changer l'état chaque fois que nous changeons le contenu du formulaire comme nous le ferions dans un markdown. Cela rendra la validation du formulaire plus facile.

Au lieu d'afficher des erreurs de formulaire pour la validation, nous utilisons des expressions régulières pour nous assurer que nous sauvegardons une recette uniquement si certaines conditions sont remplies. Ces conditions sont :

(a) Les sections nom de la recette et ingrédients ne doivent pas être vides, c'est-à-dire que les deux doivent avoir au moins un caractère.

(b) Le nom de la recette du formulaire ne peut pas commencer par un espace. Cela garantit que le nom de la recette commence par au moins un caractère alphanumérique ou un symbole.

(c) Les ingrédients de la recette du formulaire ne peuvent pas commencer ou se terminer par un espace ou une virgule. Cela est dû au fait que les ingrédients seront divisés par des virgules en un tableau qui est ensuite affiché sous forme de liste comme nos ingrédients actuels.

Le modal aura un bouton Sauvegarder la Recette qui sera désactivé jusqu'à ce que toutes les conditions soient remplies. Lorsque sauvegarder la recette est cliqué, la recette sera ajoutée à notre boîte à recettes.

Dans addrecipe.js :

```js
//importer les fichiers nécessaires
import React from 'react';
import {Modal,ControlLabel,FormGroup,FormControl,Button} from 'react-bootstrap';

//créer une classe pour afficher le modal pour ajouter une nouvelle recette et l'exporter
export class AddRecipe extends React.Component {
  constructor(props) {//créer un état pour gérer la nouvelle recette
    super(props);
    this.state = {name: "", ingredients: ""};
    this.handleRecipeNameChange = this.handleRecipeNameChange.bind(this);
    this.handleRecipeIngredientsChange = this.handleRecipeIngredientsChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleCancel = this.handleCancel.bind(this);
  }
  handleRecipeNameChange(e) {//changer le nom pour refléter l'entrée de l'utilisateur
    this.setState({name: e.target.value});
  }
  handleRecipeIngredientsChange(e) {//changer les ingrédients pour refléter l'entrée de l'utilisateur
    this.setState({ingredients: e.target.value});
  }
  handleSubmit(e) {//obtenir les données de la recette, les manipuler et appeler la fonction pour créer une nouvelle recette
    e.preventDefault();
    const onAdd = this.props.onAdd;
    const regExp = /\s*,\s*/;
    var newName = this.state.name;
    var newIngredients = this.state.ingredients.split(regExp);
    var newRecipe = {name: newName, ingredients: newIngredients};
    onAdd(newRecipe);
    this.setState({name: "", ingredients: ""});
  }
  handleCancel() {
    const onAddModal = this.props.onAddModal;
    this.setState({name: "", ingredients: ""});
    onAddModal();
  }
  render() {
    const onShow = this.props.onShow;
    var regex1 = /^\S/;
    var regex2 = /^[^,\s]/;
   var regex3 = /[^,\s]$/;
    const validRecipe = regex1.test(this.state.name) && regex2.test(this.state.ingredients) && regex3.test(this.state.ingredients);
    return(
      <Modal show={onShow} onHide={this.handleCancel}>
        <Modal.Header closeButton>
          <Modal.Title>Nouvelle Recette</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <FormGroup controlId="formControlsName">
            <ControlLabel>Nom de la Recette</ControlLabel>
            <FormControl type="text" required onChange={this.handleRecipeNameChange} value={this.state.name} placeholder="Entrez le Nom" />
          </FormGroup>
          <FormGroup controlId="formControlsIngredients">
            <ControlLabel>Ingrédients de la Recette</ControlLabel>
            <FormControl componentClass="textarea" type="text" required onChange={this.handleRecipeIngredientsChange} value={this.state.ingredients} placeholder="Entrez les Ingrédients(séparés par des virgules)" />
          </FormGroup>
        </Modal.Body>
        <Modal.Footer>
          <Button disabled={!validRecipe} bsStyle="success" onClick={this.handleSubmit}>Sauvegarder la Recette</Button>
        </Modal.Footer>
      </Modal>
    );
  }
};
```

Résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/jgKE3gUIcIhXzZw7gs16UsCITbITL2yOGOwL)
_La boîte à recettes._

![Image](https://cdn-media-1.freecodecamp.org/images/s8CjbxJM64MQnbMslBEuNxS84WmwYjgIHv9w)
_Le modal vide qui apparaît une fois le bouton "Ajouter une Recette" cliqué._

![Image](https://cdn-media-1.freecodecamp.org/images/Nj5Z7vJI5oMPU3nsBL1sGXW0vWZ03ct6auHB)
_Remplir le formulaire et le soumettre._

![Image](https://cdn-media-1.freecodecamp.org/images/LRrbrD97cXmmE31wXH0YzK1CtlWCeHge5bE6)
_La boîte à recettes mise à jour._

![Image](https://cdn-media-1.freecodecamp.org/images/rKYCMp4sQw9tkgzYBcdZ-v0DdnHMekSs4mAz)
_La vue de la nouvelle recette lorsque son nom est cliqué._

#### _Étape 5 : Créer la fonction Modifier la Recette._

Nous sommes maintenant prêts à modifier les recettes. Nous créons un fichier appelé editrecipe.js à l'intérieur du dossier components.

Les recettes seront modifiées via un formulaire modal. Nous devons d'abord pouvoir activer et désactiver le modal. Nous créons un état appelé showEdit et le définissons sur false. Ensuite, nous créons une fonction appelée showEditModal() qui change showEdit en true si elle est actuellement false et vice versa. Lorsque le bouton "Modifier" est cliqué, showEditModal() s'exécutera, showEdit passera à true, et le modal sera affiché.

Nous aurons également besoin d'un moyen de nous assurer que la recette correcte est affichée dans les champs du formulaire pour la modification. Nous créons un état appelé currentlyEditing et le définissons sur 0. Nous nous assurons ensuite que les détails de this.state.recipes[currentlyEditing] sont affichés dans le formulaire.

Puisque 0 est la valeur par défaut, chaque fois que Modifier la Recette est cliqué, le formulaire n'affichera que les détails de la première recette. Nous avons besoin d'un moyen de mettre à jour currentlyEditing à l'index de la recette que nous voulons afficher.

Dans showEditModal(), nous passons index comme argument et cet argument sera égal à l'index de la recette actuelle. Maintenant, lorsque le bouton "Modifier la Recette" est cliqué, showEditModal() s'exécutera, showEdit passera à true, currentlyEditing deviendra l'index de la recette, et le modal sera affiché avec les informations correctes de la recette. Par conséquent, showEdit et showEditModal(index) doivent être passés en tant que props à editrecipe.js.

Pour modifier une recette, une fonction editRecipe() qui prend les arguments newName, newIngredients, et currentlyEditing sera créée. Dans cette fonction, nous utilisons currentlyEditing (qui est maintenant l'index de la recette que nous modifions) pour identifier cette recette et définir son nom à newName et ses ingrédients à newIngredients. Par conséquent, editRecipe, la recette que nous devons modifier, et currentlyEditing doivent être passés en tant que props à editrecipe.js.

Dans index.js :

```js
//importer les fichiers nécessaires
import React from 'react';
import ReactDOM from 'react-dom';
import {PanelGroup,Panel,Button,ButtonToolbar,ListGroup,ListGroupItem} from 'react-bootstrap';
import {AddRecipe} from './components/addrecipe';
import {EditRecipe} from './components/editrecipe';
import './css/index.css';
//créer la classe principale pour afficher les recettes
class Recipe extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recipes: [
        {name: "Smoothie à la banane", ingredients: ["2 bananes", "1/2 tasse de yaourt à la vanille", "1/2 tasse de lait écrémé", "2 cuillères à café de miel", "une pincée de cannelle"]},
        {name: "Spaghetti", ingredients: ["Nouilles", "Sauce tomate", "Boulettes de viande"]},
        {name: "Soupe aux pois cassés", ingredients: ["1 livre de pois cassés", "1 oignon", "6 carottes", "4 onces de jambon"]}
      ],
      showAdd: false,
      showEdit: false,
      currentlyEditing: 0
    };
    this.showAddModal = this.showAddModal.bind(this);
    this.showEditModal = this.showEditModal.bind(this);
    this.addRecipe = this.addRecipe.bind(this);
    this.editRecipe = this.editRecipe.bind(this);
  }
  showAddModal() {//afficher le modal de nouvelle recette
    this.setState({showAdd: !this.state.showAdd});
  }
  showEditModal(index) {//afficher le modal de modification de recette
    this.setState({showEdit: !this.state.showEdit, currentlyEditing: index});
  }
  addRecipe(recipe) {//créer une nouvelle recette
    let recipes = this.state.recipes;
    recipes.push(recipe);
    this.setState({recipes: recipes});
    this.showAddModal();
  }
  editRecipe(newName, newIngredients, currentlyEditing) {//modifier une recette existante
    let recipes = this.state.recipes;
    recipes[currentlyEditing] = {name: newName, ingredients: newIngredients};
    this.setState({recipes: recipes});
    this.showEditModal(currentlyEditing);
  }
  render() {
    const recipes = this.state.recipes;
    return(
      <div className="jumbotron">
        <h1>BOÎTE À RECETTES</h1>
        <PanelGroup accordion id="recipes">
          {recipes.map((recipe, index) => (
            <Panel eventKey={index} key={index}>
              <Panel.Heading>
                <Panel.Title className="title" toggle>{recipe.name}</Panel.Title>
              </Panel.Heading>
              <Panel.Body collapsible>
                <ListGroup>
                  {recipe.ingredients.map((ingredient, index) => (
                    <ListGroupItem key={index}>{ingredient}</ListGroupItem>
                  ))}
                </ListGroup>
                <ButtonToolbar>
                  <Button bsStyle="warning" onClick={() => {this.showEditModal(index)}}>Modifier</Button>
                  <Button bsStyle="danger">Supprimer</Button>
                </ButtonToolbar>
              </Panel.Body>
              <EditRecipe onShow={this.state.showEdit} onEdit={this.editRecipe} onEditModal={() => {this.showEditModal(this.state.currentlyEditing)}} currentlyEditing={this.state.currentlyEditing} recipe={recipes[this.state.currentlyEditing]} />
            </Panel>
          ))}
        </PanelGroup>
        <Button bsStyle="primary" onClick={this.showAddModal}>Ajouter une Recette</Button>
        <AddRecipe onShow={this.state.showAdd} onAdd={this.addRecipe} onAddModal={this.showAddModal} />
      </div>
    );
  }
};

ReactDOM.render(<Recipe />, document.getElementById('app'));
ReactDOM.render(<Recipe />, document.getElementById('app'));
```

Dans editrecipe.js :

```js
//importer les fichiers nécessaires
import React from 'react';
import {Modal,ControlLabel,FormGroup,FormControl,Button} from 'react-bootstrap';

//créer une classe pour afficher le modal pour modifier une recette existante et l'exporter
export class EditRecipe extends React.Component {
  constructor(props) {//créer un état pour gérer la recette à modifier
    super(props);
    this.state = {name: "", ingredients: ""};
    this.handleRecipeNameChange = this.handleRecipeNameChange.bind(this);
    this.handleRecipeIngredientsChange = this.handleRecipeIngredientsChange.bind(this);
    this.handleEdit = this.handleEdit.bind(this);
    this.handleCancel = this.handleCancel.bind(this);
  }
  static getDerivedStateFromProps(props, state) {//faire de la prop recette un état
    const prevName = state.prevName;
    const prevIngredients = state.prevIngredients;
    const name = prevName !== props.recipe.name ? props.recipe.name : state.name;
    const ingredients = prevIngredients !== props.recipe.ingredients.join(",") ? props.recipe.ingredients.join(",") : state.ingredients;
    return {
      prevName: props.recipe.name, name,
      prevIngredients: props.recipe.ingredients.join(","), ingredients,
    }
  }
  handleRecipeNameChange(e) {//changer le nom pour refléter l'entrée de l'utilisateur
    this.setState({name: e.target.value});
  }
  handleRecipeIngredientsChange(e) {//changer les ingrédients pour refléter l'entrée de l'utilisateur
    this.setState({ingredients: e.target.value});
  }
  handleEdit(e) {//obtenir les données de la recette, les manipuler et appeler la fonction pour modifier une recette existante
    e.preventDefault();
    const onEdit = this.props.onEdit;
    const currentlyEditing = this.props.currentlyEditing;
    const regExp = /\s*,\s*/;
    var name = this.state.name;
    var ingredients = this.state.ingredients.split(regExp);
    onEdit(name, ingredients, currentlyEditing);
  }
  handleCancel() {
    const onEditModal = this.props.onEditModal;
    this.setState({name: this.props.recipe.name, ingredients: this.props.recipe.ingredients.join(",")});
    onEditModal();
  }
  render() {
    const onShow = this.props.onShow;
    var regex1 = /^\S/;
    var regex2 = /^[^,\s]/;
    var regex3 = /[^,\s]$/;
    const validRecipe = regex1.test(this.state.name) && regex2.test(this.state.ingredients) && regex3.test(this.state.ingredients);
    return(
      <Modal show={onShow} onHide={this.handleCancel}>
        <Modal.Header closeButton>
          <Modal.Title>Modifier la Recette</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <FormGroup controlId="formControlsName">
            <ControlLabel>Nom de la Recette</ControlLabel>
            <FormControl type="text" required onChange={this.handleRecipeNameChange} value={this.state.name} placeholder="Entrez le Nom" />
          </FormGroup>
          <FormGroup controlId="formControlsIngredients">
            <ControlLabel>Ingrédients de la Recette</ControlLabel>
            <FormControl componentClass="textarea" type="text" required onChange={this.handleRecipeIngredientsChange} value={this.state.ingredients} placeholder="Entrez les Ingrédients(séparés par des virgules)" />
          </FormGroup>
        </Modal.Body>
        <Modal.Footer>
          <Button disabled={!validRecipe} bsStyle="success" onClick={this.handleEdit}>Sauvegarder la Recette</Button>
        </Modal.Footer>
      </Modal>
    );
  }
};
```

Résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/xWn8sF69-fASP8b16qE2WGYfaESnlUSwq8N4)
_La boîte à recettes._

![Image](https://cdn-media-1.freecodecamp.org/images/CmLZh4BsZG64S5btNq6woPqCxkjvMTRyZbJ2)
_La vue d'une recette lorsque son nom est cliqué._

![Image](https://cdn-media-1.freecodecamp.org/images/XL8CPngL-wSYN34h0nmLwKmZSbeoLFWuejZw)
_La vue du modal de modification de la recette._

![Image](https://cdn-media-1.freecodecamp.org/images/xZWkhYopZy56DeL5t39i98uufYgSDa0-Gc2d)
_Les ingrédients ont été modifiés. "Huile" a été remplacé par "1 cuillère à soupe de sel"._

![Image](https://cdn-media-1.freecodecamp.org/images/DLa14Mwboe-WJTF-LeZzAQn2R7j3gLAcIuZM)
_La version modifiée de la recette._

Dans editRecipe.js, nous créons un état qui contient le nom et les ingrédients de la recette à modifier, et définissons les valeurs initiales comme des chaînes vides. Nous utilisons ensuite la nouvelle méthode de cycle de vie de React getDerivedStateFromProps pour faire du nom et des ingrédients de notre prop recette le nouveau nom et les nouveaux ingrédients de notre état. La méthode pour le faire est clairement expliquée [ici](https://reactjs.org/blog/2018/05/23/react-v-16-4.html#bugfix-for-getderivedstatefromprops).

Nous allons ensuite changer l'état chaque fois que nous changeons le contenu du formulaire et valider le formulaire comme nous l'avons fait lors de l'ajout d'une nouvelle recette.

#### _Étape 6 : Créer la fonction Supprimer la Recette._

Nous sommes maintenant prêts à supprimer des recettes. Cette étape ne nécessite pas la création d'un nouveau fichier.

Pour supprimer une recette, une fonction deleteRecipe() qui prend l'argument index sera créée. Dans cette fonction, nous utilisons l'index d'une recette pour identifier la recette à supprimer. Nous utiliserons la méthode splice de JavaScript pour supprimer la recette. Nous définissons ensuite currentlyEditing à 0 juste pour réinitialiser la boîte à recettes, c'est-à-dire que nous ne voulons pas que currentlyEditing soit encore l'index d'une recette qui n'existe plus.

Dans index.js :

```js
//importer les fichiers nécessaires
import React from 'react';
import ReactDOM from 'react-dom';
import {PanelGroup,Panel,Button,ButtonToolbar,ListGroup,ListGroupItem} from 'react-bootstrap';
import {AddRecipe} from './components/addrecipe';
import {EditRecipe} from './components/editrecipe';
import './css/index.css';
//créer la classe principale pour afficher les recettes
class Recipe extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recipes: [
        {name: "Smoothie à la banane", ingredients: ["2 bananes", "1/2 tasse de yaourt à la vanille", "1/2 tasse de lait écrémé", "2 cuillères à café de miel", "une pincée de cannelle"]},
        {name: "Spaghetti", ingredients: ["Nouilles", "Sauce tomate", "Boulettes de viande"]},
        {name: "Soupe aux pois cassés", ingredients: ["1 livre de pois cassés", "1 oignon", "6 carottes", "4 onces de jambon"]}
      ],
      showAdd: false,
      showEdit: false,
      currentlyEditing: 0
    };
    this.showAddModal = this.showAddModal.bind(this);
    this.showEditModal = this.showEditModal.bind(this);
    this.addRecipe = this.addRecipe.bind(this);
    this.editRecipe = this.editRecipe.bind(this);
    this.deleteRecipe = this.deleteRecipe.bind(this);
  }
  showAddModal() {//afficher le modal de nouvelle recette
    this.setState({showAdd: !this.state.showAdd});
  }
  showEditModal(index) {//afficher le modal de modification de recette
    this.setState({showEdit: !this.state.showEdit, currentlyEditing: index});
  }
  addRecipe(recipe) {//créer une nouvelle recette
    let recipes = this.state.recipes;
    recipes.push(recipe);
    this.setState({recipes: recipes});
    this.showAddModal();
  }
  editRecipe(newName, newIngredients, currentlyEditing) {//modifier une recette existante
    let recipes = this.state.recipes;
    recipes[currentlyEditing] = {name: newName, ingredients: newIngredients};
    this.setState({recipes: recipes});
    this.showEditModal(currentlyEditing);
  }
  deleteRecipe(index) {//supprimer une recette existante
    let recipes = this.state.recipes.slice();
    recipes.splice(index, 1);
    this.setState({recipes: recipes, currentlyEditing: 0});
  }
  render() {
    const recipes = this.state.recipes;
    return(
      <div className="jumbotron">
        <h1>BOÎTE À RECETTES</h1>
        <PanelGroup accordion id="recipes">
          {recipes.map((recipe, index) => (
            <Panel eventKey={index} key={index}>
              <Panel.Heading>
                <Panel.Title className="title" toggle>{recipe.name}</Panel.Title>
              </Panel.Heading>
              <Panel.Body collapsible>
                <ListGroup>
                  {recipe.ingredients.map((ingredient, index) => (
                    <ListGroupItem key={index}>{ingredient}</ListGroupItem>
                  ))}
                </ListGroup>
                <ButtonToolbar>
                  <Button bsStyle="warning" onClick={() => {this.showEditModal(index)}}>Modifier</Button>
                  <Button bsStyle="danger" onClick={() => {this.deleteRecipe(index)}}>Supprimer</Button>
                </ButtonToolbar>
              </Panel.Body>
              <EditRecipe onShow={this.state.showEdit} onEdit={this.editRecipe} onEditModal={() => {this.showEditModal(this.state.currentlyEditing)}} currentlyEditing={this.state.currentlyEditing} recipe={recipes[this.state.currentlyEditing]} />
            </Panel>
          ))}
        </PanelGroup>
        <Button bsStyle="primary" onClick={this.showAddModal}>Ajouter une Recette</Button>
        <AddRecipe onShow={this.state.showAdd} onAdd={this.addRecipe} onAddModal={this.showAddModal} />
      </div>
    );
  }
};

ReactDOM.render(<Recipe />, document.getElementById('app'));
```

Résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/280ZsOAYf4L1YHNsmumPhMS7Cx9NLskuWwM7)
_La boîte à recettes._

![Image](https://cdn-media-1.freecodecamp.org/images/NqLWTIFMqoGSewKoysUlOhWHJi4B9hDpeHV3)
_La boîte à recettes après la suppression de la recette "Chapati Kenyan"._

![Image](https://cdn-media-1.freecodecamp.org/images/T6k0Ddc9CgGJRH-UU7CVJOQc3LHKYEsqTOb4)
_La boîte à recettes mise à jour._

#### _Étape 7 : Ajout du Stockage Local._

Le stockage web HTML 5 permet aux applications web de stocker des données localement dans le navigateur de l'utilisateur. Il existe deux objets de stockage web :

(a) Stockage de Session : Le stockage de session stocke les données pour une session, et les données sont perdues lorsque l'onglet du navigateur est fermé.

(b) Stockage Local : Le stockage local stocke les données indéfiniment. Les données ne seront pas supprimées lorsque le navigateur est fermé, et seront disponibles tout le temps puisqu'il n'y a pas de date d'expiration.

Pour ajouter le stockage local, nous allons changer notre état de recette en un tableau vide. Nous allons d'abord obtenir les recettes du stockage local, puis définir notre état de recette à ces recettes. Nous allons utiliser la méthode de cycle de vie componentDidMount, car nous voulons charger le stockage local après que notre composant soit rendu. Nous mettrons également à jour le stockage local chaque fois que nous ajouterons, modifierons ou supprimerons une recette.

Ainsi, par exemple, si nous supprimons l'une de nos 3 recettes originales et rechargeons la page, nous ne verrons pas la recette que nous avons supprimée. Lorsque nous effaçons notre stockage local et rechargeons la page, nous verrons à nouveau la recette originale que nous avons supprimée.

Dans index.js :

```js
//importer les fichiers nécessaires
import React from 'react';
import ReactDOM from 'react-dom';
import {PanelGroup,Panel,Button,ButtonToolbar,ListGroup,ListGroupItem} from 'react-bootstrap';
import './css/index.css';
import {AddRecipe} from './components/addrecipe';
import {EditRecipe} from './components/editrecipe';
//créer la classe principale pour afficher les recettes
class Recipe extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recipes: [],
      showAdd: false,
      showEdit: false,
      currentlyEditing: 0
    };
    this.showAddModal = this.showAddModal.bind(this);
    this.showEditModal = this.showEditModal.bind(this);
    this.addRecipe = this.addRecipe.bind(this);
    this.editRecipe = this.editRecipe.bind(this);
    this.deleteRecipe = this.deleteRecipe.bind(this);
  }
  componentDidMount() {//charger les données du stockage local après que le composant soit rendu
    var recipes = (typeof localStorage["recipes"] !== "undefined") ? JSON.parse(localStorage.getItem("recipes")) : [
      {name: "Smoothie à la banane", ingredients: ["2 bananes", "1/2 tasse de yaourt à la vanille", "1/2 tasse de lait écrémé", "2 cuillères à café de miel", "une pincée de cannelle"]},
      {name: "Spaghetti", ingredients: ["Nouilles", "Sauce tomate", "Boulettes de viande"]},
      {name: "Soupe aux pois cassés", ingredients: ["1 livre de pois cassés", "1 oignon", "6 carottes", "4 onces de jambon"]}
    ];
    this.setState({recipes: recipes});
  }
  showAddModal() {//afficher le modal de nouvelle recette
    this.setState({showAdd: !this.state.showAdd});
  }
  showEditModal(index) {//afficher le modal de modification de recette
    this.setState({currentlyEditing: index, showEdit: !this.state.showEdit});
  }
  addRecipe(recipe) {//créer une nouvelle recette
    let recipes = this.state.recipes;
    recipes.push(recipe);
    localStorage.setItem('recipes', JSON.stringify(recipes));
    this.setState({recipes: recipes});
    this.showAddModal();
  }
  editRecipe(newName, newIngredients, currentlyEditing) {//modifier une recette existante
    let recipes = this.state.recipes;
    recipes[currentlyEditing] = {name: newName, ingredients: newIngredients};
    localStorage.setItem('recipes', JSON.stringify(recipes));
    this.setState({recipes: recipes});
    this.showEditModal(currentlyEditing);
  }
  deleteRecipe(index) {//supprimer une recette existante
    let recipes = this.state.recipes.slice();
    recipes.splice(index, 1);
    localStorage.setItem('recipes', JSON.stringify(recipes));
    this.setState({recipes: recipes, currentlyEditing: 0});
  }
  render() {
    const recipes = this.state.recipes;
    var currentlyEditing = this.state.currentlyEditing;
    return(
      <div className="jumbotron">
        <h1>BOÎTE À RECETTES</h1>
        <PanelGroup accordion id="recipes">
          {recipes.map((recipe, index) => (
            <Panel eventKey={index} key={index}>
              <Panel.Heading>
                <Panel.Title className="title" toggle>{recipe.name}</Panel.Title>
              </Panel.Heading>
              <Panel.Body collapsible>
                <ListGroup>
                  {recipe.ingredients.map((ingredient, index) => (
                    <ListGroupItem key={index}>{ingredient}</ListGroupItem>
                  ))}
                </ListGroup>
                <ButtonToolbar>
                  <Button bsStyle="warning" onClick={() => {this.showEditModal(index)}}>Modifier</Button>
                  <Button bsStyle="danger" onClick={() => {this.deleteRecipe(index)}}>Supprimer</Button>
                </ButtonToolbar>
              </Panel.Body>
              <EditRecipe onShow={this.state.showEdit} onEdit={this.editRecipe} onEditModal={() => {this.showEditModal(currentlyEditing)}} currentlyEditing={currentlyEditing} recipe={recipes[currentlyEditing]} />
            </Panel>
          ))}
        </PanelGroup>
        <Button bsStyle="primary" onClick={this.showAddModal}>Ajouter une Recette</Button>
        <AddRecipe onShow={this.state.showAdd} onAdd={this.addRecipe} onAddModal={this.showAddModal} />
      </div>
    );
  }
};

ReactDOM.render(<Recipe />, document.getElementById('app'));
```

Résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/47kMAn0t4eCDqcW750dE8GDmqYcl4h-gge1a)
_La boîte à recettes._

![Image](https://cdn-media-1.freecodecamp.org/images/mdmF4M34YmZWY7npdd1BuceobycVwsH4eh6U)
_La vue d'une recette lorsque son nom est cliqué._

![Image](https://cdn-media-1.freecodecamp.org/images/jYKRnx-f8SBNR0KrAqDysXwLJpwocyityzkt)
_La boîte à recettes après la suppression de la "Soupe aux pois cassés"._

![Image](https://cdn-media-1.freecodecamp.org/images/leI79SiVhNCobZCUOsNfLOJAzOtc2tFYLKdG)
_La boîte à recettes mise à jour et le stockage local._

![Image](https://cdn-media-1.freecodecamp.org/images/azGtMRgveATJsu9p-8fhvTfQPSSfXQDFZRXO)
_Le stockage local a été effacé._

![Image](https://cdn-media-1.freecodecamp.org/images/UTP4MT6WhjzI4HzMxOvjJkYKaIycG8XG4CzZ)
_La vue de la boîte à recettes après l'effacement du stockage local et le rechargement de la page web._

### Publication sur GitHub

Nous avons terminé la création de la boîte à recettes. Il est temps de la publier sur GitHub et de créer une page GitHub pour celle-ci.

Sur GitHub, créez un nouveau dépôt appelé recipe-box.

Allez dans votre répertoire de fichiers sur la ligne de commande et tapez ce qui suit :

```
git init
git add README.md
git commit -m "initial commit"
git remote add origin https://github.com/yourusername/recipe-box.git
git push -u origin master
```

Votre code est maintenant sur GitHub. Il est temps de créer une page GitHub pour le dépôt. Voici l'état actuel du fichier package.json :

![Image](https://cdn-media-1.freecodecamp.org/images/diJKdw-XmMittlIfipLKBPAbvEBzQRLjs-tx)
_fichier package.json_

Sur la ligne de commande, nous exécutons :

```
npm install gh-pages --save-dev
```

Les pages GitHub seront installées. Ensuite, nous devons spécifier notre URL "homepage", et le code de pré-déploiement et de déploiement dans "scripts", dans package.json. Le résultat final devrait être :

![Image](https://cdn-media-1.freecodecamp.org/images/1FP-l8L-Ur47NrsMDibH5iAt-mzNsVm93dNN)
_fichier package.json mis à jour_

Sur la ligne de commande, nous exécutons :

```
npm run deploy
git add .
git commit -m "created a github page for the repository"
git push origin master
```

Nous avons maintenant une page GitHub pour la boîte à recettes, et son URL est celle spécifiée dans "homepage" de package.json.

Le projet est complet. Pour référence, vous pouvez consulter mon dépôt GitHub [ici](https://github.com/edkahara/recipe-box).

### **Conclusion**

C'était certainement un défi passionnant à relever. J'ai apprécié partager cela avec vous. J'espère que vous avez appris quelque chose.

Merci d'avoir lu.