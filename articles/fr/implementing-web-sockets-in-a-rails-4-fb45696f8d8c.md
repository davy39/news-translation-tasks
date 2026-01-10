---
title: Comment implémenter les WebSockets dans Rails 4
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-16T08:05:29.000Z'
originalURL: https://freecodecamp.org/news/implementing-web-sockets-in-a-rails-4-fb45696f8d8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*irjLgFzdHlA5vZBd2p_zUg.jpeg
tags:
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: sports
  slug: sports
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment implémenter les WebSockets dans Rails 4
seo_desc: 'By Arun Mathew Kurian

  WebSockets can be implemented in Rails5 using ActionCable. It can be used for enabling
  many features like chats, notifications, and other real-time modules. But, how does
  one achieve the same goal without ActionCable and Rails 5...'
---

Par Arun Mathew Kurian

Les WebSockets peuvent être implémentés dans Rails 5 en utilisant ActionCable. Il peut être utilisé pour activer de nombreuses fonctionnalités telles que les chats, les notifications et d'autres modules en temps réel. Mais comment atteindre le même objectif sans ActionCable et Rails 5 ? Ce blog traite de la manière dont nous pouvons implémenter les WebSockets dans Rails 4.

Avant de commencer, jetons un coup d'œil rapide au concept des WebSockets.

#### Que sont les WebSockets et comment fonctionnent-ils ?

La majorité du web est basée sur les requêtes/réponses HTTP. Elles permettent la communication de nombreux hôtes et clients via des transports TCP/IP. Cela signifie que les applications web ne font généralement rien après qu'un utilisateur les a visitées dans un navigateur, que la requête a été analysée et qu'une réponse a été envoyée. Tant que l'utilisateur ne clique sur rien sur la page, le serveur ne recevra aucune nouvelle requête HTTP. Par conséquent, il restera inactif.

Il existe des technologies qui permettent au serveur de démarrer la communication avec le client lorsqu'il y a des données à envoyer. Des exemples sont “Push” ou “Comet”. Il existe la technique du long polling qui maintient une connexion HTTP ouverte une fois qu'un client se connecte au serveur. Le problème avec ces approches est la surcharge de HTTP. Ce n'est pas très adapté pour les applications à faible latence.

C'est là que les WebSockets entrent en jeu. Il s'agit d'une API qui fournit des connexions persistantes de type “socket” entre un serveur et un client. Cela permet au serveur et au client d'envoyer des données à tout moment.

Dans ce blog, nous allons créer un site d'enchères de joueurs de cricket en ligne qui utilise les web sockets dans Rails 4. Le site peut être utilisé par plusieurs utilisateurs pour enchérir sur le même joueur. Le défi est de mettre à jour l'enchère sans recharger la page et en maintenant la communication en direct.

### Démarrage

Principalement, trois gems sont utilisées pour implémenter la fonctionnalité de web socket :

**Gemfile**

```
gem ‘faye’gem ‘thin’, require: falsegem ‘render_sync’
```

Le **thin** est un serveur Ruby petit et rapide. Il doit être installé avec faye, car la gemme faye ne fonctionne pas avec des serveurs comme webrick.

La gemme suivante importante est **faye**. Faye est un ensemble d'outils pour la messagerie simple de type publication-abonnement (publish-subscribe) entre clients web. Il est livré avec des serveurs de routage de messages faciles à utiliser pour les applications Node.js et Rack, et des clients qui peuvent être utilisés sur le serveur et dans le navigateur.

La gemme **sync** ou **render_sync** est utilisée pour créer des partials en temps réel avec Rails. Sync vous permet de rendre des partials pour des modèles qui, avec un minimum de code, se mettent à jour en temps réel dans le navigateur lorsque des changements surviennent sur le serveur.

Notre objectif est d'avoir une fonctionnalité qui permet d'afficher les valeurs des enchères sur la page show d'un utilisateur. La première étape pour implémenter cela est d'installer les templates de la gemme sync.

> **_rails generate sync:install_**

Et inclure sync dans notre pipeline d'assets.

**app/assets/javascripts/application.js**

```
//= require jquery//= require jquery_ujs//= require turbolinks//= require sync//= require_tree
```

Le script de configuration est requis dans le layout de l'application

**app/views/layouts/application.html.erb**

```
<%= include_sync_config %>
```

Nous devons créer un partial et le stocker dans le répertoire **views/sync/** sous le nom **_bid_log_row.html.erb.**

Ce partial contient la valeur de l'enchère de l'utilisateur. Il ressemblera à ceci :

```
Enchère actuelle : <%= @bid_log.amount || ‘ — ‘ rescue nil%>
```

Et afin de rendre cela dans la page show, ajoutez les lignes suivantes dans la page show des utilisateurs :

**app/views/users/show.html.erb**

```
<%= sync partial: ‘bid_log_row’, resource: @bid_log %><%= sync_new partial: ‘bid_log_row’, resource: BidLog.new %>
```

Et enfin, effectuez les modifications dans le BidLogsController afin qu'il sache comment gérer les soumissions de formulaires à distance. Il synchronise également les nouvelles enchères en place.

```
class BidLogsController < ApplicationControllerrespond_to :html, :js
```

```
 def index  @bid_logs = BidLog.all  @new_bid = current_user.bid_logs.build  end
```

```
 def create  @bid_log = current_user.bid_logs.build(bid_log_params)  if @bid_log.save   sync_new @bid_log  end  respond_to do |format|   format.html { redirect_to user_path(@bid_log.player_id) }   format.json { head :no_content }  end end
```

```
private
```

```
 def bid_log_params  params.require(:bid_log).permit(:amount, :player_id) end
```

```
end
```

### Configuration

Maintenant, la partie codage de base est terminée. L'étape suivante consiste à configurer Faye. Faye doit s'exécuter sur un serveur web distinct de l'application web elle-même. Pour ce faire, vous devez créer un fichier de configuration Rackup. Ajoutez un fichier faye.ru à la racine du projet et assurez-vous qu'il ressemble à ceci :

```
require ‘faye’
```

```
bayeux = Faye::RackAdapter.new(:mount => ‘/faye’, :timeout => 25)
```

```
bayeux.listen(9292)
```

Ce fichier indique simplement à Rackup comment démarrer le serveur Faye. Essayez-le pour vous assurer qu'il fonctionne correctement. Exécutez ceci dans votre terminal :

> **_rackup faye.ru -E production -s thin_**

### Conclusion

Maintenant, nous sommes prêts. L'application peut être lancée en démarrant le serveur Rails. Le code associé à ce blog peut être trouvé [ici](https://github.com/jayakrishnang/AuctionManager-Sample-Bidding-App).