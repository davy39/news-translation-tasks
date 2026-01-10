---
title: Complexité de l'état partagé dans React – Un guide complet pour les développeurs
subtitle: ''
author: Henry Adepegba
co_authors: []
series: null
date: '2025-07-31T23:29:21.508Z'
originalURL: https://freecodecamp.org/news/shared-state-complexity-in-react-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1754003865317/3c91ac36-2e1b-4e03-ac54-64a100e44c8f.png
tags:
- name: '#reactstate'
  slug: reactstate
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: 'State Management '
  slug: state-management
- name: handbook
  slug: handbook
seo_title: Complexité de l'état partagé dans React – Un guide complet pour les développeurs
seo_desc: 'Imagine you''re building a simple shopping website. You have a product
  page where users can add items to their cart, and a header that displays the number
  of items in the cart. Sounds simple, right? But here''s the challenge: how does
  the header know w...'
---

Imaginez que vous construisez un simple site de shopping. Vous avez une page produit où les utilisateurs peuvent ajouter des articles à leur panier, et un en-tête qui affiche le nombre d'articles dans le panier. Cela semble simple, n'est-ce pas ? Mais voici le défi : **comment l'en-tête sait-il quand quelqu'un ajoute un article sur une partie complètement différente de la page ?**

C'est le **problème de l'état partagé**, qui se produit lorsque différentes parties de votre application doivent accéder et mettre à jour les mêmes informations. Dans les petites applications, ce n'est pas un gros problème. Mais à mesure que votre application grandit, la gestion de l'état partagé devient l'une des parties les plus complexes et frustrantes du développement React.

Dans ce guide, vous apprendrez :

* Ce que sont les props et le prop drilling, et pourquoi ils deviennent problématiques

* Comment reconnaître quand vous avez un problème d'état partagé

* Plusieurs solutions pour gérer efficacement l'état partagé

* Quand utiliser chaque solution

* Comment éviter les erreurs courantes que même les développeurs expérimentés commettent

À la fin, vous comprendrez comment construire des applications React qui restent organisées et maintenables à mesure qu'elles grandissent.

### Ce que nous allons couvrir :

* [Ce que nous allons couvrir :](#heading-ce-que-nous-allons-couvrir)

* [Prérequis : Ce que vous devez savoir avant de lire ce guide](#heading-prérequis-ce-que-vous-devez-savoir-avant-de-lire-ce-guide)

  * [Connaissances essentielles de React](#heading-connaissances-essentielles-de-react)

  * [Prérequis JavaScript](#heading-prérequis-javascript)

  * [Concepts React que vous rencontrerez](#heading-concepts-react-que-vous-rencontrerez)

* [Environnement de développement](#heading-environnement-de-développement)

* [Compréhension conceptuelle](#heading-compréhension-conceptuelle)

* [Ce que vous n'avez PAS besoin de savoir](#heading-ce-que-vous-navez-pas-besoin-de-savoir)

* [Questions d'auto-évaluation](#heading-questions-dauto-évaluation)

* [Préparation recommandée](#heading-préparation-recommandée)

* [Ce que ce guide vous apprendra](#heading-ce-que-ce-guide-vous-apprendra)

* [Comprendre les éléments de base : Props dans React](#heading-comprendre-les-éléments-de-base-props-dans-react)

  * [Que sont les props ?](#heading-que-sont-les-props)

  * [Une méthode plus moderne : Déstructuration des props](#heading-une-méthode-plus-moderne-déstructuration-des-props)

* [Qu'est-ce que le Prop Drilling et pourquoi est-ce un problème ?](#heading-quest-ce-que-le-prop-drilling-et-pourquoi-est-ce-un-problème)

  * [Un exemple simple : Passer un nom d'utilisateur](#heading-un-exemple-simple-passer-un-nom-dutilisateur)

  * [Un exemple réaliste : Prop drilling du panier d'achat](#heading-un-exemple-réaliste-prop-drilling-du-panier-dachat)

  * [Pourquoi cela se produit et empire](#heading-pourquoi-cela-se-produit-et-empire)

* [Solution 1 : React Context API – Comprendre le concept](#heading-solution-1-react-context-api-comprendre-le-concept)

  * [L'analogie de la station de radio](#heading-lanalogie-de-la-station-de-radio)

  * [Qu'est-ce que createContext() ?](#heading-quest-ce-que-createcontext)

  * [Créer un fournisseur de contexte de base](#heading-créer-un-fournisseur-de-contexte-de-base)

  * [Comprendre le hook useContext](#heading-comprendre-le-hook-usecontext)

  * [Créer un hook personnalisé pour une utilisation plus propre](#heading-créer-un-hook-personnalisé-pour-une-utilisation-plus-propre)

  * [Mettre tout ensemble : Exemple complet de contexte](#heading-mettre-tout-ensemble-exemple-complet-de-contexte)

* [Modèles et concepts avancés de contexte](#heading-modèles-et-concepts-avancés-de-contexte)

  * [Contexte multiple pour la séparation des préoccupations](#heading-contexte-multiple-pour-la-séparation-des-préoccupations)

  * [Comprendre useReducer pour la logique d'état complexe](#heading-comprendre-usereducer-pour-la-logique-détat-complexe)

* [Solution 2 : Bibliothèques de gestion d'état expliquées](#heading-solution-2-bibliothèques-de-gestion-détat-expliquées)

  * [Comprendre Redux : Le conteneur d'état prévisible](#heading-comprendre-redux-le-conteneur-détat-prévisible)

  * [Redux Toolkit : Redux moderne simplifié](#heading-redux-toolkit-redux-moderne-simplifié)

  * [Zustand : Gestion d'état simple et flexible](#heading-zustand-gestion-détat-simple-et-flexible)

* [Stratégies d'optimisation des performances expliquées](#heading-stratégies-doptimisation-des-performances-expliquées)

  * [Pourquoi les re-rendus inutiles se produisent-ils ?](#heading-pourquoi-les-re-rendus-inutiles-se-produisent-ils)

  * [Solution 1 : Diviser les contextes pour minimiser les re-rendus](#heading-solution-1-diviser-les-contextes-pour-minimiser-les-re-rendus)

  * [Solution 2 : Mémoïser les valeurs de contexte pour éviter la recréation d'objets](#heading-solution-2-mémoïser-les-valeurs-de-contexte-pour-éviter-la-recréation-dobjets)

  * [Solution 3 : Sélectionner uniquement ce dont vous avez besoin](#heading-solution-3-sélectionner-uniquement-ce-dont-vous-avez-besoin)

  * [Solution 4 : Utiliser React.memo pour les composants coûteux](#heading-solution-4-utiliser-reactmemo-pour-les-composants-coûteux)

  * [Solution 5 : Optimiser avec des hooks de sélecteur personnalisés](#heading-solution-5-optimiser-avec-des-hooks-de-sélecteur-personnalisés)

* [Test de l'état partagé : Une approche complète](#heading-test-de-létat-partagé-une-approche-complète)

  * [Pourquoi le test de l'état partagé est différent](#heading-pourquoi-le-test-de-létat-partagé-est-différent)

  * [Test du contexte React](#heading-test-du-contexte-react)

  * [Test des stores Redux](#heading-test-des-stores-redux)

* [Quand utiliser chaque approche : Un cadre de décision](#heading-quand-utiliser-chaque-approche-un-cadre-de-décision)

  * [Arbre de décision pour la gestion d'état](#heading-arbre-de-décision-pour-la-gestion-détat)

  * [Comparaison détaillée des approches](#heading-comparaison-détaillée-des-approches)

  * [Exemples concrets de quand utiliser chaque approche](#heading-exemples-concrets-de-quand-utiliser-chaque-approche)

* [Pièges courants et comment les éviter](#heading-pièges-courants-et-comment-les-éviter)

  * [Piège 1 : L'enfer du contexte (trop de fournisseurs imbriqués)](#heading-piège-1-lenfer-du-contexte-trop-de-fournisseurs-imbriqués)

  * [Piège 2 : Valeurs de contexte massives provoquant des re-rendus inutiles](#heading-piège-2-valeurs-de-contexte-massives-provoquant-des-re-rendus-inutiles)

  * [Piège 3 : Ne pas mémoïser les valeurs de contexte](#heading-piège-3-ne-pas-mémoïser-les-valeurs-de-contexte)

  * [Piège 4 : Prop drilling lorsque le contexte serait meilleur](#heading-piège-4-prop-drilling-lorsque-le-contexte-serait-meilleur)

  * [Piège 5 : Utiliser l'état global pour tout](#heading-piège-5-utiliser-létat-global-pour-tout)

  * [Piège 6 : Ne pas gérer les états de chargement et d'erreur dans l'état partagé](#heading-piège-6-ne-pas-gérer-les-états-de-chargement-et-derreur-dans-létat-partagé)

* [Meilleures pratiques pour un état partagé maintenable](#heading-meilleures-pratiques-pour-un-état-partagé-maintenable)

  * [1. Utiliser des conventions de nommage cohérentes](#heading-1-utiliser-des-conventions-de-nommage-cohérentes)

  * [2. Regrouper l'état et les actions liés](#heading-2-regrouper-létat-et-les-actions-liés)

  * [3. Créer des hooks de sélecteur pour un accès complexe aux données](#heading-3-créer-des-hooks-de-sélecteur-pour-un-accès-complexe-aux-données)

  * [4. Gérer correctement les effets secondaires](#heading-4-gérer-correctement-les-effets-secondaires)

  * [5. Implémenter des limites d'erreur appropriées](#heading-5-implémenter-des-limites-derreur-appropriées)

* [Conclusion : Construire des applications React maintenables](#heading-conclusion-construire-des-applications-react-maintenables)

  * [Résumé des approches](#heading-résumé-des-approches)

  * [Principes clés à retenir](#heading-principes-clés-à-retenir)

  * [L'évolution d'une application typique](#heading-lévolution-dune-application-typique)

  * [Recommandations finales](#heading-recommandations-finales)

## Prérequis : Ce que vous devez savoir avant de lire ce guide

### Connaissances essentielles de React

**Fondamentaux de React (Requis)**

* **Composants fonctionnels** : Vous devez être à l'aise avec l'écriture et l'utilisation des composants fonctionnels React

* **Syntaxe JSX** : Comprendre comment écrire du JSX, utiliser les accolades pour les expressions JavaScript et gérer les événements

* **Props de base** : Savoir comment passer et recevoir des props entre les composants parent et enfant

* **Hook useState** : Vous devez comprendre comment `useState` fonctionne, y compris les mises à jour d'état et les re-rendus

```javascript
// Vous devez être à l'aise avec du code comme ceci :
function MyComponent({ title }) {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <h1>{title}</h1>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

**Hook useEffect (Recommandé)**

* Compréhension de base des effets secondaires dans React

* Quand et pourquoi utiliser `useEffect`

* Comment fonctionnent les tableaux de dépendances

* Cela aide à comprendre les sections d'optimisation des performances

### Prérequis JavaScript

**Fonctionnalités ES6+ (Requis)**

* **Fonctions fléchées** : `const myFunc = () => {}`

* **Déstructuration** : `const { name, age } = person` et `const [first, second] = array`

* **Opérateur de propagation** : `...array` et `...object`

* **Modèles littéraux** : Utilisation des backticks et de la syntaxe `${variable}`

* **Méthodes de tableau** : `map()`, `filter()`, `find()`, `reduce()` - celles-ci apparaissent fréquemment dans les mises à jour d'état

```javascript
// Vous devez comprendre cette syntaxe :
const newItems = [...existingItems, newItem];
const { name, price } = product;
const updatedItems = items.map(item => 
  item.id === productId ? { ...item, quantity: item.quantity + 1 } : item
);
```

**JavaScript asynchrone (Utile)**

* **Promesses et async/await** : Pour comprendre les appels API dans la gestion d'état

* **Gestion de base des erreurs** : blocs try/catch

**Objets et tableaux (Requis)**

* Comment créer, modifier et accéder aux objets et tableaux imbriqués

* Comprendre la référence vs l'égalité de valeur

* Pourquoi la mutation directe est problématique dans React

### Concepts React que vous rencontrerez

**Hiérarchie des composants (Requis)**

* Comment les composants parent et enfant sont liés

* Flux de données du parent à l'enfant

* Pourquoi les données ne peuvent pas facilement circuler "latéralement" entre les composants frères

**Comportement de re-rendu (Important)**

* Quand les composants React se re-rendent

* Pourquoi le changement d'état provoque des re-rendus

* Compréhension de base que la création de nouveaux objets/fonctions provoque des re-rendus

**Gestion des événements (Requis)**

```javascript
// Vous devez être à l'aise avec :
<button onClick={() => handleClick(item.id)}>
<input onChange={(e) => setValue(e.target.value)} />
```

## Environnement de développement

**Outils que vous devriez avoir**

* **React DevTools** : Extension de navigateur pour déboguer les composants React

* **Éditeur de code** : VS Code, WebStorm, ou similaire avec la coloration syntaxique React

* **Node.js et npm/yarn** : Pour installer les packages mentionnés dans les exemples

**Utile mais non requis**

* **Bases de TypeScript** : Certains exemples mentionnent les avantages de TypeScript

* **Connaissances en test** : La section de test suppose une certaine familiarité avec Jest/React Testing Library

* **Outils de construction** : Compréhension de base de Create React App ou Vite

## Compréhension conceptuelle

**Pourquoi la gestion d'état est importante**

Vous devriez avoir rencontré ou comprendre ces points de douleur :

* Passer des données à travers plusieurs niveaux de composants

* Garder les données synchronisées dans différentes parties de votre application

* Gérer l'état complexe de l'application

**Sensibilisation de base aux performances**

* Comprendre que les re-rendus inutiles peuvent ralentir les applications

* Prise de conscience que certaines opérations sont plus coûteuses que d'autres

## Ce que vous n'avez PAS besoin de savoir

**Modèles React avancés**

* Composants d'ordre supérieur (HOCs)

* Props de rendu (bien que nous les expliquions dans l'article)

* Composants de classe ou méthodes de cycle de vie

* Hooks avancés comme `useLayoutEffect` ou `useImperativeHandle`

**Gestion d'état complexe**

* Vous n'avez pas besoin d'expérience préalable avec Redux, Context API, ou d'autres bibliothèques d'état. Je vais tout expliquer à partir de zéro

**JavaScript avancé**

* Fermetures, prototypes, ou concepts avancés de programmation fonctionnelle

* Modèles asynchrones complexes au-delà des promesses de base

## Questions d'auto-évaluation

Avant de plonger, demandez-vous :

1. **Puis-je construire une simple application React avec plusieurs composants ?**

2. **Comprends-je comment passer des données du parent à l'enfant via les props ?**

3. **Puis-je gérer les entrées de formulaire avec useState ?**

4. **Sais-je quand un composant React se re-rend ?**

5. **Suis-je à l'aise avec les méthodes de tableau comme map() et filter() ?**

Si vous avez répondu "oui" à la plupart de ces questions, vous êtes prêt pour ce guide !

## Préparation recommandée

**Si vous devez vous rafraîchir les bases de React :**

* Complétez le tutoriel officiel React (jeu tic-tac-toe)

* Construisez une simple application de todo avec un état local

* Pratiquez le passage de props entre les composants

**Si vous avez besoin d'une révision JavaScript :**

* Pratiquez la déstructuration de tableau et la syntaxe de propagation

* Révisez les fonctions fléchées et les méthodes de tableau

* Familiarisez-vous avec async/await

**Exercice d'échauffement rapide :** Essayez de construire une simple application de compteur où :

* Le composant parent détient l'état du compte

* Plusieurs composants enfants affichent ou modifient le compte

* Vous verrez rapidement pourquoi le prop drilling devient un problème !

## Ce que ce guide vous apprendra

À la fin, vous comprendrez :

* Pourquoi et quand l'état partagé devient complexe

* Comment résoudre le prop drilling avec l'API Context

* Quand utiliser Redux, Zustand, ou d'autres bibliothèques d'état

* Comment optimiser les performances avec l'état partagé

* Stratégies de test pour la gestion d'état

* Bonnes pratiques pour un code maintenable

Le guide est conçu pour vous emmener de "Je connais les bases de React" à "Je peux architecturer la gestion d'état pour des applications complexes" avec de nombreux exemples et explications tout au long du chemin.

## Comprendre les éléments de base : Props dans React

Avant de nous lancer dans la gestion d'état complexe, comprenons les fondamentaux.

### Que sont les props ?

**Props** (abréviation de "properties") sont la manière dont les composants React communiquent entre eux. Pensez aux props comme à des notes que l'on passe entre les salles de classe dans une école – elles transportent des informations d'un composant à un autre.

```javascript
// Ceci est un composant simple qui affiche les informations d'une personne
function PersonCard(props) {
  // props est un objet contenant toutes les données passées à ce composant
  return (
    <div className="person-card">
      {/* Nous accédons aux données en utilisant props.propertyName */}
      <h2>{props.name}</h2>           {/* Affiche le nom de la personne */}
      <p>Age: {props.age}</p>         {/* Affiche l'âge de la personne */}
      <p>Job: {props.job}</p>         {/* Affiche le travail de la personne */}
    </div>
  );
}

// C'est ainsi que nous UTILISONS le composant PersonCard et lui passons des props
function App() {
  return (
    <div>
      {/* 
        Nous créons un composant PersonCard et lui passons trois props :
        - name: "Sarah"
        - age: 28  
        - job: "Developer"
      */}
      <PersonCard 
        name="Sarah" 
        age={28} 
        job="Developer" 
      />
      
      {/* Nous pouvons créer un autre PersonCard avec des props différentes */}
      <PersonCard 
        name="Mike" 
        age={35} 
        job="Designer" 
      />
    </div>
  );
}
```

**Décomposons ce qui se passe :**

1. **PersonCard** est une fonction qui reçoit `props` comme paramètre

2. `props` est un objet JavaScript contenant toutes les données que nous avons passées : `{name: "Sarah", age: 28, job: "Developer"}`

3. Nous accédons aux morceaux individuels de données en utilisant la notation par points : `props.name`, `props.age`, `props.job`

4. Les accolades `{}` indiquent à React "ceci est du code JavaScript, pas du texte régulier"

5. Lorsque nous utilisons `<PersonCard name="Sarah" age={28} job="Developer" />`, React crée automatiquement l'objet props

### Une méthode plus moderne : Déstructuration des props

Au lieu d'écrire `props.name` à chaque fois, nous pouvons utiliser la **déstructuration** pour extraire les valeurs directement :

```javascript
// Au lieu de ceci :
function PersonCard(props) {
  return (
    <div className="person-card">
      <h2>{props.name}</h2>
      <p>Age: {props.age}</p>
      <p>Job: {props.job}</p>
    </div>
  );
}

// Nous pouvons écrire ceci (déstructuration de l'objet props) :
function PersonCard({ name, age, job }) {
  // La déstructuration JavaScript extrait name, age et job de l'objet props
  // C'est comme dire : "Prends l'objet props et crée des variables séparées"
  return (
    <div className="person-card">
      <h2>{name}</h2>        {/* Plus besoin de props.name */}
      <p>Age: {age}</p>      {/* Utilise simplement la variable directement */}
      <p>Job: {job}</p>
    </div>
  );
}
```

**Ce que fait la déstructuration :**

* `{ name, age, job }` indique à JavaScript : "Extrais les propriétés `name`, `age` et `job` de l'objet props"

* Il crée des variables séparées avec ces noms

* Cela rend notre code plus propre et plus facile à lire

## Qu'est-ce que le Prop Drilling et pourquoi est-ce un problème ?

**Le Prop Drilling** se produit lorsque vous devez passer des données à travers plusieurs couches de composants, même lorsque les composants intermédiaires n'utilisent pas ces données. C'est comme jouer au téléphone à travers plusieurs personnes qui ne se soucient pas du message.

### Un exemple simple : Passer un nom d'utilisateur

```javascript
// Supposons que nous voulons afficher le nom d'un utilisateur dans un composant profondément imbriqué
function App() {
  const userName = "Alice";  // Ces données commencent ici en haut
  
  return (
    <div>
      <h1>My Shopping App</h1>
      {/* Nous passons userName à Header */}
      <Header userName={userName} />
    </div>
  );
}

function Header({ userName }) {
  // Header reçoit userName mais ne l'affiche pas réellement
  // Il le passe simplement à Navigation
  return (
    <header>
      <div className="logo">ShopSmart</div>
      {/* Header passe userName à Navigation */}
      <Navigation userName={userName} />
    </header>
  );
}

function Navigation({ userName }) {
  // Navigation n'affiche pas non plus userName
  // Il le passe simplement à UserMenu
  return (
    <nav>
      <a href="/">Home</a>
      <a href="/products">Products</a>
      {/* Navigation passe userName à UserMenu */}
      <UserMenu userName={userName} />
    </nav>
  );
}

function UserMenu({ userName }) {
  // Enfin ! Ce composant utilise réellement userName
  return (
    <div className="user-menu">
      <span>Welcome, {userName}!</span>    {/* userName est affiché ici */}
    </div>
  );
}
```

**Quel est le problème ici ?**

1. **Complexité inutile** : `Header` et `Navigation` ne se soucient pas de `userName`, mais ils doivent le connaître

2. **Couplage serré** : Si nous voulons changer la façon dont `userName` fonctionne, nous devons mettre à jour plusieurs composants

3. **Fardeau de maintenance** : Ajouter un nouveau morceau de données utilisateur signifie mettre à jour quatre composants différents

4. **Code confus** : Il est difficile de suivre où les données sont réellement utilisées

Ceci est un exemple simple avec seulement un morceau de données. Imaginez ceci avec 5-10 morceaux de données différents !

### Un exemple réaliste : Prop drilling du panier d'achat

Maintenant, voyons comment cela devient un vrai cauchemar avec un panier d'achat :

```javascript
// Le composant principal App - c'est ici que vivent nos données de panier
function App() {
  // useState est un hook React qui crée un état (des données qui peuvent changer)
  // Il retourne un tableau avec deux éléments :
  // 1. La valeur actuelle (cartItems)
  // 2. Une fonction pour mettre à jour la valeur (setCartItems)
  const [cartItems, setCartItems] = useState([]);  // Commence avec un tableau vide
  
  // Un autre morceau d'état pour le prix total
  const [cartTotal, setCartTotal] = useState(0);   // Commence avec 0
  
  // Une fonction qui ajoute des articles au panier
  const addToCart = (product) => {
    // L'opérateur de propagation (...) crée un nouveau tableau avec tous les articles existants plus le nouveau
    const newCartItems = [...cartItems, product];
    setCartItems(newCartItems);                    // Met à jour les articles du panier
    setCartTotal(cartTotal + product.price);       // Met à jour le total
  };
  
  // Une fonction qui supprime des articles du panier
  const removeFromCart = (productId) => {
    // filter() crée un nouveau tableau avec uniquement les articles qui ne correspondent pas à l'ID
    const updatedItems = cartItems.filter(item => item.id !== productId);
    
    // find() localise l'article que nous supprimons afin que nous puissions soustraire son prix
    const removedItem = cartItems.find(item => item.id === productId);
    
    setCartItems(updatedItems);                           // Met à jour les articles
    setCartTotal(cartTotal - removedItem.price);          // Met à jour le total
  };

  return (
    <div className="app">
      {/* 
        Nous devons passer les données du panier à Header pour qu'il puisse afficher le nombre d'articles
        Regardez combien de props nous devons passer !
      */}
      <Header 
        cartItems={cartItems}         // Passe le tableau entier du panier
        cartTotal={cartTotal}         // Passe le prix total
        addToCart={addToCart}         // Passe la fonction d'ajout
        removeFromCart={removeFromCart} // Passe la fonction de suppression
      />
      
      {/* MainContent a également besoin de toute la fonctionnalité du panier */}
      <MainContent 
        cartItems={cartItems}
        cartTotal={cartTotal}
        addToCart={addToCart}
        removeFromCart={removeFromCart}
      />
    </div>
  );
}
```

Maintenant, voyons ce qui se passe dans le composant Header :

```javascript
function Header({ cartItems, cartTotal, addToCart, removeFromCart }) {
  // Header reçoit toutes ces props mais n'en utilise que certaines
  // Il doit les passer aux autres composants
  
  return (
    <header className="header">
      <div className="logo">ShopSmart</div>
      
      {/* 
        Navigation doit afficher le nombre d'articles du panier, donc nous passons cartItems
        Mais il n'a pas besoin de addToCart ou removeFromCart
        Cependant, nous pourrions les passer "au cas où"
      */}
      <Navigation 
        cartItems={cartItems}
        cartTotal={cartTotal}
        addToCart={addToCart}           // Navigation n'utilise pas ceci
        removeFromCart={removeFromCart}  // Navigation n'utilise pas ceci non plus
      />
      
      {/* UserMenu pourrait vouloir afficher le total du panier */}
      <UserMenu 
        cartTotal={cartTotal}
        addToCart={addToCart}           // UserMenu n'utilise pas ceci
        removeFromCart={removeFromCart}  // UserMenu n'utilise pas ceci non plus
      />
    </header>
  );
}

function Navigation({ cartItems, cartTotal, addToCart, removeFromCart }) {
  // Navigation ne se soucie que d'afficher le nombre d'articles du panier
  // Mais il reçoit TOUTES les props du panier de toute façon
  
  const itemCount = cartItems.length;  // Calcule combien d'articles dans le panier
  
  return (
    <nav className="navigation">
      <a href="/">Home</a>
      <a href="/products">Products</a>
      
      {/* C'est le SEUL endroit où Navigation utilise réellement les données du panier */}
      <a href="/cart">
        Cart 
        {/* N'afficher le badge que s'il y a des articles */}
        {itemCount > 0 && (
          <span className="cart-badge">{itemCount}</span>
        )}
      </a>
    </nav>
  );
}
```

**Les problèmes se multiplient :**

1. **Pollution des props** : Les composants reçoivent des props qu'ils n'utilisent pas

2. **Interfaces confuses** : Il est difficile de dire ce dont chaque composant a réellement besoin

3. **Effets de propagation des changements** : La modification de la fonctionnalité du panier peut nécessiter de changer 6+ composants

4. **Complexité des tests** : Tester Navigation nécessite de simuler des fonctions de panier qu'il n'utilise même pas

5. **Problèmes de performance** : Le changement des données du panier provoque le re-rendu de TOUS les composants dans la chaîne

### Pourquoi cela se produit et empire

Ce schéma émerge naturellement parce que :

1. **React est un flux de données unidirectionnel** : Les données ne peuvent circuler que de haut en bas, du parent à l'enfant

2. **Hiérarchie des composants** : Votre structure UI détermine votre flux de données

3. **Aucun mécanisme de partage intégré** : React ne fournit pas de moyen pour que les composants distants partagent des données directement

À mesure que votre application grandit, vous vous retrouvez avec :

* 10+ props étant passées à travers 5+ niveaux

* Des composants qui existent juste pour passer des props

* Des développeurs qui ont peur de refactoriser parce qu'ils pourraient casser la chaîne de props

* De nouvelles fonctionnalités nécessitant des changements dans des composants non liés

## Solution 1 : React Context API – Comprendre le concept

L'**API Context** est la solution intégrée de React pour partager des données entre des composants sans prop drilling. Pensez-y comme à une station de radio qui diffuse des informations, et n'importe quel composant peut se brancher pour écouter.

### L'analogie de la station de radio

**Le prop drilling traditionnel** est comme passer une note à travers une chaîne de personnes :

* La personne A dit à la personne B

* La personne B dit à la personne C

* La personne C dit à la personne D

* Seule la personne D a réellement besoin de l'information

**React Context** est comme une diffusion radio :

* La station de radio diffuse des informations

* Toute personne avec une radio peut écouter directement

* Pas besoin de passer des messages par des intermédiaires

### Qu'est-ce que `createContext()` ?

`createContext()` est une fonction React qui crée un "système de diffusion" pour vos données. Elle retourne deux choses :

1. **Provider** : La "station de radio" qui diffuse les données

2. **Consumer** : La "radio" que les composants utilisent pour écouter les données

```javascript
import { createContext } from 'react';

// createContext() crée notre "station de radio"
// Nous pouvons passer une valeur par défaut (comme une fréquence radio par défaut)
const CartContext = createContext();

// CartContext contient maintenant :
// - CartContext.Provider (le diffuseur)
// - CartContext.Consumer (l'écouteur, bien que nous l'utilisions rarement directement)
```

**Ce que fait createContext() :**

* Crée un objet React spécial qui peut partager des données

* La valeur par défaut est utilisée lorsqu'un composant essaie d'accéder au contexte mais n'est pas à l'intérieur d'un Provider

* Retourne un objet avec les composants Provider et Consumer

### Créer un fournisseur de contexte de base

Un **Provider** est un composant qui rend les données disponibles pour tous ses enfants :

```javascript
import { createContext, useState } from 'react';

// Étape 1 : Créer le contexte
const CartContext = createContext();

// Étape 2 : Créer un composant Provider
function CartProvider({ children }) {
  // children est une prop spéciale qui contient tous les composants à l'intérieur de CartProvider
  
  // C'est notre état de panier - comme avant
  const [cartItems, setCartItems] = useState([]);
  const [cartTotal, setCartTotal] = useState(0);
  
  // Nos fonctions de panier
  const addToCart = (product) => {
    // L'opérateur de propagation (...) crée un nouveau tableau avec tous les articles existants plus le nouveau
    const newCartItems = [...cartItems, product];
    setCartItems(newCartItems);                    // Met à jour les articles du panier
    setCartTotal(cartTotal + product.price);       // Met à jour le total
  };

  const removeFromCart = (productId) => {
    // filter() crée un nouveau tableau avec uniquement les articles qui ne correspondent pas à l'ID
    const updatedItems = cartItems.filter(item => item.id !== productId);
    
    // find() localise l'article que nous supprimons afin que nous puissions soustraire son prix
    const removedItem = cartItems.find(item => item.id === productId);
    
    setCartItems(updatedItems);                           // Met à jour les articles
    if (removedItem) {  // Assurez-vous que nous avons trouvé l'article avant de soustraire
      setCartTotal(cartTotal - removedItem.price);          // Met à jour le total
    }
  };

  // Cet objet contient tout ce que nous voulons partager
  const cartValue = {
    cartItems,      // Le tableau des articles
    cartTotal,      // Le prix total
    addToCart,      // Fonction pour ajouter des articles
    removeFromCart, // Fonction pour supprimer des articles
    itemCount: cartItems.length  // Valeur calculée pour la commodité
  };

  return (
    /* 
      CartContext.Provider est la "station de radio"
      - value prop est ce qui est "diffusé"
      - children sont tous les composants qui peuvent "écouter" cette diffusion
    */
    <CartContext.Provider value={cartValue}>
      {children}
    </CartContext.Provider>
  );
}
```

**Décomposons ce Provider :**

1. **Composant fonctionnel** : `CartProvider` est juste un composant React régulier

2. **prop children** : Cela contient tout JSX placé à l'intérieur de `<CartProvider>...</CartProvider>`

3. **Gestion d'état** : Nous gérons l'état du panier exactement comme avant avec `useState`

4. **prop value** : C'est crucial - tout ce que nous mettons ici devient disponible pour tous les composants enfants

5. **Retour JSX** : Nous enveloppons `children` dans `CartContext.Provider` pour "diffuser" nos données

### Comprendre le hook useContext

**useContext** est un hook React qui permet aux composants de "s'accorder" à une diffusion de contexte :

```javascript
import { useContext } from 'react';

function CartBadge() {
  // useContext(CartContext) "s'accorde" à nos données de panier
  // Il retourne ce que nous avons mis dans la prop value de CartProvider
  const cartData = useContext(CartContext);
  
  // cartData contient maintenant : { cartItems, cartTotal, addToCart, removeFromCart, itemCount }
  
  return (
    <div className="cart-badge">
      {/* Nous pouvons accéder à n'importe quelle propriété de notre objet cartValue */}
      <span>Cart ({cartData.itemCount})</span>
    </div>
  );
}
```

**Ce que fait useContext() :**

1. **Cherche dans l'arbre des composants** : Trouve le CartContext.Provider le plus proche

2. **Retourne la valeur** : Nous donne ce qui a été passé à la prop value

3. **Re-rend automatiquement** : Lorsque la valeur du contexte change, ce composant se met à jour

4. **Lance une erreur** : Si aucun Provider n'est trouvé, il retourne la valeur par défaut (ou undefined)

### Créer un hook personnalisé pour une utilisation plus propre

Au lieu d'utiliser `useContext(CartContext)` partout, nous pouvons créer un hook personnalisé :

```javascript
// Hook personnalisé qui enveloppe useContext
function useCart() {
  // Obtenir les données du panier à partir du contexte
  const context = useContext(CartContext);
  
  // Vérifier si nous sommes à l'intérieur d'un CartProvider
  if (context === undefined) {
    throw new Error('useCart must be used within a CartProvider');
  }
  
  return context;
}

// Maintenant les composants peuvent utiliser notre hook personnalisé
function CartBadge() {
  const { itemCount } = useCart();  // Beaucoup plus propre !
  
  return (
    <div className="cart-badge">
      <span>Cart ({itemCount})</span>
    </div>
  );
}
```

Il y a diverses raisons de créer un hook personnalisé :

1. **Meilleurs messages d'erreur** : Nous obtenons une erreur claire si quelqu'un oublie le Provider

2. **Imports plus propres** : Importer `useCart` au lieu de `useContext` et `CartContext`

3. **Flexibilité future** : Nous pouvons ajouter de la logique au hook plus tard si nécessaire

4. **Sécurité de type** : Dans TypeScript, cela fournit une meilleure inférence de type

### Mettre tout ensemble : Exemple complet de contexte

Maintenant, voyons à quoi ressemble notre panier d'achat avec Context au lieu de prop drilling :

```javascript
import { createContext, useContext, useState } from 'react';

// Étape 1 : Créer le contexte
const CartContext = createContext();

// Étape 2 : Créer un hook personnalisé
function useCart() {
  const context = useContext(CartContext);
  if (context === undefined) {
    throw new Error('useCart must be used within a CartProvider');
  }
  return context;
}

// Étape 3 : Créer le Provider
function CartProvider({ children }) {
  const [cartItems, setCartItems] = useState([]);
  const [cartTotal, setCartTotal] = useState(0);

  const addToCart = (product) => {
    const newCartItems = [...cartItems, product];
    setCartItems(newCartItems);
    setCartTotal(cartTotal + product.price);
  };

  const removeFromCart = (productId) => {
    const updatedItems = cartItems.filter(item => item.id !== productId);
    const removedItem = cartItems.find(item => item.id === productId);
    
    setCartItems(updatedItems);
    if (removedItem) {
      setCartTotal(cartTotal - removedItem.price);
    }
  };

  const value = {
    cartItems,
    cartTotal,
    addToCart,
    removeFromCart,
    itemCount: cartItems.length
  };

  return (
    <CartContext.Provider value={value}>
      {children}
    </CartContext.Provider>
  );
}

// Étape 4 : Utiliser le contexte dans les composants
function App() {
  return (
    // Envelopper notre application dans le CartProvider
    <CartProvider>
      <div className="app">
        {/* Pas de props nécessaires ! */}
        <Header />
        <MainContent />
      </div>
    </CartProvider>
  );
}

function Header() {
  // Header n'a besoin d'aucune props de panier
  return (
    <header className="header">
      <div className="logo">ShopSmart</div>
      <Navigation />  {/* Pas de props passées ici non plus */}
      <UserMenu />
    </header>
  );
}

function Navigation() {
  // Navigation obtient les données du panier directement à partir du contexte
  const { itemCount } = useCart();
  
  return (
    <nav className="navigation">
      <a href="/">Home</a>
      <a href="/products">Products</a>
      <a href="/cart">
        Cart 
        {itemCount > 0 && (
          <span className="cart-badge">{itemCount}</span>
        )}
      </a>
    </nav>
  );
}

function ProductCard({ product }) {
  // ProductCard obtient la fonction addToCart directement
  const { addToCart } = useCart();
  
  return (
    <div className="product-card">
      <h3>{product.name}</h3>
      <p>{product.description}</p>
      <span className="price">${product.price}</span>
      
      {/* Pas de prop drilling nécessaire ! */}
      <button onClick={() => addToCart(product)}>
        Add to Cart
      </button>
    </div>
  );
}

function CartSidebar() {
  // CartSidebar obtient les articles du panier et la fonction de suppression directement
  const { cartItems, removeFromCart } = useCart();
  
  return (
    <div className="cart-sidebar">
      <h3>Your Cart</h3>
      {cartItems.length === 0 ? (
        <p>Your cart is empty</p>
      ) : (
        <ul>
          {cartItems.map(item => (
            <li key={item.id}>
              <span>{item.name} - ${item.price}</span>
              <button onClick={() => removeFromCart(item.id)}>
                Remove
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

// Exporter notre Provider et hook pour une utilisation dans d'autres fichiers
export { CartProvider, useCart };
```

**Comparez ceci à notre version avec prop drilling :**

**Avant (Prop Drilling) :**

* App passe 4 props à Header

* Header passe 4 props à Navigation (même si Navigation n'a besoin que de 1)

* Navigation reçoit des props qu'il n'utilise pas

* Chaque composant de la chaîne doit connaître la structure du panier

**Après (Context) :**

* App doit seulement envelopper les composants dans CartProvider

* Header ne gère aucune props de panier

* Navigation obtient directement seulement ce dont il a besoin (`itemCount`)

* ProductCard obtient directement seulement ce dont il a besoin (`addToCart`)

* Chaque composant est indépendant et focalisé

## Modèles et concepts avancés de contexte

Maintenant que vous comprenez les bases, explorons des modèles de contexte plus sophistiqués que vous rencontrerez dans des applications réelles.

### Contexte multiple pour la séparation des préoccupations

Dans les applications réelles, vous ne voulez pas mettre tout dans un seul contexte géant. Au lieu de cela, vous pouvez créer des contextes séparés pour différents domaines :

```javascript
// Contextes séparés pour différents types de données
const UserContext = createContext();     // Authentification et profil de l'utilisateur
const ThemeContext = createContext();    // Thème et apparence de l'UI  
const CartContext = createContext();     // Fonctionnalité du panier d'achat

// Fournisseur d'utilisateur - gère l'authentification
function UserProvider({ children }) {
  const [user, setUser] = useState(null);           // Données de l'utilisateur actuel
  const [isLoggedIn, setIsLoggedIn] = useState(false); // Statut de connexion
  
  // Fonction pour connecter un utilisateur
  const login = async (email, password) => {
    try {
      // authAPI serait votre service d'authentification (comme Firebase, Auth0, etc.)
      const userData = await authAPI.login(email, password);
      setUser(userData);        // Stocker les informations de l'utilisateur
      setIsLoggedIn(true);      // Marquer comme connecté
    } catch (error) {
      console.error('Login failed:', error);
      // Gérer les erreurs de connexion (afficher un message à l'utilisateur, etc.)
    }
  };
  
  // Fonction pour déconnecter un utilisateur
  const logout = () => {
    setUser(null);            // Effacer les données de l'utilisateur
    setIsLoggedIn(false);     // Marquer comme déconnecté
    // Vous pourriez également effacer localStorage, rediriger vers la page de connexion, etc.
  };
  
  const value = {
    user,         // Objet utilisateur actuel : { id, name, email, etc. }
    isLoggedIn,   // Booléen : true si l'utilisateur est connecté
    login,        // Fonction pour se connecter
    logout,       // Fonction pour se déconnecter
  };
  
  return (
    <UserContext.Provider value={value}>
      {children}
    </UserContext.Provider>
  );
}

// Fournisseur de thème - gère l'apparence de l'UI
function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');      // 'light' ou 'dark'
  const [fontSize, setFontSize] = useState('medium'); // 'small', 'medium', 'large'
  
  // Fonction pour basculer entre les thèmes clair et foncé
  const toggleTheme = () => {
    setTheme(currentTheme => currentTheme === 'light' ? 'dark' : 'light');
  };
  
  // Fonction pour mettre à jour la taille de la police
  const updateFontSize = (size) => {
    if (['small', 'medium', 'large'].includes(size)) {
      setFontSize(size);
    }
  };
  
  const value = {
    theme,          // Thème actuel : 'light' ou 'dark'
    fontSize,       // Taille de police actuelle : 'small', 'medium', ou 'large'
    toggleTheme,    // Fonction pour basculer les thèmes
    updateFontSize, // Fonction pour changer la taille de la police
  };
  
  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}

// Hooks personnalisés pour chaque contexte
function useUser() {
  const context = useContext(UserContext);
  if (context === undefined) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
}

function useTheme() {
  const context = useContext(ThemeContext);
  if (context === undefined) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  return context;
}

// App avec plusieurs fournisseurs
function App() {
  return (
    // Vous pouvez imbriquer les fournisseurs dans n'importe quel ordre
    // Chaque fournisseur rend ses données disponibles à tous les enfants
    <UserProvider>
      <ThemeProvider>
        <CartProvider>
          <div className="app">
            <Header />
            <MainContent />
            <Footer />
          </div>
        </CartProvider>
      </ThemeProvider>
    </UserProvider>
  );
}

// Composant utilisant plusieurs contextes
function UserProfile() {
  const { user, logout } = useUser();           // Obtenir les données de l'utilisateur
  const { theme, toggleTheme } = useTheme();    // Obtenir les données du thème
  const { itemCount } = useCart();              // Obtenir les données du panier
  
  return (
    <div className={`user-profile theme-${theme}`}>
      <h2>Welcome, {user?.name}!</h2>
      <p>Items in cart: {itemCount}</p>
      
      <button onClick={toggleTheme}>
        Switch to {theme === 'light' ? 'dark' : 'light'} theme
      </button>
      
      <button onClick={logout}>
        Logout
      </button>
    </div>
  );
}
```

Pourquoi devriez-vous utiliser des contextes séparés ? Tout d'abord, pour des raisons de performance : les composants ne se re-rendent que lorsque le contexte spécifique qu'ils utilisent change. Ensuite, c'est utile pour des raisons d'organisation car les fonctionnalités liées sont regroupées ensemble. C'est également idéal pour la réutilisabilité, car vous pouvez utiliser UserProvider dans différentes applications sans fonctionnalité de panier. Et enfin, c'est plus facile de tester des composants qui dépendent uniquement de contextes spécifiques.

### Comprendre `useReducer` pour la logique d'état complexe

Lorsque l'état de votre contexte devient complexe avec plusieurs valeurs liées et une logique de mise à jour complexe, `useReducer` est souvent un meilleur choix que plusieurs appels `useState`.

**Qu'est-ce que useReducer ?** `useReducer` est un hook React qui gère l'état à travers une fonction "reducer". Au lieu de définir directement l'état, vous "dispatchez des actions" qui décrivent ce qui s'est passé, et le reducer décide comment mettre à jour l'état.

Pensez-y comme à un distributeur automatique :

* Vous appuyez sur des boutons (dispatchez des actions) pour décrire ce que vous voulez

* La machine a une logique interne (reducer) qui détermine ce qui se passe

* La machine vous donne le résultat (nouvel état)

```javascript
// D'abord, définissons les actions que notre panier peut gérer
const cartActions = {
  ADD_ITEM: 'ADD_ITEM',           // Ajouter un produit au panier
  REMOVE_ITEM: 'REMOVE_ITEM',     // Supprimer un produit complètement
  UPDATE_QUANTITY: 'UPDATE_QUANTITY', // Changer la quantité d'un article existant
  CLEAR_CART: 'CLEAR_CART',       // Vider entièrement le panier
  APPLY_DISCOUNT: 'APPLY_DISCOUNT' // Appliquer un code de réduction
};

// La fonction reducer : décide comment l'état change en fonction des actions
function cartReducer(state, action) {
  // state: état actuel du panier
  // action: objet décrivant ce qui s'est passé, comme { type: 'ADD_ITEM', payload: product }
  
  switch (action.type) {
    case cartActions.ADD_ITEM: {
      const product = action.payload;  // Le produit étant ajouté
      
      // Vérifier si ce produit est déjà dans le panier
      const existingItemIndex = state.items.findIndex(item => item.id === product.id);
      
      if (existingItemIndex >= 0) {
        // Le produit existe : augmenter sa quantité
        const updatedItems = [...state.items];  // Créer une copie du tableau des articles
        updatedItems[existingItemIndex] = {
          ...updatedItems[existingItemIndex],    // Copier les propriétés de l'article existant
          quantity: updatedItems[existingItemIndex].quantity + 1  // Augmenter la quantité
        };
        
        return {
          ...state,                              // Conserver les autres propriétés de l'état
          items: updatedItems,                   // Mettre à jour le tableau des articles
          total: state.total + product.price,   // Ajouter au total
          itemCount: state.itemCount + 1,       // Augmenter le compte
        };
      } else {
        // Nouveau produit : l'ajouter au panier
        const newItem = { 
          ...product,     // Copier toutes les propriétés du produit (id, name, price, etc.)
          quantity: 1     // Ajouter la propriété quantity
        };
        
        return {
          ...state,                                    // Conserver les autres propriétés de l'état
          items: [...state.items, newItem],           // Ajouter le nouvel article au tableau
          total: state.total + product.price,         // Ajouter au total
          itemCount: state.itemCount + 1,             // Augmenter le compte
        };
      }
    }
    
    case cartActions.REMOVE_ITEM: {
      const productId = action.payload;  // ID du produit à supprimer
      
      // Trouver l'article à supprimer
      const itemToRemove = state.items.find(item => item.id === productId);
      
      // Si l'article n'existe pas, retourner l'état inchangé
      if (!itemToRemove) return state;
      
      // Supprimer l'article du tableau
      const updatedItems = state.items.filter(item => item.id !== productId);
      
      return {
        ...state,
        items: updatedItems,
        // Soustraire le prix total de l'article supprimé (price × quantity)
        total: state.total - (itemToRemove.price * itemToRemove.quantity),
        // Soustraire la quantité de l'article supprimé
        itemCount: state.itemCount - itemToRemove.quantity,
      };
    }
    
    case cartActions.UPDATE_QUANTITY: {
      const { productId, quantity } = action.payload;
      
      // Si la quantité est 0 ou moins, supprimer l'article
      if (quantity <= 0) {
        return cartReducer(state, {
          type: cartActions.REMOVE_ITEM,
          payload: productId
        });
      }
      
      const updatedItems = state.items.map(item => {
        if (item.id === productId) {
          return { ...item, quantity };  // Mettre à jour la quantité de cet article
        }
        return item;  // Conserver les autres articles inchangés
      });
      
      // Trouver l'article pour calculer la différence de prix
      const item = state.items.find(item => item.id === productId);
      if (!item) return state;  // Article non trouvé, pas de changement
      
      const quantityDifference = quantity - item.quantity;
      
      return {
        ...state,
        items: updatedItems,
        total: state.total + (item.price * quantityDifference),
        itemCount: state.itemCount + quantityDifference,
      };
    }
    
    case cartActions.CLEAR_CART: {
      // Réinitialiser tout à l'état initial
      return {
        items: [],
        total: 0,
        itemCount: 0,
        discount: 0,
      };
    }
    
    case cartActions.APPLY_DISCOUNT: {
      const discountPercent = action.payload;  // Pourcentage de réduction (par exemple, 10 pour 10%)
      const discountAmount = state.total * (discountPercent / 100);
      
      return {
        ...state,
        discount: discountAmount,
      };
    }
    
    default:
      // Si nous ne reconnaissons pas le type d'action, retourner l'état inchangé
      return state;
  }
}

// CartProvider mis à jour utilisant useReducer
function CartProvider({ children }) {
  // État initial pour notre panier
  const initialState = {
    items: [],       // Tableau des articles du panier
    total: 0,        // Prix total avant réduction
    itemCount: 0,    // Nombre total d'articles
    discount: 0,     // Montant de la réduction
  };
  
  // useReducer prend deux arguments :
  // 1. La fonction reducer (cartReducer)
  // 2. L'état initial
  // Il retourne :
  // 1. L'état actuel
  // 2. La fonction dispatch pour envoyer des actions
  const [state, dispatch] = useReducer(cartReducer, initialState);
  
  // Fonctions créatrices d'actions - celles-ci créent des objets d'action
  const addItem = (product) => {
    dispatch({
      type: cartActions.ADD_ITEM,    // Ce qui s'est passé
      payload: product               // Les données nécessaires
    });
  };
  
  const removeItem = (productId) => {
    dispatch({
      type: cartActions.REMOVE_ITEM,
      payload: productId
    });
  };
  
  const updateQuantity = (productId, quantity) => {
    dispatch({
      type: cartActions.UPDATE_QUANTITY,
      payload: { productId, quantity }
    });
  };
  
  const clearCart = () => {
    dispatch({ type: cartActions.CLEAR_CART });
  };
  
  const applyDiscount = (discountPercent) => {
    dispatch({
      type: cartActions.APPLY_DISCOUNT,
      payload: discountPercent
    });
  };
  
  // Calculer le total final (total moins réduction)
  const finalTotal = state.total - state.discount;
  
  const value = {
    // Valeurs d'état
    items: state.items,
    total: state.total,
    itemCount: state.itemCount,
    discount: state.discount,
    finalTotal,
    
    // Fonctions d'action
    addItem,
    removeItem,
    updateQuantity,
    clearCart,
    applyDiscount,
  };
  
  return (
    <CartContext.Provider value={value}>
      {children}
    </CartContext.Provider>
  );
}
```

`useReducer` présente divers avantages par rapport à plusieurs `useState` :

1. **Logique centralisée** : Toute la logique de mise à jour du panier est au même endroit (le reducer)

2. **Mises à jour prévisibles** : Les actions décrivent ce qui s'est passé, le reducer décide comment mettre à jour

3. **Tests plus faciles** : Vous pouvez tester la fonction reducer indépendamment

4. **Mieux adapté à l'état complexe** : Lorsque l'état a plusieurs valeurs liées qui changent ensemble

5. **Débogage** : Vous pouvez journaliser toutes les actions pour voir exactement ce qui s'est passé

## Solution 2 : Bibliothèques de gestion d'état expliquées

Bien que React Context soit excellent pour les applications de complexité moyenne, les applications plus grandes bénéficient souvent de bibliothèques de gestion d'état dédiées. Explorons les options les plus populaires.

### Comprendre Redux : Le conteneur d'état prévisible

**Redux** est une bibliothèque qui fournit un seul magasin centralisé pour tout l'état de votre application. Pensez-y comme à une énorme base de données que toute votre application partage, avec des règles strictes sur la manière dont les données peuvent être modifiées.

#### Concepts de base de Redux

**1. Store** : La source unique de vérité pour l'état de votre application

```javascript
// Le store est comme une base de données qui contient TOUT l'état de votre application
import { createStore } from 'redux';

// Exemple de ce à quoi pourrait ressembler l'état complet de votre application
const initialAppState = {
  user: {
    id: null,
    name: '',
    email: '',
    isLoggedIn: false
  },
  cart: {
    items: [],
    total: 0,
    discount: 0
  },
  ui: {
    theme: 'light',
    sidebarOpen: false,
    loading: false
  }
};

// Le store contient cet état et fournit des méthodes pour interagir avec lui
const store = createStore(rootReducer, initialAppState);

// Vous pouvez obtenir l'état actuel à tout moment
const currentState = store.getState();
console.log(currentState.cart.items);  // Accéder aux articles du panier
console.log(currentState.user.name);   // Accéder au nom de l'utilisateur
```

**2. Actions** : Objets simples qui décrivent ce qui s'est passé

```javascript
// Les actions sont comme des descriptions d'événements - elles disent à Redux ce qui s'est passé
// Elles doivent avoir une propriété 'type' et éventuellement un 'payload'

// Action pour ajouter un article au panier
const addItemAction = {
  type: 'cart/addItem',              // Décrit ce qui s'est passé
  payload: {                        // Les données nécessaires
    id: 1,
    name: 'T-Shirt',
    price: 25
  }
};

// Action pour connecter un utilisateur
const loginAction = {
  type: 'user/login',
  payload: {
    id: 123,
    name: 'Alice',
    email: 'alice@example.com'
  }
};

// Action pour basculer le thème
const toggleThemeAction = {
  type: 'ui/toggleTheme'            // Pas de payload nécessaire
};

// Créateurs d'actions : fonctions qui créent des actions
function addItem(product) {
  return {
    type: 'cart/addItem',
    payload: product
  };
}

function loginUser(userData) {
  return {
    type: 'user/login',
    payload: userData
  };
}

// Utilisation
const action = addItem({ id: 1, name: 'T-Shirt', price: 25 });
console.log(action);  // { type: 'cart/addItem', payload: { ... } }
```

**3. Reducers** : Fonctions pures qui spécifient comment l'état change

```javascript
// Un reducer est une fonction qui prend l'état actuel et une action,
// et retourne un nouvel état. Il ne doit JAMAIS modifier l'état existant.

function cartReducer(state = { items: [], total: 0 }, action) {
  // state: état actuel du panier
  // action: l'objet action décrivant ce qui s'est passé
  
  switch (action.type) {
    case 'cart/addItem': {
      const product = action.payload;
      
      // NE JAMAIS modifier l'état existant directement !
      // Au lieu de cela, créer de nouveaux objets/tableaux
      return {
        ...state,                                    // Copier l'état existant
        items: [...state.items, product],           // Créer un nouveau tableau d'articles
        total: state.total + product.price          // Calculer le nouveau total
      };
    }
    
    case 'cart/removeItem': {
      const productId = action.payload;
      const itemToRemove = state.items.find(item => item.id === productId);
      
      return {
        ...state,
        items: state.items.filter(item => item.id !== productId),  // Nouveau tableau sans l'article
        total: state.total - (itemToRemove?.price || 0)           // Soustraire le prix
      };
    }
    
    default:
      // Toujours retourner l'état actuel pour les actions inconnues
      return state;
  }
}

function userReducer(state = { id: null, name: '', isLoggedIn: false }, action) {
  switch (action.type) {
    case 'user/login':
      return {
        ...state,
        ...action.payload,    // Fusionner les données utilisateur du payload
        isLoggedIn: true      // Définir le statut de connexion
      };
    
    case 'user/logout':
      return {
        id: null,
        name: '',
        email: '',
        isLoggedIn: false
      };
    
    default:
      return state;
  }
}

// Root reducer : combine tous les reducers
function rootReducer(state = {}, action) {
  return {
    cart: cartReducer(state.cart, action),    // Gérer les actions du panier
    user: userReducer(state.user, action),    // Gérer les actions de l'utilisateur
  };
}
```

**4. Dispatch** : La seule façon de déclencher des changements d'état

```javascript
// Vous ne pouvez pas changer l'état Redux directement
// Au lieu de cela, vous dispachez des actions pour décrire ce qui devrait se passer

// Obtenir la fonction dispatch du store
const { dispatch } = store;

// Dispatcher des actions pour changer l'état
dispatch(addItem({ id: 1, name: 'T-Shirt', price: 25 }));
dispatch(loginUser({ id: 123, name: 'Alice', email: 'alice@example.com' }));
dispatch({ type: 'user/logout' });

// Chaque dispatch déclenche le reducer, qui retourne un nouvel état
```

#### Comment utiliser Redux dans les composants React

Pour utiliser Redux dans React, vous avez besoin de la bibliothèque `react-redux`, qui fournit deux outils principaux :

**1. Provider** : Rend le store disponible pour tous les composants

```javascript
import { Provider } from 'react-redux';
import { createStore } from 'redux';

// Créer votre store Redux
const store = createStore(rootReducer);

function App() {
  return (
    // Provider rend le store disponible pour tous les composants enfants
    <Provider store={store}>
      <div className="app">
        <Header />
        <ProductList />
        <Cart />
      </div>
    </Provider>
  );
}
```

**2. Hooks useSelector et useDispatch**

```javascript
import { useSelector, useDispatch } from 'react-redux';

function ProductCard({ product }) {
  // useSelector extrait les données du store Redux
  // La fonction que vous passez reçoit l'objet d'état entier
  const cartItems = useSelector(state => state.cart.items);
  
  // useDispatch retourne la fonction dispatch
  const dispatch = useDispatch();
  
  // Vérifier si ce produit est déjà dans le panier
  const isInCart = cartItems.some(item => item.id === product.id);
  
  const handleAddToCart = () => {
    // Dispatcher une action pour ajouter un article
    dispatch(addItem(product));
  };
  
  return (
    <div className="product-card">
      <h3>{product.name}</h3>
      <p>{product.description}</p>
      <span className="price">${product.price}</span>
      
      <button 
        onClick={handleAddToCart}
        disabled={isInCart}
      >
        {isInCart ? 'In Cart' : 'Add to Cart'}
      </button>
    </div>
  );
}

function CartSummary() {
  // Sélectionner plusieurs morceaux d'état
  const { items, total } = useSelector(state => ({
    items: state.cart.items,
    total: state.cart.total
  }));
  
  const dispatch = useDispatch();
  
  const handleRemoveItem = (productId) => {
    dispatch(removeItem(productId));
  };
  
  return (
    <div className="cart-summary">
      <h3>Cart Summary</h3>
      <p>Total: ${total.toFixed(2)}</p>
      
      {items.map(item => (
        <div key={item.id} className="cart-item">
          <span>{item.name} - ${item.price}</span>
          <button onClick={() => handleRemoveItem(item.id)}>
            Remove
          </button>
        </div>
      ))}
    </div>
  );
}
```

### Redux Toolkit : Redux moderne simplifié

**Redux Toolkit** est la manière officielle et recommandée d'écrire la logique Redux. Il simplifie Redux en fournissant des utilitaires qui réduisent le code répétitif.

#### Ce que Redux Toolkit fournit

1. **createSlice** : Génère automatiquement des créateurs d'actions et des reducers

2. **configureStore** : Configure le store avec de bonnes valeurs par défaut

3. **Intégration d'Immer** : Permet d'écrire une logique "mutative" qui est en réalité immutable

```javascript
import { createSlice, configureStore } from '@reduxjs/toolkit';

// createSlice génère automatiquement des créateurs d'actions et des reducers
const cartSlice = createSlice({
  name: 'cart',                     // Nom pour cette partie de l'état
  
  initialState: {                   // Valeur initiale de l'état
    items: [],
    total: 0
  },
  
  reducers: {                       // Fonctions de réduction
    // Redux Toolkit utilise Immer en interne, donc nous pouvons "muter" l'état
    // (C'est en réalité la création de mises à jour immutables en arrière-plan)
    
    addItem: (state, action) => {
      const product = action.payload;
      const existingItem = state.items.find(item => item.id === product.id);
      
      if (existingItem) {
        // Mettre à jour la quantité de l'article existant
        existingItem.quantity += 1;              // Cela ressemble à une mutation !
      } else {
        // Ajouter un nouvel article
        state.items.push({                       // Cela ressemble à une mutation !
          ...product, 
          quantity: 1 
        });
      }
      
      state.total += product.price;              // Cela ressemble à une mutation !
    },
    
    removeItem: (state, action) => {
      const productId = action.payload;
      const itemIndex = state.items.findIndex(item => item.id === productId);
      
      if (itemIndex >= 0) {
        const item = state.items[itemIndex];
        state.total -= item.price * item.quantity;
        state.items.splice(itemIndex, 1);        // Supprimer du tableau
      }
    },
    
    updateQuantity: (state, action) => {
      const { productId, quantity } = action.payload;
      const item = state.items.find(item => item.id === productId);
      
      if (item) {
        const quantityDiff = quantity - item.quantity;
        item.quantity = quantity;                // Mettre à jour la quantité
        state.total += item.price * quantityDiff; // Mettre à jour le total
      }
    }
  }
});

// Exporter les créateurs d'actions (générés automatiquement par createSlice)
export const { addItem, removeItem, updateQuantity } = cartSlice.actions;

// Créer le store avec configureStore
const store = configureStore({
  reducer: {
    cart: cartSlice.reducer,        // Ajouter le reducer du panier au store
    // Vous pouvez ajouter plus de reducers ici
  }
});

// Utilisation dans les composants (identique à Redux normal)
function ShoppingCart() {
  // Note : state.cart car nous l'avons nommé 'cart' dans configureStore
  const { items, total } = useSelector(state => state.cart);
  const dispatch = useDispatch();
  
  return (
    <div>
      <h2>Shopping Cart</h2>
      <p>Total: ${total.toFixed(2)}</p>
      
      {items.map(item => (
        <div key={item.id}>
          <span>{item.name} - Qty: {item.quantity}</span>
          
          <button onClick={() => dispatch(removeItem(item.id))}>
            Remove
          </button>
          
          <input 
            type="number" 
            value={item.quantity}
            onChange={(e) => dispatch(updateQuantity({
              productId: item.id, 
              quantity: parseInt(e.target.value)
            }))}
          />
        </div>
      ))}
    </div>
  );
}
```

Redux Toolkit est meilleur que Redux vanilla pour quelques raisons clés :

1. **Moins de code répétitif** : Pas besoin d'écrire manuellement les créateurs d'actions

2. **Intégration d'Immer** : Écrire du code qui ressemble à des mutations mais qui est en réalité immutable

3. **Meilleures valeurs par défaut** : configureStore inclut des middlewares utiles automatiquement

4. **Friendly avec TypeScript** : Meilleure inférence de type et support

5. **DevTools inclus** : Les Redux DevTools fonctionnent automatiquement

### Zustand : Gestion d'état simple et flexible

**Zustand** est une bibliothèque légère de gestion d'état qui est beaucoup plus simple que Redux mais plus puissante que Context pour les états complexes.

```javascript
import { create } from 'zustand';

// Créer un store avec l'état et les actions au même endroit
const useCartStore = create((set, get) => ({
  // État initial
  items: [],
  total: 0,
  
  // Actions (fonctions qui mettent à jour l'état)
  addItem: (product) => set((state) => {
    const existingItem = state.items.find(item => item.id === product.id);
    
    if (existingItem) {
      // Mettre à jour la quantité de l'article existant
      return {
        items: state.items.map(item =>
          item.id === product.id 
            ? { ...item, quantity: item.quantity + 1 }
            : item
        ),
        total: state.total + product.price
      };
    } else {
      // Ajouter un nouvel article
      return {
        items: [...state.items, { ...product, quantity: 1 }],
        total: state.total + product.price
      };
    }
  }),
  
  removeItem: (productId) => set((state) => {
    const itemToRemove = state.items.find(item => item.id === productId);
    if (!itemToRemove) return state;
    
    return {
      items: state.items.filter(item => item.id !== productId),
      total: state.total - (itemToRemove.price * itemToRemove.quantity)
    };
  }),
  
  clearCart: () => set({ items: [], total: 0 }),
  
  // Valeurs calculées (getters)
  get itemCount() {
    return get().items.reduce((count, item) => count + item.quantity, 0);
  }
}));

// Utilisation dans les composants - très propre
function ProductCard({ product }) {
  // Obtenir uniquement la fonction dont nous avons besoin
  const addItem = useCartStore(state => state.addItem);
  
  return (
    <div className="product-card">
      <h3>{product.name}</h3>
      <p>${product.price}</p>
      <button onClick={() => addItem(product)}>
        Add to Cart
      </button>
    </div>
  );
}

function CartBadge() {
  // Obtenir uniquement la valeur calculée dont nous avons besoin
  const itemCount = useCartStore(state => state.itemCount);
  
  return (
    <div className="cart-badge">
      Cart ({itemCount})
    </div>
  );
}

function CartList() {
  // Obtenir plusieurs valeurs à la fois
  const { items, total, removeItem } = useCartStore(state => ({
    items: state.items,
    total: state.total,
    removeItem: state.removeItem
  }));
  
  return (
    <div className="cart-list">
      <h3>Your Cart - Total: ${total.toFixed(2)}</h3>
      {items.map(item => (
        <div key={item.id} className="cart-item">
          <span>{item.name} x {item.quantity}</span>
          <button onClick={() => removeItem(item.id)}>
            Remove
          </button>
        </div>
      ))}
    </div>
  );
}
```

Ce qui rend Zustand spécial :

1. **Pas de code répétitif** : Définir l'état et les actions en un seul endroit

2. **Pas de fournisseurs** : Pas besoin d'envelopper votre application dans un composant Provider

3. **Friendly avec TypeScript** : Excellent support TypeScript dès le départ

4. **Petit bundle** : Beaucoup plus petit que Redux

5. **Modèle mental simple** : Juste des hooks qui retournent l'état et les fonctions

#### Modèles avancés de Zustand

Persistance et middleware :

```javascript
import { create } from 'zustand';
import { persist, devtools } from 'zustand/middleware';

// Store avec persistance localStorage et Redux DevTools
const useCartStore = create(
  devtools(                        // Ajoute le support Redux DevTools
    persist(                       // Ajoute la persistance localStorage
      (set, get) => ({
        items: [],
        total: 0,
        
        addItem: (product) => set(
          (state) => ({
            items: [...state.items, { ...product, quantity: 1 }],
            total: state.total + product.price
          }),
          false,                   // Ne pas remplacer tout l'état
          'cart/addItem'           // Nom de l'action pour les outils de développement
        ),
        
        removeItem: (productId) => set(
          (state) => {
            const itemToRemove = state.items.find(item => item.id === productId);
            return {
              items: state.items.filter(item => item.id !== productId),
              total: state.total - (itemToRemove?.price || 0)
            };
          },
          false,
          'cart/removeItem'
        )
      }),
      {
        name: 'cart-storage',      // clé localStorage
        getStorage: () => localStorage, // Méthode de stockage
      }
    )
  )
);

// Abonnements pour les effets secondaires
useCartStore.subscribe(
  (state) => state.items,          // Surveiller le tableau des articles
  (items) => {                     // Callback lorsque les articles changent
    console.log('Cart items updated:', items);
    
    // Mettre à jour le titre de l'onglet du navigateur
    document.title = `Shopping (${items.length}) - MyStore`;
    
    // Suivre les analyses
    analytics.track('Cart Updated', {
      itemCount: items.length,
      cartValue: items.reduce((sum, item) => sum + item.price * item.quantity, 0)
    });
  }
);
```

## Stratégies d'optimisation des performances expliquées

L'état partagé peut causer des problèmes de performance lorsque les composants se re-rendent inutilement. Comprenons pourquoi cela se produit et comment l'éviter.

### Pourquoi les re-rendus inutiles se produisent-ils ?

**Voici le problème fondamental** : dans React, lorsque l'état change, tous les composants qui utilisent cet état se re-rendent, même s'ils n'affichent pas réellement les données modifiées.

```javascript
// Problème : Ce contexte provoque le re-rendu de TOUS les consommateurs lorsque n'importe quelle valeur change
const AppContext = createContext();

function AppProvider({ children }) {
  const [user, setUser] = useState({ name: 'Alice', email: 'alice@example.com' });
  const [cart, setCart] = useState({ items: [], total: 0 });
  const [theme, setTheme] = useState('light');
  
  // Lorsque n'importe laquelle de ces valeurs change, TOUS les composants utilisant useContext(AppContext) se re-rendent
  const value = {
    user, setUser,
    cart, setCart, 
    theme, setTheme
  };
  
  return (
    <AppContext.Provider value={value}>
      {children}
    </AppContext.Provider>
  );
}

// Ce composant ne se soucie que du thème, mais se re-rend lorsque l'utilisateur ou le panier change
function ThemeToggle() {
  const { theme, setTheme } = useContext(AppContext);  // Obtient TOUTES les données du contexte
  
  console.log('ThemeToggle rendering');  // Cela se journalise chaque fois que n'importe quelle valeur du contexte change
  
  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Current theme: {theme}
    </button>
  );
}
```

### Solution 1 : Diviser les contextes pour minimiser les re-rendus

Vous pouvez diviser les grands contextes en contextes plus petits et ciblés comme ceci :

```javascript
// Au lieu d'un seul grand contexte, créer des contextes séparés
const UserContext = createContext();
const CartContext = createContext();  
const ThemeContext = createContext();

function UserProvider({ children }) {
  const [user, setUser] = useState({ name: 'Alice', email: 'alice@example.com' });
  
  // Seuls les composants utilisant UserContext se re-rendent lorsque l'utilisateur change
  const value = { user, setUser };
  
  return (
    <UserContext.Provider value={value}>
      {children}
    </UserContext.Provider>
  );
}

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  
  // Seuls les composants utilisant ThemeContext se re-rendent lorsque le thème change
  const value = { theme, setTheme };
  
  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}

// Maintenant ThemeToggle ne se re-rend que lorsque le thème change
function ThemeToggle() {
  const { theme, setTheme } = useContext(ThemeContext);  // Seules les données du thème
  
  console.log('ThemeToggle rendering');  // Ne se journalise que lorsque le thème change
  
  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Current theme: {theme}
    </button>
  );
}
```

### Solution 2 : Mémoïser les valeurs de contexte pour éviter la recréation d'objets

Le problème est que la création de nouveaux objets dans le rendu provoque des re-rendus inutiles :

```javascript
//   WRONG: Crée de nouveaux objets à chaque rendu
function CartProvider({ children }) {
  const [items, setItems] = useState([]);
  const [total, setTotal] = useState(0);
  
  return (
    <CartContext.Provider value={{
      // Cela crée un NOUVEL objet à chaque fois que CartProvider se rend !
      items,                      // Même valeur, mais nouvelle référence d'objet
      total,                      // Même valeur, mais nouvelle référence d'objet
      addItem: (item) => {        // NOUVELLE fonction à chaque rendu !
        setItems([...items, item]);
      },
      removeItem: (id) => {       // NOUVELLE fonction à chaque rendu !
        setItems(items.filter(item => item.id !== id));
      }
    }}>
      {children}
    </CartContext.Provider>
  );
}
```

C'est mauvais parce que React utilise `Object.is()` pour comparer les valeurs de contexte. Même si les données sont les mêmes, un nouvel objet signifie que tous les consommateurs se re-rendent.

```javascript
//  CORRECT: Mémoïser la valeur du contexte
function CartProvider({ children }) {
  const [items, setItems] = useState([]);
  const [total, setTotal] = useState(0);
  
  // useCallback mémoïse les fonctions - elles ne changent que lorsque les dépendances changent
  const addItem = useCallback((item) => {
    setItems(prevItems => [...prevItems, item]);  // Utiliser la mise à jour de fonction
  }, []);  // Tableau de dépendances vide signifie que cette fonction ne change jamais
  
  const removeItem = useCallback((id) => {
    setItems(prevItems => prevItems.filter(item => item.id !== id));
  }, []);
  
  // useMemo mémoïse l'objet de valeur de contexte
  const value = useMemo(() => ({
    items,
    total,
    addItem,
    removeItem
  }), [items, total, addItem, removeItem]);  // Créer un nouvel objet uniquement lorsque ceux-ci changent
  
  return (
    <CartContext.Provider value={value}>
      {children}
    </CartContext.Provider>
  );
}
```

Ce que font useCallback et useMemo :

* **useCallback(fn, deps)** : Retourne une fonction mémoïsée qui ne change que lorsque les dépendances changent

* **useMemo(fn, deps)** : Retourne une valeur mémoïsée qui ne recalcule que lorsque les dépendances changent

### Solution 3 : Sélectionner uniquement ce dont vous avez besoin

Avec Redux/Zustand, assurez-vous d'être sélectif quant aux données auxquelles vous vous abonnez :

```javascript
//   WRONG: Le composant se re-rend lorsque n'importe quelle donnée du panier change
function CartBadge() {
  const { items, total, addItem, removeItem } = useCartStore();  // Obtient tout !
  
  // Ce composant ne montre que le nombre d'articles, mais se re-rend lorsque le total change
  return (
    <div className="cart-badge">
      Cart ({items.length})
    </div>
  );
}

//  CORRECT: Ne vous abonnez qu'à ce dont vous avez besoin
function CartBadge() {
  // Ne se re-rend que lorsque le tableau des articles change
  const itemCount = useCartStore(state => state.items.length);
  
  return (
    <div className="cart-badge">
      Cart ({itemCount})
    </div>
  );
}

//  ENCORE MIEUX: Utiliser un sélecteur pour les valeurs calculées
function CartBadge() {
  // Ne se re-rend que lorsque le nombre d'articles calculé change
  const itemCount = useCartStore(state => 
    state.items.reduce((count, item) => count + item.quantity, 0)
  );
  
  return (
    <div className="cart-badge">
      Cart ({itemCount})
    </div>
  );
}
```

### Solution 4 : Utiliser React.memo pour les composants coûteux

**React.memo** empêche les re-rendus des composants lorsque les props n'ont pas changé :

```javascript
// Composant coûteux qui effectue des calculs lourds
function ExpensiveProductList({ products, onAddToCart }) {
  console.log('ExpensiveProductList rendering');  // Cela devrait se journaliser rarement
  
  // Simuler un calcul coûteux
  const processedProducts = products.map(product => ({
    ...product,
    discountedPrice: product.price * 0.9,
    categories: product.categories.sort(),
    // ... plus d'opérations coûteuses
  }));
  
  return (
    <div className="product-list">
      {processedProducts.map(product => (
        <div key={product.id} className="product">
          <h3>{product.name}</h3>
          <p>Price: ${product.discountedPrice}</p>
          <button onClick={() => onAddToCart(product)}>
            Add to Cart
          </button>
        </div>
      ))}
    </div>
  );
}

//   Sans memo : Se re-rend chaque fois que le parent se rend
export default ExpensiveProductList;

//  Avec memo : Ne se re-rend que lorsque les props changent réellement
export default React.memo(ExpensiveProductList);

//  Avec comparaison personnalisée : Vous contrôlez quand il se re-rend
export default React.memo(ExpensiveProductList, (prevProps, nextProps) => {
  // Retourner true si les props sont égales (sauter le re-rendu)
  // Retourner false si les props sont différentes (re-rendre)
  
  return (
    prevProps.products.length === nextProps.products.length &&
    prevProps.onAddToCart === nextProps.onAddToCart
  );
});
```

### Solution 5 : Optimiser avec des hooks de sélecteur personnalisés

Vous pouvez créer des hooks de sélecteur réutilisables pour les modèles courants :

```javascript
// Hook personnalisé qui mémoïse les sélecteurs
function useCartSelector(selector) {
  const selectedValue = useCartStore(selector);
  
  // Le sélecteur lui-même doit être mémoïse pour éviter les re-rendus inutiles
  return useMemo(() => selectedValue, [selectedValue]);
}

// Sélecteurs prédéfinis pour les cas d'utilisation courants
const selectItemCount = (state) => state.items.length;
const selectTotal = (state) => state.total;
const selectIsEmpty = (state) => state.items.length === 0;
const selectItemById = (id) => (state) => state.items.find(item => item.id === id);

// Utilisation dans les composants
function CartBadge() {
  const itemCount = useCartStore(selectItemCount);  // Ne se re-rend que lorsque le nombre change
  
  return (
    <span className="cart-badge">{itemCount}</span>
  );
}

function CartTotal() {
  const total = useCartStore(selectTotal);  // Ne se re-rend que lorsque le total change
  
  return (
    <div className="cart-total">
      Total: ${total.toFixed(2)}
    </div>
  );
}

function ProductInCart({ productId }) {
  // Ce sélecteur est créé avec l'ID de produit spécifique
  const selectThisItem = useMemo(
    () => (state) => state.items.find(item => item.id === productId),
    [productId]
  );
  
  const item = useCartStore(selectThisItem);
  
  return (
    <div>
      {item ? `In cart: ${item.quantity}` : 'Not in cart'}
    </div>
  );
}
```

## Test de l'état partagé : Une approche complète

Le test de l'état partagé nécessite des approches différentes de celles utilisées pour tester des composants isolés. Explorons pourquoi cela est plus complexe et quelles stratégies spécifiques nous devons utiliser.

### Pourquoi le test de l'état partagé est différent

Lorsque vous testez des composants isolés, vous passez généralement des props directement au composant, vous simulez les dépendances externes et vous testez la sortie du composant en fonction d'entrées spécifiques.

Mais avec l'état partagé, vous faites face à des défis supplémentaires :

* **Dépendances à l'état externe** : Les composants dépendent du contexte, des stores Redux ou de l'état global qui doit être fourni

* **Synchronisation de l'état** : Vous devez tester que plusieurs composants restent synchronisés lorsque l'état change

* **Configuration du fournisseur** : Les composants utilisant le contexte planteront sans les fournisseurs appropriés

* **Mutations de l'état** : Tester que l'état se met à jour correctement à travers plusieurs composants

* **Comportement d'intégration** : S'assurer que tout le système de gestion d'état fonctionne ensemble

Cela signifie que vous aurez besoin de différentes stratégies de test. Vous devrez fournir l'infrastructure de gestion d'état correcte, tester comment les changements dans un composant affectent les autres, gérer gracieusement les états de chargement, les erreurs et les opérations asynchrones, et tester que les optimisations fonctionnent correctement.

Explorons chaque approche en profondeur.

### Test du contexte React

**Le défi** : Les composants utilisant le contexte ont besoin d'un fournisseur pour fonctionner, et vous devez tester à la fois la logique du contexte et le comportement des composants.

**Pourquoi le test du contexte est unique** : Contrairement aux composants réguliers qui reçoivent des props directement, les consommateurs de contexte dépendent de la présence d'un fournisseur dans l'arbre des composants. Cela crée plusieurs défis de test :

1. Les composants planteront s'ils sont utilisés en dehors d'un fournisseur

2. Chaque test a besoin de sa propre instance de fournisseur pour éviter les interférences entre les tests

3. Vous devez tester que le fournisseur et le consommateur fonctionnent correctement ensemble

4. Le test des hooks `useContext` nécessite une configuration spéciale

Voyons quelques stratégies spécifiques au contexte.

#### Configuration des tests de contexte :

```javascript
import { render, screen, fireEvent } from '@testing-library/react';
import { createContext, useContext, useState } from 'react';

// Notre configuration de contexte (comme avant)
const CartContext = createContext();

function useCart() {
  const context = useContext(CartContext);
  if (context === undefined) {
    throw new Error('useCart must be used within a CartProvider');
  }
  return context;
}

function CartProvider({ children }) {
  const [items, setItems] = useState([]);
  const [total, setTotal] = useState(0);
  
  const addItem = (product) => {
    setItems(prev => [...prev, product]);
    setTotal(prev => prev + product.price);
  };
  
  const removeItem = (productId) => {
    setItems(prev => {
      const updatedItems = prev.filter(item => item.id !== productId);
      const removedItem = prev.find(item => item.id === productId);
      
      if (removedItem) {
        setTotal(current => current - removedItem.price);
      }
      
      return updatedItems;
    });
  };
  
  const value = { items, total, addItem, removeItem };
  
  return (
    <CartContext.Provider value={value}>
      {children}
    </CartContext.Provider>
  );
}

// Composant de test qui utilise notre contexte
function TestCartComponent() {
  const { items, total, addItem, removeItem } = useCart();
  
  return (
    <div>
      <div data-testid="item-count">{items.length}</div>
      <div data-testid="total">${total.toFixed(2)}</div>
      
      <button 
        onClick={() => addItem({ id: 1, name: 'Test Product', price: 10 })}
        data-testid="add-item"
      >
        Add Item
      </button>
      
      {items.map(item => (
        <div key={item.id} data-testid={`item-${item.id}`}>
          <span>{item.name}</span>
          <button 
            onClick={() => removeItem(item.id)}
            data-testid={`remove-${item.id}`}
          >
            Remove
          </button>
        </div>
      ))}
    </div>
  );
}

// Fonction d'aide pour rendre les composants avec CartProvider
function renderWithCartProvider(component) {
  return render(
    <CartProvider>
      {component}
    </CartProvider>
  );
}
```

#### Écrire des tests de contexte :

```javascript
describe('Cart Context functionality', () => {
  test('should start with empty cart', () => {
    renderWithCartProvider(<TestCartComponent />);
    
    // Vérifier l'état initial
    expect(screen.getByTestId('item-count')).toHaveTextContent('0');
    expect(screen.getByTestId('total')).toHaveTextContent('$0.00');
  });
  
  test('should add item to cart', () => {
    renderWithCartProvider(<TestCartComponent />);
    
    // Cliquer sur le bouton d'ajout
    const addButton = screen.getByTestId('add-item');
    fireEvent.click(addButton);
    
    // Vérifier que l'article a été ajouté
    expect(screen.getByTestId('item-count')).toHaveTextContent('1');
    expect(screen.getByTestId('total')).toHaveTextContent('$10.00');
    expect(screen.getByTestId('item-1')).toBeInTheDocument();
    expect(screen.getByText('Test Product')).toBeInTheDocument();
  });
  
  test('should remove item from cart', () => {
    renderWithCartProvider(<TestCartComponent />);
    
    // Ajouter un article d'abord
    fireEvent.click(screen.getByTestId('add-item'));
    
    // Vérifier que l'article est là
    expect(screen.getByTestId('item-count')).toHaveTextContent('1');
    
    // Supprimer l'article
    fireEvent.click(screen.getByTestId('remove-1'));
    
    // Vérifier que l'article a été supprimé
    expect(screen.getByTestId('item-count')).toHaveTextContent('0');
    expect(screen.getByTestId('total')).toHaveTextContent('$0.00');
    expect(screen.queryByTestId('item-1')).not.toBeInTheDocument();
  });
  
  test('should handle multiple items', () => {
    renderWithCartProvider(<TestCartComponent />);
    
    // Ajouter plusieurs articles
    fireEvent.click(screen.getByTestId('add-item'));
    fireEvent.click(screen.getByTestId('add-item'));
    fireEvent.click(screen.getByTestId('add-item'));
    
    // Vérifier le compte et le total
    expect(screen.getByTestId('item-count')).toHaveTextContent('3');
    expect(screen.getByTestId('total')).toHaveTextContent('$30.00');
  });
  
  test('should throw error when used outside provider', () => {
    // Mock console.error pour éviter la sortie d'erreur dans les tests
    const consoleSpy = jest.spyOn(console, 'error').mockImplementation(() => {});
    
    // Cela devrait lancer une erreur
    expect(() => {
      render(<TestCartComponent />);  // Pas de wrapper CartProvider
    }).toThrow('useCart must be used within a CartProvider');
    
    consoleSpy.mockRestore();
  });
  
  test('should handle edge cases', () => {
    renderWithCartProvider(<TestCartComponent />);
    
    // Essayer de supprimer un article qui n'existe pas
    const initialCount = screen.getByTestId('item-count').textContent;
    
    // Cela ne devrait pas planter ou changer quoi que ce soit
    fireEvent.click(screen.getByTestId('add-item'));
    fireEvent.click(screen.getByTestId('remove-999'));  // Article inexistant
    
    // Le compte devrait toujours être 1
    expect(screen.getByTestId('item-count')).toHaveTextContent('1');
  });
});
```

#### Tester le contexte avec différents états initiaux :

```javascript
// Fournisseur personnalisé pour les tests avec un état initial spécifique
function TestCartProvider({ children, initialItems = [], initialTotal = 0 }) {
  const [items, setItems] = useState(initialItems);
  const [total, setTotal] = useState(initialTotal);
  
  // Même logique que CartProvider
  const addItem = (product) => {
    setItems(prev => [...prev, product]);
    setTotal(prev => prev + product.price);
  };
  
  const removeItem = (productId) => {
    setItems(prev => {
      const updatedItems = prev.filter(item => item.id !== productId);
      const removedItem = prev.find(item => item.id === productId);
      
      if (removedItem) {
        setTotal(current => current - removedItem.price);
      }
      
      return updatedItems;
    });
  };
  
  const value = { items, total, addItem, removeItem };
  
  return (
    <CartContext.Provider value={value}>
      {children}
    </CartContext.Provider>
  );
}

describe('Cart Context with initial state', () => {
  test('should work with pre-populated cart', () => {
    const initialItems = [
      { id: 1, name: 'Existing Product', price: 15 },
      { id: 2, name: 'Another Product', price: 25 }
    ];
    
    render(
      <TestCartProvider initialItems={initialItems} initialTotal={40}>
        <TestCartComponent />
      </TestCartProvider>
    );
    
    // Devrait afficher les articles existants
    expect(screen.getByTestId('item-count')).toHaveTextContent('2');
    expect(screen.getByTestId('total')).toHaveTextContent('$40.00');
    expect(screen.getByText('Existing Product')).toBeInTheDocument();
    expect(screen.getByText('Another Product')).toBeInTheDocument();
  });
});
```

### Test des stores Redux

**Pourquoi le test Redux nécessite des approches différentes :** Redux introduit un système de gestion d'état prévisible mais complexe qui nécessite des tests à plusieurs niveaux :

1. **Test de fonction pure** : Les reducers sont des fonctions pures qui peuvent être testées en isolation

2. **Test des créateurs d'actions** : S'assurer que les actions sont créées correctement

3. **Test des composants connectés** : Les composants qui utilisent `useSelector` et `useDispatch` nécessitent une configuration de store

4. **Test d'intégration** : Tester tout le flux Redux de l'envoi d'action à la mise à jour d'état au re-rendu du composant

5. **Test des actions asynchrones** : Tester les thunks, sagas, ou autres middlewares asynchrones

Le test Redux se concentre sur trois domaines : les créateurs d'actions, les reducers et les composants connectés.

#### Test des reducers (fonctions pures) :

```javascript
import cartReducer, { addItem, removeItem, updateQuantity } from './cartSlice';

describe('Cart reducer', () => {
  const initialState = {
    items: [],
    total: 0,
    itemCount: 0
  };
  
  test('should return initial state when called with undefined', () => {
    // Le reducer doit gérer l'état undefined
    const result = cartReducer(undefined, { type: 'unknown' });
    expect(result).toEqual(initialState);
  });
  
  test('should handle addItem action', () => {
    const product = { id: 1, name: 'Test Product', price: 10 };
    const action = addItem(product);
    
    const result = cartReducer(initialState, action);
    
    expect(result).toEqual({
      items: [{ ...product, quantity: 1 }],
      total: 10,
      itemCount: 1
    });
    
    // L'état initial doit rester inchangé (test d'immuabilité)
    expect(initialState.items).toHaveLength(0);
  });
  
  test('should increase quantity for existing item', () => {
    const existingState = {
      items: [{ id: 1, name: 'Test Product', price: 10, quantity: 1 }],
      total: 10,
      itemCount: 1
    };
    
    const product = { id: 1, name: 'Test Product', price: 10 };
    const action = addItem(product);
    
    const result = cartReducer(existingState, action);
    
    expect(result).toEqual({
      items: [{ id: 1, name: 'Test Product', price: 10, quantity: 2 }],
      total: 20,
      itemCount: 2
    });
  });
  
  test('should handle removeItem action', () => {
    const existingState = {
      items: [
        { id: 1, name: 'Product 1', price: 10, quantity: 2 },
        { id: 2, name: 'Product 2', price: 15, quantity: 1 }
      ],
      total: 35,
      itemCount: 3
    };
    
    const action = removeItem(1);
    const result = cartReducer(existingState, action);
    
    expect(result).toEqual({
      items: [{ id: 2, name: 'Product 2', price: 15, quantity: 1 }],
      total: 15,
      itemCount: 1
    });
  });
  
  test('should handle updateQuantity action', () => {
    const existingState = {
      items: [{ id: 1, name: 'Test Product', price: 10, quantity: 2 }],
      total: 20,
      itemCount: 2
    };
    
    const action = updateQuantity({ productId: 1, quantity: 5 });
    const result = cartReducer(existingState, action);
    
    expect(result).toEqual({
      items: [{ id: 1, name: 'Test Product', price: 10, quantity: 5 }],
      total: 50,
      itemCount: 5
    });
  });
  
  test('should remove item when quantity is set to 0', () => {
    const existingState = {
      items: [{ id: 1, name: 'Test Product', price: 10, quantity: 2 }],
      total: 20,
      itemCount: 2
    };
    
    const action = updateQuantity({ productId: 1, quantity: 0 });
    const result = cartReducer(existingState, action);
    
    expect(result).toEqual({
      items: [],
      total: 0,
      itemCount: 0
    });
  });
});
```

#### Test des composants connectés à Redux :

```javascript
import { render, screen, fireEvent } from '@testing-library/react';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import cartReducer from './cartSlice';
import ConnectedProductCard from './ProductCard';

// Helper pour créer un store de test avec un état initial
function createTestStore(initialState = {}) {
  return configureStore({
    reducer: {
      cart: cartReducer
    },
    preloadedState: {
      cart: {
        items: [],
        total: 0,
        itemCount: 0,
        ...initialState
      }
    }
  });
}

// Helper pour rendre les composants avec le store Redux
function renderWithStore(component, store) {
  return render(
    <Provider store={store}>
      {component}
    </Provider>
  );
}

describe('ConnectedProductCard', () => {
  const mockProduct = {
    id: 1,
    name: 'Test Product',
    price: 25,
    description: 'A test product'
  };
  
  test('should display product information', () => {
    const store = createTestStore();
    
    renderWithStore(<ConnectedProductCard product={mockProduct} />, store);
    
    expect(screen.getByText('Test Product')).toBeInTheDocument();
    expect(screen.getByText('$25')).toBeInTheDocument();
    expect(screen.getByText('A test product')).toBeInTheDocument();
  });
  
  test('should add item to cart when button clicked', () => {
    const store = createTestStore();
    
    renderWithStore(<ConnectedProductCard product={mockProduct} />, store);
    
    // Initialement, le panier doit être vide
    expect(store.getState().cart.items).toHaveLength(0);
    
    // Cliquer sur le bouton d'ajout au panier
    fireEvent.click(screen.getByRole('button', { name: /add to cart/i }));
    
    // Vérifier que l'article a été ajouté au store
    const cartState = store.getState().cart;
    expect(cartState.items).toHaveLength(1);
    expect(cartState.items[0]).toEqual({ ...mockProduct, quantity: 1 });
    expect(cartState.total).toBe(25);
  });
  
  test('should show "In Cart" when item is already in cart', () => {
    const store = createTestStore({
      items: [{ ...mockProduct, quantity: 1 }],
      total: 25,
      itemCount: 1
    });
    
    renderWithStore(<ConnectedProductCard product={mockProduct} />, store);
    
    // Le bouton doit être désactivé et afficher "In Cart"
    const button = screen.getByRole('button');
    expect(button).toBeDisabled();
    expect(button).toHaveTextContent('In Cart');
  });
});
```

#### Test d'intégration avec plusieurs composants connectés :

```javascript
import { render, screen, fireEvent } from '@testing-library/react';
import { Provider } from 'react-redux';
import { createTestStore } from './test-utils';
import App from './App';

describe('Cart integration', () => {
  test('should update cart badge when item is added', () => {
    const store = createTestStore();
    
    render(
      <Provider store={store}>
        <App />
      </Provider>
    );
    
    // Initialement, aucun badge de panier ne doit être visible
    expect(screen.queryByText(/cart \(/)).not.toBeInTheDocument();
    
    // Ajouter un produit au panier
    const addButton = screen.getByRole('button', { name: /add to cart/i });
    fireEvent.click(addButton);
    
    // Le badge du panier doit maintenant afficher 1 article
    expect(screen.getByText('Cart (1)')).toBeInTheDocument();
  });
  
  test('should show cart items when cart dropdown is opened', async () => {
    const store = createTestStore({
      items: [
        { id: 1, name: 'Test Product', price: 10, quantity: 1 }
      ],
      total: 10,
      itemCount: 1
    });
    
    render(
      <Provider store={store}>
        <App />
      </Provider>
    );
    
    // Ouvrir le menu déroulant du panier
    fireEvent.click(screen.getByRole('button', { name: /cart/i }));
    
    // Doit afficher l'article du panier
    expect(screen.getByText('Test Product')).toBeInTheDocument();
    expect(screen.getByText('$10.00')).toBeInTheDocument();
  });
  
  test('should remove item when remove button is clicked', () => {
    const store = createTestStore({
      items: [
        { id: 1, name: 'Test Product', price: 10, quantity: 1 }
      ],
      total: 10,
      itemCount: 1
    });
    
    render(
      <Provider store={store}>
        <App />
      </Provider>
    );
    
    // Ouvrir le menu déroulant du panier
    fireEvent.click(screen.getByRole('button', { name: /cart/i }));
    
    // Supprimer l'article
    fireEvent.click(screen.getByRole('button', { name: /remove/i }));
    
    // L'article doit avoir disparu
    expect(screen.queryByText('Test Product')).not.toBeInTheDocument();
    
    // Le badge du panier doit avoir disparu
    expect(screen.queryByText(/cart \(/)).not.toBeInTheDocument();
  });
});
```

### Test des hooks personnalisés pour la gestion d'état :

**Pourquoi le test des hooks personnalisés est unique :** Les hooks personnalisés ne peuvent pas être testés comme des fonctions régulières car ils utilisent des hooks React en interne, qui ne peuvent être appelés qu'à l'intérieur de composants React. Cela crée des défis de test spécifiques :

1. **Exigence de contexte React** : Les hooks doivent être appelés à l'intérieur d'un composant React ou d'un environnement de test

2. **Persistance de l'état** : Tester que l'état persiste correctement entre les rendus

3. **Test des effets** : Tester le nettoyage de useEffect et les changements de dépendances

4. **Isolation** : Tester la logique des hooks séparément des composants UI

5. **Cycles de rendu multiples** : Tester comment les hooks se comportent à travers les re-rendus

Vous aurez besoin de certaines utilitaires de test spéciaux :

* `renderHook()` : Rend un hook dans un composant de test

* `act()` : Assure que les mises à jour d'état sont traitées avant les assertions

* Mock timers pour tester les effets retardés

```javascript
import { renderHook, act } from '@testing-library/react';
import { useCart } from './useCart';

describe('useCart hook', () => {
  test('should initialize with empty cart', () => {
    const { result } = renderHook(() => useCart());
    
    expect(result.current.items).toEqual([]);
    expect(result.current.total).toBe(0);
    expect(result.current.itemCount).toBe(0);
  });
  
  test('should add item to cart', () => {
    const { result } = renderHook(() => useCart());
    
    const product = { id: 1, name: 'Test Product', price: 10 };
    
    act(() => {
      result.current.addItem(product);
    });
    
    expect(result.current.items).toHaveLength(1);
    expect(result.current.items[0]).toEqual({ ...product, quantity: 1 });
    expect(result.current.total).toBe(10);
    expect(result.current.itemCount).toBe(1);
  });
  
  test('should remove item from cart', () => {
    const { result } = renderHook(() => useCart());
    
    const product = { id: 1, name: 'Test Product', price: 10 };
    
    // Ajouter un article d'abord
    act(() => {
      result.current.addItem(product);
    });
    
    // Puis le supprimer
    act(() => {
      result.current.removeItem(1);
    });
    
    expect(result.current.items).toHaveLength(0);
    expect(result.current.total).toBe(0);
    expect(result.current.itemCount).toBe(0);
  });
  
  test('should handle multiple items', () => {
    const { result } = renderHook(() => useCart());
    
    const product1 = { id: 1, name: 'Product 1', price: 10 };
    const product2 = { id: 2, name: 'Product 2', price: 15 };
    
    act(() => {
      result.current.addItem(product1);
      result.current.addItem(product2);
    });
    
    expect(result.current.items).toHaveLength(2);
    expect(result.current.total).toBe(25);
    expect(result.current.itemCount).toBe(2);
  });
});
```

## Quand utiliser chaque approche : Un cadre de décision

Choisir la bonne approche de gestion d'état est crucial pour des applications maintenables. Voici comment décider :

### Arbre de décision pour la gestion d'état

1. L'état est-il uniquement nécessaire par un composant et ses enfants directs ? → Utiliser l'état local avec useState :

```javascript
// Bon pour : Les entrées de formulaire, les bascules, les données spécifiques au composant
function ContactForm() {
  const [name, setName] = useState('');        // Seule cette forme en a besoin
  const [email, setEmail] = useState('');      // Seule cette forme en a besoin
  const [isSubmitting, setIsSubmitting] = useState(false); // Seule cette forme en a besoin
  
  return (
    <form>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <input value={email} onChange={(e) => setEmail(e.target.value)} />
      <button disabled={isSubmitting}>Submit</button>
    </form>
  );
}
```

2. 3-5 composants ont-ils besoin des mêmes données, et celles-ci ne changent-elles pas fréquemment ? → Utiliser React Context :

```javascript
// Bon pour : L'authentification des utilisateurs, les paramètres de thème, les préférences de langue
const ThemeContext = createContext();

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');  // Change rarement
  
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

// Utilisé par les composants Header, Sidebar, Settings
```

3. De nombreux composants non liés ont-ils besoin des mêmes données qui changent fréquemment ? → Utiliser une bibliothèque de gestion d'état (Redux, Zustand) :

```javascript
// Bon pour : Panier d'achat, formulaires complexes, données en temps réel
const useCartStore = create((set) => ({
  items: [],
  total: 0,
  addItem: (product) => set((state) => ({
    items: [...state.items, product],
    total: state.total + product.price
  }))
}));

// Utilisé par ProductCard, CartBadge, CartSidebar, Checkout, etc.
```

4. Devez-vous encapsuler une logique réutilisable à travers plusieurs composants ? → Créer des hooks personnalisés :

```javascript
// Bon pour : Appels API, validation de formulaire, calculs complexes
function useApi(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    fetch(url)
      .then(response => response.json())
      .then(setData)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [url]);
  
  return { data, loading, error };
}

// Réutilisable à travers n'importe quel composant qui a besoin de données API
```

### Comparaison détaillée des approches

Voici un tableau utile qui présente chaque approche avec leurs meilleurs cas d'utilisation, avantages et inconvénients :

| Approche | Meilleur pour | Avantages | Inconvénients | Courbe d'apprentissage |
| --- | --- | --- | --- | --- |
| **État local** | Entrées de formulaire, bascules UI, données spécifiques au composant | Simple, rapide, intégré | Portée limitée, prop drilling | Facile |
| **Contexte** | Thème, authentification, état partagé modéré | Pas de prop drilling, intégré | Peut causer des re-rendus, pas idéal pour les mises à jour fréquentes | Moyen |
| **Redux** | État complexe, débogage time-travel, grandes équipes | Prévisible, excellents DevTools, scalable | Beaucoup de code répétitif, courbe d'apprentissage | Difficile |
| **Redux Toolkit** | Projets Redux modernes | Moins de code répétitif que Redux, bons patterns | Toujours complexe, opinionné | Moyen-Difficile |
| **Zustand** | État global simple, projets modernes | Code répétitif minimal, friendly TypeScript, petit | Moins d'écosystème, bibliothèque plus récente | Facile-Moyen |
| **Hooks personnalisés** | Logique réutilisable, complexité modérée | Composable, réutilisable, testable | Peut devenir complexe, besoin de bons patterns | Moyen |

### Exemples concrets de quand utiliser chaque approche

#### Exemples d'état local

L'état local excelle lorsque les données sont **temporaires, spécifiques au composant et n'ont pas besoin d'être partagées**. Il offre les meilleures performances et le code le plus simple car il n'y a pas de surcharge des systèmes de gestion d'état.

```javascript
//  Parfait pour l'état local
function ImageGallery({ images }) {
  const [currentIndex, setCurrentIndex] = useState(0);    // Seule cette composante s'en soucie
  const [isFullscreen, setIsFullscreen] = useState(false); // Seule cette composante s'en soucie
  
  return (
    <div className="gallery">
      <img src={images[currentIndex]} />
      <button onClick={() => setCurrentIndex(currentIndex + 1)}>Next</button>
      <button onClick={() => setIsFullscreen(true)}>Fullscreen</button>
    </div>
  );
}

//  Bon pour les formulaires
function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({});
  
  // Tout cet état est spécifique à ce formulaire
}
```

L'état local fonctionne ici parce que :

* L'état est contenu dans le composant qui l'utilise

* Aucune souscription externe ou fournisseur n'est nécessaire

* C'est facile à raisonner et à tester

* L'état s'efface automatiquement lorsque le composant est démonté

* Le composant est autonome et réutilisable

#### Exemples de contexte

Le contexte fonctionne mieux pour les **données stables dont de nombreux composants ont besoin mais qui changent rarement**. Il élimine le prop drilling tout en évitant la complexité des bibliothèques de gestion d'état complètes.

```javascript
//  Parfait pour le contexte - utilisé par de nombreux composants, change rarement
const AuthContext = createContext();

function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  
  // Le statut d'authentification ne change pas fréquemment
  // De nombreux composants doivent savoir si l'utilisateur est connecté
  
  return (
    <AuthContext.Provider value={{ user, isLoggedIn, setUser, setIsLoggedIn }}>
      {children}
    </AuthContext.Provider>
  );
}

//  Bon pour les paramètres de thème
const ThemeContext = createContext();

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  const [fontSize, setFontSize] = useState('medium');
  
  // Le thème change rarement mais affecte de nombreux composants
}
```

Le contexte excelle ici parce que :

* **Large portée, données stables** : De nombreux composants ont besoin de ces informations, mais elles ne changent pas souvent

* **Solution intégrée** : Aucune dépendance externe requise

* **Mises à jour automatiques** : Tous les consommateurs se re-rendent automatiquement lorsque le contexte change

* **Frontières claires** : Facile à comprendre quels composants ont accès aux données

* **Complexité raisonnable** : Plus complexe que l'état local mais beaucoup plus simple que Redux

Quand le contexte a du mal :

* **Mises à jour fréquentes** : Chaque changement de contexte provoque le re-rendu de tous les consommateurs

* **Logique d'état complexe** : Plusieurs pièces d'état liées deviennent ingérables

* **Performance critique** : Un grand nombre de consommateurs peut causer des problèmes de performance

#### Exemples Redux/Zustand

Ces bibliothèques brillent lorsque vous avez un **état complexe et interconnecté qui change fréquemment et doit être accessible par de nombreux composants non liés**. Elles fournissent des mises à jour prévisibles, des outils de débogage et des optimisations de performance.

```javascript
//  Parfait pour Redux/Zustand - état complexe, nombreux composants, mises à jour fréquentes
const useShoppingStore = create((set, get) => ({
  // Données du panier
  cart: { items: [], total: 0 },
  
  // Données de l'utilisateur  
  user: { profile: null, preferences: {} },
  
  // État de l'UI
  ui: { 
    sidebarOpen: false, 
    currentPage: 'home',
    notifications: []
  },
  
  // De nombreuses actions qui mettent à jour différentes parties de l'état
  addToCart: (product) => set((state) => ({
    cart: {
      ...state.cart,
      items: [...state.cart.items, { ...product, quantity: 1 }],
      total: state.cart.total + product.price
    }
  })),
  
  updateUserProfile: (profile) => set((state) => ({
    user: { ...state.user, profile }
  })),
  
  showNotification: (message) => set((state) => ({
    ui: {
      ...state.ui,
      notifications: [...state.ui.notifications, { id: Date.now(), message }]
    }
  }))
}));

// Utilisé par : ProductCard, CartBadge, UserProfile, Sidebar, Notifications, etc.
```

Pourquoi les bibliothèques de gestion d'état excellent ici :

* **Logique centralisée** : Toutes les modifications d'état passent par des mécanismes de mise à jour prévisibles

* **Optimisation des performances** : Les bibliothèques fournissent des abonnements basés sur des sélecteurs pour minimiser les re-rendus

* **Outils de débogage** : Redux DevTools, débogage time-travel, suivi des actions

* **Évolutivité** : Peut gérer des relations d'état complexes et des opérations asynchrones

* **Consistance de l'équipe** : Des modèles établis que plusieurs développeurs peuvent suivre

* **Support des middlewares** : Journalisation, persistance, gestion des erreurs peuvent être ajoutées systématiquement

**Redux** est idéal pour les grandes équipes, les flux asynchrones complexes, le besoin de prévisibilité stricte. **Zustand** est idéal pour les applications modernes qui veulent les avantages de Redux sans le code répétitif. Et **Recoil/Jotai** est idéal pour les mises à jour réactives fines et les dépendances complexes.

#### Exemples de hooks personnalisés

Les hooks personnalisés excellent lorsque vous avez une **logique avec état dont plusieurs composants ont besoin, mais où la logique elle-même est plus importante que les données**. Ils fournissent de la composition et de la réutilisabilité tout en gardant la complexité contenue.

```javascript
//  Parfait pour les hooks personnalisés - logique réutilisable
function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });
  
  const setValue = (value) => {
    try {
      setStoredValue(value);
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error('Error saving to localStorage:', error);
    }
  };
  
  return [storedValue, setValue];
}

//  Logique API réutilisable
function useApi(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    let cancelled = false;
    
    fetch(url)
      .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
      })
      .then(data => {
        if (!cancelled) {
          setData(data);
          setLoading(false);
        }
      })
      .catch(error => {
        if (!cancelled) {
          setError(error);
          setLoading(false);
        }
      });
    
    return () => { cancelled = true; };
  }, [url]);
  
  return { data, loading, error };
}

// Peut être utilisé dans n'importe quel composant qui a besoin de données API
function UserProfile({ userId }) {
  const { data: user, loading, error } = useApi(`/api/users/${userId}`);
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return <div>Welcome, {user.name}!</div>;
}
```

Pourquoi les hooks personnalisés sont parfaits ici :

* **Réutilisabilité de la logique** : Le même comportement avec état peut être utilisé dans plusieurs composants

* **Composition** : Les hooks peuvent être combinés et construits les uns sur les autres

* **Séparation des préoccupations** : La logique métier est séparée du rendu de l'UI

* **Testabilité** : La logique peut être testée indépendamment des composants

* **Flexibilité** : Chaque composant peut utiliser le hook différemment tout en partageant la logique de base

* **Pas de surcharge de fournisseur** : Contrairement au contexte, aucun composant wrapper n'est nécessaire

Quand les hooks personnalisés fonctionnent le mieux :

* **Préoccupations transversales** : Authentification, appels API, validation de formulaire, stockage local

* **Calculs complexes** : Traitement de données dont plusieurs composants ont besoin

* **Intégrations tierces** : Enveloppement de bibliothèques externes avec des interfaces React-friendly

* **Comportement avec état** : Gestion de machines d'état complexes ou de processus multi-étapes

## Pièges courants et comment les éviter

Comprendre les erreurs courantes vous aide à écrire un meilleur code, plus maintenable.

### Piège 1 : L'enfer du contexte (trop de fournisseurs imbriqués)

**Le problème :**

```javascript
//   WRONG: Trop de fournisseurs imbriqués rendent le code difficile à lire et à maintenir
function App() {
  return (
    <UserProvider>
      <ThemeProvider>
        <CartProvider>
          <NotificationProvider>
            <AnalyticsProvider>
              <FeatureFlagProvider>
                <LocaleProvider>
                  <Router>
                    <Routes />
                  </Router>
                </LocaleProvider>
              </FeatureFlagProvider>
            </AnalyticsProvider>
          </NotificationProvider>
        </CartProvider>
      </ThemeProvider>
    </UserProvider>
  );
}
```

**Pourquoi c'est mauvais :**

* Difficile à lire et à comprendre la hiérarchie des composants

* Difficile de réorganiser ou de supprimer les fournisseurs

* Chaque niveau d'imbrication ajoute de la complexité

* Les tests deviennent difficiles avec autant de fournisseurs

**Solution 1 : Combiner les fournisseurs liés**

```javascript
//  MIEUX : Regrouper les fournisseurs liés ensemble
function AppProviders({ children }) {
  return (
    <UserProvider>
      <ThemeProvider>
        <LocaleProvider>
          {children}
        </LocaleProvider>
      </ThemeProvider>
    </UserProvider>
  );
}

function ShoppingProviders({ children }) {
  return (
    <CartProvider>
      <NotificationProvider>
        {children}
      </NotificationProvider>
    </CartProvider>
  );
}

function App() {
  return (
    <AppProviders>
      <ShoppingProviders>
        <Router>
          <Routes />
        </Router>
      </ShoppingProviders>
    </AppProviders>
  );
}
```

**Solution 2 : Utiliser une bibliothèque de gestion d'état à la place**

```javascript
//  ENCORE MIEUX : Utiliser Zustand ou Redux pour un état complexe
const useAppStore = create((set) => ({
  user: null,
  theme: 'light',
  cart: { items: [], total: 0 },
  notifications: [],
  
  // Toutes les actions au même endroit
  setUser: (user) => set({ user }),
  setTheme: (theme) => set({ theme }),
  addToCart: (product) => set((state) => ({
    cart: {
      items: [...state.cart.items, product],
      total: state.cart.total + product.price
    }
  })),
  addNotification: (notification) => set((state) => ({
    notifications: [...state.notifications, notification]
  }))
}));

function App() {
  // Pas de fournisseurs nécessaires ! Utilisez simplement le store directement
  return (
    <Router>
      <Routes />
    </Router>
  );
}
```

### Piège 2 : Valeurs de contexte massives provoquant des re-rendus inutiles

**Le problème :**

```javascript
//   WRONG: Mettre tout dans un seul contexte provoque le re-rendu de tous les composants lorsque n'importe quel état change
const AppContext = createContext();

function AppProvider({ children }) {
  const [user, setUser] = useState(null);
  const [cart, setCart] = useState({ items: [], total: 0 });
  const [theme, setTheme] = useState('light');
  const [notifications, setNotifications] = useState([]);
  const [products, setProducts] = useState([]);
  const [orders, setOrders] = useState([]);
  // ... 15 autres morceaux d'état
  
  // Chaque fois que n'importe quel état change, TOUS les composants se re-rendent !
  const value = {
    user, setUser,
    cart, setCart,
    theme, setTheme,
    notifications, setNotifications,
    products, setProducts,
    orders, setOrders,
    // ... et tout le reste
  };
  
  return (
    <AppContext.Provider value={value}>
      {children}
    </AppContext.Provider>
  );
}

// Ce composant n'a besoin que du thème, mais se re-rend lorsque l'utilisateur, le panier, etc. changent
function ThemeToggle() {
  const { theme, setTheme } = useContext(AppContext);  // Obtient TOUTES les données du contexte
  
  console.log('ThemeToggle rendering');  // Cela se journalise beaucoup trop souvent !
  
  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Theme: {theme}
    </button>
  );
}
```

**Pourquoi c'est mauvais :**

* Les composants se re-rendent lorsque l'état non lié change

* Mauvaise performance à mesure que votre application grandit

* Difficile à déboguer quels changements d'état provoquent quels re-rendus

* Difficile d'optimiser les morceaux individuels d'état

**Solution : Séparer les contextes par domaine**

```javascript
//  MIEUX : Contextes séparés pour différents domaines
const UserContext = createContext();
const CartContext = createContext();  
const ThemeContext = createContext();
const NotificationContext = createContext();

function UserProvider({ children }) {
  const [user, setUser] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  
  // Seule l'état lié à l'utilisateur ici
  const value = useMemo(() => ({
    user, 
    setUser, 
    isAuthenticated, 
    setIsAuthenticated
  }), [user, isAuthenticated]);
  
  return (
    <UserContext.Provider value={value}>
      {children}
    </UserContext.Provider>
  );
}

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  const [fontSize, setFontSize] = useState('medium');
  
  // Seule l'état lié au thème ici
  const value = useMemo(() => ({
    theme, 
    setTheme, 
    fontSize, 
    setFontSize
  }), [theme, fontSize]);
  
  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}

// Maintenant ThemeToggle ne se re-rend que lorsque le thème change
function ThemeToggle() {
  const { theme, setTheme } = useContext(ThemeContext);  // Seules les données du thème
  
  console.log('ThemeToggle rendering');  // Ne se journalise que lorsque le thème change
  
  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Theme: {theme}
    </button>
  );
}
```

### Piège 3 : Ne pas mémoïser les valeurs de contexte

**Le problème :**

```javascript
//   WRONG: Crée de nouveaux objets à chaque rendu
function CartProvider({ children }) {
  const [items, setItems] = useState([]);
  const [total, setTotal] = useState(0);
  
  return (
    <CartContext.Provider value={{
      // Cela crée un NOUVEL objet à chaque fois que CartProvider se rend !
      items,                      // Même données mais nouvelle référence d'objet
      total,                      // Même données mais nouvelle référence d'objet
      addItem: (item) => {        // NOUVELLE fonction à chaque rendu !
        setItems([...items, item]);
      },
      removeItem: (id) => {       // NOUVELLE fonction à chaque rendu !
        setItems(items.filter(item => item.id !== id));
      }
    }}>
      {children}
    </CartContext.Provider>
  );
}
```

**Pourquoi c'est mauvais :**

* React utilise `Object.is()` pour comparer les valeurs de contexte

* Même si les données sont les mêmes, de nouveaux objets provoquent le re-rendu de tous les consommateurs

* Les nouvelles fonctions rompent l'optimisation dans les composants enfants

* La performance se dégrade à mesure que plus de composants utilisent le contexte

**Solution : Mémoïser les valeurs et fonctions de contexte**

```javascript
//  CORRECT: Mémoïser la valeur du contexte et les fonctions
function CartProvider({ children }) {
  const [items, setItems] = useState([]);
  const [total, setTotal] = useState(0);
  
  // useCallback mémoïse les fonctions - elles ne changent que lorsque les dépendances changent
  const addItem = useCallback((item) => {
    setItems(prevItems => [...prevItems, item]);  // Utiliser la mise à jour de fonction pour éviter la dépendance
  }, []);  // Dépendances vides = la fonction ne change jamais
  
  const removeItem = useCallback((id) => {
    setItems(prevItems => prevItems.filter(item => item.id !== id));
  }, []);
  
  const updateQuantity = useCallback((id, quantity) => {
    setItems(prevItems => 
      prevItems.map(item => 
        item.id === id ? { ...item, quantity } : item
      )
    );
  }, []);
  
  // useMemo mémoïse l'objet de valeur de contexte
  const value = useMemo(() => ({
    items,
    total,
    addItem,
    removeItem,
    updateQuantity,
    itemCount: items.length  // Valeur calculée
  }), [items, total, addItem, removeItem, updateQuantity]);
  
  return (
    <CartContext.Provider value={value}>
      {children}
    </CartContext.Provider>
  );
}
```

**Ce que font useCallback et useMemo :**

* **useCallback(fn, deps)** retourne la même référence de fonction jusqu'à ce que les dépendances changent

* **useMemo(fn, deps)** retourne la même valeur jusqu'à ce que les dépendances changent

* **Pourquoi c'est important** : Les composants React ne se re-rendent que lorsque leurs props changent par référence

### Piège 4 : Prop drilling lorsque le contexte serait meilleur

**Le problème :**

```javascript
//   WRONG: Passer les données utilisateur à travers de nombreux composants qui ne les utilisent pas
function App() {
  const [user, setUser] = useState({ name: 'Alice', role: 'admin' });
  
  return (
    <div>
      <Header user={user} />  {/* Header n'utilise pas user, il le passe simplement */}
    </div>
  );
}

function Header({ user }) {
  return (
    <header>
      <Logo />
      <Navigation user={user} />  {/* Navigation n'utilise pas user non plus */}
    </header>
  );
}

function Navigation({ user }) {
  return (
    <nav>
      <MenuItem href="/">Home</MenuItem>
      <MenuItem href="/products">Products</MenuItem>
      <UserMenu user={user} />  {/* Enfin ! Quelqu'un qui utilise user */}
    </nav>
  );
}

function UserMenu({ user }) {
  return (
    <div className="user-menu">
      <span>Welcome, {user.name}!</span>  {/* C'est ici que user est réellement utilisé */}
      {user.role === 'admin' && <a href="/admin">Admin Panel</a>}
    </div>
  );
}
```

**Pourquoi c'est problématique :**

* Header et Navigation ne se soucient pas de user mais doivent le connaître

* Ajouter de nouvelles données utilisateur nécessite de mettre à jour plusieurs composants

* Les composants deviennent fortement couplés

* Les tests deviennent complexes car vous devez simuler des props que les composants n'utilisent pas

**Solution : Utiliser le contexte pour les données qui sautent les composants intermédiaires**

```javascript
//  MIEUX : Utiliser le contexte pour les données qui doivent sauter des niveaux
const UserContext = createContext();

function UserProvider({ children }) {
  const [user, setUser] = useState({ name: 'Alice', role: 'admin' });
  
  const value = useMemo(() => ({ user, setUser }), [user]);
  
  return (
    <UserContext.Provider value={value}>
      {children}
    </UserContext.Provider>
  );
}

function useUser() {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUser must be used within UserProvider');
  }
  return context;
}

function App() {
  return (
    <UserProvider>
      <div>
        <Header />  {/* Pas de props nécessaires ! */}
      </div>
    </UserProvider>
  );
}

function Header() {
  return (
    <header>
      <Logo />
      <Navigation />  {/* Pas de props nécessaires ! */}
    </header>
  );
}

function Navigation() {
  return (
    <nav>
      <MenuItem href="/">Home</MenuItem>
      <MenuItem href="/products">Products</MenuItem>
      <UserMenu />  {/* Pas de props nécessaires ! */}
    </nav>
  );
}

function UserMenu() {
  const { user } = useUser();  // Obtient les données utilisateur directement du contexte
  
  return (
    <div className="user-menu">
      <span>Welcome, {user.name}!</span>
      {user.role === 'admin' && <a href="/admin">Admin Panel</a>}
    </div>
  );
}
```

### Piège 5 : Utiliser l'état global pour tout

**Le problème :**

```javascript
//   WRONG: Mettre l'état local de l'UI dans le store global
const useAppStore = create((set) => ({
  // État global (bon)
  user: null,
  cart: { items: [], total: 0 },
  theme: 'light',
  
  // État local de l'UI (mauvais - devrait être local au composant)
  loginModalOpen: false,
  searchQuery: '',
  currentPage: 1,
  sortDirection: 'asc',
  selectedFilters: [],
  
  // Actions pour tout
  setLoginModalOpen: (open) => set({ loginModalOpen: open }),
  setSearchQuery: (query) => set({ searchQuery: query }),
  setCurrentPage: (page) => set({ currentPage: page }),
  // ... beaucoup plus d'actions
}));

function SearchBox() {
  const { searchQuery, setSearchQuery } = useAppStore();
  
  // Cela provoque le re-rendu de TOUS les composants utilisant le store à chaque frappe de l'utilisateur !
  return (
    <input 
      value={searchQuery} 
      onChange={(e) => setSearchQuery(e.target.value)} 
    />
  );
}
```

**Pourquoi c'est mauvais :**

* Chaque frappe de clavier provoque le re-rendu de tous les consommateurs du store

* Le store devient encombré d'état UI temporaire

* Difficile de réinitialiser l'état lorsque le composant est démonté

* Augmente le couplage entre les composants non liés

**Solution : Garder l'état local local, l'état global global**

```javascript
//  MIEUX : Séparer les préoccupations locales et globales
const useAppStore = create((set) => ({
  // Seulement l'état vraiment global
  user: null,
  cart: { items: [], total: 0 },
  theme: 'light',
  
  // Actions pour l'état global uniquement
  setUser: (user) => set({ user }),
  addToCart: (product) => set((state) => ({
    cart: {
      items: [...state.cart.items, product],
      total: state.cart.total + product.price
    }
  })),
  setTheme: (theme) => set({ theme })
}));

function SearchBox() {
  // État local pour les préoccupations locales
  const [searchQuery, setSearchQuery] = useState('');
  const [isSearching, setIsSearching] = useState(false);
  
  const handleSearch = async () => {
    setIsSearching(true);
    try {
      const results = await searchAPI(searchQuery);
      // Gérer les résultats...
    } catch (error) {
      // Gérer l'erreur...
    } finally {
      setIsSearching(false);
    }
  };
  
  return (
    <div>
      <input 
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}  // Pas de re-rendus globaux !
      />
      <button onClick={handleSearch} disabled={isSearching}>
        {isSearching ? 'Searching...' : 'Search'}
      </button>
    </div>
  );
}

function LoginModal() {
  // L'état d'ouverture/fermeture de la modale est local à ce composant
  const [isOpen, setIsOpen] = useState(false);
  
  return (
    <>
      <button onClick={() => setIsOpen(true)}>Login</button>
      {isOpen && (
        <Modal onClose={() => setIsOpen(false)}>
          <LoginForm />
        </Modal>
      )}
    </>
  );
}
```

**Lignes directrices pour ce qui appartient où :**

* **État local** : Entrées de formulaire, ouverture/fermeture de modale, états de chargement, état UI temporaire

* **État global** : Authentification de l'utilisateur, panier d'achat, thème, données partagées à travers les pages

### Piège 6 : Ne pas gérer les états de chargement et d'erreur dans l'état partagé

**Le problème :**

```javascript
//   WRONG: Ne pas gérer correctement les opérations asynchrones
const useUserStore = create((set) => ({
  user: null,
  
  // États de chargement et d'erreur manquants !
  login: async (email, password) => {
    const user = await authAPI.login(email, password);  // Que se passe-t-il si cela échoue ?
    set({ user });
  }
}));

function LoginForm() {
  const { login } = useUserStore();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    await login(email, password);  // Aucun moyen d'afficher le chargement ou de gérer les erreurs
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input value={email} onChange={(e) => setEmail(e.target.value)} />
      <input value={password} onChange={(e) => setPassword(e.target.value)} />
      <button type="submit">Login</button>  {/* Pas d'état de chargement */}
    </form>
  );
}
```

**Solution : Toujours inclure les états de chargement et d'erreur**

```javascript
//  MIEUX: Gérer correctement les opérations asynchrones
const useUserStore = create((set, get) => ({
  user: null,
  loading: false,
  error: null,
  
  login: async (email, password) => {
    set({ loading: true, error: null });  // Démarrer le chargement, effacer les erreurs précédentes
    
    try {
      const user = await authAPI.login(email, password);
      set({ user, loading: false, error: null });  // Succès
    } catch (error) {
      set({ 
        loading: false, 
        error: error.message || 'Login failed',  // Stocker le message d'erreur
        user: null 
      });
    }
  },
  
  logout: () => {
    set({ user: null, error: null });  // Effacer l'utilisateur et toute erreur
  },
  
  clearError: () => {
    set({ error: null });  // Permettre l'effacement manuel de l'erreur
  }
}));

function LoginForm() {
  const { login, loading, error, clearError } = useUserStore();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    clearError();  // Effacer toute erreur précédente
    await login(email, password);
  };
  
  return (
    <form onSubmit={handleSubmit}>
      {error && (
        <div className="error-message">
          {error}
          <button onClick={clearError}> d7</button>
        </div>
      )}
      
      <input 
        value={email} 
        onChange={(e) => setEmail(e.target.value)}
        disabled={loading}  // Désactiver pendant le chargement
      />
      
      <input 
        type="password"
        value={password} 
        onChange={(e) => setPassword(e.target.value)}
        disabled={loading}  // Désactiver pendant le chargement
      />
      
      <button type="submit" disabled={loading}>
        {loading ? 'Logging in...' : 'Login'}  {/* Afficher l'état de chargement */}
      </button>
    </form>
  );
}
```

## Meilleurs pratiques pour un état partagé maintenable

Suivre des modèles établis rend votre code plus facile à comprendre et à maintenir.

### 1. Utiliser des conventions de nommage cohérentes

Soyez descriptif et cohérent avec vos noms :

```javascript
//  BON : Noms clairs et descriptifs
const useCartStore = create((set) => ({
  // Les noms d'état sont clairs
  items: [],
  totalPrice: 0,
  itemCount: 0,
  isLoading: false,
  error: null,
  
  // Les noms d'action décrivent ce qu'ils font
  addItemToCart: (product) => set((state) => ({
    items: [...state.items, { ...product, quantity: 1 }],
    totalPrice: state.totalPrice + product.price,
    itemCount: state.itemCount + 1
  })),
  
  removeItemFromCart: (productId) => set((state) => {
    const itemToRemove = state.items.find(item => item.id === productId);
    if (!itemToRemove) return state;
    
    return {
      items: state.items.filter(item => item.id !== productId),
      totalPrice: state.totalPrice - (itemToRemove.price * itemToRemove.quantity),
      itemCount: state.itemCount - itemToRemove.quantity
    };
  }),
  
  clearCart: () => set({
    items: [],
    totalPrice: 0,
    itemCount: 0,
    error: null
  })
}));

//   MAUVAIS : Noms peu clairs et incohérents
const useStore = create((set) => ({
  // Peu clair ce que sont ces éléments
  data: [],
  num: 0,
  count: 0,
  loading: false,
  err: null,
  
  // Peu clair ce que font ces éléments
  add: (x) => set((s) => ({ data: [...s.data, x] })),
  remove: (id) => set((s) => ({ data: s.data.filter(i => i.id !== id) })),
  clear: () => set({ data: [], num: 0 })
}));
```

### 2. Regrouper l'état et les actions liés

Organisez votre état par fonctionnalité, pas par type :

```javascript
//  BON : Organisé par domaines de fonctionnalités
const useAppStore = create((set, get) => ({
  // État lié à l'utilisateur
  user: {
    profile: null,
    preferences: {},
    isAuthenticated: false,
    loading: false,
    error: null
  },
  
  // État lié au panier
  cart: {
    items: [],
    total: 0,
    discount: 0,
    loading: false,
    error: null
  },
  
  // État lié à l'UI
  ui: {
    theme: 'light',
    sidebarOpen: false,
    currentPage: 'home',
    notifications: []
  },
  
  // Actions de l'utilisateur
  userActions: {
    login: async (credentials) => {
      set((state) => ({
        user: { ...state.user, loading: true, error: null }
      }));
      
      try {
        const profile = await authAPI.login(credentials);
        set((state) => ({
          user: {
            ...state.user,
            profile,
            isAuthenticated: true,
            loading: false
          }
        }));
      } catch (error) {
        set((state) => ({
          user: {
            ...state.user,
            loading: false,
            error: error.message
          }
        }));
      }
    },
    
    logout: () => {
      set((state) => ({
        user: {
          profile: null,
          preferences: {},
          isAuthenticated: false,
          loading: false,
          error: null
        }
      }));
    }
  },
  
  // Actions du panier
  cartActions: {
    addItem: (product) => set((state) => ({
      cart: {
        ...state.cart,
        items: [...state.cart.items, { ...product, quantity: 1 }],
        total: state.cart.total + product.price
      }
    })),
    
    removeItem: (productId) => {
      const state = get();
      const item = state.cart.items.find(item => item.id === productId);
      
      if (item) {
        set((state) => ({
          cart: {
            ...state.cart,
            items: state.cart.items.filter(item => item.id !== productId),
            total: state.cart.total - (item.price * item.quantity)
          }
        }));
      }
    }
  },
  
  // Actions de l'UI
  uiActions: {
    setTheme: (theme) => set((state) => ({
      ui: { ...state.ui, theme }
    })),
    
    toggleSidebar: () => set((state) => ({
      ui: { ...state.ui, sidebarOpen: !state.ui.sidebarOpen }
    })),
    
    addNotification: (notification) => set((state) => ({
      ui: {
        ...state.ui,
        notifications: [...state.ui.notifications, {
          id: Date.now(),
          ...notification
        }]
      }
    }))
  }
}));

// Utilisation propre et organisée
function ProductCard({ product }) {
  const addItem = useAppStore(state => state.cartActions.addItem);
  
  return (
    <div className="product-card">
      <h3>{product.name}</h3>
      <button onClick={() => addItem(product)}>
        Add to Cart
      </button>
    </div>
  );
}
```

### 3. Créer des hooks de sélecteur pour un accès complexe aux données

Rendez l'accès aux données prévisible et réutilisable :

```javascript
//  BON : Hooks de sélecteur dédiés
function useCartSelectors() {
  const items = useCartStore(state => state.items);
  const totalPrice = useCartStore(state => state.totalPrice);
  const itemCount = useCartStore(state => state.itemCount);
  const isLoading = useCartStore(state => state.isLoading);
  const error = useCartStore(state => state.error);
  
  // Valeurs calculées
  const isEmpty = itemCount === 0;
  const hasDiscount = useCartStore(state => state.discount > 0);
  const finalTotal = totalPrice - useCartStore(state => state.discount);
  
  return {
    items,
    totalPrice,
    itemCount,
    isLoading,
    error,
    isEmpty,
    hasDiscount,
    finalTotal
  };
}

function useCartActions() {
  const addItem = useCartStore(state => state.addItemToCart);
  const removeItem = useCartStore(state => state.removeItemFromCart);
  const updateQuantity = useCartStore(state => state.updateItemQuantity);
  const clearCart = useCartStore(state => state.clearCart);
  const applyDiscount = useCartStore(state => state.applyDiscount);
  
  return {
    addItem,
    removeItem,
    updateQuantity,
    clearCart,
    applyDiscount
  };
}

// Utilisation propre dans les composants
function CartSummary() {
  const { items, finalTotal, isEmpty, isLoading } = useCartSelectors();
  const { removeItem, clearCart } = useCartActions();
  
  if (isLoading) return <div>Loading cart...</div>;
  if (isEmpty) return <div>Your cart is empty</div>;
  
  return (
    <div className="cart-summary">
      <h3>Cart Summary</h3>
      <p>Total: ${finalTotal.toFixed(2)}</p>
      
      {items.map(item => (
        <div key={item.id} className="cart-item">
          <span>{item.name} x {item.quantity}</span>
          <button onClick={() => removeItem(item.id)}>Remove</button>
        </div>
      ))}
      
      <button onClick={clearCart}>Clear Cart</button>
    </div>
  );
}
```

### 4. Gérer correctement les effets secondaires

Séparez les effets secondaires des mises à jour d'état :

```javascript
//  BON : Gestion correcte des effets secondaires
const useCartStore = create((set, get) => ({
  items: [],
  totalPrice: 0,
  
  addItem: (product) => {
    // Mettre à jour l'état
    set((state) => {
      const newItems = [...state.items, { ...product, quantity: 1 }];
      const newTotal = state.totalPrice + product.price;
      
      return {
        items: newItems,
        totalPrice: newTotal
      };
    });
    
    // Gérer les effets secondaires APRÈS la mise à jour de l'état
    const newState = get();
    
    // Suivi des analyses
    analytics.track('Item Added to Cart', {
      productId: product.id,
      productName: product.name,
      cartTotal: newState.totalPrice,
      itemCount: newState.items.length
    });
    
    // Sauvegarder dans localStorage
    localStorage.setItem('cart', JSON.stringify({
      items: newState.items,
      totalPrice: newState.totalPrice
    }));
    
    // Afficher une notification
    toast.success(`${product.name} added to cart!`);
    
    // Mettre à jour le titre de l'onglet du navigateur
    document.title = `Shopping (${newState.items.length}) - MyStore`;
  },
  
  removeItem: (productId) => {
    const currentState = get();
    const itemToRemove = currentState.items.find(item => item.id === productId);
    
    if (!itemToRemove) return;
    
    // Mettre à jour l'état
    set((state) => ({
      items: state.items.filter(item => item.id !== productId),
      totalPrice: state.totalPrice - (itemToRemove.price * itemToRemove.quantity)
    }));
    
    // Effets secondaires
    const newState = get();
    
    analytics.track('Item Removed from Cart', {
      productId: itemToRemove.id,
      productName: itemToRemove.name,
      cartTotal: newState.totalPrice
    });
    
    localStorage.setItem('cart', JSON.stringify({
      items: newState.items,
      totalPrice: newState.totalPrice
    }));
    
    toast.info(`${itemToRemove.name} removed from cart`);
    
    document.title = `Shopping (${newState.items.length}) - MyStore`;
  }
}));
```

### 5. Implémenter des limites d'erreur appropriées

Gérer les erreurs avec grâce au niveau de l'état :

```javascript
//  BON : Gestion complète des erreurs
const useApiStore = create((set, get) => ({
  data: null,
  loading: false,
  error: null,
  retryCount: 0,
  
  fetchData: async (url, options = {}) => {
    const { maxRetries = 3, retryDelay = 1000 } = options;
    
    set({ loading: true, error: null });
    
    const attemptFetch = async (attempt) => {
      try {
        const response = await fetch(url);
        
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        const data = await response.json();
        
        set({ 
          data, 
          loading: false, 
          error: null,
          retryCount: 0 
        });
        
      } catch (error) {
        console.error(`Fetch attempt ${attempt} failed:`, error);
        
        if (attempt < maxRetries) {
          // Réessayer avec un délai exponentiel
          const delay = retryDelay * Math.pow(2, attempt - 1);
          setTimeout(() => attemptFetch(attempt + 1), delay);
          
          set({ retryCount: attempt });
        } else {
          // Échec final
          set({ 
            loading: false, 
            error: {
              message: error.message,
              type: 'FETCH_ERROR',
              timestamp: new Date().toISOString(),
              url,
              attempts: attempt
            },
            retryCount: 0
          });
        }
      }
    };
    
    await attemptFetch(1);
  },
  
  retry: () => {
    const state = get();
    if (state.error && state.error.url) {
      state.fetchData(state.error.url);
    }
  },
  
  clearError: () => {
    set({ error: null });
  }
}));

// Composant de limite d'erreur
class ApiErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }
  
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }
  
  componentDidCatch(error, errorInfo) {
    console.error('API Error Boundary caught an error:', error, errorInfo);
    
    // Signaler au service de suivi des erreurs
    errorTracking.report(error, {
      componentStack: errorInfo.componentStack,
      context: 'ApiErrorBoundary'
    });
  }
  
  render() {
    if (this.state.hasError) {
      return (
        <div className="error-fallback">
          <h2>Something went wrong</h2>
          <p>We're sorry, but something unexpected happened.</p>
          <button onClick={() => this.setState({ hasError: false, error: null })}>
            Try Again
          </button>
        </div>
      );
    }
    
    return this.props.children;
  }
}

// Utilisation avec gestion des erreurs
function DataDisplay() {
  const { data, loading, error, retry } = useApiStore();
  
  useEffect(() => {
    useApiStore.getState().fetchData('/api/data');
  }, []);
  
  if (loading) return <div>Loading...</div>;
  
  if (error) {
    return (
      <div className="error-state">
        <h3>Failed to load data</h3>
        <p>{error.message}</p>
        <p>Attempted {error.attempts} times</p>
        <button onClick={retry}>Retry</button>
      </div>
    );
  }
  
  return (
    <div>
      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
    </div>
  );
}

function App() {
  return (
    <ApiErrorBoundary>
      <DataDisplay />
    </ApiErrorBoundary>
  );
}
```

## Conclusion : Construire des applications React maintenables

Gérer la complexité de l'état partagé est l'une des compétences les plus importantes à avoir pour construire des applications React évolutives. La clé est de choisir le bon outil pour chaque situation et de suivre des modèles établis.

### Résumé des approches

**Commencez simple et montez en puissance :**

1. **État local** pour les données spécifiques au composant

2. **Contexte** pour l'état partagé modéré qui ne change pas fréquemment

3. **Bibliothèques de gestion d'état** pour l'état global complexe et fréquemment changeant

4. **Hooks personnalisés** pour la logique avec état réutilisable

### Principes clés à retenir

**1. Principe de la moindre puissance** : Utilisez la solution la plus simple qui répond à vos besoins

* N'utilisez pas Redux pour un basculement de thème

* N'utilisez pas l'état local pour l'authentification des utilisateurs

* N'utilisez pas le contexte pour les données changeant rapidement

**2. Séparation des préoccupations** : Gardez l'état lié ensemble, l'état non lié séparé

* Regroupez l'état utilisateur séparément de l'état du panier

* Ne mélangez pas l'état UI temporaire avec les données persistantes

* Séparer les actions des sélecteurs

**3. La performance compte** : Optimisez pour votre cas d'utilisation spécifique

* Mémoïsez les valeurs de contexte pour éviter les re-rendus inutiles

* Utilisez des abonnements sélectifs dans les bibliothèques de gestion d'état

* Divisez les grands contextes en contextes plus petits et ciblés

**4. Maintenabilité d'abord** : Écrivez du code que les développeurs futurs (y compris vous-même) peuvent comprendre

* Utilisez des noms descriptifs pour l'état et les actions

* Gérez les états de chargement et d'erreur de manière cohérente

* Écrivez des tests complets pour votre logique d'état

### L'évolution d'une application typique

La plupart des applications React réussies suivent ce schéma :

**Phase 1 : État local simple**

```javascript
// Commencez ici pour les nouvelles fonctionnalités
function ContactForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  // Simple et focalisé
}
```

**Phase 2 : Contexte pour les données partagées**

```javascript
// Passez au contexte lorsque plusieurs composants ont besoin des mêmes données
const UserContext = createContext();
// Utilisé par les composants Header, Sidebar, UserProfile
```

**Phase 3 : Bibliothèque de gestion d'état pour les interactions complexes**

```javascript
// Passez à l'échelle avec Redux/Zustand lorsque l'état devient complexe
const useAppStore = create((set) => ({
  user: null,
  cart: { items: [], total: 0 },
  orders: [],
  // De nombreuses pièces d'état interconnectées
}));
```

**Phase 4 : Hooks personnalisés pour les modèles réutilisables**

```javascript
// Extrayez la logique réutilisable dans des hooks personnalisés
function useApi(url) {
  // Logique API réutilisable avec chargement, erreur et nouvelle tentative
}

function useLocalStorage(key, defaultValue) {
  // Synchronisation localStorage réutilisable
}
```

### Recommandations finales

**Pour les débutants** : Commencez avec l'état local et le contexte. Maîtrisez ceux-ci avant de passer aux bibliothèques de gestion d'état.

**Pour les développeurs intermédiaires** : Apprenez bien une bibliothèque de gestion d'état (Zustand ou Redux Toolkit). Concentrez-vous sur la gestion correcte des erreurs et l'optimisation des performances.

**Pour les développeurs avancés** : Expérimentez avec différents modèles et créez des abstractions réutilisables. Concentrez-vous sur la cohérence de l'équipe et les architectures maintenables.

**Pour les équipes** : Établissez des conventions tôt et documentez vos modèles de gestion d'état. Les revues de code doivent se concentrer sur le placement correct de l'état et les implications de performance.

L'objectif n'est pas d'éliminer toute complexité, mais de la gérer de manière à évoluer avec votre application et votre équipe. Chaque morceau d'état partagé doit avoir un propriétaire clair, des modèles de mise à jour prévisibles et une gestion correcte des erreurs.

N'oubliez pas : la meilleure solution de gestion d'état est souvent une combinaison d'approches. Une application React bien architecturée utilise l'état local pour les préoccupations locales, le contexte pour le partage modéré, les bibliothèques de gestion d'état pour l'état global complexe et les hooks personnalisés pour la logique réutilisable.

En suivant ces principes et modèles, vous construirez des applications React qui sont non seulement fonctionnelles mais aussi maintenables, performantes et agréables à travailler à mesure qu'elles deviennent plus complexes.