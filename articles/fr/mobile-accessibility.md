---
title: Meilleures pratiques d'accessibilité pour le développement d'applications mobiles
subtitle: ''
author: Ilknur Eren
co_authors: []
series: null
date: '2021-09-30T21:47:00.000Z'
originalURL: https://freecodecamp.org/news/mobile-accessibility
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/IMG-0754.jpg
tags:
- name: Accessibility
  slug: accessibility
- name: mobile app development
  slug: mobile-app-development
seo_title: Meilleures pratiques d'accessibilité pour le développement d'applications
  mobiles
seo_desc: 'The United States Census Bureau estimates that more than 12% of the United
  States'' population is living with a disability. Disabilities can include vision
  difficulties, hearing difficulties, mobility challenges, and much more.

  And a person can become...'
---

Le [United States Census Bureau](https://data.census.gov/cedsci/table?q=disability&tid=ACSST1Y2019.S1810) estime que plus de 12 % de la population des États-Unis vit avec un handicap. Les handicaps peuvent inclure des difficultés visuelles, des difficultés auditives, des défis de mobilité, et bien plus encore.

Et une personne peut devenir handicapée à n'importe quel stade de sa vie.

Puisqu'une partie significative de la population a un type de handicap ou un autre, il est important de développer des technologies accessibles à tous. Ainsi, nous pouvons tous consommer du contenu technologique et personne n'est laissé pour compte.

Dans cet article, nous aborderons certaines des meilleures pratiques d'accessibilité et ce que vous pouvez faire pour rendre vos applications mobiles plus accessibles.

## Ajoutez des descriptions utiles à chaque élément

Le [Center for Disease Control and Prevention's Vision Health Initiative](https://www.cdc.gov/visionhealth/risk/burden.htm#Estimates) indique que,

> En 2015, un total de 1,02 million de personnes étaient aveugles, et environ 3,22 millions de personnes aux États-Unis avaient une déficience visuelle (VI), définie par la meilleure acuité visuelle corrigée dans l'œil le plus performant.
> 
> De plus, 8,2 millions de personnes avaient une VI due à une erreur de réfraction non corrigée. D'ici 2050, le nombre de ces conditions devrait doubler pour atteindre environ 2,01 millions de personnes aveugles, ou ayant une VI de 20/200 ou pire, 6,95 millions de personnes avec une VI, et 16,4 millions avec une VI due à une erreur de réfraction non corrigée. (Varma 2015)

Un outil d'accessibilité utile pour les personnes ayant peu ou pas de vision est un outil de lecture vocale. Cela permet à l'utilisateur d'écouter le contenu de la page web sur son téléphone.

Je voudrais vous mettre à la place de quelqu'un qui pourrait utiliser la lecture vocale sur son téléphone.

Ci-dessous se trouvent les annonces "prix réduit" de Facebook Marketplace. Écoutez simplement 22 secondes de cette voix off pour entendre comment cette section sonne pour quelqu'un utilisant l'outil.

%[https://soundcloud.com/ilknur-eren/reduced-price-audio] 

La voix off dit 'Prix réduit, bouton' pour indiquer à l'utilisateur que cette section est pour les articles à prix réduit, et qu'il y a une action de clic qu'ils peuvent effectuer dans ce focus particulier.

Ensuite, l'élément focalisé dit, "Masquer la catégorie, bouton" ce qui indique à nouveau que dans cet élément focalisé, l'utilisateur peut effectuer une action pour masquer la catégorie.

Ensuite, le "Voir tout, bouton" est focalisé. Cela indique qu'ils peuvent effectuer une action sur cet élément pour voir tous les articles de la catégorie.

Au focus suivant, nous entendons, "Aucune description de photo disponible, bouton, image". Qu'est-ce que cet article pourrait être ? Nous ne le savons pas à ce stade.

Et pour l'élément focalisé suivant, nous entendons la même chose, "Aucune description de photo disponible, bouton, image". Maintenant, deux éléments de cette liste n'ont aucun contenu pour la description.

L'élément focalisé suivant dit, "Peut-être une image de bijoux, bouton, image". Le mot "peut-être" au début de la phrase indique que l'outil de voix off n'est pas sûr de ce que l'élément pourrait être.

"Image de bijoux" est une description large, surtout si vous êtes sur un site pour faire des achats. Est-ce un collier ? Est-ce une bague ? Est-ce une boucle d'oreille ? Est-ce un ensemble de bijoux ? De quel matériau est-il fait ? À quoi ressemble-t-il ? Combien coûte ce bijou pour commencer ?

Et le dernier élément focalisé dit ce que nous avons entendu des deux premiers, "Aucune description de photo disponible, bouton, image".

C'est ainsi que les utilisateurs ayant peu ou pas de vision doivent naviguer dans les applications. Il y avait quatre boutons ici, aucun d'entre eux avec une description. Si vous utilisiez cette application, sur lequel cliqueriez-vous ?

Maintenant, je veux vous montrer l'enregistrement vidéo de la même page, que vous pouvez voir ci-dessous :

%[https://youtu.be/g0PS_DdgwGU] 

Le premier article que la voix off a mentionné comme "Aucune description de photo disponible, bouton, image" était en fait une image d'une table vintage des années 1960 et elle est gratuite.

Le deuxième article est un autocollant qui coûte 3 $ et qui dit, "Je suis toujours avec toi" avec un oiseau rouge à côté.

Le troisième article qui n'avait qu'une description partielle ("Peut-être une image de bijoux, bouton, image") est une boucle d'oreille en perle qui est en vente pour 8 $.

Enfin, le quatrième article qui disait, "Aucune description de photo disponible, bouton, image" est une carte Pokeman de Pikachu, qui coûte 9,50 $.

Vous attendiez-vous à cela après le premier clip audio ? Probablement pas. Si vous n'aviez pas vu l'image ou lu le titre, vous n'auriez aucune idée de ce qui est en vente sur Facebook marketplace.

Une façon de résoudre ce problème est de s'assurer que chaque élément a un `accessibilityLabel` avec les informations de base dont vous auriez besoin pour savoir ce que c'est sans le voir. La documentation [React Native](https://reactnative.dev/docs/accessibility#accessibilitylabel) vous indique que,

> "Pour utiliser, définissez la propriété `accessibilityLabel` sur une chaîne personnalisée sur votre View, Text ou Touchable".

Un `accessibilityLabel` est un moyen simple mais efficace de décrire l'élément pour les utilisateurs de lecteurs d'écran.

Pour vous montrer comment cela fonctionnerait, codons ensemble un exemple plus simple.

Par exemple, nous pourrions créer la liste de la table du marketplace de Facebook en ajoutant un `accessibilityLabel` à l'élément `TouchableOpacity`.

**Exemple de code :**

```php
<TouchableOpacity
  accessible={true}
  accessibilityLabel="Gratuit, table vintage des années 1960"
  >
....
</TouchableOpacity>
```

Le code ci-dessus ajoute le `accessibilityLabel` à l'élément qui contient le bouton entier. Nous avons ajouté "Gratuit, table vintage des années 1960" comme accessibilityLabel.

Lorsque le lecteur d'écran survole l'élément avec cet attribut, il lira, "Gratuit, table vintage des années 1960, bouton". Cela permettra à l'utilisateur de connaître le prix, une brève description, et le fait que c'est un bouton sur lequel ils peuvent cliquer.

Cela rend cet élément particulier beaucoup plus accessible pour ceux qui dépendent des lecteurs d'écran.

## Assurez-vous de décrire l'état de l'élément

Dans certains éléments, vous devrez décrire l'état actuel d'un composant à l'utilisateur.

Par exemple, si vous avez une case à cocher, vous devez informer l'utilisateur si la case est cochée ou non.

Un autre élément courant que vous voudrez décrire est si les boutons sont désactivés sur une page. Si l'utilisateur ne peut pas cliquer sur le bouton, alors vous devez informer l'utilisateur qu'il y a un bouton, mais qu'il est désactivé.

La page de publication LinkedIn ci-dessous contient un exemple de bouton désactivé. Le bouton n'est pas actif à moins que l'utilisateur ne tape quelque chose dans le corps de la publication :

**Exemple :**

![Image](https://www.freecodecamp.org/news/content/images/2021/09/IMG-0748.jpg align="left")

*Page de publication LinkedIn avec focus sur le bouton de publication atténué.*

Dans l'image ci-dessus, le focus est sur le bouton de publication désactivé. Lorsque la voix off est focalisée sur cette section, elle dit, "Publier, atténué, bouton". Cela informe l'utilisateur que ceci est un bouton, mais qu'il ne peut pas cliquer dessus car il est atténué.

**Exemple de code :**

Dans le code ci-dessous, lorsque vous focalisez sur le bouton, il dira, "Bouton, atténué" s'il s'agit d'un bouton désactivé.

```php
<Button accessibilityState={disabled ? {disabled: true} : {disabled: false}}>
```

Ci-dessous se trouvent d'autres façons d'informer l'utilisateur sur l'état d'un élément. Le lecteur d'écran dira soit, "Élément de menu, sélectionné" ou "Case à cocher, sélectionnée" si l'élément de menu ou la case à cocher est sélectionné.

```php
//Élément de menu
<Button accessibilityRole={"menuitem"} accessibilityState={selected ? { selected: true } : { selected: false }} />

//Case à cocher
<Checkbox label="Case à cocher" selected={checked} accessibilityState={checked ? { checked: true } : { checked: false }} />
```

## Le contexte est important

Puisque les gens écoutent une description de la page lorsqu'ils utilisent la voix off, il est important que le contexte d'un élément ait du sens et ne soit pas confus.

Cela signifie que parfois il est plus logique de regrouper certains éléments ensemble. S'il y a plus d'une action que l'utilisateur peut effectuer dans une situation particulière, nous devrions attacher `[accessibilityActions](https://reactnative.dev/docs/accessibility#accessibility-actions)` à celui-ci.

### Exemple non utile :

Ci-dessous se trouve une capture d'écran que j'ai prise de mon application LinkedIn. Cette section est un lien où, si je clique dessus, je serai redirigé vers une autre section de l'application. Ce composant a également un bouton où je peux effectuer plus d'actions sur cet élément particulier.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-24-at-4.56.25-PM.png align="left")

*Notification LinkedIn qui dit, "Un diplôme de bachelor en vaut-il vraiment la peine ? Voici ce qu'une récente enquête a trouvé." Dans la première image, le focus est sur le texte du titre. Dans la deuxième image, le focus est sur "6h" qui est à côté du titre.*

Tout d'abord, la voix off se concentre sur le titre, "Un diplôme de bachelor en vaut-il vraiment la peine ? Voici ce qu'une récente enquête a trouvé". L'élément suivant qui est focalisé est "6h", puis le focus passe aux trois points où l'utilisateur peut effectuer plus d'actions.

C'est confus lorsque le lecteur d'écran dit, "6h" – que signifie cela ? Les utilisateurs qui peuvent voir l'élément peuvent comprendre que cela a été publié il y a 6 heures. Mais le lecteur d'écran dit simplement "6h" ce qui est confus.

De plus, dans cet élément, l'utilisateur doit se concentrer sur trois sections différentes pour en déduire toute la signification prévue.

Ce qui aurait été mieux pour l'accessibilité, c'est si ce composant avait été regroupé et lu, "Un diplôme de bachelor en vaut-il vraiment la peine ? Voici ce qu'une récente enquête a trouvé, publié il y a 6 heures, actions disponibles". Ainsi, il y a un meilleur contexte pour l'ensemble de l'élément.

### Meilleur exemple :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-24-at-4.55.38-PM.png align="left")

*Composant focalisé qui lit, "Ingénieur Front-End, AWS Data Wrangler, Amazon Web Services (AWS), New York, NY," avec le bouton de marque-page dans le coin droit.*

Ci-dessus se trouve un exemple d'une autre section de l'application LinkedIn. Cette section lit, "Ingénieur Front-End, AWS Data Wrangler, Société, Amazon Web Services (AWS), Localisation, New York, NY, actions disponibles".

Bien que les mots "société" et "localisation" ne soient pas à l'écran, la voix off les lit pour donner un meilleur contexte à l'utilisateur. De plus, le bouton de marque-page n'est pas un autre élément sur lequel l'utilisateur doit faire défiler pour se concentrer – il est regroupé, ce qui donne un meilleur contexte à l'utilisateur.

**Exemple de code :**

```php
<View
  accessible={true}
  accessibilityActions={[
    { name: 'navigate', label: 'naviguer' },
    { name: 'bookmark', label: 'marque-page' },
  ]}
  onAccessibilityAction={(event) => {
    switch (event.nativeEvent.actionName) {
      case 'navigate':
        Alert.alert('Alerte', 'Navigation vers une autre page');
        break;
      case 'bookmark':
        Alert.alert('Alerte', 'Marque-page de ce lien');
        break;
    }
  }}
/>
```

Dans l'exemple de code ci-dessus, un lecteur d'écran dira, "actions disponibles, balayez vers le haut ou vers le bas pour afficher les actions personnalisées".

Lorsque l'utilisateur balaye vers le haut, il entendra "naviguer". Et ensuite, lorsqu'il balaye une fois de plus, il entendra "marque-page". Si l'utilisateur souhaite sélectionner l'une des options, il peut double-taper lorsqu'il entend l'option qu'il souhaite. Ainsi, les actions ont un meilleur contexte.

## Conclusion

Avec de petits changements dans votre code, vous pouvez rendre les applications beaucoup plus accessibles pour tous les utilisateurs. 12 pour cent de la population des États-Unis vit avec un handicap et personne ne devrait être laissé pour compte.

Les personnes handicapées peuvent utiliser des outils comme les lecteurs d'écran et bien plus encore, et c'est à vous de rendre vos applications accessibles à ces outils.

C'est la responsabilité de tous de s'assurer que la technologie est accessible à tous. Merci d'avoir lu !