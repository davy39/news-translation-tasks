---
title: How I Built a Faster and More Reliable APOD API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-12T21:05:00.000Z'
originalURL: https://freecodecamp.org/news/building-a-faster-and-more-reliable-apod-api
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/PointReyesMilkyWayDanZafra.jpeg
tags:
- name: api
  slug: api
- name: optimization
  slug: optimization
seo_title: null
seo_desc: 'By Ella Nan

  Astronomy Picture of the Day (APOD) is like the universe’s Instagram account. It’s
  a website where a new awe-inspiring image of the universe has been posted every
  day since 1995.

  As I was building a project using APOD’s official API, I fo...'
---

By Ella Nan

[Astronomy Picture of the Day](https://apod.nasa.gov/apod/) (APOD) is like the universe’s Instagram account. It’s a website where a new awe-inspiring image of the universe has been posted every day since 1995.

As I was building a project using APOD’s official API, I found that requests would periodically time out, or take a surprisingly long time to return. 

Curious and a bit confused (the data being returned was simple, shouldn’t require much computation, and should be easy to cache), I decided to poke around the API’s repo and see if I could find the cause, and perhaps even fix it.

## Website as a Database

I was fascinated to find that there was no database. The API was parsing data out of the APOD website’s HTML using BeautifulSoup, live per request. 

Then I remembered, this website was created in 1995. MySQL would have only been released mere weeks before the first APOD photo on June 16th.

![ap950616, the first APOD](https://www.freecodecamp.org/news/content/images/2022/03/1st-apod.gif)
_ap950616, the first APOD_

This wasn't great for performance though, as each day’s data that the API needed to return needed an additional network request to be fetched.

It also looked like requests for date ranges were made serially rather than in parallel, so asking for even a month of data took a long time to come back. And it took over half a minute for a year's data when it didn’t just time out or send back a server error instead.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/wompwomp.png)
_womp womp_

The official API also didn’t seem to do any caching – a request that took 30 seconds to load the first time would take another 30s to load the second time. 

I believed that we could do better.

## A faster and more reliable APOD API

Since I’m using APOD API to power a portfolio project (yes I’m job hunting 😛), I really need it to be reliable and load quickly. I decided to implement my own API. 

You can find all the code [in this GitHub repo](https://github.com/ellanan/apod-api) if you want to look through it in detail as you read.

Here are the approaches I took: 

### 1. Avoid on-demand scraping

One of the main reasons why NASA’s API response is slow is because data scraping and parsing happens live, adding a significant overhead to each request. We can separate the data extraction step from the handling of API requests.

I ended up writing a script to dump the website’s data into a single 12MB JSON file. Pretty chunky for a JSON file, but given that a free tier Vercel function can have an unzipped size of 250MB and has 1024MB of memory, it’s still small enough to be directly loaded without needing to bother with a database.

The script comprises of two parts:

* `[getDataByDate(date: DateTime)](https://github.com/ellanan/apod-api/blob/main/api/_data/getDataByDate.ts)` is a function that, when given a particular date, will fetch the corresponding APOD webpage for that day, parse pieces of data out of the HTML using [cheerio](https://www.npmjs.com/package/cheerio) (JavaScript's equivalent to BeautifulSoup), and return structured data in the form of a JavaScript object.
* [`extractData.ts`](https://github.com/ellanan/apod-api/blob/main/extractor/extractData.ts), which calls `getDataByDate` with [days from a date range](https://github.com/ellanan/apod-api/blob/b43ee90a9a1b169447ed22c9a977e259eaf9bf39/extractor/extractData.ts#L30-L35) (initially "every day between _today_ and _June 16th, 1995_") using the [async](https://www.npmjs.com/package/async) library's `eachLimit` method to make multiple requests in parallel. It [stores each day's result as a separate JSON file on the filesystem](https://github.com/ellanan/apod-api/blob/b43ee90a9a1b169447ed22c9a977e259eaf9bf39/extractor/extractData.ts#L11-L19), and finally [combines all the daily JSON data into one single data.json](https://github.com/ellanan/apod-api/blob/b43ee90a9a1b169447ed22c9a977e259eaf9bf39/extractor/extractData.ts#L58-L77). 

You might wonder – why not fetch all the data first and save just one file at the end? When making 9000+ network requests, some of them are bound to fail, and you really don't want to have to start back from zero. Saving each day's data as it runs allows us to continue from where the failure happened.

Here's a comparison of timings before and after on-demand scraping: 


<table style="font-size: 14px; border-collapse: collapse;" border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td valign="bottom" nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;"><strong>Arguments</strong></p>
</td>
<td colspan="2" valign="bottom" nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;"><strong>My APOD-API </strong></p>
</td>
<td colspan="2" valign="bottom" nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;"><strong>NASA's APOD API</strong></p>
</td>
</tr>
<tr>
<td valign="bottom" nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">&nbsp;</p>
</td>
<td style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">Average TTFB*<br>(n=20)</p>
</td>
<td style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">Standard<br/>Deviation</p>
</td>
<td style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">Average TTFB<br>(n=20)</p>
</td>
<td style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">Standard<br/>Deviation</p>
</td>
</tr>
<tr>
<td valign="bottom" nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;">
<p style="margin-top: 8px;margin-bottom: 8px;">no argument</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">110 ms</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">21 ms</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">58 ms</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">29 ms</p>
</td>
</tr>
<tr>
<td valign="bottom" nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;">
<p style="margin-top: 8px;margin-bottom: 8px;">date</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">80 ms</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">34 ms</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">105 ms</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">88 ms</p>
</td>
</tr>
<tr>
<td valign="top" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;">
<p style="margin-top: 8px;margin-bottom: 8px;">start_date=2021-01-01<br>&amp;end_date=2022-01-01</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">151 ms</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">63 ms</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">35,358 ms</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">2,891 ms</p>
</td>
</tr>
<tr>
<td valign="bottom" nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;">
<p style="margin-top: 8px;margin-bottom: 8px;">count=100</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">96 ms</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">48 ms</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">9,701 ms</p>
</td>
<td nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;text-align: center;">
<p style="margin-top: 8px;margin-bottom: 8px;">1,198 ms</p>
</td>
</tr>
</tbody>
</table>
<small><a href="https://en.wikipedia.org/wiki/Time_to_first_byte">*https://en.wikipedia.org/wiki/Time_to_first_byte</a></small>

### 2. Fallback to on-demand data extraction

The extracted JSON will only have data up to the time when extraction was run. This means that sometimes there’ll be a new APOD that will be missing from our JSON. For those situations, it’d still be nice to fallback to live requests as a supplementary source of data.

In the code of our API request handler, we [check our extracted data.json to find which date is the last date that we have data for](https://github.com/ellanan/apod-api/blob/b43ee90a9a1b169447ed22c9a977e259eaf9bf39/api/index.ts#L7-L11), and [if the number of days between the last date and today is greater than 1](https://github.com/ellanan/apod-api/blob/b43ee90a9a1b169447ed22c9a977e259eaf9bf39/api/index.ts#L103-L109),  we then [fetch data for any missing dates in parallel](https://github.com/ellanan/apod-api/blob/b43ee90a9a1b169447ed22c9a977e259eaf9bf39/api/index.ts#L114-L136) (once again using `getDataByDate`, the same function we used for extracting data for the JSON file).

### 3. Aggressively cache requests

The bulk of time on APOD’s official API was spent waiting for the server to send the first byte. Since historical data doesn’t change, and new entries are added once a day, the actual application server doesn't need to be hit most of the time.

We can use headers to tell the Content Delivery Network (CDN) to aggressively cache the response of our cloud function. I’m hosting on Vercel, but this should work with Netlify and Cloudflare as well. 

The code for the specific headers we want to send from the function handler is:

```javascript
response
    .status(200)
    .setHeader(
        'Cache-Control',
        'max-age=0, ' +
        `s-maxage=${cacheDurationSeconds}, `+
        `stale-while-revalidate=${cacheDurationSeconds}`
    )
```

Breaking that down, 

* `max-age` tells browsers how long to cache a request. If a request for a resource is within the max-age, the cached response would be used instead. We set `max-age` to `0`, following [Vercel's advice](https://vercel.com/docs/concepts/edge-network/caching), to prevent browsers from caching API response locally. That way clients will still get new data as soon as it updates.
* `s-maxage` tells servers how long to cache a request. So when a request for a resource is within the s-maxage, the server (in our case, Vercel's CDN) will send the cached response. This is really powerful since this cache is shared across all users and devices. 
* We set `s-maxage` to a variable amount of time, because for requests that ask for dates using a relative time ("today's data", or "the last 10 day's data"), we only want to ask the CDN to cache that for roughly an hour since that might update when the next APOD comes out. For requests that ask for a specific date's data (for example between "2001-01-01" and "2002-01-01"), we can ask the CDN to cache that for a lot longer, since that isn't expected to change.
* We finally set a `stale-while-revalidate` header. That way, when the specified cache time expires, instead of having the next user wait until fresh data comes back, we tell the CDN to serve the cached data to the current user – but at the same time, hit our API endpoint for fresh data and cache that for the next request.

Since our API was loading all the data into memory already, the performance difference between cached vs. uncached requests shouldn’t be too noticeable, but faster is always better. 

The main goal with caching is to avoid running the cloud function, since Vercel’s free tier has a quota of 100 GB-hours (not sure what that means, but whatever it is, I don’t want to hit it). 

Comparison of timings before and after caching requests:


<table style="font-size: 14px; border-collapse: collapse;" border="0" cellspacing="0" cellpadding="0">
    <tbody>
        <tr>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" valign="bottom" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;"><strong>Arguments</strong></p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" colspan="2" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;"><strong>My APOD-API </strong></p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" colspan="2" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;"><strong>NASA's APOD API </strong></p>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" valign="bottom" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;"></p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;">
                <p style="margin-top: 8px;margin-bottom: 8px;">Average&nbsp;TTFB<br>(n=20)</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;">
                <p style="margin-top: 8px;margin-bottom: 8px;">Standard<br>Deviation</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;">
                <p style="margin-top: 8px;margin-bottom: 8px;">Average&nbsp;TTFB<br>(n=20)</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;">
                <p style="margin-top: 8px;margin-bottom: 8px;">Standard<br>Deviation</p>
            </td>
        </tr>
        <tr>
            <td valign="bottom" nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;">
                <p style="margin-top: 8px;margin-bottom: 8px;">no argument</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">33 ms</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">11 ms</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">58 ms</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">29 ms</p>
            </td>
        </tr>
        <tr>
            <td valign="bottom" nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;">
                <p style="margin-top: 8px;margin-bottom: 8px;">date</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">37 ms</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">23 ms</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">105 ms</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">88 ms</p>
            </td>
        </tr>
        <tr>
            <td valign="top" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;">
                <p style="margin-top: 8px;margin-bottom: 8px;">start_date=2021-01-01<br>&amp;end_date=2022-01-01</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">46 ms</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">29 ms</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">35,358 ms</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">2,891 ms</p>
            </td>
        </tr>
        <tr>
            <td valign="bottom" nowrap="nowrap" style="padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;">
                <p style="margin-top: 8px;margin-bottom: 8px;">count=100</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">31 ms</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">13 ms</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">9,701 ms</p>
            </td>
            <td style="text-align: center;padding: 0 10px;border: 1px solid #cccccc;font-family: 'Helvetica', 'Arial', sans-serif;" nowrap="nowrap">
                <p style="margin-top: 8px;margin-bottom: 8px;">1,198 ms</p>
            </td>
        </tr>
    </tbody>
</table>

### 4.  (Bonus) Automated daily updates

We want to keep our data file in sync with NASA’s APOD website as much as possible, since reading data from our JSON file is much faster than falling back to fetching data over network. 

Automating this doesn't exactly improve performance –  I could set an alarm for myself to run the extraction script every night at midnight, commit any changes, and push to trigger a new deploy. 

Thankfully, I won't have to, since apparently Github Actions aren't limited to running on Pull Requests, you can schedule them too.

```yaml
name: Update Data Every 3 Hours

on:
  schedule:
    # At minute 15 past every 3rd hour.
    - cron: '15 */3 * * *'
  workflow_dispatch:

jobs:
  update-data:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: '16'
      - run: npm install
      - run: npm run update-data
      - name: Commit changes
        run: |
          if [ -n "$(git status --porcelain)" ]; then
            git config --global user.name 'your_username'
            git config --global user.email 'your_email@users.noreply.github.com'
            git add .
            git commit -m "Automated data update"
            git push
          else
            echo "no changes";
          fi
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-58.png)

## Conclusion

In summary, where possible and sensible:

1. Extract data _before_ requests are received and try to keep it up-to-date
2. Make fallback requests in parallel
3. Cache responses on the CDN

The code for all this is a bit too lengthy to fit into an article, but I believe these principles should be more broadly applicable for public-facing APIs (plenty more just on [api.nasa.gov](https://api.nasa.gov/)!). Feel free to peruse [the repo](https://github.com/ellanan/apod-api) to see how it all fits together.

Thank you for reading! I’d love to hear any feedback you may have. You can find me on Twitter [@ellanan_](https://twitter.com/ellanan_) or on [LinkedIn](https://www.linkedin.com/in/ellanan/).   

