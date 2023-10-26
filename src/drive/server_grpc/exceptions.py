from .utils import MessageLike


class DefaultProtoMessageException(Exception):
    def __init__(self, proto_message: MessageLike):
        self.proto_message = proto_message
