# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simulator.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0fsimulator.proto\x12\tsimulator\x1a\x1bgoogle/protobuf/empty.proto"\x17\n\x08\x41gentIdx\x12\x0b\n\x03idx\x18\x01 \x03(\x05"\x1a\n\x07NDArray\x12\x0f\n\x07ndarray\x18\x01 \x01(\x0c"X\n\tRigidBody\x12"\n\x06\x63\x65nter\x18\x01 \x01(\x0b\x32\x12.simulator.NDArray\x12\'\n\x0borientation\x18\x02 \x01(\x0b\x32\x12.simulator.NDArray"\x8b\x04\n\x0eSimulatorState\x12\x1f\n\x03idx\x18\x01 \x01(\x0b\x32\x12.simulator.NDArray\x12$\n\x08\x62ox_size\x18\x02 \x01(\x0b\x32\x12.simulator.NDArray\x12&\n\nmax_agents\x18\x03 \x01(\x0b\x32\x12.simulator.NDArray\x12\'\n\x0bmax_objects\x18\x04 \x01(\x0b\x32\x12.simulator.NDArray\x12)\n\rnum_steps_lax\x18\x05 \x01(\x0b\x32\x12.simulator.NDArray\x12\x1e\n\x02\x64t\x18\x06 \x01(\x0b\x32\x12.simulator.NDArray\x12 \n\x04\x66req\x18\x07 \x01(\x0b\x32\x12.simulator.NDArray\x12+\n\x0fneighbor_radius\x18\x08 \x01(\x0b\x32\x12.simulator.NDArray\x12"\n\x06to_jit\x18\t \x01(\x0b\x32\x12.simulator.NDArray\x12)\n\ruse_fori_loop\x18\n \x01(\x0b\x32\x12.simulator.NDArray\x12)\n\rcollision_eps\x18\x0b \x01(\x0b\x32\x12.simulator.NDArray\x12+\n\x0f\x63ollision_alpha\x18\x0c \x01(\x0b\x32\x12.simulator.NDArray\x12 \n\x04time\x18\r \x01(\x0b\x32\x12.simulator.NDArray"\x90\x03\n\x0b\x45ntityState\x12&\n\x08position\x18\x01 \x01(\x0b\x32\x14.simulator.RigidBody\x12&\n\x08momentum\x18\x02 \x01(\x0b\x32\x14.simulator.RigidBody\x12#\n\x05\x66orce\x18\x03 \x01(\x0b\x32\x14.simulator.RigidBody\x12"\n\x04mass\x18\x04 \x01(\x0b\x32\x14.simulator.RigidBody\x12$\n\x08\x64iameter\x18\x05 \x01(\x0b\x32\x12.simulator.NDArray\x12\'\n\x0b\x65ntity_type\x18\x06 \x01(\x0b\x32\x12.simulator.NDArray\x12&\n\nentity_idx\x18\x07 \x01(\x0b\x32\x12.simulator.NDArray\x12$\n\x08\x66riction\x18\x08 \x01(\x0b\x32\x12.simulator.NDArray\x12"\n\x06\x65xists\x18\t \x01(\x0b\x32\x12.simulator.NDArray\x12\'\n\x0b\x65nt_subtype\x18\n \x01(\x0b\x32\x12.simulator.NDArray"\xc3\x05\n\nAgentState\x12#\n\x07\x65nt_idx\x18\x01 \x01(\x0b\x32\x12.simulator.NDArray\x12 \n\x04prox\x18\x02 \x01(\x0b\x32\x12.simulator.NDArray\x12!\n\x05motor\x18\x03 \x01(\x0b\x32\x12.simulator.NDArray\x12$\n\x08\x62\x65havior\x18\x04 \x01(\x0b\x32\x12.simulator.NDArray\x12*\n\x0ewheel_diameter\x18\x05 \x01(\x0b\x32\x12.simulator.NDArray\x12%\n\tspeed_mul\x18\x06 \x01(\x0b\x32\x12.simulator.NDArray\x12%\n\tmax_speed\x18\x07 \x01(\x0b\x32\x12.simulator.NDArray\x12%\n\ttheta_mul\x18\x08 \x01(\x0b\x32\x12.simulator.NDArray\x12*\n\x0eproxs_dist_max\x18\t \x01(\x0b\x32\x12.simulator.NDArray\x12)\n\rproxs_cos_min\x18\n \x01(\x0b\x32\x12.simulator.NDArray\x12!\n\x05\x63olor\x18\x0b \x01(\x0b\x32\x12.simulator.NDArray\x12.\n\x12proximity_map_dist\x18\x0c \x01(\x0b\x32\x12.simulator.NDArray\x12/\n\x13proximity_map_theta\x18\r \x01(\x0b\x32\x12.simulator.NDArray\x12"\n\x06params\x18\x0e \x01(\x0b\x32\x12.simulator.NDArray\x12"\n\x06sensed\x18\x0f \x01(\x0b\x32\x12.simulator.NDArray\x12\x30\n\x14prox_sensed_ent_type\x18\x10 \x01(\x0b\x32\x12.simulator.NDArray\x12/\n\x13prox_sensed_ent_idx\x18\x11 \x01(\x0b\x32\x12.simulator.NDArray"\x7f\n\x0bObjectState\x12#\n\x07\x65nt_idx\x18\x01 \x01(\x0b\x32\x12.simulator.NDArray\x12(\n\x0c\x63ustom_field\x18\x02 \x01(\x0b\x32\x12.simulator.NDArray\x12!\n\x05\x63olor\x18\x03 \x01(\x0b\x32\x12.simulator.NDArray"\xc3\x01\n\x05State\x12\x32\n\x0fsimulator_state\x18\x01 \x01(\x0b\x32\x19.simulator.SimulatorState\x12,\n\x0c\x65ntity_state\x18\x02 \x01(\x0b\x32\x16.simulator.EntityState\x12*\n\x0b\x61gent_state\x18\x03 \x01(\x0b\x32\x15.simulator.AgentState\x12,\n\x0cobject_state\x18\x04 \x01(\x0b\x32\x16.simulator.ObjectState"h\n\x0bStateChange\x12\x0f\n\x07\x65nt_idx\x18\x01 \x03(\x05\x12\x0f\n\x07\x63ol_idx\x18\x02 \x03(\x05\x12\x14\n\x0cnested_field\x18\x03 \x03(\t\x12!\n\x05value\x18\x04 \x01(\x0b\x32\x12.simulator.NDArray">\n\rAddAgentInput\x12\x12\n\nmax_agents\x18\x01 \x01(\x05\x12\x19\n\x11serialized_config\x18\x02 \x01(\t"$\n\x0eIsStartedState\x12\x12\n\nis_started\x18\x01 \x01(\x08"p\n\x0eSubtypesLabels\x12\x31\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32#.simulator.SubtypesLabels.DataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"\x1b\n\x05Scene\x12\x12\n\nscene_name\x18\x01 \x01(\t2\xbc\x05\n\x0fSimulatorServer\x12\x32\n\x04Step\x12\x16.google.protobuf.Empty\x1a\x10.simulator.State"\x00\x12\x36\n\x08GetState\x12\x16.google.protobuf.Empty\x1a\x10.simulator.State"\x00\x12?\n\x0bGetNVEState\x12\x16.google.protobuf.Empty\x1a\x16.simulator.EntityState"\x00\x12@\n\rGetAgentState\x12\x16.google.protobuf.Empty\x1a\x15.simulator.AgentState"\x00\x12\x42\n\x0eGetObjectState\x12\x16.google.protobuf.Empty\x1a\x16.simulator.ObjectState"\x00\x12<\n\x08SetState\x12\x16.simulator.StateChange\x1a\x16.google.protobuf.Empty"\x00\x12\x34\n\x0cGetSceneName\x12\x10.simulator.Scene\x1a\x10.simulator.Scene"\x00\x12K\n\x11GetSubtypesLabels\x12\x19.simulator.SubtypesLabels\x1a\x19.simulator.SubtypesLabels"\x00\x12@\n\tIsStarted\x12\x16.google.protobuf.Empty\x1a\x19.simulator.IsStartedState"\x00\x12\x39\n\x05Start\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty"\x00\x12\x38\n\x04Stop\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty"\x00\x42\x34\n\x1aio.grpc.examples.simulatorB\x0eSimulatorProtoP\x01\xa2\x02\x03SIMb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "simulator_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"\n\032io.grpc.examples.simulatorB\016SimulatorProtoP\001\242\002\003SIM"
    )
    _globals["_SUBTYPESLABELS_DATAENTRY"]._options = None
    _globals["_SUBTYPESLABELS_DATAENTRY"]._serialized_options = b"8\001"
    _globals["_AGENTIDX"]._serialized_start = 59
    _globals["_AGENTIDX"]._serialized_end = 82
    _globals["_NDARRAY"]._serialized_start = 84
    _globals["_NDARRAY"]._serialized_end = 110
    _globals["_RIGIDBODY"]._serialized_start = 112
    _globals["_RIGIDBODY"]._serialized_end = 200
    _globals["_SIMULATORSTATE"]._serialized_start = 203
    _globals["_SIMULATORSTATE"]._serialized_end = 726
    _globals["_ENTITYSTATE"]._serialized_start = 729
    _globals["_ENTITYSTATE"]._serialized_end = 1129
    _globals["_AGENTSTATE"]._serialized_start = 1132
    _globals["_AGENTSTATE"]._serialized_end = 1839
    _globals["_OBJECTSTATE"]._serialized_start = 1841
    _globals["_OBJECTSTATE"]._serialized_end = 1968
    _globals["_STATE"]._serialized_start = 1971
    _globals["_STATE"]._serialized_end = 2166
    _globals["_STATECHANGE"]._serialized_start = 2168
    _globals["_STATECHANGE"]._serialized_end = 2272
    _globals["_ADDAGENTINPUT"]._serialized_start = 2274
    _globals["_ADDAGENTINPUT"]._serialized_end = 2336
    _globals["_ISSTARTEDSTATE"]._serialized_start = 2338
    _globals["_ISSTARTEDSTATE"]._serialized_end = 2374
    _globals["_SUBTYPESLABELS"]._serialized_start = 2376
    _globals["_SUBTYPESLABELS"]._serialized_end = 2488
    _globals["_SUBTYPESLABELS_DATAENTRY"]._serialized_start = 2445
    _globals["_SUBTYPESLABELS_DATAENTRY"]._serialized_end = 2488
    _globals["_SCENE"]._serialized_start = 2490
    _globals["_SCENE"]._serialized_end = 2517
    _globals["_SIMULATORSERVER"]._serialized_start = 2520
    _globals["_SIMULATORSERVER"]._serialized_end = 3220
# @@protoc_insertion_point(module_scope)
