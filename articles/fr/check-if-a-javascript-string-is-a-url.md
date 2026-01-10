---
title: Comment vérifier si une chaîne JavaScript est une URL valide
subtitle: ''
author: Vikram Aruchamy
co_authors: []
series: null
date: '2022-06-24T15:09:54.000Z'
originalURL: https://freecodecamp.org/news/check-if-a-javascript-string-is-a-url
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/freecodecamp_new.jpeg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment vérifier si une chaîne JavaScript est une URL valide
seo_desc: 'A URL – or Uniform Resource Locator – is text used to identify resources
  like web pages, images, and videos on the internet.

  We commonly refer to URLs as website addresses, and they''re used for file transfer,
  emails, and other applications.

  URLs cons...'
---

Une URL – ou Uniform Resource Locator – est un texte utilisé pour identifier des ressources comme des pages web, des images et des vidéos sur Internet.

Nous faisons communément référence aux URLs comme des adresses de sites web, et elles sont utilisées pour le transfert de fichiers, les emails et d'autres applications.

Les URLs se composent de plusieurs parties – protocole, nom de domaine, etc. – qui indiquent au navigateur comment et où récupérer la ressource.

En JavaScript, vous pouvez avoir besoin d'utiliser une URL dans les balises d'ancrage ou les boutons pour lier l'utilisateur à une autre page web. Cette chaîne URL doit être vérifiée pour s'assurer qu'il s'agit d'une URL valide dans de telles situations.

Ce tutoriel vous apprendra quelques méthodes pour vérifier si une chaîne JavaScript est une URL valide.

Pour apprendre comment obtenir l'URL actuelle en JavaScript, vous pouvez lire cet article sur [Comment obtenir l'URL actuelle en JavaScript](https://www.jsowl.com/how-to-get-the-current-url-in-javascript/).

## Comment vérifier si une chaîne est une URL valide en utilisant Regex

Les expressions régulières (regex) sont des motifs qui correspondent à des combinaisons de caractères dans une chaîne JavaScript. En JavaScript, les [expressions régulières](https://www.freecodecamp.org/news/a-quick-and-simple-guide-to-javascript-regular-expressions-48b46a68df29/) sont également connues comme des objets qui fournissent différentes méthodes pour effectuer diverses opérations.

Vous pouvez construire une expression régulière de deux manières :

* En utilisant des littéraux d'expression régulière
* En utilisant des constructeurs d'expression régulière

**Note :** Il est approprié d'utiliser la méthode d'expression régulière lorsque vous voulez simplement vérifier si une chaîne est une URL valide et que vous ne voulez pas créer d'autres objets supplémentaires.

Apprenons comment ces deux méthodes fonctionnent.

### Comment utiliser des littéraux d'expression régulière

Dans un littéral d'expression régulière, le motif est enfermé entre des barres obliques, comme vous le verrez ci-dessous.

Le motif inclut la validation des parties nécessaires dans l'`URL`. Par exemple, un protocole, `https`, un `//`, etc.

```
const urlPattern = /(?:https?):\/\/(\w+:?\w*)?(\S+)(:\d+)?(\/|\/([\w#!:.?+=&%!\-\/]))?/;

```

### Comment utiliser un constructeur d'expression régulière

Pour créer une expression régulière en utilisant la méthode de construction, utilisez le constructeur `RegExp()` et passez le motif comme paramètre.

```
const urlPattern = new RegExp('(?:https?):\/\/(\w+:?\w*)?(\S+)(:\d+)?(\/|\/([\w#!:.?+=&%!\-\/]))?');

```

Pour démontrer comment valider si une chaîne est une `URL`, créons une méthode qui validera une chaîne JavaScript `String` en utilisant le constructeur d'expression régulière et retournera `True` ou `False` en fonction du motif correspondant.

```js
	const isValidUrl = urlString=> {
	  	var urlPattern = new RegExp('^(https?:\\/\\/)?'+ // valider le protocole
	    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // valider le nom de domaine
	    '((\\d{1,3}\\.){3}\\d{1,3}))'+ // valider OU l'adresse IP (v4)
	    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // valider le port et le chemin
	    '(\\?[;&a-z\\d%_.~+=-]*)?'+ // valider la chaîne de requête
	    '(\\#[-a-z\\d_]*)?$','i'); // valider le localisateur de fragment
	  return !!urlPattern.test(urlString);
	}

```

### Comment utiliser regex pour valider une chaîne URL

Le code ci-dessous démontre comment valider différentes chaînes URL en utilisant la méthode ci-dessus :

```js
	var url = "invalidURL";
	console.log(isValidUrl(url));      //false
	 
	var url = "htt//jsowl";            //false
	console.log(isValidUrl(url));
	
    var url = "www.jsowl.com";         //true
    console.log(isValidUrl(url));
    
    var url = "https://www.jsowl.com"; //true
    console.log(isValidUrl(url));
    
    var url = "https://www.jsowl.com/remove-an-item-from-an-array-in-javascript/";
    console.log(isValidUrl(url));      //true

```

## Comment vérifier si une chaîne est une URL valide en utilisant le constructeur URL

Vous pouvez utiliser le constructeur URL pour vérifier si une chaîne est une URL valide.

[URLConstructor](https://developer.mozilla.org/en-US/docs/Web/API/URL) (`new URL(url)`) retourne un nouvel objet URL défini par les paramètres URL.

Une exception JavaScript [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError) est levée si l'URL donnée n'est pas valide.

**Note :** Il est approprié d'utiliser cette méthode lorsque vous voulez construire un objet URL dans votre programme pour des utilisations ultérieures.

### Syntaxe du constructeur URL

La syntaxe suivante explique comment créer un objet URL avec une chaîne JavaScript.

```
new URL(url);
new URL(url, base);

```

Où,

* `url` est une chaîne ou tout objet avec un [stringifier](https://developer.mozilla.org/en-US/docs/Glossary/Stringifier) qui représente une URL absolue ou relative. Si **URL** est une URL absolue, **base** sera ignorée. Si **URL** est une URL relative, **base** est requise.
* `base` (optionnel) est une chaîne représentant l'URL de base. Elle doit être passée lorsque l'URL est relative. Par défaut, elle est _undefined_ lorsqu'elle est ignorée.

### Exemple de méthode de constructeur URL

Pour démontrer comment fonctionne la méthode de constructeur URL, créons une fonction lambda en JavaScript pour construire une nouvelle URL avec la chaîne passée.

* Si la chaîne est une URL valide, un objet URL est créé et `true` est retourné
* Si la chaîne n'est pas une URL valide, une exception `TypeError` est levée et `false` est retourné

```
const isValidUrl = urlString=> {
      try { 
      	return Boolean(new URL(urlString)); 
      }
      catch(e){ 
      	return false; 
      }
  }

```

### Comment utiliser la méthode `isValidURL()`

Invoquons la méthode `isValidURL()` pour différents types de chaînes et voyons les résultats.

```
  var url = "invalidURL";
  console.log(isValidUrl(url));     //false
  
  var url = "htt//jsowl";
  console.log(isValidUrl(url));     //false
  
  var url = "www.jsowl.com";
  console.log(isValidUrl(url));     //false
  
  var url = "tcp://www.jsowl.com";
  console.log(isValidUrl(url));     //true
  
  var url = "https://www.jsowl.com/remove-an-item-from-an-array-in-javascript/";
  console.log(isValidUrl(url));     //true

```

Dans les trois premiers cas, vous pouvez voir qu'une _chaîne URL invalide_ est passée. Par conséquent, la création de l'objet URL échoue avec une `TypeError` et `false` est retourné.

Dans les deux derniers cas, une _chaîne URL valide_ est passée. Donc un objet `URL` est créé avec succès et `True` est retourné, confirmant l'URL correcte.

Regardons un autre exemple pour valider une partie spécifique de l'URL.

Dans cet exemple, vous validez un protocole spécifique dans l'URL. L'URL doit contenir le protocole `http` ou `https`.

```
	const isValidUrl = urlString=> {
		let url;
		try { 
	      	url =new URL(urlString); 
	    }
	    catch(e){ 
	      return false; 
	    }
	    return url.protocol === "http:" || url.protocol === "https:";
	}

```

### Exemple de validation d'une partie d'une URL

Invoquons la méthode `isValidURL()` pour différents types de chaînes et protocoles et voyons les résultats.

```
var url = "tcp://www.jsowl.com";
console.log(isValidUrl(url));      //false

var url = "https://www.jsowl.com";
console.log(isValidUrl(url));      //true

```

Dans le premier cas, la chaîne URL _(tcp://www.jsowl.com)_ est valide, mais elle ne contient pas de protocole spécifique (`HTTP`/`HTTPS`). Donc elle retourne _false_.

Dans le deuxième cas, la chaîne URL _[https://www.jsowl.com](https://www.jsowl.com)_ est _valide_ et contient le protocole spécifique. Donc elle retourne _true_.

## Comment vérifier si une chaîne est une URL valide en utilisant un élément d'entrée

HTML supporte un élément d'entrée avec le type [`url`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/url), spécifiquement pour représenter des valeurs d'URL.

L'attribut `value` de l'élément `<input>` contenant la chaîne est automatiquement validé en correspondant à la syntaxe de l'URL (_soit vide soit correctement formée_) avant que le formulaire puisse être soumis.

La méthode [`HTMLInputElement.checkValidity()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checkValidity) est utilisée pour vérifier si une chaîne dans l'attribut de valeur de l'élément `<input>` est une `URL`. La méthode `checkValidity()` retourne `true` si la valeur est une URL correcte et `false` si l'entrée n'est pas une URL correcte.

Créons une méthode qui crée un élément d'entrée de type `URL` et valide l'entrée en utilisant la méthode `checkValidity()`.

```
    const isValidUrl = urlString =>{
      var inputElement = document.createElement('input');
      inputElement.type = 'url';
      inputElement.value = urlString;

      if (!inputElement.checkValidity()) {
        return false;
      } else {
        return true;
      }
    } 

```

Utilisons maintenant cette méthode et validons différentes chaînes pour voir si elles sont des URLs valides.

```
    var url = "invalidURL";
    console.log(isValidUrl(url));     //false
    
    var url = "htt//jsowl";
    console.log(isValidUrl(url));     //false
    
    var url = "www.jsowl.com";
    console.log(isValidUrl(url));     //false
    
    var url = "https://www.jsowl.com";
    console.log(isValidUrl(url));     //true
    
    var url = "https://www.jsowl.com/remove-an-item-from-an-array-in-javascript/";
    console.log(isValidUrl(url));     //true

```

Voici comment vous pouvez utiliser la méthode de type d'entrée pour vérifier si une chaîne est une URL valide.

## Comment vérifier si une chaîne est une URL valide en utilisant la méthode de la balise d'ancrage

Cette section vous apprend à utiliser [HTMLAnchorElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAnchorElement) pour vérifier si une chaîne JavaScript est une URL.

**Note :** Il est approprié d'utiliser cette méthode lorsque vous voulez assigner une URL à la balise `anchor` de votre page web et vous assurer que la chaîne URL est valide et est assignée correctement à la balise `anchor`.

L'interface `HTMLAnchorElement` représente des éléments hyperliens. Elle fournit des propriétés et méthodes spéciales pour manipuler la mise en page et la présentation de tels éléments. Elle est également appelée une balise d'ancrage.

Vous pouvez assigner une URL à une balise d'ancrage en utilisant l'attribut `href`. Lors de l'assignation,

* Si une chaîne URL valide est passée, elle est assignée à la balise d'ancrage
* Si une URL invalide est passée, la [localisation actuelle du navigateur](https://www.jsowl.com/how-to-get-the-current-url-in-jquery/) est assignée à la balise d'ancrage
* Par défaut, la balise d'ancrage aura une URL vide ("")

Une fois l'URL assignée, vous pouvez extraire une partie spécifique de l'URL en utilisant les attributs expliqués ci-dessous.

<table>
<thead>
<tr>
<th>Attribut HTMLAnchorElement</th>
<th>usage</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>host</code></td>
<td>une chaîne représentant le nom d'hôte et le port</td>
</tr>
<tr>
<td><code>hostname</code></td>
<td>une chaîne représentant le nom d'hôte</td>
</tr>
<tr>
<td><code>href</code></td>
<td>une chaîne contenant une URL valide</td>
</tr>
<tr>
<td><code>origin</code></td>
<td>retourne une chaîne contenant l'origine, son schéma, le nom de domaine et le port</td>
</tr>
<tr>
<td><code>port</code></td>
<td>une chaîne représentant le port si spécifié</td>
</tr>
<tr>
<td><code>protocol</code></td>
<td>une chaîne représentant le protocole incluant le caractère final ('<code>:</code>')</td>
</tr>
<tr>
<td><code>pathname</code></td>
<td>une chaîne contenant le chemin de l'URL à partir du début (/) et n'incluant pas la chaîne de requête</td>
</tr>
</tbody>
</table>

Maintenant, voyons comment vérifier si la chaîne assignée était une URL correcte.

Si c'était une URL correcte, elle serait assignée à la balise d'ancrage. Sinon, la localisation actuelle du navigateur sera assignée à la balise d'ancrage.

Donc, pour vérifier si c'était une URL correcte, vous pouvez vérifier si l'`host` de la balise d'ancrage n'est PAS égal à la localisation actuelle en utilisant l'instruction `a.host != window.location.host`.

Regardons le code.

Nous créons une fonction lambda et l'assignons à la constante `isValidUrl` dans le code ci-dessous.

La fonction crée un élément de balise d'ancrage et assigne la chaîne URL à la balise d'ancrage. Après cela, elle vérifie si l'attribut `host` de l'élément est `null` ou non défini.

Si ce n'est pas null, elle vérifie si l'attribut `host` n'est PAS égal à l'URL actuelle du navigateur et retourne `True` lorsqu'il n'est pas égal. 

C'est parce que si l'URL passée était valide, alors la balise d'ancrage aura la valeur de l'URL. Mais si l'URL passée était invalide, la balise d'ancrage aura la localisation actuelle du navigateur. Dans ce cas, la fonction lambda retourne `False`.

```
const isValidUrl = urlString =>{	
  	var a  = document.createElement('a');
   	a.href = urlString;
   	return (a.host && a.host != window.location.host);
  }

```

Les extraits de code ci-dessous invoquent la fonction lambda `isValidUrl()` avec différentes entrées et impriment la sortie correspondante dans la console.

```js
  var url = "invalidURL";
  console.log("1.AnchorTag:  " +isValidUrl(url));    //false
  
  var url = "htt//jsowl";
  console.log("22.AnchorTag:  "+isValidUrl(url));    //false
  
  var url = "www.jsowl.com";  
  console.log("3.AnchorTag:  " +isValidUrl(url));    //false  
  
  var url = "https://www.jsowl.com";  
  console.log("4.AnchorTag:  " +isValidUrl(url));    //true 
  
  var url = "https://www.jsowl.com/remove-an-item-from-an-array-in-javascript/";
  console.log("5.AnchorTag:  " +isValidUrl(url));    //true 

```

Ce tutoriel est disponible dans [ce](https://jsfiddle.net/jsowl/mvzqh4of/266/) JSFiddle.

## Conclusion

Dans cet article, vous avez appris comment vérifier si une chaîne JavaScript est une `URL` en utilisant différentes méthodes et quand il est approprié d'utiliser chaque méthode.

Si vous avez aimé cet article, n'hésitez pas à le partager.

Vous pouvez [consulter mes autres tutoriels sur mon blog, JS Owl](https://www.jsowl.com/).