---
title: Comment créer et valider des formulaires web modernes avec HTML5
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2022-08-10T15:45:20.000Z'
originalURL: https://freecodecamp.org/news/create-and-validate-modern-web-forms-html5
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Web-Forms-2.png
tags:
- name: HTML5
  slug: html5
- name: Web Development
  slug: web-development
seo_title: Comment créer et valider des formulaires web modernes avec HTML5
seo_desc: "HTML forms consist of a body of text boxes, buttons, dropdowns and other\
  \ selection widgets. Web developers use these elements to receive users' information\
  \ on a website. \nIf you've ever searched on Google, signed up or logged into a\
  \ website, made a p..."
---

Les formulaires HTML se composent d'un corps de zones de texte, de boutons, de listes déroulantes et d'autres widgets de sélection. Les développeurs web utilisent ces éléments pour recevoir les informations des utilisateurs sur un site web. 

Si vous avez déjà recherché sur Google, vous êtes inscrit ou connecté à un site web, avez effectué un paiement ou répondu à un questionnaire, vous avez interagi avec un formulaire web.

Lors de la création pour le web, vous devez vous assurer que votre application est accessible à tous les utilisateurs. Cela inclut ceux qui nécessitent des technologies d'assistance telles que les lecteurs d'écran pour naviguer sur un site web. 

HTML5 dispose d'éléments de formulaire sémantiques qui sont le meilleur moyen d'y parvenir. Heureusement, les avantages vont au-delà de l'accessibilité :

1. Ils facilitent le développement car ils viennent avec certaines fonctionnalités gratuites et sont généralement plus faciles à comprendre.
2. Meilleur sur mobile — le HTML sémantique est plus facile à rendre réactif pour différentes tailles d'écran. Ses fichiers sont généralement plus légers que le code spaghetti non sémantique.
3. Bon pour le SEO — votre page web aura plus de chances d'être trouvée par les clients car les moteurs de recherche privilégient les mots-clés à l'intérieur des titres, des liens, etc., par rapport à ceux dans les `<div>` non sémantiques.

Dans cet article, nous allons discuter des derniers éléments et attributs des formulaires HTML5 que vous pouvez utiliser pour construire et valider le formulaire simple mais moderne que vous voyez ici :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/HTML5Form.png)

Vous pouvez voir le code source [ici](https://codepen.io/ophyboamah/pen/wvmMagP).

# Comment utiliser les nouveaux éléments de formulaire HTML5

Au fil des ans, les formulaires web ont subi diverses modifications jusqu'à l'arrivée de HTML5. 

Avec l'introduction de nouveaux éléments et attributs HTML5 améliorés, tout le monde peut apprendre à construire des formulaires beaux, fonctionnels et accessibles. 

Parmi les nombreux éléments de formulaire, certains des plus essentiels incluent :

## Contour du formulaire – Comment utiliser les balises Fieldset, Legend et Label

Vous utilisez la balise `<fieldset>` pour regrouper des éléments liés (contrôles et étiquettes) dans un formulaire web en dessinant une boîte autour d'eux. Elle contient généralement des éléments comme legend, label et inputs. 

Vous utilisez la balise `<legend>` pour définir des légendes pour les éléments fieldset. De cette manière, elle peut également être utilisée comme un moyen de regrouper des éléments. Et la balise `<label>` donne une définition à plusieurs éléments.

Vous devez toujours lier la balise `<label>` à un élément `<input>` parce que :

1. Un utilisateur peut se concentrer sur l'input en cliquant sur le label
2. Lorsque l'input est focalisé, les lecteurs d'écran lisent le label à haute voix pour aider les utilisateurs en situation de handicap.
3. Pour les cases à cocher, surtout sur mobile, les utilisateurs qui ne peuvent pas facilement cliquer sur des éléments plus petits peuvent cliquer sur le label pour basculer la case à cocher.

```html
<fieldset class="first-section">
      <legend>Contact Details</legend>
      <label for="name">Name</label>
      <input type="text" id="name" name="name" autofocus placeholder="Ophy Boamah" autocomplete="on" required> <br><br>
      <label for="email">Email</label>
      <input type="email" id="email" placeholder="ob2@hotmail.com"> <br><br>
      <label for="tel">Phone</label>
      <input type="tel" id="tel" placeholder="+233 200001212"> <br><br>
</fieldset>


```

Dans le code ci-dessus, nous utilisons la balise fieldset pour créer un groupe initial étiqueté "first-section". La balise legend contient du texte qui fournit une description pour le groupe d'éléments. Enfin, la balise label identifie chacune des entrées et leur but.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Fieldset-2.png)
_Fieldset, Legend, et Label_

## Comment utiliser le texte de l'espace réservé

Vous utilisez le texte de l'espace réservé dans les champs de saisie, et il n'est supprimé que lorsque le champ de saisie est focalisé ou rempli. 

Généralement, le texte de l'espace réservé a une couleur de police plus claire par rapport à la couleur des étiquettes et des valeurs de saisie. Vous utiliserez principalement les espaces réservés pour donner à un utilisateur des informations supplémentaires sur ce qu'il doit remplir dans un formulaire. Voici un exemple :

```html
<input type="email" id="email" placeholder="ob2@hotmail.com">

```

L'attribut type="email" garantit que la saisie n'accepte aucune autre valeur que les emails. L'attribut id lie l'élément de saisie à son étiquette pour permettre l'association et la focalisation. Le "ob2@hotmail.com" donne à l'utilisateur un indice du type de valeur que la saisie attend.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Placeholder.png)
_Espace réservé pour la saisie de l'email_

## Comment utiliser le focus

Initialement, les utilisateurs devaient cliquer dans la première boîte de saisie d'un formulaire pour commencer à le remplir. Mais HTML5 permet aux développeurs web de mettre l'accent sur les saisies avec lesquelles les utilisateurs doivent interagir en premier. 

Autofocus est un attribut que vous pouvez ajouter à un élément `<input>` ou `<textarea>` à cette fin. C'est également une fonctionnalité d'accessibilité importante car elle facilite la vie des personnes qui utilisent des lecteurs d'écran, par exemple.

Voici un exemple de l'utilisation de autofocus :

```html
<input autofocus type="text" id="name" name="name" autofocus placeholder="Ophy Boamah" required>

```

Comme on peut le voir dans le code ci-dessus, vous pouvez placer l'attribut autofocus n'importe où dans la balise input. Il est souvent suivi ou entouré par les autres attributs génériques comme name, id, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Focus.png)
_Focus de la saisie_

# Comment utiliser les nouvelles saisies HTML5

Il est probablement sûr de dire que `<input>` est l'attribut le plus populaire d'un formulaire web. En fait, tout dans un formulaire est une saisie car il nécessite une forme de données de la part des utilisateurs. Vous utilisez cet attribut le plus souvent pour recevoir du texte, des nombres et des emails, et ainsi de suite.

Différents éléments sont différenciés en utilisant la valeur de l'attribut type dans les saisies. Voici trois nouveaux exemples utiles :

## Comment utiliser l'élément de recherche

Vous utilisez l'élément de recherche pour permettre aux utilisateurs d'entrer des requêtes lorsqu'ils doivent rechercher quelque chose. Il est très similaire aux saisies de texte. 

La principale chose qui les différencie serait le style, car l'accès à la saisie en utilisant le type input[type=search] tend à être super pratique par rapport à donner une classe à une saisie de texte.

```html
<input type="search" id="email" placeholder="ob2@hotmail.com">

```

Sur certains navigateurs comme Chrome, une fois que vous commencez à taper, une icône 'x' est placée à la fin du champ de saisie. En cliquant sur cette icône, la valeur tapée dans la saisie est effacée et l'utilisation de la touche esc sur votre clavier donne le même résultat. 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/search-1.png)
_Saisie de recherche_

## Comment utiliser l'élément caché

Les développeurs web utilisent des éléments cachés pour rendre le contenu d'une saisie caché et inaccessible à un utilisateur interagissant avec un formulaire. Ce type de saisie ne se rend pas exactement visuellement. Son contenu n'est pas vu par l'utilisateur mais lors de la soumission du formulaire, il est envoyé au serveur.

```html
<input type="hidden" id="indexNumber" name="indexNumber" value="00202010">
```

## Comment utiliser l'élément de progression

C'est un élément que vous pouvez utiliser pour indiquer la progression d'une tâche. L'attribut max est utilisé pour indiquer la valeur totale de la barre de progression. L'attribut value montre essentiellement le pourcentage de la tâche qui a été complété en colorant la barre à cette étendue. L'attribut id, comme toujours, est utilisé pour lier à l'étiquette.

```html
 <label for="days">Proficiency:</label>
<progress id="days" value="27" max="100"> 27% </progress> 

```

Contrairement à la saisie avec le type range, l'élément de progression ne permet pas aux utilisateurs de faire des changements. Au lieu de cela, il communique dans un style en lecture seule.

![Barre de progression](https://www.freecodecamp.org/news/content/images/2022/08/progress.png)
_Barre de progression_

## Comment utiliser l'élément de liste de données

L'élément de liste de données spécifie une liste d'options prédéfinies pour un élément. Il est souvent utilisé pour offrir des fonctionnalités de complétion automatique pour une liste d'éléments. Cela est dû au fait que dès que vous commencez à taper, vous obtenez un aperçu de la liste des options disponibles. 

Comme montré ci-dessous, afin de lier une balise `<input>` avec une `<datalist>`, vous devez vous assurer que la valeur de l'attribut 'list' est la même que l''id' sur la datalist. 

```html
<label for="gender">Gender ??</label>
      <input list="genders" name="gender" id="gender">
      <datalist id="genders">
        <option value="female">
        <option value="male">
        <option value="other">
      </datalist>

```

Cette saisie est rendue différemment sur les divers navigateurs :

**Chrome** : Une fois que vous survolez la saisie, une icône de liste déroulante est ajoutée à la fin de la saisie. Lorsque vous cliquez dans la saisie ou sur l'étiquette, les valeurs des diverses options sont également affichées dans une liste déroulante. 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Datalist-Chrome.png)

**Firefox** : Afin de voir les valeurs des options, l'utilisateur doit entrer une partie du texte et les options seront affichées dans un style de type complétion automatique.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/datalist.png)
_Liste de données_

# Qu'est-ce que la validation de formulaire ?

Construire le formulaire est la première étape de ce processus. En tant que développeur, vous devez toujours vous assurer que vos utilisateurs fournissent des réponses précises. Cela est nécessaire car vous ne devez pas supposer que les utilisateurs feront la bonne chose. 

C'est le concept de validation dans les formulaires – prévenir les erreurs ou les attraper dès qu'elles se produisent.

## Types de validation de formulaire

Il existe deux types populaires de validation d'un formulaire web. Ils sont :

### Validation côté client

La validation côté client peut être liée à la partie 'prévenir les erreurs' de la validation. Elle implique des stratégies telles que l'exécution de certaines vérifications dans le navigateur avant de soumettre le formulaire. 

Les méthodes de validation côté client incluent l'ajout de pop-ups d'erreur et ne pas laisser un utilisateur continuer jusqu'à ce qu'il remplisse les informations correctes.

### Validation côté serveur

La validation côté serveur peut être liée à la partie 'attraper les erreurs' de la validation. 

Contrairement au côté client, ce type ne vérifie pas les erreurs pendant que les utilisateurs sont encore sur le formulaire. Au lieu de cela, il vérifie lorsque les données du formulaire sont envoyées à votre serveur web. 

Dans ce cas, vous afficheriez une page d'erreur comme retour pour indiquer la présence d'erreurs.

# Méthodes populaires de validation côté client

## Validation côté client de base

Quelques exemples de validation côté client de base incluent "Ce champ est obligatoire", "Entrez un email valide", et "Le mot de passe doit comporter au moins 8 caractères".

Ce ne sont que quelques-uns des nombreux messages d'erreur lancés aux utilisateurs lorsqu'ils ne saisissent pas les données dans le format attendu par un formulaire. 

Les attributs les plus couramment utilisés incluent :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Name-validation.png)

1. **Required** : Spécifie les champs de saisie qui doivent être remplis avant de soumettre le formulaire.
2. **Minlength et Maxlength** : Spécifient la longueur minimale et maximale attendue d'une chaîne.
3. **Min et Max** : Spécifient les valeurs minimale et maximale des nombres.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Email-Validation.png)

4. **Type** : Spécifie le type de données nécessaire pour des champs de saisie spécifiques, par exemple date, nombre, nom, email, etc.

## L'API de validation de contraintes

Comme le suggère le nom, l'[API de validation de contraintes](https://developer.mozilla.org/en-US/docs/Web/API/Constraint_validation) est une API Web qui offre des fonctionnalités de validation aux formulaires web. Vous pouvez utiliser ses nouvelles propriétés et méthodes pour modifier la validité d'une saisie de formulaire. 

Les développeurs peuvent maintenant facilement donner des fonctionnalités personnalisées et des messages d'erreur. Essentiellement, cette API vous permet de détecter les erreurs et d'afficher un message personnalisé basé sur le type d'erreur.

Vous pouvez créer une validation personnalisée et des messages d'erreur avec la méthode setCustomValidity ainsi que la propriété validationMessage.

## Autres éléments utiles à connaître

<table>
<thead>
<tr>
<th style="text-align: left">Élément</th>
<th style="text-align: center">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left"><code>autocomplete</code></td>
<td style="text-align: center">Vous pouvez utiliser l'autocomplétion pour rappeler les valeurs récemment tapées dans une saisie donnée. En dehors des données sensibles et des codes PIN à usage unique, c'est une fonctionnalité qui fait gagner du temps. Vous pouvez activer sa valeur pour la recommander pour un champ de saisie particulier ou vice versa.</td>
</tr>
<tr>
<td style="text-align: left"><code>autocorrect</code></td>
<td style="text-align: center">Utilisez ces attributs pour contrôler les fonctionnalités de correction automatique et de mise en majuscule sur certains appareils mobiles (à savoir, la version de Safari qui fonctionne sur les iPads et les iPhones)</td>
</tr>
<tr>
<td style="text-align: left"><code>spellcheck</code></td>
<td style="text-align: center">Vous pouvez définir cet attribut à true pour indiquer que l'utilisateur doit vérifier l'orthographe de certains textes, en particulier les chaînes tapées dans une saisie. Le seul problème qui en découle est que tous les textes tapés dans la saisie ne sont pas censés avoir du sens en tant que mots réels.</td>
</tr>
</tbody>
</table>

# Mettre le tout ensemble

Voici le résultat de la mise en commun des différents éléments que vous avez appris dans cet article :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/WebForm.png)

Voici le code pour cela :

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bootcamp Registration</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet"> 
</head>
<body>
  <div class="form">
    <h1>Bootcamp Registration Form</h1>
  <p>Complete this form to express your interest in the upcoming web development bootcamp.</p>
  <form>
<!-- Contact Details -->
    <fieldset class="first-section">
      <legend>Contact Details</legend>
      <label for="name">Name</label>
      <input autofocus type="text" id="name" name="name" autofocus placeholder="Ophy Boamah" autocomplete="on" required> <br><br>
      <label for="email">Email</label>
      <input type="email" id="email" placeholder="ob2@hotmail.com"> <br><br>
      <label for="tel">Phone</label>
      <input type="tel" id="tel" placeholder="+233 200001212"> <br><br>
    </fieldset>
    <!-- Personal Information -->
    <fieldset class="second-section">
      <legend>Personal Information</legend>
      <label for="dob">Birth Date</label>
      <input type="date" id="dob"> <br><br>
        <label for="gender">Gender ??</label>
      <input list="genders" name="gender" id="gender">
      <datalist id="genders">
        <option value="female">
        <option value="male">
        <option value="other">
      </datalist><br><br>
     <div class="proficiency">
        <label for="profeciency">Proficiency</label>
      <input type="range" value="4" max="10" id="profeciency" name="profeciency">
     </div>

    </fieldset>
     <!-- Preferred Language -->
     <div class="terms">
        <input type="checkbox" id="scales" name="scales" class="checkbox">
      <label for="scales">I have read and agree to the terms and conditions</label>
     </div>
    <button>Submit</button>
  </form>
  </div>
</body>
</html>
```

```css
* {
  font-family: 'Montserrat', sans-serif;
}

body {
  height: 80vh;
  margin-top: 5rem;
  background-image: url("https://images.unsplash.com/photo-1595675024853-0f3ec9098ac7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8Y29kaW5nJTIwYm9vdGNhbXB8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  padding: 10px;
}

.form {
  background-color: #fff;
  border-radius: 5px;
  padding: 15px 25px;
  width: 80%;
  margin: 0 auto;
}

.checkbox {
  width: 20px !important;
}

.first-section input {
  width: 85%;
  height: 25px;
  margin-left: 5px;
}

.second-section input{
  width: 80%;
  height: 25px;
  margin-left: 5px;
}

.form h1, p {
  text-align: center;
}
button {
  border: none;
  color: white;
  background: #1560BD;
  padding: 8px 25px;
  border-radius: 5px;
  display: block;
  margin: 20px auto 10px auto;
  width: 120px;
}

.second-section {
  margin-top: 15px;
}

.proficiency {
  display: flex;
  align-items: center;
}

.terms {
  margin-top: 15px;
  display: flex;
  align-items: center;
}

```

## Conclusion

Les nouveaux éléments et attributs de formulaire HTML5 facilitent l'accès à certaines fonctionnalités essentielles. Surtout celles qui n'étaient autrement possibles qu'avec CSS ou de nombreuses lignes de JavaScript. 

Il est maintenant plus facile que jamais de créer des formulaires web à la fois modernes et fonctionnels avec uniquement HTML. Plus important encore, cela apporte la tranquillité d'esprit aux développeurs web. Parce que vous savez que vous pouvez facilement créer des formulaires qui seront uniformes sur les différents navigateurs.

Merci d'avoir lu 👋🏾. J'espère que vous avez trouvé cela utile.