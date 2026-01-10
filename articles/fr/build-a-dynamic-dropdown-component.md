---
title: Comment créer un composant Dropdown dynamique dans React – Explication du modèle
  de composant composé React
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2024-04-17T19:21:03.000Z'
originalURL: https://freecodecamp.org/news/build-a-dynamic-dropdown-component
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Article-Cover.png
tags:
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: Comment créer un composant Dropdown dynamique dans React – Explication
  du modèle de composant composé React
seo_desc: "Dropdowns have been an important part of websites and apps for a long time.\
  \ They're an unsung heros of user interactions, silently facilitating countless\
  \ actions and decisions with just a click or tap. \nYou probably encountered one\
  \ today, whether it ..."
---

Les dropdowns font partie intégrante des sites web et des applications depuis longtemps. Ils sont les héros méconnus des interactions utilisateur, facilitant silencieusement d'innombrables actions et décisions d'un simple clic ou tap.

Vous en avez probablement rencontré un aujourd'hui, que ce soit pour sélectionner une catégorie sur votre boutique en ligne préférée ou choisir votre date de naissance sur un formulaire d'inscription.

Mais que diriez-vous s'il existait un ingrédient secret capable d'élever vos dropdowns du mundane au magnifique ?

Rejoignez-moi pour disséquer les mystères du modèle de composant composé et exploiter ses capacités pour créer un composant dropdown dynamique.

## Prérequis

* Fondamentaux de HTML, CSS et Tailwind CSS
* Fondamentaux de React et des React Hooks.

## Ce que nous allons couvrir :

1. [Comprendre les composants Dropdown](#heading-comprendre-les-composants-dropdown)
2. [Comprendre les composants composés](#heading-comprendre-les-composants-composes)
3. [Comment créer le composant Dropdown](#heading-comment-creer-le-composant-dropdown)  
– [Méthode fonctionnelle React régulière](#heading-methode-fonctionnelle-react-reguliere)  
– [Méthode du modèle de composant composé](#heading-methode-du-modele-de-composant-compose)
4. [Comparaison entre la méthode régulière et la méthode du composant composé](#heading-comparaison-entre-la-methode-reguliere-et-la-methode-du-composant-compose)
5. [Conclusion](#heading-conclusion)

## Comprendre les composants Dropdown

Les composants dropdown jouent un rôle pivot dans la conception de l'interface utilisateur, fonctionnant comme des menus interactifs qui permettent aux utilisateurs de faire des sélections à partir d'une liste d'options. Typiquement, ils comprennent une zone cliquable qui, une fois activée, révèle une liste de choix pour que l'utilisateur puisse faire une sélection.

Le fonctionnement d'un composant dropdown est simple : lorsqu'un utilisateur interagit avec lui—souvent par un clic ou un tap—le dropdown s'étend, montrant les options disponibles.

Ensuite, l'utilisateur peut choisir l'une de ces options, qui est alors soit affichée dans le dropdown lui-même, soit utilisée pour mettre à jour un champ ou un élément lié dans l'interface.

Les composants dropdown offrent une méthode propre et efficace pour présenter une variété de choix aux utilisateurs, les rendant bien adaptés aux scénarios où plusieurs options doivent être accessibles tout en maintenant une interface soignée.

Les dropdowns servent également à des fins telles que :

* **Aide à la navigation** : Agissant comme des aides à la navigation, les dropdowns aident les utilisateurs à se déplacer sur les sites web en fournissant des menus pour sauter vers différentes sections ou pages.
* **Entrées de formulaire** : Simplifiant la saisie de données, les dropdowns présentent aux utilisateurs des options prédéfinies pour la sélection, comme le choix d'un pays, d'une date de naissance ou d'une langue préférée lors de l'inscription à un compte.
* **Filtres** : Sur les plateformes de commerce électronique, les dropdowns permettent aux acheteurs d'affiner leurs résultats de recherche en sélectionnant des options comme les catégories de produits, les fourchettes de prix ou les marques.
* **Sélecteurs de menu** : Communément utilisés sur les sites web de restaurants, les dropdowns affichent des menus ou permettent aux utilisateurs de choisir un type de cuisine, facilitant l'exploration et la sélection des options de restauration.
* **Présentation de données** : Les dropdowns peuvent organiser et présenter des données de manière efficace, permettant aux utilisateurs de filtrer les informations selon des critères tels que la plage de dates, la région géographique ou la catégorie de produit dans les tableaux de bord ou les outils d'analyse.

Un exemple de composants dropdown peut être vu ici :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/01-Showing-Dropdown-Demo.gif)
_Démonstration du Dropdown_

**Ou sur la page de [Semantic UI](https://semantic-ui.com/modules/dropdown.html).**

## Comprendre les composants composés

Le modèle de composant composé est comme construire avec des blocs LEGO : vous assemblez des pièces plus petites pour créer quelque chose de plus grand et plus complexe. Dans React, c'est une manière astucieuse de concevoir des composants à partir de plusieurs parties plus petites qui fonctionnent ensemble de manière transparente.

Imaginez que vous construisez un menu dropdown. Au lieu de créer un composant monolithique qui gère tout, vous le décomposez en parties plus petites et réutilisables. Vous pourriez avoir un composant pour le bouton du dropdown, un autre pour la liste des options, et un autre pour gérer la logique d'état et d'interaction.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/01-Compound-Component-Illustration.png)
_Illustration du composant composé_

Voici où cela devient intéressant : ces composants plus petits communiquent via un contexte partagé. Le contexte est comme un messager qui transporte des informations d'un composant à un autre sans avoir besoin de les passer à travers chaque niveau de l'arbre des composants. 

C'est un outil puissant qui simplifie le processus de partage de données entre les composants, surtout lorsqu'ils sont profondément imbriqués.

Maintenant, pourquoi ce modèle est-il si bénéfique ?

* Tout d'abord, il améliore la lisibilité. En décomposant un composant complexe en parties plus petites et plus ciblées, le code devient plus facile à comprendre et à maintenir. Chaque composant a une responsabilité claire, ce qui facilite le débogage et la mise à jour.
* Deuxièmement, les composants composés améliorent la maintenabilité. Puisque chaque partie du composant gère une tâche spécifique, apporter des modifications ou ajouter de nouvelles fonctionnalités devient beaucoup plus simple. Vous pouvez modifier une partie du composant sans affecter les autres, réduisant ainsi le risque d'introduire des bugs.
* Enfin, les composants composés offrent une grande flexibilité. Vous pouvez combiner différentes parties pour créer des versions spéciales du composant sans avoir à réécrire de code. Cela facilite l'ajustement du composant pour différents usages et exigences de conception.

Ainsi, bien que l'idée d'utiliser le contexte pour créer des composants d'interface utilisateur puisse sembler inhabituelle au premier abord, c'est une manière astucieuse de créer des composants dynamiques et réutilisables qui permettent aux développeurs de créer des expériences utilisateur exceptionnelles.

Dans la section suivante, nous approfondirons comment le contexte est utilisé pour donner vie aux composants composés.

## Comment créer le composant Dropdown

J'ai préparé un dépôt GitHub avec des fichiers de démarrage pour accélérer les choses. Clonez simplement [ce dépôt](https://github.com/Daiveedjay/React-Dropdown-Component/tree/Starter) et installez les dépendances.

Dans cette section, nous allons créer un composant dropdown en utilisant la méthode fonctionnelle React régulière, puis le comparer avec le modèle CC pour saisir pleinement la différence. PS : vous allez aimer le modèle de composant composé. 😁

![Image](https://www.freecodecamp.org/news/content/images/2024/04/02-Oh-fo-sho-meme.gif)
_Oh Fo sho Snoop Dogg gif_

### Méthode fonctionnelle React régulière

Nous allons commencer par créer la structure de base de notre composant dropdown. Cela impliquera la mise en place du conteneur principal du dropdown, du bouton pour déclencher le dropdown, et de la liste des options.

```jsx
const Dropdown = () => {
  return (
    <div>
      <label className="mt-4">Assign user(s) to as task:</label>

      <button className="  px-4 w-full py-2 flex items-center justify-between  rounded border border-[#828FA340] hover:border-primary cursor-pointer relative ">
        <span className="block">
          <FiChevronDown color="#635FC7" size={24} />
        </span>
      </button>
    </div>
  );
};
```

Ce qui donne :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/02-Dropdown-button-rendered.png)
_Bouton du Dropdown rendu_

Ensuite, passez le tableau des utilisateurs dans le dropdown pour créer une liste d'utilisateurs.

```jsx
const Dropdown = ({ usersArray }) => {
  return (
    <div>
      <label className="mt-4">Assign user(s) to as task:</label>

      <button className="  px-4 w-full py-2 flex items-center justify-between  rounded border border-[#828FA340] hover:border-primary cursor-pointer relative ">
        <span className="block">
          <FiChevronDown color="#635FC7" size={24} />
        </span>
        {
          <div className="absolute bottom-full translate-x-9  left-full translate-y-full rounded bg-[#20212c] w-max">
            <ul className="flex flex-col p-2">
              {usersArray.map((user) => (
                <li
                  key={user.id}
                  className={`flex items-center gap-2 p-4 hover:bg-[#2b2c37] rounded transition-all duration-200 `}>
                  <img
                    className="w-6 h-6 "
                    src={user.imgUrl}
                    alt={`${user.name} image`}
                  />
                  <span>{user.name}</span>
                </li>
              ))}
            </ul>
          </div>
        }
      </button>
    </div>
  );
};
```

Ce qui donne :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/03-Dropdown-list-rendered.png)
_Liste du Dropdown rendue_

Pour le moment, votre liste de dropdown est affichée par défaut. Pour ajouter le comportement de bascule, créez un état pour sa visibilité.

```jsx
 const [isDropdownOpen, setIsDropdownOpen] = useState(false);
```

Ensuite, passez les deux en tant que props au composant `Dropdown`.

```jsx
<Dropdown
 usersArray={usersArray}
 isDropdownOpen={isDropdownOpen}
 setIsDropdownOpen={setIsDropdownOpen}
 />
 ```

Avant de voir le résultat, attachez une fonction de bascule qui change l'état du dropdown à vrai au bouton du dropdown.

```jsx
const toggleDropdown = () => {
    setIsDropdownOpen(true);
};
```

Votre composant dropdown devrait maintenant ressembler à ceci :

```jsx
const Dropdown = ({ usersArray, setIsDropdownOpen, isDropdownOpen }) => {
  const toggleDropdown = () => {
    setIsDropdownOpen(true);
  };

  return (
    <div>
      <label className="mt-4">Assign user(s) to as task:</label>

      <button
        className="  px-4 w-full py-2 flex items-center justify-between  rounded border border-[#828FA340] hover:border-primary cursor-pointer relative "
        // Fonction pour afficher le dropdown au clic
        onClick={toggleDropdown}>
        <span className="block">
          <FiChevronDown color="#635FC7" size={24} />
        </span>
	  // Affichage conditionnel de votre liste de dropdown
        {isDropdownOpen && (
          <div className="absolute bottom-full translate-x-9  left-full translate-y-full rounded bg-[#20212c] w-max">
            <ul className="flex flex-col p-2">
              {usersArray.map((user) => (
                <li
                  key={user.id}
                  className={`flex items-center gap-2 p-4 hover:bg-[#2b2c37] rounded transition-all duration-200 `}>
                  <img
                    className="w-6 h-6 "
                    src={user.imgUrl}
                    alt={`${user.name} image`}
                  />
                  <span>{user.name}</span>
                </li>
              ))}
            </ul>
          </div>
        )}
      </button>
    </div>
  );
};
```

Votre dropdown se comporte maintenant comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/03-Dropdown-with-list-conditionally-rendering.gif)
_Dropdown avec liste rendue conditionnellement_

Je sais que vous avez remarqué que votre dropdown ne s'ouvre que mais ne se ferme pas. Ne vous inquiétez pas, nous réglerons cela plus tard de manière plus propre. 😉

![Image](https://www.freecodecamp.org/news/content/images/2024/04/04-Trust-the-process.gif)
_Faites confiance au processus_

Ensuite, créons un moyen d'assigner des utilisateurs à la tâche. Commencez par créer un état pour stocker les utilisateurs assignés dans le composant `App`.

```jsx
 const [assignedList, setAssignedList] = useState([]);
```

Ensuite, passez les valeurs en tant que props au composant `Dropdown`.

```jsx
<Dropdown
  usersArray={usersArray}
  isDropdownOpen={isDropdownOpen}
  setIsDropdownOpen={setIsDropdownOpen}
  assignedList={assignedList}
  setAssignedList={setAssignedList}
/>
```

Pour assigner des utilisateurs à la tâche, créez une fonction de gestion qui vérifie d'abord si l'utilisateur que vous essayez d'ajouter est déjà dans le tableau, les ajoute s'ils ne le sont pas, et les supprime s'ils le sont.

```jsx
  function handleAssign(user) {
    setAssignedList((prevList) => {
      // Vérifie si l'utilisateur existe déjà dans la liste
      if (prevList.includes(user)) {
        // Si l'utilisateur existe, le supprime de la liste
        const updatedList = prevList.filter((item) => item !== user);
        return updatedList;
      } else {
        // Si l'utilisateur n'existe pas, l'ajoute à la liste
        return [...prevList, user];
      }
    });
  }
```

Pour confirmer que cette fonction fonctionne, utilisez le tableau `assignedList` pour ajouter une icône de coche à chaque utilisateur assigné.

```jsx
<ul className="flex flex-col p-2">
  {usersArray.map((user) => (
    <li
      key={user.id}
      className={`flex items-center gap-2 p-4 hover:bg-[#2b2c37] rounded transition-all duration-200 `}
      onClick={() => handleAssign(user)}
    >
      {assignedList.includes(user) && <FiCheck />}

      <img
        className="w-6 h-6 "
        src={user.imgUrl}
        alt={`${user.name} image`}
      />
      <span>{user.name}</span>
    </li>
  ))}
</ul>
```

Avec cette modification, le dropdown devrait assigner et désassigner des utilisateurs au clic de chaque utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/05-Assigning-and-unassigning-users-to-the-task.gif)
_Assignation et désassignation des utilisateurs à la tâche_

Pour améliorer l'UI, créons un composant qui affiche tous les utilisateurs assignés.

Créez un composant `AssignedList` et passez ses états respectifs.

```jsx
 <AssignedList
   assignedList={assignedList}
   setAssignedList={setAssignedList}
  />
```

Ensuite, utilisez le tableau assigné pour créer du JSX.

```jsx
function AssignedList({ assignedList, setAssignedList }) {
  return (
    <div className="mt-4 p-2 shadow-sm bg-[#828fa318] rounded">
      <h2 className="px-2 my-3 font-bold">Assigned list:</h2>
      <div className="flex flex-wrap gap-4 ">
        {assignedList?.map((user, index) => (
          <div
            key={user.id}
            className="flex items-center gap-1 w-[47.5%] p-2 hover:bg-[#20212c] rounded transition-all duration-200">
            <span>{index + 1}.</span>
            <img
              className="w-6 h-6 "
              src={user.imgUrl}
              alt={`${user.name} image`}
            />

            <span>{user.name}</span>
            <span className="ml-auto cursor-pointer p-1 hover:bg-[#2b2c37] rounded-full">
              <FaXmark />
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
```

Tester votre composant maintenant donne :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/06-Displaying-assigned-users-using-the-AssignedList-component.gif)
_Affichage des utilisateurs assignés en utilisant le composant AssignedList_

L'une des dernières touches serait d'utiliser l'icône **x** pour supprimer un utilisateur de l'assignation.

Cela peut être fait en utilisant la fonction `setAssigned` pour filtrer l'utilisateur en fonction de son `id`.

```jsx
function handleRemove(id) {
    setAssignedList((assignedList) =>
      assignedList.filter((user) => user.id !== id)
    );
  }
```

Ensuite, passez l'id de l'utilisateur depuis la boucle.

```jsx
function AssignedList({ assignedList, setAssignedList }) {
  function handleRemove(id) {
    setAssignedList((assignedList) =>
      assignedList.filter((user) => user.id !== id)
    );
  }
  return (
    <div className="mt-4 p-2 shadow-sm bg-[#828fa318] rounded">
      <h2 className="px-2 my-3 font-bold">Assigned list:</h2>
      <div className="flex flex-wrap gap-4 ">
        {assignedList?.map((user, index) => (
          <div
            key={user.id}
            className="flex items-center gap-1 w-[47.5%] p-2 hover:bg-[#20212c] rounded transition-all duration-200"
            onClick={() => handleRemove(user.id)}>
            <span>{index + 1}.</span>
            <img
              className="w-6 h-6 "
              src={user.imgUrl}
              alt={`${user.name} image`}
            />

            <span>{user.name}</span>
            <span className="ml-auto cursor-pointer p-1 hover:bg-[#2b2c37] rounded-full">
              <FaXmark />
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
```

Cela donne :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/07-Removing-users-from-assignment-using-the-AssignedList-component-1.gif)
_Suppression des utilisateurs de l'assignation en utilisant le composant AssignedList_

Une autre touche finale serait de fermer la liste du dropdown à une certaine interaction de l'utilisateur.

Pour commencer, j'aime utiliser un hook réutilisable pour cela, qui prend un élément de référence et une fonction à déclencher lorsque n'importe quelle zone en dehors de mon élément cible est cliquée.

```jsx
import { useEffect } from "react";

const useClickOutside = (ref, handler) => {
  // console.log(handler, ref);
  useEffect(() => {
    const listener = (event) => {
      // Ne rien faire si on clique sur l'élément ref ou ses éléments descendants
      if (!ref.current || ref.current.contains(event.target)) {
        return;
      }

      handler(event);
    };

    document.addEventListener("mousedown", listener);
    document.addEventListener("touchstart", listener);

    return () => {
      document.removeEventListener("mousedown", listener);
      document.removeEventListener("touchstart", listener);
    };
  }, [ref, handler]);
};

export default useClickOutside;
```

Ensuite, dans notre composant `App`, créez une référence en utilisant le hook `useRef` pour sélectionner un élément.

```jsx
  const dropdownContainerRef = useRef(null);
```

Ensuite, attribuez-la à votre élément préféré.

```jsx
export default function App() {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const [assignedList, setAssignedList] = useState([]);

  const dropdownContainerRef = useRef(null);


  return (
    <div className="bg-[#2b2c37] h-[100dvh] text-white flex  p-20 gap-4 items-center flex-col">
      <div className=" w-[400px] " ref={dropdownContainerRef}>
        <h1 className="text-2xl ">Regular Functional React Pattern</h1>
        <Dropdown
          usersArray={usersArray}
          isDropdownOpen={isDropdownOpen}
          setIsDropdownOpen={setIsDropdownOpen}
          assignedList={assignedList}
          setAssignedList={setAssignedList}
        />
        <AssignedList
          assignedList={assignedList}
          setAssignedList={setAssignedList}
        />
      </div>
    </div>
  );
}
```

Enfin, importez votre hook et passez l'élément de référence et la fonction de gestion pour fermer le dropdown.

```jsx
 useClickOutside(dropdownContainerRef, () => {
    setIsDropdownOpen(false);
  });
```

Tester votre composant maintenant donne :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/08-Closing-the-dropdown-component-with-outside-clicks.gif)
_Fermeture du composant dropdown avec des clics à l'extérieur_

Ou en utilisant un bouton prédéterminé dans le dropdown.

```jsx
<button
  className="px-4 w-full py-2 flex items-center justify-between rounded border border-[#828FA340] hover:border-primary cursor-pointer relative"
  onClick={toggleDropdown}
>
  <span className="block">
    <FiChevronDown color="#635FC7" size={24} />
  </span>
  {isDropdownOpen && (
    <div className="absolute bottom-full translate-x-9 left-full translate-y-full rounded bg-[#20212c] w-max">
      {/* Bouton de fermeture */}
      <div
        className="absolute top-0 right-0 flex items-center justify-center -translate-y-full gap-2 bg-[#C0392B] px-2 py-1 rounded-t"
        onClick={(e) => {
          e.stopPropagation();
          setIsDropdownOpen(false);
          console.log(isDropdownOpen);
        }}
      >
        <span>Fermer</span>
        <span>
          <FaXmark size={20} />
        </span>
      </div>
      <ul className="flex flex-col p-2">
        {usersArray.map((user) => (
          <li
            key={user.id}
            className={`flex items-center gap-2 p-4 hover:bg-[#2b2c37] rounded transition-all duration-200`}
            onClick={() => handleAssign(user)}
          >
            {assignedList.includes(user) && <FiCheck />}
            <img
              className="w-6 h-6"
              src={user.imgUrl}
              alt={`${user.name} image`}
            />
            <span>{user.name}</span>
          </li>
        ))}
      </ul>
    </div>
  )}
</button>
```

![Image](https://www.freecodecamp.org/news/content/images/2024/04/09-Closing-the-dropdown-with-the-designated-button.gif)
_Fermeture du dropdown avec le bouton désigné_

Le dernier changement est une question d'opinion car je préférerais afficher autre chose s'il n'y a pas d'utilisateurs actuellement assignés à la tâche.

```jsx
{assignedList.length === 0 ? (
  <p className="mt-4 p-2 shadow-sm bg-[#828fa318] rounded">
    Aucun utilisateur assigné à la tâche pour le moment.
  </p>
) : (
  <AssignedList
    assignedList={assignedList}
    setAssignedList={setAssignedList}
  />
)}
```

Cela amène l'UI à :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/10-Showing-a-default-text-when-no-users-are-assigned.gif)
_Affichage d'un texte par défaut lorsqu'aucun utilisateur n'est assigné_

### Méthode du modèle de composant composé

Maintenant, pour l'événement principal. Commencez par créer un contexte qui enveloppe l'ensemble du composant.

```jsx
const UserAssignContext = createContext();
```

Ensuite, nous rassemblons toutes les données et fonctions nécessaires que notre dropdown et ses composants vont utiliser. Cela inclut des éléments comme la liste des utilisateurs assignés, une fonction pour mettre à jour cette liste, et si le dropdown est actuellement ouvert ou non.

Après quoi, vous fournissez ces valeurs à tous ses composants enfants.

```jsx
const UserAssignDropdown = ({
  children,
  assignedList,
  setAssignedList,
  users,
}) => {
  const UserAssignDropdownRef = useRef(null);
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  return (
    <UserAssignContext.Provider
      value={{
        assignedList,
        users,
        UserAssignDropdownRef,
        isDropdownOpen,
        setIsDropdownOpen,
        setAssignedList,
      }}>
      <div ref={UserAssignDropdownRef}>{children}</div>
    </UserAssignContext.Provider>
  );
};
```

Avec notre contexte configuré, il est temps de créer les composants individuels qui composeront notre dropdown. Chaque composant interagira avec le contexte pour accéder et manipuler les données et fonctions nécessaires.

Commencez par copier chaque style des composants que nous venons de créer.

#### Le composant Header

Ce composant reste le même.

```jsx
const Header = () => {
  return <label className="mt-4 mb-2 text-sm">Assign task to:</label>;
};
```

#### Le composant Close

Ce composant obtient la fonction pour basculer le dropdown depuis le contexte.

```jsx
const Close = () => {
  const { setIsDropdownOpen } = useContext(UserAssignContext);
  return (
    <div
      className="absolute top-0 right-0 flex items-center justify-center -translate-y-full gap-2 bg-[#C0392B] px-2 py-1 rounded-t"
      onClick={(e) => {
        e.stopPropagation();
        setIsDropdownOpen(false);
      }}>
      <span>Fermer</span>
      <span>
        <FaXmark size={20} />
      </span>
    </div>
  );
};
```

#### Le composant Assigned List

Ce composant affiche la liste des utilisateurs assignés, ainsi que la suppression des utilisateurs de la liste.

```jsx
const AssignedList = () => {
  const { assignedList, setAssignedList } = useContext(UserAssignContext);

  function handleRemove(id) {
    setAssignedList((assignedList) =>
      assignedList.filter((user) => user.id !== id)
    );
  }

  if (assignedList.length === 0)
    return (
      <p className="mt-4 p-2 shadow-sm bg-[#828fa318] rounded">
        Aucun utilisateur assigné à la tâche pour le moment.
      </p>
    );

  return (
    <div className="mt-4 p-2 shadow-sm bg-[#828fa318] rounded">
      <h2 className="px-2 my-3 font-bold">Assigned list:</h2>
      <div className="flex flex-wrap gap-4 ">
        {assignedList?.map((user, index) => (
          <div
            key={user.id}
            className="flex items-center gap-1 w-[47.5%] p-2 hover:bg-[#20212c] rounded transition-all duration-200"
            onClick={() => handleRemove(user.id)}>
            <span>{index + 1}.</span>
            <img
              className="w-6 h-6 "
              src={user.imgUrl}
              alt={`${user.name} image`}
            />

            <span>{user.name}</span>
            <span className="ml-auto cursor-pointer p-1 hover:bg-[#2b2c37] rounded-full">
              <FaXmark />
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
```

#### Le composant Item

Ce composant représente chaque utilisateur et la fonctionnalité d'ajout et de suppression des utilisateurs de la liste assignée.

```jsx
const Item = ({ user }) => {
  const { assignedList, setAssignedList } = useContext(UserAssignContext);

  function handleAssign(user) {
    setAssignedList((prevList) => {
      // Vérifie si l'utilisateur existe déjà dans la liste
      if (prevList.includes(user)) {
        // Si l'utilisateur existe, le supprime de la liste
        const updatedList = prevList.filter((item) => item !== user);
        return updatedList;
      } else {
        // Si l'utilisateur n'existe pas, l'ajoute à la liste
        return [...prevList, user];
      }
    });
  }

  return (
    <li
      key={user.id}
      className={`flex items-center gap-2 p-4 hover:bg-[#2b2c37] rounded transition-all duration-200 `}
      onClick={() => handleAssign(user)}>
      {assignedList.includes(user) && <FiCheck />}

      <img className="w-6 h-6 " src={user.imgUrl} alt={`${user.name} image`} />
      <span>{user.name}</span>
    </li>
  );
};
```

#### Le composant Button

Ce composant contrôle l'affichage du composant `List` (dropdown flottant).

```jsx
const Button = () => {
  const { setIsDropdownOpen } = useContext(UserAssignContext);
  return (
    <button
      className="  px-4 py-2 flex items-center justify-between w-full rounded border border-[#828FA340] hover:border-primary cursor-pointer relative "
      onClick={() => setIsDropdownOpen(true)}>
      <span className="block">
        <FiChevronDown color="#635FC7" size={24} />
      </span>

      <UserAssignDropdown.List />
    </button>
  );
};
```

Pour combiner ce composant en un seul composant composé (composant composé), vous attribuez chaque composant au parent, comme suit ;

```jsx
UserAssignDropdown.List = ListContainer;
UserAssignDropdown.Item = Item;
UserAssignDropdown.Header = Header;
UserAssignDropdown.Button = Button;
UserAssignDropdown.AssignedList = AssignedList;
UserAssignDropdown.Close = Close;
```

Ensuite, importez votre composant composé dans votre composant `App` en tant que composant wrapper et passez les états appropriés.

```jsx
export default function App() {
  const [assignedList, setAssignedList] = useState([]);

  return (
    <div className="bg-[#2b2c37] h-[100dvh] text-white flex  p-20 gap-4 items-center flex-col">
      <div className=" w-[400px] ">
        <h1 className="text-2xl ">Compound Component Pattern</h1>
        <UserAssignDropdown
          assignedList={assignedList}
          setAssignedList={setAssignedList}
          users={usersArray}></UserAssignDropdown>
      </div>
    </div>
  );
}
```

Ensuite, dans le wrapper, rendez les enfants appropriés.

```jsx
export default function App() {
  const [assignedList, setAssignedList] = useState([]);

  return (
    <div className="bg-[#2b2c37] h-[100dvh] text-white flex  p-20 gap-4 items-center flex-col">
      <div className=" w-[400px] ">
        <h1 className="text-2xl ">Compound Component Pattern</h1>
        <UserAssignDropdown
          assignedList={assignedList}
          setAssignedList={setAssignedList}
          users={usersArray}>
          <UserAssignDropdown.Header />
          <UserAssignDropdown.Button />
          <UserAssignDropdown.AssignedList />
        </UserAssignDropdown>
      </div>
    </div>
  );
}
```

Enfin, utilisez le hook personnalisé que nous avons créé précédemment pour fermer le dropdown lorsque vous cliquez à l'extérieur du composant.

```jsx
const UserAssignContext = createContext();
const UserAssignDropdown = ({
  children,
  assignedList,
  setAssignedList,
  users,
}) => {
  const UserAssignDropdownRef = useRef(null);
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  useClickOutside(UserAssignDropdownRef, () => {
    setIsDropdownOpen(false);
  });

  return (
    <UserAssignContext.Provider
      value={{
        assignedList,
        users,
        UserAssignDropdownRef,
        isDropdownOpen,
        setIsDropdownOpen,
        setAssignedList,
      }}>
      <div ref={UserAssignDropdownRef}>{children}</div>
    </UserAssignContext.Provider>
  );
};
```

Et avec cela, votre composant fonctionne de la même manière !

![Image](https://www.freecodecamp.org/news/content/images/2024/04/11-replicating-the-same-funtionality-with-the-compound-component-pattern.gif)
_Réplication de la même fonctionnalité avec le modèle de composant composé_

Mais pourquoi s'arrêter là ?

Avec ce modèle, changer l'apparence du composant est aussi simple que de changer l'ordre dans lequel vous les rendez dans leur parent. Par exemple, si vous voulez le bouton en premier, vous changez simplement l'ordre dans le wrapper parent.

```jsx
<UserAssignDropdown
  assignedList={assignedList}
  setAssignedList={setAssignedList}
  users={usersArray}
>
  <UserAssignDropdown.Button />
  <UserAssignDropdown.Header />
  <UserAssignDropdown.AssignedList />
</UserAssignDropdown>

```

Et l'UI répond en conséquence.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/04-order-of-rendering-in-compound-component-changed.png)
_Ordre de rendu dans le composant composé changé_

Ce composant est également suffisamment flexible pour changer la disposition des éléments via des props.

Simplement en passant des props de style via un parent :

```jsx
<UserAssignDropdown
  assignedList={assignedList}
  setAssignedList={setAssignedList}
  users={usersArray}
>
  <UserAssignDropdown.Header />
  <UserAssignDropdown.Button
    listStyles={"!-left-5 !-translate-x-full bg-[#605e80] text-white border"}
  />
  <UserAssignDropdown.AssignedList />
</UserAssignDropdown>
```

Et en recevant ces props dans l'enfant :

```jsx
const Button = ({ listStyles }) => {
  const { setIsDropdownOpen, UserAssignDropdownRef } =
    useContext(UserAssignContext);
  return (
    <button
      className="  px-4 py-2 flex items-center justify-between w-full rounded border border-[#828FA340] hover:border-primary cursor-pointer relative "
      ref={UserAssignDropdownRef}
      onClick={() => setIsDropdownOpen(true)}>
      <span className="block">
        <FiChevronDown color="#635FC7" size={24} />
      </span>
      <UserAssignDropdown.List listStyles={listStyles} />
    </button>
  );
};

const ListContainer = ({ listStyles }) => {
  const { users, isDropdownOpen } = useContext(UserAssignContext);

  return (
    isDropdownOpen && (
      <ul
        className={`absolute bottom-full translate-x-9  left-full translate-y-full rounded bg-[#20212c] w-max ${listStyles}`}>
        <UserAssignDropdown.Close />
        <div className="flex flex-col p-2">
          {users?.map((user, index) => (
            <UserAssignDropdown.Item key={index} user={user} />
          ))}
        </div>
      </ul>
    )
  );
};
```

Vous pouvez facilement changer l'apparence du composant.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/12-Using-props-to-customize-the-compound-component.gif)
_Utilisation de props pour personnaliser le composant composé_

## Comparaison entre la méthode régulière et la méthode du composant composé

D'accord, faisons un pas en arrière et comparons les deux approches que nous venons d'explorer.

### Simplicité et Organisation

* **Méthode régulière** : Imaginez cela comme cuisiner un gâteau dans un grand bol. Avec la méthode régulière, nous pouvons créer un seul composant responsable de tout dans le dropdown – le bouton, la liste et tous les ingrédients. C'est comme avoir une grande carte de recette avec toutes les étapes mélangées. Cela fait le travail, mais cela peut être un peu désordonné et difficile à suivre, surtout lorsque vous essayez d'ajuster une seule partie de la recette.
* **Méthode du composant composé** : Imaginez maintenant que nous avons différents bols pour chaque ingrédient, un séparé pour la farine, un autre pour le sucre, et ainsi de suite. C'est le modèle de composant composé. Chaque partie du dropdown a son propre espace pour briller. C'est comme organiser votre cuisine – tout a sa place. Cela rend les choses plus faciles à comprendre et à modifier. Besoin de changer la farine ? Vous savez exactement où regarder.

### Flexibilité et Personnalisation

* **Méthode régulière** : Avec notre approche à un seul bol, apporter des modifications à des parties spécifiques du dropdown peut être un peu comme essayer de remplacer des ingrédients dans ce grand mélange de gâteau. Bien sûr, vous pouvez le faire, mais ce n'est pas toujours facile. Vous voulez une saveur de gâteau différente ? Vous devrez peut-être fouiller dans tout le bol pour trouver où l'ajouter.
* **Méthode du composant composé** : Avec le modèle de composant composé, c'est comme avoir des conteneurs séparés pour chaque saveur. Besoin d'ajouter des pépites de chocolat ? Il suffit de prendre le conteneur de chocolat et de saupoudrer. Chaque composant a son travail, ce qui simplifie la personnalisation. Vous voulez changer la couleur du bouton ? Pas de problème, c'est juste là dans son conteneur.

### Réutilisation et Maintenance

* **Méthode régulière** : Lorsque votre recette est toute mélangée dans un seul bol, il peut être difficile de réutiliser des parties pour un autre plat. De plus, à mesure que votre cuisine devient plus occupée, il est facile pour les choses de devenir désordonnées et difficiles à suivre. Vous pourriez vous retrouver à réécrire la recette chaque fois que vous voulez faire quelque chose de nouveau.
* **Méthode du composant composé** : Avec le modèle de composant composé, c'est comme avoir un ensemble d'outils réutilisables dans votre cuisine. Besoin de faire un type de gâteau différent ? Il suffit de prendre les outils dont vous avez besoin et de commencer à cuisiner. Chaque composant est comme un gadget spécialisé – facile à réutiliser et à maintenir. Et lorsque votre cuisine est organisée, c'est un jeu d'enfant de préparer quelque chose de nouveau.

### Informations supplémentaires

Voici les liens vers toutes les ressources dont vous pourriez avoir besoin à partir de cet article.

* [Fichiers de démarrage](https://github.com/Daiveedjay/React-Dropdown-Component/tree/Starter)
* [Modèle de fonction régulière](https://github.com/Daiveedjay/React-Dropdown-Component/tree/Regular-react-pattern)
* [Modèle de composant composé](https://github.com/Daiveedjay/React-Dropdown-Component/tree/Compound-component-pattern)

## Conclusion

En fin de compte, les deux méthodes ont leur place dans la cuisine – euh, je veux dire, dans votre code. La méthode régulière est comme votre vieux bol de mélange fiable – fiable et familier, mais peut-être pas le plus efficace pour chaque recette. 

Le modèle de composant composé est comme une cuisine bien organisée, avec tout à sa place et prêt à l'emploi. Cela peut prendre un peu plus de configuration, mais cela peut rendre votre vie beaucoup plus facile à long terme. Donc, selon ce que vous cuisinez, choisissez la méthode qui convient à votre goût – et bon codage ! 🍰🎨  


### Informations de contact

Vous voulez me contacter ? N'hésitez pas à me contacter sur les plateformes suivantes :

* Twitter / X : [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn : [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email : Jajadavidjid@gmail.com