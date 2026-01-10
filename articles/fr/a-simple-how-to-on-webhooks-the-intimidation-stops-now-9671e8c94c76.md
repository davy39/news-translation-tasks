---
title: 'Un guide simple sur les Webhooks : la peur s''arrête maintenant'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-22T15:27:09.000Z'
originalURL: https://freecodecamp.org/news/a-simple-how-to-on-webhooks-the-intimidation-stops-now-9671e8c94c76
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QNB36W_y-FapMFqIPm7ldw.png
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Un guide simple sur les Webhooks : la peur s''arrête maintenant'
seo_desc: 'By Jared Wolff

  Webhook.

  It sounds like what happens when you cross a spider and a pirate. In the world of
  the internet though, webhooks are something completely different. Webhooks help
  connect services together.

  Let me explain.

  Say we have two hypot...'
---

Par Jared Wolff

Webhook.

Cela ressemble à ce qui se passe lorsque vous croisez une araignée et un pirate. Dans le monde de l'internet, cependant, les webhooks sont quelque chose de complètement différent. Les webhooks aident à connecter les services ensemble.

Permettez-moi d'expliquer.

Imaginons que nous avons deux services hypothétiques. L'un est un service qui génère des données, et l'autre qui collecte et organise ces données.

Les développeurs du premier service ont pensé : « Bon, notre plateforme n'est utile que jusqu'à un certain point. Donnons aux utilisateurs la possibilité de transmettre des données en temps réel à d'autres services. »

Les développeurs du second service ont pensé : « Oh là là, ce serait super si nos utilisateurs pouvaient importer des données plus facilement. » Ils ont donc ajouté des webhooks pour recevoir des données en temps réel depuis un service comme le premier.

Maintenant, en tant qu'utilisateur, vous utilisez les deux services. Vous avez maintenant le pouvoir de les connecter ensemble.

La meilleure façon de l'expliquer est avec un exemple concret.

![Image](https://cdn-media-1.freecodecamp.org/images/neTkch0k1ePK9-yoALIKhtl1iPY4UXv1Ifjp)
_Êtes-vous prêt ?_

### Exemple concret

Dans un [projet récent](https://www.jaredwolff.com/homemade-indoor-air-quality-sensor/), j'ai connecté un capteur IoT à une feuille Google Docs. Cela ne m'a pris que 10 minutes environ. Je vais vous montrer comment faire la même chose maintenant.

#### Commençons d'abord par configurer la feuille Google.

* Créez une nouvelle feuille

![Image](https://cdn-media-1.freecodecamp.org/images/Zvel9b1dtdfuIcP3xQAREREdqnbbxQtBxHLL)
_Créez une nouvelle feuille._

* Une fois là-bas, allez dans **Outils** et cliquez sur **Éditeur de script**

![Image](https://cdn-media-1.freecodecamp.org/images/3hAZkBZ7FcMHNSyAkqjPKCV1OFW6wnN5HOyS)
_Créez un nouveau script basé sur la feuille._

* Une nouvelle fenêtre devrait s'ouvrir, qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/eA7rAwDdGcK3uM6pIdhCXM935Cr9c4cSaXR3)
_Nouvel écran de script._

* Copiez et collez ce code. Je vais l'expliquer après.

```
// ceci est une fonction qui se déclenche lorsque l'application web reçoit une requête POST
function doPost(e) {
    // Retourne si null
    if( e == undefined ) {
        console.log("pas de données");
        return HtmlService.createHtmlOutput("besoin de données");
    }
    // Analyse les données JSON
    var event = JSON.parse(e.postData.contents);
    var data = event.data;
```

```
// Obtient la dernière ligne sans données
var sheet = SpreadsheetApp.getActiveSheet();
var lastRow = Math.max(sheet.getLastRow(),1);
sheet.insertRowAfter(lastRow);
    // Obtient l'horodatage actuel
    var timestamp = new Date();
    // Insère les données dans la feuille
    sheet.getRange(lastRow + 1, 1).setValue(event.published_at);
    sheet.getRange(lastRow + 1, 2).setValue(data.temperature);
    sheet.getRange(lastRow + 1, 3).setValue(data.humidity);
    sheet.getRange(lastRow + 1, 4).setValue(data.pm10);
    sheet.getRange(lastRow + 1, 5).setValue(data.pm25);
    sheet.getRange(lastRow + 1, 6).setValue(data.tvoc);
    sheet.getRange(lastRow + 1, 7).setValue(data.c02);
    SpreadsheetApp.flush();
    return HtmlService.createHtmlOutput("requête post reçue");
}
```

Maintenant, comprenons tout cela.

```
function doPost(e) {
```

C'est la fonction qui est appelée lors d'un événement POST. Considérez ce script comme un serveur web. Nous lui envoyons des données à une adresse spécifique (que nous aurons dans un instant).

**e** est l'objet de l'appel HTTP. Il contiendra les données que nous lui envoyons. Il est donc bon de vérifier s'il est **NULL**. Si c'est le cas, il n'est pas nécessaire d'exécuter le script.

Si nous avons des données valides, transformons-les d'une chaîne en JSON utilisable. Vous pouvez utiliser la fonction préférée de tous, `JSON.parse`, pour ce faire.

```
var event = JSON.parse(e.postData.contents);
```

Rappelez-vous, la structure des données déterminera comment vous les traitez ! Vous devrez peut-être exécuter `JSON.parse` plusieurs fois selon le niveau d'imbrication de vos données et leur format.

Une fois que vous avez vos données, il est temps de les mettre au bon endroit !

```
// Obtient la dernière ligne sans données
var sheet = SpreadsheetApp.getActiveSheet();
var lastRow = Math.max(sheet.getLastRow(),1);
sheet.insertRowAfter(lastRow);
```

Ces trois appels vous amèneront à la première ligne disponible à partir de la ligne 1 (en laissant la ligne 0 pour les étiquettes de colonne).

Enfin, nous mettons les données dans la ligne qui leur appartient :

```
sheet.getRange(lastRow + 1, 1).setValue(event.published_at);
```

Où le premier paramètre de `sheet.getRange` est la ligne et le second est la colonne. Vous pouvez utiliser la fonction `setValue` pour définir ce que vous voulez dans cette cellule particulière.

Au fait, l'inspiration pour ce code vient de [cet article](https://blog.runscope.com/posts/tutorial-capturing-webhooks-with-google-sheets).

Super. Donc nous avons un script. Comment l'appeler ?

![Image](https://cdn-media-1.freecodecamp.org/images/xmlYv8J8o8Seprjfok6kRtE9mEeZS3GdYpmX)
_Pourquoi je ne peux rien faire tout de suite._

* Cliquez sur ce bouton **Publier**

![Image](https://cdn-media-1.freecodecamp.org/images/f7hbT1FSsO7xFFFSOdw2sTPXuCGI7YFUnELw)
_Cliquez sur le bouton « Publier »._

* Cliquez sur `Déployer en tant qu'application web`

![Image](https://cdn-media-1.freecodecamp.org/images/gvRCAP7JBc3Ov8AlE1Uv3ndchKK5LjcDr85S)
_Cliquez sur ce lien « Déployer en tant qu'application web » !_

* Modifiez les paramètres pour qu'ils correspondent à la capture d'écran ci-dessous. Ensuite, cliquez sur `Déployer`

![Image](https://cdn-media-1.freecodecamp.org/images/LTXLSZqj14WMm0V9rpyV62csz6YQ2m2qaleT)
_N'importe qui peut avoir accès pour simplifier. Pour d'autres cas d'utilisation, les connexions sont recommandées._

* Vous pouvez obtenir un écran vous demandant de mettre à jour vos permissions. Cliquez sur `Examiner les permissions`

![Image](https://cdn-media-1.freecodecamp.org/images/GjeBOC97Gcp579KijLCau3MSdzF0XvVDpIRW)
_Vous devrez autoriser l'application à utiliser votre compte pour modifier la feuille Google._

* Cliquez sur `Avancé`, puis cliquez sur `Aller à <Nom de votre fichier>` en bas à gauche.

![Image](https://cdn-media-1.freecodecamp.org/images/dXKx4QtvjijriJz8sLhBJcJBxXHZocHwJ1Rh)
_Avertissement de sécurité. Pas de soucis._

* Enfin, cliquez sur `Autoriser`

![Image](https://cdn-media-1.freecodecamp.org/images/XjQpS2dsfjH34y9PgLRBIryQvf57HkZJR-xS)
_Ceci est un mécanisme de sécurité pour Google. Puisque c'est votre application, c'est bon !_

* Dans le dernier écran, copiez votre URL de Webhook !

![Image](https://cdn-media-1.freecodecamp.org/images/OZBuLa8p0qkal7hy3DX5KhfL-5gMiQXOH0jD)
_Cette URL ne change pas, même lorsque vous publiez une « nouvelle version »._

### Testons-le

Maintenant, nous pouvons tester si tout fonctionne en utilisant Postman. Si vous n'avez pas encore utilisé Postman, c'est une interface utilisateur graphique pour `curl`.

* [Installez Postman.](https://www.getpostman.com/downloads/) Vous aurez peut-être besoin d'un compte pour aller plus loin.
* Une fois à l'intérieur, créez une nouvelle requête. Nommez-la pour que vous sachiez qu'elle appartient à ce webhook Google Docs.

![Image](https://cdn-media-1.freecodecamp.org/images/SMjDT0WyXxmyAB9AE3XlAptskaJF4RQkX6aG)
_Deux étapes très importantes. Si l'une d'entre elles est incorrecte, vous ne recevrez aucune entrée._

* Cliquez sur `body` et entrez le code de test suivant :

```
{
    "event": "gdxg",
    "data": {
        "temperature": 21
    },
    "coreid": "zczxvz",
    "published_at": "zcvzxcvx"
}
```

* Enfin, cliquez sur ce bouton bleu `Envoyer`.

![Image](https://cdn-media-1.freecodecamp.org/images/KDjc6l3qfgCOXFx1EnawJgCa3sYVAklQSaNJ)
_Ceci est des données bidon pour le test uniquement._

* Retournez à votre feuille Excel et voyez la magie !

![Image](https://cdn-media-1.freecodecamp.org/images/vSeMTe75LnIFgtwa8bsQ6gA6hS9IyD-hlwjs)
_Notez que les en-têtes sont ajoutés pour que nous sachions ce que sont les données !_

Maintenant, nous cuisinons au gaz !

![Image](https://cdn-media-1.freecodecamp.org/images/gmvzAcpsHrsdiNdvQ0zZoxukiVAlvBqAHY1z)
_M. Scary Gas Bunny Man_

### Conclusion

J'espère que vous avez réussi à faire fonctionner l'exemple ci-dessus. Heureusement pour vous, il y a beaucoup moins de choses à craindre une fois que vous avez cette partie en place et en fonctionnement !

Pour résumer, nous avons parlé des webhooks et de leur utilité. Vous devriez vous sentir confiant à ce stade pour aller configurer les vôtres. Si vous vous sentez toujours intimidé, je recommande d'utiliser des services comme Zapier ou IFTTT. (Ce sont des interfaces brillantes pour les API et les Webhooks déjà disponibles.)

Enfin, [consultez l'article complet](https://www.jaredwolff.com/homemade-indoor-air-quality-sensor/) où j'intègre le matériel et le web dans un projet génial.

Bon webhooking !