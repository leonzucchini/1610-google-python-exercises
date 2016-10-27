"""
happy.www.corp.google.com

# Background
image
cut into stripes
each stripe contains a url
some get requests in apache log files contain "puzzle"

# First task
parse log file
find all urls with "puzzle" (regex "space garbage puzzle garbage space")
check for duplicates
print puzzle URLs in alphabetical order

# todir
find all urls and download
write into output directory
give them names like "img1" "img2", ...

# use index.html to concatenate images

# Second job has images in more complicated order

"""