---
title: Comment créer des animations multi-pages avec Framer Motion et React-Router-Dom
subtitle: ''
author: Okosa Leonard
co_authors: []
series: null
date: '2024-06-17T05:57:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-multi-page-animations-using-framer-motion-and-react-router-dom
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Green-Abstract-Wavy-Background-Motivational-Quote-Facebook-Post.png
tags:
- name: React
  slug: react
- name: react router
  slug: react-router
seo_title: Comment créer des animations multi-pages avec Framer Motion et React-Router-Dom
seo_desc: 'Animations are what make plain websites turn into exciting and unforgettable
  experiences. They give your website a bit of personality and uniqueness and leave
  the visitor admiring the overall aesthetic.

  It''s a no-brainer that humans love beautiful th...'
---

Les animations sont ce qui transforme les sites web ordinaires en expériences passionnantes et mémorables. Elles donnent à votre site web un peu de personnalité et d'unicité et laissent le visiteur admirer l'esthétique globale.

Il est évident que les humains aiment les belles choses. Nous aimons tous les produits qui sont agréables à regarder.

Dans cet article, nous allons apprendre à créer des animations qui impressionnent les utilisateurs avec l'utilisation de Framer Motion et React-Router-Dom.

## Prérequis

Pour pouvoir suivre ce que nous faisons dans cet article, vous devez avoir quelques connaissances sur [React](https://react.dev/), [Framer Motion](https://www.framer.com/motion/) et [React-Router-DOM](https://reactrouter.com/).

Pour mieux apprendre Framer Motion, vous pouvez étudier leur documentation.

[Node.js](https://nodejs.org/en/download/package-manager) doit également être installé sur votre système, et vous devez avoir un éditeur de code fonctionnel. J'utiliserai [VS Code](https://code.visualstudio.com/).

## Comment configurer le projet

Pour configurer notre projet, nous allons utiliser Vite pour configurer notre environnement de développement React.

1. Ouvrez le terminal dans VS Code. Vous pouvez utiliser Ctrl + backtick(\`)
    
2. Dans votre terminal, entrez la commande suivante :
    

```plaintext
npm create vite@latest
```

3. Suivez les invites pour nommer votre projet et choisir le framework souhaité. Dans notre cas, nous utilisons React. Ce sera un projet JavaScript.
    
4. Allez dans votre répertoire de projet et utilisez `npm i` dans le terminal.
    
5. Pour démarrer votre projet, utilisez `npm run dev`.
    
6. N'oubliez pas de nettoyer votre projet en supprimant le code dans App.js et vos fichiers CSS dans le dossier `src`.
    

## Comment initialiser Framer Motion et React-Router-Dom

1. Pour installer Framer-Motion dans votre projet, ouvrez le terminal et entrez :
    

```plaintext
npm i framer-motion
```

2. Pour installer React-Router-DOM dans votre projet, ouvrez le terminal et entrez :
    

```plaintext
npm i react-router-dom
```

## Comment configurer les composants et le routage de base avec React-Router-DOM

Configurons nos composants et les pages vers lesquelles nous allons router pour ce projet.

1. Dans `src`, créez un nouveau dossier nommé `components`.
    
2. Nous allons ajouter quatre fichiers dans ce dossier nommés `Home.jsx`, `About.jsx`, `Projects.jsx` et `Navbar.jsx`.
    
3. Dans les trois premiers, nous allons créer un composant fonctionnel React. Changez le contenu de la balise `h1` dans chaque composant :
    

```jsx
const Home = () => {
 return (
    <div>
     <h1>Accueil</h1>
    </div>
 )
 }
 
 export default Home
```

4. Dans la Navbar, nous devons importer `Link` depuis React-Router-DOM pour créer des éléments d'ancrage. Nous devons ensuite créer un conteneur abritant notre logo et les liens de navigation. Le logo liera les points à notre page d'index.
    

```javascript
import {Link} from "react-router-dom"

const Navbar = () => {
 return (
     <div className="nav">
      <div className="logo">
         <Link className="nav-link" to="/">Lennythedev</Link>
     </div>
     <div>
        <div className="nav-links">
           <div className="nav-item">
            <Link className="nav-link" to="/">Accueil</Link>
           </div>
           <div className="nav-item">
            <Link className="nav-link" to="/about">À propos</Link>
           </div>
           <div className="nav-item">
            <Link className="nav-link" to="/projects">Projets</Link>
           </div>
     </div>
     </div>
     </div>
  )
 }

export default Navbar
```

5. Maintenant, allons dans notre fichier `index.js` ou `main.js`. Le but est d'envelopper toute notre application avec `BrowserRouter` qui permettra le routage dans notre application.
    

```javascript
import React from "react"
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path='/*' element={<App />} />
      </Routes>
    </Router>
  </React.StrictMode>,
)
```

6. Maintenant, dans `App.js`, nous allons compléter la dernière étape de notre configuration. Nous allons importer nos composants et certaines fonctionnalités de React-Router-DOM et rendre nos composants. En utilisant la fonctionnalité `useLocation` de React-Router-DOM, nous pouvons définir l'emplacement actuel des routes en définissant la clé sur le chemin actuel.
    

```javascript
import './App.css'
import { Routes, Route, useLocation } from 'react-router-dom'
import NavBar from './components/NavBar';
import Home from './components/Home';
import Projects from './components/Projects';
import About from './components/About';
import { AnimatePresence } from 'framer-motion';

function App() {
  const location = useLocation();
  return (
    <>
       <NavBar />
       <AnimatePresence mode='wait'>
       <Routes location={location} key={location.pathname}>
        <Route index element={<Home />} />
        <Route path='/projects' element={<Projects />}/>
        <Route path='/about' element={<About />}/>
       </Routes>
       </AnimatePresence>
    </>
  )
}

export default App
```

7. Maintenant, nous pouvons ajouter notre style dans `App.css` :
    

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  color: white;
  font-family: "Fira Sans Condensed", sans-serif;
}

html,
body {
  font-family: "Fira Sans Condensed", sans-serif;
  background: rgb(0, 162, 255);
}

.nav {
  position: fixed;
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.nav-links {
  display: flex;
  cursor: pointer;
}

.logo, .nav-item {
  margin: 2em;
  font-weight: 400;
  font-size: 1.5vw;
}

h1{
  width: 80%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  font-weight: 500;
  font-size: 10vw;
  line-height: 1;
  text-transform: uppercase;
}

a {
  text-decoration: none;
  font-weight: 500;
}
```

8. Après avoir suivi toutes les étapes, votre application devrait ressembler à ceci :
    

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Annotation-2024-06-14-200041.png align="left")

*page web stylisée sans animation*

## Comment créer des transitions avec Framer Motion

Enfin, créons notre animation pour les transitions entre les pages.

1. Créez un fichier dans les composants nommé `Box.jsx` et `import motion from framer-motion`.
    
2. Nous pouvons ensuite retourner deux divs, avec des `classNames` de `slide-in` et `slide-out`, une pour l'entrée et une autre pour la sortie.
    
3. Nous insérons notre animation dans ces divs avec l'aide de framer-motion :
    

```javascript
import { motion } from "framer-motion"

export default function Box() {
  return(
    <div>
     <motion.div
        className="slide-in"
        initial={{ scaleY: 0 }}
        animate={{ scaleY: 0 }}
        exit={{ scaleY: 1 }}
        transition={{ duration: 1, ease: [0.22, 1, 0.36, 1] }}
     />
     <motion.div
     className="slide-out"
        initial={{ scaleY: 1 }}
        animate={{ scaleY: 0 }}
        exit={{ scaleY: 0 }}
        transition={{ duration: 1, ease: [0.22, 1, 0.36, 1] }}
     />
    </div>
  )
}
```

4. Ensuite, nous ajoutons notre style dans notre fichier CSS pour `slide-in` et `slide-out` dans notre App.css
    

```css
.slide-in {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background: #0f0f0f;
  transform-origin: bottom;
}

.slide-out {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  background: #0f0f0f;
  transform-origin: top;
}
```

5. Enfin, la dernière étape consiste à utiliser `AnimatePresence` de framer-motion dans notre fichier `App.js` et à envelopper toute l'application dans `AnimatePresence` et à définir le mode comme wait. Si vous voulez en savoir plus sur `AnimatePresence`, visitez la documentation de framer-motion.
    

```javascript
import './App.css'
import { Routes, Route, useLocation } from 'react-router-dom'
import NavBar from './components/NavBar';
import Home from './components/Home';
import Projects from './components/Projects';
import About from './components/About';
import { AnimatePresence } from 'framer-motion';

function App() {
  const location = useLocation();
  return (
    <>
       <NavBar />
       <AnimatePresence mode='wait'>
       <Routes location={location} key={location.pathname}>
        <Route index element={<Home />} />
        <Route path='/projects' element={<Projects />}/>
        <Route path='/about' element={<About />}/>
       </Routes>
       </AnimatePresence>
    </>
  )
}

export default App
```

6. Enfin, notre travail devrait ressembler à la vidéo ci-dessous :
    

%[https://youtu.be/Sb1txpdycpA?si=LagMe6asQhVYr6te] 

## Conclusion

Créer des animations multi-pages avec Framer Motion et React-Router-Dom améliore l'expérience utilisateur en fournissant des transitions fluides.

Cette intégration exploite la puissance des capacités d'animation de Framer Motion avec les fonctionnalités de routage de React-Router-Dom, résultant en des applications web dynamiques et interactives.