# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import game_pb2 as game__pb2


class GameServiceStub(object):
    """The game service definition now includes methods for joining and receiving updates
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.JoinGame = channel.unary_unary(
                '/game.GameService/JoinGame',
                request_serializer=game__pb2.JoinGameRequest.SerializeToString,
                response_deserializer=game__pb2.JoinGameResponse.FromString,
                )
        self.UpdatePosition = channel.unary_unary(
                '/game.GameService/UpdatePosition',
                request_serializer=game__pb2.Position.SerializeToString,
                response_deserializer=game__pb2.Position.FromString,
                )
        self.GetPositions = channel.stream_stream(
                '/game.GameService/GetPositions',
                request_serializer=game__pb2.Position.SerializeToString,
                response_deserializer=game__pb2.Position.FromString,
                )


class GameServiceServicer(object):
    """The game service definition now includes methods for joining and receiving updates
    """

    def JoinGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPositions(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GameServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'JoinGame': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinGame,
                    request_deserializer=game__pb2.JoinGameRequest.FromString,
                    response_serializer=game__pb2.JoinGameResponse.SerializeToString,
            ),
            'UpdatePosition': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePosition,
                    request_deserializer=game__pb2.Position.FromString,
                    response_serializer=game__pb2.Position.SerializeToString,
            ),
            'GetPositions': grpc.stream_stream_rpc_method_handler(
                    servicer.GetPositions,
                    request_deserializer=game__pb2.Position.FromString,
                    response_serializer=game__pb2.Position.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'game.GameService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GameService(object):
    """The game service definition now includes methods for joining and receiving updates
    """

    @staticmethod
    def JoinGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/game.GameService/JoinGame',
            game__pb2.JoinGameRequest.SerializeToString,
            game__pb2.JoinGameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/game.GameService/UpdatePosition',
            game__pb2.Position.SerializeToString,
            game__pb2.Position.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPositions(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/game.GameService/GetPositions',
            game__pb2.Position.SerializeToString,
            game__pb2.Position.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
