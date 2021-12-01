load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@io_bazel_rules_docker//docker/util:run.bzl", "container_run_and_commit")
load("@pip_deps//:requirements.bzl", "requirement")
load("@rules_proto//proto:defs.bzl", "proto_library")
load("@rules_proto_grpc//python:defs.bzl", "python_grpc_library")
load("@rules_python//python:defs.bzl", "py_binary", "py_library")

proto_library(
    name = "hello_world_proto",
    srcs = ["hello_world.proto"],
    deps = [
        "@com_google_googleapis//google/api:annotations_proto",
    ],
)

python_grpc_library(
    name = "hello_world_py_proto",
    protos = [":hello_world_proto"],
    deps = [
        "@com_google_googleapis//google/api:annotations_py_proto",
        "@com_google_googleapis//google/api:http_py_proto",
    ],
)

py_library(
    name = "hello_world_py",
    srcs = [
        "hello_world_servicer.py",
    ],
    deps = [
        ":hello_world_py_proto",
        requirement("chevron"),
    ],
)

py_binary(
    name = "hello_world_server_py",
    srcs = ["hello_world_server.py"],
    legacy_create_init = False,
    main = "hello_world_server.py",
    deps = [
        ":hello_world_py",
        requirement("grpcio"),
        requirement("grpcio-reflection"),
    ],
)

container_run_and_commit(
    name = "hello_world_server_py_base",
    commands = [
        "apt-get update",
        "DEBIAN_FRONTEND=noninteractive && apt-get -y install --no-install-recommends python3",
        "ln -sf /usr/bin/python3 /usr/bin/python",
    ],
    image = "@ubuntu_focal//image",
)

py3_image(
    name = "hello_world_server_py_image",
    srcs = ["hello_world_server.py"],
    base = ":hello_world_server_py_base",
    layers = [
        ":hello_world_py",
        requirement("grpcio"),
        requirement("grpcio-reflection"),
    ],
    legacy_create_init = False,
    main = "hello_world_server.py",
)
