import re
#import lxml.html

def parse_links_regex(filename):
    """question 2a

    Using the re module, write a function that takes a path to an HTML file
    (assuming the HTML is well-formed) as input and returns a dictionary
    whose keys are the text of the links in the file and whose values are
    the URLs to which those links correspond. Be careful about how you handle
    the case in which the same text is used to link to different urls.
    
    For example:

        You can get file 1 <a href="1.file">here</a>.
        You can get file 2 <a href="2.file">here</a>.

    What does it make the most sense to do here? 
    """
    dict = {}
    keylinks = re.findall('<a href="([^"]+)"[^>]*>([^<]+)</a>', open(filename).read())
    for key in keylinks:
        try:
            dict[key[1]] = [key[0]]
        except KeyError:
            dict[key[1]].append(key[0])
    return dict

def parse_links_xpath(filename):
    """question 2b

    Do the same using xpath and the lxml library from http://lxml.de rather
    than regular expressions.
    
    Which approach is better? (Hint: http://goo.gl/mzl9t)
    """
#The following is simply a guess. I couldn't test it because of my failure to load lxml
"""
    infile = open(filename)
    src = infile.read()
    infile.close()

    gen = lxml.html.iterlinks(src)
    links = list(gen)

    dict = {}

    for l in links:
        try:
            dictionary[l[0].text] = l[2]
        except KeyError:
            dictionary[l[0].text].append(l[2])

    return dictionary
    """
