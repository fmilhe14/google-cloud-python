# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/dataset.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.automl_v1beta1.proto import (
    annotation_payload_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_annotation__payload__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    data_items_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__items__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    image_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_image__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    text_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    translation_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_translation__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/dataset.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_pb=_b(
        '\n/google/cloud/automl_v1beta1/proto/dataset.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a:google/cloud/automl_v1beta1/proto/annotation_payload.proto\x1a\x32google/cloud/automl_v1beta1/proto/data_items.proto\x1a-google/cloud/automl_v1beta1/proto/image.proto\x1a,google/cloud/automl_v1beta1/proto/text.proto\x1a\x33google/cloud/automl_v1beta1/proto/translation.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcc\x03\n\x07\x44\x61taset\x12_\n\x1ctranslation_dataset_metadata\x18\x17 \x01(\x0b\x32\x37.google.cloud.automl.v1beta1.TranslationDatasetMetadataH\x00\x12p\n%image_classification_dataset_metadata\x18\x18 \x01(\x0b\x32?.google.cloud.automl.v1beta1.ImageClassificationDatasetMetadataH\x00\x12n\n$text_classification_dataset_metadata\x18\x19 \x01(\x0b\x32>.google.cloud.automl.v1beta1.TextClassificationDatasetMetadataH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x15\n\rexample_count\x18\x15 \x01(\x05\x12/\n\x0b\x63reate_time\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x12\n\x10\x64\x61taset_metadataB\x84\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_annotation__payload__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__items__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_image__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_translation__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_DATASET = _descriptor.Descriptor(
    name="Dataset",
    full_name="google.cloud.automl.v1beta1.Dataset",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="translation_dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.translation_dataset_metadata",
            index=0,
            number=23,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="image_classification_dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.image_classification_dataset_metadata",
            index=1,
            number=24,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="text_classification_dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.text_classification_dataset_metadata",
            index=2,
            number=25,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.automl.v1beta1.Dataset.name",
            index=3,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.automl.v1beta1.Dataset.display_name",
            index=4,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="example_count",
            full_name="google.cloud.automl.v1beta1.Dataset.example_count",
            index=5,
            number=21,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.cloud.automl.v1beta1.Dataset.create_time",
            index=6,
            number=14,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="dataset_metadata",
            full_name="google.cloud.automl.v1beta1.Dataset.dataset_metadata",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=402,
    serialized_end=862,
)

_DATASET.fields_by_name[
    "translation_dataset_metadata"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_translation__pb2._TRANSLATIONDATASETMETADATA
)
_DATASET.fields_by_name[
    "image_classification_dataset_metadata"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_image__pb2._IMAGECLASSIFICATIONDATASETMETADATA
)
_DATASET.fields_by_name[
    "text_classification_dataset_metadata"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_text__pb2._TEXTCLASSIFICATIONDATASETMETADATA
)
_DATASET.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DATASET.oneofs_by_name["dataset_metadata"].fields.append(
    _DATASET.fields_by_name["translation_dataset_metadata"]
)
_DATASET.fields_by_name[
    "translation_dataset_metadata"
].containing_oneof = _DATASET.oneofs_by_name["dataset_metadata"]
_DATASET.oneofs_by_name["dataset_metadata"].fields.append(
    _DATASET.fields_by_name["image_classification_dataset_metadata"]
)
_DATASET.fields_by_name[
    "image_classification_dataset_metadata"
].containing_oneof = _DATASET.oneofs_by_name["dataset_metadata"]
_DATASET.oneofs_by_name["dataset_metadata"].fields.append(
    _DATASET.fields_by_name["text_classification_dataset_metadata"]
)
_DATASET.fields_by_name[
    "text_classification_dataset_metadata"
].containing_oneof = _DATASET.oneofs_by_name["dataset_metadata"]
DESCRIPTOR.message_types_by_name["Dataset"] = _DATASET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dataset = _reflection.GeneratedProtocolMessageType(
    "Dataset",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DATASET,
        __module__="google.cloud.automl_v1beta1.proto.dataset_pb2",
        __doc__="""A workspace for solving a single, particular machine learning (ML)
  problem. A workspace contains examples that may be annotated.
  
  
  Attributes:
      dataset_metadata:
          Required. The dataset metadata that is specific to the problem
          type.
      translation_dataset_metadata:
          Metadata for a dataset used for translation.
      image_classification_dataset_metadata:
          Metadata for a dataset used for image classification.
      text_classification_dataset_metadata:
          Metadata for a dataset used for text classification.
      name:
          Output only. The resource name of the dataset. Form: ``project
          s/{project_id}/locations/{location_id}/datasets/{dataset_id}``
      display_name:
          Required. The name of the dataset to show in the interface.
          The name can be up to 32 characters long and can consist only
          of ASCII Latin letters A-Z and a-z, underscores (\_), and
          ASCII digits 0-9.
      example_count:
          Output only. The number of examples in the dataset.
      create_time:
          Output only. Timestamp when this dataset was created.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.Dataset)
    ),
)
_sym_db.RegisterMessage(Dataset)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(),
    _b(
        "\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1"
    ),
)
# @@protoc_insertion_point(module_scope)
