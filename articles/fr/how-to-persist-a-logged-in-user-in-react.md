---
title: Comment maintenir un utilisateur connecté dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-15T21:39:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-persist-a-logged-in-user-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Slice-3-1-.png
tags:
- name: keep a user signed in
  slug: keep-a-user-signed-in
- name: localstorage
  slug: localstorage
- name: login forms
  slug: login-forms
- name: React
  slug: react
seo_title: Comment maintenir un utilisateur connecté dans React
seo_desc: 'By Adebola Adeniran

  If you run a quick Google search for persisting a logged-in user in React (or keeping
  a user logged in in React), you don''t get a lot of straightforward results. There
  aren''t really any easy to follow examples on how to achieve th...'
---

Par Adebola Adeniran

Si vous effectuez une recherche rapide sur Google pour maintenir un utilisateur connecté dans React (ou garder un utilisateur connecté dans React), vous n'obtenez pas beaucoup de résultats simples. Il n'y a pas vraiment d'exemples faciles à suivre sur la façon d'y parvenir. J'ai donc décidé d'écrire ce guide simple.

Vous avez peut-être fait une recherche sur ce sujet et vu le mot **localStorage** mentionné. Oui, nous allons utiliser **localStorage**, mais je vais vous montrer exactement comment cela se fait.

## Quelques notes sur localStorage.

1. **localStorage** est la base de données du navigateur. Les données sont stockées dans votre navigateur dans la mémoire de votre ordinateur.
2. **localStorage** est spécifique à une origine. En d'autres termes, le localStorage d'un site web ne peut pas être accessible par un autre.

## Installation initiale

Commençons. J'ai déployé un simple serveur express sur Heroku pour tester cette application.

1. Créez une nouvelle application React et allez dans le composant **`<App />`**.
2. Installez axios en utilisant `npm install axios` et importez-le dans **`<App />`**
3. Ensuite, créez un simple formulaire de connexion qui accepte un nom d'utilisateur et un mot de passe.

```
import React, { useState } from "react";
import axios from "axios";

const App = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [user, setUser] = useState()

  const handleSubmit = async e => {
    
  };

// si un utilisateur est présent, affichez le message ci-dessous
  if (user) {
    return <div>{user.name} est connecté</div>;
  }

  // si aucun utilisateur n'est présent, affichez le formulaire de connexion
  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="username">Nom d'utilisateur : </label>
      <input
        type="text"
        value={username}
        placeholder="entrez un nom d'utilisateur"
        onChange={({ target }) => setUsername(target.value)}
      />
      <div>
        <label htmlFor="password">Mot de passe : </label>
        <input
          type="password"
          value={password}
          placeholder="entrez un mot de passe"
          onChange={({ target }) => setPassword(target.value)}
        />
      </div>
      <button type="submit">Connexion</button>
    </form>
  );
};

export default App;

```

Comme vous pouvez le voir, nous avons défini une fonction asynchrone **handleSubmit** pour traiter la demande de connexion. Nous avons également défini une conditionnelle qui affiche un message **user.name est connecté** si nous avons un utilisateur, et le formulaire de connexion si nous n'avons pas d'utilisateur.

Ensuite, complétons la fonction. Cette fonction fonctionnera selon les étapes suivantes :

1. Envoyer les détails de connexion au serveur.
2. Si la demande est réussie (async-await), stocker les informations de l'utilisateur dans localStorage et définir l'état de l'utilisateur.

## Gérer l'événement de connexion

Définissons le gestionnaire d'événements **handleSubmit**.

  ```
  const handleSubmit = async e => {
    e.preventDefault();
    const user = { username, password };
    // envoyer le nom d'utilisateur et le mot de passe au serveur
    const response = await axios.post(
      "http://blogservice.herokuapp.com/api/login",
      user
    );
    // définir l'état de l'utilisateur
    setUser(response.data)
    // stocker l'utilisateur dans localStorage
    localStorage.setItem('user', response.data)
    console.log(response.data)
  };
  ```

Note : Utilisez un bloc **tryCatch** pour gérer les erreurs dans les fonctions asynchrones.

Maintenant que notre fonction est terminée, vous pouvez exécuter **npm start** pour tester votre application. Connectez-vous avec le **nom d'utilisateur** : user2, **mot de passe** : password.

Vous devriez recevoir ce qui suit en réponse. Le _userId_, _token_ et _username_

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-52.png)

## Vérifier si un utilisateur s'est déjà connecté

Ensuite, nous voulons un moyen de vérifier s'il y a un utilisateur connecté chaque fois que l'application se charge. Pour cela, nous utilisons le hook useEffect.

```
 useEffect(() => {
    const loggedInUser = localStorage.getItem("user");
    if (loggedInUser) {
      const foundUser = JSON.parse(loggedInUser);
      setUser(foundUser);
    }
  }, []);
```

N'oubliez pas d'utiliser un tableau de dépendances vide dans votre hook useEffect afin qu'il vérifie s'il y a un utilisateur connecté la première fois que l'application se charge.

Maintenant, notre application devrait fonctionner parfaitement. Nous obtenons la page ci-dessous après qu'un utilisateur s'est connecté pour la première fois et que ses détails sont stockés. Si vous actualisez la page, vous verrez que notre utilisateur reste connecté et que la page connectée continue de s'afficher.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-55.png)


En bonus, voici comment implémenter la déconnexion.

## Implémentation de la fonctionnalité de déconnexion

Pour se déconnecter, nous vidons simplement l'état de l'utilisateur et supprimons l'utilisateur de localStorage.

Implémentons cela.

Tout d'abord, nous créons un bouton de déconnexion

```
<button onClick={handleLogout}>déconnexion</button>
```

Ensuite, nous créons la fonction de déconnexion.

```
const handleLogout = () => {
    setUser({});
    setUsername("");
    setPassword("");
    localStorage.clear();
  };
```

Et c'est tout, nous avons terminé.

Voici un lien vers le [gist](https://gist.github.com/onedebos/bbf7cd4634bce53103c1cfefa6164637) complet sur GitHub. Vous pouvez me suivre là-bas pour plus de mises à jour.