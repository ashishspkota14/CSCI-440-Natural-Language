import rtn, simple, english

sentence = ['a','book','on','the','table','with','a','cover']
for t in rtn.match3(english.net, ':noun3', 1, sentence) :
    print("Got one!!\n  %s\n" % str(t))

