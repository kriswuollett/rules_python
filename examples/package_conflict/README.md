# python module conflicts

Install Bazelisk and try running:

```console
$ bazel run //hello_world:hello_world_server_py
```

The module `google.api` cannot be found:

```
Python 3.9.8 (main, Nov 10 2021, 09:21:22) 
[Clang 13.0.0 (clang-1300.0.29.3)]
################################################################################
/private/var/tmp/_bazel_kris/d8a7b0be849d6541bed1bb847a481917/execroot/__main__/bazel-out/darwin-fastbuild/bin/hello_world/hello_world_server_py.runfiles/com_google_protobuf/python
google/ (NO __init__.py)
google/protobuf/__init__.py

# Protocol Buffers - Google's data interchange format
# Copyright 2008 Google Inc.  All rights reserved.
# https://developers.google.com/protocol-buffers/
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Copyright 2007 Google Inc. All Rights Reserved.

__version__ = '3.18.0'


################################################################################
/private/var/tmp/_bazel_kris/d8a7b0be849d6541bed1bb847a481917/execroot/__main__/bazel-out/darwin-fastbuild/bin/hello_world/hello_world_server_py.runfiles/pip_deps_pypi__protobuf
google/__init__.py

# __path__ manipulation added by bazelbuild/rules_python to support namespace pkgs.
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

google/protobuf/__init__.py

# Protocol Buffers - Google's data interchange format
# Copyright 2008 Google Inc.  All rights reserved.
# https://developers.google.com/protocol-buffers/
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Copyright 2007 Google Inc. All Rights Reserved.

__version__ = '3.19.1'


################################################################################
/private/var/tmp/_bazel_kris/d8a7b0be849d6541bed1bb847a481917/execroot/__main__/bazel-out/darwin-fastbuild/bin/hello_world/hello_world_server_py.runfiles/com_google_googleapis
google/ (NO __init__.py)
google/api/ (NO__init__.py)

################################################################################
/usr/local/lib/python3.9/site-packages
google/ (NO __init__.py)
google/protobuf/__init__.py

# Protocol Buffers - Google's data interchange format
# Copyright 2008 Google Inc.  All rights reserved.
# https://developers.google.com/protocol-buffers/
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Copyright 2007 Google Inc. All Rights Reserved.

__version__ = '3.17.3'


Traceback (most recent call last):
  File "/private/var/tmp/_bazel_kris/d8a7b0be849d6541bed1bb847a481917/execroot/__main__/bazel-out/darwin-fastbuild/bin/hello_world/hello_world_server_py.runfiles/__main__/hello_world/hello_world_server.py", line 36, in <module>
    from hello_world import HelloWorldServicer, hello_world_pb2, hello_world_pb2_grpc
  File "/private/var/tmp/_bazel_kris/d8a7b0be849d6541bed1bb847a481917/execroot/__main__/bazel-out/darwin-fastbuild/bin/hello_world/hello_world_server_py.runfiles/__main__/hello_world/hello_world_py_proto_pb/hello_world/hello_world_pb2.py", line 14, in <module>
    from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
ModuleNotFoundError: No module named 'google.api'
```

A possible solution is to completely remove the `protobuf`'s `google/__init__.py` file instead of
using the `__path__` manipulation. Try removing the file named like
`/private/var/tmp/_bazel_kris/d8a7b0be849d6541bed1bb847a481917/execroot/__main__/bazel-out/darwin-fastbuild/bin/hello_world/hello_world_server_py.runfiles/pip_deps_pypi__protobuf/google/__init__.py`
and try running the server again.
