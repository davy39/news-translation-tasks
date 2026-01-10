---
title: Qu'est-ce que le test logiciel ? Les 10 types de tests les plus courants utilisés
  par les développeurs dans les projets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-13T19:27:45.000Z'
originalURL: https://freecodecamp.org/news/types-of-software-testing
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/pexels-thisisengineering-3861969.jpg
tags:
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
- name: unit testing
  slug: unit-testing
- name: usability testing
  slug: usability-testing
seo_title: Qu'est-ce que le test logiciel ? Les 10 types de tests les plus courants
  utilisés par les développeurs dans les projets
seo_desc: "By Nahla Davies\nSoftware development and testing go hand in hand. And\
  \ in the era of agile software development, with quick releases of small iterations,\
  \ you should do testing more and more frequently. \nIn order to perform effective\
  \ testing, you need ..."
---

Par Nahla Davies

Le développement et le test de logiciels vont de pair. Et à l'ère du développement logiciel agile, avec des sorties rapides de petites itérations, vous devriez effectuer des tests de plus en plus fréquemment.

Afin de réaliser des tests efficaces, vous devez connaître les différents types de tests et savoir quand les utiliser.

Dans cet article, je vais aborder certains des tests à votre disposition pour vous aider à garantir l'opérabilité, l'intégrité et la sécurité de vos produits et applications.

## La pyramide des tests logiciels

![La pyramide des tests logiciels](https://www.freecodecamp.org/news/content/images/2021/05/Instagram-Square-Pyramid-Chart---CC.png)
_La pyramide des tests logiciels. Profitez de ce graphique gratuit et partagez-le sur votre blog ou Twitter._

La pyramide des tests logiciels couvre toutes les étapes [du cycle de vie du développement logiciel](https://www.freecodecamp.org/news/get-a-basic-understanding-of-the-life-cycles-of-software-development/) (SDLC). Elle s'étend des tests unitaires à la base, passe par les tests d'intégration et se termine par les tests fonctionnels au sommet.

Il n'y a pas de répartition fixe entre ces types de tests. Au lieu de cela, vous devez déterminer quels tests conviennent le mieux à vos besoins individuels. Pour prendre ces décisions sur les types de tests dont vous avez besoin, vous devez équilibrer leur coût, le temps qu'ils prendront et les ressources qu'ils nécessiteront.

Les développeurs de logiciels agiles [utilisent également les quadrants de tests logiciels](https://www.kaizenko.com/what-is-the-agile-testing-quadrant/) qui catégorisent les tests selon qu'ils sont orientés métier ou technologie, et s'ils critiquent le produit ou soutiennent l'équipe.

Le test unitaire, par exemple, est un test orienté technologie qui soutient l'équipe, tandis que le test d'utilisabilité est un test orienté métier qui critique le produit.

Passons maintenant en revue quelques types de tests importants.

## Définition des tests unitaires

Le test unitaire [implique de tester des composants de code individuels](https://www.freecodecamp.org/news/unit-tests-explained/) plutôt que le code dans son ensemble. Il vérifie le fonctionnement de toute la logique de vos composants pour identifier les bogues tôt dans le SDLC, ce qui vous permet de corriger les erreurs avant de poursuivre le développement.

Le test unitaire est connu sous le nom de test « boîte blanche », car le test se déroule avec une connaissance complète de la structure et de l'environnement de l'application.

Un exemple de test unitaire consiste à créer des objets simulés (mocks) pour tester des sections de code, comme des fonctions avec des variables qui n'ont pas encore été créées.

```javascript
const mocha = require('mocha')
const chai = require('chai')  // C'est une bibliothèque d'assertion
describe('Test to check add function', function(){
  it('should add two numbers', function(){
    (add(2,3)).should.equal(5)  // Vérification que 2+3 doit être égal à 5 en utilisant la fonction add fournie
  });
});
```

## Définition des tests d'intégration

L'étape supérieure au test unitaire est le test d'intégration, qui combine des composants individuels et les teste en groupes. Le test d'intégration identifie les problèmes dans la manière dont les composants individuels interagissent entre eux pour voir si le code répond à toutes ses spécifications fonctionnelles.

Le test d'intégration diffère du test unitaire en ce qu'il se concentre sur les modules et les composants travaillant indépendamment par rapport au groupe global. D'un autre côté, le test unitaire se concentre sur l'isolement des modules ou des composants avant le test.

Le but du test d'intégration est d'exposer tout problème ou vulnérabilité logicielle entre les modules ou composants intégrés.

À titre d'exemple simplifié, si vous deviez effectuer un test d'intégration d'un service de messagerie que vous construisez, vous devriez tester les composants individuels tels que la rédaction d'un message, l'enregistrement des brouillons, l'envoi, le déplacement vers la boîte de réception, la déconnexion, et ainsi de suite.

Vous effectueriez d'abord un test unitaire des fonctionnalités individuelles, suivi du test d'intégration pour chacune des fonctions liées.

## Définition des tests de bout en bout

Au sommet de la pyramide se trouve le test de bout en bout (E2E). Comme son nom l'indique, le test de bout en bout [reproduit le fonctionnement complet de l'application](https://www.freecodecamp.org/news/end-to-end-testing-tutorial/) afin de tester toutes les connexions et dépendances de l'application. Cela inclut la connectivité réseau, l'accès à la base de données et les dépendances externes.

Vous effectuez les tests E2E dans un environnement qui simule l'environnement utilisateur réel.

Vous pouvez déterminer le succès d'un test E2E à l'aide de plusieurs mesures, notamment un statut du test (à suivre avec un visuel, tel qu'un graphique) et un statut et rapport (qui doit afficher l'état d'exécution et toutes les vulnérabilités ou défauts découverts).

## Types de tests logiciels

Au sein des niveaux de la pyramide de tests se trouve une grande variété de processus spécifiques pour tester diverses fonctions et caractéristiques de l'application, ainsi que l'intégrité et la sécurité de l'application.

### Définition des tests de sécurité des applications

L'un des types de tests les plus importants pour les applications est le test de sécurité des applications. Les tests de sécurité vous aident à identifier les vulnérabilités des applications qui pourraient être exploitées par des pirates et à les corriger avant de publier votre produit ou application.

Il existe une [gamme de tests de sécurité des applications](https://securityboulevard.com/2020/03/application-security-testing-trends-in-2020/) à votre disposition, avec différents tests applicables à différentes parties du cycle de vie du développement logiciel.

Vous pouvez trouver différents types de tests de sécurité des applications à différents niveaux de la pyramide de tests. Chaque test a ses propres forces et faiblesses. Vous devriez utiliser les différents types de tests ensemble pour garantir leur intégrité globale.

### Définition des tests statiques de sécurité des applications (SAST)

Vous devriez utiliser les tests statiques de sécurité des applications (SAST) tôt dans le SDLC. C'est un exemple de test unitaire.

Le SAST reflète les connaissances du développeur, y compris la conception générale et l'implémentation de l'application, et il s'agit donc d'un test en boîte blanche, ou de l'intérieur vers l'extérieur.

Le SAST analyse le code lui-même plutôt que l'application finale, et vous pouvez l'exécuter sans réellement exécuter le code.

![Image](https://lh4.googleusercontent.com/R4aFSAcHZcrpNNzFnLlYk-vtXFq7QnjIJKzx_jvqmt-ycGE8CcMozgirFIxfXVXKkjYs1dV_nIQrhCFRC809_Kzp3FLvMqRw519XnDQHX8VEV0065Scw-SzxQlJg44xWeggZx2-e)
_[Source de l'image](https://www.seciq.in/static-application-security-testing/)_

Selon les analystes de sécurité de [Cloud Defense](https://www.clouddefense.ai/sast-static-application-security-testing) :

> « SAST vérifie votre code pour détecter les violations des règles de sécurité et compare les vulnérabilités trouvées entre les branches source et cible... vous serez ensuite averti si les dépendances de votre projet sont affectées par des vulnérabilités nouvellement divulguées. »

Une fois que vous avez connaissance des vulnérabilités, vous pouvez les résoudre avant la construction finale de l'application.

Vous devriez appliquer le SAST lors de la phase de développement de vos projets logiciels. Une bonne approche consistera à concevoir et à écrire vos applications pour inclure des analyses SAST dans votre flux de travail de développement.

### Définition des tests dynamiques de sécurité des applications (DAST)

À l'autre extrémité du spectre se trouvent les tests dynamiques de sécurité des applications (DAST), qui testent l'application entièrement compilée. Vous concevez et exécutez ces tests sans aucune connaissance des structures ou du code sous-jacents.

Parce que le DAST applique la perspective du pirate, il est connu sous le nom de test en boîte noire, ou de l'extérieur vers l'intérieur.

Le DAST fonctionne en attaquant le code en cours d'exécution et en cherchant à exploiter les vulnérabilités potentielles. Le DAST peut employer des techniques d'attaque courantes telles que le cross-site scripting (XSS) et l'injection SQL.

Le DAST est utilisé tard dans le SDLC et est un exemple de test de sécurité d'intégration. Bien que lent (un test DAST complet d'une application entière peut prendre en moyenne cinq à sept jours), il vous révélera les vulnérabilités les plus probables de vos applications que les pirates exploiteraient.

### Définition des tests interactifs de sécurité des applications

Le test interactif de sécurité des applications (IAST) est une méthodologie de test plus récente qui [combine l'efficacité du SAST et du DAST](https://developer.ibm.com/recipes/tutorials/what-is-interactive-application-security-testing/) tout en surmontant les problèmes associés à ces tests plus établis.

L'IAST effectue une analyse continue en temps réel d'une application pour détecter les erreurs et les vulnérabilités à l'aide d'un agent de surveillance inséré. Même si l'IAST fonctionne dans une application en cours d'exécution, il est considéré comme un processus de test précoce du SDLC.

Quel que soit le type de logiciel que vous cherchez à tester, l'IAST est mieux utilisé dans un environnement QA (Assurance Qualité), ou un environnement conçu pour reproduire la production aussi fidèlement que possible sans que vos clients ou utilisateurs n'y accèdent réellement.

### Définition des tests de compatibilité

Le test de compatibilité évalue comment votre application fonctionne et quel est son niveau de sécurité sur divers appareils et environnements, y compris les appareils mobiles et sur différents systèmes d'exploitation.

Le test de compatibilité peut également évaluer si une version actuelle d'un logiciel est compatible avec d'autres versions de logiciels. Les tests de version peuvent être tournés vers le passé (rétrocompatibilité) ou vers l'avenir.

![Image](https://lh6.googleusercontent.com/SDElGdbGkactASCRfFSfWXcdOM36IiAQnDZ3uofeiYAeaxzvwvaQzB9cEqEcUFu7L6Z3GxjoC_nCMy0NhgANP8XdjP3s9MKcxvvMdrZsIsmq3kuIJMYbmViDsbAQpBrvyGZscgm0)
_[Source de l'image](https://www.testrigtechnologies.com/service/compatibility-testing/)_

Les exemples de tests de compatibilité incluent :

* les tests de navigateur (vérifier que votre site Web ou site mobile est entièrement compatible avec différents navigateurs)
* les tests mobiles (s'assurer que votre application est compatible avec iOS et Android)
* ou les tests logiciels (si vous créez plusieurs applications logicielles qui doivent interagir les unes avec les autres, vous devrez effectuer des tests de compatibilité pour vous assurer qu'elles le font réellement).

## Au-delà de la pyramide des tests logiciels

Les versions modifiées de la pyramide de tests peuvent inclure un niveau situé à côté ou au-dessus des tests de bout en bout. Ce niveau se compose de tests axés sur l'utilisateur de l'application.

### Définition des tests de performance

Vous devez savoir comment l'application fonctionnera dans diverses conditions, et c'est l'objectif des tests de performance. Les tests de performance peuvent modéliser diverses charges et contraintes pour évaluer la robustesse de l'application. Le type de test de performance est basé sur les conditions appliquées.

Un exemple de test de performance est le test de charge, qui [détermine la charge maximale](https://www.freecodecamp.org/news/practical-guide-to-load-testing/) appliquée au système au moment d'une panne.

Un autre exemple comme le test de scalabilité, quant à lui, applique une charge augmentant progressivement au système pour évaluer les moyens de s'adapter aux contraintes supplémentaires du système.

Et le test de pic (spike testing) évalue l'effet de l'application de changements de charge soudains et importants au système.

Vous devriez effectuer des tests de performance sur tout système logiciel avant de le mettre sur le marché. Testez-le par rapport à la stabilité, à la scalabilité et à la rapidité afin d'identifier ce qu'il faut corriger avant la mise en ligne.

### Définition des tests d'utilisabilité

Tester l'utilisation réelle de l'interface de l'application est une tâche importante. C'est une chose de comprendre si l'application fonctionne comme prévu. C'en est une autre de comprendre si la conception elle-même est acceptable pour les utilisateurs. C'est là que les tests d'utilisabilité interviennent.

Avec les tests d'utilisabilité, les développeurs peuvent évaluer les réactions des utilisateurs à des caractéristiques et fonctions spécifiques de l'application. Cela inclut des fonctionnalités dont vous savez peut-être à l'avance qu'elles seront moins souhaitables du point de vue de l'utilisateur mais qui sont [nécessaires pour une sécurité robuste](https://privacycanada.net/programming-security-for-beginners/) et un bon fonctionnement (comme les exigences de mots de passe complexes).

Le test d'utilisabilité ne concerne pas tant les problèmes cosmétiques ou la correction des erreurs de grammaire dans les textes écrits (bien que ces deux points soient certainement importants en soi). Il s'agit plutôt de la facilité avec laquelle l'application terminée peut être utilisée par l'utilisateur final.

## Conclusion

Le test n'est pas seulement quelque chose que la division QA devrait faire après que vous avez fini de développer une application. C'est aussi une partie importante du [processus de développement logiciel](https://www.freecodecamp.org/news/software-quality-assurance-guide/).

Savoir quels tests sont à votre disposition et comment ils fonctionnent vous aidera à garantir que votre application fonctionne bien, qu'elle est sécurisée et qu'elle est acceptable pour l'utilisateur final.