---
title: Comment construire un moteur de recherche Fullstack en temps réel avec React
  et Express avec Postgres
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-16T19:05:00.000Z'
originalURL: https://freecodecamp.org/news/react-express-fullstack-search-engine-with-psql
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/photo-1525278070609-779c7adb7b71.jpg
tags:
- name: Express
  slug: express
- name: postgres
  slug: postgres
- name: React
  slug: react
seo_title: Comment construire un moteur de recherche Fullstack en temps réel avec
  React et Express avec Postgres
seo_desc: "By Mohammad Iqbal\nIn this tutorial we will go through and setup a full\
  \ stack search engine with React as the front end, Node and Express for the server,\
  \ and PostgreSQL for the database. \nThis search engine will be slightly more complex\
  \ than a simple ..."
---

Par Mohammad Iqbal

Dans ce tutoriel, nous allons passer en revue et configurer un moteur de recherche full stack avec React comme front-end, Node et Express pour le serveur, et PostgreSQL pour la base de données. 

Ce moteur de recherche sera légèrement plus complexe qu'une simple configuration de recherche de texte. Par exemple, un utilisateur pourra obtenir des formes pluriel des mots ainsi que des temps passés et présents des mots. Une recherche de "cats" retournera également des résultats pour "cat". Une recherche de "walked" retournera un résultat de "walk", et ainsi de suite.

Au lieu de partir de zéro, nous pouvons utiliser un simple projet de démarrage :

[https://github.com/iqbal125/react-hooks-complete-fullstack](https://github.com/iqbal125/react-hooks-complete-fullstack)

Vous pouvez regarder une version vidéo fullstack de ce tutoriel ici 
[https://www.youtube.com/playlist?list=PLMc67XEAt-yzxRboCFHza4SBOxNr7hDD5](https://www.youtube.com/playlist?list=PLMc67XEAt-yzxRboCFHza4SBOxNr7hDD5)

### TS vector et TS query de PostgreSQL

Pour accomplir cette fonctionnalité de recherche complexe, nous utiliserons la [fonctionnalité de recherche de texte intégrée](https://www.postgresql.org/docs/10/datatype-textsearch.html) de PostgreSQL. 

Les 2 types de données qui rendront cela possible sont les types de données `tsvector` et `tsquery` de PSQL.

`tsvector` : une liste de **lexèmes**. Un **lexème** est un mot qui vous permet de fusionner différentes variations de ce mot. Par exemple, un texte de "walked" sera converti et enregistré comme un lexème de "walk". Cela retournera des résultats pour les recherches de texte de "walk", "walking" et "walked". 

`tsquery` : est une liste de lexèmes qui sont comparés avec des tsvectors. Un morceau de texte est d'abord converti en tsquery puis comparé avec un tsvector pour voir s'il y a une correspondance. 



![Image](https://www.freecodecamp.org/news/content/images/2019/09/image.png)

Ce diagramme explique essentiellement comment la vectorisation TS se produit. Lorsqu'un utilisateur soumet un post, le post ainsi que l'auteur du post sont convertis en un seul tableau de vecteurs TS et enregistrés sous forme de 1 ligne. 

De plus, les doublons sont supprimés et la forme de base du mot est utilisée comme lexème. 

### Exemple concret 

Disons que vous soumettez un post avec le titre "cats" et le corps "fishes". 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-73.png)

"cat" retournera un résultat de recherche de "cats"

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-74.png)

Cela fonctionnera également avec des pluriels non standard, "fish" retournera un résultat pour "fishes". 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-75.png)

Cela s'applique également aux temps présent et passé des mots. Disons que nous avons ce post de "walking" et "acted" : 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-76.png)

"walk" retournera un résultat de recherche de "walking" : 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-77.png)

Même chose avec "act" et "acted".

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-78.png)

Si vous voulez regarder sous le capot, les lexèmes ressemblent à ceci dans la base de données PSQL. 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-79.png)

La colonne de vecteur de recherche est 'cat': 1 'fish':2 'test91': 3. Remarquez que même si nous avons soumis notre post avec le titre "cats" et le corps "fishes", les mots sont convertis sous la forme racine. 

C'est essentiellement ce qui permet des comparaisons avec d'autres formes du mot et rend cette recherche complexe possible.  

Si cela vous semble bien, nous pouvons commencer avec la configuration du code.  

### Configuration de React

```jsx

//posts.js

.... 
const handleSearch = (event) => {
   setState({posts_search: []});
   const search_query = event.target.value
   axios.get('/api/get/searchpost', {params: {search_query: search_query} })
     .then(res => res.data.length !== 0
                    ? setState({posts_search: [...res.data]})
                    : null )
     .catch(function (error) {
       console.log(error);
       })
   }
   
....

    <TextField
      id="search"
      label="Recherche"
      margin="normal"
      onChange={handleSearch}
    />
    
 ...
```

Nous avons seulement vraiment besoin de 2 parties principales sur notre front-end pour que cela fonctionne. La fonction qui fait l'appel API au serveur et l'élément d'entrée qui déclenche la fonction à chaque frappe. 

La fonction `handleSearch()` extrait essentiellement le texte de l'élément d'entrée et l'envoie en tant que paramètre dans une requête **axios get**.

Cela peut facilement être inséré dans n'importe quel composant React. 

C'est vraiment tout pour la configuration de React. La vraie magie se passe côté serveur et base de données.

### Configuration de la base de données

Voici le **schéma SQL** pour les posts. Remarquez que nous n'avons qu'une seule colonne `search_vector` de type de données `TSVECTOR`. Nous n'avons pas de colonne `TSQUERY` puisque la requête n'est pas stockée dans notre base de données, elle est juste utilisée comme comparaison. 

```sql
CREATE TABLE posts (
  pid SERIAL PRIMARY KEY,
  title VARCHAR(255),
  body VARCHAR,
  search_vector TSVECTOR,
  user_id INT REFERENCES users(uid),
  author VARCHAR REFERENCES users(username),
  date_created TIMESTAMP,
  like_user_id INT[] DEFAULT ARRAY[]::INT[],
  likes INT DEFAULT 0
);
```

Cette colonne de vecteur de recherche contiendra les lexèmes pour le titre, le corps et l'auteur du post combinés en un seul tableau. Nous pouvons voir comment cela est utilisé dans la configuration du serveur. 

### Configuration du serveur

```javascript

//Search Posts
router.get('/api/get/searchpost', (req, res, next) => {
  search_query = String(req.query.search_query)
  pool.query(`SELECT * FROM posts
              WHERE search_vector @@ to_tsquery($1)`,
    [ search_query ], (q_err, q_res) => {
    if (q_err) return next(q_err);
    res.json(q_res.rows);
  });
});

//Save posts to db
router.post('/api/post/posttodb', (req, res, next) => {
  const body_vector = String(req.body.body)
  const title_vector = String(req.body.title)
  const username_vector = String(req.body.username)

  const search_array = [title_vector,
                         body_vector, 
                         username_vector]
  
  const values = [req.body.title, 
                  req.body.body, 
                  search_array, 
                  req.body.uid, 
                  req.body.username]
  
  pool.query(`INSERT INTO
              posts(title, body, search_array, user_id, author, date_created)
              VALUES($1, $2, to_tsvector($3), $4, $5, NOW())`,
    values, (q_err, q_res) => {
    if (q_err) return next(q_err);
    res.json(q_res.rows);
  });
});

```

Le moteur de recherche fonctionne grâce à ce que nous faisons au moment où nous enregistrons les posts, et non au moment où la recherche a lieu. 

Vous pouvez voir dans notre deuxième fonction que nous commençons par transformer notre titre, notre corps et l'auteur de notre post en chaînes de caractères, puis nous les combinons dans un tableau appelé `search_array`. 

Ensuite, nous utilisons une simple commande SQL insert pour insérer le post entier dans la base de données. Pendant ce temps, nous exécutons également la fonction `to_tsvector()` sur notre `search_array`. 

`to_tsvector()` est une fonction PSQL donnée et est ce qui transforme notre tableau en un `tsvector` et permet la recherche plus tard. 

Ensuite, la recherche devient simple à ce stade. Nous obtenons simplement notre texte du front-end et le convertissons en une chaîne de caractères. 

Ensuite, nous utilisons la fonction `to_tsquery()` pour le transformer en un type de données `tsquery`. Nous pouvons ensuite utiliser ce `ts_query` pour vérifier la colonne `search_vector` et voir s'il y a une correspondance avec l'opérateur `@@`.

Si oui, nous retournons les posts correspondants. Ensuite, les posts correspondants seront retournés à notre front-end comme une requête API régulière et seront résolus comme une promesse. 

Puisque React est une application monopage, le navigateur ne se rechargera pas et la recherche semblera en temps réel.  

Merci d'avoir lu !

> Connectez-vous avec moi sur Twitter pour plus de mises à jour sur les futurs tutoriels : [https://twitter.com/iqbal125sf](https://twitter.com/iqbal125sf)