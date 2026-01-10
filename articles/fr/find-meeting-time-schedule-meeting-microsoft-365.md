---
title: Comment trouver un créneau de réunion et planifier une réunion sur Microsoft
  365
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-26T21:34:19.000Z'
originalURL: https://freecodecamp.org/news/find-meeting-time-schedule-meeting-microsoft-365
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-25-at-13.03.43.png
tags:
- name: JavaScript
  slug: javascript
- name: Microsoft
  slug: microsoft
- name: Web Development
  slug: web-development
seo_title: Comment trouver un créneau de réunion et planifier une réunion sur Microsoft
  365
seo_desc: 'By Waldek Mastykarz

  A common functionality that many work apps have is letting users schedule a meeting
  with others in their organization. Here''s how to do it on Microsoft 365.

  Work Apps Need Work Data

  If your organization uses Microsoft 365, it shou...'
---

Par Waldek Mastykarz

Une fonctionnalité courante que de nombreuses applications professionnelles possèdent est de permettre aux utilisateurs de planifier une réunion avec d'autres personnes de leur organisation. Voici comment le faire sur Microsoft 365.

## Les applications professionnelles ont besoin de données professionnelles

Si votre organisation utilise Microsoft 365, elle devrait envisager de l'intégrer avec les applications qu'elle utilise pour le travail.

Apporter des données et des informations de Microsoft 365 dans le contexte des applications professionnelles aide les utilisateurs à rester dans le flux de leur travail et à avoir accès à toutes les informations pertinentes en un seul endroit.

Par exemple, votre organisation dispose d'une application qu'elle utilise pour gérer des projets. En plus des informations sur le projet lui-même, les utilisateurs de l'application auront également besoin d'informations sur les personnes impliquées dans le projet pour obtenir des mises à jour ou planifier des réunions.

Les informations sur les personnes de votre organisation et leur travail sont stockées sur Microsoft 365 et vous pouvez les intégrer dans le contexte de votre application.

Lorsque vous développez des applications pour le travail, vous pouvez utiliser [Microsoft Graph](https://graph.microsoft.com/) - l'API pour Microsoft 365, pour interagir avec Microsoft 365 et récupérer les données qui y sont stockées.

## Trouver un créneau de réunion et planifier une réunion avec des participants sur Microsoft 365

De nombreux scénarios de travail nécessitent la possibilité de planifier une réunion avec d'autres personnes de votre organisation. Pour les organisations qui utilisent Microsoft 365, cette fonctionnalité est facilement disponible dans Microsoft Outlook.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-173.png)
_Planification d'une réunion dans Microsoft Outlook sur le web_

Mais que faire si vous ne voulez pas que vos utilisateurs quittent votre application, aillent sur Outlook et planifient manuellement la réunion avec les bonnes personnes ?

En utilisant Microsoft Graph, vous pouvez permettre aux utilisateurs de **sélectionner des participants, trouver un créneau de réunion approprié et planifier une réunion directement depuis votre application**. Laissez-moi vous montrer comment.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-176.png)
_Application web personnalisée permettant aux utilisateurs de trouver un créneau de réunion et de planifier une réunion_

Une application exemple construite en utilisant des fragments de code de cet article est disponible sur [GitHub](https://github.com/waldekmastykarz/mgt-spa-findmeetingtimes). Pour l'exécuter, vous aurez besoin de [Node.js LTS](https://nodejs.org/) et d'un locataire développeur Microsoft 365 que vous pouvez obtenir gratuitement depuis le [programme développeur Microsoft 365](https://developer.microsoft.com/microsoft-365/dev-program).

### Sélectionner les participants à la réunion

La première étape consiste à permettre aux utilisateurs de sélectionner avec qui ils souhaitent se réunir.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-179.png)
_Application web avec quelques personnes sélectionnées pour trouver des créneaux de réunion disponibles_

Le moyen le plus simple de le faire est d'utiliser le composant [People picker](https://learn.microsoft.com/graph/toolkit/components/people-picker) de Microsoft Graph Toolkit.

> [Microsoft Graph Toolkit](https://aka.ms/mgt-docs) est un ensemble de composants web connectés à Microsoft Graph, qui fonctionnent dans n'importe quel framework web.

Pour ajouter le sélecteur de personnes, vous ajouteriez à votre application :

```html
<mgt-people-picker></mgt-people-picker>
```

Le sélecteur de personnes récupère automatiquement les informations sur les personnes de votre organisation depuis Microsoft 365 et filtre la liste au fur et à mesure que vous tapez. Chaque personne apparaît avec son nom et sa photo pour aider les utilisateurs à sélectionner la bonne personne.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/select-people-graph-mgt.gif)
_Sélection de personnes depuis Microsoft 365 dans une application web personnalisée_

En le combinant avec le [composant Login](https://learn.microsoft.com/graph/toolkit/components/login) de Microsoft Graph Toolkit, vous permettez aux utilisateurs de se connecter à votre application avec leur compte Microsoft 365 et d'accéder à l'API Microsoft Graph.

### Trouver des créneaux de réunion

L'étape suivante consiste à trouver des créneaux de réunion disponibles pour les participants sélectionnés, y compris l'utilisateur actuel.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-178.png)
_Créneaux de réunion disponibles pour les personnes sélectionnées depuis Microsoft 365_

Plutôt que de devoir télécharger les calendriers de tous les utilisateurs et de chercher manuellement un créneau de réunion approprié, vous pouvez appeler l'API [`findMeetingTimes` de Microsoft Graph](https://learn.microsoft.com/graph/api/user-findmeetingtimes?view=graph-rest-1.0&tabs=javascript), en passant en arguments le tableau des participants et la durée de la réunion.

```javascript
const meetingTimes = await graphClient
  .api('/me/findMeetingTimes')
  .post({
    attendees: document.querySelector('mgt-people-picker').selectedPeople.map(p => {
      return {
        emailAddress: {
          address: p.userPrincipalName,
          name: p.displayName
        },
        type: 'required'
      };
    }),
    maxCandidates: 3,
    meetingDuration: `PT${document.querySelector('#duration').value}`,
    returnSuggestionReasons: true,
    minimumAttendeePercentage: 100
  });
availableMeetingTimes = meetingTimes.meetingTimeSuggestions;
```

Vous pouvez obtenir la liste des participants depuis le sélecteur de personnes qui expose la liste des personnes sélectionnées par l'utilisateur.

Lorsque vous demandez des créneaux de réunion disponibles, vous pouvez passer de nombreuses options supplémentaires, telles que le nombre de suggestions que vous souhaitez obtenir (`maxCandidates`), le pourcentage minimum de participants qui doivent pouvoir assister à la réunion (`minimumAttendeePercentage`), ou entre quelles heures la réunion doit avoir lieu.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/find-meeting-times-graph.gif)
_Trouver des créneaux de réunion disponibles pour les participants sélectionnés et la durée de la réunion_

### Planifier une réunion

La dernière étape consiste à planifier une réunion.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-180.png)
_Planification d'une réunion sur Microsoft 365 depuis une application web personnalisée_

À ce stade, vous disposez de toutes les informations nécessaires pour envoyer une invitation de réunion aux personnes sélectionnées au nom de l'utilisateur actuel.

Vous pouvez le faire en appelant l'API `events` de Microsoft Graph, en passant dans le corps de la requête toutes les informations telles que le sujet, l'heure de début et de fin, et la liste des participants.

```javascript
const meetingTime = availableMeetingTimes[selectedMeetingTime].meetingTimeSlot;

await graphClient
  .api('/me/events')
  .post({
    subject: document.querySelector('#subject').value,
    start: meetingTime.start,
    end: meetingTime.end,
    attendees: document.querySelector('mgt-people-picker').selectedPeople.map(p => {
      return {
        emailAddress: {
          address: p.userPrincipalName,
          name: p.displayName
        },
        type: 'required'
      };
    })
  });
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/scheduling-meeting-graph.gif)
_Planification d'une réunion sur Microsoft 365 depuis une application web personnalisée_

## Résumé

En intégrant Microsoft 365 dans vos applications professionnelles, vous aidez vos utilisateurs à travailler plus efficacement.

En utilisant l'API Microsoft Graph, vous pouvez apporter des données et des informations de Microsoft 365 dans vos applications professionnelles. Cela fournit à vos utilisateurs toutes les informations dont ils ont besoin pour accomplir leurs tâches.

Parce qu'ils ont toutes les informations dont ils ont besoin à portée de main, ils n'ont pas besoin de basculer entre différentes applications et peuvent rester dans le flux de leur travail. Et en utilisant des composants web de Microsoft Graph Toolkit, vous pouvez construire des applications connectées à Microsoft 365 encore plus rapidement.

Consultez l'[application exemple](https://github.com/waldekmastykarz/mgt-spa-findmeetingtimes), et j'ai hâte d'avoir de vos nouvelles sur ce que vous en pensez et quels autres scénarios d'intégration vous intéresseraient.