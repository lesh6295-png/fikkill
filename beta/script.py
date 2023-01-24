

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=50,
                           requestsPerConnection=1000,
                           pipeline=False
                           )
    comments = open('D:\\fickill\\beta\\comments.txt').readlines()
    end = open('D:\\fickill\\beta\\end.txt').readlines()
    start = open('D:\\fickill\\beta\\start.txt').readlines()
    errors = open('D:\\fickill\\beta\\errors.txt').readlines()

    for word in range(1,50):
        err = random.choice(errors)
        engine.queue(target.req, [err.rstrip(),random.choice(start),err,random.choice(end), random.choice(comments), 33609713])
        #engine.queue(target.req, [words[word].rstrip(),random.choice(words),random.choice(words),random.choice(words)])


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status != 404:
        table.add(req)