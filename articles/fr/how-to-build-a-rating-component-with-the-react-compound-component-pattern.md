---
title: Comment créer un composant de notation avec le motif des composants composés
  React
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2024-06-03T22:03:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-rating-component-with-the-react-compound-component-pattern
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Group-341.png
tags:
- name: components
  slug: components
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment créer un composant de notation avec le motif des composants composés
  React
seo_desc: "Have you ever watched a captivating movie or used a fantastic product and\
  \ wanted to share your experience? In today's world, feedback is critical, and ratings\
  \ are like currency. \nRating systems are everywhere, from the classic star ratings\
  \ on movie r..."
---

Avez-vous déjà regardé un film captivant ou utilisé un produit fantastique et voulu partager votre expérience ? Dans le monde d'aujourd'hui, les retours sont cruciaux, et les notations sont comme une monnaie d'échange. 

Les systèmes de notation sont partout, des classiques étoiles sur les sites de critique de films aux pouces levés/baissés omniprésents sur les plateformes de streaming. Ils guident nos choix, façonnent nos opinions et influencent finalement le succès des produits et services.

Dans cet article, nous allons créer un composant de notation sur le thème du cinéma en utilisant le motif des composants composés dans React. Je vais vous guider à travers la structuration du composant, la gestion de son état et la conception d'une interface utilisateur interactive qui capture l'essence de la notation.

## Prérequis

Bien que cet article soit conçu pour être aussi basique que possible, avoir une compréhension de base du motif des composants composés React est bénéfique. 

Si vous n'avez aucune expérience avec cela, ne vous inquiétez pas – je vous ai couvert ! Rendez-vous simplement sur [cet article sur les composants composés](https://www.freecodecamp.org/news/build-a-dynamic-dropdown-component/) où je le décompose plus en détail. D'autres prérequis incluent.

* Les bases de HTML, CSS et Tailwind CSS
* Les bases de JavaScript, React et React Hooks.

## **Ce que nous allons couvrir :**

1. [Comprendre les composants de notation](#heading-comprendre-les-composants-de-notation)  
– [Ce qui compose un composant de notation](#heading-ce-qui-compose-un-composant-de-notation)  
– [Avantages des composants de notation](#heading-avantages-des-composants-de-notation)
2. [Comment construire un composant de notation](#heading-construire-un-composant-de-notation)                                                                                
– [Méthode React régulière](#heading-methode-react-reguliere)  
 
– [Méthode des composants composés](#heading-methode-des-composants-composes)
3. [Comment améliorer le composant de notation](#heading-comment-ameliorer-le-composant-de-notation)
4. [Et juste pour le plaisir](#heading-et-juste-pour-le-plaisir)
5. [Conclusion](#heading-conclusion)

## Comprendre les composants de notation

Les composants de notation sont une partie essentielle des applications web modernes, en particulier dans les contextes où les retours des utilisateurs sont cruciaux. Ces composants fournissent une interface conviviale pour que les personnes expriment leurs opinions, souvent de manière quantifiable.

### Ce qui compose un composant de notation ?

Un composant de notation est un élément d'interface utilisateur qui permet aux utilisateurs de fournir une notation, généralement sur une échelle fixe. Voici les éléments typiques qui composent un composant de notation :

* **Icônes ou symboles** : Ce sont les représentations visuelles de l'échelle de notation. Les exemples courants incluent les étoiles, les cœurs, les pouces ou les valeurs numériques.
* **États interactifs** : Ces composants changent souvent d'apparence en fonction de l'interaction de l'utilisateur, comme le survol ou le clic.
* **Mécanisme de retour** : Certains composants de notation affichent un retour immédiat, comme la mise en surbrillance des icônes sélectionnées ou l'affichage de la valeur de la notation.
* **Fonctionnalités d'accessibilité** : Il est crucial de s'assurer que le composant est accessible à tous les utilisateurs, y compris la navigation au clavier et les lecteurs d'écran.
* **Retour personnalisé** : Certains composants de notation incluent une zone de texte permettant aux utilisateurs de commenter. Ce retour aide à clarifier les raisons derrière leurs notations et leur permet de signaler tout problème qu'ils rencontrent.

### Avantages des composants de notation

Les composants de notation offrent plusieurs avantages, tant pour les utilisateurs que pour les développeurs :

* **Engagement des utilisateurs** : Ils rendent facile et agréable pour les utilisateurs de fournir des retours, ce qui peut augmenter l'engagement.
* **Retour quantifiable** : Les notations fournissent des données claires et quantifiables qui peuvent être facilement analysées pour évaluer la satisfaction des utilisateurs.
* **Guider les décisions** : Pour les autres utilisateurs, les notations aident à prendre des décisions éclairées sur les films, les produits, les services et plus encore.
* **Améliorer les produits** : Pour les entreprises, les notations sont inestimables pour comprendre les préférences des utilisateurs et les domaines à améliorer.

## Comment construire un composant de notation

J'ai préparé un dépôt GitHub avec des fichiers de démarrage pour accélérer les choses. Clonez simplement [ce dépôt](https://github.com/Daiveedjay/Rating-Component) et installez les dépendances.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Let-s-get-this-party-started.gif)
_Commençons la fête_

Dans cette section, nous allons construire un seul composant de notation avec React régulier, puis le reconstruire avec le motif CC.

### Méthode React régulière

Vous vous demandez probablement pourquoi nous passons par la peine de construire d'abord le composant sans le motif des composants composés.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/woah-peter-griffin.gif)
_woah peter griffin_

Eh bien, en apprenant le motif des composants composés, j'ai eu du mal à comprendre pleinement la logique et j'ai fini avec quelques bugs qui auraient pu être évités avec une meilleure compréhension. 

Pour aider à cela, j'ai trouvé que construire une version plus petite de la fonctionnalité avant de mettre en œuvre complètement le CCP a finalement accéléré mon processus de développement.

Pour commencer, créez un `RatingComponent` et importez-le dans votre composant `App`.

```js
import RatingComponent from "./RatingComponent";
import { Toaster } from "react-hot-toast";

export default function App() {
  return (
    <main className=" bg-[#EAF2F8]  gap-4 min-h-[100dvh] flex justify-center items-center flex-col">
      <Toaster />
      <h1 className="text-3xl ">My Ratings Component</h1>
      <RatingComponent />
    </main>
  );
}
```

Ensuite, rendez-vous dans votre `RatingComponent` et ajoutez un peu de code standard pour créer une interface de notation standard.

```js
import { FiStar } from "react-icons/fi";
export default function RatingComponent() {
  return (
    <div className="flex bg-white items-center justify-between  border border-black rounded-md min-w-[600px]  p-2">
      <div className="p-2 text-base font-semibold">
        Intersteller <span className="text-gray-400 ">(2014)</span>
      </div>
      <div className="flex gap-4 p-2">
        {Array.from({ length: 5 }).map((_, index) => (
          <div key={index} className="flex justify-center">
            <FiStar
              size={25}
              strokeWidth={0}
              fill={"gold"}
              cursor="pointer"
              className="star"
            />
          </div>
        ))}
      </div>
    </div>
  );
}
```

Cela donne à votre interface utilisateur cet aspect :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/1-Ratings-UI-created.png)
_Interface utilisateur des notations créée_

Pour le moment, votre interface utilisateur est statique et n'a aucun moyen de changer les valeurs de notation. Pour ajouter de l'interactivité, créez un état qui contient la valeur initiale de la notation.

```js
const [stars, setStarts] = useState(0);
```

Ensuite, attachez le gestionnaire de paramétrage pour mettre à jour la valeur des étoiles lorsque vous cliquez sur une étoile.

```js
<FiStar
    size={25}
    strokeWidth={0}
    fill={"gold"}
    cursor="pointer"
    className="star"
    onClick={() => setStarts(index + 1)}
 />
```

**Note** : Nous ajoutons 1 à la valeur définie puisque les tableaux sont basés sur zéro.

Pour confirmer la valeur de l'étoile définie au clic, ajoutez une valeur de remplissage dynamique à chaque étoile.

```js
 <FiStar
   size={25}
   strokeWidth={0}
   fill={index + 1 <= stars ? "gold" : "#D6DBDF"}
   cursor="pointer"
   className="star"
   onClick={() => setStarts(index + 1)}
/>
```

Ce qui donne ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/testing-the-rating-component-1.gif)
_Test du composant de notation_

Pour améliorer davantage le retour utilisateur, nous pouvons convertir la signification de chaque étoile et l'afficher.

Commencez par créer un tableau d'étiquettes et de couleurs pour les étoiles.

```js
 const ratingData = [
    { label: "Poor", color: "#E74C3C" },
    { label: "Bad", color: "#E59866" },
    { label: "Okay", color: "#F7DC6F" },
    { label: "Good", color: "#76D7C4" },
    { label: "Great", color: "#229954" },
  ];
```

Ensuite, appliquez ces données pour refléter les notations actuelles.

```js
export default function RatingComponent() {
  const [stars, setStarts] = useState(0);

  const ratingData = [
    { label: "Poor", color: "#E74C3C" },
    { label: "Bad", color: "#E59866" },
    { label: "Okay", color: "#F7DC6F" },
    { label: "Good", color: "#76D7C4" },
    { label: "Great", color: "#229954" },
  ];
  return (
    <div className="flex bg-white items-center justify-between  border border-black rounded-md min-w-[600px]  p-2">
      <div className="p-2 text-base font-semibold">
        Intersteller <span className="text-gray-400 ">(2014)</span>
      </div>
      <div className="flex gap-4 p-2">
        {Array.from({ length: 5 }).map((_, index) => (
          <div key={index} className="flex justify-center">
            <FiStar
              size={25}
              strokeWidth={0}
              fill={index + 1 <= stars ? "gold" : "#D6DBDF"}
              cursor="pointer"
              className="star"
              onClick={() => setStarts(index + 1)}
            />
          </div>
        ))}
      </div>
      {stars > 0 ? (
        <div
          className="font-semibold min-w-[60px] p-2"
          style={{ color: ratingData[stars - 1]?.color }}>
          {ratingData[stars - 1]?.label}
        </div>
      ) : (
        <p className="font-semibold text-gray-400">No ratings yet...</p>
      )}
    </div>
  );
}
```

Ce qui donne ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/testing-the-rating-component-with-label-cues.gif)
_Test du composant de notation avec des indices d'étiquettes_

Et voilà ! Votre composant de notation est entièrement fonctionnel et chaque utilisateur peut l'utiliser efficacement pour laisser une critique précise.

### Méthode des composants composés

Pour cette méthode, nous allons aller plus loin et créer plusieurs composants de notation, car si nous ne faisons pas le maximum, que faisons-nous ? 😌

Commencez par créer le contexte pour le composant.

```js
const RatingContext = createContext();

const MultiRatingsComponent = ({
  children,
  ratingsData,

}) => {
  return (
    <RatingContext.Provider
      value={{
        ratingsData,
      }}>
      <div className="relative">{children}</div>
    </RatingContext.Provider>
  );
};
```

Puisque nous allons travailler avec plusieurs ensembles de données pour créer de nombreux composants de notation, la structure des données transmises serait différente.

```js
export default function App() {
  const multiRatings = [
    { name: "The Dark Knight", year: 2008, length: 5, rating: 0 },
    { name: "Knives Out", year: 2019, length: 5, rating: 0 },
    { name: "Serendipity", year: 2001, length: 5, rating: 0 },
    { name: "The Dressmaker", year: 2015, length: 5, rating: 0 },
    { name: "The Grand Budapest Hotel", year: 2015, length: 5, rating: 0 },
  ];
  const [ratings, setRatings] = useState(multiRatings);

  return (
    <main className="bg-[#EAF2F8] gap-4 min-h-[100vh] flex justify-center items-center flex-col">
      <Toaster />
      <h1 className="text-3xl">My Ratings Component</h1>
      <MultiRatingsComponent
        ratingsData={ratings}>
      </MultiRatingsComponent>
    </main>
  );
}
```

Ensuite, développez le reste du composant nécessaire pour que notre interface utilisateur ressemble au composant unique que nous avons créé précédemment.

```js
const MultiRatingsComponent = ({
  children,
  ratingsData,

}) => {
  const [userFeedback, setUserFeedback] = useState([]);
  return (
    <RatingContext.Provider
      value={{
        ratingsData,
      }}>
      <div className="relative ">{children}</div>
    </RatingContext.Provider>
  );
};

const Label = ({ name, year }) => {
  return (
    <div className="flex flex-col justify-center gap-1 text-base font-semibold min-w-[220px]">
      <h3>{name}</h3>
      <span className=" text-[12px]  text-[#AAB7B8]">{year}</span>
    </div>
  );
};

const RatingsContainer = () => {
  const { ratingsData, updateRating } = useContext(RatingContext);

  return (
    <div className="min-w-[600px] bg-white rounded-md flex flex-col">
      {ratingsData &&
        ratingsData.map((singleData, index) => (
          <div
            key={index}
            className="flex items-center px-4 py-6 border-[#f7f8f9] gap-[75px] border-[0.5px]">
            <Label name={singleData.name} year={singleData.year} />
            <div className="flex gap-4 ">
              {Array.from({ length: 5 }).map((_, starIndex) => (
                <RatingIcon
                  key={starIndex}
                  filled={starIndex < singleData.rating}
                />
              ))}
            </div>
          </div>
        ))}
    </div>
  );
};

const RatingIcon = ({ filled }) => {
  return (
    <FiStar
      size={25}
      strokeWidth={0}
      fill={filled ? "gold" : "#AAB7B8"}
      cursor="pointer"
      className="star"
    />
  );
};
```

Ensuite, attribuez chaque composant à son parent pour former le composant composé.

```js
MultiRatingsComponent.Label = Label;
MultiRatingsComponent.RatingsContainer = RatingsContainer;
MultiRatingsComponent.RatingIcon = RatingIcon;
```

Pour voir l'interface utilisateur de votre composant, imbriquez le `RatingsContainer` à l'intérieur de son parent (le composant `App`).

```js
export default function App() {
  const multiRatings = [
    { name: "The Dark Knight", year: 2008, length: 5, rating: 0 },
    { name: "Knives Out", year: 2019, length: 5, rating: 0 },
    { name: "Serendipity", year: 2001, length: 5, rating: 0 },
    { name: "The Dressmaker", year: 2015, length: 5, rating: 0 },
    { name: "The Grand Budapest Hotel", year: 2015, length: 5, rating: 0 },
  ];

  const [ratings, setRatings] = useState(multiRatings);

  return (
    <main className="bg-[#EAF2F8] gap-4 min-h-[100vh] flex justify-center items-center flex-col">
      <Toaster />
      <h1 className="text-3xl">My Ratings Component</h1>
      <MultiRatingsComponent
        ratingsData={ratings}>
        <MultiRatingsComponent.RatingsContainer />
      </MultiRatingsComponent>
    </main>
  );
}
```

Avec cela, votre interface utilisateur devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/2-Ratings-UI-with-CC-pattern.png)
_Interface utilisateur des notations avec le motif CC_

Pour ajouter notre fonctionnalité précédente où nous pouvions définir des notations, ainsi que montrer leur signification via des étiquettes, commencez par créer une fonction de mise à jour dans le composant `App`.

```js
  const updateRating = (index, newRating) => {
    setRatings((prevRatings) =>
      prevRatings.map((r, i) => (i === index ? { ...r, rating: newRating } : r))
    );
    console.log(ratings);
  };
```

Cette fonction utilise l'index du composant cliqué pour trouver les données particulières, puis modifie la propriété de notation en fonction de l'étoile sur laquelle vous cliquez.

Pour l'utiliser, passez-la dans le `MultiRatingsComponent` via les props, puis partagez-la avec tous ses enfants avec son contexte.

```js
const MultiRatingsComponent = ({
  children,
  ratingsData,
  updateRating,
}) => {
  const [userFeedback, setUserFeedback] = useState([]);
  return (
    <RatingContext.Provider
      value={{
        ratingsData,
        updateRating,
      }}>
      <div className="relative ">{children}</div>
    </RatingContext.Provider>
  );
};
```

Ensuite, consommez ce contexte dans `RatingsContainer`.

```js
const RatingsContainer = () => {
  const { ratingsData, updateRating } = useContext(RatingContext);

  return (
    <div className="min-w-[600px] bg-white rounded-md flex flex-col">
      {ratingsData &&
        ratingsData.map((singleData, index) => (
          <div
            key={index}
            className="flex items-center px-4 py-6 border-[#f7f8f9] gap-[75px] border-[0.5px]">
            <Label name={singleData.name} year={singleData.year} />
            <div className="flex gap-4 ">
              {Array.from({ length: 5 }).map((_, starIndex) => (
                <RatingIcon
                  key={starIndex}
                  filled={starIndex < singleData.rating}
                    onClick={() => updateRating(index, starIndex + 1)}
                />
              ))}
            </div>
          </div>
        ))}
    </div>
  );
};
```

Juste avant de vérifier l'interface utilisateur, créez un composant `RatingsLabel` pour montrer la signification de chaque étoile juste à côté de chaque étoile.

```js
const RatingLabel = ({ ratingValue }) => {
  const ratingLabel = [
    { label: "Poor", color: "#E74C3C" },
    { label: "Bad", color: "#E59866" },
    { label: "Okay", color: "#F7DC6F" },
    { label: "Good", color: "#76D7C4" },
    { label: "Great", color: "#229954" },
  ];
  return (
    <>
      {ratingValue > 0 ? (
        <div
          className="font-semibold min-w-[60px] p-2"
          style={{ color: ratingLabel[ratingValue - 1]?.color }}>
          {ratingLabel[ratingValue - 1]?.label}
        </div>
      ) : (
        <p className="font-semibold text-gray-400">No ratings yet...</p>
      )}
    </>
  );
};

MultiRatingsComponent.RatingLabel = RatingLabel;
```

Et imbriquez-le dans le `RatingsContainer`.

```js
const RatingsContainer = () => {
  const { ratingsData, updateRating } = useContext(RatingContext);

  return (
    <div className="min-w-[600px] bg-white rounded-md flex flex-col">
      {ratingsData &&
        ratingsData.map((singleData, index) => (
          <div
            key={index}
            className="flex items-center px-4 py-6 border-[#f7f8f9] gap-[75px] border-[0.5px]">
            <Label name={singleData.name} year={singleData.year} />
            <div className="flex gap-4 ">
              {Array.from({ length: 5 }).map((_, starIndex) => (
                <RatingIcon
                  key={starIndex}
                  filled={starIndex < singleData.rating}
                  onClick={() => updateRating(index, starIndex + 1)}
                />
              ))}
            </div>
            <RatingLabel ratingValue={singleData.rating} />
          </div>
        ))}
    </div>
  );
};
```

Roulement de tambour, s'il vous plaît...

![Image](https://www.freecodecamp.org/news/content/images/2024/06/testing-the-rating-component-with-CC-pattern-and-label-cues.gif)
_Test du composant de notation avec le motif CC et des indices d'étiquettes_

Avec cette implémentation, vous pouvez facilement avoir plusieurs barres de notation, et la gestion de chaque état serait un jeu d'enfant.

## Comment améliorer le composant de notation

Hélas, il y a une fonctionnalité que nous n'avons pas implémentée. Aucun grand composant de notation n'est complet sans un formulaire qui permet aux utilisateurs d'exprimer leurs opinions au-delà de quelques étoiles.

Pour créer un composant de commentaire, créez un formulaire et un état pour gérer ce formulaire.

```js
const Comment = () => {
  const [comment, setComment] = useState("");

  return (
    <div className="w-full mt-2 ">
      <label className="p-2 text-base font-semibold ">Comment</label>
      <form className="relative " onSubmit={(e)=> handleSubmit(e)}>
        <textarea
          name="comment"
          placeholder="Add a review"
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          className="w-full p-4 rounded-md resize-none min-h-20"></textarea>
        <button className="font-semibold absolute -bottom-1/2 right-0 border bg-[#5499C7] transition-all hover:bg-[#21618C] rounded-md py-2 px-4 text-white">
          Submit
        </button>
      </form>
    </div>
  );
};

MultiRatingsComponent.Comment = Comment;
```

Ensuite, créez une fonction de gestion pour ce formulaire.

```js
  const handleSubmit = (e) => {
    e.preventDefault();

    if (comment.length < 3) {
      toast.error("Please add more text");
      return;
    }

    // Clear the comment input
    setComment("");
  };
```

Pour voir les commentaires après qu'un utilisateur a soumis le formulaire, créez un état pour contenir ces commentaires dans le contexte parent.

```js
const MultiRatingsComponent = ({
  children,
  ratingsData,
  updateRating,

}) => {
  const [userFeedback, setUserFeedback] = useState([]);
  return (
    <RatingContext.Provider
      value={{
        ratingsData,
        updateRating,
        userFeedback,
        setUserFeedback,
        
      }}>
      <div className="relative ">{children}</div>
    </RatingContext.Provider>
  );
};
```

Ensuite, consommez ce contexte et stockez les données soumises dans le contexte parent.

```js
 const { userFeedback, setUserFeedback,} =
    useContext(RatingContext);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (comment.length < 3) {
      toast.error("Please add more text");
      return;
    }

    // Create a new feedback object
    const newFeedback = { comment };

    // Update the userFeedback state
    setUserFeedback([...userFeedback, newFeedback]);

    // Clear the comment input
    setComment("");
  };
```

Pour afficher tous les commentaires laissés par les utilisateurs, créez un composant `UserFeedback` comme suit :

```js
const UserFeedback = () => {
  const { userFeedback } = useContext(RatingContext);
  return (
    <div className="absolute top-0 px-8 py-2 translate-x-full bg-white rounded-md max-w-[300px] -right-5">
      {userFeedback.length > 0 ? (
        <>
          <h3 className="mb-2 text-xl font-semibold">
            Here are what user think
          </h3>
          <ul>
            {userFeedback.map((user, index) => (
              <li key={index} className="px-2 ">
                <h4>
                  {index + 1}.{" "}
                  <span className="font-semibold ">{user.name} </span> --{" "}
                  {user.text}
                </h4>
              </li>
            ))}
          </ul>
        </>
      ) : (
        <p className="font-semibold ext-xl">No user feedback yet...</p>
      )}
    </div>
  );
};
MultiRatingsComponent.UserFeedback = UserFeedback;
```

Ce composant consomme l'état contenant les commentaires des utilisateurs et les affiche à l'écran.

Juste avant de le tester, je voulais reproduire une particularité amusante que j'ai remarquée chez Google chaque fois que quelqu'un consulte vos documents. Ils attribuent un nom aléatoire à chaque utilisateur et nous ferons de même.

Rendez-vous dans votre composant `App` et créez ce tableau :

```js
 const randomNames = [
    "Anonymous Llama",
    "Mysterious Moose",
    "Stealthy Sloth",
    "Phantom Panda",
    "Incognito Iguana",
    "Unknown Unicorn",
    "Enigmatic Elephant",
    "Ghostly Giraffe",
    "Shadowy Shark",
    "Cryptic Cobra",
    "Silent Swan",
    "Nameless Narwhal",
    "Obscure Octopus",
    "Unseen Uakari",
    "Hidden Hedgehog",
    "Masked Macaw",
    "Veiled Vulture",
    "Concealed Chameleon",
    "Covert Cockatoo",
    "Invisible Impala",
  ];
```

Ensuite, passez-le dans votre `MultiRatingsComponent` via les props.

```js
const MultiRatingsComponent = ({
  children,
  ratingsData,
  updateRating,
  randomNames,
}) => {
  const [userFeedback, setUserFeedback] = useState([]);
  return (
    <RatingContext.Provider
      value={{
        ratingsData,
        updateRating,
        userFeedback,
        setUserFeedback,
        randomNames,
      }}>
      <div className="relative ">{children}</div>
    </RatingContext.Provider>
  );
};
```

Enfin, modifiez votre fonction de gestion de formulaire pour envoyer un nom aléatoire avec le commentaire.

```js
const Comment = () => {
  const [comment, setComment] = useState("");
  const { userFeedback, setUserFeedback, randomNames } =
    useContext(RatingContext);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (comment.length < 3) {
      toast.error("Please add more text");
      return;
    }

    // Generate a random name between 1 and the length of the array
    const randomName =
      randomNames[Math.floor(Math.random() * randomNames.length)];

    // Create a new feedback object
    const newFeedback = { name: randomName, comment };

    // Update the userFeedback state
    setUserFeedback([...userFeedback, newFeedback]);

    // Clear the comment input
    setComment("");
  };
```

Enfin, rendez les composants `Comment` et `UserFeedback` dans leur parent à l'intérieur du composant `App`.

```js
export default function App() {
  const multiRatings = [
    { name: "The Dark Knight", year: 2008, length: 5, rating: 0 },
    { name: "Knives Out", year: 2019, length: 5, rating: 0 },
    { name: "Serendipity", year: 2001, length: 5, rating: 0 },
    { name: "The Dressmaker", year: 2015, length: 5, rating: 0 },
    { name: "The Grand Budapest Hotel", year: 2015, length: 5, rating: 0 },
  ];

  const randomNames = [...];

  const [ratings, setRatings] = useState(multiRatings);

  const updateRating = (index, newRating) => {
    setRatings((prevRatings) =>
      prevRatings.map((r, i) => (i === index ? { ...r, rating: newRating } : r))
    );
  };
  return (
    <main className="bg-[#EAF2F8] gap-4 min-h-[100vh] flex justify-center items-center flex-col">
      <Toaster />
      <h1 className="text-3xl">My Ratings Component</h1>
      <MultiRatingsComponent
        ratingsData={ratings}
        updateRating={updateRating}
        randomNames={randomNames}>
        <MultiRatingsComponent.RatingsContainer />
        <MultiRatingsComponent.Comment />
        <MultiRatingsComponent.UserFeedback />
      </MultiRatingsComponent>
    </main>
  );
}
```

Et... Presto !

![Image](https://www.freecodecamp.org/news/content/images/2024/06/testing-the-rating-component-with-CC-pattern--label-cues-and-comments.gif)
_Test du composant de notation avec le motif CC, des indices d'étiquettes et des commentaires_

Votre composant de notation est terminé, avec la fonctionnalité ajoutée des commentaires.  2B50  
Comment noteriez-vous le parcours tout au long de cette construction ? 5 étoiles ? 😉

### Informations supplémentaires

Voici les liens vers toutes les ressources dont vous pourriez avoir besoin à partir de cet article.

* [Fichiers de démarrage](https://github.com/Daiveedjay/Rating-Component)
* [Motif React régulier](https://github.com/Daiveedjay/Rating-Component/tree/Single-Rating-Component)
* [Motif des composants composés](https://github.com/Daiveedjay/Rating-Component/tree/Compound-Component-Rating)

### Et juste pour le plaisir...

Puisque nous avons construit un composant de notation centré sur les films, voici 5 films que je considère dignes de 5 étoiles, dans le désordre.

* [The Grand Budapest Hotel](https://www.google.com/search?q=The+Grand+Budapest+Hotel&oq=The+Grand+Budapest+Hotel&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiPAjIHCAIQABiPAjIGCAMQRRhA0gEHMzUyajBqN6gCALACAA&sourceid=chrome&ie=UTF-8) (Comédie/Policier)
* [The Magnificent Seven](https://www.google.com/search?gs_ssp=eJzj4tVP1zc0TDLPNi5JKzE2YPSSKslIVchNTM_LTMtMTs0rUShOLUvNUzAyMDQDACXhDZw&q=the+magnificent+seven+2016&oq=the+magnifi&gs_lcrp=EgZjaHJvbWUqDAgCEC4YQxiABBiKBTIGCAAQRRg5MgoIARAuGNQCGIAEMgwIAhAuGEMYgAQYigUyBwgDEAAYgAQyBwgEEC4YgAQyCggFEC4Y1AIYgAQyCggGEC4Y1AIYgAQyBwgHEAAYgAQyBwgIEC4YgAQyBwgJEAAYjwLSAQg0NjQxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8) (Western/Action)
* [Django Unchained](https://www.google.com/search?q=django+unchained&sca_esv=616ade3b683ed7c0&sxsrf=ADLYWIK4xUiB8xs1iwXWvE9LfHZsNyCFsg%3A1717326804304&ei=1FNcZqaeEtqyhbIPzYCtwQU&gs_ssp=eJzj4tLP1TdIL88qN0g2YPQSSMlKzEvPVyjNS85IzMxLTQEAlJcKLw&oq=django&gs_lp=Egxnd3Mtd2l6LXNlcnAiBmRqYW5nbyoCCAAyDRAuGIAEGLEDGEMYigUyChAAGIAEGEMYigUyChAuGIAEGEMYigUyDRAAGIAEGLEDGEMYigUyChAAGIAEGEMYigUyChAuGIAEGEMYigUyChAAGIAEGEMYigUyChAAGIAEGBQYhwIyBRAAGIAEMgUQABiABDIoEC4YgAQYsQMYQxiKBRiXBRjcBBjeBBjgBBj0AxjxAxj1Axj2A9gBA0jCHlDHBFiUEXACeAGQAQCYAZgCoAH0C6oBAzItNrgBAcgBAPgBAZgCCKACtwyoAhHCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICDhAAGLADGOQCGNYE2AEBwgITEC4YgAQYsAMYQxjIAxiKBdgBAsICBxAjGCcY6gLCAhYQLhiABBhDGLQCGMgDGIoFGOoC2AECwgIKECMYgAQYJxiKBcICERAuGIAEGLEDGNEDGIMBGMcBwgIIEAAYgAQYsQPCAgQQABgDwgILEAAYgAQYsQMYgwHCAiUQLhiABBhDGIoFGJcFGNwEGN4EGOAEGPQDGPEDGPUDGPYD2AEDwgIFEC4YgATCAigQLhiABBixAxhDGIoFGJcFGNwEGN4EGOAEGPQDGPEDGPUDGPYD2AEDmAMJiAYBkAYTugYGCAEQARgJugYGCAIQARgIugYGCAMQARgUkgcFMi4wLjagB72FAQ&sclient=gws-wiz-serp) (Western/Action)
* [Ford vs Ferrari](https://www.google.com/search?q=ford+vs+ferrari&sca_esv=616ade3b683ed7c0&sxsrf=ADLYWIL6hL7o3cnMX0eikkhJDvlhvLACHg%3A1717327001772&ei=mVRcZpjqLr6whbIP-eS7kAw&gs_ssp=eJzj4tVP1zc0TDOrNC5IK6o0YPTiT8svSlEoK1ZISy0qSizKBACjAwqR&oq=ford+vs+fer&gs_lp=Egxnd3Mtd2l6LXNlcnAiC2ZvcmQgdnMgZmVyKgIIADINEC4YgAQYsQMYQxiKBTIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIoEC4YgAQYsQMYQxiKBRiXBRjcBBjeBBjgBBj0AxjxAxj1Axj2A9gBA0jnMFCGA1jZJHAEeAGQAQCYAY8CoAHRF6oBBjAuMi4xMbgBAcgBAPgBAZgCEqACuiSoAhLCAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICDhAAGLADGOQCGNYE2AEBwgITEC4YgAQYsAMYQxjIAxiKBdgBAsICBxAjGCcY6gLCAhYQLhiABBhDGLQCGMgDGIoFGOoC2AECwgIZEC4YgAQYQxjUAhi0AhjIAxiKBRjqAtgBAsICChAjGIAEGCcYigXCAgQQIxgnwgIKEC4YgAQYQxiKBcICERAuGIAEGLEDGNEDGIMBGMcBwgIIEAAYgAQYsQPCAgsQABiABBixAxiDAcICChAAGIAEGEMYigXCAhAQABiABBixAxhDGIMBGIoFwgIrEC4YgAQYsQMYQxiKBRiXBRjcBBjeBBjgBBj0AxjxAxj1Axj2Axj3A9gBA8ICDRAAGIAEGLEDGEMYigXCAhAQABiABBixAxhDGMkDGIoFwgILEAAYgAQYkgMYigXCAgoQABiABBgUGIcCmAMKiAYBkAYTugYGCAEQARgJugYGCAIQARgIugYGCAMQARgUkgcKNC4wLjEzLjctMaAH3qsB&sclient=gws-wiz-serp) (Sports/Action)
* [Inception](https://www.imdb.com/title/tt1375666/) (Action/Science-fiction)

## Conclusion

En conclusion, créer un composant de notation sur le thème du cinéma en utilisant le motif des composants composés dans React est un succès garanti pour vos projets. Cette approche vous permet de créer une base de code élégante, modulaire et maintenable. 

Maîtriser cette technique garantit que votre système de notation est à la fois fonctionnel et prêt pour l'avenir. Lumière, caméra, action – que votre parcours de codage brille avec des critiques cinq étoiles et des ovations debout !

### Aimez-vous mes articles ?

N'hésitez pas à [m'offrir un café ici](https://www.buymeacoffee.com/JajaDavid), pour garder mon cerveau en marche et fournir plus d'articles comme celui-ci.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/coffee-tom.gif)
_Café Tom_

### Informations de contact

Vous voulez vous connecter ou me contacter ? N'hésitez pas à me contacter sur les plateformes suivantes :

* Twitter / X : [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn : [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email : Jajadavidjid@gmail.com