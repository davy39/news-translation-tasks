---
title: Comment créer un site portfolio – Un guide pour les développeurs débutants
subtitle: ''
author: Jemima Abu
co_authors: []
series: null
date: '2021-03-29T22:29:35.000Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-creating-a-portfolio-website
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/A-Beginner-s-Guide-To-Creating-A-Portfolio-Website-1.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: personal development
  slug: personal-development
- name: portfolio
  slug: portfolio
- name: Website design
  slug: website-design
seo_title: Comment créer un site portfolio – Un guide pour les développeurs débutants
seo_desc: "At the beginning of 2021, I decided to revamp my portfolio site, as I do\
  \ every other year. \nIf you've never deployed a website before, it can be quite\
  \ confusing figuring out how to get your website online. Things like getting a domain\
  \ name, uploading..."
---

Au début de l'année 2021, j'ai décidé de rénover [mon site portfolio](https://www.jemimaabu.com), comme je le fais tous les deux ans.

Si vous n'avez jamais déployé de site web auparavant, il peut être assez confus de comprendre comment mettre votre site en ligne. Des choses comme obtenir un nom de domaine, télécharger les fichiers nécessaires et choisir où héberger votre site peuvent être écrasantes.

Je me souviens à quel point j'ai trouvé difficile de configurer mon site web la première fois et je voulais aider les autres à éviter les erreurs que j'ai faites, alors j'ai envoyé ce tweet :

![Tweet de @jemimaabu sur Twitter. Le texte dit "Aii, je change à nouveau la conception de mon site web. Cette fois, je veux avoir une session de programmation en binôme avec quelqu'un qui essaie de configurer un site portfolio. Nous discuterons de tout ce que vous devez savoir, de l'obtention d'un nom de domaine à la mise en ligne du site web. Envoyez-moi un DM". 12:15. 24 janv. 2021. Twitter pour Android](https://www.freecodecamp.org/news/content/images/2021/03/portfolio-tweet.png)

J'ai reçu plus de réponses que prévu, alors j'ai fini par planifier 9 sessions de 2 heures chacune pour chaque week-end de février.

L'idée était qu'à la fin de février, j'aurais terminé la conception de mon portfolio puisque je supposais qu'aider les autres me permettrait de rester sur la bonne voie avec mon plan. Ce plan n'a pas fonctionné, mais j'ai beaucoup appris en cours de route.

À la fin de février, j'ai aidé avec succès 6 développeurs (allant du niveau débutant à intermédiaire, avec un ratio de 1:2 femmes-hommes de 3 pays différents) à configurer leur site portfolio d'une manière ou d'une autre. Je vais documenter les principales leçons de chaque session ici.

Dans cet article, nous allons couvrir tout ce que vous devez savoir sur la configuration de votre site portfolio – de l'achat d'un nom de domaine à la mise en ligne du site. Alors, commençons.

## 1) Comment obtenir un nom de domaine

Un nom de domaine est l'emplacement de votre site en ligne. C'est comme avoir un nom d'utilisateur pour le world wide web que les visiteurs tapent dans la barre d'URL pour accéder à votre site.

Un nom de domaine se compose d'un nom (comme `google`) et d'une extension (comme `.com`) et il pointe vers une adresse IP spécifique pour le site que vous déployez.

![Barre d'URL montrant "http://www."](https://www.freecodecamp.org/news/content/images/2021/03/domain.jpeg)

L'achat d'un nom de domaine auprès d'un registre vous permet de déterminer vers quel emplacement ce domaine pointe. Il existe plusieurs registres où vous pouvez acheter un domaine, alors vous devriez faire vos recherches et décider lequel vous convient le mieux.

Voici quelques registres de domaines que je recommande en fonction de leurs caractéristiques :

1. **[NameCheap](https://shareasale.com/r.cfm?b=1197848&u=2778801&m=46483&urllink=&afftrack=0https://www.shareasale.com/r.cfm?u=2778801&m=46483&b=518798)** – C'est l'une des plateformes les plus populaires, donc elle offre beaucoup de support client et une configuration sans tracas. Ils offrent également une confidentialité de domaine gratuite. Je recommande d'utiliser cela si vous voulez acheter un domaine rapidement.
2. **[Bluehost](https://www.bluehost.com/track/jemabu)** – Bluehost offre de grandes options d'hébergement et dispose d'une plateforme WordPress intégrée. J'ai personnellement utilisé Bluehost pour certains sites clients dans le passé et j'aime vraiment l'interface propre et le guide d'intégration qu'il fournit. Je recommande d'utiliser Bluehost pour héberger des sites WordPress.
3. **[NameSilo](https://www.namesilo.com/?rid=17e7856ns)** – Un avantage majeur de NameSilo est qu'ils offrent des [add-ons gratuits](https://www.namesilo.com/pricing?rid=17e7856ns) tels que la confidentialité WHOIS (garder vos détails d'enregistrement en sécurité) et la redirection d'e-mails (envoyer des e-mails de `me@mysite.com` à votre adresse e-mail réelle). Je recommande d'utiliser cela si vous avez besoin de nombreux add-ons supplémentaires sur votre domaine.
4. **[Netim](https://www.netim.com/?partnerid=AJ2220)** – Je recommande d'utiliser Netim pour acheter des domaines géographiques tels que `.eu` ou `.me`. Une option amusante est d'acheter un domaine qui se termine par les derniers caractères de votre nom, par exemple `www.jemi.ma`.

> Méfiez-vous des frais cachés lors de l'achat d'un domaine. De nombreux registres ont tendance à offrir des noms de domaine très bon marché, voire gratuits, mais il y a généralement des frais supplémentaires dans la méthode de renouvellement. Faites attention aux add-ons dont vous n'avez peut-être pas besoin.

Plusieurs des développeurs lors des sessions de programmation en binôme avaient payé pour des noms de domaine `.com`, mais la majorité ne possédait pas de nom de domaine et n'était pas intéressée à en acheter un, du moins pour l'instant.

Les avantages d'avoir un nom de domaine personnalisé sont :

* cela améliore vos classements SEO
* cela semble plus professionnel lorsque vous envoyez un lien à un employeur ou client potentiel.

Les fournisseurs de domaines facturent les noms de domaine annuellement, et un domaine `.com` peut vous coûter entre 10 et 30 dollars par an, selon les éventuelles additions.

Si vous n'êtes pas à l'aise avec l'idée de payer pour un nom de domaine pour l'instant, vous pouvez opter pour une option de domaine gratuit. Nous explorerons les options de domaine gratuit dans la section suivante.

## 2) Comment choisir une plateforme d'hébergement

Lorsque vous construisez un site web, vous pouvez y accéder sur votre machine en allant sur `localhost` ou index.html. Cependant, si vous voulez que d'autres personnes puissent accéder à votre site web sur Internet, vous devez le télécharger sur une plateforme d'hébergement.

Une plateforme d'hébergement est le `localhost` d'Internet – c'est un serveur accessible par tous.

La plupart des registres de domaines offrent également des options d'hébergement, mais il n'est pas nécessaire d'avoir votre domaine et votre hébergement au même endroit, car la plupart des registres facturent des frais supplémentaires pour l'hébergement. Une fois que vous avez acheté un nom de domaine, vous pouvez utiliser n'importe quelle plateforme d'hébergement que vous souhaitez.

Il existe un certain nombre de plateformes d'hébergement qui offrent un hébergement et des noms de domaine gratuits (avec le domaine de la plateforme attaché) et vous pouvez choisir n'importe quelle plateforme en fonction de la manière dont vous souhaitez structurer votre portfolio.

Explorons les options suivantes.

### Comment héberger un site portfolio sans écrire de code

**Plateforme : [webflow.com](https://webflow.grsm.io/jemabu)**

![Une image de la page d'accueil de webflow.com. L'image contient le texte "La manière moderne de construire pour le texte. Webflow permet aux designers de créer des sites web professionnels et personnalisés dans un canevas entièrement visuel sans code."](https://www.freecodecamp.org/news/content/images/2021/03/webflow.png)

Webflow est un site de glisser-déposer qui vous permet de créer des sites web magnifiques en écrivant peu ou pas de code.

Avec Webflow, vous pouvez créer des mises en page et des animations incroyables en utilisant les fonctions HTML et CSS sur leur tableau de bord, et il est livré avec un CMS intégré afin que vous n'ayez pas à vous soucier de la mise à jour du contenu ou du stockage des images.

Webflow offre une option de domaine gratuit avec une extension `webflow.io`, par exemple `myportfolio.webflow.io`. Avec cette option, vous pouvez créer un site statique avec 2 pages. Ils ont également une [vitrine de projets](https://webflow.grsm.io/jadsc) que vous pouvez cloner et [un forum en ligne](https://webflow.grsm.io/jafrm) où vous pouvez obtenir des réponses à la plupart de vos questions.

Je recommande Webflow aux designers et développeurs qui ont des connaissances en mises en page et animations CSS et qui veulent configurer rapidement leur site.

### Comment héberger un portfolio statique construit avec HTML et CSS

**Plateforme** : **[GitHub Pages](https://pages.github.com/)**

![GitHub Pages Sites web pour vous et vos projets. Hébergés directement depuis votre dépôt GitHub. Il suffit de modifier, de pousser, et vos modifications sont en ligne.](https://www.freecodecamp.org/news/content/images/2021/03/gitpages.png)

GitHub Pages est une fonctionnalité de la plateforme GitHub qui vous permet d'afficher le code de votre dépôt sur un site `github.io` – donc l'URL ressemblerait à `my-portfolio.github.io`

Les pages GitHub sont mieux adaptées aux sites web statiques (c'est-à-dire un site construit avec HTML et CSS avec un contenu fixe et aucune interaction serveur ou processus de construction nécessaire). C'est aussi très simple à configurer et peut prendre aussi peu que 10 minutes pour mettre votre site en ligne.

Pour créer une page GitHub, votre dépôt doit inclure un fichier `index.html` dans le dossier racine. Ensuite, allez sur la page des paramètres de votre dépôt et sélectionnez votre branche principale comme source dans la section GitHub Pages.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-13-at-18.01.23.png)

C'était la méthode utilisée par la plupart des développeurs lors des sessions de programmation en binôme, car elle prenait le moins de temps et avait peu ou pas de complications. Je recommande GitHub Pages pour les développeurs débutants qui veulent déployer rapidement leurs sites statiques.

### Comment héberger un site qui utilise un framework comme React ou Vue

**Plateforme :** **[Netlify](https://www.netlify.com/)**

![Page d'accueil de Netlify. Applications web modernes livrées plus rapidement Un flux de travail intuitif basé sur Git et une puissante plateforme serverless pour construire, déployer et collaborer sur des applications web](https://www.freecodecamp.org/news/content/images/2021/03/netlify.png)

Si vous construisez votre site web avec un framework front-end qui nécessite un processus de construction, Netlify est votre meilleur choix. Il est parfait pour les sites dynamiques (c'est-à-dire un site qui génère du contenu à partir d'un serveur ou qui a des fonctionnalités nécessitant des scripts – comme l'envoi de messages via un formulaire de contact) et il fonctionne également avec les sites statiques.

[Netlify dispose d'une excellente documentation](https://www.netlify.com/topics/tutorials/) qui fournit des informations sur toutes les questions que vous pourriez avoir concernant l'utilisation du site. Il dispose également de fonctionnalités clés pour améliorer votre site comme [Netlify Forms](https://www.netlify.com/products/forms/) qui vous permettent de configurer un formulaire de contact sur votre site sans code côté serveur.

J'utilise actuellement Netlify pour héberger mon site et c'est ma plateforme préférée jusqu'à présent. Je la recommande aux développeurs qui veulent mettre leur site (statique ou dynamique) en ligne sans tracas pour configurer un processus de construction.

### Comment héberger un site avec un serveur backend

**Plateforme :** **[Heroku](https://heroku.com)**

![Image](https://www.freecodecamp.org/news/content/images/2021/03/heroku.png)

Si votre site portfolio nécessite des données d'un serveur backend (comme obtenir une liste de vos projets à partir d'une application RESTful), alors vous devrez également déployer ce serveur pour que le frontend puisse y accéder.

Heroku est une plateforme qui vous permet de déployer des applications backend dans huit langages pris en charge (y compris Node.js et Python). Elle permet également de déployer des sites frontend statiques et dynamiques afin que vous puissiez créer deux projets – un pour votre code frontend et l'autre pour l'application backend.

Vous pouvez visiter le [Heroku Dev Center](https://devcenter.heroku.com/) pour plus d'informations sur la prise en main de Heroku.

Je n'ai pas personnellement utilisé la plateforme Heroku pour déployer des applications backend auparavant, mais l'un des programmeurs lors de la session de programmation en binôme l'a fait, alors j'ai pensé l'inclure également. Je la recommande aux développeurs full-stack qui veulent afficher leurs compétences frontend et backend sur leur portfolio.

## 3) Comment déployer votre site

Déployer un site signifie placer le code que vous avez écrit sur la plateforme d'hébergement. Sur les anciennes plateformes, vous deviez télécharger le code et toutes les ressources vers un cPanel (qui est essentiellement l'explorateur de fichiers pour les plateformes d'hébergement).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/cpanel.png)
_Source : **À quoi sert cPanel et pourquoi en ai-je besoin ? - A2Hosting**_

De nos jours, les sites web sont devenus beaucoup plus compliqués que de simples fichiers `.html`, donc ils nécessitent différentes méthodes de déploiement.

Si vous avez une application React, par exemple, le projet devra être construit (comme lorsque vous exécutez `npm start` sur votre ordinateur portable pour voir l'application) chaque fois qu'il est déployé sur le domaine.

Selon la plateforme d'hébergement que vous avez choisie, la méthode de déploiement est différente. Vous pouvez configurer le déploiement continu à partir d'un dépôt GitHub sur Netlify ([documentation ici](https://docs.netlify.com/configure-builds/get-started/)) et Heroku ([documentation ici](https://devcenter.heroku.com/articles/github-integration)). Cela signifie que chaque fois que vous poussez un nouveau changement vers votre dépôt, le changement est reflété dans votre site.

![Créer un nouveau site De zéro à héros, trois étapes faciles pour mettre votre site sur Netlify. Se connecter au fournisseur Git Choisir un dépôt Paramètres du site, et déployer ! Déploiement continu Choisissez le fournisseur Git où le code source de votre site est hébergé. Lorsque vous poussez vers Git, nous exécutons votre outil de construction de choix sur nos serveurs et déployons le résultat.](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-13-at-19.04.00.png)

Si vous choisissez d'utiliser un nom de domaine personnalisé, vous devrez lier ce nom de domaine à votre site. Par exemple, sur Netlify, votre application est créée avec une extension `netlify.app` par défaut, donc elle ressemble à `myportfolio.netlify.app`, mais vous pouvez [définir un nom de domaine personnalisé](https://docs.netlify.com/domains-https/custom-domains/). Vous pouvez également définir un [nom de domaine personnalisé sur Heroku](https://devcenter.heroku.com/articles/custom-domains).

Lier un domaine personnalisé sur ces plateformes signifie que vous devrez mettre à jour les enregistrements DNS (Domain Name System) de votre fournisseur de domaine. Le DNS est ce qui permet aux utilisateurs d'accéder à votre site avec votre nom de domaine, par exemple `portfolio.com` au lieu d'une adresse IP comme `127.0.0.1`. Vous pouvez en lire plus sur le [DNS ici](https://www.freecodecamp.org/news/what-is-dns/).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/godaddy.gif)
_Source : Ajouter un enregistrement A - GoDaddy_

## 4. Comment choisir un design pour votre site

Un autre sujet que nous avons abordé lors des sessions était le choix d'un design. Certains des développeurs avaient déjà leurs sites construits, mais d'autres n'avaient aucune idée du type de mise en page à adopter.

En ce qui concerne le choix d'un design de portfolio, je recommande de consulter les portfolios d'autres développeurs pour trouver de l'inspiration et des idées sur la manière de structurer votre site. Cet article montre [**15 Portfolios de Développeurs Web**](https://www.freecodecamp.org/news/15-web-developer-portfolios-to-inspire-you-137fb1743cae/) ou, si vous avez besoin de plus d'inspiration, essayez [**63 Exemples**](https://www.noupe.com/design/web-developer-portfolio-examples.html).

Vous pouvez également lire cet article sur **[5 Projets à Inclure dans Votre Portfolio Front End](https://www.freecodecamp.org/news/coding-projects-to-include-in-your-frontend-portfolio/)** pour des idées de projets.

Il est important de déterminer le but de votre portfolio et de vous assurer que ce but est évident dans chaque partie de votre site.

Par exemple, si vous essayez d'utiliser votre portfolio pour obtenir un emploi, assurez-vous de mettre en avant vos compétences et votre expérience sur la page principale et incluez des appels à l'action pour permettre aux gens de consulter votre CV ou de vous envoyer un message.

Si votre portfolio est destiné à vous obtenir des clients pour des travaux freelance, concentrez-vous sur les projets précédents que vous avez réalisés et les avis d'autres clients.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/employ-adam.jpg)
_Source : https://www.bmediagroup.com/news/employ-adam/_

## Conclusion

Récapitulons ce que nous avons couvert dans cet article. Pour déployer votre site en ligne, vous devrez :

1. Acheter un domaine auprès d'un fournisseur de domaines.
2. Choisir une plateforme d'hébergement, en fonction de la manière dont vous souhaitez construire votre site.
3. Lier votre domaine à votre plateforme d'hébergement en mettant à jour vos enregistrements DNS auprès de votre fournisseur de domaines.
4. Configurer le déploiement de votre site à partir de votre plateforme d'hébergement selon leur documentation.

J'ai écrit cet article et proposé les sessions de programmation en binôme parce que je me souviens à quel point il était compliqué de déployer mon premier site web. Je me souviens également des nombreuses erreurs que j'ai faites et que j'aurais pu éviter (comme payer 10 fois le tarif initial lors du renouvellement de l'un de mes domaines grâce à une série d'add-ons dont je n'avais pas besoin), alors j'espère que vous l'avez trouvé utile.

Si c'est le cas, ou si vous avez d'autres questions, vous pouvez me le faire savoir sur [Twitter](https://www.twitter.com/jemimaabu) ou m'envoyer un message sur mon [site web](https://www.jemimaabu.com#contact).