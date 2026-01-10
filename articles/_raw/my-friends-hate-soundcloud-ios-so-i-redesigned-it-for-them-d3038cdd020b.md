---
title: My friends hate SoundCloud iOS so I redesigned it for them
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-22T02:35:54.000Z'
originalURL: https://freecodecamp.org/news/my-friends-hate-soundcloud-ios-so-i-redesigned-it-for-them-d3038cdd020b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pGIr42haQHsmxo9BXZl3JA.png
tags:
- name: Design
  slug: design
- name: music
  slug: music
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By kelleytmnguyen

  What started out as a casual conversation with my friends turned into a serious
  exploration. This was partially because I love SoundCloud, and partially because
  I needed to challenge myself in order to move forward in my career.

  I s...'
---

By kelleytmnguyen

What started out as a casual conversation with my friends turned into a serious exploration. This was partially because I love SoundCloud, and partially because I needed to challenge myself in order to move forward in my career.

I started using SoundCloud obsessively back in 2013, and have since started using other streaming applications as well. SoundCloud is amazing. Whenever I go through its community, I can look forward to discovering so much new talent.

So I set out to redesign SoundCloud’s iOS app from the ground up, the way me and my friends would like it to be.

### Part I — Starting from scratch

#### Iteration I

For the past six months, I couldn’t fight a feeling that SoundCloud had changed ever since they released their mobile platform. And not in a good way. When I would ask my friends how they felt about it, they’d get all worked up. We’d debate over what we still loved about it and what was going wrong; I’d get into deep conversations with my Lyft drivers; I’d discretely slip questions about SoundCloud into random discussions.

Lo and behold, _I found that most of us avoided using it._

So, I became more and more curious… ?

![Image](https://cdn-media-1.freecodecamp.org/images/9BQ24j7g766fg6HShFYdr-zgjqdwiLy3uemj)
_Fry from Futrama_

What made other mobile streaming applications stronger or weaker than SoundCloud? What were the details of our unhappiness? What needed to change? To gain insight, I expanded my streaming experience and started using Spotify and Apple Music, comparing and contrasting their strengths, weaknesses, and patterns. What elements and terms were universal across these streaming platforms?

![Image](https://cdn-media-1.freecodecamp.org/images/n9P-Tv9rdUfHrAjOaAUwtsx2-oYUyt9dgmzZ)

![Image](https://cdn-media-1.freecodecamp.org/images/f7IS7IxlKgsLZEiizsphiaVUHx3Nbf5whKBX)

![Image](https://cdn-media-1.freecodecamp.org/images/3WkO4I0VMNKo66NLaHE7XKUSiuN2yJLEMoa2)

After mentally compiling a list of suggestions and improvements for SoundCloud (from informal conversations etc.), I realized the inevitable.

> _If I wanted to redesign SoundCloud, I had to start from scratch_.

I had to start at ground zero.

#### Situation

In 2016, global recorded music market grew by 5.9% due to streaming ([IFPI Facts and Stats 2016](http://www.ifpi.org/facts-and-stats.php)). 59% of digital revenues that same year came from streaming alone. As one of the most popular streaming platforms, SoundCloud strongly emphasizes their community, recording 847 million electronic connections made in 2015. It boasts one of the largest grassroots digital community of electronic music estimated at over 10 million.

![Image](https://cdn-media-1.freecodecamp.org/images/ky8PKlQIeHaKsmvDL4C4q-sPilwzMBUq-Gk4)
_[https://soundcloud.com/for/electronic](https://soundcloud.com/for/electronic" rel="noopener" target="_blank" title=")_

#### **Hypotheses**

SoundCloud became a music streaming competitor in 2016 after debuting their subscription service SoundCloud Go. The press expressed less than satisfied reviews upon its release; SoundCloud then responded by releasing a new tier called SoundCloud Go+ in 2017. As the [platform struggles to win users over Spotify Premium](https://about.crunchbase.com/news/streaming-wars-continue-soundcloud-balance/?utm_source=cb_daily&utm_medium=email&utm_campaign=20170518&utm_content=intro&utm_term=content&send_email=kelleytmnguyen@gmail.com), I began forming hypotheses.

> 1. Music streaming and discovery is a very social activity  
>  2. Making playlists is crucial to one’s listening experience  
>  3. Discovering new music must be convenient

#### Market Research I

Globally, the highest shares of electronic music are held in Europe and Asia, and the highest streams of electronic music are in America, Great Britain, Denmark and Mexico. ([IMS Summit Business Report 2017](http://www.internationalmusicsummit.com/wp-content/uploads/2017/05/IMS-Business-Report-2017-vFinal2.pdf))

![Image](https://cdn-media-1.freecodecamp.org/images/vRNW1hs96uWqCDp2Waq8KpfhDNY4pAsCyPJw)
_[Who is the electronic music listener?](http://www.nielsen.com/us/en/insights/news/2014/who-is-the-electronic-music-listener.html" rel="noopener" target="_blank" title=") (Nielsen)_

> “Millennials are 40% more likely to attend a club event in the USA, and total 2 billion globally” — International Music Summit Business Report 2017

#### **Research I**

_Stakeholders_

I divided stakeholders into two categories: hobbyists and professionals. To address a need that everyone shared, I looked at their overarching role.

> Each stakeholder was ultimately a listener.

In effect, I focused my questions around the habits of listeners and streamers. For this round, I collected responses from 23 participants whom were between the ages of 18 and 28. 82% were male and 80% were in college.

![Image](https://cdn-media-1.freecodecamp.org/images/blasAotnuWo8cXB2ngt8vbmVooOYMghId1Ia)
_Stakeholders_

I discovered that my participants were more likely to repeatedly see tracks reposted to their feed from the same group of artists. They found themselves in a feedback loop, where the same tracks would circulate from the same users. Users were less likely to find new music and were influenced by features such as ‘like’ and ‘repost’ count. A few of them said that they would scroll through 3 or 5 tracks on their feed, lose interest, and move on to something else.

**More questions started to form.** How important is a user’s connection to the online music community? How often do listeners listen to their friend’s music? How are they influenced by reposted tracks and like count?

_Interviews_

I had 5 interviews, each of which lasted about 30 minutes. I asked over 20 questions, aiming to uncover what each individual believed the strengths and weaknesses of SoundCloud iOS were. My interviews exposed a lack of trust for SoundCloud’s recommendations as a discovery platform. SoundCloud was not thought to be as polished as Spotify and Apple Music. **Rather, it was viewed as a portfolio for developing artists instead of a professional discography.** All of my results are compiled [here](https://docs.google.com/document/d/1Knf2hzWY4bebUQhTu35HNFuVnH2RcPb9meRNNi_m4uM/edit#heading=h.f0z79jq5lysy).

![Image](https://cdn-media-1.freecodecamp.org/images/NYz7nLd-sXsAAOwYinjstlO3lAwsGVmN0Zhu)

From my gathered data, I could paint a better picture. I illustrated the type of behaviors I would be designing for with [personas and scenarios](https://files.persona.co/44294/sc-pov-personas.pdf). The first scenario is a story about a friend whose listening experience spurred her to share a track with a friend. The second tells of a young, working adult who wishes to have a new listening experience while driving to work in traffic.

![Image](https://cdn-media-1.freecodecamp.org/images/jvIjVk-VUthDKGpJTe6KY5qV0TLPIadO-uv1)
_Primary Persona_

![Image](https://cdn-media-1.freecodecamp.org/images/ojrCJXO9ACc18f8n-3wkARphJgzOue6xg-5w)

![Image](https://cdn-media-1.freecodecamp.org/images/-9OSPqjvcHnlQqV128rJerN-ay6g0-UotAt5)

**100% of survey and interview participants listened to variations of electronic music.** This included a wide breadth of sub-genres including trap, electronica, and pop. 60% of interviewees stated that they listened to podcasts, sets, or mixes, all of which could last between 30 minutes to 3 hours. Their feedback supported my understanding of SoundCloud as a platform for electronic music, whether in the form of rap production or sub-genres.

#### To revisit my hypotheses:

> 1. My interviews ultimately showed that music streaming and discovery are not heavily social activities, but personal explorations. Individual taste is extremely unique.

> 2. Not everyone makes playlists because it takes much more effort than the average user can afford.

> 3. The solution? Give listeners the music they never knew they wanted. Or in other words, humans are lazy, so we gotta do all the work.

Most importantly, SoundCloud’s electronic music community and repository must be at the very surface. This would mean **curating content** (recorded sets, influencers, live mixes), and **organizing libraries** of music in order to **engage the habits** of the electronic music community. To address the needs of my subjects, I made the following proposals:

#### Proposals

> 1. A new page dedicated to Events and Mixes

> 2. Organize and categorize collection of saved music

> 3. A new page dedicated to Curators

> 4. A separate module for popular reposted tracks

> 5. Focus solely on community of electronic and dance music

### Prototyping

#### User Flows

After I studied common music streaming applications and digested SoundCloud’s mobile pathways, I roughly visualized its most important features. These features guided which [user flows and pathways](https://files.persona.co/44294/sc-infoarch-sitemaps.pdf) I believed users would most likely follow when using SoundCloud.

#### Low Fidelity

Taking the information organized through sitemaps and user flows, I created low-fidelity wireframes for Profile or Home, Library, and Discovery using paper prototypes. I moved to [digital wireframes](https://files.persona.co/44294/_Flows-ilovepdf-compressed.pdf) afterwards and drew basic [wireframe maps](https://files.persona.co/44294/sc_Wireframe_Flows.pdf) to group screens together.

![Image](https://cdn-media-1.freecodecamp.org/images/7cqLGhC8DxKxJiJoeTYt7HKkMAHcBjeBENqA)

![Image](https://cdn-media-1.freecodecamp.org/images/-BH85pzoax9EpfIZs0atxK6DJehO0mcxypPS)

#### Mid Fidelity

From low-fidelity, I took note of the significance and purpose of each element and page. Again, the following are organized by the main branches of the application: Profile or Home, Discover, and Library.

![Image](https://cdn-media-1.freecodecamp.org/images/CkuW3ywdUc-0ahlBrU2A5RsQFpAP6ABM2GGT)

![Image](https://cdn-media-1.freecodecamp.org/images/JakjIw0q1to54VNpYsR-TjoQvAunxQ6GdJIU)

![Image](https://cdn-media-1.freecodecamp.org/images/dDdJlqNz23U2smXf95FoP8-Fn0PcJQ2IfPWi)

**Events & Mixes**

![Image](https://cdn-media-1.freecodecamp.org/images/tUnDd7ZG-bMwEsMMqbyMKz5sKOuUP5C8gYyN)

_Discover > Mixe_s >

1. Featured — collaborators, suggested artists etc.

2. Events — festivals, performances

3. Location — major cities and scenes

4. Podcasts — residents, daily mixes

**Curators**

_Discover > Mixe_s >

1. Record labels — professional distributors

2. Self-made — YouTube channels

3. Music collectives — groups, collaborators

Press — magazines and PR premiering music

![Image](https://cdn-media-1.freecodecamp.org/images/5ejrGDxnv5h54tacFw-PutIOWyCA8CydOTa9)

![Image](https://cdn-media-1.freecodecamp.org/images/9Fk7N2h1gu2TAq7Pua0uR3K7orP-HcgQU6GM)

![Image](https://cdn-media-1.freecodecamp.org/images/iy7eMfhZ6vzFEv7QuyEdyfd4lQFxdAxO97Wb)

#### High Fidelity

[Online Prototype](https://xd.adobe.com/view/145e74af-77aa-42c7-8951-5d683f98d40a/)

Let me know your thoughts about how the infrastructure works for you, what could be better about the interface, and your overall experience.

**Part I** was my first run on Adobe XD, and I’m impressed by how easy it was to use the Prototyping feature. Part I also covers initial research findings and the first interactive mockup. For **Part II**, I’ll be focusing on visual design and microinteractions using Sketch and Principle, smoothing out the edges of the first model for a better second iteration.

### Part II — Taking a step back

#### Iteration II

**Thanks for reading so far!** The final bits of this project have made me more excited about interaction design as a whole. I found these gifs to show you guys how I feel about the progress ?

![Image](https://cdn-media-1.freecodecamp.org/images/561gyDyTr0gLeUdjk2pkxQW7d2zoYVFXpE8S)

![Image](https://cdn-media-1.freecodecamp.org/images/hnm75Ubkf4hcyQId3H9f4Oq4uFwuS10sOIY7)
_L: Sailor Moon, R: Finn from Adventure Time_

Before moving onto the last half of this project, I looked at how SoundCloud has changed within the past couple of months. I reviewed the data I had collected a few months earlier and sifted through SoundCloud’s current [activity](https://soundcloud.com/charts/top). Artists like _Lil Uzi Vert_, _Post Malone_, and _Travis Scott_ have been at the top of SoundCloud’s charts, making hip-hop as popular as (if not more than) electronic. After basing this project on subjects who mostly listened to electronic music, I thought I had to pivot in a totally new direction.

> I took a step back.

If SoundCloud’s base had shifted, I knew I needed more evidence. I had focused on a small sample size in my own network and needed to expand. Why not gather more data about music streaming?

#### Market Research II

Compiled through a series of articles, press releases, and research from [NYTimes](https://www.nytimes.com/2015/02/26/arts/music/flume-rises-in-the-edm-world.html), [Forbes](https://www.forbes.com/sites/bobbyowsinski/2016/06/16/twitter-invests-soundcloud-but-why/#e1f34c72051e), [WMagazine](https://www.wmagazine.com/story/soundcloud-rappers-lil-uzi-vert-lil-yachty), and more, I realized the trend for hip-hop through SoundCloud emerged in the last couple of years. The top 3 artists on SoundCloud in 2015 were **Drake**, **Major Lazer**, and **G-Eazy** ([Forbes 2015](https://www.forbes.com/sites/hughmcintyre/2015/08/23/soundclouds-ten-most-played-artists-this-year-tell-a-lot-about-its-users/2/#7b1192be3990)). In 2016, the top album was _Coloring Book_ by **Chance the Rapper**, the most favorited track _Panda_ by **Desiigner**, and most followed: **Lil Uzi Vert**.

![Image](https://cdn-media-1.freecodecamp.org/images/nRvZ-zluuzHuDwjG1Sq0vfdLu6xVeo1iSmHE)
_[SoundCloud 2016 Overview](https://blog.soundcloud.com/2017/01/19/throwbackto2016/" rel="noopener" target="_blank" title=")_

#### Research II

I made another survey that was more concise and focused on quantitative data. Consisting of four, multiple choice questions, I gathered responses from 167 participants.

![Image](https://cdn-media-1.freecodecamp.org/images/OmAGdb8RZCYXzzbU3mpNM2lVlGpR4i14dgZQ)
_Q1: What is your age?_

![Image](https://cdn-media-1.freecodecamp.org/images/tHys7jUHi4BBnA76ViKd3SeIiE2Lx7XBmspW)
_Q2: What genre(s) do you listen to the most?_

![Image](https://cdn-media-1.freecodecamp.org/images/cPRMUHsYigkBxzVLXOR7uPaOIiMaZvef8J38)
_Q3: What streaming application(s) do you use on your phone?_

![Image](https://cdn-media-1.freecodecamp.org/images/xsVvvSS9Iugb7AcCUnIo9lzQGwjMv9dKjy7K)
_Q4: What do you use your streaming application(s) for?_

The following are the results: **Electronic music and hip-hop** tied for most-listened-to genre. Most music streamers ranged between the ages of 16 and 27, averaging at about **21 years of age**. **Spotify leads** against SoundCloud as the most preferred, mobile, streaming platform. **Streaming** was considered the most important activity, then discovery, then making playlists.

#### To revisit my proposals:

> 1. Organize and categorize collection of saved music

> 2. A separate module for popular reposted tracks

> 3. Focus on community of electronic, dance, and hip-hop

> 4. Structure pages of Discover to mold to genres and community

Most of the round 2 results mirrored that of the data I had collected a few months ago, but I did learn something new:

> **One of SoundCloud’s strongest points as a platform is its versatility and ability to evolve with its audience.**

In order to morph with its community, the design must be unbiased, favor all genres of music, and build on characteristics of SoundCloud’s current brand: stark and neutral.

### Icons

I tried a hand at making icons to get a feel for perfecting pixels. Granted this was my first time and there is a lot of room for improvement, I could see how my attention to detail could get carried away.

![Image](https://cdn-media-1.freecodecamp.org/images/5-oAzMkMCpDE0DGNDTPxQfC5UIocKygeWUX5)

![Image](https://cdn-media-1.freecodecamp.org/images/EisEtfNUaqTym322sERowBgOA6A3ZQTCOu0v)

### Visual Design and Microinteractions

#### **Home**

For SoundCloud iOS, Home’s purpose (and only purpose) is to show the activity of the people you follow. All posts are dumped into the feed in chronological order. The most salient elements of the feed are each post’s artwork and like and repost count.

![Image](https://cdn-media-1.freecodecamp.org/images/yyy1QXgnv9ESjQKVe3JEDhRMFqGJz2TBdgud)
_SoundCloud vs Iteration 2: Home_

**Popular in Your Feed** allows listeners to see the activity of users they follow. The first track in this module shows that 35 people Mary follows liked a post from Paramore. The module compiles the activity into one notification and accounts for duplicates. If the people Mary follows reflect facets of her own music taste, Mary might like the track too.

![Image](https://cdn-media-1.freecodecamp.org/images/aA-hilb9MiElkzGppTE5MPUPtIgTjdm0KfiL)

![Image](https://cdn-media-1.freecodecamp.org/images/UMxPI--66qWeuaLf5kaqW6pm2nd5yV0EG1cn)
_Iteration 2: Popular in Your Feed_

Let’s say a post has fewer than 10 likes and a non-attractive album cover. Would you listen to it? _If we’re being honest, you’re less likely to play a post that appears less professional and numbers always play a part in influencing your expectations._

I took away the like and repost counts to lessen judgment and bias. The icons on the right hand side categorize posts into types: stations, mixes, playlist, albums, or tracks. To focus on listening instead of appearance, **Your Feed** emphasizes title, artist, and type.

![Image](https://cdn-media-1.freecodecamp.org/images/UQlhqJ8o9TnCQbFiOrq8OHLB3xSOtWNwG0UP)
_Iteration 2: Your Feed_

#### Search

![Image](https://cdn-media-1.freecodecamp.org/images/LXv2RnP8zCMYBHfLsgNdN-4sAKiR4vqg0EYh)
_Iteration 1: search and album description_

On SoundCloud iOS, pressing on the Search tab takes you to their version of Discover. Pressing on the search bar at the top of the page changes it to Search. **I separated Search and Discover into 2 separate tabs for navigation.** If the listener would like to only search, they’d press on the Search button. Here’s an example of my first iteration.

**Search** contains Recent Searches and the results are divided into previews of each classification i.e. tracks, albums, people.

I took away the filter bar that horizontally scrolled, using only a single vertical scroll to eliminate the time it would take for one to move up, down, and to the sides. The redesign of **Search** optimizes results by finding the most relevant item as the Top Result and giving snippets of what type of results there are.

![Image](https://cdn-media-1.freecodecamp.org/images/BAJ8aBO5ihE7c61sXTAjxjDXLmX5-D-T-3iH)
_SoundCloud 5.7.1 vs Iteration 2: Search_

To apply genres to tracks, SoundCloud allows users to label their uploads using hashtags. I thought that the hashtags could use a little more life to bring attention to them.

![Image](https://cdn-media-1.freecodecamp.org/images/6gmfL65V4xNsoUyztfrtTmkb6ZazJCdOdugG)
_Iteration 2: album description and hashtags_

#### Discover

The Discover page of the first iteration focused more on breaking down SoundCloud by types such as tracks, playlists, and albums. What I noticed was that navigating through these items became repetitive (tracks, playlists, and albums would all have modules for hot, new, and suggested). There wasn’t a theme behind each menu item.

![Image](https://cdn-media-1.freecodecamp.org/images/yrhzoSRFsUTAm4WdZ-5LzzpnOOXwUyn1ZNG9)
_Iteration 1 vs Iteration 2: Discover landing_

To make the menu items less arbitrary, I revised the sitemap of **Discover** to fit SoundCloud’s age demographic of avid festival attendants. I also tried to maintain a level of flexibility to the modules featured on each page. Due to the different focuses of the project, I left out Charts when brainstorming features of Discover and emphasized **Your Cloud, Around the World, Extended Play** and **Curated**.

![Image](https://cdn-media-1.freecodecamp.org/images/14Pkfn94iCIW8JcvAsBU3pT3HCc6YFJy6OgS)
_Revised Discover sitemap_

![Image](https://cdn-media-1.freecodecamp.org/images/aaODZWvC4TK8Tk1-FgL6ccOY5eksp6nCMpOy)
_SoundCloud vs Iteration 2: Discover landing_

_Discover > Featur_ed  
SoundCloud’s newest addition to Discover [is The Upl](https://techcrunch.com/2017/05/03/soundclouds-the-upload-uses-machine-learning-to-help-you-find-new-tracks/)oad. As a preview for hot artists or playlists curated by SoundCloud, I created **a Featu**red window that let’s users browse through fresh, new music and talent.

![Image](https://cdn-media-1.freecodecamp.org/images/JcXxfQzrg16xtJBxHX6q-0eQ-lyJvBVIfBAF)
_Iteration 2: featured scroll for Discover_

_Discover > Your Cl_oud  
Your Following and Followers make **up Your Cl**oud, which is where your taste in music resides. Your Cloud is made up of your immediate peers as well as suggested content that you might like. With all this information swirling around the (Sou_nd)Cl_oud (ha get it), this feature captures the relevant stuff to strengthen and expand upon your listening experience.

![Image](https://cdn-media-1.freecodecamp.org/images/KeXd3jPGNAND1SZNhn-E5XrhZZnJ1C5pqjQS)
_Left to Right: Your Cloud, Around the World, Hot &amp; New, Extended Play, and Curated_

_Discover > Around the Wo_rld  
As a global platform for independent artists in so many different parts of the world, SoundCloud has become a voice for major cities and scene**s. Around the Wo**rld covers large-scale events, live sets, and movements. This page is meant to bring global activity to the surface of SoundCloud.

![Image](https://cdn-media-1.freecodecamp.org/images/RIsaqRK917HcHXs0t5IA7gWqE3FtjbYCqdRI)
_Artwork for ‘Live Events’ and ‘Cities_

![Image](https://cdn-media-1.freecodecamp.org/images/8TjLy0tFqOqjgU4pmLGAClwIJhL8rQ8SceqA)

_Discover > Hot &_ New  
This already exists on SoundCloud Desktop (but not on mobile) under Charts. Hot & New identifies viral and notable releases from up and coming artists, which is perfect for hot hip-hop artists and rappers.

_Discover > Extended P_lay  
Electronic music is known for sets and longer performanc**es. Extended Pl**ay compiles uploads that are classified as mixes or stations so that users can listen to music for hours of listening.

_Discover > Cura_ted  
Since humans are lazy by natur**e, Cura**ted is SoundCloud’s way of giving back to the listener with hand-picked playlists. These playlists can range from sub-genres to movements in the music scene.

![Image](https://cdn-media-1.freecodecamp.org/images/Zoei7OuoPsOw82V7UyYE6dPxyz4lScaGhCFP)
_Artwork for ‘SoundCloud Playlists’ and ‘Upcoming Events’_

#### Now Playing

I kept SoundCloud’s navigation tab and waveform for Now Playing, but made controls like pause, next, and repeat more obvious for the user. I focused less on the artwork to bring out the feeling of a media player. I also placed the option to repost tracks within the **Now Playing** screen to encourage listeners to play tracks before they repost to their profile.

![Image](https://cdn-media-1.freecodecamp.org/images/xCx4LxpwCy6eFRAraFG8xIrhSfORfa3Ti4HA)
_Iteration 2: track description and more_

#### Library

If SoundCloud was catered more to vinyl collectors and spinners, I could see how Collection would be a great name for the library of music. But since SoundCloud covers such a vast group of listeners, I wanted to use **Library** because it’s a more common title.

![Image](https://cdn-media-1.freecodecamp.org/images/klmAmcra8oyZGjAsScdSlTQxb3y3fSzTL1f1)
_SoundCloud vs Iteration 2: Library_

I put in a feature that could filter tracks not just by when they were liked, but by artist, genre, or title. Here’s an example of how I thought it would look like.

![Image](https://cdn-media-1.freecodecamp.org/images/WLLRMJJYRffOnKWuyoXZUFKch12OSsgflLis)
_Iteration 2: filter library by artist_

On SoundCloud, liking something will bump the like count and add it to the Library, but there is no feedback to show that ‘added to Library’ has been performed. Similar to how Apple Music or Spotify notifies the user when a track is added to the library, I illustrated the action for SoundCloud.

![Image](https://cdn-media-1.freecodecamp.org/images/BH66xhRTOEwLtQXfRWKyNQhluUpHhGWqHyuG)
_Iteration 2: adding to and removing from library_

#### Profile

Last but not least, the profile! Some of the suggestions that my interviewees asked for was to show and access the description, links, and followers/following count. I mirrored the way posts are listed on Discover on this artist’s profile.

![Image](https://cdn-media-1.freecodecamp.org/images/etwy0QmonIeN30zsSvjFoqGi-XeStaJc39Uu)
_Iteration 2: artist profile and more options_

Anything description related comes from the top down. For more options like following, reposting or accessing an artist’s tracks, the menu comes from the bottom up.

![Image](https://cdn-media-1.freecodecamp.org/images/VHH-bvKEeCIBTMdVG-h6JTrVUpV8hOplOApX)
_Iteration 2: artist description_

### Reflecting on what was done

What started out as casual conversation with my friends turned into a deep investigation into our habits as humans and needs as listeners. For the past 4 months, I explored each facet of user experience design and found that my fascination with human-computer interaction stemmed from my compassion for people.

I took on this project as a challenge to myself, to see what I could really do. No second-guesses, no take-backs. I confronted judgments, expectations, and my biggest barrier: myself. Throughout this endeavor, I exercised my strengths, and built upon my weaknesses. Some powerful things I learned was knowing how to handle change, how crucial iteration is, and being thorough. Most importantly, _there is a lot more to learn_ in design and research.

So, where to? I can’t tell you that, seeing as I don’t have a solid answer (some of us don’t and that’s perfectly ok). But I can tell you this: I’m headed for a lifetime of learning; becoming a product designer; and shooting for the moon and beyond!

Feel free to visit me at my [website](http://www.kelley-nguyen.me) if you’d like to learn more.  
Thanks for watching!! ?

