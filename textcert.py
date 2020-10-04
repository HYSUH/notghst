'''
Copyright(c) 2014 YSUV - Print certificates in human readable format
Use pyopenssl to perform the following equivalent openssl command
    openssl x509 -noout -in <cert in PEM format> -text

MIT licence
'''


import sys
import argparse
from OpenSSL.crypto import (FILETYPE_TEXT, FILETYPE_PEM, load_certificate,
                            dump_certificate
                            )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Prints the PEM certifcate'
                                                 'file in human readable '
                                                 'format')

    parser.add_argument('filename', help='certificate filename')
    args = parser.parse_args()
    if args.filename:
        with open(args.filename, 'r') as f:
            buffer = f.read()
            cert = load_certificate(FILETYPE_PEM, buffer)
            print dump_certificate(FILETYPE_TEXT, cert)
