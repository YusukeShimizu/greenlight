# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greenlight.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10greenlight.proto\x12\ngreenlight\"H\n\x11HsmRequestContext\x12\x0f\n\x07node_id\x18\x01 \x01(\x0c\x12\x0c\n\x04\x64\x62id\x18\x02 \x01(\x04\x12\x14\n\x0c\x63\x61pabilities\x18\x03 \x01(\x04\".\n\x0bHsmResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\r\x12\x0b\n\x03raw\x18\x02 \x01(\x0c\"]\n\nHsmRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\r\x12.\n\x07\x63ontext\x18\x02 \x01(\x0b\x32\x1d.greenlight.HsmRequestContext\x12\x0b\n\x03raw\x18\x03 \x01(\x0c\"\x07\n\x05\x45mpty\"O\n\x07\x41\x64\x64ress\x12(\n\x04type\x18\x01 \x01(\x0e\x32\x1a.greenlight.NetAddressType\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\"\x10\n\x0eGetInfoRequest\"\xb2\x01\n\x0fGetInfoResponse\x12\x0f\n\x07node_id\x18\x01 \x01(\x0c\x12\r\n\x05\x61lias\x18\x02 \x01(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\x0c\x12\x11\n\tnum_peers\x18\x04 \x01(\r\x12&\n\taddresses\x18\x05 \x03(\x0b\x32\x13.greenlight.Address\x12\x0f\n\x07version\x18\x06 \x01(\t\x12\x13\n\x0b\x62lockheight\x18\x07 \x01(\r\x12\x0f\n\x07network\x18\x08 \x01(\t\"\r\n\x0bStopRequest\"\x0e\n\x0cStopResponse\"/\n\x0e\x43onnectRequest\x12\x0f\n\x07node_id\x18\x01 \x01(\t\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\t\"4\n\x0f\x43onnectResponse\x12\x0f\n\x07node_id\x18\x01 \x01(\t\x12\x10\n\x08\x66\x65\x61tures\x18\x02 \x01(\t\"#\n\x10ListPeersRequest\x12\x0f\n\x07node_id\x18\x01 \x01(\t\"\x81\x01\n\x04Htlc\x12\x11\n\tdirection\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0e\n\x06\x61mount\x18\x03 \x01(\t\x12\x0e\n\x06\x65xpiry\x18\x04 \x01(\x04\x12\x14\n\x0cpayment_hash\x18\x05 \x01(\t\x12\r\n\x05state\x18\x06 \x01(\t\x12\x15\n\rlocal_trimmed\x18\x07 \x01(\x08\"\xeb\x02\n\x07\x43hannel\x12\r\n\x05state\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12\x18\n\x10short_channel_id\x18\x03 \x01(\t\x12\x11\n\tdirection\x18\x04 \x01(\r\x12\x12\n\nchannel_id\x18\x05 \x01(\t\x12\x14\n\x0c\x66unding_txid\x18\x06 \x01(\t\x12\x15\n\rclose_to_addr\x18\x07 \x01(\t\x12\x10\n\x08\x63lose_to\x18\x08 \x01(\t\x12\x0f\n\x07private\x18\t \x01(\x08\x12\r\n\x05total\x18\n \x01(\t\x12\x12\n\ndust_limit\x18\x0b \x01(\t\x12\x11\n\tspendable\x18\x0c \x01(\t\x12\x12\n\nreceivable\x18\r \x01(\t\x12\x1b\n\x13their_to_self_delay\x18\x0e \x01(\r\x12\x19\n\x11our_to_self_delay\x18\x0f \x01(\r\x12\x0e\n\x06status\x18\x10 \x03(\t\x12\x1f\n\x05htlcs\x18\x11 \x03(\x0b\x32\x10.greenlight.Htlc\"\x86\x01\n\x04Peer\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x11\n\tconnected\x18\x02 \x01(\x08\x12&\n\taddresses\x18\x03 \x03(\x0b\x32\x13.greenlight.Address\x12\x10\n\x08\x66\x65\x61tures\x18\x04 \x01(\t\x12%\n\x08\x63hannels\x18\x05 \x03(\x0b\x32\x13.greenlight.Channel\"4\n\x11ListPeersResponse\x12\x1f\n\x05peers\x18\x01 \x03(\x0b\x32\x10.greenlight.Peer\"3\n\x11\x44isconnectRequest\x12\x0f\n\x07node_id\x18\x01 \x01(\t\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\"\x14\n\x12\x44isconnectResponse\"B\n\x0eNewAddrRequest\x12\x30\n\x0c\x61\x64\x64ress_type\x18\x01 \x01(\x0e\x32\x1a.greenlight.BtcAddressType\"T\n\x0fNewAddrResponse\x12\x30\n\x0c\x61\x64\x64ress_type\x18\x01 \x01(\x0e\x32\x1a.greenlight.BtcAddressType\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"=\n\x10ListFundsRequest\x12)\n\x07minconf\x18\x01 \x01(\x0b\x32\x18.greenlight.Confirmation\"\x96\x01\n\x0fListFundsOutput\x12$\n\x06output\x18\x01 \x01(\x0b\x32\x14.greenlight.Outpoint\x12\"\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x12.greenlight.Amount\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12(\n\x06status\x18\x05 \x01(\x0e\x32\x18.greenlight.OutputStatus\"\xac\x01\n\x10ListFundsChannel\x12\x0f\n\x07peer_id\x18\x01 \x01(\x0c\x12\x11\n\tconnected\x18\x02 \x01(\x08\x12\x18\n\x10short_channel_id\x18\x03 \x01(\x04\x12\x17\n\x0four_amount_msat\x18\x04 \x01(\x04\x12\x13\n\x0b\x61mount_msat\x18\x05 \x01(\x04\x12\x14\n\x0c\x66unding_txid\x18\x06 \x01(\x0c\x12\x16\n\x0e\x66unding_output\x18\x07 \x01(\r\"q\n\x11ListFundsResponse\x12,\n\x07outputs\x18\x01 \x03(\x0b\x32\x1b.greenlight.ListFundsOutput\x12.\n\x08\x63hannels\x18\x02 \x03(\x0b\x32\x1c.greenlight.ListFundsChannel\"a\n\x07\x46\x65\x65rate\x12+\n\x06preset\x18\x01 \x01(\x0e\x32\x19.greenlight.FeeratePresetH\x00\x12\x0f\n\x05perkw\x18\x05 \x01(\x04H\x00\x12\x0f\n\x05perkb\x18\x06 \x01(\x04H\x00\x42\x07\n\x05value\"\x1e\n\x0c\x43onfirmation\x12\x0e\n\x06\x62locks\x18\x01 \x01(\r\"\xc0\x01\n\x0fWithdrawRequest\x12\x13\n\x0b\x64\x65stination\x18\x01 \x01(\t\x12\"\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x12.greenlight.Amount\x12$\n\x07\x66\x65\x65rate\x18\x03 \x01(\x0b\x32\x13.greenlight.Feerate\x12)\n\x07minconf\x18\x07 \x01(\x0b\x32\x18.greenlight.Confirmation\x12#\n\x05utxos\x18\x08 \x03(\x0b\x32\x14.greenlight.Outpoint\",\n\x10WithdrawResponse\x12\n\n\x02tx\x18\x01 \x01(\x0c\x12\x0c\n\x04txid\x18\x02 \x01(\x0c\"\xbe\x01\n\x12\x46undChannelRequest\x12\x0f\n\x07node_id\x18\x01 \x01(\x0c\x12\"\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x12.greenlight.Amount\x12$\n\x07\x66\x65\x65rate\x18\x03 \x01(\x0b\x32\x13.greenlight.Feerate\x12\x10\n\x08\x61nnounce\x18\x07 \x01(\x08\x12)\n\x07minconf\x18\x08 \x01(\x0b\x32\x18.greenlight.Confirmation\x12\x10\n\x08\x63lose_to\x18\n \x01(\t\"(\n\x08Outpoint\x12\x0c\n\x04txid\x18\x01 \x01(\x0c\x12\x0e\n\x06outnum\x18\x02 \x01(\r\"o\n\x13\x46undChannelResponse\x12\n\n\x02tx\x18\x01 \x01(\x0c\x12&\n\x08outpoint\x18\x02 \x01(\x0b\x32\x14.greenlight.Outpoint\x12\x12\n\nchannel_id\x18\x03 \x01(\x0c\x12\x10\n\x08\x63lose_to\x18\x04 \x01(\t\"\x1a\n\x07Timeout\x12\x0f\n\x07seconds\x18\x01 \x01(\r\"!\n\x0e\x42itcoinAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"\x87\x01\n\x13\x43loseChannelRequest\x12\x0f\n\x07node_id\x18\x01 \x01(\x0c\x12.\n\x11unilateraltimeout\x18\x02 \x01(\x0b\x32\x13.greenlight.Timeout\x12/\n\x0b\x64\x65stination\x18\x03 \x01(\x0b\x32\x1a.greenlight.BitcoinAddress\"b\n\x14\x43loseChannelResponse\x12\x30\n\nclose_type\x18\x01 \x01(\x0e\x32\x1c.greenlight.CloseChannelType\x12\n\n\x02tx\x18\x02 \x01(\x0c\x12\x0c\n\x04txid\x18\x03 \x01(\x0c\"l\n\x06\x41mount\x12\x16\n\x0cmillisatoshi\x18\x01 \x01(\x04H\x00\x12\x11\n\x07satoshi\x18\x02 \x01(\x04H\x00\x12\x11\n\x07\x62itcoin\x18\x03 \x01(\x04H\x00\x12\r\n\x03\x61ll\x18\x04 \x01(\x08H\x00\x12\r\n\x03\x61ny\x18\x05 \x01(\x08H\x00\x42\x06\n\x04unit\"X\n\x0eInvoiceRequest\x12\"\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x12.greenlight.Amount\x12\r\n\x05label\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"\x8d\x02\n\x07Invoice\x12\r\n\x05label\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\"\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x12.greenlight.Amount\x12$\n\x08received\x18\x04 \x01(\x0b\x32\x12.greenlight.Amount\x12)\n\x06status\x18\x05 \x01(\x0e\x32\x19.greenlight.InvoiceStatus\x12\x14\n\x0cpayment_time\x18\x06 \x01(\r\x12\x13\n\x0b\x65xpiry_time\x18\x07 \x01(\r\x12\x0e\n\x06\x62olt11\x18\x08 \x01(\t\x12\x14\n\x0cpayment_hash\x18\t \x01(\x0c\x12\x18\n\x10payment_preimage\x18\n \x01(\x0c\"Q\n\nPayRequest\x12\x0e\n\x06\x62olt11\x18\x01 \x01(\t\x12\"\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x12.greenlight.Amount\x12\x0f\n\x07timeout\x18\x03 \x01(\r\"\xe6\x01\n\x07Payment\x12\x13\n\x0b\x64\x65stination\x18\x01 \x01(\x0c\x12\x14\n\x0cpayment_hash\x18\x02 \x01(\x0c\x12\x18\n\x10payment_preimage\x18\x03 \x01(\x0c\x12%\n\x06status\x18\x04 \x01(\x0e\x32\x15.greenlight.PayStatus\x12\"\n\x06\x61mount\x18\x05 \x01(\x0b\x32\x12.greenlight.Amount\x12\'\n\x0b\x61mount_sent\x18\x06 \x01(\x0b\x32\x12.greenlight.Amount\x12\x0e\n\x06\x62olt11\x18\x07 \x01(\t\x12\x12\n\ncreated_at\x18\x08 \x01(\x01\"C\n\x11PaymentIdentifier\x12\x10\n\x06\x62olt11\x18\x01 \x01(\tH\x00\x12\x16\n\x0cpayment_hash\x18\x02 \x01(\x0cH\x00\x42\x04\n\x02id\"H\n\x13ListPaymentsRequest\x12\x31\n\nidentifier\x18\x01 \x01(\x0b\x32\x1d.greenlight.PaymentIdentifier\"=\n\x14ListPaymentsResponse\x12%\n\x08payments\x18\x01 \x03(\x0b\x32\x13.greenlight.Payment\"W\n\x11InvoiceIdentifier\x12\x0f\n\x05label\x18\x01 \x01(\tH\x00\x12\x13\n\tinvstring\x18\x02 \x01(\tH\x00\x12\x16\n\x0cpayment_hash\x18\x03 \x01(\x0cH\x00\x42\x04\n\x02id\"H\n\x13ListInvoicesRequest\x12\x31\n\nidentifier\x18\x01 \x01(\x0b\x32\x1d.greenlight.InvoiceIdentifier\"\x16\n\x14StreamIncomingFilter\"=\n\x14ListInvoicesResponse\x12%\n\x08invoices\x18\x01 \x03(\x0b\x32\x13.greenlight.Invoice\"\'\n\x08TlvField\x12\x0c\n\x04type\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x0c\"\xa5\x01\n\x0fOffChainPayment\x12\r\n\x05label\x18\x01 \x01(\t\x12\x10\n\x08preimage\x18\x02 \x01(\x0c\x12\"\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x12.greenlight.Amount\x12\'\n\textratlvs\x18\x04 \x03(\x0b\x32\x14.greenlight.TlvField\x12\x14\n\x0cpayment_hash\x18\x05 \x01(\x0c\x12\x0e\n\x06\x62olt11\x18\x06 \x01(\t\"M\n\x0fIncomingPayment\x12/\n\x08offchain\x18\x01 \x01(\x0b\x32\x1b.greenlight.OffChainPaymentH\x00\x42\t\n\x07\x64\x65tails\"x\n\x0cRoutehintHop\x12\x0f\n\x07node_id\x18\x01 \x01(\x0c\x12\x18\n\x10short_channel_id\x18\x02 \x01(\t\x12\x10\n\x08\x66\x65\x65_base\x18\x03 \x01(\x04\x12\x10\n\x08\x66\x65\x65_prop\x18\x04 \x01(\r\x12\x19\n\x11\x63ltv_expiry_delta\x18\x05 \x01(\r\"3\n\tRoutehint\x12&\n\x04hops\x18\x01 \x03(\x0b\x32\x18.greenlight.RoutehintHop\"\xa8\x01\n\x0eKeysendRequest\x12\x0f\n\x07node_id\x18\x01 \x01(\x0c\x12\"\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x12.greenlight.Amount\x12\r\n\x05label\x18\x03 \x01(\t\x12)\n\nroutehints\x18\x04 \x03(\x0b\x32\x15.greenlight.Routehint\x12\'\n\textratlvs\x18\x05 \x03(\x0b\x32\x14.greenlight.TlvField\"\x12\n\x10StreamLogRequest\"\x18\n\x08LogEntry\x12\x0c\n\x04line\x18\x01 \x01(\t*:\n\x0eNetAddressType\x12\x08\n\x04Ipv4\x10\x00\x12\x08\n\x04Ipv6\x10\x01\x12\t\n\x05TorV2\x10\x02\x12\t\n\x05TorV3\x10\x03*-\n\x0e\x42tcAddressType\x12\n\n\x06\x42\x45\x43H32\x10\x00\x12\x0f\n\x0bP2SH_SEGWIT\x10\x01*.\n\x0cOutputStatus\x12\r\n\tCONFIRMED\x10\x00\x12\x0f\n\x0bUNCONFIRMED\x10\x01*1\n\rFeeratePreset\x12\n\n\x06NORMAL\x10\x00\x12\x08\n\x04SLOW\x10\x01\x12\n\n\x06URGENT\x10\x02*.\n\x10\x43loseChannelType\x12\n\n\x06MUTUAL\x10\x00\x12\x0e\n\nUNILATERAL\x10\x01*2\n\rInvoiceStatus\x12\n\n\x06UNPAID\x10\x00\x12\x08\n\x04PAID\x10\x01\x12\x0b\n\x07\x45XPIRED\x10\x02*2\n\tPayStatus\x12\x0b\n\x07PENDING\x10\x00\x12\x0c\n\x08\x43OMPLETE\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x32\xf3\n\n\x04Node\x12\x44\n\x07GetInfo\x12\x1a.greenlight.GetInfoRequest\x1a\x1b.greenlight.GetInfoResponse\"\x00\x12;\n\x04Stop\x12\x17.greenlight.StopRequest\x1a\x18.greenlight.StopResponse\"\x00\x12H\n\x0b\x43onnectPeer\x12\x1a.greenlight.ConnectRequest\x1a\x1b.greenlight.ConnectResponse\"\x00\x12J\n\tListPeers\x12\x1c.greenlight.ListPeersRequest\x1a\x1d.greenlight.ListPeersResponse\"\x00\x12M\n\nDisconnect\x12\x1d.greenlight.DisconnectRequest\x1a\x1e.greenlight.DisconnectResponse\"\x00\x12\x44\n\x07NewAddr\x12\x1a.greenlight.NewAddrRequest\x1a\x1b.greenlight.NewAddrResponse\"\x00\x12J\n\tListFunds\x12\x1c.greenlight.ListFundsRequest\x1a\x1d.greenlight.ListFundsResponse\"\x00\x12G\n\x08Withdraw\x12\x1b.greenlight.WithdrawRequest\x1a\x1c.greenlight.WithdrawResponse\"\x00\x12P\n\x0b\x46undChannel\x12\x1e.greenlight.FundChannelRequest\x1a\x1f.greenlight.FundChannelResponse\"\x00\x12S\n\x0c\x43loseChannel\x12\x1f.greenlight.CloseChannelRequest\x1a .greenlight.CloseChannelResponse\"\x00\x12\x42\n\rCreateInvoice\x12\x1a.greenlight.InvoiceRequest\x1a\x13.greenlight.Invoice\"\x00\x12\x34\n\x03Pay\x12\x16.greenlight.PayRequest\x1a\x13.greenlight.Payment\"\x00\x12<\n\x07Keysend\x12\x1a.greenlight.KeysendRequest\x1a\x13.greenlight.Payment\"\x00\x12S\n\x0cListPayments\x12\x1f.greenlight.ListPaymentsRequest\x1a .greenlight.ListPaymentsResponse\"\x00\x12S\n\x0cListInvoices\x12\x1f.greenlight.ListInvoicesRequest\x1a .greenlight.ListInvoicesResponse\"\x00\x12S\n\x0eStreamIncoming\x12 .greenlight.StreamIncomingFilter\x1a\x1b.greenlight.IncomingPayment\"\x00\x30\x01\x12\x43\n\tStreamLog\x12\x1c.greenlight.StreamLogRequest\x1a\x14.greenlight.LogEntry\"\x00\x30\x01\x12\x42\n\x11StreamHsmRequests\x12\x11.greenlight.Empty\x1a\x16.greenlight.HsmRequest\"\x00\x30\x01\x12\x41\n\x11RespondHsmRequest\x12\x17.greenlight.HsmResponse\x1a\x11.greenlight.Empty\"\x00\x32s\n\x03Hsm\x12<\n\x07Request\x12\x16.greenlight.HsmRequest\x1a\x17.greenlight.HsmResponse\"\x00\x12.\n\x04Ping\x12\x11.greenlight.Empty\x1a\x11.greenlight.Empty\"\x00\x62\x06proto3')

_NETADDRESSTYPE = DESCRIPTOR.enum_types_by_name['NetAddressType']
NetAddressType = enum_type_wrapper.EnumTypeWrapper(_NETADDRESSTYPE)
_BTCADDRESSTYPE = DESCRIPTOR.enum_types_by_name['BtcAddressType']
BtcAddressType = enum_type_wrapper.EnumTypeWrapper(_BTCADDRESSTYPE)
_OUTPUTSTATUS = DESCRIPTOR.enum_types_by_name['OutputStatus']
OutputStatus = enum_type_wrapper.EnumTypeWrapper(_OUTPUTSTATUS)
_FEERATEPRESET = DESCRIPTOR.enum_types_by_name['FeeratePreset']
FeeratePreset = enum_type_wrapper.EnumTypeWrapper(_FEERATEPRESET)
_CLOSECHANNELTYPE = DESCRIPTOR.enum_types_by_name['CloseChannelType']
CloseChannelType = enum_type_wrapper.EnumTypeWrapper(_CLOSECHANNELTYPE)
_INVOICESTATUS = DESCRIPTOR.enum_types_by_name['InvoiceStatus']
InvoiceStatus = enum_type_wrapper.EnumTypeWrapper(_INVOICESTATUS)
_PAYSTATUS = DESCRIPTOR.enum_types_by_name['PayStatus']
PayStatus = enum_type_wrapper.EnumTypeWrapper(_PAYSTATUS)
Ipv4 = 0
Ipv6 = 1
TorV2 = 2
TorV3 = 3
BECH32 = 0
P2SH_SEGWIT = 1
CONFIRMED = 0
UNCONFIRMED = 1
NORMAL = 0
SLOW = 1
URGENT = 2
MUTUAL = 0
UNILATERAL = 1
UNPAID = 0
PAID = 1
EXPIRED = 2
PENDING = 0
COMPLETE = 1
FAILED = 2


_HSMREQUESTCONTEXT = DESCRIPTOR.message_types_by_name['HsmRequestContext']
_HSMRESPONSE = DESCRIPTOR.message_types_by_name['HsmResponse']
_HSMREQUEST = DESCRIPTOR.message_types_by_name['HsmRequest']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_ADDRESS = DESCRIPTOR.message_types_by_name['Address']
_GETINFOREQUEST = DESCRIPTOR.message_types_by_name['GetInfoRequest']
_GETINFORESPONSE = DESCRIPTOR.message_types_by_name['GetInfoResponse']
_STOPREQUEST = DESCRIPTOR.message_types_by_name['StopRequest']
_STOPRESPONSE = DESCRIPTOR.message_types_by_name['StopResponse']
_CONNECTREQUEST = DESCRIPTOR.message_types_by_name['ConnectRequest']
_CONNECTRESPONSE = DESCRIPTOR.message_types_by_name['ConnectResponse']
_LISTPEERSREQUEST = DESCRIPTOR.message_types_by_name['ListPeersRequest']
_HTLC = DESCRIPTOR.message_types_by_name['Htlc']
_CHANNEL = DESCRIPTOR.message_types_by_name['Channel']
_PEER = DESCRIPTOR.message_types_by_name['Peer']
_LISTPEERSRESPONSE = DESCRIPTOR.message_types_by_name['ListPeersResponse']
_DISCONNECTREQUEST = DESCRIPTOR.message_types_by_name['DisconnectRequest']
_DISCONNECTRESPONSE = DESCRIPTOR.message_types_by_name['DisconnectResponse']
_NEWADDRREQUEST = DESCRIPTOR.message_types_by_name['NewAddrRequest']
_NEWADDRRESPONSE = DESCRIPTOR.message_types_by_name['NewAddrResponse']
_LISTFUNDSREQUEST = DESCRIPTOR.message_types_by_name['ListFundsRequest']
_LISTFUNDSOUTPUT = DESCRIPTOR.message_types_by_name['ListFundsOutput']
_LISTFUNDSCHANNEL = DESCRIPTOR.message_types_by_name['ListFundsChannel']
_LISTFUNDSRESPONSE = DESCRIPTOR.message_types_by_name['ListFundsResponse']
_FEERATE = DESCRIPTOR.message_types_by_name['Feerate']
_CONFIRMATION = DESCRIPTOR.message_types_by_name['Confirmation']
_WITHDRAWREQUEST = DESCRIPTOR.message_types_by_name['WithdrawRequest']
_WITHDRAWRESPONSE = DESCRIPTOR.message_types_by_name['WithdrawResponse']
_FUNDCHANNELREQUEST = DESCRIPTOR.message_types_by_name['FundChannelRequest']
_OUTPOINT = DESCRIPTOR.message_types_by_name['Outpoint']
_FUNDCHANNELRESPONSE = DESCRIPTOR.message_types_by_name['FundChannelResponse']
_TIMEOUT = DESCRIPTOR.message_types_by_name['Timeout']
_BITCOINADDRESS = DESCRIPTOR.message_types_by_name['BitcoinAddress']
_CLOSECHANNELREQUEST = DESCRIPTOR.message_types_by_name['CloseChannelRequest']
_CLOSECHANNELRESPONSE = DESCRIPTOR.message_types_by_name['CloseChannelResponse']
_AMOUNT = DESCRIPTOR.message_types_by_name['Amount']
_INVOICEREQUEST = DESCRIPTOR.message_types_by_name['InvoiceRequest']
_INVOICE = DESCRIPTOR.message_types_by_name['Invoice']
_PAYREQUEST = DESCRIPTOR.message_types_by_name['PayRequest']
_PAYMENT = DESCRIPTOR.message_types_by_name['Payment']
_PAYMENTIDENTIFIER = DESCRIPTOR.message_types_by_name['PaymentIdentifier']
_LISTPAYMENTSREQUEST = DESCRIPTOR.message_types_by_name['ListPaymentsRequest']
_LISTPAYMENTSRESPONSE = DESCRIPTOR.message_types_by_name['ListPaymentsResponse']
_INVOICEIDENTIFIER = DESCRIPTOR.message_types_by_name['InvoiceIdentifier']
_LISTINVOICESREQUEST = DESCRIPTOR.message_types_by_name['ListInvoicesRequest']
_STREAMINCOMINGFILTER = DESCRIPTOR.message_types_by_name['StreamIncomingFilter']
_LISTINVOICESRESPONSE = DESCRIPTOR.message_types_by_name['ListInvoicesResponse']
_TLVFIELD = DESCRIPTOR.message_types_by_name['TlvField']
_OFFCHAINPAYMENT = DESCRIPTOR.message_types_by_name['OffChainPayment']
_INCOMINGPAYMENT = DESCRIPTOR.message_types_by_name['IncomingPayment']
_ROUTEHINTHOP = DESCRIPTOR.message_types_by_name['RoutehintHop']
_ROUTEHINT = DESCRIPTOR.message_types_by_name['Routehint']
_KEYSENDREQUEST = DESCRIPTOR.message_types_by_name['KeysendRequest']
_STREAMLOGREQUEST = DESCRIPTOR.message_types_by_name['StreamLogRequest']
_LOGENTRY = DESCRIPTOR.message_types_by_name['LogEntry']
HsmRequestContext = _reflection.GeneratedProtocolMessageType('HsmRequestContext', (_message.Message,), {
  'DESCRIPTOR' : _HSMREQUESTCONTEXT,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.HsmRequestContext)
  })
_sym_db.RegisterMessage(HsmRequestContext)

HsmResponse = _reflection.GeneratedProtocolMessageType('HsmResponse', (_message.Message,), {
  'DESCRIPTOR' : _HSMRESPONSE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.HsmResponse)
  })
_sym_db.RegisterMessage(HsmResponse)

HsmRequest = _reflection.GeneratedProtocolMessageType('HsmRequest', (_message.Message,), {
  'DESCRIPTOR' : _HSMREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.HsmRequest)
  })
_sym_db.RegisterMessage(HsmRequest)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.Empty)
  })
_sym_db.RegisterMessage(Empty)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESS,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.Address)
  })
_sym_db.RegisterMessage(Address)

GetInfoRequest = _reflection.GeneratedProtocolMessageType('GetInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINFOREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.GetInfoRequest)
  })
_sym_db.RegisterMessage(GetInfoRequest)

GetInfoResponse = _reflection.GeneratedProtocolMessageType('GetInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETINFORESPONSE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.GetInfoResponse)
  })
_sym_db.RegisterMessage(GetInfoResponse)

StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.StopRequest)
  })
_sym_db.RegisterMessage(StopRequest)

StopResponse = _reflection.GeneratedProtocolMessageType('StopResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPRESPONSE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.StopResponse)
  })
_sym_db.RegisterMessage(StopResponse)

ConnectRequest = _reflection.GeneratedProtocolMessageType('ConnectRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.ConnectRequest)
  })
_sym_db.RegisterMessage(ConnectRequest)

ConnectResponse = _reflection.GeneratedProtocolMessageType('ConnectResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTRESPONSE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.ConnectResponse)
  })
_sym_db.RegisterMessage(ConnectResponse)

ListPeersRequest = _reflection.GeneratedProtocolMessageType('ListPeersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPEERSREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.ListPeersRequest)
  })
_sym_db.RegisterMessage(ListPeersRequest)

Htlc = _reflection.GeneratedProtocolMessageType('Htlc', (_message.Message,), {
  'DESCRIPTOR' : _HTLC,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.Htlc)
  })
_sym_db.RegisterMessage(Htlc)

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), {
  'DESCRIPTOR' : _CHANNEL,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.Channel)
  })
_sym_db.RegisterMessage(Channel)

Peer = _reflection.GeneratedProtocolMessageType('Peer', (_message.Message,), {
  'DESCRIPTOR' : _PEER,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.Peer)
  })
_sym_db.RegisterMessage(Peer)

ListPeersResponse = _reflection.GeneratedProtocolMessageType('ListPeersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPEERSRESPONSE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.ListPeersResponse)
  })
_sym_db.RegisterMessage(ListPeersResponse)

DisconnectRequest = _reflection.GeneratedProtocolMessageType('DisconnectRequest', (_message.Message,), {
  'DESCRIPTOR' : _DISCONNECTREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.DisconnectRequest)
  })
_sym_db.RegisterMessage(DisconnectRequest)

DisconnectResponse = _reflection.GeneratedProtocolMessageType('DisconnectResponse', (_message.Message,), {
  'DESCRIPTOR' : _DISCONNECTRESPONSE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.DisconnectResponse)
  })
_sym_db.RegisterMessage(DisconnectResponse)

NewAddrRequest = _reflection.GeneratedProtocolMessageType('NewAddrRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEWADDRREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.NewAddrRequest)
  })
_sym_db.RegisterMessage(NewAddrRequest)

NewAddrResponse = _reflection.GeneratedProtocolMessageType('NewAddrResponse', (_message.Message,), {
  'DESCRIPTOR' : _NEWADDRRESPONSE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.NewAddrResponse)
  })
_sym_db.RegisterMessage(NewAddrResponse)

ListFundsRequest = _reflection.GeneratedProtocolMessageType('ListFundsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTFUNDSREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.ListFundsRequest)
  })
_sym_db.RegisterMessage(ListFundsRequest)

ListFundsOutput = _reflection.GeneratedProtocolMessageType('ListFundsOutput', (_message.Message,), {
  'DESCRIPTOR' : _LISTFUNDSOUTPUT,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.ListFundsOutput)
  })
_sym_db.RegisterMessage(ListFundsOutput)

ListFundsChannel = _reflection.GeneratedProtocolMessageType('ListFundsChannel', (_message.Message,), {
  'DESCRIPTOR' : _LISTFUNDSCHANNEL,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.ListFundsChannel)
  })
_sym_db.RegisterMessage(ListFundsChannel)

ListFundsResponse = _reflection.GeneratedProtocolMessageType('ListFundsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTFUNDSRESPONSE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.ListFundsResponse)
  })
_sym_db.RegisterMessage(ListFundsResponse)

Feerate = _reflection.GeneratedProtocolMessageType('Feerate', (_message.Message,), {
  'DESCRIPTOR' : _FEERATE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.Feerate)
  })
_sym_db.RegisterMessage(Feerate)

Confirmation = _reflection.GeneratedProtocolMessageType('Confirmation', (_message.Message,), {
  'DESCRIPTOR' : _CONFIRMATION,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.Confirmation)
  })
_sym_db.RegisterMessage(Confirmation)

WithdrawRequest = _reflection.GeneratedProtocolMessageType('WithdrawRequest', (_message.Message,), {
  'DESCRIPTOR' : _WITHDRAWREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.WithdrawRequest)
  })
_sym_db.RegisterMessage(WithdrawRequest)

WithdrawResponse = _reflection.GeneratedProtocolMessageType('WithdrawResponse', (_message.Message,), {
  'DESCRIPTOR' : _WITHDRAWRESPONSE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.WithdrawResponse)
  })
_sym_db.RegisterMessage(WithdrawResponse)

FundChannelRequest = _reflection.GeneratedProtocolMessageType('FundChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _FUNDCHANNELREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.FundChannelRequest)
  })
_sym_db.RegisterMessage(FundChannelRequest)

Outpoint = _reflection.GeneratedProtocolMessageType('Outpoint', (_message.Message,), {
  'DESCRIPTOR' : _OUTPOINT,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.Outpoint)
  })
_sym_db.RegisterMessage(Outpoint)

FundChannelResponse = _reflection.GeneratedProtocolMessageType('FundChannelResponse', (_message.Message,), {
  'DESCRIPTOR' : _FUNDCHANNELRESPONSE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.FundChannelResponse)
  })
_sym_db.RegisterMessage(FundChannelResponse)

Timeout = _reflection.GeneratedProtocolMessageType('Timeout', (_message.Message,), {
  'DESCRIPTOR' : _TIMEOUT,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.Timeout)
  })
_sym_db.RegisterMessage(Timeout)

BitcoinAddress = _reflection.GeneratedProtocolMessageType('BitcoinAddress', (_message.Message,), {
  'DESCRIPTOR' : _BITCOINADDRESS,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.BitcoinAddress)
  })
_sym_db.RegisterMessage(BitcoinAddress)

CloseChannelRequest = _reflection.GeneratedProtocolMessageType('CloseChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOSECHANNELREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.CloseChannelRequest)
  })
_sym_db.RegisterMessage(CloseChannelRequest)

CloseChannelResponse = _reflection.GeneratedProtocolMessageType('CloseChannelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLOSECHANNELRESPONSE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.CloseChannelResponse)
  })
_sym_db.RegisterMessage(CloseChannelResponse)

Amount = _reflection.GeneratedProtocolMessageType('Amount', (_message.Message,), {
  'DESCRIPTOR' : _AMOUNT,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.Amount)
  })
_sym_db.RegisterMessage(Amount)

InvoiceRequest = _reflection.GeneratedProtocolMessageType('InvoiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVOICEREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.InvoiceRequest)
  })
_sym_db.RegisterMessage(InvoiceRequest)

Invoice = _reflection.GeneratedProtocolMessageType('Invoice', (_message.Message,), {
  'DESCRIPTOR' : _INVOICE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.Invoice)
  })
_sym_db.RegisterMessage(Invoice)

PayRequest = _reflection.GeneratedProtocolMessageType('PayRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAYREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.PayRequest)
  })
_sym_db.RegisterMessage(PayRequest)

Payment = _reflection.GeneratedProtocolMessageType('Payment', (_message.Message,), {
  'DESCRIPTOR' : _PAYMENT,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.Payment)
  })
_sym_db.RegisterMessage(Payment)

PaymentIdentifier = _reflection.GeneratedProtocolMessageType('PaymentIdentifier', (_message.Message,), {
  'DESCRIPTOR' : _PAYMENTIDENTIFIER,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.PaymentIdentifier)
  })
_sym_db.RegisterMessage(PaymentIdentifier)

ListPaymentsRequest = _reflection.GeneratedProtocolMessageType('ListPaymentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPAYMENTSREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.ListPaymentsRequest)
  })
_sym_db.RegisterMessage(ListPaymentsRequest)

ListPaymentsResponse = _reflection.GeneratedProtocolMessageType('ListPaymentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPAYMENTSRESPONSE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.ListPaymentsResponse)
  })
_sym_db.RegisterMessage(ListPaymentsResponse)

InvoiceIdentifier = _reflection.GeneratedProtocolMessageType('InvoiceIdentifier', (_message.Message,), {
  'DESCRIPTOR' : _INVOICEIDENTIFIER,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.InvoiceIdentifier)
  })
_sym_db.RegisterMessage(InvoiceIdentifier)

ListInvoicesRequest = _reflection.GeneratedProtocolMessageType('ListInvoicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTINVOICESREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.ListInvoicesRequest)
  })
_sym_db.RegisterMessage(ListInvoicesRequest)

StreamIncomingFilter = _reflection.GeneratedProtocolMessageType('StreamIncomingFilter', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINCOMINGFILTER,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.StreamIncomingFilter)
  })
_sym_db.RegisterMessage(StreamIncomingFilter)

ListInvoicesResponse = _reflection.GeneratedProtocolMessageType('ListInvoicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTINVOICESRESPONSE,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.ListInvoicesResponse)
  })
_sym_db.RegisterMessage(ListInvoicesResponse)

TlvField = _reflection.GeneratedProtocolMessageType('TlvField', (_message.Message,), {
  'DESCRIPTOR' : _TLVFIELD,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.TlvField)
  })
_sym_db.RegisterMessage(TlvField)

OffChainPayment = _reflection.GeneratedProtocolMessageType('OffChainPayment', (_message.Message,), {
  'DESCRIPTOR' : _OFFCHAINPAYMENT,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.OffChainPayment)
  })
_sym_db.RegisterMessage(OffChainPayment)

IncomingPayment = _reflection.GeneratedProtocolMessageType('IncomingPayment', (_message.Message,), {
  'DESCRIPTOR' : _INCOMINGPAYMENT,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.IncomingPayment)
  })
_sym_db.RegisterMessage(IncomingPayment)

RoutehintHop = _reflection.GeneratedProtocolMessageType('RoutehintHop', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEHINTHOP,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.RoutehintHop)
  })
_sym_db.RegisterMessage(RoutehintHop)

Routehint = _reflection.GeneratedProtocolMessageType('Routehint', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEHINT,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.Routehint)
  })
_sym_db.RegisterMessage(Routehint)

KeysendRequest = _reflection.GeneratedProtocolMessageType('KeysendRequest', (_message.Message,), {
  'DESCRIPTOR' : _KEYSENDREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.KeysendRequest)
  })
_sym_db.RegisterMessage(KeysendRequest)

StreamLogRequest = _reflection.GeneratedProtocolMessageType('StreamLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMLOGREQUEST,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.StreamLogRequest)
  })
_sym_db.RegisterMessage(StreamLogRequest)

LogEntry = _reflection.GeneratedProtocolMessageType('LogEntry', (_message.Message,), {
  'DESCRIPTOR' : _LOGENTRY,
  '__module__' : 'greenlight_pb2'
  # @@protoc_insertion_point(class_scope:greenlight.LogEntry)
  })
_sym_db.RegisterMessage(LogEntry)

_NODE = DESCRIPTOR.services_by_name['Node']
_HSM = DESCRIPTOR.services_by_name['Hsm']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NETADDRESSTYPE._serialized_start=5078
  _NETADDRESSTYPE._serialized_end=5136
  _BTCADDRESSTYPE._serialized_start=5138
  _BTCADDRESSTYPE._serialized_end=5183
  _OUTPUTSTATUS._serialized_start=5185
  _OUTPUTSTATUS._serialized_end=5231
  _FEERATEPRESET._serialized_start=5233
  _FEERATEPRESET._serialized_end=5282
  _CLOSECHANNELTYPE._serialized_start=5284
  _CLOSECHANNELTYPE._serialized_end=5330
  _INVOICESTATUS._serialized_start=5332
  _INVOICESTATUS._serialized_end=5382
  _PAYSTATUS._serialized_start=5384
  _PAYSTATUS._serialized_end=5434
  _HSMREQUESTCONTEXT._serialized_start=32
  _HSMREQUESTCONTEXT._serialized_end=104
  _HSMRESPONSE._serialized_start=106
  _HSMRESPONSE._serialized_end=152
  _HSMREQUEST._serialized_start=154
  _HSMREQUEST._serialized_end=247
  _EMPTY._serialized_start=249
  _EMPTY._serialized_end=256
  _ADDRESS._serialized_start=258
  _ADDRESS._serialized_end=337
  _GETINFOREQUEST._serialized_start=339
  _GETINFOREQUEST._serialized_end=355
  _GETINFORESPONSE._serialized_start=358
  _GETINFORESPONSE._serialized_end=536
  _STOPREQUEST._serialized_start=538
  _STOPREQUEST._serialized_end=551
  _STOPRESPONSE._serialized_start=553
  _STOPRESPONSE._serialized_end=567
  _CONNECTREQUEST._serialized_start=569
  _CONNECTREQUEST._serialized_end=616
  _CONNECTRESPONSE._serialized_start=618
  _CONNECTRESPONSE._serialized_end=670
  _LISTPEERSREQUEST._serialized_start=672
  _LISTPEERSREQUEST._serialized_end=707
  _HTLC._serialized_start=710
  _HTLC._serialized_end=839
  _CHANNEL._serialized_start=842
  _CHANNEL._serialized_end=1205
  _PEER._serialized_start=1208
  _PEER._serialized_end=1342
  _LISTPEERSRESPONSE._serialized_start=1344
  _LISTPEERSRESPONSE._serialized_end=1396
  _DISCONNECTREQUEST._serialized_start=1398
  _DISCONNECTREQUEST._serialized_end=1449
  _DISCONNECTRESPONSE._serialized_start=1451
  _DISCONNECTRESPONSE._serialized_end=1471
  _NEWADDRREQUEST._serialized_start=1473
  _NEWADDRREQUEST._serialized_end=1539
  _NEWADDRRESPONSE._serialized_start=1541
  _NEWADDRRESPONSE._serialized_end=1625
  _LISTFUNDSREQUEST._serialized_start=1627
  _LISTFUNDSREQUEST._serialized_end=1688
  _LISTFUNDSOUTPUT._serialized_start=1691
  _LISTFUNDSOUTPUT._serialized_end=1841
  _LISTFUNDSCHANNEL._serialized_start=1844
  _LISTFUNDSCHANNEL._serialized_end=2016
  _LISTFUNDSRESPONSE._serialized_start=2018
  _LISTFUNDSRESPONSE._serialized_end=2131
  _FEERATE._serialized_start=2133
  _FEERATE._serialized_end=2230
  _CONFIRMATION._serialized_start=2232
  _CONFIRMATION._serialized_end=2262
  _WITHDRAWREQUEST._serialized_start=2265
  _WITHDRAWREQUEST._serialized_end=2457
  _WITHDRAWRESPONSE._serialized_start=2459
  _WITHDRAWRESPONSE._serialized_end=2503
  _FUNDCHANNELREQUEST._serialized_start=2506
  _FUNDCHANNELREQUEST._serialized_end=2696
  _OUTPOINT._serialized_start=2698
  _OUTPOINT._serialized_end=2738
  _FUNDCHANNELRESPONSE._serialized_start=2740
  _FUNDCHANNELRESPONSE._serialized_end=2851
  _TIMEOUT._serialized_start=2853
  _TIMEOUT._serialized_end=2879
  _BITCOINADDRESS._serialized_start=2881
  _BITCOINADDRESS._serialized_end=2914
  _CLOSECHANNELREQUEST._serialized_start=2917
  _CLOSECHANNELREQUEST._serialized_end=3052
  _CLOSECHANNELRESPONSE._serialized_start=3054
  _CLOSECHANNELRESPONSE._serialized_end=3152
  _AMOUNT._serialized_start=3154
  _AMOUNT._serialized_end=3262
  _INVOICEREQUEST._serialized_start=3264
  _INVOICEREQUEST._serialized_end=3352
  _INVOICE._serialized_start=3355
  _INVOICE._serialized_end=3624
  _PAYREQUEST._serialized_start=3626
  _PAYREQUEST._serialized_end=3707
  _PAYMENT._serialized_start=3710
  _PAYMENT._serialized_end=3940
  _PAYMENTIDENTIFIER._serialized_start=3942
  _PAYMENTIDENTIFIER._serialized_end=4009
  _LISTPAYMENTSREQUEST._serialized_start=4011
  _LISTPAYMENTSREQUEST._serialized_end=4083
  _LISTPAYMENTSRESPONSE._serialized_start=4085
  _LISTPAYMENTSRESPONSE._serialized_end=4146
  _INVOICEIDENTIFIER._serialized_start=4148
  _INVOICEIDENTIFIER._serialized_end=4235
  _LISTINVOICESREQUEST._serialized_start=4237
  _LISTINVOICESREQUEST._serialized_end=4309
  _STREAMINCOMINGFILTER._serialized_start=4311
  _STREAMINCOMINGFILTER._serialized_end=4333
  _LISTINVOICESRESPONSE._serialized_start=4335
  _LISTINVOICESRESPONSE._serialized_end=4396
  _TLVFIELD._serialized_start=4398
  _TLVFIELD._serialized_end=4437
  _OFFCHAINPAYMENT._serialized_start=4440
  _OFFCHAINPAYMENT._serialized_end=4605
  _INCOMINGPAYMENT._serialized_start=4607
  _INCOMINGPAYMENT._serialized_end=4684
  _ROUTEHINTHOP._serialized_start=4686
  _ROUTEHINTHOP._serialized_end=4806
  _ROUTEHINT._serialized_start=4808
  _ROUTEHINT._serialized_end=4859
  _KEYSENDREQUEST._serialized_start=4862
  _KEYSENDREQUEST._serialized_end=5030
  _STREAMLOGREQUEST._serialized_start=5032
  _STREAMLOGREQUEST._serialized_end=5050
  _LOGENTRY._serialized_start=5052
  _LOGENTRY._serialized_end=5076
  _NODE._serialized_start=5437
  _NODE._serialized_end=6832
  _HSM._serialized_start=6834
  _HSM._serialized_end=6949
# @@protoc_insertion_point(module_scope)
