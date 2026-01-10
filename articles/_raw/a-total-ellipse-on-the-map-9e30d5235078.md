---
title: A Total Ellipse on the Map
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T21:26:26.000Z'
originalURL: https://freecodecamp.org/news/a-total-ellipse-on-the-map-9e30d5235078
coverImage: https://cdn-media-1.freecodecamp.org/images/0*4Di0P5E6_sQYXxYV.jpg
tags:
- name: algorithms
  slug: algorithms
- name: code
  slug: code
- name: maps
  slug: maps
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Dalya Gartzman

  Or, how to choose the best way to walk to the beach after work

  It was a cool autumn evening when Hila Kloper and I were thinking of going to the
  beach after work. The beach is about 2.5Km away from the office.

  We were even consideri...'
---

By Dalya Gartzman

#### Or, how to choose the best way to walk to the beach after work

It was a cool autumn evening when Hila Kloper and I were thinking of going to the beach after work. The beach is about 2.5Km away from the office.

We were even considering strolling down the streets of Tel Aviv, willing to stretch our path to 3Km, and thinking to ourselves “mmm we wonder how far this stretch can take us?”

Well, long story short, we didn’t go to the beach. Instead, we wrote a script that draws an ellipse around the office and the beach. The ellipse covers the city area we _may_ go through if we ever decide to go to the beach after work.

![Image](https://cdn-media-1.freecodecamp.org/images/Kpo6C3-boqp5qXw2eZlhoJsP10FM0kZhDnIv)
_When developers want to do something fun outside and they end up writing a script about it instead._

### It’s the Ellipse of Life

**Or - why should we care about ellipses?**

A circle is in some way the “natural” area around one point. An ellipse is the “natural” area around two points or a line. To name a few examples, [bodies of mass move in elliptic orbits](https://en.wikipedia.org/wiki/Elliptic_orbit), ellipses represent the [distortion caused by projecting a 3D map on 2D](https://en.wikipedia.org/wiki/Tissot%27s_indicatrix), and ellipses are also an accurate way to plot [confidence of noisy GPS data](https://anitagraser.com/2018/09/04/plotting-gps-trajectories-with-error-ellipses-using-time-manager/) (and [confidence areas in 2D data](https://www.xarg.org/2018/04/how-to-plot-a-covariance-error-ellipse/) in general).

In our case, we wanted to draw an area around the line starting at our office and ending at the beach. The easiest solution we found for [drawing ellipses](https://gis.stackexchange.com/questions/243459/drawing-ellipse-with-shapely) involved [shapely](https://pypi.org/project/Shapely/) and [pyplot.](https://matplotlib.org/) It still required some modifications due to our GPS and map constraints.

So, if you are here because you are looking for an easy copy-pastable code that draws an ellipse on a map — you can go to [this repository](https://github.com/DalyaG/CodeSnippetsForPosterity/tree/master/PlotEllipse) we made. If you are also interested to learn **how** we found the complete solution to our problem, you are welcome to join us for the ride. We rediscover elementary geometry, learn about coordinates systems, and play around with some math code.

### Girls Just Wanna Have Ellipses

> **Us:** “Oh there must be a package somewhere that can draw an ellipse on a map!”  
> **The Internet:** “No there isn’t.”  
> **Us:** “But there must be a simple copy-pastable code somewhere!”  
> **Stackoverflow:** “I have incomprehensible ones if you want.”  
> **Us:** “Well, OK, we’ll take an hour and make one ourselves!”  
> **Reality:** “…”

Figuring out what an ellipse actually is was the first challenge.  
[Wolfram Alpha](http://mathworld.wolfram.com/Ellipse.html) told us that an ellipse is the set of points that have the same sum-of-distances from two mutual centers. Or something like that. Wolfram Alpha can be rather cryptic sometimes. But they have a gif so that’s nice.

![Image](https://cdn-media-1.freecodecamp.org/images/ubxw-BHnbWQyhC1gHYMoJV3BRDBG-2RUlr7I)
_Ah… now that’s clear._

So all we have to do is make sure we have these inputs:

* `p1, p2` - GPS coordinates.
* `r` - the radius which is actually the sum of distances from a point on the ellipse to the two centers.

Then follow this plan:

1. Find `a` and `b`, the axes of the ellipse.
2. Draw an ellipse around the origin `(0,0)` measured in meters.
3. Move the ellipse to the center between the input GPS locations.
4. Rotate according to the angle between the input GPS locations.

![Image](https://cdn-media-1.freecodecamp.org/images/-970C4VzJQ2BxklnOsjfYlAp2MbeTUrmq-Mk)

And that’s it.

Sounds simple enough, right?

### The Long and Winding Road (That Leads to Ellipse)

#### Step 1. Find the axes.

Here we needed to do some basic Pythagorean algebra. This image from [Wikipedia](https://en.wikipedia.org/wiki/Ellipse) was somewhat helpful:

![Image](https://cdn-media-1.freecodecamp.org/images/am1h1sbO6znf1TBZs-I-G2j6seQMYXDX12k5)

Computing `c` from GPS coordinates was easy thanks to [haversine](https://pypi.org/project/haversine/) package.

```python
def GetEllipseAxisLengths(p1_lat, p1_lng, p2_lat, p2_lng,
                          radius_in_meters):
    c2 = haversine((p1_lat, p1_lng), (p2_lat, p2_lng)) * 1000.0
    if radius_in_meters < c2:
        raise ValueError("Please specify radius larger than the               
                          distance between the two input points.")
    a = radius_in_meters / 2.0
    b = sqrt(pow(a, 2) - pow(c2 / 2.0, 2))
    return a, b
```

#### Step 2. Draw an Ellipse Around the Origin.

What we did here is that we took evenly spaced points on the `x` axis and for each one found the two points on the ellipse that project to it:

![Image](https://cdn-media-1.freecodecamp.org/images/prw5iyWrz2XEn9FVkbcOvoF-VA-STwLSc1Oy)
_Luckily we found this lovely equation on Wikipedia._

```python
def GetEllipsePointInMeters(a, b, num_points):
    """
    :param a: length of "horizontal" axis in meters
    :param b: length of "vertical" axis in meters
    :param num_points: (half the) number of points to draw
    :return: List of tuples of perimeter points on the ellipse, 
             centered around (0,0), in m.
    """
    x_points = list(np.linspace(-a, a, num_points))[1:-1]
    y_points_pos = [sqrt(pow(a, 2) - pow(x, 2)) * 
                    (float(b) / float(a))
                    for x in x_points]
    y_points_neg = [-y for y in y_points_pos]

    perimeter_points_in_meters = 
        [tuple([-a, 0])] + \
        [tuple([x, y]) for x, y in zip(x_points, y_points_pos)] + \
        [tuple([a, 0])] + \
        list(reversed([tuple([x, y]) 
                       for x, y in zip(x_points, y_points_neg)]))
    return perimeter_points_in_meters
```

#### Step 3. How Do You Even Add Meters to GPS?

Well this was a tricky one, and the answer lies in understanding that

![Image](https://cdn-media-1.freecodecamp.org/images/Hc00Kw6PkLDTkU8eq7GYS6fj10fIP48qGltv)
_Unleashing the secrets of elementary geometry._

> Fun fact: the Earth’s radius is around 6371000 meters on average!

```python
def AddMetersToPoint(center_lng, center_lat, dx, dy):
    """
    :param center_lng, center_lat: GPS coordinates of the center  
           between the two input points.
    :param dx: distance to add to x-axis (lng) in meters
    :param dy: distance to add to y-axis (lat) in meters
    """
    new_x = (center_lng + (dx / R_EARTH) * (180 / pi) /   
             np.cos(center_lat * pi/180))
    new_y = center_lat + (dy / R_EARTH) * (180 / pi)
    return tuple([new_x, new_y])
```

#### Step 4. Rotate.

This time, the wonders of the internet did not fail us (as they did on our major ellipse-drawing task). We found [shapely](https://pypi.org/project/Shapely/) package to do the rotation for us. The one trick to remember here is that you can’t rotate the points one by one. Rather you should _form a shape first_, and then _rotate the entire shape_.

```python
def GetEllipsePoints(p1_lat, p1_lng, p2_lat, p2_lng, 
                     perimeter_points_in_meters):
    """
    Enter ellipse centers in lat-lng and ellipse perimeter points    
    around the origin (0,0), and get points on the perimeter of the 
    ellipse around the centers in lat-lng.
    :param p1_lat: lat coordinates of center point 1
    :param p1_lng: lng coordinates of center point 1
    :param p2_lat: lat coordinates of center point 2
    :param p2_lng: lng coordinates of center point 2
    :param perimeter_points_in_meters: List of tuples of perimeter 
           points on the ellipse, centered around (0,0), in m.
    :return: List of the points we really want, tuples of (lat,lng)
    """
    center_lng = (p1_lng + p2_lng) / 2.0
    center_lat = (p1_lat + p2_lat) / 2.0
    perimeter_points_in_lng_lat = \
        [AddMetersToPoint(center_lng, center_lat, p[0], p[1])
         for p in perimeter_points_in_meters]
    ellipse = LineString(perimeter_points_in_lng_lat)

    angle = degrees(atan2(p2_lat - p1_lat, p2_lng - p1_lng))
    ellipse_rotated = affinity.rotate(ellipse, angle)

    ellipse_points_lng_lat = list(ellipse_rotated.coords)
    ellipse_points = [tuple([p[1], p[0]]) 
                      for p in ellipse_points_lng_lat]
    return ellipse_points
```

#### Surprise! Step 5. Draw on s2 Map!

We wanted to present the ellipse nicely on an [s2map](http://s2map.com). Apparently you can do that by opening the URL from inside your script. We used [subprocess](https://docs.python.org/2/library/subprocess.html) to do that.

```python
def OpenS2Map(points):
    url = \
      "http://s2map.com/#order=latlng&mode=polygon&s2=false" \
      "&points={}".format(str(points).replace(" ", ","))
    cmd = ["python", "-m", "webbrowser", "-t", url]
    subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                     stderr=subprocess.STDOUT).communicate()
```

![Image](https://cdn-media-1.freecodecamp.org/images/OMCosB902DjSzC27OJcbQG3Z4UNQTBVq5LwC)
_OK. can we go the beach now?_

### The Neighbor’s Ellipse Is Rounder

You might notice our ellipse is not perfect. The points are evenly spaced on the axis between the centers, but they are not evenly spaced on the perimeter of the ellipse. The `GPS->meters->GPS` transformation might result in loss of meters here and there. But hey, done is better than perfect, and we have to leave something to do for the next time we want to go to the beach, right?

