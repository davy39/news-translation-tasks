---
title: Si vous voulez construire une cabane dans l'arbre (ou une application logicielle)
  sécurisée, commencez par le bas
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-05-17T20:52:28.000Z'
originalURL: https://freecodecamp.org/news/if-you-want-to-build-a-treehouse-start-at-the-bottom
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/cover.png
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: 'development process '
  slug: development-process
- name: information security
  slug: information-security
- name: threat modeling
  slug: threat-modeling
seo_title: Si vous voulez construire une cabane dans l'arbre (ou une application logicielle)
  sécurisée, commencez par le bas
seo_desc: "If you’ve ever watched a kid draw a treehouse, you have some idea of how\
  \ applications are built when security isn’t made a priority. \nIt’s far more fun\
  \ to draw the tire swing, front porch, and swimming pool than to worry about how\
  \ a ten-thousand-gall..."
---

Si vous avez déjà vu un enfant dessiner une cabane dans l'arbre, vous avez une idée de la façon dont les applications sont construites lorsque la sécurité n'est pas une priorité. 

Il est bien plus amusant de dessiner la balançoire, le porche et la piscine que de se soucier de la façon dont un seau de dix mille gallons d'eau reste suspendu en plein air. 

Avec trop d'attention portée aux fonctionnalités amusantes et tape-à-l'œil, les fondations en souffrent.

![Une bande dessinée que j'ai dessinée sur la construction de châteaux avec de mauvaises fondations. Ce n'est pas si drôle.](https://victoria.dev/blog/if-you-want-to-build-a-treehouse-start-at-the-bottom/for-the-turrets.png)
_Une bande dessinée que j'ai dessinée sur la construction de fondations stables. Ce n'est pas si drôle._

Bien sûr, passer des heures excessives à construire un back-end comme Fort Knox peut ne pas être nécessaire pour votre application non plus. Être un défenseur de la sécurité ne signifie pas toujours porter votre chapeau en papier aluminium (bien que vous ayez l'air élégant avec), mais cela signifie construire une quantité appropriée de sécurité.

Combien de sécurité est approprié ? La réponse, frustrante, est : « cela dépend ». La bonne quantité de sécurité pour votre application dépend de qui l'utilise, de ce qu'elle fait et, surtout, des choses indésirables qu'elle pourrait être amenée à faire. 

Il faut une certaine analyse pour prendre des décisions sur les types de risques auxquels votre application est confrontée et sur la manière dont vous allez vous préparer à les gérer. D'accord, c'est le bon moment pour mettre votre chapeau en papier aluminium. Imaginons le pire.

## Modélisation des menaces : quel est le pire qui pourrait arriver ?

Un _modèle de menace_ est un terme pompeux pour le résultat de l'imagination des pires choses qui pourraient arriver à une application. Utiliser votre imagination pour évaluer les risques (appelé de manière appropriée _évaluation des risques_) est une méthode commodément non destructive pour trouver des moyens par lesquels une application peut être attaquée. 

Vous n'aurez besoin d'aucun outil – juste une compréhension de la façon dont l'application pourrait fonctionner et un peu d'imagination. Vous voudrez enregistrer vos résultats avec un stylo et du papier. Pour les jeunes, cela signifie l'application de notes sur votre téléphone.

Plusieurs méthodologies différentes pour l'évaluation des risques des applications peuvent être trouvées dans le monde du logiciel, y compris le [NIST Special Publication 800-30](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final) détaillé. Chaque cadre de méthode a des étapes et des résultats spécifiques, et entrera dans divers niveaux de détail lorsqu'il s'agit de définir les menaces. 

Si vous suivez un cadre, choisissez d'abord celui que vous êtes le plus susceptible de compléter. Vous pouvez toujours ajouter plus de profondeur et de détail à partir de là.

Même les évaluations de risques informelles sont bénéfiques. Prenant généralement la forme d'un ensemble de questions, elles peuvent être orientées autour des menaces possibles, de l'impact sur les actifs ou des moyens par lesquels une vulnérabilité pourrait être exploitée. 

Voici quelques exemples de questions abordant chaque orientation :

* Quel type d'adversaire voudrait pirater mon application ? Que chercheraient-ils ?
* Si le contrôle de _x_ tombait entre de mauvaises mains, que pourrait faire un attaquant avec ?
* Où une vulnérabilité de _x_ pourrait-elle se produire dans mon application ?

Un modèle de menace de base explique les considérations techniques, commerciales et humaines pour chaque risque. Il détaillera généralement :

* Les vulnérabilités ou composants qui peuvent causer le risque
* L'impact qu'une exécution réussie du risque aurait sur l'application
* Les conséquences pour les utilisateurs ou l'organisation de l'application

Le résultat d'un exercice d'évaluation des risques est votre modèle de menace. En d'autres termes, c'est une liste de choses que vous aimeriez beaucoup ne pas voir se produire. 

Il est généralement classé dans une hiérarchie de risques, du pire au plus léger. Les pires risques ont l'impact le plus négatif et sont les plus importants à protéger. Les risques les plus légers sont les plus acceptables — bien qu'ils soient toujours un résultat indésirable, ils ont le moins d'impact négatif sur l'application et les utilisateurs.

Vous pouvez utiliser cette hiérarchie résultante comme guide pour déterminer combien de vos efforts de cybersécurité appliquer à chaque domaine de risque. Une quantité appropriée de sécurité pour votre application éliminera (lorsque cela est possible) ou atténuera les pires risques.

## Pousser à gauche

Bien que cela ressemble à un mème de mouvement de danse, _pousser à gauche_ fait plutôt référence à l'intégration de la plus grande partie possible de votre sécurité planifiée dès les premières étapes du développement logiciel.

Construire un logiciel ressemble beaucoup à construire une cabane dans l'arbre, juste sans l'air frais agréable. Vous commencez avec les composants de support de base, comme attacher une plateforme à un arbre. Ensuite viennent le cadre, les murs et le toit, et enfin, vos suspensions murales rustiques-modernes dignes d'Instagram et votre buste de cerf.

Plus vous avancez dans le processus de construction, plus il devient difficile et coûteux d'apporter des modifications à un composant que vous avez déjà installé. 

Si vous découvrez un problème avec les murs seulement après que le toit soit mis en place, vous devrez peut-être changer ou retirer le toit afin de le réparer. Des parallèles similaires peuvent être tirés pour les composants logiciels, mais sans la même facilité à démêler les parties attachées.

Dans le cas d'une cabane dans l'arbre, il est plutôt impossible de commencer par les décorations ou même un toit, puisque vous ne pouvez pas vraiment les suspendre en plein air. 

Dans le cas du développement logiciel, il est malheureusement possible de construire de nombreux composants et abstractions de couche supérieure sans une architecture de support suffisante. 

Une approche de poussée à gauche considère chaque couche supplémentaire comme ajoutant des coûts et des complications. Pousser à gauche signifie tenter de mitiger les risques de sécurité autant que possible à chaque étape du développement avant de passer à la suivante.

## Construire de bas en haut

En considérant votre modèle de menace dès les premières étapes du développement de votre application, vous réduisez les chances de nécessiter une coûteuse rénovation plus tard. Vous pouvez faire des choix concernant l'architecture, les composants et le code qui soutiennent les principaux objectifs de sécurité de votre application particulière.

Bien qu'il ne soit pas possible de prévoir toute la fonctionnalité que votre application pourrait un jour devoir supporter, il est possible de préparer une fondation solide qui permet d'ajouter des fonctionnalités supplémentaires de manière plus sécurisée. Construire une sécurité appropriée de bas en haut aidera à rendre la mitigation des risques de sécurité beaucoup plus facile à l'avenir.