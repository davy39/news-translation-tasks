---
title: How to build freeCodeCamp’s recipe box using React and local storage
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
seo_title: null
seo_desc: 'By Edward Njoroge

  I completed my first edition of the Free Code Camp recipe box project on May 3,
  2018. I put it up here for review. Then I didn’t check the reviews for a few weeks.
  When I returned, I was shocked to learn that I had overlooked an imp...'
---

By Edward Njoroge

I completed my first edition of the Free Code Camp recipe box project on May 3, 2018. I put it up [here](https://forum.freecodecamp.org/t/check-out-my-recipe-box/177769/2) for review. Then I didn’t check the reviews for a few weeks. When I returned, I was shocked to learn that I had overlooked an important feature in forms.

![Image](https://cdn-media-1.freecodecamp.org/images/GlNVp3au86v0MmkdMc-Qv-GH9KnVI88LeNFo)

I know. Terrible mistake. My form allowed for the creation of an empty recipe. This oversight shows the importance of allowing other people to review your code.

It turned out I wasn’t the only one that missed this important feature. I checked freeCodeCamp’s example project for the recipe box ([here](https://codepen.io/FreeCodeCamp/full/xVXWag/)) and it was missing the same feature. Validation is not mentioned in the user stories ([here](https://www.freecodecamp.org/challenges/build-a-recipe-box)) either.

I figured that if I included validation in my project, I could try to convince freeCodeCamp to make my recipe box the example project for this challenge. So I restarted the project, and during this process I was inspired to write this Medium post.

### Building the recipe box

For this project, we will use create-react-app, React bootstrap, and bootstrap CSS.

#### Step 1: Set up the React environment and add React bootstrap.

```
npx create-react-app recipe-box
npm install react-bootstrap --save
```

We will create a file directory that resembles the one below:

![Image](https://cdn-media-1.freecodecamp.org/images/66AzutgiMLsdMyNrX8WS7xaM-Q6XfL2RQZpb)

We delete favicon.ico and manifest.json from the public folder, and everything except index.js and index.css from the src folder. Inside the SRC folder, create a components folder and a CSS folder. Move index.css to the CSS folder.

#### _Step 2: Set up the html in index.html._

In index.html:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Recipe Box</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="This is a Free Code Camp Project called Recipe Box">
    <meta name="keywords" content="HTML, CSS, JAVASCRIPT, REACTJS">
    <meta name="author" content="Your Name">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/css?family=Mina" rel="stylesheet">
  </head>
  <body>
    <!--set up a div where all the code will be rendered-->
    <div class="container" id="app"></div>
  </body>
</html>
```

#### _Step 3: Set up the first view of the recipe box._

In index.js, we create an initial list of recipes in this.state and display them.

In index.js:

```js
//import the necessary files
import React from 'react';
import ReactDOM from 'react-dom';
import {PanelGroup,Panel,Button,ButtonToolbar,ListGroup,ListGroupItem} from 'react-bootstrap';
import './css/index.css';
//create the main class for displaying the recipes
class Recipe extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recipes: [
        {name: "Banana Smoothie", ingredients: ["2 bananas", "1/2 cup vanilla yogurt", "1/2 cup skim milk", "2 teaspoons honey", "pinch of cinnamon"]},
        {name: "Spaghetti", ingredients: ["Noodles", "Tomato Sauce", "Meatballs"]},
        {name: "Split Pea Soup", ingredients: ["1 pound split peas", "1 onion", "6 carrots", "4 ounces of ham"]}
      ]
    };
  }
  render() {
    const recipes = this.state.recipes;
    return(
      <div className="jumbotron">
        <h1>RECIPE BOX</h1>
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
                  <Button bsStyle="warning">Edit</Button>
                  <Button bsStyle="danger">Delete</Button>
                </ButtonToolbar>
              </Panel.Body>
            </Panel>
          ))}
        </PanelGroup>
        <Button bsStyle="primary">Add Recipe</Button>
      </div>
    );
  }
};

ReactDOM.render(<Recipe />, document.getElementById('app'));
```

In index.css:

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

Result:

![Image](https://cdn-media-1.freecodecamp.org/images/9wFXTAqnvx1TmKw-iuixpJkXOQTcpF-8xOLg)
_The recipe box._

![Image](https://cdn-media-1.freecodecamp.org/images/KZ5eebS0feoWVzNArylgcBvs9IeO0McXWamW)
_The view of a recipe when its name is clicked on._

#### _Step 4: Creating the Add Recipe function._

We are now ready to add recipes. We create a file called addrecipe.js inside the components folder.

Recipes will be added through a modal form. We must first be able to activate and deactivate the modal. We create a state called showAdd and set it to false. Then we create a function called showAddModal() that changes showAdd to true if its currently false and vice versa.

When the “Add Recipe” button is clicked, showAdd will turn to true and the modal will be displayed. Therefore, showAdd and showAddModal() must be passed as props to addrecipe.js.

To add a recipe, an addRecipe() function that takes the argument ‘recipe’ will be created. It takes the details for the new recipe, and pushes them to the end of the recipe state array. This function will also be passed as a prop to addrecipe.js.

In index.js:

```js
//import the necessary files
import React from 'react';
import ReactDOM from 'react-dom';
import {PanelGroup,Panel,Button,ButtonToolbar,ListGroup,ListGroupItem} from 'react-bootstrap';
import {AddRecipe} from './components/addrecipe';
import './css/index.css';
//create the main class for displaying the recipes
class Recipe extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recipes: [
        {name: "Banana Smoothie", ingredients: ["2 bananas", "1/2 cup vanilla yogurt", "1/2 cup skim milk", "2 teaspoons honey", "pinch of cinnamon"]},
        {name: "Spaghetti", ingredients: ["Noodles", "Tomato Sauce", "Meatballs"]},
        {name: "Split Pea Soup", ingredients: ["1 pound split peas", "1 onion", "6 carrots", "4 ounces of ham"]}
      ],
      showAdd: false
    };
    this.showAddModal = this.showAddModal.bind(this);
    this.addRecipe = this.addRecipe.bind(this);
  }
  showAddModal() {//show the new recipe modal
    this.setState({showAdd: !this.state.showAdd});
  }
  addRecipe(recipe) {//create a new recipe
    let recipes = this.state.recipes;
    recipes.push(recipe);
    this.setState({recipes: recipes});
    this.showAddModal();
  }
  render() {
    const recipes = this.state.recipes;
    return(
      <div className="jumbotron">
        <h1>RECIPE BOX</h1>
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
                  <Button bsStyle="warning">Edit</Button>
                  <Button bsStyle="danger">Delete</Button>
                </ButtonToolbar>
              </Panel.Body>
            </Panel>
          ))}
        </PanelGroup>
        <Button bsStyle="primary" onClick={this.showAddModal}>Add Recipe</Button>
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

In addrecipe.js, we create a state that holds the new recipe name and recipe ingredients, and the initial values are empty strings. We will then change the state every time we change the contents of the form as we would in a markdown. This will make form validation easier.

Instead of displaying form errors for validation, we use regular expression to ensure that we only save a recipe if some conditions are met. These conditions are:

(a) Both the recipe name and ingredients sections must not be empty, that is both must have at least one character.

(b) The form recipe name cannot begin with a space. This ensures that the recipe name begins with at least one alphanumeric character or symbol.

(c)The form recipe ingredients cannot begin or end with a space or comma. This is because ingredients will be split by commas into an array that is then displayed as a list like our current ingredients are.

The modal will have a Save Recipe button which will be disabled until all conditions are met. When save recipe is clicked, the recipe will be added to our recipe box.

In addrecipe.js:

```js
//import the necessary files
import React from 'react';
import {Modal,ControlLabel,FormGroup,FormControl,Button} from 'react-bootstrap';

//create a class for displaying the modal for adding a new recipe and export it
export class AddRecipe extends React.Component {
  constructor(props) {//create a state to handle the new recipe
    super(props);
    this.state = {name: "", ingredients: ""};
    this.handleRecipeNameChange = this.handleRecipeNameChange.bind(this);
    this.handleRecipeIngredientsChange = this.handleRecipeIngredientsChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleCancel = this.handleCancel.bind(this);
  }
  handleRecipeNameChange(e) {//change the name to reflect user input
    this.setState({name: e.target.value});
  }
  handleRecipeIngredientsChange(e) {//change the ingredients to reflect user input
    this.setState({ingredients: e.target.value});
  }
  handleSubmit(e) {//get the recipe data, manipulate it and call the function for creating a new recipe
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
          <Modal.Title>New Recipe</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <FormGroup controlId="formControlsName">
            <ControlLabel>Recipe Name</ControlLabel>
            <FormControl type="text" required onChange={this.handleRecipeNameChange} value={this.state.name} placeholder="Enter Name" />
          </FormGroup>
          <FormGroup controlId="formControlsIngredients">
            <ControlLabel>Recipe Ingredients</ControlLabel>
            <FormControl componentClass="textarea" type="text" required onChange={this.handleRecipeIngredientsChange} value={this.state.ingredients} placeholder="Enter Ingredients(separate by commas)" />
          </FormGroup>
        </Modal.Body>
        <Modal.Footer>
          <Button disabled={!validRecipe} bsStyle="success" onClick={this.handleSubmit}>Save Recipe</Button>
        </Modal.Footer>
      </Modal>
    );
  }
};
```

Result:

![Image](https://cdn-media-1.freecodecamp.org/images/jgKE3gUIcIhXzZw7gs16UsCITbITL2yOGOwL)
_The recipe box._

![Image](https://cdn-media-1.freecodecamp.org/images/s8CjbxJM64MQnbMslBEuNxS84WmwYjgIHv9w)
_The blank modal that appears once the “Add Recipe” button is clicked._

![Image](https://cdn-media-1.freecodecamp.org/images/Nj5Z7vJI5oMPU3nsBL1sGXW0vWZ03ct6auHB)
_Filling in the form and submitting it._

![Image](https://cdn-media-1.freecodecamp.org/images/LRrbrD97cXmmE31wXH0YzK1CtlWCeHge5bE6)
_The updated recipe box._

![Image](https://cdn-media-1.freecodecamp.org/images/rKYCMp4sQw9tkgzYBcdZ-v0DdnHMekSs4mAz)
_The view of the new recipe when its name is clicked on._

#### _Step 5: Creating the Edit Recipe function._

We are now ready to edit recipes. We create a file called editrecipe.js inside the components folder.

Recipes will be edited through a modal form. We must first be able to activate and deactivate the modal. We create a state called showEdit and set it to false. Then we create a function called showEditModal() that changes showEdit to true if its currently false and vice versa. When the “Edit” button is clicked, showEditModal() will run, showEdit will turn to true, and the modal will be displayed.

We will also need a way to ensure that the correct recipe is displayed on the form fields for editing. We create a state called currentlyEditing and set it to 0. We then ensure that the details of this.state.recipes[currentlyEditing] are displayed on the form.

Since 0 is the default, whenever Edit Recipe is clicked, the form will only show the details of the first recipe. We need a way to update currentlyEditing to the index of the recipe we want displayed.

In showEditModal(), we pass index as an argument and this argument will be equal to the index of the current recipe. Now when the “Edit Recipe” button is clicked, showEditModal() will run, showEdit will turn to true, currentlyEditing will become the index of the recipe, and the modal will be displayed with the correct recipe’s information. Therefore, showEdit and showEditModal(index) must be passed as props to editrecipe.js.

To edit a recipe, an editRecipe() function that takes the arguments newName, newIngredients, and currentlyEditing will be created. In this function, we use currentlyEditing (which is now the index of the recipe we are editing) to identify that recipe and set its name to the newName and its ingredients to the newIngredients. Therefore, editRecipe, the recipe we need to edit, and currentlyEditing must be passed as props to editrecipe.js.

In index.js:

```js
//import the necessary files
import React from 'react';
import ReactDOM from 'react-dom';
import {PanelGroup,Panel,Button,ButtonToolbar,ListGroup,ListGroupItem} from 'react-bootstrap';
import {AddRecipe} from './components/addrecipe';
import {EditRecipe} from './components/editrecipe';
import './css/index.css';
//create the main class for displaying the recipes
class Recipe extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recipes: [
        {name: "Banana Smoothie", ingredients: ["2 bananas", "1/2 cup vanilla yogurt", "1/2 cup skim milk", "2 teaspoons honey", "pinch of cinnamon"]},
        {name: "Spaghetti", ingredients: ["Noodles", "Tomato Sauce", "Meatballs"]},
        {name: "Split Pea Soup", ingredients: ["1 pound split peas", "1 onion", "6 carrots", "4 ounces of ham"]}
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
  showAddModal() {//show the new recipe modal
    this.setState({showAdd: !this.state.showAdd});
  }
  showEditModal(index) {//show the edit recipe modal
    this.setState({showEdit: !this.state.showEdit, currentlyEditing: index});
  }
  addRecipe(recipe) {//create a new recipe
    let recipes = this.state.recipes;
    recipes.push(recipe);
    this.setState({recipes: recipes});
    this.showAddModal();
  }
  editRecipe(newName, newIngredients, currentlyEditing) {//edit an existing recipe
    let recipes = this.state.recipes;
    recipes[currentlyEditing] = {name: newName, ingredients: newIngredients};
    this.setState({recipes: recipes});
    this.showEditModal(currentlyEditing);
  }
  render() {
    const recipes = this.state.recipes;
    return(
      <div className="jumbotron">
        <h1>RECIPE BOX</h1>
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
                  <Button bsStyle="warning" onClick={() => {this.showEditModal(index)}}>Edit</Button>
                  <Button bsStyle="danger">Delete</Button>
                </ButtonToolbar>
              </Panel.Body>
              <EditRecipe onShow={this.state.showEdit} onEdit={this.editRecipe} onEditModal={() => {this.showEditModal(this.state.currentlyEditing)}} currentlyEditing={this.state.currentlyEditing} recipe={recipes[this.state.currentlyEditing]} />
            </Panel>
          ))}
        </PanelGroup>
        <Button bsStyle="primary" onClick={this.showAddModal}>Add Recipe</Button>
        <AddRecipe onShow={this.state.showAdd} onAdd={this.addRecipe} onAddModal={this.showAddModal} />
      </div>
    );
  }
};

ReactDOM.render(<Recipe />, document.getElementById('app'));
ReactDOM.render(<Recipe />, document.getElementById('app'));
```

In editrecipe.js:

```js
//import the necessary files
import React from 'react';
import {Modal,ControlLabel,FormGroup,FormControl,Button} from 'react-bootstrap';

//create a class for displaying the modal for editing an existing recipe and export it
export class EditRecipe extends React.Component {
  constructor(props) {//create a state to handle the recipe to be edited
    super(props);
    this.state = {name: "", ingredients: ""};
    this.handleRecipeNameChange = this.handleRecipeNameChange.bind(this);
    this.handleRecipeIngredientsChange = this.handleRecipeIngredientsChange.bind(this);
    this.handleEdit = this.handleEdit.bind(this);
    this.handleCancel = this.handleCancel.bind(this);
  }
  static getDerivedStateFromProps(props, state) {//make the recipe prop a state
    const prevName = state.prevName;
    const prevIngredients = state.prevIngredients;
    const name = prevName !== props.recipe.name ? props.recipe.name : state.name;
    const ingredients = prevIngredients !== props.recipe.ingredients.join(",") ? props.recipe.ingredients.join(",") : state.ingredients;
    return {
      prevName: props.recipe.name, name,
      prevIngredients: props.recipe.ingredients.join(","), ingredients,
    }
  }
  handleRecipeNameChange(e) {//change the name to reflect user input
    this.setState({name: e.target.value});
  }
  handleRecipeIngredientsChange(e) {//change the ingredients to reflect user input
    this.setState({ingredients: e.target.value});
  }
  handleEdit(e) {//get the recipe data, manipulate it and call the function for editing an existing recipe
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
          <Modal.Title>Edit Recipe</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <FormGroup controlId="formControlsName">
            <ControlLabel>Recipe Name</ControlLabel>
            <FormControl type="text" required onChange={this.handleRecipeNameChange} value={this.state.name} placeholder="Enter Name" />
          </FormGroup>
          <FormGroup controlId="formControlsIngredients">
            <ControlLabel>Recipe Ingredients</ControlLabel>
            <FormControl componentClass="textarea" type="text" required onChange={this.handleRecipeIngredientsChange} value={this.state.ingredients} placeholder="Enter Ingredients(separate by commas)" />
          </FormGroup>
        </Modal.Body>
        <Modal.Footer>
          <Button disabled={!validRecipe} bsStyle="success" onClick={this.handleEdit}>Save Recipe</Button>
        </Modal.Footer>
      </Modal>
    );
  }
};
```

Result:

![Image](https://cdn-media-1.freecodecamp.org/images/xWn8sF69-fASP8b16qE2WGYfaESnlUSwq8N4)
_The recipe box._

![Image](https://cdn-media-1.freecodecamp.org/images/CmLZh4BsZG64S5btNq6woPqCxkjvMTRyZbJ2)
_The view of a recipe when its name is clicked on._

![Image](https://cdn-media-1.freecodecamp.org/images/XL8CPngL-wSYN34h0nmLwKmZSbeoLFWuejZw)
_The view of the recipe’s edit modal._

![Image](https://cdn-media-1.freecodecamp.org/images/xZWkhYopZy56DeL5t39i98uufYgSDa0-Gc2d)
_The ingredients have been edited. “Oil” has been replaced with “1 Tablespoon of Salt”._

![Image](https://cdn-media-1.freecodecamp.org/images/DLa14Mwboe-WJTF-LeZzAQn2R7j3gLAcIuZM)
_The edited version of the recipe._

In editRecipe.js, we create a state that holds the name and ingredients of the recipe to be edited, and set the initial values as empty strings. We then use React’s new life cycle method getDerivedStateFromProps to make our recipe prop’s name and ingredients the new name and ingredients of our state. The method for doing so is clearly explained [here](https://reactjs.org/blog/2018/05/23/react-v-16-4.html#bugfix-for-getderivedstatefromprops).

We will then change the state every time we change the contents of the form and validate the form as we did when adding a new recipe.

#### _Step 6: Creating the Delete Recipe function._

We are now ready to delete recipes. This step does not need the creation of a new file.

To delete a recipe, a deleteRecipe() function that takes the argument index will be created. In this function, we use the index of a recipe to identify the recipe to be deleted. We will use JavaScript’s splice method to delete the recipe. We then set currentlyEditing to 0 just to reset the recipe box, that is, we don’t want currentlyEditing to still be the index of a recipe that doesn’t exist anymore.

In index.js:

```js
//import the necessary files
import React from 'react';
import ReactDOM from 'react-dom';
import {PanelGroup,Panel,Button,ButtonToolbar,ListGroup,ListGroupItem} from 'react-bootstrap';
import {AddRecipe} from './components/addrecipe';
import {EditRecipe} from './components/editrecipe';
import './css/index.css';
//create the main class for displaying the recipes
class Recipe extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      recipes: [
        {name: "Banana Smoothie", ingredients: ["2 bananas", "1/2 cup vanilla yogurt", "1/2 cup skim milk", "2 teaspoons honey", "pinch of cinnamon"]},
        {name: "Spaghetti", ingredients: ["Noodles", "Tomato Sauce", "Meatballs"]},
        {name: "Split Pea Soup", ingredients: ["1 pound split peas", "1 onion", "6 carrots", "4 ounces of ham"]}
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
  showAddModal() {//show the new recipe modal
    this.setState({showAdd: !this.state.showAdd});
  }
  showEditModal(index) {//show the edit recipe modal
    this.setState({showEdit: !this.state.showEdit, currentlyEditing: index});
  }
  addRecipe(recipe) {//create a new recipe
    let recipes = this.state.recipes;
    recipes.push(recipe);
    this.setState({recipes: recipes});
    this.showAddModal();
  }
  editRecipe(newName, newIngredients, currentlyEditing) {//edit an existing recipe
    let recipes = this.state.recipes;
    recipes[currentlyEditing] = {name: newName, ingredients: newIngredients};
    this.setState({recipes: recipes});
    this.showEditModal(currentlyEditing);
  }
  deleteRecipe(index) {//delete an existing recipe
    let recipes = this.state.recipes.slice();
    recipes.splice(index, 1);
    this.setState({recipes: recipes, currentlyEditing: 0});
  }
  render() {
    const recipes = this.state.recipes;
    return(
      <div className="jumbotron">
        <h1>RECIPE BOX</h1>
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
                  <Button bsStyle="warning" onClick={() => {this.showEditModal(index)}}>Edit</Button>
                  <Button bsStyle="danger" onClick={() => {this.deleteRecipe(index)}}>Delete</Button>
                </ButtonToolbar>
              </Panel.Body>
              <EditRecipe onShow={this.state.showEdit} onEdit={this.editRecipe} onEditModal={() => {this.showEditModal(this.state.currentlyEditing)}} currentlyEditing={this.state.currentlyEditing} recipe={recipes[this.state.currentlyEditing]} />
            </Panel>
          ))}
        </PanelGroup>
        <Button bsStyle="primary" onClick={this.showAddModal}>Add Recipe</Button>
        <AddRecipe onShow={this.state.showAdd} onAdd={this.addRecipe} onAddModal={this.showAddModal} />
      </div>
    );
  }
};

ReactDOM.render(<Recipe />, document.getElementById('app'));
```

Result:

![Image](https://cdn-media-1.freecodecamp.org/images/280ZsOAYf4L1YHNsmumPhMS7Cx9NLskuWwM7)
_The recipe box._

![Image](https://cdn-media-1.freecodecamp.org/images/NqLWTIFMqoGSewKoysUlOhWHJi4B9hDpeHV3)
_The recipe box after the “Kenyan Chapati” recipe is deleted._

![Image](https://cdn-media-1.freecodecamp.org/images/T6k0Ddc9CgGJRH-UU7CVJOQc3LHKYEsqTOb4)
_The updated recipe box._

#### _Step 7: Adding Local Storage._

HTML 5 Web Storage allows web applications to store data locally within the user’s browser. There are two web storage objects:

(a) Session Storage: Session storage stores data for one session, and the data is lost when the browser tab is closed.

(b) Local Storage: Local storage stores data indefinitely. The data will not be deleted when the browser is closed, and will be available all the time since there is no expiration date.

To add local storage, we will change our recipe state to an empty array. We will get the recipes from local storage first and then set our recipe state to these recipes. We will use the life cycle method componentDidMount, because we want to load the local storage after our component renders. We will also be updating local storage whenever we add, edit, or delete a recipe.

So if, for example, we delete one of our original 3 recipes and reload the page, we will not see the recipe we deleted. When we clear our local storage and reload the page, we will once again see the original recipe we deleted.

In index.js:

```js
//import the necessary files
import React from 'react';
import ReactDOM from 'react-dom';
import {PanelGroup,Panel,Button,ButtonToolbar,ListGroup,ListGroupItem} from 'react-bootstrap';
import './css/index.css';
import {AddRecipe} from './components/addrecipe';
import {EditRecipe} from './components/editrecipe';
//create the main class for displaying the recipes
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
  componentDidMount() {//load the local storage data after the component renders
    var recipes = (typeof localStorage["recipes"] !== "undefined") ? JSON.parse(localStorage.getItem("recipes")) : [
      {name: "Banana Smoothie", ingredients: ["2 bananas", "1/2 cup vanilla yogurt", "1/2 cup skim milk", "2 teaspoons honey", "pinch of cinnamon"]},
      {name: "Spaghetti", ingredients: ["Noodles", "Tomato Sauce", "Meatballs"]},
      {name: "Split Pea Soup", ingredients: ["1 pound split peas", "1 onion", "6 carrots", "4 ounces of ham"]}
    ];
    this.setState({recipes: recipes});
  }
  showAddModal() {//show the new recipe modal
    this.setState({showAdd: !this.state.showAdd});
  }
  showEditModal(index) {//show the edit recipe modal
    this.setState({currentlyEditing: index, showEdit: !this.state.showEdit});
  }
  addRecipe(recipe) {//create a new recipe
    let recipes = this.state.recipes;
    recipes.push(recipe);
    localStorage.setItem('recipes', JSON.stringify(recipes));
    this.setState({recipes: recipes});
    this.showAddModal();
  }
  editRecipe(newName, newIngredients, currentlyEditing) {//edit an existing recipe
    let recipes = this.state.recipes;
    recipes[currentlyEditing] = {name: newName, ingredients: newIngredients};
    localStorage.setItem('recipes', JSON.stringify(recipes));
    this.setState({recipes: recipes});
    this.showEditModal(currentlyEditing);
  }
  deleteRecipe(index) {//delete an existing recipe
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
        <h1>RECIPE BOX</h1>
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
                  <Button bsStyle="warning" onClick={() => {this.showEditModal(index)}}>Edit</Button>
                  <Button bsStyle="danger" onClick={() => {this.deleteRecipe(index)}}>Delete</Button>
                </ButtonToolbar>
              </Panel.Body>
              <EditRecipe onShow={this.state.showEdit} onEdit={this.editRecipe} onEditModal={() => {this.showEditModal(currentlyEditing)}} currentlyEditing={currentlyEditing} recipe={recipes[currentlyEditing]} />
            </Panel>
          ))}
        </PanelGroup>
        <Button bsStyle="primary" onClick={this.showAddModal}>Add Recipe</Button>
        <AddRecipe onShow={this.state.showAdd} onAdd={this.addRecipe} onAddModal={this.showAddModal} />
      </div>
    );
  }
};

ReactDOM.render(<Recipe />, document.getElementById('app'));
```

Result:

![Image](https://cdn-media-1.freecodecamp.org/images/47kMAn0t4eCDqcW750dE8GDmqYcl4h-gge1a)
_The recipe box._

![Image](https://cdn-media-1.freecodecamp.org/images/mdmF4M34YmZWY7npdd1BuceobycVwsH4eh6U)
_The view of a recipe when its name is clicked on._

![Image](https://cdn-media-1.freecodecamp.org/images/jYKRnx-f8SBNR0KrAqDysXwLJpwocyityzkt)
_The recipe box after “Split Pea Soup” has been deleted._

![Image](https://cdn-media-1.freecodecamp.org/images/leI79SiVhNCobZCUOsNfLOJAzOtc2tFYLKdG)
_The updated recipe box and the local storage._

![Image](https://cdn-media-1.freecodecamp.org/images/azGtMRgveATJsu9p-8fhvTfQPSSfXQDFZRXO)
_Local storage has been cleared._

![Image](https://cdn-media-1.freecodecamp.org/images/UTP4MT6WhjzI4HzMxOvjJkYKaIycG8XG4CzZ)
_The view of the recipe box after local storage has been cleared and the web page reloaded._

### Posting on GitHub

We are done making the recipe box. Time to post it on GitHub and create a GitHub page for it.

On GitHub, create a new repository called recipe-box.

Go to your file directory on the command line and type the following:

```
git init
git add README.md
git commit -m "initial commit"
git remote add origin https://github.com/yourusername/recipe-box.git
git push -u origin master
```

Your code is now on GitHub. Now its time to create a GitHub page for the repository. This should be the current status of the package.json file:

![Image](https://cdn-media-1.freecodecamp.org/images/diJKdw-XmMittlIfipLKBPAbvEBzQRLjs-tx)
_package.json file_

On the command line we run:

```
npm install gh-pages --save-dev
```

GitHub pages will be installed. Then we must specify our “homepage” URL, and predeploy and deploy code in “scripts”, in package.json. The end result should be:

![Image](https://cdn-media-1.freecodecamp.org/images/1FP-l8L-Ur47NrsMDibH5iAt-mzNsVm93dNN)
_updated package.json file_

On the command line we run:

```
npm run deploy
git add .
git commit -m "created a github page for the repository"
git push origin master
```

We now have a GitHub page for the recipe box, and its URL is the one specified in “homepage” of package.json.

The project is complete. For reference you can check out my GitHub repository [here](https://github.com/edkahara/recipe-box).

### **Conclusion**

This was certainly a thrilling challenge to tackle. I enjoyed sharing this with you. I hope you’ve learned something from it.

Thank you for reading.

