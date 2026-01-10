---
title: 'Tutoriel AJAX : Qu''est-ce que l''AJAX et comment l''utiliser'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-22T17:37:00.000Z'
originalURL: https://freecodecamp.org/news/ajax-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c72740569d1a4ca3245.jpg
tags:
- name: Ajax
  slug: ajax
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: 'Tutoriel AJAX : Qu''est-ce que l''AJAX et comment l''utiliser'
seo_desc: 'What is AJAX?

  AJAX stands for Asynchronous JavaScript And XML. It is not a programming language.
  It is a technology for developing better, faster and interactive Web Applications
  using HTML, CSS, JavaScript and XML.


  HTML : Hypertext Markup Language ...'
---

## **Qu'est-ce que l'AJAX ?**

**AJAX** signifie **Asynchronous JavaScript And XML**. Ce n'est pas un langage de programmation. C'est une technologie pour développer de meilleures applications Web, plus rapides et interactives, en utilisant HTML, CSS, JavaScript et XML.

1. HTML : Hypertext Markup Language (HTML) est utilisé pour définir la structure d'une application Web.
2. CSS : Cascading Style Sheet (CSS) est utilisé pour fournir l'apparence et le style à une application Web.
3. JavaScript : JavaScript est utilisé pour rendre une application Web interactive, intéressante et conviviale.
4. XML : Extensible Markup Language (XML) est un format pour stocker et transporter des données depuis le serveur Web.

### Que signifie Asynchrone dans AJAX ?

Asynchrone signifie que l'application Web peut envoyer et recevoir des données du serveur Web sans rafraîchir la page. Ce processus en arrière-plan d'envoi et de réception de données depuis le serveur, ainsi que la mise à jour de différentes sections d'une page Web, définit la propriété/caractéristique asynchrone de l'AJAX.

## Comment fonctionne AJAX

AJAX utilise un objet intégré au navigateur **XMLHttpRequest** pour demander des données à un serveur Web et **HTML DOM** pour afficher ou utiliser les données.

**Objet XMLHttpRequest** : Il s'agit d'une API sous forme d'objet dont les méthodes aident au transfert de données entre un navigateur Web et un serveur Web.

**HTML DOM** : Lorsqu'une page Web est chargée, le navigateur crée un Document Object Model de la page.

![Image](https://i.imgur.com/pfC7QFH.png)

**Créer un objet XMLHttpRequest :**

```javascript
var xhttp = new XMLHttpRequest();
```

**Propriétés de l'objet XMLHttpRequest :**

`readyState` est une propriété de l'objet XMLHttpRequest qui contient le statut de la requête XMLHttpRequest.

* 0 : requête non initialisée
* 1 : connexion au serveur établie
* 2 : requête reçue
* 3 : traitement de la requête
* 4 : requête terminée et réponse prête

`onreadystatechange` est une propriété de l'objet XMLHttpRequest qui définit une fonction à appeler lorsque la propriété readyState change.

`status` est une propriété de l'objet XMLHttpRequest qui retourne le numéro de statut d'une requête

* 200 : "OK"
* 403 : "Forbidden"
* 404 : "Not Found"

**Méthodes de l'objet XMLHttpRequest :** Pour envoyer une requête à un serveur Web, nous utilisons les méthodes open() et send() de l'objet XMLHttpRequest.

```javascript
xhttp.open("GET", "content.txt", true);
xhttp.send();
```

**Créer une fonction changeContent() en utilisant JavaScript :**

```javascript
function changeContent() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("foo").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "content.txt", true);
xhttp.send();
}
```

**Exemple AJAX pour changer le contenu d'une page Web :**

```html
<!DOCTYPE html>
<html>
<body>

<div id="foo">
<h2>L'objet XMLHttpRequest</h2>
<button type="button" onclick="changeContent()">Changer le contenu</button>
</div>

<script>
function changeContent() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("foo").innerHTML =
      this.responseText;
    }
  };
  xhttp.open("GET", "content.txt", true);
  xhttp.send();
}
</script>

</body>
</html>
```

Le fichier `content.txt` doit être présent dans le répertoire racine de l'application Web.