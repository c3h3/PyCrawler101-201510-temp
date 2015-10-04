# create a counter start from 1
counter = 1

# create a while loop, and keep going until no resources
while True:
    # when while loop go to the end, it will occurs a exception
    try:
        # {} is where you put conter in
        url = "http://pi.isuphoto.org/post/{}"
        res = resquests.get(url.format(counter))
        print res
        # and more code if you need...
        # then move to next resource
        counter += 1
    # when no resources, a exception happens, print then handle it
    except Exception, e:
        print str(e)
        # and more code if you need...
        # exit while loop 
        break
    
