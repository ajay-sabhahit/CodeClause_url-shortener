#import libraries to be used

import pyshorteners as ps

long_url = input("Enter the url needed to be shortened:\n")

#define the function

def short_url(long_url):
    short = ps.Shortener()
    print(short.tinyurl.short(long_url))

#call the function
short_url(long_url)
