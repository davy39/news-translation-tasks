---
title: Comment exploiter le stockage local pour créer des applications ultra-rapides
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-25T18:44:13.000Z'
originalURL: https://freecodecamp.org/news/how-leverage-local-storage-to-build-lightning-fast-apps-4e8218134e0c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f0xRT52dcYqbK3JN_6fMgA.jpeg
tags:
- name: Android
  slug: android
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment exploiter le stockage local pour créer des applications ultra-rapides
seo_desc: 'By Nikita Kozlov

  Users love fast, responsive apps. They don’t want to hear about how API calls take
  time. They just want to see updates immediately. Right now. And we as a developers
  should strive to provide that. So how can we?

  The solution: storing...'
---

Par Nikita Kozlov

Les utilisateurs adorent les applications rapides et réactives. Ils ne veulent pas entendre parler du temps que prennent les appels API. Ils veulent simplement voir les mises à jour immédiatement. Tout de suite. Et en tant que développeurs, nous devons nous efforcer de fournir cela. Alors, comment pouvons-nous y parvenir ?

La solution : stocker ces changements localement, puis les synchroniser avec vos serveurs de temps en temps. Mais cela devient bien plus complexe lorsque des éléments comme la latence de connexion sont pris en compte.

Prenons Medium comme exemple. Les utilisateurs de Medium peuvent recommander un article à leurs abonnés en appuyant sur un petit cœur vert (il y en a un sur cette page aussi ?). En appuyant une deuxième fois sur le cœur, l'utilisateur peut arrêter de le recommander.

### La fonctionnalité est simple, mais les cas particuliers posent beaucoup de problèmes

Je ne sais pas exactement ce qui se passe à l'intérieur de l'application de Medium, mais pour simplifier, imaginons que le premier appui ajoute un élément à la liste de recommandations, et le second le retire.

Voyons quels types de problèmes cela pourrait nous causer si nous décidions d'ajouter une fonctionnalité similaire à notre application :

1. Nous devons prendre en compte que l'utilisateur peut commencer à appuyer comme un fou. Ce comportement pourrait entraîner un flux d'événements.
2. Internet n'est pas toujours rapide. Sur une mauvaise connexion réseau, même les appels API les plus simples pourraient prendre plusieurs secondes à se terminer. Pendant ce temps, l'utilisateur pourrait quitter l'écran actuel, puis revenir.
3. De temps en temps, les appels API peuvent échouer, et notre système doit être capable de se rétablir dans de telles situations.
4. Les utilisateurs peuvent avoir plusieurs appareils avec la même application, ou ils peuvent utiliser à la fois la version mobile de l'application et le site web correspondant en tandem. Dans les deux cas, nous devons avoir une politique pour synchroniser les données avec notre backend afin de mettre à jour son état.

Ce n'est pas une liste exhaustive des défis auxquels nous sommes confrontés, mais ce sont ceux sur lesquels cet article se concentrera.

### Définir le problème

![Image](https://cdn-media-1.freecodecamp.org/images/Hjb48bUy1QlA3xfQFwB96yKGdr8O7PlH-Iy8)

Avant de commencer à discuter de l'implémentation, définissons nos critères d'acceptation. La tâche consiste à développer une fonctionnalité qui permet à l'utilisateur d'ajouter et de supprimer des éléments d'une certaine liste. La liste est stockée sur notre backend.

L'implémentation doit répondre aux exigences suivantes :

1. **L'interface utilisateur réagit immédiatement aux actions de l'utilisateur.** L'utilisateur veut voir les résultats de ses actions immédiatement. Si plus tard nous ne pouvons pas synchroniser ces changements, nous devons en informer notre utilisateur et revenir à l'état précédent.
2. **L'interaction depuis plusieurs appareils est prise en charge.** Cela ne signifie pas que nous devons prendre en charge les changements en temps réel, mais nous devons récupérer la collection entière de temps en temps. De plus, notre backend nous fournit des points de terminaison API pour les ajouts et les suppressions, que nous devons utiliser pour supporter une meilleure synchronisation.
3. **L'intégrité des données est garantie.** Chaque fois qu'un appel de synchronisation échoue, notre application doit se rétablir élégamment des erreurs.

Heureusement, nous n'avons pas besoin d'implémenter toute la fonctionnalité, mais plutôt de développer un mécanisme de stockage qui nous permettra de l'implémenter. Examinons différentes façons de répondre à ces exigences.

### L'approche directe

![Image](https://cdn-media-1.freecodecamp.org/images/oLDGe3QJgeliWCKWuLDgQQCdjPlubHuDZK91)

La première solution qui vient à l'esprit est de stocker une copie locale de la liste, puis de la mettre à jour lorsque l'utilisateur effectue un changement.

La plupart des problèmes avec cette approche sont liés aux conditions de course ou aux échecs d'appels API, par exemple :

1. **Collisions entre la récupération et la modification de la liste.** Imaginons que nous avons commencé à récupérer des éléments de notre backend pour mettre à jour notre stockage local, et que l'utilisateur a effectué un changement avant que cette opération ne soit terminée. Cela entraînerait un conflit de fusion entre la liste récupérée et la liste locale. Nous devons donc distinguer, par exemple, entre un élément qui n'a pas encore été ajouté et un élément qui a déjà été supprimé du web ou d'un autre appareil.
2. **Échec de l'appel API.** Les utilisateurs peuvent effectuer de nombreux changements rapidement, et ils peuvent également les annuler rapidement. Par exemple, les utilisateurs peuvent ajouter un élément à une liste, puis le supprimer, puis l'ajouter à nouveau. Si le premier ajout échoue, nous devons nous en remettre. Dans ce cas, nous devons supprimer l'élément de la liste. Mais cela ruinerait l'intégrité de nos données, car l'élément devrait en fait être dans la liste, puisque le dernier appel que nous avons fait était un ajout et qu'il n'était pas encore terminé.

Même s'il pourrait y avoir un moyen de faire fonctionner cette approche, je soutiendrais que le stockage local devrait conserver plus d'informations que simplement le résultat final attendu. Cela nous permettra de nous remettre de tous les problèmes que nous pourrions rencontrer.

### Gardons l'historique de tout ce que l'utilisateur fait

![Image](https://cdn-media-1.freecodecamp.org/images/lMQoXy6k3uoNG9h23dxkNilJYjvn390W2iEt)

Voici une approche différente : gardons la liste que nous avons récupérée de l'API, ainsi que tout ce que l'utilisateur a fait. Chaque enregistrement correspondrait à un appel API (respectivement "ajouter" et "supprimer").

Une fois notre appel API terminé, nous pouvons mettre à jour notre copie locale et supprimer l'enregistrement de notre historique. Lorsque nous voulons synchroniser le navigateur de l'utilisateur avec notre backend, nous récupérons simplement la version de cette liste et remplaçons notre copie.

Nous n'avons plus de problèmes avec les échecs d'appels API, car nous connaissons l'état exact avant l'appel, et nous pouvons simplement supprimer cet enregistrement de l'historique sans perdre l'intégrité des données.

Le principal problème avec cela est la performance. Chaque fois que nous voulons vérifier si un élément particulier est dans la liste, nous devons parcourir tous les enregistrements pour calculer ce que notre utilisateur devrait s'attendre à voir.

Bien sûr, la performance dépend de la quantité d'interactions que notre utilisateur peut faire dans un certain laps de temps, et de la manière dont les données sont stockées. De plus, gardez à l'esprit que **l'optimisation prématurée est la source de tous les maux**, donc si vous n'avez pas ce problème, alors probablement c'est une voie à suivre.

Je pense que cette approche est excellente lorsque l'utilisateur crée du contenu dans l'application, car elle expose de nombreuses façons de gérer les problèmes de synchronisation. Mais notre problème est plus simple que cela, donc nous devrions être en mesure de faire quelques optimisations et d'augmenter encore les performances.

### Le juste milieu

![Image](https://cdn-media-1.freecodecamp.org/images/uk9K56dmC1IhVJgyo0opNtr6nenHfsAThhrO)

Il est possible d'avoir juste assez d'informations pour se remettre des cas négatifs. Avoir deux listes supplémentaires — une pour les ajouts en cours, et une pour les suppressions en cours — devrait suffire. Pour garantir l'intégrité des données, vous devriez simplement appliquer quelques règles :

1. **Les listes d'ajouts et de suppressions ont la priorité sur la liste principale.** Par exemple, supposons qu'un élément est à la fois dans la liste des suppressions et dans la liste principale. Lorsque le navigateur vérifie si l'élément est dans la liste, il devrait retourner faux.
2. **Un élément ne peut pas être dans les deux listes en même temps.** Si l'utilisateur a effectué plusieurs actions sur un seul élément, le dernier changement devrait avoir la priorité. Par exemple, si l'utilisateur a ajouté puis supprimé l'élément, en résultat il devrait être dans la liste des suppressions. Peu importe que l'élément soit dans la liste principale ou non.
3. **Uniquement après que le dernier appel API pour un certain élément est terminé peut-il être supprimé de la liste correspondante.** Par exemple, l'utilisateur pourrait avoir ajouté l'élément, l'avoir supprimé, puis l'avoir ajouté à nouveau avant que le premier appel ne soit terminé. Dans ce cas, l'élément serait dans la liste des ajouts. Mais il ne devrait être supprimé de là que après que le deuxième ajout soit terminé. Cela peut être réalisé en attribuant un ID à chaque entrée dans ces listes. Plus tard, après que l'appel API soit terminé, l'entrée serait supprimée en utilisant cet ID.
4. **Après chaque appel API, la liste principale doit être mise à jour.** La liste principale doit refléter l'état réel du backend au mieux de nos connaissances. Donc dans le cas d'un ajout et d'une suppression consécutifs, même si du côté de l'application cela semblerait que l'élément n'était pas dans la liste, après le premier appel nous devrions l'ajouter à la liste principale.

### Quelques mots sur les échecs d'appels API

Il existe différentes raisons pour lesquelles un appel API peut échouer. Certaines sont temporaires, d'autres non. Certaines sont fatales, et d'autres peuvent être récupérées. Quelle que soit la solution, même les requêtes échouées doivent retourner certaines informations sur la cause du problème.

Je pense que les codes d'état HTTP sont parfaits pour cela. Par exemple, si le code d'état est _504 Gateway Timeout_, alors réessayer pourrait être une bonne idée, mais s'il est _400 Bad Request_, alors il est probable que quelque chose ne va pas dans la logique du client et qu'une simple logique de réessai n'aidera pas. Certaines d'entre elles, comme _401 Unauthorized_, pourraient nécessiter certaines actions de l'utilisateur. _410 Gone_ ou _404 Not Found_ pendant l'appel de suppression pourrait signifier que l'utilisateur a supprimé cet élément depuis un autre appareil et il est probable que nous puissions même dire à l'utilisateur que l'opération a réussi, puisque l'intention de l'utilisateur est satisfaite.

Si pour une raison quelconque votre API n'utilise pas les codes d'état HTTP appropriés (je ne veux même pas savoir pourquoi), elle doit encore fournir des informations concernant la cause d'un problème. Sinon, vous pourriez rencontrer des problèmes étranges. Par exemple, si l'appel de suppression a échoué parce que l'élément **n'est plus** dans la liste, mais que nous n'avons pas d'informations sur la cause, alors l'application penserait que l'élément **est** dans la liste jusqu'au prochain cycle de récupération de la liste entière.

### Conclusion

La première solution était une simple liste. Elle était rapide, mais la gestion des cas négatifs était difficile.

Dans la deuxième approche, nous avons créé une structure de données qui agit comme une liste, mais qui a persisté les enregistrements de tous les changements effectués. Cela pouvait gérer les cas négatifs, mais c'était beaucoup plus lent.

Notre juste milieu était une solution qui — de l'extérieur — agit toujours comme une liste. Mais elle nous permet d'équilibrer la performance et de nous remettre facilement des erreurs.

Les problèmes mentionnés dans cet article ne sont qu'un aspect du problème. L'autre est le nombre d'appels API effectués. Si l'utilisateur effectue beaucoup d'interactions similaires, nous pouvons essayer de minimiser le nombre d'appels API effectués. Cette optimisation affecte également la structure de notre stockage local.

Je discuterai de cela et proposerai une solution supplémentaire à ces problèmes dans mes prochains articles.

Merci d'avoir lu cet article. Si vous l'avez aimé, n'oubliez pas de cliquer sur le ? ci-dessous. Vous pouvez également [me suivre sur Twitter](https://twitter.com/Nikita_E_Kozlov).