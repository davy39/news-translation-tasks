---
title: Comment devenir un développeur web Full Stack – Guide pour débutants
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-02-05T01:34:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-become-a-full-stack-web-developer-in-2020
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/How-to-Become-a-Full-Stack-Web-Developer-Book-Cover--1-.png
tags:
- name: full stack
  slug: full-stack
- name: JAMstack
  slug: jamstack
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment devenir un développeur web Full Stack – Guide pour débutants
seo_desc: 'Full stack web developers are the Swiss Army knife of the code world. Having
  that designation means you can produce end to end solutions, which is a highly marketable
  and agile skillset. But what does it actually take to achieve that status?

  Whether ...'
---

Les développeurs web full stack sont les couteaux suisses du monde du code. Avoir cette désignation signifie que vous pouvez produire des solutions de bout en bout, ce qui est une compétence très commercialisable et agile. Mais que faut-il vraiment pour atteindre ce statut ?

Que vous soyez nouveau, expérimenté ou spécialisé dans une extrémité de la stack, il y a beaucoup à digérer ici. N'hésitez pas à plonger dès le début ou à sauter là où vous avez le plus besoin de soutien.

* [Tout d'abord, qu'est-ce qui fait vraiment d'un développeur un full stack ?](#heading-qu-est-ce-qui-fait-reellement-d-un-developpeur-un-full-stack)
* [Avant de plonger, parlons de cette concentration](#heading-avant-de-plonger-parlons-de-cette-concentration)
* [Alors, par où commencer ?](#heading-alors-par-ou-commencer)
* [Front End](#heading-front-end)
* [Back End](#heading-back-end)
* [DevOps et le cloud](#heading-devops-et-le-cloud)
* [Et le design ?](#heading-et-le-design)
* [Autres choses si vous débutez](#heading-autres-choses-si-vous-debutez)
* [Autres choses si vous cherchez plus](#heading-autres-choses-si-vous-cherchez-plus)

## Tout d'abord, qu'est-ce qui fait vraiment d'un développeur un full stack ?

C'est amusant et à la mode de dire que [tout développeur front end est un développeur full stack](https://full-stack.netlify.com/), mais être capable de déployer un site web sur [Netlify](https://www.netlify.com/) ne fait pas de vous un full stack.

Ce n'est pas pour être décourageant – simplement, réalistement, avoir uniquement cette expérience ne tiendra pas bien face à ce titre de poste lors de votre prochain entretien. Bien que vous créiez et déployiez techniquement votre travail de bout en bout, Netlify, [Zeit](https://zeit.co/), et d'autres fournisseurs vous donnent le pouvoir de le faire avec leurs outils magiques qui retirent la majorité du travail des opérations de la stack de l'équation.

Ce n'est pas pour enlever ce que nous sommes tous capables d'accomplir maintenant en tant que développeurs front end. Le mouvement croissant pour compiler et déployer des sites web statiques a simplement rendu ce processus plus simple sur la deuxième moitié de la stack avec des avantages à tous les niveaux.

De plus, avec la flexibilité des options d'outils comme la possibilité d'exécuter JS sur un serveur, nos compétences sont capables de s'adapter à plus de cas d'utilisation que jamais auparavant.

### D'où nous venons

Le paysage du développement web a changé rapidement. [Wordpress](https://wordpress.org/) a été le roi des CMS pendant un certain temps maintenant, représentant plus d'un tiers des sites web qui utilisent un CMS et aidant PHP à gagner en popularité. Mais d'autres ont travaillé sur des solutions maison.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/wordpress-cms-share.jpg)
_[https://trends.builtwith.com/cms](https://trends.builtwith.com/cms)_

Celles-ci représentaient une stack web plus traditionnelle comme [LAMP](https://en.wikipedia.org/wiki/LAMP_(software_bundle)). Dans ces cas, vous aviez des serveurs web exécutant généralement un type de système de gestion de contenu et un langage côté serveur (comme PHP) qui interfacerait avec les bases de données et produirait le code qui serait finalement livré au navigateur.

En plus de cela, vous pourriez avoir Javascript créant des fonctionnalités interactives avec CSS gérant l'affichage de la page. Maintenant, dans certains cas, avoir un serveur Wordpress géré est tout ce dont vous avez besoin pour certains hébergeurs web. Mais d'autres sites plus grands nécessiteraient une autre équipe pour gérer ces services et le pipeline de déploiement pour mettre le code en production.

### Où nous en sommes et où nous allons

Bien que [Wordpress ne parte pas](https://trends.builtwith.com/cms/WordPress), les architectures [serverless](https://aws.amazon.com/serverless/) et [JAMstack](https://jamstack.org/) prennent de l'essor. Pour ceux qui ne sont pas familiers, l'idée n'est pas qu'il n'y ait littéralement aucun serveur, mais il s'agit davantage d'utiliser des serveurs qui sont gérés pour vous dans le cloud.

Des services comme [AWS Lambda](https://aws.amazon.com/lambda/) vous permettent de créer une "fonction" qui traite des entrées et sorties simples. Attachez cela à [API Gateway](https://aws.amazon.com/api-gateway/) et vous avez immédiatement un endpoint avec lequel vous pouvez interagir sans jamais avoir à gérer réellement un serveur.

D'autres comme [S3](https://aws.amazon.com/s3/) vous permettent de déposer du HTML, du CSS, du JS, des images et tout autre actif statique dans le stockage et de servir le site directement à partir de celui-ci. Rien n'est traité sur le serveur, vous servez simplement les fichiers statiques au client.

Le côté brillant de cela est qu'il y a beaucoup moins de frais généraux et c'est généralement beaucoup moins cher. Dans de nombreux cas, vous obtiendrez également un énorme gain de performance, où servir un site à partir de s3 nécessitera moins de traitement pour obtenir cette [première réponse au navigateur](https://developers.google.com/web/tools/lighthouse/audits/ttfb), ce qui peut directement équivaloir à une expérience utilisateur améliorée.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/brett-rambo-thumbs-up.gif)
_Pouce levé pour une bonne expérience utilisateur !_

Ce n'est pas pour vous pousser vers le JAMstack, mais pour montrer que le paradigme full stack est en train de changer et que c'est quelque chose qui vaut la peine d'être examiné. Il existe encore un sens traditionnel de la différence dans le travail, mais cela devient un peu différent.

Les équipes DevOps gèrent désormais les ressources cloud et les déploiements. Les développeurs backend créent désormais des API et du code qui interfacent avec des services en utilisant des outils comme les fonctions lambda. Et les développeurs front end travaillent principalement en Javascript en créant des applications [React](https://reactjs.org/) ou [Vue](https://vuejs.org/) qui se connectent aux services créés par vos développeurs backend. Arguablement, cela pourrait ou non inclure des choses comme CSS, mais c'est une autre boîte de vers sur le titre officiel sous lequel ce travail tombe (spoiler : cela dépend de l'équipe).

Bien qu'il y ait encore une séparation des responsabilités, la ligne s'estompe et rend plus facile la répartition de votre concentration.

## Avant de plonger, parlons de cette concentration

Il peut être assez tentant de vouloir plonger directement et couvrir tout le spectre d'un développeur full stack, mais il y a quelque chose à dire sur la concentration. C'est la base de l'expression "[jack of all trades, master of none](https://en.wikipedia.org/wiki/Jack_of_all_trades,_master_of_none)", où vous essayez d'apprendre un peu de chaque partie de la stack complète et ne maîtrisez jamais vraiment rien.

Cela peut être dangereux lorsque vous commencez à essayer de construire vos forces en tant que nouveau développeur. Essayez donc d'évaluer quel type d'apprenant vous êtes et concentrez-vous là où cela compte. Si vous avez du mal avec un programme d'études étalé, cela ne vous aidera pas nécessairement à obtenir l'expérience dont vous avez besoin pour décrocher ce premier emploi ou cet emploi de rêve que vous visez.

Une approche novatrice, par exemple, pourrait être d'avoir une concentration individuelle, mais de construire les compétences full stack autour de cette force. Cela pourrait être un développeur front end qui peut déployer ses propres applications web et continuer à construire sur cette connaissance fondamentale.

En plus de cela, faire partie d'un développeur full stack ne consiste pas nécessairement à pouvoir dire que vous connaissez les langages x, y et z. Comprendre le code et les concepts de conception de logiciels ainsi que pouvoir relever n'importe quel défi à portée de main, stack mise à part, est ce qui fait un grand développeur.

En résumé, essayez de déterminer ce qui est le mieux pour vous et ne laissez pas votre haute ambition entraver la maîtrise de votre parcours.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/mr-miyagi-approves.gif)
_M. Miyagi approuve_

## Alors, par où commencer ?

Aux fins de cet article, nous allons nous en tenir aux points de rupture traditionnels de ce qui divise la stack (front end, back end, etc.). Bien que [certaines personnes disent que ce n'est plus vraiment une chose](https://medium.com/better-programming/2020-001-full-stack-pronounced-dead-355d7f78e733), réalistement, il y a des tonnes d'emplois pour les développeurs full stack et au quotidien, ils se réfèrent aux points de rupture traditionnels. "Développeur full stack" ne va définitivement nulle part.

En ce qui concerne la stack, nous allons nous appuyer sur les architectures serverless / JAMstack, car cela ne va faire que croître. Et si vous les apprenez, cela ne fera que vous rendre plus commercialisable avec le nombre d'emplois qui apparaissent autour.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/boomshakalaka.gif)
_Boomshakalaka !_

Comme vous le remarquerez ci-dessous, cela n'est pas censé être exhaustif avec chaque type de base de données et chaque type de solution de rendu. Un développeur solide devrait être capable d'être flexible avec ses outils, cherchant à comprendre les concepts de son travail plutôt que d'être borné et de ne pouvoir être productif que dans un seul framework.

Bien que vous puissiez travailler dans React et être à l'aise avec cela dans votre travail actuel (c'est bien !), votre prochain emploi pourrait être lourd sur Vue ou "surprise !" votre chef d'équipe veut réécrire l'application en [Svelte](https://svelte.dev/). Essayez de comprendre pourquoi vous utilisez un framework UI en premier lieu et comment il vous aide à résoudre le problème à portée de main.

Maintenant, plongeons-nous dedans...

## Front End

Le front end d'un site web ou d'une application est généralement l'UI avec laquelle la personne utilisant votre service interagit. Le plus grand langage dans le jeu est Javascript, où vous vous appuierez généralement sur des bibliothèques UI telles que React ou Vue pour gérer les composants de votre projet.

L'utilisation de ces frameworks UI vous permettra de créer des "composants", essentiellement des blocs de code, qui finiront par produire du HTML avec la capacité de créer des interactions et des états dynamiques directement avec votre code. Cela devient vraiment puissant, et bien qu'il puisse y avoir une petite courbe au début, cela devient assez agréable à travailler une fois que vous en avez l'habitude.

Que vous soyez nouveau dans le domaine ou bien expérimenté, vous pourriez éventuellement rencontrer jQuery. Bien qu'il ait ses mérites et ait bien servi la communauté, les fonctionnalités natives de Javascript ont vraiment évolué et créé moins de demande pour la fonctionnalité que jQuery était capable de fournir. Maintenant, les développeurs s'appuient sur les frameworks UI et le Javascript natif.

Il est donc bon de comprendre ce qu'est jQuery, mais je ne recommande pas de prendre le temps de l'apprendre à ce stade. La bonne chose est que si vous décrochez un emploi qui l'utilise, vous pouvez écrire du Javascript natif directement avec jQuery, donc apprendre le Javascript vanilla lui-même est la bonne réponse.

### Alors, que devrais-je apprendre ?

Si vous êtes vraiment débutant, prenez le temps d'apprendre le HTML et le CSS de base. Cela peut ne pas être aussi amusant et attrayant que de plonger directement dans Javascript, mais [construire sur les fondamentaux](https://www.freecodecamp.org/news/put-down-the-javascript-learn-html-css/) de ce qui fait le web sera la clé pour bien commencer.

Ensuite, apprenez Javascript. Il restera roi dans un avenir prévisible. Javascript fournira la base de tout framework ou bibliothèque que vous construisez, donc comprendre comment les bits et morceaux du langage lui-même fonctionnent vous aidera à propulser votre voyage d'apprentissage du côté front end des choses.

Cela facilitera également votre vie lorsque vous essayez de comprendre certaines des complexités des différents modèles et des [concepts derrière les frameworks](https://reactjs.org/docs/getting-started.html#javascript-resources) que vous utiliserez.

En parlant de frameworks, React et Vue sont probablement les meilleurs candidats étant donné leur popularité. React est le plus populaire de la bande et ne va faire que croître. Son équipe travaille constamment à faire mûrir le framework et à produire des API qui aideront à construire des applications web modernes et rapides.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/front-end-framework-usage.jpg)
_[2019 State of JS Frameworks](https://2019.stateofjs.com/front-end-frameworks/#front_end_frameworks_section_overview)_

Commencer avec [Create React App](https://github.com/facebook/create-react-app) ou [Gatsby](https://www.gatsbyjs.org/) vous aidera même à lancer facilement une application React et à vous mettre immédiatement dans une position où vous pouvez bidouiller dans le code.

Bien qu'il y aurait des avantages à mentionner les préprocesseurs CSS et les outils comme Sass, il existe une tonne de solutions maintenant pour CSS incluant [CSS-in-JS](https://cssinjs.org/).

Bien que mettre CSS à l'intérieur de JS ait quelques [avantages et inconvénients](https://www.freecodecamp.org/news/you-dont-need-css-in-js-why-i-use-stylesheets/), il n'est pas nécessairement utile de pointer ce qu'il faut utiliser comme direction particulière, car cela dépendra vraiment de l'équipe.

Comprendre les bases et la puissance de CSS et comment l'utiliser dans sa forme vanilla vous aidera à vous préparer à l'utiliser quel que soit le framework.

### Ressources

* Certification Responsive Web Design de freecodecamp.org [https://www.freecodecamp.org/learn](https://www.freecodecamp.org/learn)
* "Posez le Javascript : apprenez d'abord HTML & CSS" [https://www.freecodecamp.org/news/put-down-the-javascript-learn-html-css/](https://www.freecodecamp.org/news/put-down-the-javascript-learn-html-css/)
* Introduction à Javascript de MDN [https://developer.mozilla.org/fr/docs/Web/JavaScript/A_re-introduction_to_JavaScript](https://developer.mozilla.org/fr/docs/Web/JavaScript/A_re-introduction_to_JavaScript)
* Cours par email Just Javascript [https://justjavascript.com/](https://justjavascript.com/)
* Jeu d'apprentissage JSRobot [https://lab.reaal.me/jsrobot/](https://lab.reaal.me/jsrobot/)
* Introduction à React de reactjs.org [https://reactjs.org/tutorial/tutorial.html](https://reactjs.org/tutorial/tutorial.html)
* Tutoriels de gatsbyjs.org [https://www.gatsbyjs.org/tutorial/](https://www.gatsbyjs.org/tutorial/)

## Back End

Dans le monde JAMstack, le back end fera généralement référence aux API que nos fronts utilisent pour créer des expériences dynamiques en interagissant avec des endpoints depuis le client (comme ceux dans les API [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)). Être capable de faire ces requêtes depuis le client éliminera le besoin de faire ce traitement avant que la page ne soit servie au navigateur.

Bien que vous ne devriez pas avoir l'impression de ne pouvoir coder qu'en un seul langage, être capable d'écrire en Javascript donne un bel avantage ici, car vous pouvez vous développer dans les fondamentaux du travail avec le côté back end des choses avec un langage familier (ou vice versa avec le front end).

[NodeJS](https://nodejs.org/en/) est un runtime commun que vous trouverez dans la plupart des environnements cloud comme option et vous donnera une expérience similaire à ce à quoi vous vous attendez dans un navigateur. La principale différence est que vous n'aurez pas accès à certaines API de navigateur et qu'il n'y aura pas d'objet `window` et les API qui y sont associées.

Cela dit, Python est également [un autre langage populaire](https://pypl.github.io/PYPL.html) et est en croissance, surtout étant donné sa popularité dans la communauté de la science des données et de l'ingénierie. PHP et Ruby, bien que valides et vous donneront des options sur le marché de l'emploi, ne semblent pas être aussi populaires et pas autant en tendance à la hausse que Javascript et Python.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/language-popularity.jpg)
_[Langages populaires sur Github](https://madnight.github.io/githut/#/pull_requests/2019/4)_

Avec le langage de votre choix, votre meilleur pari sera d'apprendre à créer des services cloud avec lesquels vos applications peuvent interagir.

Créer une simple lambda avec laquelle vous pouvez jouer, que ce soit dans AWS, Netlify, ou tout autre fournisseur cloud, vous donnera une bonne expérience de ce à quoi vous pourriez vous attendre lorsque vous travaillez dans le domaine.

Et même si vous ne développez peut-être pas directement dans une lambda dans l'emploi que vous trouvez, vous pourrez commencer à vous familiariser avec des concepts qui sont fondamentaux pour travailler avec le back end. Et vous utiliserez finalement ces fonctions pour vous connecter à d'autres services et bases de données afin de créer vos propres services dynamiques.

### Alors, que devrais-je apprendre ?

Si vous travaillez déjà sur l'apprentissage de Javascript du côté front end des choses, continuez en utilisant Javascript pour votre backend. Lancez une lambda en utilisant [Netlify functions](https://docs.netlify.com/functions/overview/), où vous n'avez besoin de vous concentrer que sur le code et Netlify s'occupe du reste (comme la construction et le déploiement de votre fonction).

Avec votre langage de choix et votre première fonction, essayez de commencer à travailler avec d'autres services dans votre code pour obtenir de l'expérience avec les API tierces.

Peut-être construire un endpoint qui peut [envoyer un tweet](https://github.com/colbyfayock/tweet) en utilisant l'[API Twitter](https://developer.twitter.com/en/docs) (mais ne l'abusez pas). Apprenez à créer une base de données et configurez votre fonction pour interagir avec elle dans un modèle CRUD, ce qui vous donnera un cas d'utilisation plus réaliste pour la façon dont une application typique pourrait interagir avec un backend.

Votre objectif ici devrait être de créer des services avec lesquels votre front end interagira via un endpoint pour effectuer des opérations pour la personne utilisant votre application. La bonne nouvelle est que, étant donné l'élan du cloud, vous aurez une tonne d'options, et [des options gratuites](https://aws.amazon.com/free/) ou des niveaux, pour commencer à jouer.

### Ressources

* "Super simple start to serverless" [https://kentcdodds.com/blog/super-simple-start-to-serverless](https://kentcdodds.com/blog/super-simple-start-to-serverless)
* "Building Serverless CRUD apps with Netlify Functions & FaunaDB" [https://www.netlify.com/blog/2018/07/09/building-serverless-crud-apps-with-netlify-functions-faunadb/](https://www.netlify.com/blog/2018/07/09/building-serverless-crud-apps-with-netlify-functions-faunadb/)

## DevOps et le cloud

DevOps découle du besoin de pouvoir créer des solutions qui lissent et accélèrent le processus de passage du code des personnes qui l'écrivent à un état déployé.

Ce travail peut aller de nombreuses responsabilités à quelques-unes, qu'il s'agisse d'écrire des scripts bash pour une solution personnalisée ou d'écrire un modèle [CloudFormation](https://aws.amazon.com/cloudformation/) qui crée toutes les ressources nécessaires pour qu'une application s'exécute.

Vous trouverez généralement cela inclus dans le cadre d'une orchestration plus large des flux de travail [CI/CD](https://en.wikipedia.org/wiki/CI/CD) qui automatisent le processus de construction et de déploiement.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/continuous-integration-continuous-deploy-1.jpg)
_Pipeline CI / CD_

Et cela change constamment ! Étant donné le boom du serverless, le [framework serverless](https://serverless.com/) est apparu, ce qui gère beaucoup de cela pour vous de manière plus facile, ce qui a même conduit AWS à créer sa propre solution [SAM](https://aws.amazon.com/serverless/sam/). Des outils comme [Jenkins](https://jenkins.io/) existent depuis un certain temps pour la partie CI/CD des choses, mais maintenant vous voyez [Github](https://github.com/features/actions), [Gitlab](https://about.gitlab.com/product/continuous-integration/), et d'autres fournisseurs de contrôle de source fournir leurs propres solutions et outils comme [CircleCI](https://circleci.com/) qui s'intègrent directement dans votre projet.

Ce n'est pas encore parfait – écrire des modèles CloudFormation est intimidant. Écrire des scripts d'automatisation n'est pas non plus ce qu'il y a de plus amusant, bien que ce soit super gratifiant quand ça marche !

Mais cela s'améliore, c'est là que des produits comme Netlify et Zeit interviennent. Bien qu'ils soient plus enracinés dans le côté hébergement statique des choses, où vous compilez votre application et la déposez dans le stockage, leurs offres grandissent, comme les [Fonctions de Netlify](https://www.netlify.com/products/functions/) qui ne sont vraiment que des Lambdas AWS plus faciles à configurer et à déployer vers un endpoint entièrement fonctionnel (c'est sérieusement super facile).

### Alors, que devrais-je apprendre ?

Si c'est la première fois que vous configurez ce genre de chose, commencez avec Netlify. Configurez une application React ou même simplement un fichier HTML simple dans un dépôt Github, connectez-le à un nouveau compte Netlify, et regardez-le se déployer.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/netlify-setup.jpg)
_Démarrage facile avec [Netlify](https://www.netlify.com/)_

À partir de là, ou si vous avez déjà un peu d'expérience, commencez à vous intéresser à ce qui se passe en coulisses. Netlify prend probablement votre code, exécute les commandes que vous avez configurées (comme `yarn build`) dans un environnement virtuel, dépose les fichiers construits dans un stockage comme S3, et place un CDN devant comme CloudFront pour servir depuis un endpoint.

Essayez d'abord de faire cela manuellement depuis votre ordinateur en utilisant la console AWS et leur CLI, puis écrivez un script pour automatiser tout le processus en intégrant Circle CI dans votre projet Github au lieu de Netlify pour le déployer réellement sur AWS.

Passer cela à un niveau supérieur inclura le lancement de services avec lesquels votre backend pourrait interagir. Avez-vous une base de données que vos services utilisent ? Vous pouvez automatiser le lancement de cette base de données en utilisant CloudFormation ou des scripts bash.

Traiter votre infrastructure comme du code avec des ressources jetables et facilement recréables vous aidera, vous et vos projets, à devenir plus flexibles et à avoir une meilleure capacité à redémarrer en cas de défaillance.

Et tout cela s'applique à tout fournisseur de cloud ou de CI/CD, pas seulement AWS et Circle CI. Choisissez votre cloud et votre outil de workflow préférés et lancez-vous. L'important est de commencer à examiner les besoins de votre projet et de creuser ce qui se passe réellement dans les parties automatisées de la stack. Cela vous aidera à apprendre davantage et à devenir plus ingénieux pour les besoins de votre projet.

### Ressources

* "Un guide étape par étape : Déploiement sur Netlify" [https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/](https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/)
* "Configuration d'un site web statique" [https://docs.aws.amazon.com/AmazonS3/latest/dev/HostingWebsiteOnS3Setup.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/HostingWebsiteOnS3Setup.html)
* "Formation AWS Certified Cloud Practitioner 2019 - Un cours vidéo gratuit de 4 heures" [https://www.freecodecamp.org/news/aws-certified-cloud-practitioner-training-2019-free-video-course/](https://www.freecodecamp.org/news/aws-certified-cloud-practitioner-training-2019-free-video-course/)
* Voir les ressources Javascript dans Front End ci-dessus

## Et le design ?

Oui, vous devriez comprendre les bases du design. Non, vous n'avez pas besoin d'être un designer.

Il y a de nombreux aspects du design qui accéléreront vos capacités en tant que développeur. Bien que nous sachions tous que les designers visuels et UX produisent de la magie, avoir une compréhension de base peut empêcher votre application de devenir une énorme déception.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/pied-piper-user-interface.jpg)
_L'application fictive Pied Piper a coulé à cause d'une mauvaise expérience utilisateur_

Tout le monde dans le processus de développement travaille vers un objectif qui impacte un utilisateur final d'une manière ou d'une autre. Être capable de comprendre les besoins que votre travail essaie de résoudre et comment cela impacte les utilisateurs aidera l'équipe dans son ensemble à développer une solution finale plus complète.

Considérez un développeur backend créant une API pour permettre à quelqu'un de gérer les utilisateurs dans une application. Les exigences de l'API sont assez légères et n'incluent que le nom de l'utilisateur. Fournir cela comme un seul champ "nom" au lieu de "prénom" et "nom" pourrait ne pas être la solution la plus intuitive pour la plupart. Mais cela pourrait être une négligence qui complique la manière dont le développeur front end l'expose dans l'UI, ce qui rendrait cela pénible pour le développeur à afficher ou pourrait rendre cela confus pour l'utilisateur final à consommer.

En plus de tout cela, le design peut directement impacter la conversion. Si vous construisez dans l'espace ecommerce, avoir un bouton qui ne ressemble pas à un bouton peut empêcher les gens d'ajouter un produit à leur panier. Cela, bien sûr, empêchera un achat, ce qui est une perte de revenus. Comprendre comment humaniser l'UI même dans un sens de base peut littéralement faire gagner de l'argent à votre projet ou simplement aider quelqu'un à l'utiliser plus facilement.

Et plus important encore, vous voulez que votre site soit accessible. De nombreuses personnes ont des besoins différents, qu'ils ne puissent pas voir les couleurs de la même manière ou ne puissent pas entendre les sons que votre application produit, vous voulez reconnaître les besoins des autres et essayer de concevoir de manière à rendre votre application utilisable par tous.

### Alors, que devrais-je apprendre ?

Bien que je ne m'attende pas à ce que vous suiviez un cours entier pour cela, essayez d'être conscient et curieux. Et peut-être que la prochaine fois, ne sautez pas cet [article de design](https://www.freecodecamp.org/news/tag/design/) que vous avez vu apparaître sur le [Twitter de freeCodeCamp](https://twitter.com/freecodecamp).

Lorsque vous créez des solutions, essayez d'imaginer comment votre travail sera utilisé. De quoi les autres développeurs de votre équipe auront-ils besoin de votre API ? De quoi les personnes utilisant votre application auront-elles besoin de votre interface ?

Vous pouvez également essayer de vous inspirer de ce que font les autres dans votre domaine. À quoi vous attendez-vous qu'une application ressemble lorsqu'elle fournit une fonctionnalité similaire ? Ce n'est pas une licence pour copier ou voler, mais vous devriez comprendre les besoins que leur solution résout. Considérez pourquoi leur bouton Ajouter au panier est si grand, pourquoi ils donnent aux utilisateurs la possibilité de zoomer sur une photo de produit, ou comment vous pouvez rendre un design de table légèrement plus utilisable.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/dribbble-table-design.jpg)
_[Design de produit "table" sur Dribbble](https://dribbble.com/search/shots/popular/product-design?q=table)_

En ce qui concerne l'accessibilité, essayez d'apprendre les bases. Il y a une quantité croissante de ressources disponibles pour vous aider à comprendre les besoins des autres. Essayez de comprendre quels sont les handicaps et comment ils pourraient affecter l'utilisation de votre application. Peut-être regardez quelques modèles courants sur la façon d'aborder ces préoccupations.

Plus souvent qu'autrement, ce n'est pas trop difficile à incorporer, et si vous prenez l'habitude de le faire dès le début, vous n'y penserez même pas la prochaine fois que vous construirez une application.

### Ressources

* Design pour les développeurs [https://thoughtbot.com/upcase/design-for-developers](https://thoughtbot.com/upcase/design-for-developers)
* Hack Design [https://hackdesign.org](https://hackdesign.org)
* Design pour les hackers [https://designforhackers.com/](https://designforhackers.com/)
* Introduction à l'accessibilité web [https://webaim.org/intro/](https://webaim.org/intro/)

## Autres choses si vous débutez

Une grande partie de cet article suppose que vous avez quelques bases comme comprendre ce qu'est [git](https://en.wikipedia.org/wiki/Git) et le contrôle de source ou simplement avoir votre éditeur de code configuré. Si vous débutez vraiment, vous allez vouloir au moins avoir une compréhension simple de ces concepts, car cela deviendra rapidement plus difficile sans eux.

Il y a aussi quelque chose à dire sur l'apprentissage de l'utilisation de votre terminal. Cela peut être accablant de ne pas utiliser une interface graphique si vous êtes nouveau, mais une fois que vous commencez, vous découvrirez rapidement que vous serez plus productif en utilisant un terminal et que de nombreux projets nécessitent l'utilisation d'un terminal de toute façon.

### Alors, que devrais-je apprendre ?

Tout d'abord, configurez votre éditeur de code. [Visual Studio Code](https://code.visualstudio.com/) est très à la mode en ce moment, mais il y en a d'autres qui vous serviront bien selon vos préférences comme [Atom](https://atom.io/) ou [Sublime Text](https://www.sublimetext.com/). Vous trouverez même des IDE basés sur le cloud comme [Repl.it](https://repl.it/) ou vous pouvez simplement commencer avec une barrière d'entrée plus basse en jouant dans [CodePen](https://codepen.io/) ou [JSFiddle](https://jsfiddle.net/).

![Image](https://www.freecodecamp.org/news/content/images/2020/02/visual-studio-code-so-hot.jpg)
_Visual Studio Code est très à la mode en ce moment_

Dans tous les cas, une fois que vous êtes prêt à commencer à coder, vous voulez comprendre ce qu'est le contrôle de source, où git est le plus grand acteur en ce moment. Git est un outil puissant qui vous permet de suivre les changements de code et de devenir plus productif en collaborant avec d'autres développeurs.

Vous allez vouloir vous familiariser avec certaines des commandes de base de git comme l'ajout de nouveaux changements ainsi que ce que sont les branches et comment les utiliser. Git est un monde immense, vous n'avez pas besoin de le maîtriser tout de suite, vous apprendrez rapidement qu'il y a une quantité infinie de nouvelles choses à apprendre sur votre chemin pour maîtriser votre git fu.

Pour beaucoup d'outils que vous utiliserez, il existe des interfaces graphiques comme [GitKraken](https://www.gitkraken.com/), mais vous serez toujours un peu limité dans ce que vous pouvez faire. Apprendre à vous débrouiller avec les terminaux par défaut de votre machine ou télécharger d'autres options comme [iterm2](https://iterm2.com/) (ma préférence) ou [Xterm.js](https://xtermjs.org/) sera votre meilleur pari. Bonus : vous vous sentirez comme un hacker de film chaque fois que vous l'utiliserez (ou est-ce juste moi ?).

![Image](https://www.freecodecamp.org/news/content/images/2020/02/hacking-swordfish.gif)
_Hugh Jackman piratant dans Swordfish_

### Ressources

* Commencer avec Visual Studio Code [https://www.codecademy.com/articles/visual-studio-code](https://www.codecademy.com/articles/visual-studio-code)
* Ressources Git de Github [https://try.github.io/](https://try.github.io/)
* Apprendre git par le jeu de branchement [https://learngitbranching.js.org/](https://learngitbranching.js.org/)
* Introduction à la ligne de commande Mac [https://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line](https://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line)

## Autres choses si vous cherchez plus

Il y a tellement plus que vous pouvez rapidement explorer. N'oubliez pas de ne pas disperser votre concentration et essayez de ne pas vous submerger. Mais si vous vous sentez bien là où vous en êtes, il y a d'autres concepts qui ne feront qu'aider lorsque vous relevez des défis dans le monde réel.

### [Tests](https://en.wikipedia.org/wiki/Software_testing) et les différentes méthodologies

Écrire du code est une chose, mais être capable de mettre en place des tests efficaces aidera à renforcer votre code et à prévenir les bugs. Vous ne voulez pas gaspiller votre temps futur ou même coûter de l'argent à votre produit lorsque le site tombe en panne. Apprendre à écrire des tests et les différentes approches est important pour solidifier votre code.

### Outils de navigateur comme [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)

L'un des outils les plus puissants que vous pouvez avoir lors du débogage, à mon avis, est d'être capable de déboguer votre application dans le navigateur.

Qu'il s'agisse de regarder comment le DOM est rendu, [jouer avec le CSS](https://developers.google.com/web/tools/chrome-devtools/inspect-styles/edit-styles), ou déboguer vos requêtes réseau, vous apprendrez rapidement comment gagner du temps et identifier plus facilement d'où vient le bug.

### [HTTP](https://developers.google.com/web/fundamentals/performance/http2) et comment déboguer les requêtes dans le [panneau réseau](https://developers.google.com/web/tools/chrome-devtools/network)

Étant donné que le web est basé sur l'internet, votre application fera finalement des requêtes à d'autres serveurs. Lorsque cela se produit, comprendre les goulots d'étranglement des requêtes ou simplement comment une requête est faite peut vous aider à comprendre pourquoi votre application semble lente ou pourquoi votre bouton d'enregistrement ne fonctionne pas.

Avoir une compréhension de base de comment les requêtes fonctionnent et comment les visualiser pour le débogage vous mènera loin dans votre voyage.

### Logiciels open source et gestionnaires de paquets

Celui-ci n'est pas tant une compétence ou un outil à apprendre qu'une manière dont le logiciel est distribué. Lorsque vous commencez à construire des solutions de code, vous découvrirez que beaucoup d'entre nous s'appuient sur des paquets open source. La plupart du temps, c'est via [npm](https://www.npmjs.com/) si vous écrivez en Javascript, ce qui nous aide à devenir plus productifs sans avoir à réinventer la roue chaque fois.

Passez du temps à comprendre le concept open source et envisagez même de redonner en contribuant à votre projet préféré. Prêter main forte est généralement super apprécié, vous aidera à gagner de l'expérience, et vous pourriez même pouvoir obtenir [du swag gratuit sur votre première pull request approuvée](https://www.gatsbyjs.org/contributing/contributor-swag/) ! Soyez simplement respectueux, il y a aussi une vraie personne de l'autre côté de la demande.

## Qu'est-ce d'autre ?

Cette liste peut continuer à l'infini car il y a tant de choses dans le monde du codage. Qu'est-ce d'autre que vous pensez être important dans le voyage de quelqu'un pour devenir un maître du développement ? Envoyez-moi un [tweet ou un DM](https://twitter.com/colbyfayock) si vous pensez que j'ai oublié quelque chose d'important !

## Vous êtes en feu ! Tout rassembler

Étant donné toute l'expérience que vous aurez accumulée avec ce qui précède, vous devriez être en mesure de créer une application entière de bout en bout par vous-même. Comprenez-vous le pouvoir que vous avez ?

![Image](https://www.freecodecamp.org/news/content/images/2020/02/thanos-glove-1.gif)
_Thanos serrant le gantlet_

C'est là que le plaisir commence. Essayez de créer une nouvelle application – peu importe ce que c'est, construisez simplement quelque chose. La meilleure chose que vous puissiez faire pour apprendre est de gagner de l'expérience en faisant. Peu importe que ce soit l'un des millions de tutoriels todo que vous trouverez ou en vous apprenant à coder en construisant l'un des plus grands réseaux sociaux comme le [créateur d'Instagram](https://thenextweb.com/2012/04/10/instagrams-ceo-had-no-formal-programming-training-hes-a-marketer-who-learned-to-code-by-night/).

À partir de là, vous devriez être capable de créer :

* Une application web front end qui s'exécute dans le navigateur
* Des services backend auxquels votre application web peut faire des requêtes via des endpoints
* Écrire un script à intégrer dans un outil CI/CD pour automatiser votre processus de construction et de déploiement
* Bonus : prendre de bonnes décisions sur l'apparence de votre interface pour que les gens puissent l'utiliser !

Allez de l'avant et construisez ! [Partagez avec nous votre parcours de développement](https://twitter.com/intent/tweet?text=My%20%23codejourney%20started%20with...%0A%0AHow%20to%20Become%20a%20Full%20Stack%20Web%20Developer%20in%20a%20JAMstack%202020%0A@colbyfayock%20@freecodecamp%0Ahttps%3A%2F%2Fwww.freecodecamp.org%2Fnews%2Fhow-to-become-a-full-stack-web-developer-in-2020) sur Twitter en utilisant le hashtag #codejourney. Nous aimerions en savoir plus sur là où vous avez été et ce que vous avez construit ou où vous allez et ce que vous voulez construire.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f60a Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e9f60a Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>