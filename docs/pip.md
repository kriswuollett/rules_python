<!-- Generated with Stardoc: http://skydoc.bazel.build -->

<a name="#compile_pip_requirements"></a>

## compile_pip_requirements

<pre>
compile_pip_requirements(<a href="#compile_pip_requirements-name">name</a>, <a href="#compile_pip_requirements-extra_args">extra_args</a>, <a href="#compile_pip_requirements-visibility">visibility</a>, <a href="#compile_pip_requirements-requirements_in">requirements_in</a>, <a href="#compile_pip_requirements-requirements_txt">requirements_txt</a>, <a href="#compile_pip_requirements-tags">tags</a>,
                         <a href="#compile_pip_requirements-kwargs">kwargs</a>)
</pre>

Generates targets for managing pip dependencies with pip-compile.

By default this rules generates a filegroup named "[name]" which can be included in the data
of some other compile_pip_requirements rule that references these requirements
(e.g. with `-r ../other/requirements.txt`).

It also generates two targets for running pip-compile:

- validate with `bazel test <name>_test`
- update with   `bazel run <name>.update`


**PARAMETERS**


| Name  | Description | Default Value |
| :-------------: | :-------------: | :-------------: |
| name |  base name for generated targets, typically "requirements"   |  none |
| extra_args |  passed to pip-compile   |  <code>[]</code> |
| visibility |  passed to both the _test and .update rules   |  <code>["//visibility:private"]</code> |
| requirements_in |  file expressing desired dependencies   |  <code>None</code> |
| requirements_txt |  result of "compiling" the requirements.in file   |  <code>None</code> |
| tags |  tagging attribute common to all build rules, passed to both the _test and .update rules   |  <code>None</code> |
| kwargs |  other bazel attributes passed to the "_test" rule   |  none |


<a name="#pip_install"></a>

## pip_install

<pre>
pip_install(<a href="#pip_install-requirements">requirements</a>, <a href="#pip_install-name">name</a>, <a href="#pip_install-kwargs">kwargs</a>)
</pre>

Accepts a `requirements.txt` file and installs the dependencies listed within.

Those dependencies become available in a generated `requirements.bzl` file.

This macro runs a repository rule that invokes `pip`. In your WORKSPACE file:

```python
pip_install(
    requirements = ":requirements.txt",
)
```

You can then reference installed dependencies from a `BUILD` file with:

```python
load("@pip//:requirements.bzl", "requirement")
py_library(
    name = "bar",
    ...
    deps = [
       "//my/other:dep",
       requirement("requests"),
       requirement("numpy"),
    ],
)
```

> Note that this convenience comes with a cost.
> Analysis of any BUILD file which loads the requirements helper in this way will
> cause an eager-fetch of all the pip dependencies,
> even if no python targets are requested to be built.
> In a multi-language repo, this may cause developers to fetch dependencies they don't need,
> so consider using the long form for dependencies if this happens.

In addition to the `requirement` macro, which is used to access the `py_library`
target generated from a package's wheel, the generated `requirements.bzl` file contains
functionality for exposing [entry points][whl_ep] as `py_binary` targets.

[whl_ep]: https://packaging.python.org/specifications/entry-points/

```python
load("@pip_deps//:requirements.bzl", "entry_point")

alias(
    name = "pip-compile",
    actual = entry_point(
        pkg = "pip-tools",
        script = "pip-compile",
    ),
)
```

Note that for packages whose name and script are the same, only the name of the package
is needed when calling the `entry_point` macro.

```python
load("@pip_deps//:requirements.bzl", "entry_point")

alias(
    name = "flake8",
    actual = entry_point("flake8"),
)
```


**PARAMETERS**


| Name  | Description | Default Value |
| :-------------: | :-------------: | :-------------: |
| requirements |  A 'requirements.txt' pip requirements file.   |  none |
| name |  A unique name for the created external repository (default 'pip').   |  <code>"pip"</code> |
| kwargs |  Keyword arguments passed directly to the <code>pip_repository</code> repository rule.   |  none |


<a name="#pip_parse"></a>

## pip_parse

<pre>
pip_parse(<a href="#pip_parse-requirements_lock">requirements_lock</a>, <a href="#pip_parse-name">name</a>, <a href="#pip_parse-kwargs">kwargs</a>)
</pre>

Accepts a locked/compiled requirements file and installs the dependencies listed within.

Those dependencies become available in a generated `requirements.bzl` file.

This macro runs a repository rule that invokes `pip`. In your WORKSPACE file:

```python
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pip_deps",
    requirements_lock = ":requirements.txt",
)

load("@pip_deps//:requirements.bzl", "install_deps")

install_deps()
```

You can then reference installed dependencies from a `BUILD` file with:

```python
load("@pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "bar",
    ...
    deps = [
       "//my/other:dep",
       requirement("requests"),
       requirement("numpy"),
    ],
)
```

In addition to the `requirement` macro, which is used to access the generated `py_library`
target generated from a package's wheel, The generated `requirements.bzl` file contains
functionality for exposing [entry points][whl_ep] as `py_binary` targets as well.

[whl_ep]: https://packaging.python.org/specifications/entry-points/

```python
load("@pip_deps//:requirements.bzl", "entry_point")

alias(
    name = "pip-compile",
    actual = entry_point(
        pkg = "pip-tools",
        script = "pip-compile",
    ),
)
```

Note that for packages whose name and script are the same, only the name of the package
is needed when calling the `entry_point` macro.

```python
load("@pip_deps//:requirements.bzl", "entry_point")

alias(
    name = "flake8",
    actual = entry_point("flake8"),
)
```


**PARAMETERS**


| Name  | Description | Default Value |
| :-------------: | :-------------: | :-------------: |
| requirements_lock |  A fully resolved 'requirements.txt' pip requirement file     containing the transitive set of your dependencies. If this file is passed instead     of 'requirements' no resolve will take place and pip_repository will create     individual repositories for each of your dependencies so that wheels are     fetched/built only for the targets specified by 'build/run/test'.   |  none |
| name |  The name of the generated repository. The generated repositories     containing each requirement will be of the form &lt;name&gt;_&lt;requirement-name&gt;.   |  <code>"pip_parsed_deps"</code> |
| kwargs |  Additional keyword arguments for the underlying     <code>pip_repository</code> rule.   |  none |


<a name="#pip_repositories"></a>

## pip_repositories

<pre>
pip_repositories()
</pre>

    Obsolete macro to pull in dependencies needed to use the pip_import rule.

**PARAMETERS**



