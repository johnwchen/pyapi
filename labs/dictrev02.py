#!/usr/bin/env python3

def main():
    firewalldict = {'sip':'5060', 'ssh':'22', 'http':'80'}
    print(firewalldict)

    firewalldict['https'] =443

    print('The print statement can be passed multiple items, provided they are separated by commas')
    print("The port in use for HTTP Secure is:", firewalldict['https'])

    print(firewalldict.keys())
    print(firewalldict.values())
    del firewalldict["sip"]
    print(firewalldict)

if __name__ == "__main__":
    main()