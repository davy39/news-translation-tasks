---
title: Comment utiliser les formulaires HTML – Les bases des formulaires HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-03-06T10:37:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-html-forms
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/glenn-carstens-peters-RLw-UC03Gwc-unsplash.jpg
tags:
- name: Form validations
  slug: form-validations
- name: forms
  slug: forms
- name: HTML
  slug: html
seo_title: Comment utiliser les formulaires HTML – Les bases des formulaires HTML
seo_desc: "By Kelechukwu Isaac Awoke\nHTML forms are used to get information from\
  \ users. They are widely used in webpages or apps for surveys or registration processes.\
  \ \nHTML form basics include the common HTML elements, tags, attributes, concepts,\
  \ or best pract..."
---

Par Kelechukwu Isaac Awoke

Les formulaires HTML sont utilisés pour obtenir des informations des utilisateurs. Ils sont largement utilisés dans les pages web ou les applications pour les sondages ou les processus d'inscription. 

Les bases des formulaires HTML incluent les éléments HTML courants, les balises, les attributs, les concepts ou les meilleures pratiques nécessaires pour créer de bons formulaires HTML. Les données collectées sont envoyées à un serveur pour traitement.

* [Structure de base d'un formulaire HTML](#heading-structure-de-base-dun-formulaire-html)
* [Comment utiliser les éléments de formulaire HTML](#heading-comment-utiliser-les-elements-de-formulaire-html)
* [Comment utiliser l'élément HTML <input>](#heading-comment-utiliser-lelement-html-input)
* [Comment utiliser l'élément HTML <label>](#heading-comment-utiliser-lelement-html-label)
* [Comment utiliser l'élément HTML <textarea>](#heading-comment-utiliser-lelement-html-textarea)
* [Comment utiliser l'élément HTML <select>](#heading-comment-utiliser-lelement-html-select)
* [Validation de formulaire](#heading-validation-de-formulaire)
* [Importance de la validation de formulaire](#heading-importance-de-la-validation-de-formulaire)
* [Types de validation de formulaire](#heading-types-de-validation-de-formulaire)
* [Techniques de validation courantes](#heading-techniques-de-validation-courantes)
* [Soumission de formulaire et méthodes](#heading-soumission-de-formulaire-et-methodes)
* [Comment styliser les formulaires HTML](#heading-comment-styliser-les-formulaires-html)
* [Meilleures pratiques et accessibilité](#heading-meilleures-pratiques-et-accessibilite)
* [Conclusion](#heading-conclusion)

## Structure de base d'un formulaire HTML

Vous pouvez utiliser l'élément `<form>` pour créer un formulaire HTML

```html
<form action="submit_form" method=" post">
  <label for="name">Nom :</label>
  <input type="text" id="name" name=" name" required>
  
  <label for="email">Email :</label>
  <input type="email" id="email" name="email" required>
  
  <button type="submit">Soumettre</button>
</form>
```

L'élément HTML `<form>` est un conteneur pour plusieurs éléments de formulaire HTML. L'élément `<form>` peut contenir les éléments suivants :

* `<input>`
* `<label>`
* `<select>`
* `<textarea>`
* `<button>`
* `<fieldset>`
* `<legend>`
* `<datalist>`
* `<output>`
* `<option>`
* `<optgroup>`

## Comment utiliser les éléments de formulaire HTML

Dans cette section, vous apprendrez à utiliser certains des éléments de formulaire HTML.

### Comment utiliser l'élément HTML <input>

L'élément `<input>` est l'élément de formulaire le plus couramment utilisé. Le type d'information qu'un élément `<input>` peut contenir dépend de l'attribut `<type>`. 

L'élément `<input>` ne peut accepter qu'un type particulier de données qui lui est assigné en utilisant l'attribut `<type>`.

```html
<form action="">
      <input
        type="text"
        id="name"
        name="username"
        placeholder="Entrez votre nom d'utilisateur"
        required
      />
      <input
        type="password"
        id="security"
        name="password"
        placeholder="Entrez votre mot de passe"
        required
      />
      <input type="email" name="email" placeholder="Entrez votre email" />
      <input type="checkbox" name="subscribe" value="yes" /> S'abonner à la
      newsletter <input type="radio" name="gender" value="male" /> Homme
      <input type="radio" name="gender" value="female" /> Femme
      <input type="submit" name="submit" />
</form>
```

Les attributs `<type>` suivants peuvent être assignés à un élément `<input>` :

* `<input type="text">` : Permet à l'utilisateur de saisir du texte.
* `<input type="email">` : La saisie de l'utilisateur doit suivre un format d'email.
* `<input type="password">` : Accepte un mot de passe de l'utilisateur. Les mots de passe sont masqués, généralement affichés sous forme d'astérisques (*) ou de points, pour protéger la confidentialité de la saisie.
* `<input type="checkbox">` : L'utilisateur peut sélectionner aucune ou plusieurs des cases à cocher affichées. Les cases à cocher peuvent être cochées ou décochées.
* `<input type="radio">` : Permet à l'utilisateur de sélectionner une seule option parmi les boutons radio à choix multiples.
* `<input type="submit">` : Permet à l'utilisateur de soumettre le formulaire.

Les attributs suivants sont d'autres attributs possibles trouvés dans l'élément input :

* `<input name=" ">` : Assigne un nom au champ de saisie. Le nom assigné identifie les données de saisie lorsque le formulaire est soumis.
* `<input id=" ">` : L'identifiant crée un id unique pour le champ de saisie. Il est généralement associé au CSS pour le style et à JavaScript pour d'autres manipulations.
* `<input value=" ">` : Utilisé pour définir la valeur initiale du champ de saisie. La valeur initiale par défaut donne à l'utilisateur une idée des informations requises.
* `<input placeholder=" ">` : Une valeur pseudo faible définie pour le champ de saisie qui disparaît une fois que l'utilisateur commence à taper. Donne un indice sur les données à entrer, similaire à l'attribut value.
* `<input required>` : Exige que le champ de saisie soit rempli avant la soumission. Affiche un message d'erreur lorsqu'il n'est pas rempli.
* `<input disabled>` : Comme son nom l'indique, cela empêche l'utilisateur d'interagir avec le champ de saisie. Désactive le champ de saisie pour qu'il n'accepte pas de saisie. Avec cet attribut, le champ de saisie devient non cliquable.
* `<input readonly>` : L'utilisateur ne peut que lire la valeur initialement définie mais ne peut pas la changer. Contrairement à l'attribut disabled, le champ de saisie est cliquable mais ne peut pas être modifié.

Notez que l'élément `<input>` ne contient pas d'attribut `for`.

### Comment utiliser l'élément HTML <label>

L'élément label associe du texte à une saisie de formulaire, une case à cocher ou un bouton radio.

```html
<form action=" ">
	<label for="name" id="user">Nom d'utilisateur :</label>
</form> 
```

L'élément label décrit les informations requises dans le champ de texte.

L'élément label est important pour l'accessibilité, ce qui facilite la navigation dans le formulaire pour les utilisateurs de lecteurs d'écran. Les technologies d'assistance lisent le label à haute voix pour les utilisateurs.

Cliquer sur le label met en focus le champ de saisie correspondant lorsque l'attribut `for` de l'élément label correspond à l'attribut id de l'élément de saisie, ce qui rend plus pratique pour les utilisateurs d'interagir avec le formulaire.

Label améliore l'utilisation globale du formulaire, fournissant un contexte et des conseils.

Les attributs suivants sont les attributs couramment utilisés pour l'élément `label` :

* `<label for=" "></label>` : Associe le label à l'élément de formulaire correspondant, généralement un élément de saisie. La valeur de l'attribut `for` est toujours la même que la valeur id de l'élément de formulaire associé, généralement l'élément de saisie.
* attribut id `<label id=" "></label>` : Donne au label un identifiant unique. La valeur est définie sur la même valeur que l'attribut `for` de l'élément de formulaire correspondant, généralement un élément de saisie. Utilisé pour sélectionner le label pour le style en CSS ou d'autres manipulations en JavaScript.

### Comment utiliser l'élément HTML <textarea>

Un champ de saisie de texte multiligne, permet aux utilisateurs d'écrire des textes plus longs ou des paragraphes. Les attributs `rows` et `cols` contrôlent la taille initiale de la zone de texte. 

```html
<form action="">
      <label for="testimony">Témoignage :</label>
      <textarea name="testimony" id="testimony" cols="30" rows="10"></textarea>
</form>
```

L'attribut `rows` contrôle la hauteur (taille verticale) de la zone de texte, déterminant le nombre de lignes visibles tandis que l'attribut `cols` contrôle la largeur (taille horizontale), spécifiant le nombre de caractères visibles par ligne. 

Notez que la zone de texte peut s'ajuster pour faire tenir le texte saisi dans sa largeur définie.

Contrairement au champ de saisie monoligne, l'élément `textarea` n'a pas d'attribut `maxlength` ou d'attribut `value`. Le contenu est placé entre les balises d'ouverture et de fermeture. 

Pour l'accessibilité, il est bon de pratique d'associer un label ou un contexte avec l'élément `textarea` pour aider les utilisateurs qui utilisent des lecteurs d'écran ou d'autres technologies d'assistance.

#### Comment utiliser l'élément HTML <select>

L'élément `<select>` crée une liste déroulante, qui permet aux utilisateurs de sélectionner une ou plusieurs options parmi les choix listés.

```html
<form action="">
      <label for="numbers">Choisissez un nombre préféré :</label>
      <select name="numbers" id="numbers" size="5" multiple>
        <option value="" disabled selected>Sélectionnez un nombre</option>
        <option value="one">1</option>
        <option value="two">2</option>
        <option value="three">3</option>
        <option value="four">4</option>
        <option value="five">5</option>
        <option value="six">6</option>
        <option value="seven">7</option>
        <option value="eight">8</option>
        <option value="nine">9</option>
        <option value="ten">10</option>
      </select>
</form>
```

L'élément `<option>` est contenu dans l'élément `<select>`. L'élément `<option>` contient les éléments à sélectionner. Chaque `<option>` représente un élément dans la liste déroulante.

Chaque élément `<option>` doit avoir un attribut `<value=" ">`, qui contient la valeur à soumettre lorsque le formulaire contenant l'élément `<select>` est soumis. Si l'attribut `<value=" ">` est omis, le contenu textuel de l'élément `<option>` devient la valeur à soumettre à la place.

L'attribut `<name=" ">` identifie le contrôle de sélection côté serveur lorsque le formulaire est soumis. Le `<name=" ">` est important pour le traitement des données du formulaire sur le serveur. 

Vous pouvez sélectionner l'une des options comme sélection par défaut en incluant l'attribut `<selected>` dans l'élément `<option>`. Si aucune option n'est sélectionnée, alors la première option de la liste sera sélectionnée par défaut.

L'attribut `<size=" ">` définit le nombre d'options que vous pouvez voir à la fois dans la liste déroulante en définissant l'attribut `<size=" ">` sur le `<select>`. Notez que les autres options sont visibles lorsque vous faites défiler vers le bas. 

L'inclusion de l'attribut `<disabled>` sur l'élément `<select>` désactive l'option de sélection et empêche les utilisateurs de sélectionner une option. L'option de sélection devient non cliquable. 

De plus, plusieurs options peuvent être sélectionnées en incluant l'attribut `<multiple>` sur l'élément `<select>`. Vous pouvez maintenir la touche `Ctrl` (ou Commande sur Mac) pour sélectionner plusieurs options.

Comprendre l'élément `<select>` et utiliser les attributs nécessaires peut rendre votre formulaire pratique pour que les utilisateurs sélectionnent différentes options et pour un traitement facile de l'élément `<select>` côté serveur.

## Validation de formulaire

En termes simples, il s'agit du processus de vérification si les données saisies dans le formulaire sont correctes, complètes et respectent le format spécifié.

### Importance de la validation de formulaire

* **Précision des données** : Empêche la soumission de données incorrectes ou incomplètes.
* **Sécurité** : Vérifie les données pour empêcher la soumission de données incorrectes ou malveillantes, réduisant ainsi les attaques nuisibles ou les violations de données. 
* **Expérience utilisateur** : Remplir les formulaires devient moins stressant grâce à un message d'erreur rapide si l'utilisateur saisit des données incorrectes. Il peut également être utilisé pour suggérer le format attendu. 
* **Efficacité** : La validation du formulaire avant la soumission permet d'économiser du temps et des ressources. Réduit les requêtes inutiles au serveur, améliorant ainsi les performances globales de votre application.

### Types de validation de formulaire

1. **Validation côté client** : Le navigateur de l'utilisateur effectue les vérifications avant la soumission. Comment le navigateur valide-t-il les formulaires ? Les navigateurs utilisent JavaScript, CSS ou des attributs HTML pour valider les formulaires. L'avantage de la validation côté client est le message d'erreur rapide que l'utilisateur reçoit lorsque les données sont incorrectes ou incomplètes. La réponse est rapide et ne nécessite pas de validation côté serveur. L'un des inconvénients est que la validation côté client peut être contournée par un utilisateur expérimenté. 
2. **Validation côté serveur** : Le serveur vérifie les données du formulaire après la soumission. La validation côté serveur est plus robuste et sécurisée. Elle effectue une double vérification et valide à nouveau les données du formulaire, même si la validation côté client échoue ou est contournée. La validation côté serveur est généralement effectuée en utilisant des langages de script comme PHP ou ASP.NET. 

Notez que vous pouvez utiliser l'un ou l'autre des deux ou une combinaison des deux.    

### Techniques de validation courantes

Ce sont des attributs HTML courants qui vous aident à décider du modèle de validation du formulaire.

#### Limites de longueur 

Vous pouvez utiliser l'attribut `maxlength` pour définir le nombre maximum de caractères qu'un champ de saisie peut contenir.

```html
<form>
  <input type="text" id="username" name="username" placeholder="Nom d'utilisateur" maxlength="20" required>
  <button type="submit">Soumettre</button>
</form>
```

#### Champs obligatoires 

Exige que certains champs de saisie soient remplis avant la soumission du formulaire. L'attribut `<required>` est utilisé pour effectuer cette technique. Un message d'erreur est affiché lorsque le champ obligatoire n'est pas rempli par l'utilisateur. 

```html
<form>
  <input type="text" id="username" name="username" placeholder="Nom d'utilisateur" required>
  <input type="email" id="email" name="email" placeholder="Email" required>
  <button type="submit">Soumettre</button>
</form>
```

#### Format de données 

Assure que les données saisies par l'utilisateur suivent le format requis. L'attribut de type `<input type="email">` défini sur email exigera que l'utilisateur entre le format d'email correct (par exemple : moi@example.com) avant la soumission du formulaire. 

La même chose se produit si l'attribut de type est défini sur number `<input type="number">`, l'utilisateur ne peut mettre que des données de 0-9.

```html
<form>
  <input type="email" id="email" name="email" placeholder="Email" required>
  <button type="submit">Soumettre</button>
</form>
```

#### Force du mot de passe 

L'attribut `<pattern="">` est utilisé pour spécifier la complexité du mot de passe, comme la longueur minimale, et l'inclusion de lettres majuscules ou minuscules, de chiffres et de caractères spéciaux. 

L'attribut `<title="">` affiche le message d'erreur lorsque l'utilisateur survole le champ de saisie ou lorsque le mot de passe saisi ne correspond pas au format de mot de passe spécifié. Plus la complexité du mot de passe est élevée, plus le compte utilisateur est protégé contre les accès non autorisés.

```html
<form>
  <input type="password" id="password" name="password" placeholder="Mot de passe" pattern="(?=.\d)(?=.[a-z])(?=.*[A-Z]).{8,}" title="Le mot de passe doit contenir au moins un chiffre, une lettre majuscule, une lettre minuscule et au moins 8 caractères ou plus" required>
  <button type="submit">Soumettre</button>
</form>
```

#### Valeurs numériques 

Vous pouvez définir la plage de valeurs numériques à entrer par l'utilisateur en utilisant les attributs `min` et `max`. Par exemple, pour vérifier si un utilisateur est dans la plage d'âge spécifiée :

```html
<form>
  <input type="number" id="age" name="age" placeholder="Âge" min="18" max="100" required>
  <button type="submit">Soumettre</button>
</form>
```

Avoir une bonne pratique de validation de formulaire aide à créer des formulaires avec des données précises et réduit la vulnérabilité aux attaques malveillantes. 

## Soumission de formulaire et méthodes

Lorsque le bouton de soumission est cliqué après avoir rempli un formulaire, vos informations sont envoyées au serveur pour traitement. Cela s'appelle la soumission de formulaire. 

### Méthodes de soumission de formulaire

Les données du formulaire sont envoyées au serveur en utilisant l'attribut `method`. Il existe deux méthodes couramment utilisées :

#### Méthode GET

Avec la méthode `get` `<method="get">`, les données du formulaire sont envoyées en utilisant l'URL dans la barre d'adresse du navigateur vers le serveur. 

```html
<form action="http://example.com" method="get">
          <input type="text" name="name" />
          <input type="submit" value="Soumettre" />
 </form>
```

En utilisant l'exemple de code ci-dessus, lorsque l'utilisateur entre un nom (disons que le nom de l'utilisateur est KC) dans le champ de saisie nommé ''name'', et clique sur le bouton de soumission, les données du formulaire seront envoyées au serveur dans l'URL comme ceci : "http://example.com?name=KC". 

La méthode GET n'est pas sécurisée, car elle est couramment utilisée pour envoyer de petites quantités de données qui ne sont pas sensibles.  

#### Méthode POST

L'attribut de méthode post `<method=post>` envoie les données du formulaire dans le corps de la requête HTTP au serveur, plutôt que dans l'URL.

```html
<form action="http://example.com" method="get">
          <input type="text" name="name" />
          <input type="submit" value="Soumettre" />
 </form>
```

En utilisant le même exemple de code ci-dessus, la méthode POST enverra les données du formulaire au serveur comme ceci : "https://example.com/submit.php". 

Vous devriez remarquer que la requête POST ne contient pas les données du formulaire dans l'URL mais pointe plutôt vers le script côté serveur (submit.php) qui traitera les données du formulaire. 

Les données du formulaire envoyées ne sont pas visibles. La requête POST est utilisée pour soumettre des informations sensibles, comme les mots de passe, puisque les données ne sont pas visibles dans l'URL, mais plutôt envoyées dans la requête HTTP body.

## Comment styliser les formulaires HTML

Les formulaires HTML peuvent être stylisés en utilisant CSS, comme tout autre élément HTML. Vous pouvez faire ce qui suit avec CSS pour correspondre au design de votre site web :

* **Sélecteurs** : Les sélecteurs CSS tels que les sélecteurs d'éléments, les sélecteurs de classe ou les sélecteurs d'ID peuvent être utilisés pour sélectionner des éléments spécifiques dans le code HTML pour le style.
* **Typographie** : La typographie peut être utilisée pour définir la famille de polices, ajuster la taille, le poids de la police et la couleur du texte dans l'élément de formulaire pour améliorer la lisibilité. 
* **Modèle de boîte** : Avec la connaissance des propriétés CSS comme le padding, la bordure et la marge, qui affectent l'espacement et la mise en page, vous pouvez styliser les éléments HTML.
* **Couleurs et arrière-plans** : La couleur de votre texte ou de l'arrière-plan peut être stylisée en utilisant les propriétés CSS comme la couleur et la couleur d'arrière-plan (ou l'image d'arrière-plan) respectivement. 
* **Réactivité** : Avec les requêtes média, vous pouvez rendre votre formulaire réactif et l'adapter à différentes tailles d'écran et appareils. 
* **Mise en page** : Vous pouvez contrôler la mise en page d'un formulaire pour le rendre convivial avec les propriétés CSS comme display, float et positionnement.

## Meilleures pratiques et accessibilité

Comme tout autre document HTML, assurez-vous que votre formulaire respecte les normes web et est accessible aux personnes handicapées. Pour les meilleures pratiques et l'accessibilité, prenez note de ce qui suit :

### Structures et sémantique

* Utilisez toujours des éléments HTML sémantiques appropriés (comme `<form>`, `<input>`, `<label>`, etc.) pour structurer non seulement les formulaires mais aussi tout autre document HTML.
* Imbriquez correctement les éléments et associez les labels à leurs champs de saisie respectifs. 
* Assurez-vous que vos champs de saisie ont les attributs de type appropriés.

### Gestion des erreurs et validation

* Combinez la validation côté client et côté serveur pour éviter la soumission de données incorrectes ou incomplètes.
* Utilisez l'attribut approprié pour afficher les messages d'erreur lorsque la soumission du formulaire échoue ou que des erreurs de validation se produisent. 

### Design réactif

* Vos formulaires doivent être réactifs et s'adapter à diverses tailles d'écran et appareils.
* Utilisez les requêtes média CSS pour ajuster les mises en page et les styles de vos formulaires en fonction de la taille de la fenêtre.

### Design et contraste

* Utilisez des polices et des couleurs faciles à voir.
* Le contraste de couleur entre le texte et l'arrière-plan doit assurer la lisibilité, surtout pour les utilisateurs ayant une vision réduite. 

### Rôles et attributs ARIA

* Les rôles et attributs ARIA (Accessible Rich Internet Application) améliorent l'accessibilité pour les utilisateurs de lecteurs d'écran ou d'autres technologies d'assistance.
* Les attributs ARIA (`aria-labelledby`, `aria-describedby`, et `aria-invalid`) fournissent un contexte et des commentaires supplémentaires pour les éléments de formulaire.

## Conclusion

Créer de bons formulaires HTML qui respectent les normes web améliore l'interaction et l'expérience utilisateur sur votre site web. En suivant les meilleures pratiques et l'accessibilité, les développeurs peuvent créer des formulaires conviviaux et efficaces pour collecter des données auprès des utilisateurs. 

Vous pouvez en apprendre davantage sur les formulaires HTML et le design web réactif en utilisant la [Certification en Design Web Réactif de freeCodeCamp](https://www.freecodecamp.org/learn/2022/responsive-web-design/)