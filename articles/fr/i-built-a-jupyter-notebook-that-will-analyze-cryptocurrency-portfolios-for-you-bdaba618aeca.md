---
title: J'ai créé un Jupyter Notebook qui analysera vos portefeuilles de cryptomonnaies
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-20T10:35:13.000Z'
originalURL: https://freecodecamp.org/news/i-built-a-jupyter-notebook-that-will-analyze-cryptocurrency-portfolios-for-you-bdaba618aeca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yclB_TfehNu8DxAADDBzXg.png
tags:
- name: Bitcoin
  slug: bitcoin
- name: Cryptocurrency
  slug: cryptocurrency
- name: data scientist
  slug: data-scientist
- name: Investing
  slug: investing
- name: Python
  slug: python
seo_title: J'ai créé un Jupyter Notebook qui analysera vos portefeuilles de cryptomonnaies
seo_desc: 'By Grant Bartel

  The amount of engagement in the crypto investment space needs no introduction. With
  market caps, volumes, and public awareness on the rise, I thought I’d put together
  a simple Jupyter notebook to get a clearer and broader viewpoint in...'
---

Par Grant Bartel

L'ampleur de l'engagement dans l'espace d'investissement crypto n'a besoin d'aucune introduction. Avec [les capitalisations boursières, les volumes et la notoriété publique en hausse](http://www.ibtimes.co.uk/year-cryptocurrencies-became-mainstream-1654616), j'ai pensé mettre ensemble un simple Jupyter notebook pour obtenir une vue plus claire et plus large des activités d'investissement au sein de mon propre portefeuille crypto.

TL;DR [voici le code](https://github.com/grantathon/crypto_portfolio_analysis) ;)

### Pourquoi devrions-nous analyser nos portefeuilles ?

Parce que nous manquons définitivement des détails importants sur nos investissements en ne regardant que la valeur totale de nos portefeuilles (potentiellement bien garnis) — même si j'aime regarder Blockfolio de temps en temps. Parce que voir notre Ripple s'envoler et éclipser le reste de nos investissements augmente probablement substantiellement notre risque financier. Parce que nous voulons tous que notre argent croisse, mais y parvenir en choisissant un ensemble diversifié de cryptos est plus facile et plus sûr que de choisir un coup de poker qui pourrait finir en échec (et nous ruiner).

Et soyons réalistes, les gains du marché sont simplement trop importants pour que nous restions dans l'ignorance des véritables caractéristiques de nos portefeuilles d'investissement.

### Caractéristiques importantes du portefeuille

Il existe plusieurs caractéristiques de notre portefeuille que nous devrions examiner attentivement, y compris le rendement **et** le risque. Mais souvent, nous nous fixons sur l'un et pas sur l'autre.

Nous pouvons examiner le rendement de plusieurs manières : le montant d'argent que nous avons gagné depuis le début jusqu'à la date actuelle, le taux moyen d'argent que nous avons gagné sur des périodes spécifiques (par exemple, les rendements annuels), la performance de nos investissements par rapport à plusieurs caractéristiques d'un benchmark (par exemple, [alpha](https://www.investopedia.com/terms/a/alpha.asp)), et même le taux de croissance annuel composé qu'il aurait fallu pour atteindre notre investissement actuel basé sur notre point de départ (c'est-à-dire, [CAGR](https://en.wikipedia.org/wiki/Compound_annual_growth_rate)).

Tout aussi important, sinon plus, est la manière dont nous examinons le risque et son effet sur le rendement. Je ne sais pas pour vous, mais je veux m'assurer que je fais un bon rendement basé sur un niveau de risque avec lequel je me sens à l'aise. Si nous prenons un énorme risque pour obtenir un rendement particulier alors que nous aurions pu prendre beaucoup moins de risque pour obtenir ce même rendement, le chemin à prendre pour un investissement plus **efficient** est clair.

C'est là que la compréhension de la volatilité, des corrélations et des rendements ajustés au risque entrent en jeu en calculant des statistiques telles que l'écart-type des rendements (ou volatilité), [bêta](https://www.investopedia.com/terms/b/beta.asp), le [ratio de Sharpe](https://en.wikipedia.org/wiki/Sharpe_ratio), et le [ratio de Sortino](https://en.wikipedia.org/wiki/Sortino_ratio).

Et bien que nous puissions calculer toutes les statistiques sous le soleil pour mesurer la performance de notre portefeuille, cela ne sert pas à grand-chose si nous n'incluons pas un point de référence pour voir comment nous nous en sortons en comparaison. Cela s'appelle un [benchmark](https://www.investopedia.com/terms/b/benchmark.asp), et nous utiliserons le chouchou des cryptomonnaies : Bitcoin.

### Présentation du Notebook

Je ne veux pas afficher un tas de code ici parce que je pense que vous devriez parcourir le notebook vous-même et vous familiariser avec les choses. N'ayez pas peur, le notebook inclut des explications claires et le code est commenté ! Cela vous aidera également à mieux comprendre cet article. Si vous le souhaitez, clonez [le dépôt](https://github.com/grantathon/crypto_portfolio_analysis) et essayez-le d'abord. Cependant, je vais vous montrer des résultats à travers quelques statistiques et de belles visualisations.

Pour commencer, nous devons créer une feuille de transactions qui émule la manière dont nous avons investi notre portefeuille. Celle ci-dessous est incluse dans [le dépôt](https://github.com/grantathon/crypto_portfolio_analysis). Ce sont en fait les mêmes cryptos dans lesquels j'ai investi et les moments où je les ai achetés et vendus jusqu'à présent, mais le montant d'argent et les allocations (c'est-à-dire, le montant que j'ai acheté et vendu) ne sont pas ;)

![Image](https://cdn-media-1.freecodecamp.org/images/XzoSg0XtQ6s8pL4cdk3sKG-k381rkitWdTtr)

Vous pouvez considérer la feuille de transactions comme notre **stratégie d'investissement**. Ce sont les transactions que nous avons décidé de prendre en fonction de nos pouvoirs de sorcellerie ou de ce qu'un algorithme nous a dit.

![Image](https://cdn-media-1.freecodecamp.org/images/sikS8FYcWs5FmvVcfZY2naHH5UxGyMPDn3PJ)
_Source : [Playstarbound](https://community.playstarbound.com/threads/glitch-ship-ai-feedback.80652/page-11" rel="noopener" target="_blank" title=")_

Avec la feuille de transactions, nous avons également besoin de données de marché historiques. J'ai choisi de faire quelque chose de simple : télécharger quelques CSVs depuis [CoinGecko](https://www.coingecko.com/) et les mettre dans un dossier de données. Tirer des données d'une API serait mieux cependant !

Maintenant, nous voulons exécuter un backtest sur notre stratégie d'investissement. En termes simples, exécuter un backtest nous permet de revenir dans le temps à notre première transaction, d'avancer dans le temps et de simuler l'activité de trading qui s'est produite dans notre portefeuille jusqu'à aujourd'hui. Un backtester peut être très sophistiqué et peut être utilisé dans de nombreux scénarios différents (pour les passionnés de finance : jeu de mots intentionnel), mais dans notre cas, c'est plutôt simple.

![Image](https://cdn-media-1.freecodecamp.org/images/I05CqzVIRz3ccjLIjcy85QUBz5apBZ4xWAcG)

Sur la base des statistiques ci-dessus, il est clair que notre portefeuille s'est plutôt bien comporté par rapport à notre benchmark. Les rendements sont meilleurs, la volatilité n'est que légèrement pire, et notre bêta est surprenamment inférieur à 100 %. Et regardez cet alpha !

OK. Les chiffres sont bien, mais je veux voir quelques graphiques.

![Image](https://cdn-media-1.freecodecamp.org/images/pnWUDH7fXvwbY-DlQ2wiYuK1inrGjP4P9vnY)

Cela semble intimidant. Le graphique ci-dessus montre comment la valeur en USD de notre portefeuille a évolué au fil du temps, y compris tous nos flux de trésorerie (c'est-à-dire, dépôts et retraits). Bien que ce soit bien de visualiser cela, il est difficile d'avoir une idée claire de la performance réelle de notre portefeuille lorsque les flux de trésorerie sont inclus. Par exemple, si j'ai déposé 1 million de dollars (je souhaite), le portefeuille semblerait avoir un énorme pic !

![Image](https://cdn-media-1.freecodecamp.org/images/aI9DYZ7J2guZE1BcBaJ04dLfbPDaavgNcBPm)

C'est mieux. En supprimant les rendements quotidiens lorsque des flux de trésorerie ont été observés, nous avons une représentation plus précise de la véritable performance de notre portefeuille. Heureusement, nous avons un très petit nombre de flux de trésorerie, donc cette méthode est acceptable. Comme vous pouvez le voir, il nous a fallu un certain temps pour rattraper Bitcoin, mais nous l'avons fait et finalement dépassé (merci [Golem](https://golem.network/) et [NEO](https://neo.org/)).

![Image](https://cdn-media-1.freecodecamp.org/images/H5PJZhnLSD23zJVoy7jFUAO8vDDzNGesxa3c)

En fait, vous pouvez voir qu'après le boom fou de Bitcoin, Ethereum et Litecoin (aka le boom de Coinbase), notre portefeuille est devenu plus diversifié. Cela a sûrement eu beaucoup à voir avec l'atténuation des baisses à venir de Bitcoin et les rendements probablement plus élevés exprimés parmi les actifs nouvellement ajoutés.

![Image](https://cdn-media-1.freecodecamp.org/images/jD3HVn19ylfyNF6clE3QMxThd9ZbX6Q0WGVH)

Eh bien, voilà. Clairement, notre portefeuille a connu beaucoup moins de volatilité (c'est-à-dire, risque) après la diversification. La diversification (et la chance) pour la victoire !

![Image](https://cdn-media-1.freecodecamp.org/images/BcXX6mRbl6s-S5cUvheXUxWzYQNLcNAbIQbd)

Pour moi, c'est le graphique le plus intéressant. Il s'agit d'une matrice qui représente les corrélations entre tous les actifs de notre portefeuille. Bien que de nombreux actifs aient eu une [corrélation moyenne à élevée](https://statistics.laerd.com/statistical-guides/pearson-correlation-coefficient-statistical-guide.php) les uns avec les autres, [Bitcoin Cash](https://www.bitcoincash.org/) avait une très faible corrélation avec chaque actif. Vous pouvez même voir qu'il était négativement corrélé avec [OmiseGO](https://omisego.network/) ! Les corrélations changent avec le temps, mais il est néanmoins intéressant de voir ces types de relations au sein de notre portefeuille.

Encore une fois, allez-y et clonez [le dépôt](https://github.com/grantathon/crypto_portfolio_analysis) et jouez un peu pour que vous puissiez comprendre en détail comment nous avons analysé notre portefeuille. Vous pouvez même ajouter votre propre feuille de transactions pour avoir un aperçu du vôtre. Et si vous trouvez des bugs, faites-le moi savoir !

### Résumé

J'espère que vous avez acquis une meilleure appréciation de l'importance de regarder votre portefeuille à travers diverses lentilles. Il est difficile d'avoir une compréhension claire en visualisant simplement les mouvements de prix des actifs, surtout avec tout ce qui s'est passé récemment dans l'espace crypto. De plus, il n'est pas toujours clair combien de risque nous prenons au fil du temps, et comment ces risques évolueront lorsque nous investirons.

Ce qui est clair, c'est que la diversification dans un tel marché est importante, car aucun de nous ne sait où ce marché va. Dans cette optique, mieux vaut garder un œil sur votre navire tout en affrontant les tempêtes et HODL.

Au fait, rien de tout cela ne doit être considéré comme un conseil en investissement et il en va de même pour le code. Quels que soient les investissements que vous poursuivez, ils sont purement à votre propre discrétion.

Divulgation complète : Au moment de la rédaction de cet article, j'avais investi dans BCH, BTC, ETH, GNT, LTC, NEO et OMG.

_Je suis Grant et je suis un professionnel indépendant du SEO et du contenu. Si vous cherchez à augmenter le trafic de recherche organique de votre marque, je peux vous aider avec votre [SEO fintech](https://www.writefintech.com/). Santé !_