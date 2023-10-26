from concurrent import futures

import grpc
from django.conf import settings
from drive_bot_proto.client_pb2 import DESCRIPTOR
from drive_bot_proto.client_pb2_grpc import add_DriveBotServiceServicer_to_server
from grpc_reflection.v1alpha import reflection
from loguru import logger

from drive.server_grpc.interceptors import TokenAuthenticatorInterceptor
from drive.server_grpc.servicer import DriveBotServiceGRPC


def serve() -> None:
    interceptors = [TokenAuthenticatorInterceptor()]
    thread_pool = futures.ThreadPoolExecutor(max_workers=settings.GRPC_CONCURRENCY)
    server = grpc.server(thread_pool=thread_pool, interceptors=interceptors)

    add_DriveBotServiceServicer_to_server(
        DriveBotServiceGRPC(),
        server,
    )
    service_names = [
        DESCRIPTOR.services_by_name["DriveBotService"].full_name,
        reflection.SERVICE_NAME,
    ]
    reflection.enable_server_reflection(service_names, server)

    listen_addr = f"[::]:{settings.GRPC_SERVICE_PORT}"
    server.add_insecure_port(listen_addr)

    server.start()

    logger.info(f"GRPC server successfully started at {settings.GRPC_SERVICE_PORT}")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()
