---
title: Comment supprimer tous les posts enregistrés de Facebook en utilisant JavaScript
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2024-10-30T19:17:57.450Z'
originalURL: https://freecodecamp.org/news/remove-all-saved-posts-from-facebook-using-javascript
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/PTiQqAKzbmM/upload/94f3490edcd662844a0bf56f2e6b0ce2.jpeg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment supprimer tous les posts enregistrés de Facebook en utilisant JavaScript
seo_desc: 'If you''re an avid Facebook user, you''ve probably saved countless posts,
  videos, and links to revisit later.

  But sometimes, these saved posts accumulate and become overwhelming. You may decide
  to un-save them all at once rather than manually uncheckin...'
---

Si vous êtes un utilisateur assidu de Facebook, vous avez probablement enregistré d'innombrables posts, vidéos et liens à consulter plus tard.

Mais parfois, ces posts enregistrés s'accumulent et deviennent écrasants. Vous pouvez décider de tout désenregistrer d'un coup plutôt que de désélectionner manuellement chacun d'eux, surtout si vous avez accumulé une grande collection.

Voici un guide étape par étape pour désenregistrer en masse tous vos éléments enregistrés sur Facebook.

**Avertissement :** Avant de continuer, notez que cette méthode désenregistrera tous les éléments affichés sur la page de manière permanente. Une fois désenregistrés, les éléments n'apparaîtront plus dans votre liste d'enregistrements. Il n'y a aucun moyen de les récupérer à moins de réenregistrer manuellement chaque post. Veuillez utiliser cette méthode avec prudence.

De plus, vous devrez peut-être utiliser `allow pasting` et appuyer sur la touche Entrée si Facebook vous avertit avant d'appliquer des commandes JavaScript dans la console.

### **Étape 1 : Faites défiler vos éléments enregistrés**

Commencez par vous rendre dans la section des éléments enregistrés de Facebook. Vous pouvez y accéder en cliquant sur l'icône de menu (trois lignes horizontales) dans l'application mobile ou sur la section enregistrée du côté gauche de la page d'accueil dans la version de bureau.

Faites défiler vers le bas pour charger et afficher tous les éléments enregistrés que vous souhaitez désenregistrer. Facebook ne charge que quelques éléments à la fois lorsque vous faites défiler, alors assurez-vous d'avoir chargé tout ce que vous souhaitez désenregistrer.

### **Étape 2 : Ouvrez la console de développement**

Pour commencer le processus de désenregistrement en masse, vous devrez utiliser la console de développement de votre navigateur. Voici comment faire :

* Sur **Google Chrome** : Appuyez sur `Ctrl + Shift + J` (Windows) ou `Cmd + Option + J` (Mac) pour ouvrir la console.
  
* Sur **Firefox** : Appuyez sur `Ctrl + Shift + K` (Windows) ou `Cmd + Option + K` (Mac).
  

Une fois la console ouverte, vous pouvez commencer à exécuter les commandes JavaScript nécessaires.

### **Étape 3 : Ouvrez le menu contextuel pour chaque élément**

Vous devrez d'abord ouvrir le menu contextuel (les trois points à côté de chaque post enregistré) pour chaque élément de la page. C'est là que Facebook vous permet de désenregistrer des posts individuels.

Copiez et collez la commande suivante dans la console et appuyez sur **Entrée** :

```javascript
Array.from(document.querySelector('[role=main]').querySelectorAll('[aria-label="More"]')).slice(1).map(e => e.click())
```

Cette commande trouve tous les boutons "More" sur la page et ouvre le menu contextuel pour chaque élément enregistré.

### **Étape 4 : Désenregistrez chaque élément**

Une fois les menus contextuels ouverts pour chaque post enregistré, il est temps de les désenregistrer en masse. Pour cela, exécutez la commande suivante dans la console :

```javascript
Array.from(document.querySelectorAll('[role=menuitem]')).map(e => e.click())
```

Cette commande clique sur l'option "Un-save" dans chaque menu contextuel qui a été ouvert, supprimant les éléments de votre liste d'enregistrements.

### **Rappel important :**

Tous les éléments affichés sur la page seront désenregistrés **de manière permanente**. Assurez-vous d'avoir passé en revue les éléments avant de procéder avec cette méthode.

## **Conclusion**

Cette méthode vous évite la corvée de désenregistrer manuellement les éléments un par un. N'oubliez pas de faire défiler et de charger tous les éléments enregistrés avant d'exécuter le script pour vous assurer que rien n'est laissé derrière.

De plus, comme cette méthode n'affecte que les éléments actuellement affichés, vous devrez peut-être faire défiler et répéter le processus si vous avez beaucoup de posts enregistrés.

En suivant ces étapes, vous pouvez facilement désencombrer vos éléments enregistrés sur Facebook et ne garder que ce qui compte vraiment.

Vous pouvez me suivre sur [GitHub](https://github.com/FahimFBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), et [YouTube](https://youtube.com/@FahimAmin) pour obtenir plus de contenu comme celui-ci. De plus, mon [site web](https://www.fahimbinamin.com/) est toujours disponible pour vous !

Ressource : [Commentaire GitHub](https://github.com/bouiboui/facebook-saved/issues/6#issuecomment-755982611)