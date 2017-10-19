import whois

domain = whois.whois(raw_input('Enter domain name: '))

print "The domain %s was registered by %s on %s with Name Servers: %s" % (domain.id, domain.creation_date, domain.name, domain.nameservers)