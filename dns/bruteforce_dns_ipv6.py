#!/usr/bin/python

import dns.resolver
myquery = dns.resolver.Resolver()
domain= "yahoo.com"

def func_aaaa(_target):
    question = myquery.query(_target, 'AAAA')

    for _addr in question:
        print('[+] - ' + _target + '---> ' + str(_addr))

def bruteforce_dns_ipv4(_wordlist):
    with open(_wordlist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")

            if not machine:
                break

            try:
                target = machine + "." + domain
                func_aaaa(target)
            except:
                pass

bruteforce_dns_ipv4("file.txt")

