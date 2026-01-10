---
title: Comment créer une boîte d'alerte JavaScript ou une fenêtre contextuelle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-25T19:20:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-javascript-alert-box-or-popup-window
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d8d740569d1a4ca385a.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment créer une boîte d'alerte JavaScript ou une fenêtre contextuelle
seo_desc: 'Popup boxes (or dialog boxes) are modal windows used to notify or warn
  the user, or to get input from the user.

  Popup boxes prevent the user from accessing other aspects of a program until the
  popup is closed, so they should not be overused.

  There ar...'
---

Les boîtes contextuelles (ou boîtes de dialogue) sont des fenêtres modales utilisées pour notifier ou avertir l'utilisateur, ou pour obtenir une entrée de l'utilisateur.

Les boîtes contextuelles empêchent l'utilisateur d'accéder à d'autres aspects d'un programme jusqu'à ce que la boîte contextuelle soit fermée, elles ne doivent donc pas être surutilisées.

Il existe trois types différents de méthodes de boîte contextuelle utilisées en JavaScript : [window.alert()](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert), [window.confirm()](https://developer.mozilla.org/en-US/docs/Web/API/Window/confirm) et [window.prompt()](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt).

### **Alerte**

La [méthode alert](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert) affiche des messages qui ne nécessitent pas que l'utilisateur entre une réponse. Une fois cette fonction appelée, une boîte de dialogue d'alerte apparaîtra avec le message (facultatif) spécifié. Les utilisateurs devront confirmer le message avant que l'alerte ne disparaisse.

### **Exemple :**

`window.alert("Bienvenue sur notre site web");`

![Exemple d'alerte MDN](https://mdn.mozillademos.org/files/130/AlertHelloWorld.png)

### **Confirmer**

La [méthode confirm](https://developer.mozilla.org/en-US/docs/Web/API/Window/confirm) est similaire à `window.alert()`, mais affiche également un bouton d'annulation dans la boîte contextuelle. Les boutons renvoient des valeurs booléennes : true pour OK et false pour Annuler.

### **Exemple :**

```javascript
var result = window.confirm('Êtes-vous sûr ?');
if (result === true) {
    window.alert('D'accord, si vous êtes sûr.');
} else { 
    window.alert('Vous semblez incertain.');
}
```

![Exemple de confirmation MDN](https://mdn.mozillademos.org/files/7163/firefoxcomfirmdialog_zpsf00ec381.png)

### **Invite**

La [méthode prompt](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt) est généralement utilisée pour obtenir une entrée de texte de l'utilisateur. Cette fonction peut prendre deux arguments, tous deux facultatifs : un message à afficher à l'utilisateur et une valeur par défaut à afficher dans le champ de texte.

### **Exemple :**

`var age = prompt('Quel âge avez-vous ?', '100');`

![Exemple d'invite MDN](https://mdn.mozillademos.org/files/11303/prompt.png)

### **Autres options de conception :**

Si vous n'êtes pas satisfait des boîtes contextuelles JavaScript par défaut, vous pouvez utiliser diverses bibliothèques d'interface utilisateur. Par exemple, SweetAlert offre un bon remplacement pour les modales JavaScript standard. Vous pouvez l'inclure dans votre HTML via un CDN (réseau de diffusion de contenu) et commencer à l'utiliser.

```html
<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
```

La syntaxe est la suivante : `swal(title, subtitle, messageType)`

```javascript
swal("Oups !", "Quelque chose s'est mal passé sur la page !", "error");
```

Le code ci-dessus produira la boîte contextuelle suivante :

![Exemple SweetAlert](https://ludu-assets.s3.amazonaws.com/lesson-content/rWqOoQXgDrSVSMrAKiZ9)

SweetAlert n'est en aucun cas le seul substitut aux modales standard, mais il est propre et facile à implémenter.

#### **Plus d'informations :**

* [MDN window.alert()](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert)
* [MDN window.confirm()](https://developer.mozilla.org/en-US/docs/Web/API/Window/confirm)
* [MDN window.prompt()](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt)