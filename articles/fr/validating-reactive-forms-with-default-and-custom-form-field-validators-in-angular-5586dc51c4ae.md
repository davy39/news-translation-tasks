---
title: Comment valider les formulaires réactifs par défaut et personnalisés dans Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-01T17:50:28.000Z'
originalURL: https://freecodecamp.org/news/validating-reactive-forms-with-default-and-custom-form-field-validators-in-angular-5586dc51c4ae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*I4kNKF1MI99L2iMqq0it-g.jpeg
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: Comment valider les formulaires réactifs par défaut et personnalisés dans
  Angular
seo_desc: 'By Luuk Gruijs

  When presenting forms to your users, it’s considered very user-friendly to give
  them immediate feedback on whether what they type is actually correct. Besides that,
  it could also limit the number of requests to the server. You would be...'
---

Par Luuk Gruijs

Lors de la présentation de formulaires à vos utilisateurs, il est considéré comme très convivial de leur donner un retour immédiat sur la validité de ce qu'ils saisissent. En outre, cela pourrait également limiter le nombre de requêtes envoyées au serveur. Vous pourriez ainsi intercepter 99 % des erreurs avant d'envoyer votre formulaire au serveur.

![Image](https://cdn-media-1.freecodecamp.org/images/qLQsIH1hq10Ki5q5JGFTidYla1fKkVsR67EZ)
_Photo par [Unsplash](https://unsplash.com/photos/twukN12EN7c?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Simon Matzinger</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Lors de l'utilisation de formulaires réactifs, Angular offre seulement une poignée de validateurs très génériques. Les validateurs de champs de formulaire par défaut sont :

* **min** : la valeur doit être supérieure à un certain nombre.
* **max** : la valeur doit être inférieure à un certain nombre.
* **required** : la valeur ne peut pas être vide.
* **requiredTrue** : la valeur doit être vraie.
* **email** : la valeur doit être une adresse email.
* **minLength** : la valeur doit contenir un nombre minimum de caractères.
* **maxLength** : la valeur doit contenir un nombre maximum de caractères.

Il est probable que les validateurs ci-dessus ne puissent pas répondre aux exigences de votre serveur. Par conséquent, vous ne pouvez pas donner à l'utilisateur le retour qu'il aimerait obtenir et l'aider à soumettre un formulaire correct. Pour cela, vous allez avoir besoin de validateurs de champs de formulaire personnalisés.

### Création d'un validateur de champ de formulaire personnalisé

Un validateur de champ de formulaire est une fonction qui prend votre contrôle de formulaire — le champ de saisie — et valide la valeur de ce contrôle de formulaire par rapport à une certaine condition. Cette fonction ne retourne rien lorsque tout est correct ou un objet indiquant ce qui n'a pas fonctionné.

Un cas d'utilisation très courant d'un validateur personnalisé est de vérifier si le formulaire correspond aux règles de sanitization du serveur. Cela signifie que le validateur vérifie si les caractères que votre utilisateur saisit dans votre formulaire sont autorisés. Créons ce validateur de formulaire maintenant.

### Construction du formulaire

Pour utiliser ce validateur, nous devons créer un formulaire et le définir là. À cette fin, nous allons créer un simple formulaire d'inscription utilisateur. Nous utilisons la méthode réactive pour créer le formulaire. Cela peut être fait comme suit :

Le template peut alors ressembler à ceci :

Nous avons maintenant un formulaire réactif fonctionnel. Cependant, nous n'avons appliqué aucune validation de formulaire. Pour ajouter une validation de formulaire, nous passons simplement nos validateurs dans la fonction de création de formulaire comme ceci :

Nous avons utilisé les validateurs required et email d'Angular. Nous avons également importé notre validateur personnalisé validateCharacters. La dernière chose que nous devons faire est de présenter les erreurs potentielles à nos utilisateurs.

### Présentation des erreurs à l'utilisateur

Il y a deux moments où nous voulons présenter les erreurs à nos utilisateurs : lorsque le focus passe d'un champ à l'autre et juste avant la soumission finale du formulaire.

Créons un service de formulaire pour cela. Ce service pourrait potentiellement ressembler à ceci :

La méthode `validateForm` accepte le formulaire à valider, un objet d'erreurs de formulaire et un booléen indiquant s'il faut vérifier les champs modifiés ou non. La fonction parcourt ensuite tous les contrôles de formulaire et vérifie s'il y a des erreurs sur ce contrôle. Si c'est le cas, nous trouvons le message d'erreur correct qui provient de la méthode `validationMessages` et renvoyons l'objet d'erreurs de formulaire.

Pour utiliser ce service d'erreurs dans nos composants, nous devons faire ce qui suit :

Maintenant, la dernière étape consiste à afficher les messages d'erreur dans notre template. Nous pouvons le faire comme ceci :

Si des erreurs apparaissent sur un champ particulier, nous affichons le message qui se trouve dans l'objet `formErrors`. Ci-dessous se trouve une démonstration complète. Jouez avec les champs. Essayez de remplir des caractères comme `!#$^` dans le champ de nom et voyez si notre validateur de formulaire personnalisé fonctionne. Si aucune erreur n'apparaît, cliquez sur le bouton d'inscription et voyez le message de succès.

### Conclusion

J'espère que cet article vous aide à valider vos formulaires et à offrir une meilleure expérience à vos utilisateurs lorsqu'ils remplissent les formulaires.

#### Vous cherchez un emploi à Amsterdam ?

Je travaille pour **Sytac** en tant que développeur front-end senior. Nous recherchons des développeurs mid/senior spécialisés dans Angular, React, Java ou Scala. Sytac est une société de conseil très ambitieuse aux Pays-Bas.

Si vous pensez avoir ce qu'il faut pour travailler avec les meilleurs, envoyez-moi un email à [luuk.gruijs@sytac.io](mailto:luuk.gruijs@sytac.io) et je serai ravi de vous en dire plus.