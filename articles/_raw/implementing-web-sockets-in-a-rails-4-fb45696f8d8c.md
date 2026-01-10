---
title: How to implement WebSockets in Rails 4
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
seo_title: null
seo_desc: 'By Arun Mathew Kurian

  WebSockets can be implemented in Rails5 using ActionCable. It can be used for enabling
  many features like chats, notifications, and other real-time modules. But, how does
  one achieve the same goal without ActionCable and Rails 5...'
---

By Arun Mathew Kurian

WebSockets can be implemented in Rails5 using ActionCable. It can be used for enabling many features like chats, notifications, and other real-time modules. But, how does one achieve the same goal without ActionCable and Rails 5? This blog deals with how we can implement WebSockets in Rails 4.

Before we start, let’s have a quick look at the concept of WebSockets.

#### What are WebSockets and how do they work?

The majority of the web is based on HTTP request/responses. They enable the communication of many hosts and clients over TCP/IP transports. This means that web applications usually don’t do anything after a user visits them in a browser and parses the request and sends a response. Until the user clicks something on the page, the server won’t receive any new HTTP request. Therefore it will stand idle.

There are technologies that enable the server to start communication with the client when there is data to be sent. Examples are “Push” or “Comet”. There is the long polling technique which keeps an HTTP connection open once a client connects to the server. The bad thing with these approaches is the overhead of HTTP. It isn’t very good for low latency applications.

This is where WebSockets come into the picture. They are an API that provides “socket” persistent connections between a server and a client. This enables both server and client to send data at any time.

In this blog, we will create an online cricket player auction site that uses web sockets in Rails 4. The site can be used by multiple users to bid for the same player. The challenge is to update the bid without reloading the page and keeping up the live communication.

### Getting started

Mainly three gems are used for implementing the web socket functionality:

**Gemfile**

```
gem ‘faye’gem ‘thin’, require: falsegem ‘render_sync’
```

The **thin** is a small and fast ruby server. It should be installed with faye, as the faye gem doesn’t work with servers like webrick.

The next important gem is **faye**. Faye is a set of tools for simple publish-subscribe messaging between web clients. It ships with easy-to-use message routing servers for Node.js and Rack applications, and clients that can be used on the server and in the browser.

The **sync** or **render_sync** gem is used to create real-time partials with Rails. Sync lets you render partials for models that, with minimal code, update in real-time in the browser when changes occur on the server.

Our objective is to have a functionality which allows displaying the bid values on the show page of a user. The first step for implementing this is to install templates from the sync gem.

> **_rails generate sync:install_**

And require sync in our asset pipeline.

**app/assets/javascripts/application.js**

```
//= require jquery//= require jquery_ujs//= require turbolinks//= require sync//= require_tree
```

The configuration script is required in the application layout

**app/views/layouts/application.html.erb**

```
<%= include_sync_config %>
```

We need to create a partial and store it in the directory **views/sync/** as **_bid_log_row.html.erb.**

This partial contains the value of the user’s bid. It will look like this:

```
Current Bid: <%= @bid_log.amount || ‘ — ‘ rescue nil%>
```

And in order to render this in the show page, add the following lines in the users show page:

**app/views/users/show.html.erb**

```
<%= sync partial: ‘bid_log_row’, resource: @bid_log %><%= sync_new partial: ‘bid_log_row’, resource: BidLog.new %>
```

And lastly, make the changes in the BidLogsController so it knows how to handle remote form submissions. It also syncs the new bids in place.

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

Now the basic coding part is done. Next step is to configure Faye. Faye needs to run on a separate web server from the web application itself. To accomplish this, you need to create a Rackup config file. Add a faye.ru file to the root of the project and make sure it looks like this:

```
require ‘faye’
```

```
bayeux = Faye::RackAdapter.new(:mount => ‘/faye’, :timeout =&gt; 25)
```

```
bayeux.listen(9292)
```

This file simply tells Rackup how to start the Faye server. Try it out to ensure that it’s working correctly. Run this in your Terminal:

> **_rackup faye.ru -E production -s thin_**

### Wrapping up

Now we are good to go. The application can be run by starting the Rails server. The code associated with this blog can be found [here](https://github.com/jayakrishnang/AuctionManager-Sample-Bidding-App).

