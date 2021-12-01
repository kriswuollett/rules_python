import chevron

from hello_world import hello_world_pb2, hello_world_pb2_grpc


class HelloWorldServicer(hello_world_pb2_grpc.HelloWorldServiceServicer):
    template: str

    def __init__(self, template: str) -> None:
        super().__init__()
        self.template = template

    def GetGreeting(self, request: hello_world_pb2.HelloWorldRequest, context):
        response = hello_world_pb2.HelloWorldResponse()
        response.greeting = chevron.render(self.template, {
            "name": request.name
        })
        return response
