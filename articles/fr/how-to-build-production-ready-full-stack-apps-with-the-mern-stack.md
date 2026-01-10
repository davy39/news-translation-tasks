---
title: Comment construire des applications Full Stack prêtes pour la production avec
  la pile MERN
subtitle: ''
author: Mohit Menghnani
co_authors: []
series: null
date: '2025-07-07T13:48:52.634Z'
originalURL: https://freecodecamp.org/news/how-to-build-production-ready-full-stack-apps-with-the-mern-stack
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1751502709499/b43b3607-f01b-45c0-9797-75eef92497c6.png
tags:
- name: full stack
  slug: full-stack
- name: software development
  slug: software-development
- name: clean code
  slug: clean-code
- name: best practices
  slug: best-practices
seo_title: Comment construire des applications Full Stack prêtes pour la production
  avec la pile MERN
seo_desc: 'As developers, we’re always looking for more efficient tools. The MERN
  stack (MongoDB, Express.js, React, and Node.js) stands out for its JavaScript-centric
  nature, offering a unified language across the entire application.

  In this guide, you''ll buil...'
---

En tant que développeurs, nous cherchons toujours des outils plus efficaces. La pile MERN (MongoDB, Express.js, React et Node.js) se distingue par sa nature centrée sur JavaScript, offrant un langage unifié pour toute l'application.

Dans ce guide, vous allez construire une application complète de gestion de tâches avec authentification des utilisateurs, routes protégées et fonctionnalités CRUD complètes, construite avec React en frontend et Express/MongoDB en backend.

Cet article servira de guide pratique et axé sur le code pour construire, sécuriser et déployer une application MERN, s'appuyant sur ma propre expérience pratique. Chaque section contient du code que vous pouvez exécuter, et je donnerai des explications concises tout au long du processus.

Peu importe si vous débutez avec MERN ou si vous cherchez à améliorer vos connaissances en architecture et en déploiement de production, cet article est conçu pour vous amener de zéro à la production en toute confiance.

## Table des matières

* [Prérequis](#heading-prerequisites)
    
    * [Outils et pile technologique](#heading-outils-et-pile-technologique)
        
    * [Compétences et configuration](#heading-competences-et-configuration)
        
* [Configuration du projet : poser les bases](#heading-configuration-du-projet-poser-les-bases)
    
    * [Structure du projet](#heading-structure-du-projet)
        
    * [Qualité du code : linting et formatage](#heading-qualite-du-code-linting-et-formatage)
        
* [Tests : assurer la robustesse](#heading-tests-assurer-la-robustesse)
    
    * [Tests backend (Node.js/Express.js)](#heading-tests-backend-nodejsexpressjs)
        
    * [Tests frontend (React Testing Library + Cypress)](#heading-tests-frontend-react-testing-library-cypress)
        
* [Comment construire le gestionnaire de tâches](#heading-comment-construire-le-gestionnaire-de-taches)
    
    * [Implémentation backend (Node.js/Express.js)](#heading-implementation-backend-nodejsexpressjs)
        
    * [Implémentation frontend (React)](#heading-implementation-frontend-react)
        
* [Déploiement : de](#heading-deploiement-de-localhost-a-live) [Localhost](http://Localhost) [à Live](#heading-deploiement-de-localhost-a-live)
    
    * [Déploiement backend (Node.js/Express.js)](#heading-deploiement-backend-nodejsexpressjs)
        
    * [Déploiement frontend (React)](#heading-deploiement-frontend-react)
        
    * [Déploiement de la base de données (MongoDB Atlas)](#heading-deploiement-de-la-base-de-donnees-mongodb-atlas)
        
    * [1\. Exemple de configuration .env](#heading-1-exemple-de-configuration-env)
        
    * [2\. Connexion à MongoDB dans app.js](#heading-2-connexion-a-mongodb-dans-appjs)
        
    * [Autres options de déploiement](#heading-autres-options-de-deploiement)
        
* [Bonnes pratiques de sécurité : renforcer votre application](#heading-bonnes-pratiques-de-securite-renforcer-votre-application)
    
    * [Configuration de la validation et de la sanitisation des entrées](#heading-configuration-de-la-validation-et-de-la-sanitisation-des-entrees)
        
    * [Ajouter l'authentification et l'autorisation](#heading-ajouter-lauthentification-et-lautorisation)
        
    * [Implémenter la limitation de débit](#heading-implementer-la-limitation-de-debit)
        
    * [Configuration CORS (Cross-Origin Resource Sharing)](#heading-configuration-cors-cross-origin-resource-sharing)
        
    * [Utiliser les variables d'environnement](#heading-utiliser-les-variables-denvironnement)
        
* [Surveillance et journalisation avec Winston et Morgan](#heading-surveillance-et-journalisation-avec-winston-et-morgan)
    
    * [Surveillance des erreurs frontend (Sentry)](#heading-surveillance-des-erreurs-frontend-sentry)
        
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de vous lancer dans le projet, voici ce dont vous aurez besoin pour tirer le meilleur parti de ce tutoriel :

### Outils et pile technologique

Vous utiliserez les technologies suivantes tout au long du projet :

* **Node.js & npm** – Environnement d'exécution backend et gestionnaire de paquets
    
* **Express.js** – Framework web pour Node
    
* **MongoDB Atlas** – Base de données NoSQL hébergée dans le cloud
    
* **Mongoose** – ODM pour MongoDB
    
* **React** – Bibliothèque d'interface utilisateur frontend
    
* **React Router** – Pour le routage côté client
    
* **Axios** – Pour effectuer des requêtes API
    
* **Jest & Supertest** – Pour les tests backend
    
* **React Testing Library & Cypress** – Pour les tests unitaires et E2E frontend
    
* **ESLint + Prettier** – Pour le formatage et le linting du code
    
* **Husky** – Pour configurer les hooks pré-commit
    
* **Helmet, Joi, express-rate-limit, cors** – Pour la sécurité, la validation et les bonnes pratiques
    
* **PM2 & NGINX** – Pour le déploiement backend
    
* **Sentry** – Pour la surveillance des erreurs
    

### Compétences et configuration

* Connaissance de base de JavaScript, React et Node.js
    
* Familiarité avec les API REST et les flux de requêtes/réponses HTTP
    
* Git et un compte GitHub pour le contrôle de version
    
* Un compte MongoDB Atlas gratuit
    
* Node.js et npm installés localement (Node 18+ recommandé)
    

## **Configuration du projet : poser les bases**

Une structure de projet bien organisée est cruciale pour la maintenabilité. Nous adopterons ici une séparation claire entre le frontend et le backend.

### **Structure du projet**

Cette structure sépare clairement le frontend React (client/) du backend Node.js/Express.js (server/), favorisant la modularité et une gestion plus facile.

```javascript
my-mern-app/                # Dossier racine
├── client/                 # Frontend React
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
├── server/                 # Backend Node.js/Express.js
│   ├── config/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── app.js
│   └── package.json
```

### **Qualité du code : linting et formatage**

La cohérence est essentielle lorsque vous construisez une application de niveau production comme celle-ci. Nous utiliserons ESLint avec le style Airbnb et Prettier pour une qualité et un formatage de code automatisés.

Pour installer ces outils, exécutez cette commande dans votre terminal :

```bash
npm install --save-dev eslint prettier eslint-config-airbnb-base eslint-plugin-prettier
```

Et voici quelques configurations avec leurs configurations recommandées :

Cette configuration configure ESLint pour un projet Node.js en utilisant les guides de style Airbnb et Prettier, avec des règles personnalisées pour assouplir les contraintes de linting strictes comme permettre `console.log` et désactiver les noms de fonction obligatoires.

#### **.eslintrc.js (exemple côté serveur)**

```javascript
module.exports = {

  env: {

    node: true,

    commonjs: true,

    es2021: true,

  },

  extends: ["airbnb-base", "prettier"],

  plugins: ["prettier"],

  parserOptions: {

    ecmaVersion: 12,

  },

  rules: {

    "prettier/prettier": "error",

    "no-console": "off",

    "func-names": "off",

    "no-process-exit": "off",

    "class-methods-use-this": "off",

    "import/no-extraneous-dependencies": "off",

  },

};
```

#### **.prettierrc**

Cette configuration impose un formatage cohérent : ajoute des points-virgules, utilise des virgules finales lorsque c'est valide, et préfère les guillemets simples pour les chaînes.

```json
{

  "semi": true,

  "trailingComma": "all",

  "singleQuote": true

}
```

### **Contrôle de version : Essentiels Git**

Git est indispensable. Vous pouvez utiliser des branches de fonctionnalités et des pull requests pour le développement collaboratif, ce qui facilite le travail sur de grands projets avec des collègues. Envisagez d'utiliser Husky pour les hooks pré-commit afin de faire respecter le linting et les tests.

#### Installer Husky :

Installez Husky pour gérer facilement les hooks Git, vous permettant d'automatiser des tâches comme le linting et les tests avant les commits.

```bash
npm install husky --save-dev
```

#### package.json (ajouter un script)

Ce fichier `package.json` configure un projet Node.js nommé `my-mern-app`, et configure un script `prepare` pour installer les hooks Git en utilisant Husky (v7). Il est prêt pour ajouter l'automatisation pré-commit, comme le linting ou les tests.

```json
{

  "name": "my-mern-app",

  "version": "1.0.0",

  "description": "",

  "main": "index.js",

  "scripts": {

    "prepare": "husky install"

  },

  "keywords": [],

  "author": "",

  "license": "ISC",

  "devDependencies": {

    "husky": "^7.0.0"

  }

}
```

#### Créer un hook pré-commit

La commande suivante configure un hook pré-commit qui exécute automatiquement vos tests et votre linter avant chaque commit, garantissant la qualité du code et empêchant les erreurs d'entrer dans votre base de code.

```json
npx husky add .husky/pre-commit "npm test && npm run lint"
```

## **Tests : assurer la robustesse**

Les tests automatisés sont essentiels. Nous couvrirons les tests unitaires, d'intégration et de bout en bout dans ce guide.

### Tests backend (Node.js/Express.js)

Vous utiliserez Jest pour les tests unitaires et Supertest pour les tests d'intégration API.

##### Installez-les comme ceci :

```bash
npm install --save-dev jest supertest
```

Vous utiliserez Jest pour écrire des tests unitaires pour votre code JavaScript et Supertest pour tester les requêtes HTTP contre votre API Express.js.

#### Exemple de test (server/tests/auth.test.js) :

Ce suite de tests utilise Supertest pour simuler des appels API pour l'inscription et la connexion des utilisateurs, en vérifiant que les réponses ont les codes de statut et les propriétés attendus.

```javascript
const request = require('supertest');

const app = require('../app'); // Votre instance d'application Express

describe('Auth API', () => {

  it('should register a new user', async () => {

    const res = await request(app)

      .post('/api/auth/register')

      .send({

        username: 'testuser',

        email: 'test@example.com',

        password: 'password123',

      });

    expect(res.statusCode).toEqual(201);

    expect(res.body).toHaveProperty('_id');

  });


  it('should login an existing user', async () => {

    const res = await request(app)

      .post('/api/auth/login')

      .send({

        email: 'test@example.com',

        password: 'password123',

      });

    expect(res.statusCode).toEqual(200);

    expect(res.headers['set-cookie']).toBeDefined();

  });

});
```

### Tests frontend (React Testing Library + Cypress)

Vous utiliserez Jest et React Testing Library pour les tests unitaires/d'intégration, et Cypress pour les tests E2E.

##### Vous pouvez les installer comme ceci :

```bash
npm install --save-dev @testing-library/react @testing-library/jest-dom jest cypress
```

React Testing Library vous aidera à tester vos composants React, et Cypress fournira des tests complets de bout en bout de votre application frontend.

#### Exemple de test de composant (client/src/components/Button.test.js) :

Ce test unitaire utilise React Testing Library pour rendre un composant Button et vérifie que le contenu textuel spécifié est présent dans le rendu.

```javascript
import React from 'react';

import { render, screen } from '@testing-library/react';

import Button from './Button';


test('renders button with text', () => {

  render(<Button>Click Me</Button>);

  const buttonElement = screen.getByText(/Click Me/i);

  expect(buttonElement).toBeInTheDocument();

});
```

Le test Cypress suivant simule un flux complet d'authentification utilisateur, de l'inscription à la connexion et à la déconnexion, en vérifiant les changements d'URL attendus et le contenu de la page.

```javascript
Example E2E Test (cypress/e2e/auth.cy.js)

describe('Authentication Flow', () => {

  it('should allow a user to register and login', () => {

    cy.visit('/register');

    cy.get('input[name="username"]').type('e2euser');

    cy.get('input[name="email"]').type('e2e@example.com');

    cy.get('input[name="password"]').type('password123');

    cy.get('button[type="submit"]').click();

    cy.url().should('include', '/dashboard');

    cy.contains('Welcome, e2euser');

    cy.get('button').contains('Logout').click();

    cy.url().should('include', '/login');

    cy.get('input[name="email"]').type('e2e@example.com');

    cy.get('input[name="password"]').type('password123');

    cy.get('button[type="submit"]').click();

    cy.url().should('include', '/dashboard');

  });

});
```

## **Comment construire le gestionnaire de tâches**

Nous allons construire un simple gestionnaire de tâches avec authentification des utilisateurs et opérations CRUD pour les tâches afin que vous puissiez voir comment tout cela s'assemble.

### Implémentation backend (Node.js/Express.js)

#### Dépendances

Commencez par installer nos bibliothèques backend principales : Express pour le routage, Mongoose pour les interactions avec MongoDB, dotenv pour les variables d'environnement, bcrypt/jsonwebtoken/cookie-parser pour une authentification sécurisée, et helmet pour définir des en-têtes HTTP sécurisés :

```bash
npm install express mongoose dotenv bcryptjs jsonwebtoken cookie-parser
```

#### server/app.js (Point d'entrée)

Ensuite, nous allons configurer le premier ou le point d'entrée principal pour le backend. Il s'agit du fichier principal de l'application Express.js, qui configure le middleware, établit une connexion à MongoDB et configure les routes API pour l'authentification et la gestion des tâches.

```javascript
const express = require('express');

const mongoose = require('mongoose');

const dotenv = require('dotenv');

const cookieParser = require('cookie-parser');

const helmet = require('helmet');

const authRoutes = require('./routes/authRoutes');

const taskRoutes = require('./routes/taskRoutes');

const { notFound, errorHandler } = require('./middleware/errorMiddleware');

dotenv.config();


const app = express();

app.use(helmet());

app.use(express.json());

app.use(cookieParser());


mongoose.connect(process.env.MONGO_URI)

  .then(() => console.log('MongoDB connected!'))

  .catch(err => console.error('MongoDB connection error:', err));


app.use('/api/auth', authRoutes);

app.use('/api/tasks', taskRoutes);


app.get('/', (req, res) => {

  res.send('MERN Task Manager API is running!');

});


app.use(notFound);

app.use(errorHandler);


const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {

  console.log(`Server running on port ${PORT}`);

});

```

#### server/.env

Pour éviter de coder en dur les secrets, nous allons ajouter un fichier `.env` où nous pouvons stocker en toute sécurité les variables d'environnement, telles que notre URI de base de données et notre secret JWT. Ce fichier stocke les variables d'environnement sensibles telles que votre chaîne de connexion MongoDB, le port du serveur et le secret JWT, les gardant sécurisées et séparées de votre base de code.

```bash
MONGO_URI=your_mongodb_connection_string_here

PORT=5000

JWT_SECRET=supersecretjwtkey
```

#### server/models/User.js

Maintenant, définissons notre modèle User en utilisant MongoDB. Ce schéma inclut des champs pour le nom d'utilisateur, l'email et le mot de passe, avec des hooks pré-sauvegarde pour le hachage du mot de passe et une méthode pour la comparaison des mots de passe.

```javascript
const mongoose = require('mongoose');

const bcrypt = require('bcryptjs');


const UserSchema = new mongoose.Schema({

  username: {

    type: String,

    required: true,

    unique: true,

  },

  email: {

    type: String,

    required: true,

    unique: true,

  },

  password: {

    type: String,

    required: true,

  },

});

UserSchema.pre('save', async function (next) {

  if (!this.isModified('password')) {

    next();

  }

  const salt = await bcrypt.genSalt(10);

  this.password = await bcrypt.hash(this.password, salt);

});


UserSchema.methods.matchPassword = async function (enteredPassword) {

  return await bcrypt.compare(enteredPassword, this.password);

};


module.exports = mongoose.model('User', UserSchema);

```

#### server/models/Task.js

Ensuite, nous allons créer le modèle Task. Ce schéma définit le modèle Task, qui lie chaque tâche à un utilisateur et inclut des champs pour le titre, la description, l'état d'achèvement et l'horodatage de création.

```javascript
const mongoose = require('mongoose');


const TaskSchema = new mongoose.Schema({

  user: {

    type: mongoose.Schema.Types.ObjectId,

    ref: 'User',

    required: true,

  },

  title: {

    type: String,

    required: true,

    trim: true,

  },

  description: {

    type: String,

    trim: true,

  },

  completed: {

    type: Boolean,

    default: false,

  },

  createdAt: {

    type: Date,

    default: Date.now,

  },

});


module.exports = mongoose.model('Task', TaskSchema);

```

#### server/controllers/authController.js

Construisons maintenant le contrôleur d'authentification. Ce contrôleur gère les flux d'authentification des utilisateurs, y compris l'inscription, la connexion, la déconnexion et la récupération des profils utilisateurs, en utilisant des JWT et des cookies sécurisés HTTP-only.

```javascript
const User = require('../models/User');

const jwt = require('jsonwebtoken');

const generateToken = (id) => {

  return jwt.sign({ id }, process.env.JWT_SECRET, {

    expiresIn: '1h',

  });

};

exports.registerUser = async (req, res) => {

  const { username, email, password } = req.body;

  try {

    const userExists = await User.findOne({ email });

    if (userExists) return res.status(400).json({ message: 'User already exists' });

    const user = await User.create({ username, email, password });

    if (user) {

      const token = generateToken(user._id);

      res.cookie('token', token, { httpOnly: true, secure: process.env.NODE_ENV === 'production', maxAge: 3600000 });

      res.status(201).json({ id: user.id, username: user.username, email: user.email });

    } else {

      res.status(400).json({ message: 'Invalid user data' });

    }

  } catch (error) {

    res.status(500).json({ message: error.message });

  }

};


exports.loginUser = async (req, res) => {

  const { email, password } = req.body;

  try {

    const user = await User.findOne({ email });

    if (user && (await user.matchPassword(password))) {

      const token = generateToken(user._id);

      res.cookie('token', token, { httpOnly: true, secure: process.env.NODE_ENV === 'production', maxAge: 3600000 });

      res.json({ id: user.id, username: user.username, email: user.email });

    } else {

      res.status(401).json({ message: 'Invalid email or password' });

    }

  } catch (error) {

    res.status(500).json({ message: error.message });

  }

};


exports.logoutUser = (req, res) => {

  res.cookie('token', '', { httpOnly: true, expires: new Date(0) });

  res.status(200).json({ message: 'Logged out successfully' });

};


exports.getUserProfile = async (req, res) => {

  try {

    const user = await User.findById(req.user._id).select('-password');

    if (user) {

      res.json(user);

    } else {

      res.status(404).json({ message: 'User not found' });

    }

  } catch (error) {

    res.status(500).json({ message: error.message });

  }

};

```

#### server/controllers/taskController.js

Il est maintenant temps d'implémenter le contrôleur de tâches. Ce contrôleur fournit la logique pour récupérer, créer, mettre à jour et supprimer des tâches, en s'assurant que les utilisateurs ne peuvent interagir qu'avec leurs propres tâches.

```javascript
const Task = require('../models/Task');


exports.getTasks = async (req, res) => {

  try {

    const tasks = await Task.find({ user: req.user._id });

    res.status(200).json(tasks);

  } catch (error) {

    res.status(500).json({ message: error.message });

  }

};


exports.createTask = async (req, res) => {

  const { title, description } = req.body;

  if (!title) return res.status(400).json({ message: 'Please add a title' });

  try {

    const task = await Task.create({ title, description, user: req.user._id });

    res.status(201).json(task);

  } catch (error) {

    res.status(500).json({ message: error.message });

  }

};


exports.updateTask = async (req, res) => {

  try {

    const task = await Task.findById(req.params.id);

    if (!task) return res.status(404).json({ message: 'Task not found' });

    if (task.user.toString() !== req.user._id.toString()) return res.status(401).json({ message: 'Not authorized' });


    const updatedTask = await Task.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });

    res.status(200).json(updatedTask);

  } catch (error) {

    res.status(500).json({ message: error.message });

  }

};


exports.deleteTask = async (req, res) => {

  try {

    const task = await Task.findById(req.params.id);

    if (!task) return res.status(404).json({ message: 'Task not found' });

    if (task.user.toString() !== req.user._id.toString()) return res.status(401).json({ message: 'Not authorized' });


    await Task.deleteOne({ _id: req.params.id });

    res.status(200).json({ message: 'Task removed' });

  } catch (error) {

    res.status(500).json({ message: error.message });

  }

};

```

#### server/middleware/authMiddleware.js

Pour protéger les routes privées, nous allons créer un middleware qui vérifie le JWT à partir des cookies de la requête, garantissant que seuls les utilisateurs authentifiés peuvent accéder à des endpoints spécifiques.

```javascript
const jwt = require('jsonwebtoken');

const User = require('../models/User');

exports.protect = async (req, res, next) => {

  let token;

  if (req.cookies.token) {

    try {

      token = req.cookies.token;

      const decoded = jwt.verify(token, process.env.JWT_SECRET);

      req.user = await User.findById(decoded.id).select('-password');

      next();

    } catch (error) {

      res.status(401).json({ message: 'Not authorized, token failed' });

    }

  } else {

    res.status(401).json({ message: 'Not authorized, no token' });

  }

};

```

#### server/middleware/errorMiddleware.js

Pour gérer les erreurs de manière propre dans notre backend, nous allons ajouter un middleware de gestion des erreurs global qui peut gérer les erreurs 404 Not Found et fournir un mécanisme centralisé de gestion des erreurs pour des réponses d'erreur API cohérentes.

```javascript
exports.notFound = (req, res, next) => {

  const error = new Error(`Not Found - ${req.originalUrl}`);

  res.status(404);

  next(error);

};


exports.errorHandler = (err, req, res, next) => {

  const statusCode = res.statusCode === 200 ? 500 : res.statusCode;

  res.status(statusCode);

  res.json({

    message: err.message,

    stack: process.env.NODE_ENV === 'production' ? null : err.stack,

  });

};

```

#### server/routes/authRoutes.js

Définissons maintenant nos routes d'authentification. Ces endpoints permettent l'authentification des utilisateurs et mappent les méthodes HTTP à leurs fonctions de contrôleur correspondantes.

```javascript
const express = require('express');

const { registerUser, loginUser, logoutUser, getUserProfile } = require('../controllers/authController');

const { protect } = require('../middleware/authMiddleware');


const router = express.Router();


router.post('/register', registerUser);

router.post('/login', loginUser);

router.get('/logout', logoutUser);

router.get('/profile', protect, getUserProfile);


module.exports = router;
```

#### server/routes/taskRoutes.js

Maintenant, nous allons ajouter les routes pour les opérations de tâches. Ce fichier définit les routes API pour la gestion des tâches, en appliquant le middleware protect pour sécuriser toutes les opérations liées aux tâches.

```javascript
const express = require('express');

const { getTasks, createTask, updateTask, deleteTask } = require('../controllers/taskController');

const { protect } = require('../middleware/authMiddleware');

const router = express.Router();

router.route('/').get(protect, getTasks).post(protect, createTask);

router.route('/:id').put(protect, updateTask).delete(protect, deleteTask);

module.exports = router;
```

### Implémentation Frontend (React)

#### Dépendances

Maintenant, vous devrez initialiser un nouveau projet React et installer vos bibliothèques essentielles : Axios pour les requêtes HTTP, React Router pour la navigation, et React Toastify pour afficher les notifications.

```bash
npm install axios react-router-dom react-toastify
```

#### client/src/index.js

Commençons le frontend en configurant le point d'entrée. Ici, nous rendons le composant principal App et l'enveloppons avec AuthProvider pour fournir un contexte d'authentification globalement.

```javascript
import React from 'react';

import ReactDOM from 'react-dom/client';

import './index.css';

import App from './App';

import { AuthProvider } from './context/AuthContext';


const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(

  <React.StrictMode>

    <AuthProvider>

      <App />

    </AuthProvider>

  </React.StrictMode>

);
```

#### client/src/App.js

Ensuite, nous allons définir notre composant principal App. Cela configure le routage côté client pour l'application, et définit les routes publiques et privées, et inclut une barre de navigation et un système de notifications toast.

```javascript
import React from 'react';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import { ToastContainer } from 'react-toastify';

import 'react-toastify/dist/ReactToastify.css';


import Navbar from './components/Navbar';

import Register from './pages/Register';

import Login from './pages/Login';

import Dashboard from './pages/Dashboard';

import PrivateRoute from './components/PrivateRoute';


function App() {

  return (

    <Router>

      <Navbar />

      <ToastContainer />

      <div className="container">

        <Routes>

          <Route path="/register" element={<Register />} />

          <Route path="/login" element={<Login />} />

          <Route path="/dashboard" element={<PrivateRoute />}>

            <Route index element={<Dashboard />} />

          </Route>

          <Route path="/" element={<h1>Welcome to Task Manager!</h1>} />

        </Routes>

      </div>

    </Router>

  );

}

export default App;
```

#### client/src/context/AuthContext.js

Nous allons créer un contexte d'authentification qui gère l'état d'authentification global. Il fournit des fonctions pour la connexion, l'inscription et la déconnexion des utilisateurs, et charge automatiquement les données utilisateur au montage du composant.

```javascript
import React, { createContext, useState, useEffect } from 'react';

import axios from 'axios';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {

  const [user, setUser] = useState(null);

  const [loading, setLoading] = useState(true);


  useEffect(() => {

    const loadUser = async () => {

      try {

        const res = await axios.get('/api/auth/profile');

        setUser(res.data);

      } catch (err) {

        setUser(null);

      } finally {

        setLoading(false);

      }

    };

    loadUser();

  }, []);


  const login = async (email, password) => {

    try {

      const res = await axios.post('/api/auth/login', { email, password });

      setUser(res.data);

      return true;

    } catch (err) {

      console.error(err.response.data.message);

      return false;

    }

  };


  const register = async (username, email, password) => {

    try {

      const res = await axios.post('/api/auth/register', { username, email, password });

      setUser(res.data);

      return true;

    } catch (err) {

      console.error(err.response.data.message);

      return false;

    }

  };


  const logout = async () => {

    try {

      await axios.get('/api/auth/logout');

      setUser(null);

    } catch (err) {

      console.error(err);

    }

  };


  return (

    <AuthContext.Provider value={{ user, loading, login, register, logout }}>

      {children}

    </AuthContext.Provider>

  );

};


export default AuthContext;
```

#### client/src/components/Navbar.js

Voici un composant de barre de navigation dynamique qui affiche dynamiquement des liens en fonction de l'état d'authentification de l'utilisateur, montrant soit des options de connexion/inscription, soit un message de bienvenue et un bouton de déconnexion.

```javascript
import React, { useContext } from 'react';

import { Link } from 'react-router-dom';

import AuthContext from '../context/AuthContext';


const Navbar = () => {

  const { user, logout } = useContext(AuthContext);


  return (

    <nav>

      <h1>Task Manager</h1>

      <div>

        {user ? (

          <>

            <span>Welcome, {user.username}</span>

            <button onClick={logout}>Logout</button>

            <Link to="/dashboard">Dashboard</Link>

          </>

        ) : (

          <>

            <Link to="/login">Login</Link>

            <Link to="/register">Register</Link>

          </>

        )}

      </div>

    </nav>

  );

};


export default Navbar;

```

#### client/src/components/PrivateRoute.js

Pour protéger certaines pages, nous pouvons créer un composant Private Route. Il s'agit d'un garde pour les routes privées, garantissant que seuls les utilisateurs authentifiés peuvent y accéder et redirigeant les utilisateurs non authentifiés vers la page de connexion.

```javascript
import React, { useContext } from 'react';

import { Navigate, Outlet } from 'react-router-dom';

import AuthContext from '../context/AuthContext';


const PrivateRoute = () => {

  const { user, loading } = useContext(AuthContext);


  if (loading) {

    return <div>Loading...</div>; // Ou un spinner

  }


  return user ? <Outlet /> : <Navigate to="/login" replace />;

};

export default PrivateRoute;
```

#### client/src/pages/Register.js

Maintenant, créons le composant Register, qui fournit un formulaire d'inscription utilisateur, gère l'état des entrées et la soumission du formulaire, et affiche des messages de succès ou d'erreur à l'aide de notifications toast.

```javascript
import React, { useState, useContext } from 'react';

import { useNavigate } from 'react-router-dom';

import { toast } from 'react-toastify';

import AuthContext from '../context/AuthContext';


const Register = () => {

  const [username, setUsername] = useState('');

  const [email, setEmail] = useState('');

  const [password, setPassword] = useState('');

  const { register } = useContext(AuthContext);

  const navigate = useNavigate();


  const handleSubmit = async (e) => {

    e.preventDefault();

    const success = await register(username, email, password);

    if (success) {

      toast.success('Registration successful!');

      navigate('/dashboard');

    } else {

      toast.error('Registration failed. Please try again.');

    }

  };


  return (

    <div>

      <h2>Register</h2>

      <form onSubmit={handleSubmit}>

        <div>

          <label>Username:</label>

          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />

        </div>

        <div>

          <label>Email:</label>

          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />

        </div>

        <div>

          <label>Password:</label>

          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />

        </div>

        <button type="submit">Register</button>

      </form>

    </div>

  );

};


export default Register;
```

#### client/src/pages/Login.js

Maintenant, pour le formulaire de connexion, il fonctionne de manière similaire à la page d'inscription mais connecte les utilisateurs au système. Cette page gère les champs de saisie, traite les soumissions de formulaire et fournit un retour via des notifications toast.

```javascript
import React, { useState, useContext } from 'react';

import { useNavigate } from 'react-router-dom';

import { toast } from 'react-toastify';

import AuthContext from '../context/AuthContext';


const Login = () => {

  const [email, setEmail] = useState('');

  const [password, setPassword] = useState('');

  const { login } = useContext(AuthContext);

  const navigate = useNavigate();


  const handleSubmit = async (e) => {

    e.preventDefault();

    const success = await login(email, password);

    if (success) {

      toast.success('Login successful!');

      navigate('/dashboard');

    } else {

      toast.error('Login failed. Invalid credentials.');

    }

  };


  return (

    <div>

      <h2>Login</h2>

      <form onSubmit={handleSubmit}>

        <div>

          <label>Email:</label>

          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />

        </div>

        <div>

          <label>Password:</label>

          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />

        </div>

        <button type="submit">Login</button>

      </form>

    </div>

  );

};


export default Login;
```

#### client/src/pages/Dashboard.js

Enfin, nous allons construire la page Dashboard. Ce composant de tableau de bord affiche les tâches d'un utilisateur, lui permettant de créer de nouvelles tâches, de marquer les tâches comme complètes ou incomplètes, et de supprimer des tâches, avec des mises à jour en temps réel.

```javascript
import React, { useState, useEffect, useContext } from 'react';

import axios from 'axios';

import { toast } from 'react-toastify';

import AuthContext from '../context/AuthContext';


const Dashboard = () => {

  const { user } = useContext(AuthContext);

  const [tasks, setTasks] = useState([]);

  const [newTaskTitle, setNewTaskTitle] = useState('');

  const [newTaskDescription, setNewTaskDescription] = useState('');


  useEffect(() => {

    if (user) {

      fetchTasks();

    }

  }, [user]);


  const fetchTasks = async () => {

    try {

      const res = await axios.get('/api/tasks');

      setTasks(res.data);

    } catch (err) {

      toast.error('Failed to fetch tasks.');

      console.error(err);

    }

  };


  const handleCreateTask = async (e) => {

    e.preventDefault();

    try {

      await axios.post('/api/tasks', { title: newTaskTitle, description: newTaskDescription });

      setNewTaskTitle('');

      setNewTaskDescription('');

      toast.success('Task created successfully!');

      fetchTasks();

    } catch (err) {

      toast.error('Failed to create task.');

      console.error(err);

    }

  };


  const handleUpdateTask = async (id, completed) => {

    try {

      await axios.put(`/api/tasks/${id}`, { completed });

      toast.success('Task updated successfully!');

      fetchTasks();

    } catch (err) {

      toast.error('Failed to update task.');

      console.error(err);

    }

  };


  const handleDeleteTask = async (id) => {

    try {

      await axios.delete(`/api/tasks/${id}`);

      toast.success('Task deleted successfully!');

      fetchTasks();

    } catch (err) {

      toast.error('Failed to delete task.');

      console.error(err);

    }

  };


  return (

    <div>

      <h2>Welcome, {user ? user.username : 'Guest'}!</h2>

      <h3>Your Tasks</h3>

      <form onSubmit={handleCreateTask}>

        <input

          type="text"

          placeholder="New Task Title"

          value={newTaskTitle}

          onChange={(e) => setNewTaskTitle(e.target.value)}

          required

        />

        <input

          type="text"

          placeholder="Description (optional)"

          value={newTaskDescription}

          onChange={(e) => setNewTaskDescription(e.target.value)}

        />

        <button type="submit">Add Task</button>

      </form>

      <ul>

        {tasks.map((task) => (

          <li key={task._id}>

            <span style={{ textDecoration: task.completed ? 'line-through' : 'none' }}>

              {task.title}: {task.description}

            </span>

            <button onClick={() => handleUpdateTask(task._id, !task.completed)}>

              {task.completed ? 'Mark Incomplete' : 'Mark Complete'}

            </button>

            <button onClick={() => handleDeleteTask(task._id)}>Delete</button>

          </li>

        ))}

      </ul>

    </div>

  );

};


export default Dashboard;
```

## **Déploiement : de Localhost à Live**

Le déploiement d'une application MERN implique de déployer l'API backend et l'application React frontend séparément.

Parlons de pourquoi nous le faisons séparément. Comme vous l'avez vu ci-dessus, dans une application MERN, le frontend et le backend sont séparés par conception. React gère l'interface utilisateur, tandis qu'Express et Node gèrent la logique serveur et les appels API. Parce qu'ils servent des rôles différents, vous devrez les déployer séparément.

Le backend s'exécute sur un serveur compatible Node.js, qui se connecte à une base de données telle que MongoDB Atlas. Le frontend, une fois construit, devient des fichiers statiques qui peuvent être hébergés n'importe où, d'NGINX aux plateformes d'hébergement comme Netlify ou Vercel.

Cette séparation vous offre flexibilité et amélioration de la scalabilité. Passons en revue comment déployer chaque partie.

### **Déploiement Backend (Node.js/Express.js)**

Pour le déploiement backend, des plateformes comme Heroku, Render ou AWS EC2 sont des choix courants. Ici, je vais décrire une approche générale pour une VM cloud sur AWS EC2

#### 1. Préparation pour la production

Pour commencer, définissez l'environnement sur `production` et installez uniquement les dépendances dont votre application a besoin pour fonctionner, optimisant ainsi les performances de votre application. Sauter les devDependencies aide à réduire son empreinte.

```bash
export NODE_ENV=production

npm install --production
```

#### 2. Gestionnaire de processus (PM2)

Ensuite, nous allons configurer un gestionnaire de processus pour maintenir notre serveur backend en fonctionnement de manière fiable. PM2 est un outil populaire qui gère les redémarrages automatiques si votre application Node.js plante, gère plusieurs instances d'application et aide également à garantir une haute disponibilité dans les environnements de production.

```bash
npm install -g pm2

pm2 start server/app.js --name mern-api

pm2 save

pm2 startup
```

#### 3. NGINX comme proxy inverse

Maintenant que notre backend fonctionne avec PM2, nous avons besoin d'un moyen de gérer le trafic web entrant. C'est là qu'intervient NGINX. Nous allons installer NGINX pour servir de proxy inverse haute performance dirigeant le trafic web entrant vers votre backend Node.js et servant les fichiers statiques du frontend.

```bash
sudo apt update

sudo apt install nginx
```

Une fois NGINX installé, il est temps de le configurer (/etc/nginx/sites-available/default ou un nouveau fichier de configuration). Nous allons le configurer pour transférer les requêtes API au backend et servir l'application React, agissant comme le point d'entrée unique. Vous pouvez mettre à jour le fichier de configuration par défaut ou en créer un nouveau :

```nginx
# /etc/nginx/sites-available/default
server {

  listen 80;

  server_name your_domain_or_ip;


  location /api/ {

    proxy_pass http://localhost:5000;

    proxy_http_version 1.1;

    proxy_set_header Upgrade $http_upgrade;

    proxy_set_header Connection 'upgrade';

    proxy_set_header Host $host;

    proxy_cache_bypass $http_upgrade;

  }


  location / {

    root /var/www/my-mern-app/client/build; # Chemin vers votre dossier de build React

    try_files $uri /index.html;

  }

}
```

Avec la configuration NGINX créée, nous allons l'activer et redémarrer le service pour appliquer les modifications, rendant votre application accessible en ligne :

```bash
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

sudo systemctl restart nginx
```

#### 4. HTTPS avec Certbot (Let's Encrypt)

Pour sécuriser votre application avec HTTPS, nous pouvons installer Certbot et l'utiliser pour obtenir et configurer automatiquement un certificat SSL/TLS gratuit de Let's Encrypt, permettant des connexions HTTPS sécurisées pour votre domaine.

```bash
sudo snap install --classic certbot

sudo certbot --nginx -d your_domain_or_ip
```

### **Déploiement Frontend (React)**

Avec le backend déployé, passons au frontend. Pour le frontend React, nous allons construire l'application et servir les fichiers statiques via NGINX (comme montré ci-dessus) ou un site statique dédié hébergé sur des plateformes comme Netlify, Vercel ou AWS S3 + CloudFront.

#### Construire l'application React

Cette commande compile et optimise votre application React dans un dossier build contenant des actifs statiques, prêts pour un déploiement efficace sur n'importe quel serveur web ou service d'hébergement statique.

```bash
cd client

npm run build
```

### **Déploiement de la base de données (MongoDB Atlas)**

Pour la production, nous allons utiliser un service MongoDB géré comme MongoDB Atlas. Il gère la réplication, le sharding et les sauvegardes, simplifiant considérablement la gestion de la base de données.

#### Créer un cluster sur MongoDB Atlas

* Inscrivez-vous/Connectez-vous à MongoDB Atlas.
    
* Créez un nouveau cluster (choisissez un fournisseur cloud et une région).
    
* Configurez un utilisateur de base de données avec les permissions appropriées.
    
* Configurez l'accès réseau (autorisez les connexions depuis l'adresse IP de votre serveur).
    
* Obtenez votre chaîne de connexion et mettez à jour MONGO_URI dans votre fichier server/.env.
    

#### 1. Exemple de configuration .env

Après avoir créé le cluster et l'utilisateur dans MongoDB Atlas, vous recevrez une chaîne de connexion. Vous devez mettre à jour votre fichier .env avec celle-ci

```ini
# server/.env
MONGO_URI=mongodb+srv://yourUser:yourPassword@cluster0.mongodb.net/yourDBName
JWT_SECRET=your_secret_jwt_key
NODE_ENV=production
```

#### 2. Connexion à MongoDB dans app.js

Ensuite, dans le fichier server/app.js, assurez-vous d'utiliser la chaîne de connexion de la variable d'environnement :

```javascript
const mongoose = require('mongoose');
const dotenv = require('dotenv');
dotenv.config();

mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('MongoDB connected!'))
  .catch((err) => console.error('Connection error:', err));
```

### **Autres options de déploiement**

Bien que cet article vous guide à travers un déploiement manuel avec EC2 et NGINX, d'autres plateformes peuvent simplifier le processus :

* **Render**, **Railway** et **Heroku** offrent un déploiement full-stack facile avec intégration GitHub.
    
* **Vercel** et **Netlify** sont idéaux pour héberger le frontend React.
    
* Vous pouvez envisager d'utiliser **Docker** pour maintenir des environnements cohérents entre le développement et la production.
    
* Pour CI/CD, le Linting, les Tests et le Déploiement peuvent être automatisés à chaque push en utilisant des outils comme **GitHub Actions**
    

Il n'y a pas de bon ou de mauvais choix ici. Sélectionnez la configuration qui convient le mieux à l'échelle de votre projet, à l'expérience de votre équipe et au niveau de contrôle souhaité.

## **Bonnes pratiques de sécurité : renforcer votre application**

La sécurité est primordiale. Vous pouvez implémenter ces bonnes pratiques pour protéger votre application MERN.

### **Configuration de la validation et de la sanitisation des entrées**

Validez et sanitisez toujours les entrées côté serveur. Vous pouvez utiliser des bibliothèques comme Joi ou Zod pour faciliter ce processus.

#### Exemple avec Joi :

Pour valider et sanitiser les données entrantes sur le serveur, nous allons utiliser Joi, une bibliothèque puissante pour définir des schémas et imposer des règles d'entrée.

```bash
npm install joi
```

Maintenant que nous avons installé Joi, nous allons l'utiliser pour définir des règles de validation strictes pour les entrées d'inscription et de connexion des utilisateurs. Cela garantit la qualité des données et empêche les attaques par injection courantes.

```javascript
// server/validators/authValidator.js

const Joi = require('joi');


const registerSchema = Joi.object({

  username: Joi.string().min(3).max(30).required(),

  email: Joi.string().email().required(),

  password: Joi.string().min(6).required(),

});


const loginSchema = Joi.object({

  email: Joi.string().email().required(),

  password: Joi.string().required(),

});


module.exports = { registerSchema, loginSchema };

```

Ensuite, nous allons intégrer ces schémas directement dans notre contrôleur d'authentification pour valider automatiquement les corps de requête entrants par rapport aux schémas prédéfinis.

```javascript
// server/controllers/authController.js (extrait)

const { registerSchema, loginSchema } = require('../validators/authValidator');


exports.registerUser = async (req, res) => {

  const { error } = registerSchema.validate(req.body);

  if (error) return res.status(400).json({ message: error.details[0].message });

  // ... reste de la logique d'inscription

};


exports.loginUser = async (req, res) => {

  const { error } = loginSchema.validate(req.body);

  if (error) return res.status(400).json({ message: error.details[0].message });

  // ... reste de la logique de connexion

};

```

### **Ajouter l'authentification et l'autorisation**

Vous pouvez utiliser des JWT pour l'authentification et implémenter un middleware pour les routes protégées.

#### Implémentation JWT (couvert dans authController.js et authMiddleware.js ci-dessus)

Aspects clés :

* Cookies HttpOnly : Stockez les JWT dans des cookies HttpOnly pour empêcher l'accès côté client JavaScript, atténuant les attaques XSS.
    
* Flag Secure : Utilisez secure: true en production pour garantir que les cookies ne sont envoyés que via HTTPS.
    

Ces pratiques garantissent que les jetons d'authentification sont transmis et stockés de manière sécurisée, protégeant contre les vulnérabilités web courantes comme le Cross-Site Scripting (XSS).

### **Implémenter la limitation de débit**

Pour protéger notre API contre les abus et les intentions malveillantes, nous allons implémenter une limitation de débit de base. Cela aide à protéger contre les tentatives de connexion par force brute et les attaques DDoS.

#### Installation

Nous allons installer le package express-rate-limit pour cela

```bash
npm install express-rate-limit
```

#### server/app.js (extrait)

Une fois installé, configurons le limiteur de débit et appliquons-le à toutes les requêtes entrantes. Cela garantit qu'aucune IP unique ne peut submerger votre serveur avec des appels répétés. Le middleware suivant limite chaque adresse IP à 200 requêtes dans une fenêtre de 15 minutes.

```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({

  windowMs: 15 * 60 * 1000, // 15 minutes

  max: 200, // Limite chaque IP à 200 requêtes par windowMs

  message: 'Too many requests from this IP, please try again after 15 minutes',

});

app.use(limiter); // Appliquer à toutes les requêtes
```

### **Configuration CORS (Cross-Origin Resource Sharing)**

Ensuite, nous nous concentrons sur l'activation de la communication sécurisée entre votre frontend et votre backend. Par défaut, tous les navigateurs bloquent les requêtes cross-origin, nous devons donc configurer CORS (Cross-Origin Resource Sharing) pour permettre à l'application React de communiquer avec l'API Express.

#### Installation

```bash
npm install cors
```

#### server/app.js (extrait)

Une fois installé, nous pouvons configurer CORS pour notre application Express, en spécifiant les origines autorisées et en activant le partage des informations d'identification pour les requêtes cross-origin sécurisées. N'oubliez pas de remplacer l'origine par votre URL de production réelle lors du déploiement.

```javascript
const cors = require('cors');

app.use(cors({

  origin: 'http://localhost:3000', // Remplacez par votre URL frontend en production

  credentials: true,

}));
```

### **Utiliser les variables d'environnement**

Pour garder les informations sensibles sécurisées et hors de votre base de code, nous allons utiliser des variables d'environnement. Cela nous permet de gérer efficacement les secrets, tels que les chaînes de connexion à la base de données et les clés JWT, sans les coder en dur ou les inclure dans le code source.

Créez un fichier `.env` dans votre répertoire `server/` :

#### .env (exemple)

Ce fichier .env stocke les détails de configuration sensibles comme les chaînes de connexion à la base de données et les clés API

```ini
MONGO_URI=your_mongodb_connection_string

JWT_SECRET=your_super_secret_jwt_key

NODE_ENV=production
```

## **Surveillance et journalisation avec Winston et Morgan**

Une fois l'application en ligne, il est crucial de surveiller le comportement et de détecter rapidement les problèmes. La surveillance et la journalisation vous aident à mesurer les performances, à trouver les bugs et à conserver un journal de toute l'activité du serveur.

Nous utiliserons Morgan pour journaliser les requêtes HTTP et Winston pour une journalisation plus générale de l'application.

### Installation

Nous allons installer Morgan pour journaliser les requêtes HTTP et Winston pour une journalisation complète et personnalisable de l'application.

```bash
npm install morgan winston
```

### server/config/logger.js

Ensuite, configurons Winston pour gérer nos journaux d'application. Cela affichera les journaux sur la console par défaut, avec des options pour activer la journalisation basée sur des fichiers pour les erreurs et les informations générales.

```javascript
const winston = require('winston');

const logger = winston.createLogger({

  level: 'info',

  format: winston.format.combine(

    winston.format.timestamp(),

    winston.format.json()

  ),

  transports: [

    new winston.transports.Console(),

    // new winston.transports.File({ filename: 'error.log', level: 'error' }),

    // new winston.transports.File({ filename: 'combined.log', level: 'info' }),

  ],

});

module.exports = logger;
```

### server/app.js (extrait)

Avec Winston et Morgan configurés, intégrons-les maintenant dans notre fichier `app.js`. Nous utiliserons Morgan pour la journalisation des requêtes pendant le développement et remplacerons les appels standard `console.log` par des logs Winston pour une journalisation structurée et configurable de l'application.

```javascript
const morgan = require('morgan');

const logger = require('./config/logger');

if (process.env.NODE_ENV === 'development') {

  app.use(morgan('dev'));

}

// Remplacer console.log par logger.info pour la connexion à la base de données

mongoose.connect(process.env.MONGO_URI)

  .then(() => logger.info('MongoDB connected!'))

  .catch(err => logger.error('MongoDB connection error:', err));


// Remplacer console.log dans app.listen

app.listen(PORT, () => {

  logger.info(`Server running on port ${PORT}`);

});
```

### **Surveillance des erreurs frontend (Sentry)**

Pour surveiller les erreurs dans le frontend, nous allons intégrer Sentry. C'est un outil fantastique pour suivre les exceptions et les problèmes de performance en temps réel. Il nous aide à capturer et à signaler les erreurs côté client.

#### Installation

```bash
npm install @sentry/react @sentry/tracing
```

#### client/src/index.js (extrait)

Après l'installation, initialisons Sentry dans l'application React afin qu'il puisse automatiquement capturer les erreurs et les données de performance. Nous allons ajouter cela à notre fichier `index.js`.

```javascript
import * as Sentry from '@sentry/react';

import { BrowserTracing } from '@sentry/tracing';


Sentry.init({

  dsn: "YOUR_SENTRY_DSN", // Remplacez par votre DSN Sentry

  integrations: [new BrowserTracing()],

  tracesSampleRate: 1.0,

  environment: process.env.NODE_ENV,

});
```

Et c'est tout ! Félicitations pour avoir construit et déployé une application full-stack MERN.

## **Conclusion**

Cet article a fourni un guide pratique axé sur le code pour construire, sécuriser et déployer une application MERN. En se concentrant sur des exemples de code pratiques et des configurations essentielles, vous disposez maintenant d'une base solide pour vos projets MERN.

N'oubliez pas que l'apprentissage continu et l'adaptation sont essentiels dans le monde en constante évolution du développement web. Bon codage !