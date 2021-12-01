import os
import sys

print(f"Python {sys.version}")

for sys_path in sys.path:
    if not os.path.isdir(sys_path):
        continue

    for item_name in os.listdir(sys_path):
        item_path = os.path.join(sys_path, item_name)
        if item_name == "google" and os.path.isdir(item_path):
            print("################################################################################")
            print(sys_path)
            if os.path.isfile(os.path.join(item_path, "__init__.py")):
                print(f"{item_name}/__init__.py")
                with open(os.path.join(item_path, "__init__.py")) as f:
                    print()
                    print(f.read())
            else:
                print(f"{item_name}/ (NO __init__.py)")
            for sub_item in os.listdir(item_path):
                sub_path = os.path.join(item_path, sub_item)
                if os.path.isdir(sub_path):
                    if os.path.isfile(os.path.join(sub_path, "__init__.py")):
                        print(f"{item_name}/{sub_item}/__init__.py")
                        with open(os.path.join(sub_path, "__init__.py")) as f:
                            print()
                            print(f.read())
                    else:
                        print(f"{item_name}/{sub_item}/ (NO__init__.py)")
            print()

from concurrent.futures import ThreadPoolExecutor
import grpc
import grpc_reflection.v1alpha.reflection

from hello_world.hello_world_servicer import HelloWorldServicer, hello_world_pb2, hello_world_pb2_grpc


def server_main() -> None:
    max_workers = 10
    use_reflection = True
    insecure_ports = ["[::]:50051"]

    server = grpc.server(ThreadPoolExecutor(max_workers=max_workers))
    service_names = []

    # hello_world
    servicer = HelloWorldServicer(template="Hello, {{name}}!")
    hello_world_pb2_grpc.add_HelloWorldServiceServicer_to_server(servicer, server)
    full_name = hello_world_pb2.DESCRIPTOR.services_by_name["HelloWorldService"].full_name
    service_names.append(full_name)

    if use_reflection:
        service_names.append(grpc_reflection.v1alpha.reflection.SERVICE_NAME)
        grpc_reflection.v1alpha.reflection.enable_server_reflection(
            service_names, server)

    for insecure_port in insecure_ports:
        server.add_insecure_port(insecure_port)

    print()
    print()
    print("Starting server on port 50051!")

    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    server_main()
