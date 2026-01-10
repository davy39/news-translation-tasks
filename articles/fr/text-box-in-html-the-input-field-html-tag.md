---
title: Zone de texte en HTML – La balise de champ de saisie HTML
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-10T20:02:45.000Z'
originalURL: https://freecodecamp.org/news/text-box-in-html-the-input-field-html-tag
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/aaron-burden-y02jEX_B0O0-unsplash.jpg
tags:
- name: forms
  slug: forms
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Zone de texte en HTML – La balise de champ de saisie HTML
seo_desc: 'In this article you''ll learn how to create a text input field in HTML.
  You''ll also learn about web forms and get an overview of how they work, since text
  boxes are a common feature of every form.

  Let''s get started!

  What are Web Forms?

  Forms are an ef...'
---

Dans cet article, vous apprendrez à créer un champ de saisie de texte en HTML. Vous en apprendrez également sur les formulaires web et aurez un aperçu de leur fonctionnement, puisque les zones de texte sont une caractéristique courante de chaque formulaire.

Commençons !

## Qu'est-ce que les formulaires web ?
Les formulaires sont un moyen efficace de collecter des informations.

Il existe de nombreux cas où vous devriez remplir un formulaire physique, un document physique imprimé, et fournir des détails personnels.

Par exemple, vous pouvez remplir un formulaire et le remettre à quelqu'un lorsque vous commencez un nouvel emploi, ou lorsque vous allez pour un examen médical, ou lorsque vous êtes en train de louer/acheter une maison – ou à tout autre moment où des papiers sont nécessaires.

Tout comme les formulaires physiques, les formulaires web numériques en ligne sont un moyen de recevoir et de collecter des saisies, des informations et des données importantes des utilisateurs et des visiteurs, en utilisant une combinaison de technologies web.

Un formulaire web imite un formulaire physique en contenant des espaces pour que les utilisateurs remplissent leurs informations.

Les formulaires web utilisent une variété d'outils, ou *contrôles de formulaire*, pour collecter les saisies des utilisateurs.

Un site web peut avoir une boîte de recherche, ou un champ de saisie de texte, pour entrer une seule ligne de texte. Cela permet aux utilisateurs de rechercher quelque chose de spécifique.

Un site web peut également contenir un formulaire d'inscription qui permet aux utilisateurs de s'inscrire à une newsletter ou à d'autres mises à jour.

Cela contiendrait typiquement un champ de saisie de texte pour entrer le prénom, le nom et l'adresse e-mail de l'utilisateur.

De nombreux sites web ont également des formulaires d'inscription/connexion lors d'un achat en ligne, par exemple, où les utilisateurs entrent leur nom d'utilisateur dans un champ de texte et leur mot de passe dans un champ séparé. Bien que les champs de mot de passe soient également des champs de texte, chaque caractère de texte est couvert par un point noir pour masquer ce qui est tapé.

Un site web peut également avoir une zone de texte plus grande pour que les utilisateurs entrent des passages de texte plus longs, ce qui est utile pour laisser un commentaire sous un article de blog.

De nombreux formulaires permettent également à l'utilisateur de choisir une option particulière parmi plusieurs options en sélectionnant un bouton radio. Ils peuvent permettre à l'utilisateur de choisir plus d'une option en cochant/décochant une case à cocher.

Enfin, tous les formulaires ont un bouton de soumission, pour soumettre les données à un serveur où elles seront stockées ou traitées.

## Comment fonctionnent les formulaires web

Internet est un grand réseau mondial qui connecte des millions d'ordinateurs à travers le monde.

Les ordinateurs qui font partie du réseau communiquent entre eux en envoyant et en recevant des informations.

La manière dont cela est réalisé est grâce à l'architecture client/serveur de requête/réponse du web.

Le client, qui est typiquement un navigateur web tel que Google Chrome, envoie une requête à un serveur web.

Un serveur web est un matériel ou un logiciel informatique qui stocke les fichiers qui composent les sites web et les distribue chaque fois qu'il reçoit une requête pour le faire.

La requête pourrait être de visualiser un formulaire qui fait partie d'une page web.

Le serveur envoie en retour les fichiers qui composent le formulaire web en réponse. Le navigateur web assemble ensuite les fichiers ensemble et l'utilisateur visualise le formulaire dans le navigateur web.

Ce cycle de requête/réponse est structuré par un protocole, appelé HTTP (qui signifie HyperText Transfer Protocol).

Ainsi, lors de l'utilisation d'un formulaire web, un utilisateur entre les données nécessaires. Ensuite, après la validation côté client qui vérifie si tous les champs obligatoires sont remplis et si les données sont au bon format, l'utilisateur clique sur le bouton de soumission.

Les données sont ensuite envoyées au serveur en *paires nom-valeur* dans une requête HTTP. Cette méthode d'organisation des informations en paires nom-valeur garantit que les données correctes correspondent à l'élément de formulaire correct.

Ensuite, un langage côté serveur tel que PHP, Ruby ou Python est utilisé pour traiter les informations et les stocker dans une base de données pour une utilisation ou une récupération ultérieure.

## Comment créer des formulaires web en HTML

Pour créer un formulaire en HTML, vous devez utiliser l'élément `<form>` qui est utilisé pour collecter des informations.

L'élément `<form>` a une balise d'ouverture `<form>` et une balise de fermeture `</form>`.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire web</title>
</head>
<body>
    <form>
        
    </form>
</body>
</html>
```

L'élément `<form>` prend deux attributs :

- L'attribut `action`, qui spécifie l'URL où vous souhaitez que les données soient envoyées et traitées.
- L'attribut `method` qui accepte comme valeur l'un des deux verbes HTTP, soit `GET` soit `POST`. Si aucun attribut `method` n'est inclus, la méthode `GET` est utilisée par défaut.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire web</title>
</head>
<body>
    <form action="/url" method="GET">

    </form>
</body>
</html>
```

Cependant, cela seul ne collecte aucune saisie de l'utilisateur.

## Qu'est-ce que l'élément HTML `input` ?

L'élément `<input>` est le plus couramment utilisé pour collecter et récupérer les données des utilisateurs à partir d'un formulaire web.

C'est là que les utilisateurs entrent leurs données.

Il est imbriqué à l'intérieur de l'élément `<form>` et c'est un élément auto-fermant. Cela signifie qu'il ne nécessite pas de balise de fermeture. (Les balises de fermeture ont une barre oblique, `</>`.)

Vous l'utilisez pour créer différents styles de champs de saisie, ou *contrôles de saisie de formulaire*, pour que les utilisateurs entrent une variété de types d'informations.

Il crée des champs de texte, des champs d'e-mail, des champs de mot de passe, des cases à cocher, des boutons radio, des menus déroulants, des boutons de soumission, la possibilité de sélectionner et de télécharger des fichiers et des images depuis l'ordinateur de l'utilisateur, et bien plus encore.

La manière de déterminer le type de champ de saisie, ou contrôle de saisie de formulaire, est de définir l'attribut `type` et de lui attribuer une valeur.

La syntaxe générale de `<input>` ressemble à ceci :

```html
<input type="value"> <!-- la valeur de l'attribut type détermine le style du champ de saisie -->

```

Par exemple, pour créer un champ qui permet aux utilisateurs de télécharger un fichier, l'élément `<input>` ressemblerait à ceci :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire web</title>
</head>
<body>
    <form action="/url" method="GET">
        <input type="file">
    </form>
</body>
</html>
```

L'attribut `type` détermine quel type de données l'élément `input` peut accepter.

## Comment créer un champ de saisie de texte en HTML

La valeur par défaut de l'attribut `type` de `input` lorsqu'il n'est pas spécifié est **text**. Ainsi, la saisie de texte est le style de saisie le plus courant.

La ligne `<input type="text">` crée un champ de saisie de texte sur une seule ligne, où l'utilisateur peut taper n'importe quelle saisie de texte.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire web</title>
</head>
<body>
    <form action="/url" method="GET">
        <p>Veuillez entrer du texte ci-dessous :</p>
        <input type="text">
    </form>
</body>
</html>
```

Lorsque vous visualisez la page dans le navigateur, vous pouvez voir qu'un champ de saisie de texte sur une seule ligne a été créé :

![Screenshot-2022-01-09-at-5.52.22-PM](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-2022-01-09-at-5.52.22-PM.png)

### Comment ajouter un texte de remplissage à un champ de texte

Le texte de remplissage, également appelé texte de remplissage, est un moyen d'inciter et de donner un indice aux utilisateurs sur le type d'informations qu'ils doivent remplir dans le formulaire. Il peut également offrir une valeur par défaut avant qu'ils ne commencent à taper.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire web</title>
</head>
<body>
    <form action="/url" method="GET">
        <p>Veuillez entrer votre prénom et votre nom :</p>
        <input type="text" placeholder="John">
        <input type="text" placeholder="Doe">
    </form>
</body>
</html>
```

Le code ci-dessus donnerait le résultat suivant :

![Screenshot-2022-01-09-at-6.09.59-PM](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-2022-01-09-at-6.09.59-PM.png)

### L'importance de l'attribut `name` dans les champs de texte

Lors de la soumission du formulaire et de son envoi au serveur, le serveur doit distinguer et différencier les différents types de données soumises qu'il collecte.

Par exemple, il doit savoir lequel est le nom d'utilisateur, lequel est le mot de passe et lequel est l'adresse e-mail.

Cela signifie que chaque champ de texte a besoin d'un attribut `name` et d'une valeur pour rendre le type de données soumises plus clair.

Par exemple, vous pourriez utiliser ce qui suit pour inciter quelqu'un à entrer son nom complet dans un champ de texte :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire web</title>
</head>
<body>
    <form action="/url" method="GET">
        <p>Veuillez entrer votre nom complet :</p>
        <input type="text" name="name" placeholder="John Doe">
    </form>
</body>
</html>
```

![Screenshot-2022-01-09-at-6.28.10-PM](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-2022-01-09-at-6.28.10-PM.png)

Supposons que l'utilisateur entre le nom "John Bexley" dans le champ de texte. Cela deviendra alors la valeur de l'attribut `name`.

Comme mentionné précédemment, les données dans les formulaires sont envoyées en paires nom-valeur. Dans ce cas, le serveur saura que le `name` de l'utilisateur est `John Bexley`, spécifiquement cela ressemblera à `name=John Bexley`.

Pour donner un autre exemple :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire web</title>
</head>
<body>
    <form action="/url" method="GET">
        <p>Veuillez entrer votre prénom :</p>
        <input type="text" name="first_name" placeholder="John">
        <p>Veuillez entrer votre nom :</p>
        <input type="text" name="last_name" placeholder="Doe">
    </form>
</body>
</html>
```

Le code ci-dessus a deux champs de texte séparés pour que l'utilisateur entre son prénom et son nom séparément.

S'ils entrent "John" comme prénom, la paire nom-valeur envoyée au serveur serait `first_name=John`.

S'ils entrent "Bexley" comme nom, la paire nom-valeur envoyée au serveur serait `last_name=Bexley`.

### Comment rendre les informations de texte obligatoires

Vous pouvez faire en sorte que certains champs soient obligatoires et doivent être remplis par les utilisateurs.

HTML5 a introduit la validation côté client.

Il s'agit d'une fonctionnalité où un message est affiché si l'utilisateur n'a pas rempli les champs obligatoires ou n'a pas entré les informations correctement. Cela signifie également qu'ils ne pourront pas soumettre le formulaire.

Tout ce que vous devez faire pour activer cela est d'ajouter l'attribut `required` à l'élément `<input>`. Cet attribut n'a pas besoin d'avoir une valeur.

Gardez à l'esprit que lors de l'ajout de plusieurs attributs à l'élément `<input>`, vous n'avez pas à ajouter des éléments dans un certain ordre.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire web</title>
</head>
<body>
    <form action="/url" method="GET">
        <p>Veuillez entrer votre prénom et votre nom :</p>
        <input type="text" name="first_name" placeholder="John" required>
        <input type="text" name="last_name" placeholder="Doe" required>
        <button type="submit">Soumettre</button>  
    </form>
</body>
</html>
```

Regardez ce qui se passe si un utilisateur ne remplit pas l'un des champs :

![Screenshot-2022-01-09-at-6.59.44-PM](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-2022-01-09-at-6.59.44-PM.png)

Un message apparaîtra et l'utilisateur ne pourra pas soumettre le formulaire si les champs obligatoires n'ont pas été complétés.

### Comment définir un nombre minimum et maximum de caractères dans une zone de texte

Vous pouvez spécifier le nombre minimum et maximum de caractères qu'un utilisateur peut entrer dans un champ de texte.

Pour créer un nombre minimum de caractères, utilisez l'attribut `minlength`.

Par exemple, vous pouvez faire en sorte que le nom d'utilisateur d'un utilisateur soit *au moins* trois caractères de long :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire web</title>
</head>
<body>
    <form action="/url" method="GET">
        <p>Veuillez entrer votre nom d'utilisateur</p>
        <input type="text" name="username" minlength="3" required>
        <button type="submit">Soumettre</button>  
    </form>
</body>
</html>
```

L'utilisateur ne pourra pas soumettre le formulaire si le nom d'utilisateur est plus court que trois caractères :

![Screenshot-2022-01-10-at-4.04.00-PM](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-2022-01-10-at-4.04.00-PM.png)

Pour limiter le nombre de caractères qu'un utilisateur entre dans un champ de texte, utilisez l'attribut `maxlength`.

Un exemple de combinaison des attributs `minlength` et `maxlength` pourrait ressembler à ceci :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire web</title>
</head>
<body>
    <form action="/url" method="GET">
        <p>Veuillez entrer votre nom d'utilisateur</p>
        <input type="text" name="username" minlength="3" maxlength="20" required>
        <button type="submit">Soumettre</button>  
    </form>
</body>
</html>
```

Dans l'exemple ci-dessus, le nom d'utilisateur d'un utilisateur doit comporter au moins 3 caractères et ne pas dépasser 20 caractères.

### Comment étiqueter les contrôles de formulaire

Jusqu'à présent, j'ai utilisé un élément `<p>` pour écrire du texte avant la zone de texte, de cette manière incitant l'utilisateur et lui faisant savoir ce qu'il doit entrer.

Mais ce n'est pas une meilleure pratique et ce n'est pas accessible.

Chaque contrôle de formulaire, dans ce cas chaque champ de texte, doit avoir son propre élément `<label>`.

Cela rend le formulaire accessible pour les utilisateurs malvoyants qui utilisent des technologies d'assistance telles que les lecteurs d'écran.

Une façon de l'utiliser est de nestifier tout texte introductif et le `<input type="text">` dans un élément `<label>` comme ceci :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire web</title>
</head>
<body>
    <form action="/url" method="GET">
        <label>
            Veuillez entrer votre nom d'utilisateur
            <input type="text" name="username" minlength="3" maxlength="20" required>
        </label>
        <button type="submit">Soumettre</button>  
    </form>
</body>
</html>
```

![Screenshot-2022-01-10-at-4.58.37-PM](https://www.freecodecamp.org/news/content/images/2022/01/Screenshot-2022-01-10-at-4.58.37-PM.png)

Une autre façon d'utiliser l'élément `<label>` et d'avoir le même résultat est de le séparer de l'élément `<input>`.

Dans ce cas, l'attribut `for` doit être ajouté à `<label>`, et l'attribut `id` ajouté à `<input>`, afin d'associer les deux l'un à l'autre.

La valeur de `for` sera la même que `id`.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire web</title>
</head>
<body>
    <form action="/url" method="GET">
        <label for="username"> Veuillez entrer votre nom d'utilisateur :</label>
            <input type="text" id="username" name="username" minlength="3" maxlength="20" required>
        <button type="submit">Soumettre</button>  
    </form>
</body>
</html>
```

## Conclusion

En résumé, pour créer un champ de saisie de texte en HTML, vous avez besoin au moins :

- D'un élément `<input>`, qui est généralement placé à l'intérieur d'un élément `<form>`.
- De définir l'attribut `type` pour qu'il ait une valeur de `text`. Cela créera un champ de saisie de texte sur une seule ligne.
- N'oubliez pas d'ajouter un attribut `name`. Cela identifie les informations pour chaque contrôle de formulaire qui est créé et rend les choses plus claires pour le serveur.

Pour en savoir plus sur HTML et CSS, consultez la [Certification en Conception Web Réactive](https://www.freecodecamp.org/learn/2022/responsive-web-design/) de freeCodeCamp, où vous apprendrez de manière interactive tout en construisant des projets amusants en cours de route.

Merci d'avoir lu et bon codage !