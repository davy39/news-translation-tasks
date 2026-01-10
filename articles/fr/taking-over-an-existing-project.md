---
title: Conseils pour le code hérité – Comment reprendre un projet existant et sa base
  de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-17T16:01:28.000Z'
originalURL: https://freecodecamp.org/news/taking-over-an-existing-project
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/exisiting-proj.jpg
tags:
- name: project management
  slug: project-management
- name: software development
  slug: software-development
- name: tips
  slug: tips
seo_title: Conseils pour le code hérité – Comment reprendre un projet existant et
  sa base de code
seo_desc: 'By Milecia McGregor

  Working as a developer means you need to know how to dive into existing code bases.
  When you inherit a project, there are a lot of specifics that you don''t know, like
  why some of the code is written a certain way.

  So when it''s tim...'
---

Par Milecia McGregor

Travailler en tant que développeur signifie que vous devez savoir comment plonger dans des bases de code existantes. Lorsque vous reprenez un projet, il y a beaucoup de détails spécifiques que vous ne connaissez pas, comme pourquoi certaines parties du code sont écrites d'une certaine manière.

Ainsi, lorsque vient le moment de la réunion de transfert, vous devez savoir quelles questions poser. C'est le meilleur moment pour obtenir les informations dont vous avez besoin pour démarrer.

Ces questions se posent dans chaque projet. Vous pouvez commencer un nouvel emploi ou travailler sur un projet différent dans votre entreprise actuelle. Quoi qu'il en soit, voici quelques points que vous devriez aborder lors des réunions de transfert.

## Savoir ce que le projet est censé faire

![Image](https://www.freecodecamp.org/news/content/images/2020/05/what-it-does.png)

À quoi sert exactement cette application et qui l'utilise ? Sans ce contexte, il sera vraiment difficile de comprendre comment implémenter de nouvelles fonctionnalités ou corriger des bugs.

Demandez à connaître l'utilisation générale de l'application. Apprenez le flux de travail des différentes parties de l'application et comment les utilisateurs la parcourent. S'il y a une liste de tâches, obtenez une présentation ou plus de détails sur chacun des éléments de la liste.

C'est l'un des rares moments où tout le monde est prêt à se concentrer sur les questions concernant le projet. Donc, s'il y a _quoi que ce soit_ qui n'est pas clair pour vous, ne quittez pas cette réunion sans avoir une meilleure compréhension.

Bien sûr, des choses apparaissent une fois que vous commencez à creuser, mais c'est votre chance d'éviter une grande partie de la confusion. Essayez d'obtenir une compréhension générale de l'application avant de plonger dans des questions spécifiques. Apprendre le secteur dans lequel l'application opère peut également aider à répondre aux questions qui se posent lors de votre développement.

## Savoir comment la gestion du contrôle de source est effectuée

![Image](https://www.freecodecamp.org/news/content/images/2020/05/source-control.png)

Bien que la plupart des projets utilisent Git, tout le monde n'utilise pas GitHub. Certains projets peuvent être hébergés dans BitBucket, Azure DevOps, ou même sur un SVN. Vous devez savoir où le code est conservé dans le contrôle de version afin de pouvoir le télécharger sur votre machine et également pour pouvoir effectuer le dépannage lorsque ces bugs de production inévitables apparaissent.

Assurez-vous d'avoir accès au dépôt de code et que vous avez le bon niveau de permissions pour effectuer le travail dont vous avez besoin. Lorsque vous recevez vos identifiants de connexion, vérifiez-les immédiatement.

Plus tôt vous pourrez trouver de petits problèmes comme ceux-ci, plus le projet se déroulera sans encombre à long terme. Corrigiez un petit bug et faites un commit rapide pour vous assurer que vous pouvez pousser vos branches locales vers l'emplacement du dépôt distant.

De plus, jetez un rapide coup d'œil à toutes les personnes qui ont accès au dépôt. Ce seront des informations utiles lorsqu'il sera temps pour les pull requests et les revues de code. C'est aussi le moment de s'assurer que seules les personnes nécessaires ont accès au code.

Notez les utilisateurs que vous ne connaissez pas et vérifiez avec un chef de projet ou quelqu'un pour voir s'ils ont toujours besoin d'accès.

## Savoir comment exécuter le projet

![Image](https://www.freecodecamp.org/news/content/images/2020/05/run-code.png)

La partie la plus difficile de la reprise d'un nouveau projet peut être de le configurer et de l'exécuter sur votre machine pour la première fois. Il y a beaucoup de commandes ponctuelles qui peuvent être perdues si le processus n'a pas été bien documenté.

Quelques points que vous devez vérifier et qui ne sont pas évidents incluent vos variables d'environnement, les versions des logiciels que vous exécutez et les noms de fichiers que vous référencez.

D'autres choses qui peuvent survenir incluent la configuration d'une nouvelle base de données locale et le chargement des données de base, ainsi que la modification des chaînes de connexion aux API ou aux bases de données.

```
REACT_APP_NAME="Boogaloo"
REACT_APP_API="https://not-staging.morwl.com/api"
API_KEY=ij2i0r9j02tt904tn93
```

Si vous rencontrez des problèmes lors de la configuration, assurez-vous de les documenter afin que ce soit plus facile pour le prochain développeur. De plus, vous ne savez jamais quand vous devrez réinitialiser votre ordinateur et ces notes vous seront utiles.

Une fois que vous avez l'application en cours d'exécution, vérifiez que tout fonctionne comme dans l'environnement de développement ou de production. Vous devriez voir le même comportement dans tous les environnements jusqu'à ce que les gens commencent à pousser des changements.

## Connaître le processus de test

![Image](https://www.freecodecamp.org/news/content/images/2020/05/testing.png)

Il existe de nombreuses formes différentes de tests que votre application peut subir et vous devez savoir comment ce processus fonctionne. Les tests unitaires sont courants dans la plupart des projets à un certain degré, alors vérifiez toujours leur présence. Certaines entreprises effectuent des tests d'intégration pour s'assurer qu'aucun changement cassant ne se glisse dans les pipelines de build ou de déploiement.

D'autres endroits ont même des testeurs logiciels dédiés qui exécuteront des scénarios utilisateurs pour voir comment les choses fonctionneront lorsque les vrais utilisateurs verront les mises à jour. Vous devez être conscient de toutes les étapes que votre application traversera.

Lorsque vous commencez ce nouveau projet, regarder les tests peut vous donner une bonne idée de comment l'application fonctionne. S'il n'y a pas de tests dans le projet, c'est votre chance de commencer à les ajouter. Avoir une certaine couverture de code donne le ton pour l'application à l'avenir, indiquant qu'il devrait probablement y avoir plus de tests ajoutés à mesure que le code est développé.

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import Items from '../src/components/Items';
import CreateItemModal from '../src/components/CreateItemModal';

configure({ adapter: new Adapter() });
jest.mock('../__mocks__/getAllItemsMockRequest.js');

describe('Le composant Items fonctionne', () => {
    it('Items se rend sans planter', () => {
        const div = document.createElement('div');
        ReactDOM.render(<Items />, div);
        ReactDOM.unmountComponentAtNode(div);
    });

    it('devrait basculer CreateItemModal', () => {
        const div = document.createElement('div');
        const ItemComponent = shallow(<Items />, div);
        ItemComponent.find('#add-item-icon').simulate('click');
        expect(ItemComponent.contains(<CreateItemModal />)).toBe(true);
        ReactDOM.unmountComponentAtNode(div);
    });
});
```

Travailler avec des testeurs logiciels est généralement un processus plus impliqué. Il y a généralement un système en place comme Jira ou Basecamp où les bugs et les fonctionnalités peuvent être discutés et suivis à travers les sprints. Suivez le processus qu'ils ont en place et cela aidera à faire passer votre code à la phase de déploiement plus rapidement et de manière plus cohérente.

## Connaître le processus de déploiement

![Image](https://www.freecodecamp.org/news/content/images/2020/05/deploy-process.png)

Bien que les services cloud aient pris en charge la plupart des besoins d'hébergement des entreprises, vous devrez peut-être encore travailler avec un serveur physique. Avoir ces informations vous aidera à comprendre la stratégie de déploiement avec laquelle vous allez travailler.

Y a-t-il un processus de build/déploiement continu en place ou devrez-vous effectuer des déploiements manuels depuis votre machine ? Sachez comment les migrations doivent être gérées dans les différents environnements. Clarifiez toutes les parties courantes du déploiement d'une application pour cette application particulière.

De petites choses bizarres peuvent se produire avec les services cloud que seules les personnes qui ont géré les déploiements auparavant connaissent, alors assurez-vous de demander s'il y a un comportement étrange auquel vous devriez faire attention. Puisque vous avez déjà corrigé un petit bug pour vérifier que vous pouvez pousser vos changements, allez-y et déployez cette petite correction dans l'environnement de développement.

```yml
version: 2
jobs:
  build:
    docker:
      - image: circleci/<language>:<version TAG>
    steps:
      - checkout
      - run: <command>
  test:
    docker:
      - image: circleci/<language>:<version TAG>
    steps:
      - checkout
      - run: <command>
workflows:
  version: 2
  build_and_test:
    jobs:
      - build
      - test
```

C'est votre test pour voir si vous comprenez vraiment comment les déploiements fonctionnent. Espérons que vous n'aurez pas à faire beaucoup de déploiements manuels et que vous travaillerez avec des pipelines CI/CD pour que le processus reste cohérent.

## Savoir à qui vous adresser pour les différentes parties du projet

![Image](https://www.freecodecamp.org/news/content/images/2020/05/team.png)

Sauf si vous êtes responsable de l'ensemble de l'application, du front-end jusqu'à la base de données, il y a probablement d'autres personnes qui couvrent des parties du code ou du système que vous ne toucherez jamais. Il est important de savoir qui sont ces personnes afin de savoir à qui poser vos questions.

De plus, c'est une excellente façon de faire connaissance avec d'autres équipes qui travaillent sur le projet et d'apprendre ce qu'elles font. Si vous êtes seul à travailler sur toutes les parties d'un projet, assurez-vous d'obtenir tous les identifiants de connexion possibles, car ce sera à vous de répondre à toutes les questions.

## Connaître les services tiers utilisés par le projet

![Image](https://www.freecodecamp.org/news/content/images/2020/05/third-party.png)

Lorsque vous commencez à déboguer des problèmes, savoir où trouver la documentation est le moyen le plus rapide de corriger les choses. Cela signifie connaître les services utilisés par l'application et où ils sont utilisés. Une façon de le découvrir est de vérifier le fichier _package.json_ ou _App.config_ de votre projet pour voir ce qui est installé.

```json
{
    "name": "dog-finder",
    "version": "0.1.0",
    "scripts": {
        "build": "npm install",
        "start": "npm run build && concurrently --kill-others \"node ./server.js\" \"http-server\""
    },
    "dependencies": {
        "concurrently": "^5.1.0",
        "cors": "^2.8.5",
        "express": "^4.17.1",
        "johnny-five": "^1.4.0",
        "path": "^0.12.7"
    }
}

```

Cela vous aidera à résoudre de nombreux problèmes qui surviennent en production et cela vous aidera à poser de meilleures questions. Vous aurez également besoin d'identifiants pour la plupart des services, donc cela surgira probablement lorsque vous essayerez d'exécuter le projet pour la première fois.

Quelques grands avantages à examiner les services tiers tôt sont d'apprendre les changements de compatibilité de version et les problèmes connus.

Une plainte courante à laquelle vous serez confronté sur des projets plus anciens est que l'application ne fonctionne plus comme avant et que personne ne sait pourquoi. Examiner ces services est un endroit rapide et facile pour commencer à chercher tandis que vous vous préparez à reprendre le projet.

## Connaître la meilleure façon de contacter les décideurs

![Image](https://www.freecodecamp.org/news/content/images/2020/05/decision-maker.png)

Même si vous reprenez le développement principal d'un projet, il y aura toujours quelqu'un comme un chef de projet qui guidera les tâches sur lesquelles vous travaillez. Obtenez ses coordonnées dès que vous obtenez l'approbation pour commencer le projet. C'est l'une des personnes qui pourra répondre à vos questions de haut niveau.

Si vous travaillez avec une petite entreprise, il serait également bon d'avoir les coordonnées de quelqu'un comme le PDG ou le CTO, car ils pourront vous donner un oui ou un non direct à beaucoup de vos questions.

Par exemple, si vous avez recherché un nouveau service de base de données qui réduira leur facture de 10 % et augmentera les performances globales de l'application, vous voulez savoir si vous pouvez apporter ces changements ou non.

Apprenez à connaître les personnes qui peuvent vous donner l'approbation ou des conseils pour les prochaines étapes que vous entreprenez, puis enregistrez leurs e-mails et numéros de téléphone.

Une situation où cela est particulièrement crucial est s'il y a un incendie en production. Lorsque vous pouvez obtenir ces décisions rapides immédiatement, cela peut sauver des milliers de dollars à une entreprise, donc ils comprendront si vous les appelez.

## Connaître votre calendrier

![Image](https://www.freecodecamp.org/news/content/images/2020/05/timeline.png)

Parfois, il est si facile de se laisser absorber par les détails minutieux que lorsqu'un calendrier est proposé, accepter semble sensé.

Avant de vous engager pleinement dans une durée de travail, assurez-vous d'avoir fait une évaluation appropriée de ce qu'on vous demande de faire avec les ressources qui vous sont fournies. Faites un rapide balayage du code pour avoir une idée de ce avec quoi vous allez travailler et voyez combien de temps il faut aux gens pour répondre à vos questions initiales.

Ainsi, lorsque vous recevez une date limite, vous pouvez expliquer pourquoi elle est ou n'est pas raisonnable pour la quantité de travail demandée. Vous voulez toujours donner des estimations réalistes afin que votre client ou chef de projet ne donne pas de faux espoirs aux autres. Il est préférable de leur dire dès le début si quelque chose prendra plus ou moins de temps que ce qu'ils attendent.

Lorsque vous avez des attentes raisonnables, cela rend le projet plus fluide pour tout le monde. Il y a moins de sessions de codage paniquées et vous êtes en mesure de livrer un code de qualité qui n'aura pas à être débogué en production.

## Connaître la portée de votre travail

![Image](https://www.freecodecamp.org/news/content/images/2020/05/scope.png)

La portée des projets tend à s'étendre lentement à mesure que vous progressez. Vous commencez à recevoir des retours ici et là sur des "petits ajustements" qui devraient être faits. Ensuite, cela se transforme en une question de priorité et ce n'est plus le travail original avec lequel vous avez commencé.

Une façon de prévenir l'expansion de la portée est de convenir d'une liste fixe de tâches ou d'une fonctionnalité spécifique qui doit être implémentée. Tout le reste peut être noté et abordé dans une autre partie du travail du projet, mais pas maintenant.

Une fois que le travail a été convenu, il devrait y avoir un état final clair dans lequel le projet se trouvera à la fin.

## Réflexions finales

Reprendre un projet existant est une compétence spéciale car ce n'est pas quelque chose que vous faites tout le temps. Certaines personnes travaillent sur un produit ou une gamme de produits pendant une grande partie de leur carrière, donc la configuration de nouveaux projets ne se produit que de temps en temps.

Cependant, si vous faites du conseil ou du travail freelance, vous devrez savoir comment faire cela avec confiance de manière régulière. Habituellement, il y a de petits changements de configuration que vous devez comprendre et une fois que vous les avez configurés, vous n'aurez plus à vous en soucier.

Ce ne sont que quelques points que j'essaie de vérifier lorsque je configure un nouveau projet. Certains de ces conseils s'appliquent également aux projets open source. Avez-vous quelque chose que vous vérifiez toujours lorsque vous vous installez ?

---

J'écris aussi sur d'autres sujets aléatoires dans la tech, comme les guitars aériennes et la VR. Vous devriez me suivre sur [Twitter](https://twitter.com/FlippedCoding) pour en apprendre davantage sur ces sujets cool.