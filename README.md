getPyModuleList.py
------------------
The following python script parses the python website using Beautiful soup to
output a list of modules supported by the python version. The script optionally
also takes a python module as input and checks whether the module is supported
in the python version. The following are some examples:

```

    python getPyModuleList.py -h
    usage: getPyModuleList.py [-h] version [module]
    
    Get the list of python modules based on version
    
    positional arguments:
      version     python version
      module      module to check
    
    optional arguments:
      -h, --help  show this help message and exit
    
    
    python getPyModuleList.py 2.7
    [u'filecmp', u'heapq', u'code', u'dbm', u'imageop', u'distutils',..]
    
    python getPyModuleList.py 2.7 turtle
    turtle is supported
    
    python getPyModuleList.py 2.7 requests
    requests is not supported
```

testHttpsServer.py
------------------

Tests whether a website supports http-to-https redirection, secure cookies,
and Strict-Transport-Security

```

    python testHttpsServer.py -h
    usage: testHttpsServer.py [-h] hostname
    
    Tests whether a website supports http-to-https redirection, secure cookies,
    and Strict-Transport-Security
    
    positional arguments:
      hostname    for example www.example.com
    
    optional arguments:
       -h, --help  show this help message and exit

```
