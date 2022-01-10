load("@pip_deps//:requirements.bzl", "entry_point")

alias(
    name = "hjson",
    actual = entry_point(
      "hjson",
    ),
)

alias(
    name = "hjson_pkg_script",
    actual = entry_point(
      pkg = "hjson",
      script = "hjson",
    ),
)

alias(
    name = "hjson_pkg_script_in_bin",
    actual = entry_point(
      pkg = "hjson",
      script = "bin/hjson",
    ),
)
