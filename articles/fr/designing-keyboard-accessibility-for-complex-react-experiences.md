---
title: Comment concevoir l'accessibilité clavier pour des expériences React complexes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-11T19:10:00.000Z'
originalURL: https://freecodecamp.org/news/designing-keyboard-accessibility-for-complex-react-experiences
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/r.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: React
  slug: react
seo_title: Comment concevoir l'accessibilité clavier pour des expériences React complexes
seo_desc: "By James Y Rauhut\nLast week was my last week at Pingboard as a UX designer\
  \ and engineer. But I still believe the product includes the world's best org chart\
  \ solution. \nUsing a mouse, you can quickly drag-and-drop any org structure and\
  \ employee data s..."
---

Par James Y Rauhut

La semaine dernière était ma dernière semaine chez Pingboard en tant que designer UX et ingénieur. Mais je crois toujours que le produit inclut la meilleure solution d'organigramme au monde. 

Avec une souris, vous pouvez rapidement glisser-déposer n'importe quelle structure d'organigramme et les données des employés restent synchronisées avec vos autres outils. L'aspect le plus impressionnant est la manière dont l'organigramme est _vivant_. Les employés peuvent explorer l'organigramme par eux-mêmes et même le rendre disponible au public.

Mais que se passe-t-il si un utilisateur ne peut pas naviguer dans l'organigramme avec sa souris ? Trois Américains sur dix ont une forme de handicap. Beaucoup de ces handicaps limitent les personnes à naviguer sur le web uniquement avec leur clavier.

Si un utilisateur essayait de naviguer dans l'organigramme avec la touche de tabulation, le focus sautait autrefois d'un nœud à l'autre de manière imprévisible. 

Et oubliez l'édition de l'organigramme sans souris : beaucoup des actions d'édition étaient cachées dans des menus et modales de débordement inaccessibles. Nous avons passé une année à rendre l'organigramme entièrement accessible au clavier.

%[https://vimeo.com/438922739]

La solution n'a pas été trouvée en un seul sprint. Cela a été plusieurs versions étalées sur une année. 

Dans cet article de blog, je vais d'abord détailler le processus de conception de ces interactions. La section suivante entrera dans les détails de la mise en œuvre de ces interactions dans React. 

J'espère qu'à la fin, vous aurez appris à gérer les problèmes courants pour ajouter l'accessibilité clavier aux expériences complexes !

## Comment concevoir une expérience inclusive

Vous devez toujours savoir quel aspect de l'accessibilité vous essayez de résoudre. Les solutions d'accessibilité sont rarement une solution 1:1 pour un handicap spécifique. 

Par exemple, ajouter l'accessibilité clavier peut aider les personnes ayant une grande variété de handicaps moteurs et visuels. L'accessibilité clavier ne fera pas grand-chose pour le daltonisme, qui est un handicap visuel. C'est pourquoi je dis que nous rendons l'organigramme accessible au clavier plutôt que généralement accessible.

L'un des meilleurs aspects de l'accessibilité pour le web est que nous avons des directives acceptées internationalement. Le W3C a un document appelé les [Pratiques de création WAI-ARIA](https://www.w3.org/TR/wai-aria-practices-1.1/). Je sais que c'est un peu long, mais voici pourquoi c'est si génial : cette ressource gratuite inclut des modèles de conception détaillés pour les éléments d'interface utilisateur courants.

Vous voulez savoir comment les accordéons, les menus déroulants, les modales et les popovers doivent fonctionner ? Le document spécifie les interactions clavier exactes nécessaires avec des exemples codés. Ces modèles ont rendu la mise à jour de nos composants communs très facile.

### Comment trouver le bon modèle mental

![Trois joueurs de basket avec le logo React sur leurs maillots lisant un playbook ensemble](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/avz8acnbvxfuqr75yeem.jpeg)

La partie délicate de la conception de l'accessibilité clavier pour l'organigramme était la navigation de carte à carte. Il n'y avait aucun modèle dans le document pour les organigrammes. Alors, que faire ?!

Eh bien, l'un des meilleurs attributs de la conception d'interaction est la familiarité. Nous avons commencé à étudier le document pour trouver le **modèle mental** le plus proche de la navigation dans un organigramme. Les modèles mentaux sont des représentations dérivées d'autres expériences :

> "Concevez en gardant à l'esprit les modèles d'interaction des gens. S'il existe un modèle mental standard pour le fonctionnement de quelque chose, essayez de concevoir en exploitant ce modèle. Lorsque cela n'est pas possible (par exemple, le système est nouveau et novateur), créez une expérience d'interaction qui s'inspire des modèles mentaux courants autant que possible..." – [Principes universels de la conception par Lidwell, Holden et Butler](https://bookshop.org/books/universal-principles-of-design-revised-and-updated-125-ways-to-enhance-usability-influence-perception-increase-appeal-make-better-design-decision/9781592535873)

Alors, quel était le modèle le plus similaire avec lequel les gens interagissent tous les jours ? La réponse était une fenêtre de recherche pour naviguer dans les fichiers et dossiers, formellement connue sous le nom de [vue en arbre](https://www.w3.org/TR/wai-aria-practices-1.1/examples/treeview/treeview-1/treeview-1a.html). Le modèle mental de navigation entre des fichiers parallèles et de creusement plus profond dans les dossiers était une correspondance pour les utilisateurs !

La seule modification que nous avons dû apporter était d'inverser l'axe des touches de direction. Dans la navigation de dossiers, vous allez plus profond lorsque vous appuyez sur la touche _flèche droite_, mais il semblait plus naturel dans l'organigramme d'utiliser la touche _flèche bas_. Nous avons fini avec les contrôles clavier suivants :

* _Flèche Gauche_ et _Flèche Droite_ – Déplace le focus vers un nœud adjacent dans la structure de données.
* _Flèche Bas_ – Lorsque le focus est sur un nœud fermé, ouvre le nœud, et le focus ne bouge pas. Lorsque le focus est sur un nœud ouvert, déplace le focus vers le premier nœud enfant. Lorsque le focus est sur un nœud final, ne fait rien.
* _Flèche Haut_ – Lorsque le focus est sur un nœud ouvert, ferme le nœud. Lorsque le focus est sur un nœud enfant qui est également soit un nœud final soit un nœud fermé, déplace le focus vers son nœud parent. Lorsque le focus est sur un nœud racine qui est également soit un nœud final soit un nœud fermé, ne fait rien.
* _Home_ et _End_ – Déplace le focus vers les premier et dernier nœuds.
* a-z, A-Z – Le focus se déplace vers le nœud suivant avec un titre de poste ou de département qui commence par le caractère tapé. La recherche revient au premier nœud si un nom correspondant n'est pas trouvé parmi les nœuds qui suivent le nœud focalisé. La recherche ignore les nœuds qui sont des descendants de nœuds fermés.
* * (astérisque) – Développe tous les nœuds frères fermés qui sont au même niveau que le nœud focalisé. Le focus ne bouge pas.

### Comment traduire les interactions de survol au clavier

Un aspect agréable de notre organigramme est la propreté des cartes lors de la navigation. Chaque carte peut potentiellement avoir huit boutons attachés, mais nous les cachons jusqu'à ce que vous survoliez la carte avec le curseur de la souris. 

Alors, comment accommoder la navigation au clavier lorsque tous les boutons sont cachés ?

Nous avons décidé de révéler toutes les actions de la carte (boutons) lorsque vous sélectionnez une carte avec la touche entrée. À partir de ce moment, nous basculons les interactions clavier vers ce que l'on appelle une [grille de disposition](https://www.w3.org/TR/wai-aria-practices/examples/grid/LayoutGrids.html). 

Le modèle mental le plus proche que nous avons trouvé pour les grilles de disposition est la navigation dans une feuille de calcul avec les touches de direction. 

Une partie délicate de la mise en œuvre d'une grille de disposition est la disposition de l'interaction. Vous savez visuellement où se trouvent les éléments dans la disposition, mais les dispositions d'interaction vous obligent à placer les actions dans une grille stricte de colonnes et de lignes. 

Les dispositions d'interaction sont un document technique clair qui indique à un développeur exactement où le focus ira en fonction de la touche de direction pressée.

En parlant de focus, passons à la mise en œuvre technique...

## Comment coder des états de focus accessibles avec React

Lorsque vous parlez d'accessibilité clavier sur le web, vous parlez principalement de l'état de focus. 

Un navigateur ne peut avoir qu'un seul élément focalisé à la fois. Nous avons l'habitude de naviguer dans le navigateur avec nos claviers en utilisant la touche de tabulation pour avancer et les touches shift + tab pour reculer. 

Comme nous l'avons vu dans la section précédente sur la conception d'interaction, différentes expériences nécessitent des contrôles clavier plus complexes pour déplacer l'état de focus.

Si React est la bibliothèque que nous utilisons pour rendre l'interface utilisateur, nous devons penser aux états de focus dans ce contexte. Il y a quatre défis courants lors de la gestion de l'état de focus dans React :

1. Créer des interactions clavier personnalisées
2. Piéger le focus dans les composants appropriés
3. Passer le focus à d'autres composants
4. Passer le focus à des composants pas encore montés

**Conseil rapide :** Dans beaucoup des exemples ci-dessous, nous allons travailler sur une modale (dialogue). Honnêtement, il existe un million de solutions open-source pour des modales accessibles que vous devriez considérer avant de créer la vôtre. La raison pour laquelle les exemples sont précieux est qu'ils vous permettront de reconnaître et de résoudre les problèmes courants d'état de focus dans React.

### Comment créer des interactions clavier personnalisées dans React

Pour les composants courants, je ne peux pas recommander assez [Reakit](https://reakit.io/). C'est une bibliothèque de composants non stylisés et accessibles au clavier avec des dialogues, des popovers, et bien plus encore. Je l'utilise pour tous mes projets personnels de nos jours. Combiné avec [Framer Motion](https://www.framer.com/motion/) pour l'animation et [Styled Components](https://styled-components.com/) pour le style, c'est un mélange redoutable.

Mais que faire si vous devez créer une interaction clavier personnalisée dans React ? Eh bien, bien qu'il soit intelligent d'avoir des connaissances de base sur les [événements clavier](https://www.javascripttutorial.net/javascript-dom/javascript-keyboard-events/), ils sont assez faciles avec les hooks React ! 

Voici une simple interaction clavier utilisant une bibliothèque de hooks React appelée [React-Use](https://streamich.github.io/react-use/?path=/story/sensors-usekey--docs) :

%[https://codesandbox.io/s/1-keyboard-accessible-modal-br4vo?from-embed]

C'est tout. C'est la solution.

Ci-dessus, nous respectons la spécification de la modale pour fermer une modale en utilisant la touche échap. Non seulement c'est génial pour l'accessibilité, mais c'est aussi génial pour tout raccourci clavier utile !

### Comment piéger le focus à l'intérieur des composants dans React

**Attention :** Les deux prochaines démonstrations peuvent être buggées sur cette page car elles se disputent l'état de focus. Vous devriez soit n'avoir qu'une seule modale de démonstration ouverte à la fois, soit cliquer sur "Open Sandbox" pour les vérifier dans des fenêtres séparées pour une meilleure expérience.

Voici maintenant la mauvaise nouvelle concernant le composant modale ci-dessus : rien n'a obtenu le focus lorsque la modale a été ouverte. En réalité, le premier élément focalisable à l'intérieur de la modale devrait obtenir le focus et l'état de focus ne devrait jamais pouvoir s'échapper de la modale.

Nous allons résoudre ce problème en ajoutant un piège de focus via [React Focus Lock](https://github.com/theKashey/react-focus-lock#readme) à la modale. Le focus ne pourra pas s'échapper du piège de focus jusqu'à ce qu'il soit démonté et le premier élément focalisable sera automatiquement focalisé :

%[https://codesandbox.io/s/2-keyboard-accessible-modal-with-focus-trap-owxdt?from-embed]

Il existe de nombreuses dépendances différentes qui résoudront le piégeage du focus. Il est également assez facile de le mettre en œuvre dans des situations personnalisées. Vous devez penser à tout ce qui est nécessaire :

* Trouver le premier et le dernier élément focalisable avec l'interface utilisateur que vous souhaitez piéger
* Si l'utilisateur appuie sur tabulation tout en étant focalisé sur le dernier élément, focaliser le premier élément
* Si l'utilisateur appuie sur _shift_ + _tab_ tout en étant focalisé sur le premier élément, focaliser le dernier élément

### Comment passer le focus à d'autres composants

![Joueur de basket étiqueté 'A' passant un ballon de basket disant 'Focus' à un autre joueur](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fw30yo7xaqln9gtuxwds.jpeg)

Un autre problème courant que nous avons rencontré était de placer des composants avec des raccourcis clavier à l'intérieur d'autres composants qui utilisent les mêmes touches de raccourci. 

Par exemple, que faire si vous avez un menu déroulant à l'intérieur d'une modale ? Lorsque le menu déroulant est développé, la touche échap devrait fermer le menu déroulant, mais pas la modale. 

Nous pouvons mettre en pause les raccourcis de la modale avec un état de hook :

%[https://codesandbox.io/s/3-keyboard-accessible-modal-with-pausing-focus-trap-9lcfl?from-embed]

Il y a deux props importantes que nous avons incluses dans notre nouveau composant de menu de débordement : onClose et onOpen. Chaque fois que le menu est ouvert ou fermé, nous déclenchons la prop respective. Cela permet au composant modale de mettre en pause et de reprendre son propre piège de focus lorsque cela est nécessaire et de laisser le piège de focus du menu de débordement prendre le relais.

## Comment passer le focus à des composants pas encore montés

Il existe de grandes entreprises avec de grands organigrammes. Cela signifie que pour que notre expérience d'organigramme soit performante, nous devons faire beaucoup de chargement asynchrone de l'organigramme. Lorsque les utilisateurs développent les cartes des managers, nous chargeons alors plus de données dans l'organigramme.

Alors, comment passer le focus aux cartes qui n'existent pas encore ? Je détesterais ajouter un setTimeout pour retarder le déclenchement du transfert. Il serait génial si le focus savait où la carte allait être et pouvait la rencontrer là-bas lorsqu'elle est prête. 

Parlons de **polling**. C'est lorsque l'état d'un système externe est continuellement demandé. En développement web, nous utilisons couramment le polling pour que les applications web demandent au serveur si elles ont terminé avec un certain type de données. 

Nous pouvons également utiliser un exemple très simple de polling pour demander si la carte de l'organigramme qui a besoin de focus a été rendue :

```javascript
let polling = null;
let pollCount = 0;
polling = setInterval(() => {
 if (pollCount > 20) {
  clearInterval(polling)
  return;
 }

 const nodeInDOM = getNodeInDOM(node);

 if (nodeInDOM) {
  nodeInDOM.focus();
  clearInterval(polling);
  return;
 }

 pollCount =+ 1;
}, 100);

```

Maintenant, vous devez fournir votre propre identifiant de nœud et `getNodeInDOM`, mais c'est tout ce à quoi se résume le polling pour le focus. Nous vérifions toutes les dixièmes de seconde pendant jusqu'à deux secondes si la carte est apparue ou non. Pourriez-vous l'appeler un hack ? Bien sûr. Mais c'est un hack fiable.

![Joueur étiqueté 'composant B' lançant le ballon de basket là où le joueur étiqueté 'composant A' l'attrapera et le dunkera dans un panier.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/agqv4f8exxj6kktpfl1m.jpeg)

## Rendre le monde meilleur

J'ai eu la chance de participer à de nombreuses grandes versions chez [Pingboard](https://pingboard.com), mais celle-ci semble être la plus impactante. 

C'est génial de s'assurer que tout le monde peut utiliser les mêmes outils. Travailler sur une expérience plus ancienne nous a également formés à livrer de nouvelles expériences avec l'accessibilité à l'esprit.

J'espère que votre entreprise considère à la fois les ramifications éthiques et légales de laisser des expériences inaccessibles. 

Si vous avez besoin d'aide pour convaincre votre entreprise de la nécessité de l'accessibilité, j'ai [une présentation et un guide gratuits](https://seejamescode.com/how-to-align-your-team-on-the-need-for-accessibility) disponibles. N'hésitez pas à [me contacter sur Twitter](https://twitter.com/seejamescode) si vous avez des questions sur cet article !