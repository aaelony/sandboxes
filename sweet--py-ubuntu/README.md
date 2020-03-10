# Ubuntu Python installs 

```
make build
make run
```

Or if you're just wanting to run Tensorflow (python2) on ubuntu:
```
docker run -it --rm tensorflow/tensorflow bash
```

## Todo: Issues to fix

### Theano/pymc3 install problems

```
root@4a6ce75aa6ad:/# python
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pymc3 

You can find the C code in this temporary file: /tmp/theano_compilation_error_5p8lpuod
library inuxkit-x86_64-with-Ubuntu-18.04-bionic-x86_64-3.6.9-64/lazylinker_ext/mod.cpp:1:10: is not found.
Traceback (most recent call last):
  File "/venv/lib/python3.6/site-packages/theano/gof/lazylinker_c.py", line 81, in <module>
    actual_version, force_compile, _need_reload))
ImportError: Version check of the existing lazylinker compiled file. Looking for version 0.211, but found None. Extra debug information: force_compile=False, _need_reload=True

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/venv/lib/python3.6/site-packages/theano/gof/lazylinker_c.py", line 105, in <module>
    actual_version, force_compile, _need_reload))
ImportError: Version check of the existing lazylinker compiled file. Looking for version 0.211, but found None. Extra debug information: force_compile=False, _need_reload=True

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/venv/lib/python3.6/site-packages/pymc3/__init__.py", line 5, in <module>
    from .distributions import *
  File "/venv/lib/python3.6/site-packages/pymc3/distributions/__init__.py", line 1, in <module>
    from . import timeseries
  File "/venv/lib/python3.6/site-packages/pymc3/distributions/timeseries.py", line 2, in <module>
    import theano.tensor as tt
  File "/venv/lib/python3.6/site-packages/theano/__init__.py", line 110, in <module>
    from theano.compile import (
  File "/venv/lib/python3.6/site-packages/theano/compile/__init__.py", line 12, in <module>
    from theano.compile.mode import *
  File "/venv/lib/python3.6/site-packages/theano/compile/mode.py", line 11, in <module>
    import theano.gof.vm
  File "/venv/lib/python3.6/site-packages/theano/gof/vm.py", line 674, in <module>
    from . import lazylinker_c
  File "/venv/lib/python3.6/site-packages/theano/gof/lazylinker_c.py", line 140, in <module>
    preargs=args)
  File "/venv/lib/python3.6/site-packages/theano/gof/cmodule.py", line 2396, in compile_str
    (status, compile_stderr.replace('\n', '. ')))
Exception: Compilation failed (return status=1): /root/.theano/compiledir_Linux-4.19-linuxkit-x86_64-with-Ubuntu-18.04-bionic-x86_64-3.6.9-64/lazylinker_ext/mod.cpp:1:10: fatal error: Python.h: No such file or directory.  #include <Python.h>.           ^~~~~~~~~~. compilation terminated.. 

```

### Tensorflow

Not certain how to avoid or fix below message warnings:

```python
root@faba9477e85e:/# python
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
2020-03-10 18:41:23.297609: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'libnvinfer.so.6'; dlerror: libnvinfer.so.6: cannot open shared object file: No such file or directory
2020-03-10 18:41:23.297768: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'libnvinfer_plugin.so.6'; dlerror: libnvinfer_plugin.so.6: cannot open shared object file: No such file or directory
2020-03-10 18:41:23.297814: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:30] Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.

```



# Cleanup

When you need to cleanup...

```
docker system prune -a
```
