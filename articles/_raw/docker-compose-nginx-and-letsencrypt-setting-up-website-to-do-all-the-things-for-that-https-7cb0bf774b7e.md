---
title: How to setup your website for that sweet, sweet HTTPS with Docker, Nginx, and
  letsencrypt
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-19T18:48:35.000Z'
originalURL: https://freecodecamp.org/news/docker-compose-nginx-and-letsencrypt-setting-up-website-to-do-all-the-things-for-that-https-7cb0bf774b7e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*m-xEibEV8ttbhv7W.png
tags:
- name: Docker
  slug: docker
- name: nginx
  slug: nginx
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Russell Hammett Jr. (Kritner)

  I’ve used letsencrypt in the past for free certs. I have not successfully utilized
  it since moving over to docker/kestrel/nginx. That all changed today, and I had
  a hell of a time figuring out what I was doing to get ...'
---

By Russell Hammett Jr. (Kritner)

I’ve used [letsencrypt](https://letsencrypt.org/) in the past for free certs. I have not successfully utilized it since moving over to docker/kestrel/nginx. That all changed today, and I had a hell of a time figuring out what I was doing to get it working.

This whole Unix, docker, nginx, stuff is pretty new (to me), so maybe it’s just something simple I was missing the whole time. Nonetheless, I’m hoping this will help someone else, or me several months down the road if I decide to do it again.

#### Original Setup

I have a [.net core](https://www.microsoft.com/net/download) website, being hosted via [kestrel](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-2.1), running on [docker](https://www.docker.com/), with a reverse proxy via [nginx](https://www.nginx.com/). Up until now, that reverse proxying from nginx was only working over http/port 80. I don’t know a whole lot about reverse proxies. From the sound of it, it can take in requests, and forward them to a specific location on behalf of the requester. In my case, the nginx container receives http requests, and nginx forwards that request onto my kestrel hosted .net core site. Is that right? Hopefully!

As mentioned previously, the nginx was only working with http traffic. I was having a lot of trouble getting it working with https, the original configuration is as follows:

docker-compose:

```
version: '3.6'services:    kritner-website-web:    image: ${DOCKER_REGISTRY}/kritnerwebsite    expose:      - "5000"    networks:      - frontend    restart: always    container_name: kritnerwebsite_web  kritner-website-nginx:    image: nginx:latest    ports:      - "80:80"    volumes:      - ../src/nginx/nginx.conf:/etc/nginx/nginx.conf    depends_on:      - kritner-website-web    networks:      - frontend    restart: always    container_name: kritnerwebsite_nginx
```

```
networks:  frontend:
```

In the docker-compose file, I’m using two separate containers — the website, which exposes port 5000 (on the docker network, not publicly), and nginx which operates on port 80.

nginx.conf

```
worker_processes 4; events { worker_connections 1024; } http {    sendfile on;     upstream app_servers {        server kritner-website-web:5000;    }     server {        listen 80;         location / {            proxy_pass         http://app_servers;            proxy_redirect     off;            proxy_set_header   Host $host;            proxy_set_header   X-Real-IP $remote_addr;            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;            proxy_set_header   X-Forwarded-Host $server_name;        }    }}
```

In the config file, we’re setting up an upstream server with the same name that we’re calling our container service from the docker-compose file `kritner-website-web:5000`.

Note, all the above can be found at this [commit point](https://github.com/Kritner/KritnerWebsite/tree/0e86849c97bdcabf68d0df7ed7eb7e5eebdccd4f) on my website’s repository.

#### Enter HTTPS

Letsencrypt is a certificate authority that offers free certs to help secure your website. Why is HTTPS via TLS important? Well, there’s a whole lot to that, and how it works. The basic idea is the user’s traffic is encrypted on either end prior to being sent to the other end. This means if you’re on public wifi, and on https, someone that was “sniffing the wire” so to speak, would see that traffic is occurring, but not the content of said traffic. Since both ends are encrypting/decrypting said traffic with the same encryption key.

If you were on an http site, this traffic would be sent back and forth in plain text. Meaning your data is in danger of being eavesdropped on! Maybe I’ll write a bit more about encryption at some point. (*note to self*) Especially since it’s something I’m doing as my day job!

letsencrypt is a service I’ve used before. There are various implementations to try to make it as easy as possible to use. Through research for this post, I happened upon [this](https://letsencrypt.org/docs/client-options/).

Although I hadn’t found this page until now, it would have been useful prior to beginning my adventure. I wanted to use letsencrypt along with my docker container website, and nginx, with as little maintenance as possible. letsencrypt certificates are only good for 90 days.

In my research, I happened upon a docker image [linuxserver/letsencrypt](https://hub.docker.com/r/linuxserver/letsencrypt/) that promises to utilize nginx, letsencrypt certificate generation, AND auto renewal. Sounds awesome! While the documentation of the image seems mostly adequate — for someone well versed in all this process. I found it to be lacking. The whole setup process took me some time to figure out. Hence this post, to hopefully help out the next person, or again me in the future!

![Image](https://cdn-media-1.freecodecamp.org/images/uDVdXYEOt66dbf284uuJT0gybayII2EW3lTF)
_Linux Server.IO logo_

#### Struggles

The things I most struggled with when getting this linuxserver/letsencrypt image up and working were:

* How docker volumes “work” and their relationship with this container
* How to set volumes up to utilize my configuration (related to the above point) — I was initially having a lot of trouble figuring out why my settings changed on the container were being changed back on reloading of said container (because that’s what they’re supposed to do)
* How to set up the correct nginx configuration — where to put it, and what to put in it.

#### Docker volumes

Docker volumes ([doc](https://docs.docker.com/storage/volumes/)):

> Volumes are the preferred mechanism for persisting data generated by and used by Docker containers. While [bind mounts](https://docs.docker.com/storage/bind-mounts/) are dependent on the directory structure of the host machine, volumes are completely managed by Docker. Volumes have several advantages over bind mounts

letsencrypt has a lot of configuration to go along with it. It took a while for me to realize, but I needed a volume that mapped from a directory on the **docker host** to a specific directory on the letsencrypt image. I eventually accomplished this in the compose file like so:

```
volumes:      - ${DOCKER_KRITNER_NGINX}:/config       - ./nginx.conf:/config/nginx/site-confs/default
```

The first item in the array (`${DOCKER_KRITNER_NGINX}:/config`) takes a new environment variable that maps the host directory (defined in the variable) to the `/config` within the docker container itself. This means that the **docker host** (at the env var path) will contain the same config as the **docker container** at the secondary portion of the volume mapping (`/config`)

The second item (`./nginx.conf:/config/nginx/site-confs/default`) maps my local repositories nginx.conf file (the file where I set up the reverse proxy) to override the `/config/nginx/site-confs/default` file on the docker host and container.

The full list of files that I ended up needing to modify for my particular situation was:

* `/config/dns-conf/dnsimple.ini`
* `/config/nginx/site-confs/default`

The `dnsimple.ini` configuration was add my api key, and the `…/default` houses the nginx configuration.

The final `default` configuration I ended up with is:

```
upstream app_servers {        server kritnerwebsite:5000;}
```

```
## Version 2018/09/12 - Changelog: https://github.com/linuxserver/docker-letsencrypt/commits/master/root/defaults/default
```

```
# listening on port 80 disabled by default, remove the "#" signs to enable# redirect all traffic to httpsserver { listen 80; server_name kritnerwebsite; return 301 https://$host$request_uri;}
```

```
# main server blockserver { listen 443 ssl;
```

```
# enable subfolder method reverse proxy confs include /config/nginx/proxy-confs/*.subfolder.conf;
```

```
# all ssl related config moved to ssl.conf include /config/nginx/ssl.conf;  # enable for ldap auth #include /config/nginx/ldap.conf;
```

```
client_max_body_size 0;
```

```
location / {            proxy_pass         http://app_servers;            proxy_redirect     off;            proxy_set_header   Host $host;            proxy_set_header   X-Real-IP $remote_addr;            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;            proxy_set_header   X-Forwarded-Host $server_name;    }
```

```
}
```

```
# enable subdomain method reverse proxy confsinclude /config/nginx/proxy-confs/*.subdomain.conf;# enable proxy cache for authproxy_cache_path cache/ keys_zone=auth_cache:10m;
```

There are a few changes from the default that was there, which I’ll try to highlight next.

```
upstream app_servers {        server kritnerwebsite:5000;}
```

Above is pretty cool, since docker has its own internal DNS (I guess?). You can set up an upstream server by the containers name, in my case “kritnerwebsite”. (Note: I changed it from earlier in the post, which was “kritner-website-web”.)

```
# listening on port 80 disabled by default, remove the "#" signs to enable# redirect all traffic to httpsserver { listen 80; server_name kritnerwebsite; return 301 https://$host$request_uri;}
```

Uncommented out this section from the default, applied my server_name of “kritnerwebsite”

```
# main server blockserver { listen 443 ssl;
```

```
# enable subfolder method reverse proxy confs include /config/nginx/proxy-confs/*.subfolder.conf;
```

```
# all ssl related config moved to ssl.conf include /config/nginx/ssl.conf;  # enable for ldap auth #include /config/nginx/ldap.conf;
```

```
client_max_body_size 0;
```

```
location / {            proxy_pass         http://app_servers;            proxy_redirect     off;            proxy_set_header   Host $host;            proxy_set_header   X-Real-IP $remote_addr;            proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;            proxy_set_header   X-Forwarded-Host $server_name;    }
```

```
}
```

In the above, it’s mostly from the “default” save for “location” and everything within that object. Here, we’re setting up the reverse proxy to forward requests to “/” (anything) to our `http://app_servers` (kritnerwebsite as per our upstream).

#### docker-compose.yml

Our docker compose file didn’t change a *whole* lot from the initial. There were a few notable changes, which I’ll also get into describing:

```
version: '3.6'services:    nginx:    image: linuxserver/letsencrypt    ports:      - "80:80"      - "443:443"    volumes:      - ${DOCKER_KRITNER_NGINX}:/config       - ./nginx.conf:/config/nginx/site-confs/default    depends_on:      - kritnerwebsite    networks:      - frontend    container_name: nginx    environment:      - PUID=1001 # get on dockerhost through command "id <user>""      - PGID=1001      - EMAIL=kritner@gmail.com      - URL=kritner.com      - SUBDOMAINS=www      - TZ=America/NewYork      - VALIDATION=dns # using dns validation      - DNSPLUGIN=dnsimple # via dnsimple, note there is additional configuration require separate from this file      # - STAGING=true # this should be uncommented when testing for initial success, to avoid some rate limiting
```

```
kritnerwebsite:    image: ${DOCKER_REGISTRY}/kritnerwebsite    networks:      - frontend    expose:      - "5000"    restart: always    container_name: kritnerwebsite  networks:  frontend:
```

for the new parts:

```
nginx:    image: linuxserver/letsencrypt
```

Using a different image — linuxserver/letsencrypt instead of nginx. This image has nginx included, but also certbot, along with a cronjob to run certbot at application start.

```
ports:      - "80:80"      - "443:443"
```

Now we’re using both http and https ports (though note, we’re redirecting http calls to https via the nginx config).

```
volumes:      - ${DOCKER_KRITNER_NGINX}:/config       - ./nginx.conf:/config/nginx/site-confs/default
```

Already discussed earlier in the post, we’re using these volumes to properly set up the nginx configuration, with our dnsimple api key, as well as our reverse proxying to the kritnerwebsite.

```
environment:      - PUID=1001 # get on dockerhost through command "id <user>"      - PGID=1001      - EMAIL=kritner@gmail.com      - URL=kritner.com      - SUBDOMAINS=www      - TZ=America/NewYork      - VALIDATION=dns # using dns validation      - DNSPLUGIN=dnsimple # via dnsimple, note there is additional configuration require separate from this file      # - STAGING=true # this should be uncommented when testing for initial success, to avoid some rate limiting
```

Environment variables needed as per the letsencrypt documentation can be found [here](https://hub.docker.com/r/linuxserver/letsencrypt/).

* PUID/PGID — get on dockerhost through command “id <user>”
* Email — well, your email (used for cert expiration emails apparently)
* URL — the main domain URL
* subdomains — any subdomains to the URL to be certified
* TZ — timezone
* Validation — the type of validation to do — I’m using DNSimple, so i needed DNS in this field. Other options are html, tls-sni
* dnsplugin — dnsimple — other options are `cloudflare`, `cloudxns`, `digitalocean`, `dnsmadeeasy`, `google`, `luadns`, `nsone`, `rfc2136` and `route53` as per the letsencrypt documentation
* Staging=true — I used this for testing out all my various attempts prior to getting it working. letsencrypt has rate limiting when not running in staging mode (or at least in staging it’s harder to run up against).

All the above changes, experimenting, failing, and then finally succeeding can be found in [this pull request](https://github.com/Kritner/KritnerWebsite/pull/24/commits).

The final result?

![Image](https://cdn-media-1.freecodecamp.org/images/8p9oqF7gDeWHXY9oqutUsEB5rmbmH8zh9D8s)
_Awww yeah_

and from [https://www.ssllabs.com/](https://www.ssllabs.com/) —

![Image](https://cdn-media-1.freecodecamp.org/images/YcQFIv8RixHyyhSlurfdIZVZmbttLUOQi5V0)

Not an “A+”, but really not bad for using one pre-built docker image for my HTTPs needs!

Related:

* [Going from an “A” to an “A+” on ssllabs.com](https://medium.com/@kritner/going-from-an-a-to-an-a-on-ssllabs-com-570d2e245100)

