#!/usr/bin/python

import shodan
shodan_mykey='HHxgUv88iHq8G6kXJA7JGbfmLIij84iz'
shodan_api= shodan.Shodan(shodan_mykey)
shodan_target='179.191.78.194'
shodan_host = shodan_api.host(shodan_target)


def shodan_info():
    print('[*] - Informacoes genericas do ALVO')
    print('IP alvo:', shodan_host['ip_str'])
    print('Organizacao:', shodan_host.get('org','n/a'))
    print('Sistema Operacional:', shodan_host.get('os','n/a'))

def shodan_portscan():
    print('[*] - Identificacao de portas abertas')

    for _line in shodan_host['data']:
        print("[+] - Porta Aberta:", _line['port'])
        print("[+] - Banner:", _line['data'])
        print("-" * 60)


def shodan_vuln():
    print('[*] - Lista de possiveis vulnerabilidades:')

    for item in shodan_host['vulns']:
        CVE = item.replace('!','')
        print('Vulnerability', CVE)





print("-" * 60)
print("-" * 60)
shodan_info()
print('-' * 60)
shodan_portscan()
print('-' * 60)
shodan_vuln()
print("-" * 60)



