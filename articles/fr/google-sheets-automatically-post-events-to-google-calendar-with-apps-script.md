---
title: Google Sheets – Comment publier automatiquement des événements sur Google Calendar
  avec Apps Script
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-05-24T21:44:39.000Z'
originalURL: https://freecodecamp.org/news/google-sheets-automatically-post-events-to-google-calendar-with-apps-script
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Sheets-to-Calendar3.jpg
tags:
- name: google apps script
  slug: google-apps-script
- name: google sheets
  slug: google-sheets
seo_title: Google Sheets – Comment publier automatiquement des événements sur Google
  Calendar avec Apps Script
seo_desc: 'In this article we''ll link two Google services -> Google Sheets and Google
  Calendar.

  By using a very short custom function in Google Apps Script, we can add a list of
  events from a Google Sheet to a Google Calendar. 🤯

  And we''ll even have it email ou...'
---

Dans cet article, nous allons lier deux services Google -> Google Sheets et Google Calendar.

En utilisant une fonction personnalisée très courte dans Google Apps Script, nous pouvons ajouter une liste d'événements depuis une feuille Google Sheet à un Google Calendar. 🤏

Et nous allons même envoyer un email à nos invités. 🔥

Voici la vidéo d'accompagnement de l'article :

%[https://youtu.be/FxxPq2wXcK4]

## Configuration de Google Sheets

Notre feuille est assez simple. Nous avons des noms d'événements, des dates, des heures de début, des heures de fin et des emails d'invités.

La seule chose curieuse est le formatage de nos dates et heures - je vais couvrir cela au fur et à mesure, mais vous pouvez voir que les colonnes B et C répètent les informations des colonnes D, E et F...

![Capture d'écran des informations d'événement dans Google Sheet](https://www.freecodecamp.org/news/content/images/2024/03/1684886378577.png)

Google Calendar doit recevoir les heures de début et de fin sous la forme d'un objet date/heure complet. Mais dans Google Sheet, il n'y a pas de moyen facile de créer une validation de données de liste déroulante pour que les utilisateurs sélectionnent un objet date/heure.

Dans la colonne D, j'ai mis une validation de données pour sélectionner une date valide.

![Capture d'écran de la validation de données pour une date valide](https://www.freecodecamp.org/news/content/images/2024/03/1684886609169.png)

Et dans les colonnes E et F, j'ai créé une liste déroulante d'heures valides.

![Capture d'écran de la validation de données pour une heure valide](https://www.freecodecamp.org/news/content/images/2024/03/1684886767503.png)

Les colonnes B et C combinent ces informations dans un format utilisable pour envoyer à Google Calendar en utilisant la fonction =TEXT() pour concaténer la date et les heures ensemble.

![Capture d'écran de la concaténation de texte dans Google Sheets](https://www.freecodecamp.org/news/content/images/2024/03/1684886775902.png)

Je promets que cela aura plus de sens dans une seconde ! 😃

## Configuration du calendrier

Créons un nouveau calendrier dans Google Calendar.

![Capture d'écran des options de nouveau calendrier](https://www.freecodecamp.org/news/content/images/2024/03/1684887186669.png)

Sous vos calendriers dans la barre latérale gauche de Google Calendar, cliquez sur l'icône plus pour en ajouter un nouveau.

Donnez-lui un nom et une description si vous le souhaitez, et nous sommes prêts à commencer.

![Capture d'écran de la création d'un nouveau calendrier](https://www.freecodecamp.org/news/content/images/2024/03/1684887287557.png)

Faites défiler un peu dans les paramètres du calendrier jusqu'à la section Intégrer le calendrier. Copiez l'ID du calendrier. C'est ainsi que nous ferons communiquer Apps Script avec le Calendrier !

![Capture d'écran de l'ID du calendrier](https://www.freecodecamp.org/news/content/images/2024/03/1684887643027.png)

## Apps Script + CalendarApp

Apps Script est génial. 👍

La [Classe CalendarApp](https://developers.google.com/apps-script/reference/calendar/calendar-app) permet à un script d'accéder au Google Calendar d'un utilisateur et d'y apporter des modifications.

Voici le script complet, et nous allons passer en revue ce qui se passe ci-dessous.

```javascript
// Crée une variable events qui est un tableau de tableaux
function createCalendarEvent() {
	let events = SpreadsheetApp.getActiveSpreadsheet().getRangeByName("events").getValues();

	// Crée un événement pour chaque élément du tableau events
    
	events.forEach(function(e){
    	CalendarApp.getCalendarById("f7574e7b4d1ad00c9ecd7f1eba5bed329e8600e317cd387a400748d67f301d06@group.calendar.google.com").createEvent(
      	e[0],
      	new Date(e[1]),
      	new Date(e[2]),
      	{guests: e[6],sendInvites: true}
    );
  })
}
```

J'ai nommé la plage `A3:B8` comme "events". Ensuite, dans Apps Script, nous créons une variable nommée events qui récupère toutes les valeurs de cette plage entière. Nous avons utilisé une petite plage, mais vous pourriez la faire aussi longue que nécessaire.

```javascript
let events = SpreadsheetApp.getActiveSpreadsheet().getRangeByName("events").getValues();
```

Ensuite, nous parcourons chaque élément et ajoutons les événements à notre calendrier.

La première partie est celle où nous utilisons cette chaîne d'ID de calendrier que nous avons récupérée de Google Calendar pour la méthode `getCalendarById`.

Ensuite, nous utilisons la méthode `createEvent` pour extraire les données de chaque ligne de notre Google Sheet et créer de nouveaux événements.

Voici la description de `createEvent` depuis la [page des développeurs](https://developers.google.com/apps-script/reference/calendar/calendar-app#createeventtitle,-starttime,-endtime,-options) :

![Capture d'écran de la méthode createEvent](https://www.freecodecamp.org/news/content/images/2024/03/1684888482755.png)

Vous pouvez considérer chaque ligne de données dans Google Sheet comme un tableau de valeurs. À la position zéro se trouve le nom de l'événement, à la position un se trouve la date et l'heure de début de l'événement, et ainsi de suite.

![Capture d'écran illustrant un tableau de tableaux](https://www.freecodecamp.org/news/content/images/2024/03/1684938707460.jpeg)

En utilisant `e[0]`, nous pouvons accéder à l'élément qui se trouve à la position zéro pour chaque fois que nous parcourons la boucle forEach... ce qui revient effectivement à parcourir chaque ligne de données.

Et c'est là que les choses un peu étranges que nous avons faites avec les heures de début et de fin entrent en jeu.

Parce que les valeurs dans les colonnes B et C sont des chaînes de caractères puisque nous les avons concaténées ensemble, nous devons maintenant les transformer en objets date complets.

C'est pourquoi nous passons `new Date(e[1])` et `new Date(e[2])` dans notre fonction createEvent.

C'est un peu une méthode fastidieuse pour nous permettre d'utiliser ces sélections de liste déroulante dans Google Sheets plutôt que de taper péniblement un objet date/heure complet.

L'expérience utilisateur > le code. 👍

Et enfin, nous ajoutons un paramètre optionnel pour envoyer des invitations aux invités.

## Envoyer avec un bouton

C'est tout ce qu'il y a à faire avec Apps Script. 🎉

En tant que fonctionnalité supplémentaire, nous avons attaché un script au dessin de rectangle arrondi pour en faire fonctionner comme un bouton. Chaque fois que ce bouton est pressé, les événements dans Google Sheet seront ajoutés à Google Calendar.

![Capture d'écran de l'attribution d'un script à un dessin dans Google Sheets](https://www.freecodecamp.org/news/content/images/2024/03/1684938905901.png)

J'espère que cela a été utile pour vous !

Veuillez venir consulter et vous abonner à ma [chaîne YouTube](https://www.youtube.com/@eamonncottrell?sub_confirmation=1) où je publie des vidéos hebdomadaires sur la programmation et les feuilles de calcul.

Si vous souhaitez recevoir ma newsletter dans votre boîte de réception, [consultez-la ici](https://got-sheet.beehiiv.com/subscribe).