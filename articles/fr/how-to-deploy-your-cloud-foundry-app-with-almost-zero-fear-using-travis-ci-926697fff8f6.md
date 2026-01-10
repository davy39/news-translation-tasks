---
title: Comment déployer votre application Cloud Foundry avec (presque) zéro crainte
  en utilisant Travis CI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-15T17:19:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-your-cloud-foundry-app-with-almost-zero-fear-using-travis-ci-926697fff8f6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PXXH-HGbEP2x3LWooWGLlA.jpeg
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Devops
  slug: devops
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment déployer votre application Cloud Foundry avec (presque) zéro crainte
  en utilisant Travis CI
seo_desc: 'By Robin Bobbitt

  Application deployments to the cloud should be painless. We should be able to deploy
  new code continuously, as often as we want, without fear. The blue-green deployment
  model enables us to do this.

  I recently joined a new team at wor...'
---

Par Robin Bobbitt

Les déploiements d'applications dans le cloud devraient être indolores. Nous devrions pouvoir déployer du nouveau code en continu, aussi souvent que nous le souhaitons, sans crainte. Le modèle de [déploiement blue-green](https://docs.cloudfoundry.org/devguide/deploy-apps/blue-green.html) nous permet de le faire.

J'ai récemment rejoint une nouvelle équipe au travail qui déployait des applications Cloud Foundry node.js sur l'IBM Cloud en utilisant Travis avec le [fournisseur de déploiement Bluemix CloudFoundry](https://docs.travis-ci.com/user/deployment/bluemixcloudfoundry/). Cela fonctionne très bien pour configurer rapidement et facilement votre déploiement avec seulement quelques paramètres.

Malheureusement, chaque déploiement signifie une interruption de votre application lorsque la version existante s'arrête et que la nouvelle version démarre. De plus, il n'y a pas de vérification que le nouveau code est bon avant que l'ancien code ne soit supprimé.

Avec la technique de déploiement blue-green, votre application actuelle (Blue) continue de fonctionner et de recevoir le trafic réseau. Pendant ce temps, votre nouveau code d'application (Green) est déployé sur une route temporaire. La nouvelle application Green peut être validée sur la route temporaire. Si des problèmes surviennent, le déploiement s'arrête. L'application Blue continue de servir le trafic sans interruption. Une fois que l'application Green est validée, le routeur est mis à jour pour pointer vers l'application Green. L'application Blue peut être arrêtée.

De cette manière, il y a toujours une version de l'application disponible pour recevoir le trafic. Tout problème dans le déploiement ou l'exécution du nouveau code n'affectera pas la disponibilité de votre application.

J'ai immédiatement commencé à chercher un moyen de déployer nos applications en blue-green. Dans l'intérêt d'écrire le moins de code personnalisé possible, j'ai décidé d'utiliser le [plugin cf-blue-green-deploy](https://github.com/bluemixgaragelondon/cf-blue-green-deploy) pour l'interface de ligne de commande (CLI) de Cloud Foundry. Je vais partager ici comment j'ai fait cela.

Je vais supposer que si vous êtes arrivé ici, vous êtes probablement passé le point de simplement ["commencer" avec Travis](https://docs.travis-ci.com/user/getting-started/). Je ne couvrirai pas ces détails ici.

Si vous n'êtes pas intéressé à suivre et que vous voulez simplement accéder directement aux détails, vous pouvez cloner mon exemple fonctionnel depuis [GitHub](https://github.com/robinbobbitt/blue-green-cf-travis).

### **Installation de l'interface de ligne de commande CF et du plugin blue-green**

Puisque nous n'utilisons pas le [fournisseur de déploiement](https://github.com/travis-ci/dpl) de Cloud Foundry, nous devons installer nous-mêmes l'interface de ligne de commande Cloud Foundry, ainsi que le plugin de déploiement blue-green. Nous pouvons le faire dans la phase `before_deploy` du [cycle de vie de construction de Travis](https://docs.travis-ci.com/user/customizing-the-build/).

Notez que la phase `before_deploy` s'exécute avant chaque fournisseur de déploiement. Si vous faites des choses supplémentaires dans votre phase de déploiement, vous pouvez vouloir déplacer ces étapes dans la phase `after_success` (qui s'exécute une seule fois après une construction réussie) pour éviter des installations supplémentaires inutiles. Vous pourriez également déplacer ces étapes dans le script de déploiement lui-même, que nous allons écrire ensuite.

Quelle que soit l'endroit où vous le placez, voici le script :

```
- echo "Installation de l'interface de ligne de commande cf"
- test x$TRAVIS_OS_NAME = "xlinux" && rel="linux64-binary" || rel="macosx64"; wget "https://cli.run.pivotal.io/stable?release=${rel}&source=github" -qO cf.tgz && tar -zxvf cf.tgz && rm cf.tgz
- export PATH="$PATH:."
- cf --version
```

```
- echo "Installation du plugin de déploiement blue-green cf"
- cf add-plugin-repo CF-Community https://plugins.cloudfoundry.org
- cf install-plugin blue-green-deploy -r CF-Community -f
```

La commande pour installer l'interface de ligne de commande provient directement de la source CloudFoundry DPL [source](https://github.com/travis-ci/dpl/blob/master/lib/dpl/provider/cloud_foundry.rb). Les commandes pour installer le plugin de déploiement blue-green proviennent du [README](https://github.com/bluemixgaragelondon/cf-blue-green-deploy) du plugin.

### **Invoquer le déploiement blue-green**

Pour invoquer le déploiement blue-green, nous allons utiliser le [fournisseur de déploiement de script](https://github.com/travis-ci/dpl#script), qui exécute une commande fournie et vérifie un statut zéro comme indication de succès.

```
deploy:
  # lors de la mise à jour de la branche master, nous déployons sur Cloud Foundry
  provider: script
  skip_cleanup: true
  script:
    ./scripts/cf-blue-green-deploy.sh blue-green-cf-travis manifest.yml prod
  on:
    branch: master
```

Notez que `skip_cleanup` est défini sur `true`. Sans cela, l'interface de ligne de commande cf et le plugin de déploiement blue-green que vous venez d'installer seraient supprimés avant l'exécution du déploiement.

Le [script cf-blue-green-deploy.sh](https://github.com/robinbobbitt/blue-green-cf-travis/blob/master/scripts/cf-blue-green-deploy.sh) se connecte à l'API Cloud Foundry et invoque le plugin de déploiement blue-green. En plus de spécifier un nom d'application et un fichier manifest, vous pouvez également passer un script de test de fumée au plugin de déploiement blue-green. Le plugin appellera le script de test de fumée après que le nouveau code d'application a été déployé, mais avant que la route de l'application ne soit basculée vers la nouvelle application. Cela vous permet d'exécuter n'importe quel nombre de tests sur le nouveau code avant que le trafic réel n'y accède.

Le script de test de fumée reçoit un seul argument. L'argument est l'URL temporaire de la nouvelle application déployée. Si le script de test de fumée se termine avec succès, le déploiement blue-green se terminera en basculant la route vers la nouvelle application. Si le script de test de fumée se termine avec un échec, le trafic continue de circuler vers l'ancienne version de l'application. La nouvelle version reste disponible pour le dépannage.

Dans mon projet d'exemple, le script de test de fumée invoque une API /version et vérifie qu'elle retourne un code de statut 200.

Dans nos vrais projets au travail, nous exécutons une collection Postman contre la nouvelle application déployée. Vous voulez que votre suite de tests de fumée soit suffisamment grande pour que vous ayez confiance en votre nouveau code, mais pas si grande qu'elle prend un long temps à compléter un déploiement ou que des tests instables vous empêchent de compléter un déploiement réussi.

Vous pourriez éventuellement exécuter une suite plus complète de tests de régression en tant qu'étape `after_deploy`, après que votre nouveau code soit en ligne.

### **Effets secondaires d'un déploiement blue-green dans IBM Cloud**

Il y a quelques nuances de cette approche à connaître si vous déployez sur IBM Cloud. Parce que vous créez une nouvelle instance d'application CF chaque fois que vous déployez en blue-green, votre guid d'application changera. Si vous utilisez le service de surveillance de disponibilité, vos tests configurés seront perdus lorsque votre guid changera.

Pour contourner cela, créez une application factice permanente. Écrivez vos tests pour votre application déployée en blue-green dans la configuration de cette application factice. Vous pouvez spécifier n'importe quelle URL lorsque vous écrivez vos tests de surveillance de disponibilité.

De même, si vous utilisez le service d'analyse des logs, vous verrez que lorsque vous cliquez sur le lien "View in Kibana" dans l'onglet Logs du tableau de bord de votre application, vous serez dirigé vers une recherche Kibana sur la chaîne de guid de l'application. Les logs de l'application d'avant votre déploiement le plus récent ne s'afficheront pas. Pour contourner cela, vous pouvez simplement filtrer sur le nom de l'application plutôt que sur le guid de l'application.

Un autre service qui a le même problème est l'Auto-Scaling. Chaque fois qu'une nouvelle application est créée dans le cadre du déploiement blue-green, elle doit avoir sa politique d'Auto-Scaling reconfigurée. Il existe une interface de ligne de commande disponible que vous pourriez probablement utiliser pour scripter cela, mais je n'ai pas encore eu besoin d'essayer cela.

Si l'un de ces problèmes est un non-départ pour vous, vous avez toujours la possibilité d'écrire un script de déploiement blue-green personnalisé qui utilise deux applications CF permanentes, une blue et une green. Ces deux applications se relayeraient pour être en ligne et être inactives. Vous pourriez configurer les deux applications avec une politique d'auto-scaling, par exemple.

Bien sûr, cette approche signifie que vous ne pouvez pas tirer parti du plugin de déploiement blue-green décrit dans cet article, et vous devez maintenir votre propre script personnalisé.

### **Conclusion**

Dans cet article, nous avons examiné comment nous pouvons réaliser un déploiement à faible risque et sans temps d'arrêt en utilisant Travis et le plugin de déploiement blue-green cf.

Dans un projet réel, nous aurions encore plus de garanties, car nous aurions une suite de tests unitaires en place, et les erreurs là-bas échoueraient la construction Travis avant que le déploiement n'ait une chance de s'exécuter. Nous aurions également potentiellement des branches de développement et de staging configurées pour se déployer dans leurs propres espaces respectifs dans notre organisation Cloud Foundry, nous permettant de valider et de stabiliser l'application si nécessaire avant de promouvoir les changements en production.

Merci d'avoir lu ! C'est mon premier article Medium, et j'espère que vous l'avez trouvé utile.