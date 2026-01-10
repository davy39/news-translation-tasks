---
title: J'ai créé une application qui rend l'apprentissage des algorithmes et des structures
  de données bien plus amusant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-20T17:15:35.000Z'
originalURL: https://freecodecamp.org/news/i-built-an-app-that-makes-learning-algorithms-and-data-structures-way-more-fun-46fbb8afacaf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8NEXTT3SN0DQ9Di99WK_CA.png
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: J'ai créé une application qui rend l'apprentissage des algorithmes et des
  structures de données bien plus amusant
seo_desc: 'By peterWeinberg

  I’m a self-taught programmer. This means I’m constantly dealing with impostor syndrome.
  It’s not uncommon for me to feel like I’m inadequate, and at a disadvantage for
  grasping complex Computer Science concepts.

  I’ve never been any g...'
---

Par peterWeinberg

[Je suis un programmeur autodidacte](https://medium.freecodecamp.org/the-freecodecamp-alumni-network-a-homegrown-mentorship-network-for-fcc-alumni-529e4531c34f). Cela signifie que je dois constamment faire face au [syndrome de l'imposteur](https://guide.freecodecamp.org/working-in-tech/imposter-syndrome). Il n'est pas rare que je me sente inadéquat et désavantagé pour comprendre des concepts complexes en informatique.

Je n'ai jamais été très bon en maths. Et j'ai toujours associé de solides compétences en maths à la capacité naturelle de quelqu'un à exceller en programmation. J'ai l'impression de devoir travailler plus dur que les autres (ceux qui ont des compétences innées en maths) pour apprendre les mêmes concepts. Avec cette idée bien ancrée dans mon esprit, j'étais convaincu de ne jamais pouvoir apprendre des choses comme le parcours des arbres binaires de recherche, ou comment analyser mentalement des cauchemars récursifs comme le Mergesort.

Pourtant, avec un peu d'effort, j'ai réussi à me surprendre. Alors je voulais partager un peu comment j'ai fait, et les résultats tangibles de mes efforts. Comme toujours, avec l'espoir qu'il y ait des contributeurs prêts à aider !

Voici [CS-Playground-React](http://cs-playground-react.surge.sh/), un simple bac à sable JavaScript dans le navigateur pour apprendre et pratiquer les algorithmes et les structures de données.

Cette application de préparation aux entretiens, sans inscription, sauvegarde automatiquement votre progression, offre des solutions lorsque vous êtes bloqué, et regorge de [liens vers des articles utiles, des tutoriels et d'autres ressources](https://github.com/no-stack-dub-sack/cs-playground-react/blob/master/RESOURCES.md) pour rendre votre parcours beaucoup moins douloureux que le mien !

Permettez-moi de reconnaître d'emblée que cette application n'a rien de révolutionnaire. (Je sais que vous y pensiez !) Il existe de nombreuses applications qui enseignent des compétences similaires et vous permettent d'écrire et d'exécuter du code directement dans votre navigateur.

Mais CS Playground React vise à être extrêmement minimaliste et se concentre sur un ensemble très spécifique de sujets. De plus, ce n'est _pas_ censé être la prochaine grande chose. Construire cette application était simplement ma façon de rendre l'apprentissage de ces concepts amusant. Si elle finit par être une ressource précieuse pour ne serait-ce qu'une autre personne en cours de route, tant mieux.

L'application est toujours en cours de développement, et il reste beaucoup de terrain à couvrir en matière de contenu et de fonctionnalités potentielles. Donc, si vous connaissez un défi ou une structure de données intéressante que je n'ai pas couverte, ou si vous voyez quelque chose que vous pensez pouvoir améliorer, n'hésitez pas à [ouvrir une issue](https://github.com/no-stack-dub-sack/cs-playground-react/issues/new) ou à soumettre une pull request. ?

Si vous voulez simplement essayer l'application, ne lisez pas plus loin — elle est en ligne [ici](http://cs-playground-react.surge.sh) (également disponible en https, et enregistrera un service worker pour le cache hors ligne).

Si vous êtes intéressé par le code, [ne cherchez pas plus loin](https://github.com/no-stack-dub-sack/cs-playground-react).

Le reste est tout le truc ennuyeux sur le pourquoi et le comment :-)

### Pourquoi j'ai construit cela

Mes motivations pour construire cette application étaient simples : je voulais apprendre, et je voulais rendre l'apprentissage plus facile et plus amusant. Plus important encore, c'est pourquoi je voulais apprendre ces compétences spécifiques.

Au cours des 18 derniers mois, je peux dire en toute confiance que j'ai appris à coder. Bien que j'hésite encore à m'appeler programmeur. Et ce n'est pas parce que je ne code pas pour gagner ma vie (je ne le fais pas), mais plutôt à cause du phénomène du [syndrome de l'imposteur](https://en.wikipedia.org/wiki/Impostor_syndrome) dont j'ai parlé plus tôt. Je sais construire des choses, bien sûr. Mais jusqu'à très récemment, je savais très peu de choses sur l'informatique formelle.

En apprenant les fondamentaux de l'informatique, j'espérais non seulement me sentir plus confiant en me considérant comme un programmeur, mais aussi aider les autres à me voir ainsi.

Les programmeurs autodidactes sont une pilule que l'industrie technologique a trouvé plus facile à avaler ces dernières années. Surtout dans des régions comme la Silicon Valley, où les bootcamps de codage ont poussé à chaque coin de rue.

Pourtant, il reste un obstacle majeur à surmonter pour la plupart des programmeurs espérant entrer dans l'industrie sans une éducation formelle en informatique.

Alors, pour aider à atténuer le choc de détenir un baccalauréat ès arts plutôt qu'un baccalauréat ès sciences, je me suis lancé dans l'apprentissage de certains des concepts qu'un étudiant en première ou deuxième année d'informatique pourrait apprendre. Je pensais que cela compléterait certaines de mes compétences de développement plus pratiques, et aiderait les autres à me prendre plus au sérieux en tant que programmeur.

J'ai utilisé un ensemble de sujets connus pour être courants lors des entretiens de programmation comme base de ce que je voulais couvrir.

Tri à bulles, Tri par sélection, Tri par insertion, Tri fusion, Tri rapide, Tri par tas, Piles, Files d'attente, Listes chaînées, Tables de hachage et Arbres binaires de recherche. Phwewf...

J'étais super intimidé par cette liste de problèmes et j'avais repoussé leur résolution depuis un certain temps.

Refusant d'accepter la défaite, j'ai finalement commencé à creuser. Traquant des tutoriels, lisant chaque article que je pouvais trouver, et tournant en rond de confusion autour de moi jour après jour.

Avec le temps, cependant, certains des concepts commençaient à s'imprégner. Mais il y avait quelques problèmes :

1. **Je commençais à m'ennuyer un peu.** J'adore résoudre des problèmes, mais soyons réalistes, résoudre le parcours `reverseLevelOrder` d'un arbre binaire de recherche est beaucoup moins amusant que de résoudre un problème réel pour votre dernière application.
2. **Cela prenait _beaucoup_ de temps.** Je travaille à temps plein (sans écrire de code toute la journée) et mon temps libre pour coder est extrêmement précieux. Je savais que je passerais des mois sur cela, et j'ai commencé à m'inquiéter de perdre le contact avec mes compétences plus commercialisables.

Tout ce truc d'informatique est génial à avoir dans son bagage, mais soyons réalistes, nous, les développeurs web, sommes le plus souvent engagés pour construire des choses. Et il n'y a pas trop d'utilisations pratiques pour la plupart de ces concepts dans le développement web quotidien.

Pour moi, apprendre ces concepts était une question de fierté, et je n'allais pas abandonner. Mais ma priorité numéro un était toujours d'être compétent en développement web pratique.

J'ai donc décidé de réunir les deux idées. La solution était de construire une application simple qui m'aiderait à atteindre mes objectifs _et_ à rester bien pratiqué dans mes compétences de base.

Pour moi, la meilleure façon d'apprendre quelque chose (surtout quelque chose d'aride), c'est de le relier à quelque chose que vous aimez. Donc, alors que je construisais cette application et que je m'amusais beaucoup, je développis également du contenu pour elle.

Maintenant, apprendre les algorithmes et les structures de données faisait partie intégrante de mon dernier projet. Parce que, bien sûr, quel est l'intérêt de construire une application de préparation aux entretiens si vous n'allez pas la remplir de problèmes !

Tous les quelques jours, j'apprenais un nouvel algorithme ou une nouvelle structure de données. Une fois que je l'avais presque maîtrisé, je compilais les ressources d'apprentissage et l'ajoutais à l'application. Maintenant, je pouvais le pratiquer encore et encore dans un espace de travail super simple que j'avais construit moi-même. N'est-ce pas génial ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*LMKb4tY_71Nr3NuuPrlwQg.gif)
_Un site vraiment cool que j'ai trouvé qui visualise comment les algorithmes de tri et les structures de données fonctionnent. Voici Quicksort en action sur un tableau de 100 éléments. Vous pouvez trouver la liste complète des visualisations [ici](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html" rel="noopener" target="_blank" title="). Merci USF, c'est génial !_

Le point principal est que j'ai pris quelque chose que j'avais repoussé depuis longtemps, et j'ai trouvé un moyen de le rendre amusant. Et en effet, j'ai eu plus de succès à atteindre mes objectifs grâce à cela.

J'ai construit cette application pour moi, mais je voulais la partager avec vous tous pour une raison. Si même une autre personne trouve CS-Playground-React utile, j'aurai l'impression d'avoir fait ma part (ou au moins une partie) pour rendre à cette communauté.

Il y a tant de programmeurs qui partagent librement leurs connaissances et leurs expériences, et demandent peu ou rien en retour. Sans une communauté aussi ouverte d'esprit, apprendre à coder par soi-même serait à peine possible.

Il y a dix ans, il y avait beaucoup moins d'options en matière d'apprentissage autodirigé. Je suis donc reconnaissant chaque jour de vivre à une époque de l'information où tant de connaissances sont si facilement accessibles.

Cela a rendu ce voyage possible pour moi, et j'espère que quelqu'un d'autre tombera sur cet article et découvrira que son propre voyage est devenu un peu plus facile.

#### Pile technologique et astuces

Au cas où vous seriez intéressé, j'ai construit cette application avec React & React-Redux (bien que la [première version](https://github.com/no-stack-dub-sack/algos-and-data-structures) était en JavaScript, CSS et HTML vanilla). Elle utilise également [CodeMirror](https://codemirror.net/) et [React-Codemirror2](https://github.com/scniro/react-codemirror2) pour intégrer un éditeur dans le navigateur (NOTE : l'original React-CodeMirror n'est plus maintenu et ne fonctionne pas bien avec les versions plus récentes de React, alors allez donner une étoile au dépôt de [Scniro](https://github.com/scniro) sur GitHub pour avoir pris la relève !).

#### Console simulée

Une petite astuce me permet de déclencher une action Redux chaque fois qu'un utilisateur appelle `console.log` dans son code. De cette manière, je peux capturer les messages journalisés et à mon tour simuler une console dans le navigateur pour montrer la sortie du code — ce que je trouvais plutôt cool ! Vous pouvez exécuter `clearConsole()` à tout moment pour effacer les messages de la console simulée.

#### Persistance du code

Je voulais rendre cette application super facile à utiliser. Au lieu d'implémenter une base de données et de demander aux utilisateurs de se connecter, j'ai choisi une approche plus simple pour sauvegarder la progression. Redux gère l'état de l'application pendant chaque session, et j'utilise `localStorage` pour persister le code entre les sessions. L'application récupère cet état sauvegardé lors de votre prochaine visite et réhydrate le store Redux avec celui-ci. Ainsi, vous pouvez reprendre là où vous vous étiez arrêté.

Si pour une raison quelconque vous souhaitez effacer toute votre progression, vous pouvez exécuter `resetState()` à tout moment dans l'éditeur. Si vous ne souhaitez pas enregistrer votre code dans le stockage local, laissez un commentaire `// DO NOT SAVE` dans votre code avant de naviguer ailleurs. Cela empêchera l'enregistrement de tout code, non seulement pour ce fichier.

En aparté, il s'avère qu'il existe un package qui fait cela pour vous, appelé Redux-Persist (que j'ai découvert après coup). Mais pour un cas d'utilisation simple, si vous pouvez faire quelque chose avec quelques lignes de code, ou installer un package NPM pour faire la même chose ? Je choisirai toujours la première option. Il est probable que vous économisez des centaines de lignes de code et un tout nouvel ensemble de dépendances. C'est toujours un compromis, et vous devez décider quand la solution hautement optimisée (mais plus lourde) est meilleure que votre solution simpliste.

#### Panneaux redimensionnables

Le dernier tour que j'avais dans ma manche était de rendre l'espace de travail flexible et facile à utiliser. Je voulais donner aux utilisateurs la possibilité de redimensionner à la fois l'éditeur et la console, alors j'ai utilisé un petit script que j'ai trouvé appelé `[simpleDrag.js](https://github.com/lingtalfi/simpledrag)`, les `refs` de React, et la magie de flexbox pour rendre cela possible.

Merci de votre lecture, et bon codage !