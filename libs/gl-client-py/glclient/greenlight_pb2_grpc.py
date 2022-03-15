# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import greenlight_pb2 as greenlight__pb2


class NodeStub(object):
    """The node service represents your node running on greenlight's
    infrastructure. You can use the exposed RPC methods to interact
    with your node. The URI used to connect to the node depends on
    where the node is being scheduled and is returned by the
    `Scheduler.Schedule()` RPC call.

    Notice that in order to connect to the node the caller must use the
    node-specific mTLS keypair returned by `Scheduler.Register()` or
    `Scheduler.Recover()`. In particular the anonymous mTLS keypair is
    rejected by the node.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetInfo = channel.unary_unary(
                '/greenlight.Node/GetInfo',
                request_serializer=greenlight__pb2.GetInfoRequest.SerializeToString,
                response_deserializer=greenlight__pb2.GetInfoResponse.FromString,
                )
        self.Stop = channel.unary_unary(
                '/greenlight.Node/Stop',
                request_serializer=greenlight__pb2.StopRequest.SerializeToString,
                response_deserializer=greenlight__pb2.StopResponse.FromString,
                )
        self.ConnectPeer = channel.unary_unary(
                '/greenlight.Node/ConnectPeer',
                request_serializer=greenlight__pb2.ConnectRequest.SerializeToString,
                response_deserializer=greenlight__pb2.ConnectResponse.FromString,
                )
        self.ListPeers = channel.unary_unary(
                '/greenlight.Node/ListPeers',
                request_serializer=greenlight__pb2.ListPeersRequest.SerializeToString,
                response_deserializer=greenlight__pb2.ListPeersResponse.FromString,
                )
        self.Disconnect = channel.unary_unary(
                '/greenlight.Node/Disconnect',
                request_serializer=greenlight__pb2.DisconnectRequest.SerializeToString,
                response_deserializer=greenlight__pb2.DisconnectResponse.FromString,
                )
        self.NewAddr = channel.unary_unary(
                '/greenlight.Node/NewAddr',
                request_serializer=greenlight__pb2.NewAddrRequest.SerializeToString,
                response_deserializer=greenlight__pb2.NewAddrResponse.FromString,
                )
        self.ListFunds = channel.unary_unary(
                '/greenlight.Node/ListFunds',
                request_serializer=greenlight__pb2.ListFundsRequest.SerializeToString,
                response_deserializer=greenlight__pb2.ListFundsResponse.FromString,
                )
        self.Withdraw = channel.unary_unary(
                '/greenlight.Node/Withdraw',
                request_serializer=greenlight__pb2.WithdrawRequest.SerializeToString,
                response_deserializer=greenlight__pb2.WithdrawResponse.FromString,
                )
        self.FundChannel = channel.unary_unary(
                '/greenlight.Node/FundChannel',
                request_serializer=greenlight__pb2.FundChannelRequest.SerializeToString,
                response_deserializer=greenlight__pb2.FundChannelResponse.FromString,
                )
        self.CloseChannel = channel.unary_unary(
                '/greenlight.Node/CloseChannel',
                request_serializer=greenlight__pb2.CloseChannelRequest.SerializeToString,
                response_deserializer=greenlight__pb2.CloseChannelResponse.FromString,
                )
        self.CreateInvoice = channel.unary_unary(
                '/greenlight.Node/CreateInvoice',
                request_serializer=greenlight__pb2.InvoiceRequest.SerializeToString,
                response_deserializer=greenlight__pb2.Invoice.FromString,
                )
        self.Pay = channel.unary_unary(
                '/greenlight.Node/Pay',
                request_serializer=greenlight__pb2.PayRequest.SerializeToString,
                response_deserializer=greenlight__pb2.Payment.FromString,
                )
        self.Keysend = channel.unary_unary(
                '/greenlight.Node/Keysend',
                request_serializer=greenlight__pb2.KeysendRequest.SerializeToString,
                response_deserializer=greenlight__pb2.Payment.FromString,
                )
        self.ListPayments = channel.unary_unary(
                '/greenlight.Node/ListPayments',
                request_serializer=greenlight__pb2.ListPaymentsRequest.SerializeToString,
                response_deserializer=greenlight__pb2.ListPaymentsResponse.FromString,
                )
        self.ListInvoices = channel.unary_unary(
                '/greenlight.Node/ListInvoices',
                request_serializer=greenlight__pb2.ListInvoicesRequest.SerializeToString,
                response_deserializer=greenlight__pb2.ListInvoicesResponse.FromString,
                )
        self.StreamIncoming = channel.unary_stream(
                '/greenlight.Node/StreamIncoming',
                request_serializer=greenlight__pb2.StreamIncomingFilter.SerializeToString,
                response_deserializer=greenlight__pb2.IncomingPayment.FromString,
                )
        self.StreamLog = channel.unary_stream(
                '/greenlight.Node/StreamLog',
                request_serializer=greenlight__pb2.StreamLogRequest.SerializeToString,
                response_deserializer=greenlight__pb2.LogEntry.FromString,
                )
        self.StreamHsmRequests = channel.unary_stream(
                '/greenlight.Node/StreamHsmRequests',
                request_serializer=greenlight__pb2.Empty.SerializeToString,
                response_deserializer=greenlight__pb2.HsmRequest.FromString,
                )
        self.RespondHsmRequest = channel.unary_unary(
                '/greenlight.Node/RespondHsmRequest',
                request_serializer=greenlight__pb2.HsmResponse.SerializeToString,
                response_deserializer=greenlight__pb2.Empty.FromString,
                )


class NodeServicer(object):
    """The node service represents your node running on greenlight's
    infrastructure. You can use the exposed RPC methods to interact
    with your node. The URI used to connect to the node depends on
    where the node is being scheduled and is returned by the
    `Scheduler.Schedule()` RPC call.

    Notice that in order to connect to the node the caller must use the
    node-specific mTLS keypair returned by `Scheduler.Register()` or
    `Scheduler.Recover()`. In particular the anonymous mTLS keypair is
    rejected by the node.

    """

    def GetInfo(self, request, context):
        """Retrieve general information about the node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
        """The stop is a RPC command to shut off the c-lightning node
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConnectPeer(self, request, context):
        """Connect to a node in the network. (`Connect` alone clashes
        with tonic internals).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPeers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disconnect(self, request, context):
        """The disconnect RPC command closes an existing connection to
        a peer, identified by node_id, in the Lightning Network, as long
        as it doesn't have an active channel. If force is set then
        it will disconnect even with an active channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NewAddr(self, request, context):
        """The newaddr RPC command generates a new address which can
        subsequently be used to fund channels managed by the
        c-lightning node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFunds(self, request, context):
        """Retrieve a list of funds managed by this node.

        This includes both on-chain funds and off-chain
        funds. Off-chain funds are bound to a channel, and we
        consider only the balance that is currently spendable by
        the node, i.e., we do not return the full channel's
        capacity, just the balance that belongs to this node.

        The on-chain funds correspond to outputs that the wallet
        can spend.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FundChannel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseChannel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateInvoice(self, request, context):
        """Create a new invoice to receive an incoming payment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pay(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Keysend(self, request, context):
        """Send a spontaneous payment, optionally with some extra information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPayments(self, request, context):
        """Retrieve a list of payment performed by this node.

        The query can optionally be restricted to a single payment
        matching criteria that can be specified in the
        `ListPaymentsRequest`

        Notice: this does not include any payment that were
        received by this node, just the outgoing payments. Incoming
        payments can be retrieved using `ListInvoices`
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListInvoices(self, request, context):
        """Retrieve invoices that were created via CreateInvoice

        The query can optionally be restricted to only return a
        single invoice matching the given criteria.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamIncoming(self, request, context):
        """Stream incoming payments

        Currently includes off-chain payments received matching an
        invoice or spontaneus paymens through keysend.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamLog(self, request, context):
        """Stream the logs as they are produced by the node

        Mainly intended for debugging clients by tailing the log as
        they are written on the node. The logs start streaming from
        the first beginning, in order to allow inspection of events
        after an error occurred, That also means that the logs can
        be rather large, and should not be streamed onto
        resource-constrained devices.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamHsmRequests(self, request, context):
        """////////////////////////////// HSM Messages ////////////////////////

        The following messages are related to communicating HSM
        requests back and forth. Chances are you won't need to
        interact with these at all, unless you want to embed the
        hsmd into your client. We recommend using a standalone hsmd
        such as hagrid, keeper of keys, to get started.

        Stream requests from the node to any key device that can
        respond to them.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RespondHsmRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInfo,
                    request_deserializer=greenlight__pb2.GetInfoRequest.FromString,
                    response_serializer=greenlight__pb2.GetInfoResponse.SerializeToString,
            ),
            'Stop': grpc.unary_unary_rpc_method_handler(
                    servicer.Stop,
                    request_deserializer=greenlight__pb2.StopRequest.FromString,
                    response_serializer=greenlight__pb2.StopResponse.SerializeToString,
            ),
            'ConnectPeer': grpc.unary_unary_rpc_method_handler(
                    servicer.ConnectPeer,
                    request_deserializer=greenlight__pb2.ConnectRequest.FromString,
                    response_serializer=greenlight__pb2.ConnectResponse.SerializeToString,
            ),
            'ListPeers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPeers,
                    request_deserializer=greenlight__pb2.ListPeersRequest.FromString,
                    response_serializer=greenlight__pb2.ListPeersResponse.SerializeToString,
            ),
            'Disconnect': grpc.unary_unary_rpc_method_handler(
                    servicer.Disconnect,
                    request_deserializer=greenlight__pb2.DisconnectRequest.FromString,
                    response_serializer=greenlight__pb2.DisconnectResponse.SerializeToString,
            ),
            'NewAddr': grpc.unary_unary_rpc_method_handler(
                    servicer.NewAddr,
                    request_deserializer=greenlight__pb2.NewAddrRequest.FromString,
                    response_serializer=greenlight__pb2.NewAddrResponse.SerializeToString,
            ),
            'ListFunds': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFunds,
                    request_deserializer=greenlight__pb2.ListFundsRequest.FromString,
                    response_serializer=greenlight__pb2.ListFundsResponse.SerializeToString,
            ),
            'Withdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.Withdraw,
                    request_deserializer=greenlight__pb2.WithdrawRequest.FromString,
                    response_serializer=greenlight__pb2.WithdrawResponse.SerializeToString,
            ),
            'FundChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.FundChannel,
                    request_deserializer=greenlight__pb2.FundChannelRequest.FromString,
                    response_serializer=greenlight__pb2.FundChannelResponse.SerializeToString,
            ),
            'CloseChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseChannel,
                    request_deserializer=greenlight__pb2.CloseChannelRequest.FromString,
                    response_serializer=greenlight__pb2.CloseChannelResponse.SerializeToString,
            ),
            'CreateInvoice': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateInvoice,
                    request_deserializer=greenlight__pb2.InvoiceRequest.FromString,
                    response_serializer=greenlight__pb2.Invoice.SerializeToString,
            ),
            'Pay': grpc.unary_unary_rpc_method_handler(
                    servicer.Pay,
                    request_deserializer=greenlight__pb2.PayRequest.FromString,
                    response_serializer=greenlight__pb2.Payment.SerializeToString,
            ),
            'Keysend': grpc.unary_unary_rpc_method_handler(
                    servicer.Keysend,
                    request_deserializer=greenlight__pb2.KeysendRequest.FromString,
                    response_serializer=greenlight__pb2.Payment.SerializeToString,
            ),
            'ListPayments': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPayments,
                    request_deserializer=greenlight__pb2.ListPaymentsRequest.FromString,
                    response_serializer=greenlight__pb2.ListPaymentsResponse.SerializeToString,
            ),
            'ListInvoices': grpc.unary_unary_rpc_method_handler(
                    servicer.ListInvoices,
                    request_deserializer=greenlight__pb2.ListInvoicesRequest.FromString,
                    response_serializer=greenlight__pb2.ListInvoicesResponse.SerializeToString,
            ),
            'StreamIncoming': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamIncoming,
                    request_deserializer=greenlight__pb2.StreamIncomingFilter.FromString,
                    response_serializer=greenlight__pb2.IncomingPayment.SerializeToString,
            ),
            'StreamLog': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamLog,
                    request_deserializer=greenlight__pb2.StreamLogRequest.FromString,
                    response_serializer=greenlight__pb2.LogEntry.SerializeToString,
            ),
            'StreamHsmRequests': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamHsmRequests,
                    request_deserializer=greenlight__pb2.Empty.FromString,
                    response_serializer=greenlight__pb2.HsmRequest.SerializeToString,
            ),
            'RespondHsmRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.RespondHsmRequest,
                    request_deserializer=greenlight__pb2.HsmResponse.FromString,
                    response_serializer=greenlight__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'greenlight.Node', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Node(object):
    """The node service represents your node running on greenlight's
    infrastructure. You can use the exposed RPC methods to interact
    with your node. The URI used to connect to the node depends on
    where the node is being scheduled and is returned by the
    `Scheduler.Schedule()` RPC call.

    Notice that in order to connect to the node the caller must use the
    node-specific mTLS keypair returned by `Scheduler.Register()` or
    `Scheduler.Recover()`. In particular the anonymous mTLS keypair is
    rejected by the node.

    """

    @staticmethod
    def GetInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/GetInfo',
            greenlight__pb2.GetInfoRequest.SerializeToString,
            greenlight__pb2.GetInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/Stop',
            greenlight__pb2.StopRequest.SerializeToString,
            greenlight__pb2.StopResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConnectPeer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/ConnectPeer',
            greenlight__pb2.ConnectRequest.SerializeToString,
            greenlight__pb2.ConnectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPeers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/ListPeers',
            greenlight__pb2.ListPeersRequest.SerializeToString,
            greenlight__pb2.ListPeersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disconnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/Disconnect',
            greenlight__pb2.DisconnectRequest.SerializeToString,
            greenlight__pb2.DisconnectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NewAddr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/NewAddr',
            greenlight__pb2.NewAddrRequest.SerializeToString,
            greenlight__pb2.NewAddrResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListFunds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/ListFunds',
            greenlight__pb2.ListFundsRequest.SerializeToString,
            greenlight__pb2.ListFundsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Withdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/Withdraw',
            greenlight__pb2.WithdrawRequest.SerializeToString,
            greenlight__pb2.WithdrawResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FundChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/FundChannel',
            greenlight__pb2.FundChannelRequest.SerializeToString,
            greenlight__pb2.FundChannelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/CloseChannel',
            greenlight__pb2.CloseChannelRequest.SerializeToString,
            greenlight__pb2.CloseChannelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateInvoice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/CreateInvoice',
            greenlight__pb2.InvoiceRequest.SerializeToString,
            greenlight__pb2.Invoice.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Pay(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/Pay',
            greenlight__pb2.PayRequest.SerializeToString,
            greenlight__pb2.Payment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Keysend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/Keysend',
            greenlight__pb2.KeysendRequest.SerializeToString,
            greenlight__pb2.Payment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPayments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/ListPayments',
            greenlight__pb2.ListPaymentsRequest.SerializeToString,
            greenlight__pb2.ListPaymentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListInvoices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/ListInvoices',
            greenlight__pb2.ListInvoicesRequest.SerializeToString,
            greenlight__pb2.ListInvoicesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamIncoming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/greenlight.Node/StreamIncoming',
            greenlight__pb2.StreamIncomingFilter.SerializeToString,
            greenlight__pb2.IncomingPayment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/greenlight.Node/StreamLog',
            greenlight__pb2.StreamLogRequest.SerializeToString,
            greenlight__pb2.LogEntry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamHsmRequests(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/greenlight.Node/StreamHsmRequests',
            greenlight__pb2.Empty.SerializeToString,
            greenlight__pb2.HsmRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RespondHsmRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Node/RespondHsmRequest',
            greenlight__pb2.HsmResponse.SerializeToString,
            greenlight__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class HsmStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Request = channel.unary_unary(
                '/greenlight.Hsm/Request',
                request_serializer=greenlight__pb2.HsmRequest.SerializeToString,
                response_deserializer=greenlight__pb2.HsmResponse.FromString,
                )
        self.Ping = channel.unary_unary(
                '/greenlight.Hsm/Ping',
                request_serializer=greenlight__pb2.Empty.SerializeToString,
                response_deserializer=greenlight__pb2.Empty.FromString,
                )


class HsmServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Request(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HsmServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Request': grpc.unary_unary_rpc_method_handler(
                    servicer.Request,
                    request_deserializer=greenlight__pb2.HsmRequest.FromString,
                    response_serializer=greenlight__pb2.HsmResponse.SerializeToString,
            ),
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=greenlight__pb2.Empty.FromString,
                    response_serializer=greenlight__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'greenlight.Hsm', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Hsm(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Request(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Hsm/Request',
            greenlight__pb2.HsmRequest.SerializeToString,
            greenlight__pb2.HsmResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greenlight.Hsm/Ping',
            greenlight__pb2.Empty.SerializeToString,
            greenlight__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
