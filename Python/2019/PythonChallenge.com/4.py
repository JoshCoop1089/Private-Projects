# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:40:15 2019

@author: joshc
"""
"""
<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough. -->

"""

def urlget(reps, nums, url, count = 3):
    for i in range(reps):
        with rq.urlopen(url+nums) as request:
           count += 1
           string = str(request.read(300))
           print("url is:" + string)
           pattern = re.compile("ing is ")
           loc = re.search(pattern, string)
           print(loc)
           location = str(loc).split(",")
           print(location)
           num = int(location[1][1:-1])
           print("count is: " + str(count))
           nums = string[num:-1]
    return nums
import urllib.request as rq
import re as re
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nums = "94485"
count = 3
nums = urlget(82, nums, url)
nums = urlget(200, str(int(nums)/2), url, count = 85)
print(url+nums)

#url to stage 5-> peak.html
