'''
Copyright(c) 2014 YSUV - Print certificates in human readable format
Use pyopenssl to perform the following equivalent openssl command
    openssl x509 -noout -in <cert in PEM format> -text

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to
do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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
