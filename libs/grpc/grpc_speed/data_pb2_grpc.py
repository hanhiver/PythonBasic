# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import data_pb2 as data__pb2


class DnetPredictStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.dnet_detect = channel.unary_unary(
        '/ImagePredict.DnetPredict/dnet_detect',
        request_serializer=data__pb2.Data.SerializeToString,
        response_deserializer=data__pb2.Data.FromString,
        )


class DnetPredictServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def dnet_detect(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DnetPredictServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'dnet_detect': grpc.unary_unary_rpc_method_handler(
          servicer.dnet_detect,
          request_deserializer=data__pb2.Data.FromString,
          response_serializer=data__pb2.Data.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ImagePredict.DnetPredict', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))