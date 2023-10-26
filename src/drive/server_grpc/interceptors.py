import grpc
from grpc import ServicerContext, StatusCode

from drive.bot import models


class TokenAuthenticatorInterceptor(grpc.ServerInterceptor):
    @staticmethod
    def _get_token(token: str) -> models.APIToken | None:
        token_records = models.APIToken.objects.filter(key=token)
        return token_records.first()

    def intercept_service(self, continuation, handler_call_details):
        metadata = dict(handler_call_details.invocation_metadata)
        token = self._get_token(metadata.get("authorization"))
        if token and not token.user.is_blocked:
            original_handler = continuation(handler_call_details)

            def new_handler(request, context):
                context.main_language = token.user.main_language
                return original_handler.unary_unary(request, context)

            return grpc.unary_unary_rpc_method_handler(
                new_handler,
                request_deserializer=original_handler.request_deserializer,
                response_serializer=original_handler.response_serializer,
            )
        return grpc.unary_unary_rpc_method_handler(
            lambda req, context: grpc.RpcError("Invalid token!")
        )
