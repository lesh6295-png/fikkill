import random
# Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=800,
                           requestsPerConnection=3000,
                           pipeline=False
                           )
                           
    START_FNF = 1
    END_FNF = 1+1
    REPARE = 10
    GLOBAL_REPARE = 100

    words = open('words.txt').readlines()
    
    #for i in range(3, 8):
    #    engine.queue(target.req, randstr(i), learn=1)
    #    engine.queue(target.req, target.baseInput, learn=2)
    
    for q in range(1,len(words)/10):
        for j in range(1,REPARE):
            for i in range(START_FNF,END_FNF):
                #engine.queue(target.req, [str(i).rstrip(), random.choice(words).rstrip()])
                #engine.queue(target.req, [str(random.randint(START_FNF,END_FNF)).rstrip(), random.choice(words).rstrip()])
                engine.queue(target.req, ['12889441'.rstrip(), 'я стал знаменитым!'.rstrip()])

    
    """for q in range(1,100):
        for i in open('D:\\words.txt'):
            engine.queue(target.req, i.rstrip());

    """

def handleResponse(req, interesting):
    if req.status==0:
        return;
    if req.status==403:
        return
    if req.status!=200:
        table.add(req)
