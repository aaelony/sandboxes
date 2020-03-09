
```
make build
make run
```

Or if you're just wanting to run Tensorflow (python2) on ubuntu:
```
docker run -it --rm tensorflow/tensorflow bash
```


Not certain how to avoid or fix below message warnings:

```python
>>> import tensorflow as tf
2020-03-09 21:06:34.952677: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'libnvinfer.so.6'; dlerror: libnvinfer.so.6: cannot open shared object file: No such file or directory
2020-03-09 21:06:34.953100: W tensorflow/stream_executor/platform/default/dso_loader.cc:55] Could not load dynamic library 'libnvinfer_plugin.so.6'; dlerror: libnvinfer_plugin.so.6: cannot open shared object file: No such file or directory
2020-03-09 21:06:34.953394: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:30] Cannot dlopen some TensorRT libraries. If you would like to use Nvidia GPU with TensorRT, please make sure the missing libraries mentioned above are installed properly.
```
