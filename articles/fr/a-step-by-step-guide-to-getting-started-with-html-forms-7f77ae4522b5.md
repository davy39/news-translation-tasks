---
title: Un guide étape par étape pour commencer avec les formulaires HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-13T23:55:42.000Z'
originalURL: https://freecodecamp.org/news/a-step-by-step-guide-to-getting-started-with-html-forms-7f77ae4522b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7dd2MZ78ekF3bA3N0Jlvmw.gif
tags:
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Un guide étape par étape pour commencer avec les formulaires HTML
seo_desc: 'By Abhishek Jakhar

  Overview

  HTML forms are required when you want to collect some data from the person who visits
  your website. For example, when you register/login for applications like Uber, Netflix,
  or Facebook, you enter information like Name, Em...'
---

Par Abhishek Jakhar

#### Aperçu

Les formulaires HTML sont nécessaires lorsque vous souhaitez collecter des données auprès de la personne qui visite votre site web. Par exemple, lorsque vous vous inscrivez ou vous connectez à des applications comme Uber, Netflix ou Facebook, vous entrez des informations comme le **Nom**, **Email** et **Mot de passe** via des formulaires HTML.

Maintenant, nous allons apprendre tous les éléments nécessaires pour créer un formulaire.

> **NOTE :** J'ai déjà ajouté le style en utilisant CSS et donc mes éléments auront une apparence différente, mais ils fonctionneront exactement de la même manière.  
> Si vous souhaitez que vos éléments ressemblent aux miens, vous pouvez trouver mon fichier CSS dans les liens donnés ci-dessous :  
> CSS personnalisé : [https://gist.github.com/abhishekjakhar/493d920a219ed9d88f1846cd31de7751](https://gist.github.com/abhishekjakhar/493d920a219ed9d88f1846cd31de7751)  
> Normalize CSS :  
> [https://gist.github.com/abhishekjakhar/3a6c25fa61a293b6a56d28f98497808b](https://gist.github.com/abhishekjakhar/3a6c25fa61a293b6a56d28f98497808b)

#### Élément Form

C'est le premier élément que nous allons apprendre. Cet élément enveloppe tous les autres éléments qui vont à l'intérieur de notre formulaire. C'est l'élément form.

Notre formulaire ne soumettra pas les données quelque part car il n'est pas connecté à un serveur. Pour connecter notre formulaire à un serveur et traiter nos données, nous pouvons utiliser n'importe quel langage côté serveur comme Node, Python, Ruby ou PHP. La partie de traitement des données implique deux attributs importants qui sont attachés à l'élément form. Examinons ces attributs.

**Attributs :**

1. **action :** L'attribut action est l'adresse web (URL) d'un programme qui traite les informations soumises par notre formulaire.
2. **method :** C'est la [méthode HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) que le navigateur utilise pour soumettre le formulaire, les valeurs possibles sont **POST** et **GET.**

* **POST** — Les données du corps du formulaire sont envoyées au serveur.
* **GET** — Les données sont envoyées à l'intérieur de l'URL et les paramètres sont séparés par un point d'interrogation.

> **Note :** Vous ne pouvez pas avoir de **formulaires** imbriqués **à l'intérieur d'un autre formulaire**. Cela signifie que vous ne pouvez pas avoir un élément <form> à l'intérieur d'un autre élément <form>.

#### Élément Input

L'élément input est l'élément de formulaire le plus couramment utilisé. Il est utilisé pour créer un **champ de texte** où l'utilisateur peut taper certaines **informations**, par exemple **email**, **mot de passe**, etc.

Créons un champ de texte où l'utilisateur peut taper son nom.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pGZFUO5zQ1_QquSAcECo_Q.gif)

> **Note :** L'élément input est une balise auto-fermante, donc il n'est pas nécessaire de taper une balise de fermeture pour correspondre à la balise d'ouverture.

J'ai ajouté trois attributs dans la balise input ci-dessus. Examinons chacun d'eux en détail.

**type**

L'attribut **type** indique quel type d'entrée nous voulons. Si nous donnons une valeur de **text** à l'attribut **type**, cela signifie que la valeur que nous entrons dans le champ de saisie est de type texte. Il existe de nombreuses valeurs possibles pour cet attribut particulier. Certaines valeurs possibles sont email, tel pour téléphone et password, etc.

Exemple : Lorsque vous vous connectez à l'un de vos comptes (Amazon/Netflix), vous devez entrer deux choses : **email** et **mot de passe**. Dans ce cas particulier, l'élément **input** est utilisé. L'attribut **type** est donné avec la valeur **email** et **password** respectivement.

**id**

L'attribut ID n'est pas obligatoire, mais c'est une bonne idée d'en ajouter un. Dans certains cas, cela est utile pour cibler des éléments avec CSS/JavaScript. L'attribut ID est ajouté afin que nous puissions associer des **labels** à des **contrôles de formulaire spécifiques**.

**name**

L'attribut name est nécessaire. Lorsque le formulaire est soumis au code côté serveur, le serveur peut comprendre les données du formulaire et traiter les valeurs de manière appropriée.

**placeholder**

C'est un court indice qui est affiché dans le champ de saisie avant que l'utilisateur ne saisisse une valeur. Lorsque l'utilisateur commence à taper dans le champ de saisie, le placeholder disparaît.

Voyons à quoi ressemblent quelques autres éléments d'entrée de base.

> **Note :** L'utilisation de **différentes valeurs** pour l'attribut **type** produira des résultats différents. Par exemple, vous pouvez faire en sorte que l'entrée soit de type email, texte ou mot de passe, etc. Tous montrent un **comportement légèrement différent**, que vous verrez ci-dessous.

Plusieurs éléments d'entrée (Texte, Email, Mot de passe)

Plusieurs éléments d'entrée (Texte, Email, Mot de passe)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UgNfHeAhkl-GQ0btgglbXA.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*I5AeYrtMwoAi-UtAxdPw9g.gif)
_Éléments **Input** sans **placeholder** (à gauche) et avec l'attribut **placeholder** (à droite)_

#### Élément Textarea

Parfois, une seule ligne de texte ne suffit pas et un simple élément d'entrée ne fonctionnera pas. Par exemple, certains sites web ont un formulaire de contact pour que les gens tapent leurs questions ou messages. Dans ces cas, il est préférable d'utiliser l'élément `textarea`.

L'élément **<textarea>** n'est pas une balise auto-fermante, donc nous devons taper à la fois la balise d'ouverture et la balise de fermeture. (<textarea></textarea>)

**Attributs :**

* **id :** Identique à celui mentionné ci-dessus dans l'élément <input/>.
* **name :** Identique à celui mentionné ci-dessus dans l'élément <input/>.
* **cols :** Spécifie la largeur visible d'une zone de texte.
* **rows :** Spécifie le nombre visible de lignes dans une zone de texte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_k2gP5oTjbllKQtpDBfaAA.gif)
_Élément Textarea_

Vous pouvez voir que la textarea nous permet de taper sur plusieurs lignes. Une textarea est redimensionnable par l'utilisateur, vous pouvez voir dans l'illustration ci-dessus que je redimensionne la textarea.

> **Note :** Dans la plupart des navigateurs, l'élément **textarea** est redimensionnable.

#### Élément Button

L'élément button est l'un des éléments de formulaire les plus importants. Sans un bouton, vous ne pouvez pas soumettre de formulaire au serveur pour traitement.

L'élément button accepte l'attribut appelé **type**. Cet attribut accepte trois valeurs : **submit**, **reset** et **button**.

**Attributs :**

* **type**="reset" : Il **effacera** **toutes les données du formulaire** lorsqu'il est cliqué.
* **type**="button" : Il n'a aucun comportement par défaut et est principalement utilisé avec JavaScript pour le programmer pour un **comportement personnalisé**.
* **type**="submit" : Le comportement par défaut du **type submit** est, comme son nom l'indique, de soumettre le formulaire et d'envoyer toutes les données au serveur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*j8Pb34UJc8luxp_yUHBmRA.gif)
_Bouton de type submit_

#### Élément Label

Pour l'instant, il est impossible pour l'utilisateur de savoir quel contrôle de formulaire fait quoi. Il n'y a aucun moyen de savoir où vous allez entrer l'email et où vous allez entrer le mot de passe. Le formulaire semble très incomplet et désordonné.

Nous pouvons étiqueter chacun de nos contrôles de formulaire en utilisant l'élément label.

L'attribut le plus utilisé avec un **label** est **for**.

**Attributs :**

* **for :** L'attribut **for** associe le label à un élément de formulaire particulier. La manière dont il **correspond est par ID**. Comme vous pouvez le voir dans l'exemple ci-dessus, la **valeur de l'attribut ID** donnée à l'élément input est **email**. La valeur de l'attribut **for** donnée à l'élément label est également **email**, donc ils sont associés l'un à l'autre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ksf3FWyd6KOa4QIak8mSfA.gif)

> **Note :** Lorsque nous cliquons sur le label, nous obtenons automatiquement le focus sur le champ de saisie qui est associé au label. C'est un comportement par défaut.

Maintenant, notre formulaire a l'air très bien 😊.

#### Menus Sélection

Parfois, lorsque vous créez un formulaire, vous ne voulez pas que l'utilisateur puisse taper du texte. Plutôt, vous voulez peut-être qu'il choisisse parmi **certaines options prédéfinies que vous fournissez**.

Chaque fois que vous avez une liste d'options qui est plus longue que, disons, quatre ou cinq choses, il est préférable d'opter pour le menu de sélection car il économise de l'espace.

Supposons que notre formulaire est destiné aux étudiants qui vont demander une admission à une université. Nous voulons permettre aux étudiants de sélectionner parmi une liste prédéfinie de programmes universitaires.

L'élément de menu de sélection est créé en utilisant les balises d'ouverture et de fermeture **<select>**.

**<select>** — L'élément select **rend un menu déroulant** qui contient des options sélectionnables**. L'**élément select ne fera rien, par lui-même. Cet élément de formulaire a en fait besoin d'éléments supplémentaires à l'intérieur, exactement **comme** les éléments <ul> ont besoin d'éléments <li>. Les éléments **que nous mettons** à l'intérieur de l'élément select sont appelés éléments option.

**Attributs :**

* **name :** Identique à celui mentionné ci-dessus dans l'élément <input/>.

**<option>** — L'élément option représente l'un des choix qu'un utilisateur peut choisir dans un menu de sélection**. L'**élément <option> utilise un attribut appelé value.

**Attributs :**

* **value :** Lorsque vous soumettez un formulaire au code côté serveur, chaque élément de formulaire a une valeur associée pour les entrées de texte et les zones de texte. Cette valeur est ce que l'utilisateur tape dans le champ. Cependant, puisque nous créons ces options prédéfinies, nous devons spécifier à quoi la valeur doit ressembler lorsqu'elle est soumise. Donc, nous utilisons l'attribut **value** pour spécifier les valeurs des options prédéfinies.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EkXaeFfKPsK1lbiDAeQvyg.gif)
_Menu Sélection_

Maintenant, nous avons l'étiquette Sélectionner des Cours avec le menu de sélection que nous venons de créer. Maintenant, nous pouvons également organiser notre liste en groupes logiques avec l'élément **<optgroup>**.

**Attributs :**

* **label :** Le nom du groupe d'options. Dans l'exemple donné ci-dessous, notre liste d'options a été divisée en deux groupes avec l'étiquette Ingénierie et Gestion.

Dans l'exemple donné ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/1*GHsseV7OitD9m9mTjHb8BA.gif)

#### Boutons Radio

Les menus de sélection sont excellents si vous avez beaucoup d'options. Si vous avez quelque chose comme 5 options ou moins, il est préférable d'utiliser des boutons radio.

La différence entre le Menu Sélection et le Bouton Radio est que les boutons radio vous montrent toutes les options à la fois. Comme le menu de sélection, l'utilisateur ne peut en choisir qu'une seule.

**Attributs :**

* **name :** Identique à celui mentionné ci-dessus dans l'élément <input/>.
* **value :** Puisque nous créons ces options prédéfinies, nous devons spécifier à quoi la valeur doit ressembler lorsqu'elle est soumise. Donc, nous utilisons l'attribut **value** pour spécifier les valeurs des options prédéfinies.

> **_Note:_** _Si vous sélectionnez une option et que vous essayez ensuite de sélectionner une autre option, vous verrez qu'elle désélectionne l'option précédente. La manière dont il sait faire cela est parce que nous avons l'attribut **name** exactement identique. Donc, il sait que ces deux boutons radio font partie du même groupe._

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jxp4WvykcA7siX0SG2P2CQ.gif)

> **Note :** Le nom doit être le même si nous voulons que les boutons radio fassent partie du même groupe de boutons radio.

#### Cases à cocher

Parfois, vous avez peut-être un groupe d'options prédéfinies. Vous voulez que l'utilisateur puisse sélectionner plusieurs options et pas seulement une d'entre elles. C'est là que les cases à cocher sont utiles.

**Attributs :**

* **name :** Identique à celui mentionné ci-dessus dans l'élément <input/>.
* **value :** Puisque nous créons ces options prédéfinies, nous devons spécifier à quoi la valeur doit ressembler lorsqu'elle est soumise. Donc, nous utilisons l'attribut **value** pour spécifier les valeurs des options prédéfinies.
* **checked :** Par défaut, une case à cocher est décochée. Vous pouvez définir l'état par défaut à coché en utilisant l'attribut appelé **checked**. N'oubliez pas que c'est un attribut booléen.

```
<input type="checkbox" checked id="name" value="abhishek" name="user_name" />
```

Dans l'exemple donné ci-dessous, j'ai utilisé le label pour chaque option individuelle. J'ai connecté la **case à cocher** et un **label** en utilisant l'attribut **for** du **label** et l'attribut **id** de la **case à cocher**.

> **_Note:_** _Il peut être difficile de cliquer sur une petite case à cocher. Il est recommandé d'envelopper un élément <label> autour de la case à cocher. Si nous cliquons sur le label, notre case à cocher se coche ou se décoche également. Je ne l'ai pas fait ci-dessous, mais vous pouvez le faire pour améliorer l'UX._

![Image](https://cdn-media-1.freecodecamp.org/images/1*SFY1wuzU-95_FqsrkfuFMw.gif)

#### Différence entre Case à cocher et Bouton radio

1. La case à cocher peut exister **seule**, tandis que les boutons radio ne peuvent apparaître que comme un **groupe** (au minimum 2 boutons radio doivent être présents).
2. La sélection de la case à cocher est **optionnelle**, mais le choix de l'un des boutons radio est **obligatoire**.

#### Le Formulaire Complet

![Image](https://cdn-media-1.freecodecamp.org/images/1*BWh2qjSRTuAa6ixPGsKcrg.png)

Nous avons appris beaucoup d'éléments de formulaire HTML et avons couvert les essentiels.

Ne vous inquiétez pas de tout mémoriser. Presque aucun développeur web professionnel ne peut nommer chaque attribut ou élément. Ce qui est plus important que la mémorisation, c'est d'apprendre à chercher des choses dans la documentation lorsque vous en avez besoin.

Vous pouvez essayer d'ajouter votre propre CSS pour faire en sorte que ce formulaire ait l'apparence que vous souhaitez.

Vous pouvez en apprendre plus sur les formulaires dans le lien donné ci-dessous

[**Formulaires HTML**](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms)  
[_Ce module fournit une série d'articles qui vous aideront à maîtriser les formulaires HTML. Les formulaires HTML sont un outil très puissant pour..._developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms)

J'espère que vous avez trouvé cet article informatif et utile. J'adorerais avoir votre retour !

**Merci d'avoir lu !**