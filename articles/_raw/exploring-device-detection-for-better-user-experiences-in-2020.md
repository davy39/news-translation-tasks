---
title: How to Detect Your User's Device So You can Improve Their User Experience
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-15T06:41:54.000Z'
originalURL: https://freecodecamp.org/news/exploring-device-detection-for-better-user-experiences-in-2020
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dde740569d1a4ca3a1c.jpg
tags:
- name: user experience
  slug: user-experience
seo_title: null
seo_desc: 'By Leonardo Faria

  A few months ago I watched a great talk from the Chrome Dev Summit about performance
  in slow devices.

  https://youtu.be/puUPpVrIRkc

  It blew my mind all the work done by Facebook in identifying devices to create a
  better user experien...'
---

By Leonardo Faria

A few months ago I watched a great talk from the Chrome Dev Summit about performance in slow devices.

%[https://youtu.be/puUPpVrIRkc]

<p>It blew my mind all the work done by Facebook in identifying devices to create a better user experience. Fast-forward to now, and I've decided to study a bit more about the topic and see what I can do at <a href="https://www.thinkific.com">Thinkific</a> (the company I work for).</p><h2 id="user-agents">User agents</h2><p>User agents are well-known by developers. We use them to detect bots, redirect users to a specific version of our website or append CSS classes on our page so we can create different experiences.</p><p>At Thinkific we already use the&nbsp;<a href="https://github.com/fnando/browser">browser Ruby gem</a>&nbsp;to parse the user-agent and get relevant info (bot detection for instance). So, I decided to persist the main info in a visitor_device table – here is the schema:</p><div><div id="highlighter_373452" class="syntaxhighlighter nogutter code plain"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="plain plain">tenant_id: the course creator school the visitor is checking</code></div><div class="line number2 index1 alt1"><code class="plain plain">raw: the raw ua</code></div><div class="line number3 index2 alt2"><code class="plain plain">type: desktop / mobile / tablet / bot / other</code></div><div class="line number4 index3 alt1"><code class="plain plain">browser_name</code></div><div class="line number5 index4 alt2"><code class="plain plain">browser_version</code></div><div class="line number6 index5 alt1"><code class="plain plain">platform_name</code></div><div class="line number7 index6 alt2"><code class="plain plain">platform_version</code></div><div class="line number8 index7 alt1"><code class="plain plain">hardware: hstore containing memory, processor, device_model, device_name</code></div><div class="line number9 index8 alt2"><code class="plain plain">connection: hstore containing downlink_max, connection_type</code></div></div></td></tr></tbody></table></div></div><p>You probably noticed that a few things there are not available in the UA string. Time for new JavaScript APIs:</p><h2 id="getting-hardware-info-using-javascript">Getting hardware info using JavaScript</h2><p>As covered in the Chrome Dev Summit video, we can use JS to get this info.</p><h3 id="memory">Memory</h3><p><code>navigator.deviceMemory</code>&nbsp;will return a floating-point number. There are things to consider here:</p><ul><li>It only works over HTTPS</li><li>Support is quite limited (Chrome only basically)</li></ul><p>More about it:</p><ul><li><a href="https://github.com/w3c/device-memory">Spec from W3C</a></li><li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigator/deviceMemory">MDN Docs</a></li><li><a href="https://caniuse.com/#feat=mdn-api_navigator_devicememory">Can I use deviceMemory</a></li></ul><h3 id="processors">Processors</h3><p><code>navigator.hardwareConcurrency</code>&nbsp;will return the number of logical cores of the user’s CPU. Support for this is&nbsp;<a href="https://caniuse.com/#feat=hardwareconcurrency">decent</a>.</p><h2 id="detecting-connection-info-using-javascript">Detecting connection info using JavaScript</h2><p><code>navigator.connection</code>&nbsp;is a new API containing information about the system’s connection, such as the current bandwidth of the user’s device or whether the connection is metered. The support is quite limited (Chrome only basically) but things are promising.</p><p>More about it:</p><ul><li><a href="https://googlechrome.github.io/samples/network-information/">Chrome example</a></li><li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigator/connection">MDN Docs</a></li><li><a href="https://caniuse.com/#feat=netinfo">Can I use Network Information API</a></li></ul><h2 id="detecting-the-device-model">Detecting the device model</h2><p>The user agent&nbsp;<em>may</em>&nbsp;return some information about the model name.&nbsp;<a href="https://userstack.com/">userstack</a>&nbsp;is a service that gives you information based on the user agent. It works well and it is easy to integrate, however, depending on your needs, they can’t help.</p><p>Take for instance iDevices. Their user agent is basically the same so you can’t differentiate an iPad Pro from an old iPad that runs the last iOS. For these cases, you may need a better detection based on resolution, pixel density and other hardware information exposed in the browser. I did some quick research on this and found 3 products so far:&nbsp;<a href="https://web.wurfl.io/#wurfl-js">WURFL.io</a>,&nbsp;<a href="https://deviceatlas.com/products/web">DeviceAtlas</a>&nbsp;and&nbsp;<a href="https://51degrees.com/">51Degrees</a>. I haven’t had time to try their products yet, but I am looking forward to doing it (and posting about it)</p><h2 id="faq">FAQ</h2><p><em>Question: Why not use Google Analytics / Mixpanel / Kibana / New Relic / your tool here?</em></p><p>We could get browser info inside other tools. But as a SaaS product we don’t use our own Google Analytics property (customers add their own). Also, adblockers may block these third-party tools. Last but not least, by having this info in our side we can adapt better.</p><p><em>Question: Do you have a list of low-end/high-end devices?</em></p><p>No. Maybe this can be built combining the number of processors and memory but I didn’t invest much time on this. In this project, my colleague created a Rails helper that would determine if the user would use the lite or default version of a website based on hardware. On this topic, it is important to mention that Facebook has a library for Android called <a href="https://github.com/facebook/device-year-class/">Device Year Class</a>.</p>

_Also posted on [my blog](http://bit.ly/2FWop4N). If you like this content, follow me on [Twitter](https://twitter.com/leozera) and [GitHub](https://github.com/leonardofaria)._

By the way - Thinkific is [hiring](https://bit.ly/thnk-senior-front-end-eng) [for](https://bit.ly/thnk-senior-full-stack-eng) [several positions](https://www.thinkific.com/careers/) if you are interested.

