---
title: Voici ce que j'ai appris à la plus grande conférence React au monde
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-24T16:39:19.000Z'
originalURL: https://freecodecamp.org/news/heres-what-i-learned-at-the-world-s-biggest-react-conference-6e97d0e8d1f8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ja7ihxQHNwiXqKuDNzxYRA.jpeg
tags:
- name: education
  slug: education
- name: React
  slug: react
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: Voici ce que j'ai appris à la plus grande conférence React au monde
seo_desc: 'By Jake Prins

  On Friday, April 13th, three colleagues and I from Inspire attended the biggest
  React conference in the world: React Amsterdam. Together with 1200 frontend and
  full stack developers from across the globe, we gathered in the tech heart o...'
---

Par Jake Prins

Le vendredi 13 avril, trois collègues et moi-même de [Inspire](https://www.inspire.nl/) avons assisté à la plus grande conférence React au monde : [React Amsterdam](https://react.amsterdam/). Avec 1200 développeurs frontend et full stack du monde entier, nous nous sommes réunis dans le cœur technologique de l'Europe pour un événement avec plus de 25 intervenants.

Permettez-moi de vous raconter cinq choses que j'ai apprises lors d'une journée remplie de grandes conférences, de beaucoup de café et, bien sûr, de quelques bières.

#### 1. Programmation réactive

Il y aura toujours un nouveau framework JavaScript à apprendre. La technologie continuera d'évoluer et de changer, et les développeurs continueront de réécrire des applications. [Tracy Lee](https://twitter.com/ladyleet) a parlé de la programmation réactive, qui peut vous permettre de simplement copier-coller la plupart de votre code d'un framework à un autre.

Dans sa conférence, Tracy a montré pourquoi la programmation réactive peut être une manière plus efficace de coder. Elle a également discuté de la manière dont elle a été adoptée par des leaders de l'industrie tels que Netflix, Slack, Microsoft et Facebook comme nouvelle norme pour le développement d'applications. Cela semble très prometteur, en particulier des bibliothèques comme RxJS, qui aident les développeurs à livrer des fonctionnalités complexes plus rapidement avec moins de code, plus maintenable.

Plus les développeurs adoptent ce concept, mieux c'est.

Comme Tracy l'a mentionné dans son article de blog :

> « Plus les gens comprennent la programmation réactive, plus nous serons tous productifs en tant qu'un seul web moderne. Le seul obstacle à l'adoption est de ne pas comprendre le paradigme et le langage qui l'entoure. »

Je pense que ce n'est pas une mauvaise idée d'investir un peu de temps pour apprendre la programmation réactive, et RxJS pourrait être une excellente bibliothèque pour commencer.

Regardez la conférence complète [ici](https://www.youtube.com/watch?v=smBND2pwdUE&feature=youtu.be&t=23m9s).

#### 2. React Navigation

Lors de l'implémentation de la navigation dans votre application React Native, vous avez deux options : vous pouvez utiliser une bibliothèque qui enveloppe les API de navigation natives pour la plateforme, ou vous pouvez utiliser une réimplémentation de ces API en utilisant les mêmes primitives React Native que vous utilisez dans toute votre application. [Brent Vatne](https://twitter.com/notbrent), qui travaille chez Expo, a donné une belle conférence sur un projet open source sur lequel il travaille : [React Navigation](https://reactnavigation.org/).

En nous fournissant un aperçu clair de la manière dont vous pouvez utiliser différents types comme les navigateurs switch ou stack dans votre application, Brent nous a donné une meilleure compréhension de la manière dont la navigation fonctionne. Il a également montré comment faire de superbes transitions avec la bibliothèque React Navigation.

En outre, Brent a mentionné quelques bonnes raisons de choisir une « navigation basée sur JavaScript » plutôt qu'une « navigation basée sur le natif ». Pour apprendre à en tirer pleinement parti, je recommande de lire la documentation de la bibliothèque React Navigation ou de consulter [cet article](https://medium.com/@christian.falch/fluid-transitions-with-react-navigation-a049d2f71494) de Christian Falch sur les transitions fluides avec React Navigation.

Regardez la conférence complète [ici](https://www.youtube.com/watch?v=N-X3Z5A-pW4&feature=youtu.be&t=40m5s).

![Image](https://cdn-media-1.freecodecamp.org/images/chEvig54HuWfmM-UQZ1I9oUgkiFBkV5b4UPm)
_[https://github.com/fram-x/fluidtransitions](https://github.com/fram-x/fluidtransitions" rel="noopener" target="_blank" title=")_

#### 3. D3 et React, ensemble

L'une des conférences les plus impressionnantes de la journée portait sur D3 et React, par [Shirley Wu](https://twitter.com/sxywu). D3 est une bibliothèque pour construire des visualisations de données, et elle peut fonctionner avec React. Le défi de l'intégration de D3 avec React est que React et D3 veulent tous deux contrôler le DOM. Principalement en laissant D3 faire tous les calculs et React faire tout le rendu, Shirley nous a montré comment gérer ce défi et pourquoi D3 et React peuvent fonctionner ensemble.

Elle a également démontré [ce projet](https://pudding.cool/2017/03/hamilton/) qui vaut le coup d'œil. Terminer la conférence avec un peu de codage en direct devant une grande foule a montré pourquoi Shirley Wu est la vraie affaire, et cela a fait de cette conférence l'une des plus intéressantes de la journée.

Lisez plus sur ce sujet dans [son article de blog](https://medium.com/@sxywu/on-d3-react-and-a-little-bit-of-flux-88a226f328f3) ou regardez la conférence complète [ici](https://www.youtube.com/watch?v=smBND2pwdUE&feature=youtu.be&t=2h36m).

#### 4. React Native VR + AR rendu simple

L'écosystème React a donné aux développeurs l'opportunité de cibler des plateformes qui étaient autrefois considérées comme hors de portée pour les développeurs JavaScript. [Nader Dabit](https://twitter.com/dabit3) a donné une belle conférence sur la plateforme [Viro](https://viromedia.com/) qui ouvre la porte au développement de la réalité augmentée et de la réalité virtuelle.

Créer votre propre application AR avec React Native est en fait assez simple et direct si vous utilisez [Viro React](https://github.com/viromedia/viro). Cela vous permet de créer des applications amusantes comme l'application de démonstration de Nader, qui permettait aux utilisateurs de télécharger des photos prises lors de la conférence dans une salle virtuelle, ainsi que de se promener et d'interagir avec elles en AR.

Bien que cette technologie puisse être amusante à expérimenter, je ne peux pas m'imaginer l'utiliser pour des implémentations utiles. Je pense également que la plupart des développeurs AR et VR professionnels ne construisent probablement pas leurs projets avec React Native. Mais si vous avez le temps et une bonne dose de créativité, vous pourriez vouloir essayer Viro.

Regardez la conférence complète [ici](https://www.youtube.com/watch?v=N-X3Z5A-pW4&feature=youtu.be&t=2h08m30s).

![Image](https://cdn-media-1.freecodecamp.org/images/6YBHlbXVzbuVRnGkAjDxGMSBRrv-zoplUg1f)
_[https://github.com/viromedia/viro](https://github.com/viromedia/viro" rel="noopener" target="_blank" title=")_

#### 5. Gestion d'état React à l'ère de GraphQL

Enfin, mais non des moindres, je veux mentionner la grande présentation de [Kristijan Ristovski](https://twitter.com/thekitze), également connu sous le nom de Kitze. Il a parlé de la (non)nécessité des bibliothèques de gestion d'état lorsque GraphQL s'occupe de gérer les données dans nos applications.

GraphQL est un langage de requête de données bien documenté qui fournit une alternative à REST et aux architectures de services web ad-hoc. Il vous permet de retourner des résultats de données complexes via un seul appel d'API.

Ou comme Kitze l'a dit :

> « GraphQL est la chose qui va finalement remplacer REST, mais vous continuez à vous dire que vous n'avez pas besoin de l'apprendre. »

Kitze a ouvert sa conférence agréable avec une explication amusante de pourquoi les termes « Rockstar- », « Senior- » ou « Ninja- » développeur sont si stupides, ce qui a montré qu'il avait plus à dire que simplement à quel point GraphQL est génial.

Il a exploré toutes les possibilités et comparé les combinaisons de React, Apollo, Redux, MobX et Next.js. Mais au lieu de simplement vanter tous ces projets géniaux, il est resté réaliste et a parlé des cas d'utilisation pratiques.

Par exemple, Redux, un concept brillant qui est (sur)utilisé par de nombreux développeurs React. Même le créateur de Redux a dit :

> « C'est définitivement surestimé, de bas niveau et souvent utilisé inutilement. »

Vous pouvez lire plus à ce sujet de la part du créateur de Redux dans son propre article de blog, [You Might Not Need Redux](https://medium.com/@dan_abramov/you-might-not-need-redux-be46360cf367).

Kitze a continué et a montré une simple question que quelqu'un a posée sur Reddit : _« Bonjour Reddit, je viens de commencer ma première application React. Que devrais-je utiliser pour faire des requêtes réseau ? »_ La réponse la plus votée ? _« Utilisez simplement redux-saga. »_ Qui dit JUSTE utiliser redux-saga ? Comme Kitze l'a dit, c'est comme avoir un ami qui vous dit qu'il y a un bug dans sa maison et vous lui dites d'utiliser un bazooka.

Le monde du frontend évolue très rapidement, et les batailles des différentes technologies continueront pour toujours. Mais le problème est que nous demandons « Qu'est-ce qui est mieux ? » au lieu de :

* Qu'est-ce qui convient à mon application ?
* Qu'est-ce qui convient à mon équipe ?
* Qu'est-ce qui convient à notre cas d'utilisation ?

Kitze a terminé sa conférence avec la question « Avons-nous même besoin d'une bibliothèque de gestion d'état lorsque nous utilisons GraphQL ? » La réponse : peut-être.

Tout dépend de votre projet. Si vous voulez des conseils un peu plus spécifiques, je recommande de regarder la conférence complète pour quelques exemples.

![Image](https://cdn-media-1.freecodecamp.org/images/NV-jARGXYZtHo4kIN2tQBAYTbbzPQDGIWDzd)
_Passer de Redux à React Apollo ([https://dev-blog.apollodata.com/reducing-our-redux-code-with-react-apollo-5091b9de9c2a](https://dev-blog.apollodata.com/reducing-our-redux-code-with-react-apollo-5091b9de9c2a" rel="noopener" target="_blank" title="))_

Les seules choses restantes à mentionner sur la conférence de Kitze sont ces simples conseils :

* Arrêtez de chercher l'approbation externe.
* Arrêtez de chercher des réponses aux projets des autres.
* Arrêtez de vous sentir insécure à propos de votre code, car aujourd'hui personne ne sait vraiment ce qu'il fait.
* Pour l'amour de Dieu : supprimez votre compte Twitter.

Regardez la conférence complète [ici](https://www.youtube.com/watch?v=smBND2pwdUE&feature=youtu.be&t=5h2m44s).

#### Réflexions finales

Bien qu'il y ait eu beaucoup plus de présentations intéressantes en plus des cinq conférences que j'ai mentionnées, toutes n'étaient pas aussi engageantes et intéressantes. Toutes les conférences n'étaient pas aussi approfondies que nous l'espérions, et montrer beaucoup de documentation qui peut facilement être trouvée en ligne ne conviendra pas à tout le monde.

En dehors de cela, la plupart des intervenants ont démontré à quel point ils sont passionnés et l'expérience globale était géniale !

React Amsterdam est une conférence bien organisée qui offrait beaucoup à apprendre. Espérons que cet article vous a donné un aperçu de quelques sujets intéressants que vous pourriez vouloir approfondir.

Merci d'avoir lu ! J'espère que les informations étaient utiles. Suivez-moi sur Medium pour plus d'articles liés à la technologie ou sur Twitter et Instagram @jakeprins_nl.