'''
Copyright(c) 2014 YSUV - Tests a website whether it supports some of
the security concepts listed at:
http://www.html5rocks.com/en/tutorials/security/transport-layer-security/

(1) Switching from http to https
(2) Check whether cookies are set using `secure`
(3) Supports strict transport security - domain and subdomains



MIT licence

'''

import httplib
import argparse
from urlparse import urlparse


class SSLTest:

    SUPPORTED = '[ SUPPORTED      ] : '
    NOT_SUPPORTED = '[ NOT-SUPPORTED  ] : '
    NOT_APPLICABLE = '[ NOT-APPLICABLE ] : '
    ERROR = '[ ERROR ] : '

    def __init__(self, url):
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url

        parsedUrl = urlparse(url)
        self.hostname = parsedUrl.netloc
        self.path = parsedUrl.path
        self.query = parsedUrl.query

    def testRedirectToHttps(self):
        ''' Tests whether the server redirects a http url to
        https thereby always forcing the client to use https
        '''
        httpConn, res = self.connectToServer(httplib.HTTPConnection)
        if not res:
            return
        redirection = [httplib.MOVED_PERMANENTLY,
                       httplib.FOUND,
                       httplib.TEMPORARY_REDIRECT]
        testName = 'Redirection to https!'
        location = res.getheader('Location')
        if res.status in redirection and location \
           and location.startswith('https'):
            print self.SUPPORTED + testName
        else:
            print self.NOT_SUPPORTED + testName

    def connectToServer(self, connFunc):
        httpsConn = None
        res = None

        try:
            httpsConn = connFunc(self.hostname)
            httpsConn.request('GET', '/', body=None, headers={})
            res = httpsConn.getresponse()
        except Exception as e:
            print self.ERROR + 'Couldnt connect to the server'
            print 'Exception details: ' + str(e)
            httpsConn.close()
        finally:
            return httpsConn, res

    def testStrictTransportSecurity(self):
        ''' Tests whether Strict transport security is supported '''

        httpsConn, res = self.connectToServer(httplib.HTTPSConnection)
        if not res:
            return

        testName = 'Strict-Transport-Security!'
        if res.getheader('strict-transport-security'):
            print self.SUPPORTED + testName
            header = res.getheader('strict-transport-security').split(';')
            header = [val.lower() for val in header]
            testName = 'Strict-Transport-Security subdomain support!'
            if 'includeSubDomains'.lower() in header:
                print self.SUPPORTED + testName
            else:
                print self.NOT_SUPPORTED + testName
        else:
            print self.NOT_SUPPORTED + testName
        httpsConn.close()

    def testSecureCookies(self):
        ''' Tests whether the cookies set are secure '''
        httpsConn, res = self.connectToServer(httplib.HTTPSConnection)
        if not res:
            return
        cookie_header = res.getheader('Set-Cookie')
        if cookie_header is None:
            print self.NOT_APPLICABLE + 'Site has not set a cookie!'
            return
        cookie_values = cookie_header.split('; ')
        cookie_values = [val.lower() for val in cookie_values]

        testName = 'Cookies protected with \'secure\'!'
        if 'secure' in cookie_values:
            print self.SUPPORTED + testName
            return
        elif 'httponly' in cookie_values:
            print self.SUPPORTED + 'Cookies protected with HttpOnly!'
        print self.NOT_SUPPORTED + testName
        httpsConn.close()

    def run_tests(self):
        self.testRedirectToHttps()
        self.testStrictTransportSecurity()
        self.testSecureCookies()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Tests whether a website '
                                                 'supports http-to-https '
                                                 'redirection, '
                                                 'secure cookies, and '
                                                 'Strict-Transport-Security')

    parser.add_argument('hostname', help='for example www.example.com')
    args = parser.parse_args()
    if args.hostname:
        test = SSLTest(args.hostname)
        test.run_tests()
