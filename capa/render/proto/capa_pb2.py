# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: capa/render/proto/capa.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63\x61pa/render/proto/capa.proto\"Q\n\nAPIFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03\x61pi\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"l\n\x07\x41\x64\x64ress\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.AddressType\x12\x15\n\x01v\x18\x02 \x01(\x0b\x32\x08.IntegerH\x00\x12%\n\x0ctoken_offset\x18\x03 \x01(\x0b\x32\r.Token_OffsetH\x00\x42\x07\n\x05value\"\xe4\x01\n\x08\x41nalysis\x12\x0e\n\x06\x66ormat\x18\x01 \x01(\t\x12\x0c\n\x04\x61rch\x18\x02 \x01(\t\x12\n\n\x02os\x18\x03 \x01(\t\x12\x11\n\textractor\x18\x04 \x01(\t\x12\r\n\x05rules\x18\x05 \x03(\t\x12\x1e\n\x0c\x62\x61se_address\x18\x06 \x01(\x0b\x32\x08.Address\x12\x17\n\x06layout\x18\x07 \x01(\x0b\x32\x07.Layout\x12&\n\x0e\x66\x65\x61ture_counts\x18\x08 \x01(\x0b\x32\x0e.FeatureCounts\x12+\n\x11library_functions\x18\t \x03(\x0b\x32\x10.LibraryFunction\"S\n\x0b\x41rchFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04\x61rch\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"`\n\nAttackSpec\x12\r\n\x05parts\x18\x01 \x03(\t\x12\x0e\n\x06tactic\x18\x02 \x01(\t\x12\x11\n\ttechnique\x18\x03 \x01(\t\x12\x14\n\x0csubtechnique\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\"K\n\x11\x42\x61sicBlockFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"-\n\x10\x42\x61sicBlockLayout\x12\x19\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x08.Address\"U\n\x0c\x42ytesFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05\x62ytes\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"g\n\x15\x43haracteristicFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x16\n\x0e\x63haracteristic\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"V\n\x0c\x43lassFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06\x63lass_\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"K\n\x11\x43ompoundStatement\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"W\n\rExportFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06\x65xport\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"G\n\rFeatureCounts\x12\x0c\n\x04\x66ile\x18\x01 \x01(\x04\x12(\n\tfunctions\x18\x02 \x03(\x0b\x32\x15.FunctionFeatureCount\"\xf7\x06\n\x0b\x46\x65\x61tureNode\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x18\n\x02os\x18\x02 \x01(\x0b\x32\n.OSFeatureH\x00\x12\x1c\n\x04\x61rch\x18\x03 \x01(\x0b\x32\x0c.ArchFeatureH\x00\x12 \n\x06\x66ormat\x18\x04 \x01(\x0b\x32\x0e.FormatFeatureH\x00\x12\x1e\n\x05match\x18\x05 \x01(\x0b\x32\r.MatchFeatureH\x00\x12\x30\n\x0e\x63haracteristic\x18\x06 \x01(\x0b\x32\x16.CharacteristicFeatureH\x00\x12 \n\x06\x65xport\x18\x07 \x01(\x0b\x32\x0e.ExportFeatureH\x00\x12!\n\x07import_\x18\x08 \x01(\x0b\x32\x0e.ImportFeatureH\x00\x12\"\n\x07section\x18\t \x01(\x0b\x32\x0f.SectionFeatureH\x00\x12-\n\rfunction_name\x18\n \x01(\x0b\x32\x14.FunctionNameFeatureH\x00\x12&\n\tsubstring\x18\x0b \x01(\x0b\x32\x11.SubstringFeatureH\x00\x12\x1e\n\x05regex\x18\x0c \x01(\x0b\x32\r.RegexFeatureH\x00\x12 \n\x06string\x18\r \x01(\x0b\x32\x0e.StringFeatureH\x00\x12\x1f\n\x06\x63lass_\x18\x0e \x01(\x0b\x32\r.ClassFeatureH\x00\x12&\n\tnamespace\x18\x0f \x01(\x0b\x32\x11.NamespaceFeatureH\x00\x12\x1a\n\x03\x61pi\x18\x10 \x01(\x0b\x32\x0b.APIFeatureH\x00\x12%\n\tproperty_\x18\x11 \x01(\x0b\x32\x10.PropertyFeatureH\x00\x12 \n\x06number\x18\x12 \x01(\x0b\x32\x0e.NumberFeatureH\x00\x12\x1e\n\x05\x62ytes\x18\x13 \x01(\x0b\x32\r.BytesFeatureH\x00\x12 \n\x06offset\x18\x14 \x01(\x0b\x32\x0e.OffsetFeatureH\x00\x12$\n\x08mnemonic\x18\x15 \x01(\x0b\x32\x10.MnemonicFeatureH\x00\x12/\n\x0eoperand_number\x18\x16 \x01(\x0b\x32\x15.OperandNumberFeatureH\x00\x12/\n\x0eoperand_offset\x18\x17 \x01(\x0b\x32\x15.OperandOffsetFeatureH\x00\x12)\n\x0b\x62\x61sic_block\x18\x18 \x01(\x0b\x32\x12.BasicBlockFeatureH\x00\x42\t\n\x07\x66\x65\x61ture\"W\n\rFormatFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"@\n\x14\x46unctionFeatureCount\x12\x19\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x08.Address\x12\r\n\x05\x63ount\x18\x02 \x01(\x04\"\\\n\x0e\x46unctionLayout\x12\x19\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x08.Address\x12/\n\x14matched_basic_blocks\x18\x02 \x03(\x0b\x32\x11.BasicBlockLayout\"d\n\x13\x46unctionNameFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x15\n\rfunction_name\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"X\n\rImportFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07import_\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\",\n\x06Layout\x12\"\n\tfunctions\x18\x01 \x03(\x0b\x32\x0f.FunctionLayout\":\n\x0fLibraryFunction\x12\x19\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x08.Address\x12\x0c\n\x04name\x18\x02 \x01(\t\"Y\n\x07MBCSpec\x12\r\n\x05parts\x18\x01 \x03(\t\x12\x11\n\tobjective\x18\x02 \x01(\t\x12\x10\n\x08\x62\x65havior\x18\x03 \x01(\t\x12\x0e\n\x06method\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\"\x9a\x01\n\x0cMaecMetadata\x12\x1b\n\x13\x61nalysis_conclusion\x18\x01 \x01(\t\x12\x1e\n\x16\x61nalysis_conclusion_ov\x18\x02 \x01(\t\x12\x16\n\x0emalware_family\x18\x03 \x01(\t\x12\x18\n\x10malware_category\x18\x04 \x01(\t\x12\x1b\n\x13malware_category_ov\x18\x05 \x01(\t\"\x82\x02\n\x05Match\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12#\n\tstatement\x18\x02 \x01(\x0b\x32\x0e.StatementNodeH\x00\x12\x1f\n\x07\x66\x65\x61ture\x18\x03 \x01(\x0b\x32\x0c.FeatureNodeH\x00\x12\x18\n\x08\x63hildren\x18\x05 \x03(\x0b\x32\x06.Match\x12\x1b\n\tlocations\x18\x06 \x03(\x0b\x32\x08.Address\x12&\n\x08\x63\x61ptures\x18\x07 \x03(\x0b\x32\x14.Match.CapturesEntry\x1a;\n\rCapturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.Addresses:\x02\x38\x01\x42\x06\n\x04node\"U\n\x0cMatchFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05match\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"\x8b\x01\n\x08Metadata\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgv\x18\x03 \x03(\t\x12\x17\n\x06sample\x18\x04 \x01(\x0b\x32\x07.Sample\x12\x1b\n\x08\x61nalysis\x18\x05 \x01(\x0b\x32\t.Analysis\x12\x17\n\x06\x66lavor\x18\x06 \x01(\x0e\x32\x07.Flavor\"[\n\x0fMnemonicFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08mnemonic\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"]\n\x10NamespaceFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"`\n\rNumberFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x17\n\x06number\x18\x02 \x01(\x0b\x32\x07.Number\x12\x18\n\x0b\x64\x65scription\x18\x05 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"O\n\tOSFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02os\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"a\n\rOffsetFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x18\n\x06offset\x18\x02 \x01(\x0b\x32\x08.Integer\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"\x7f\n\x14OperandNumberFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\r\x12 \n\x0eoperand_number\x18\x03 \x01(\x0b\x32\x08.Integer\x12\x18\n\x0b\x64\x65scription\x18\x04 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"\x7f\n\x14OperandOffsetFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\r\x12 \n\x0eoperand_offset\x18\x03 \x01(\x0b\x32\x08.Integer\x12\x18\n\x0b\x64\x65scription\x18\x04 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"|\n\x0fPropertyFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x11\n\tproperty_\x18\x02 \x01(\t\x12\x13\n\x06\x61\x63\x63\x65ss\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x04 \x01(\tH\x01\x88\x01\x01\x42\t\n\x07_accessB\x0e\n\x0c_description\"\x7f\n\x0eRangeStatement\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03min\x18\x02 \x01(\x04\x12\x0b\n\x03max\x18\x03 \x01(\x04\x12\x1b\n\x05\x63hild\x18\x04 \x01(\x0b\x32\x0c.FeatureNode\x12\x18\n\x0b\x64\x65scription\x18\x05 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"U\n\x0cRegexFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05regex\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"\x90\x01\n\x0eResultDocument\x12\x17\n\x04meta\x18\x01 \x01(\x0b\x32\t.Metadata\x12)\n\x05rules\x18\x02 \x03(\x0b\x32\x1a.ResultDocument.RulesEntry\x1a:\n\nRulesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1b\n\x05value\x18\x02 \x01(\x0b\x32\x0c.RuleMatches:\x02\x38\x01\"`\n\x0bRuleMatches\x12\x1b\n\x04meta\x18\x01 \x01(\x0b\x32\r.RuleMetadata\x12\x0e\n\x06source\x18\x02 \x01(\t\x12$\n\x07matches\x18\x03 \x03(\x0b\x32\x13.Pair_Address_Match\"\x8a\x02\n\x0cRuleMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x0f\n\x07\x61uthors\x18\x03 \x03(\t\x12\x15\n\x05scope\x18\x04 \x01(\x0e\x32\x06.Scope\x12\x1b\n\x06\x61ttack\x18\x05 \x03(\x0b\x32\x0b.AttackSpec\x12\x15\n\x03mbc\x18\x06 \x03(\x0b\x32\x08.MBCSpec\x12\x12\n\nreferences\x18\x07 \x03(\t\x12\x10\n\x08\x65xamples\x18\x08 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12\x0b\n\x03lib\x18\n \x01(\x08\x12\x1b\n\x04maec\x18\x0b \x01(\x0b\x32\r.MaecMetadata\x12\x18\n\x10is_subscope_rule\x18\x0c \x01(\x08\"A\n\x06Sample\x12\x0b\n\x03md5\x18\x01 \x01(\t\x12\x0c\n\x04sha1\x18\x02 \x01(\t\x12\x0e\n\x06sha256\x18\x03 \x01(\t\x12\x0c\n\x04path\x18\x04 \x01(\t\"Y\n\x0eSectionFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07section\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"V\n\rSomeStatement\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\r\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"\xbc\x01\n\rStatementNode\x12\x0c\n\x04type\x18\x01 \x01(\t\x12 \n\x05range\x18\x02 \x01(\x0b\x32\x0f.RangeStatementH\x00\x12\x1e\n\x04some\x18\x03 \x01(\x0b\x32\x0e.SomeStatementH\x00\x12&\n\x08subscope\x18\x04 \x01(\x0b\x32\x12.SubscopeStatementH\x00\x12&\n\x08\x63ompound\x18\x05 \x01(\x0b\x32\x12.CompoundStatementH\x00\x42\x0b\n\tstatement\"W\n\rStringFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06string\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"b\n\x11SubscopeStatement\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x15\n\x05scope\x18\x02 \x01(\x0e\x32\x06.Scope\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"]\n\x10SubstringFeature\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x11\n\tsubstring\x18\x02 \x01(\t\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x0e\n\x0c_description\"&\n\tAddresses\x12\x19\n\x07\x61\x64\x64ress\x18\x01 \x03(\x0b\x32\x08.Address\"F\n\x12Pair_Address_Match\x12\x19\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x08.Address\x12\x15\n\x05match\x18\x02 \x01(\x0b\x32\x06.Match\"7\n\x0cToken_Offset\x12\x17\n\x05token\x18\x01 \x01(\x0b\x32\x08.Integer\x12\x0e\n\x06offset\x18\x02 \x01(\x04\",\n\x07Integer\x12\x0b\n\x01u\x18\x01 \x01(\x04H\x00\x12\x0b\n\x01i\x18\x02 \x01(\x12H\x00\x42\x07\n\x05value\"8\n\x06Number\x12\x0b\n\x01u\x18\x01 \x01(\x04H\x00\x12\x0b\n\x01i\x18\x02 \x01(\x12H\x00\x12\x0b\n\x01\x66\x18\x03 \x01(\x01H\x00\x42\x07\n\x05value*\xcb\x01\n\x0b\x41\x64\x64ressType\x12\x1b\n\x17\x41\x44\x44RESSTYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x41\x44\x44RESSTYPE_ABSOLUTE\x10\x01\x12\x18\n\x14\x41\x44\x44RESSTYPE_RELATIVE\x10\x02\x12\x14\n\x10\x41\x44\x44RESSTYPE_FILE\x10\x03\x12\x18\n\x14\x41\x44\x44RESSTYPE_DN_TOKEN\x10\x04\x12\x1f\n\x1b\x41\x44\x44RESSTYPE_DN_TOKEN_OFFSET\x10\x05\x12\x1a\n\x16\x41\x44\x44RESSTYPE_NO_ADDRESS\x10\x06*G\n\x06\x46lavor\x12\x16\n\x12\x46LAVOR_UNSPECIFIED\x10\x00\x12\x11\n\rFLAVOR_STATIC\x10\x01\x12\x12\n\x0e\x46LAVOR_DYNAMIC\x10\x02*\xa5\x01\n\x05Scope\x12\x15\n\x11SCOPE_UNSPECIFIED\x10\x00\x12\x0e\n\nSCOPE_FILE\x10\x01\x12\x12\n\x0eSCOPE_FUNCTION\x10\x02\x12\x15\n\x11SCOPE_BASIC_BLOCK\x10\x03\x12\x15\n\x11SCOPE_INSTRUCTION\x10\x04\x12\x11\n\rSCOPE_PROCESS\x10\x05\x12\x10\n\x0cSCOPE_THREAD\x10\x06\x12\x0e\n\nSCOPE_CALL\x10\x07\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'capa.render.proto.capa_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MATCH_CAPTURESENTRY._options = None
  _MATCH_CAPTURESENTRY._serialized_options = b'8\001'
  _RESULTDOCUMENT_RULESENTRY._options = None
  _RESULTDOCUMENT_RULESENTRY._serialized_options = b'8\001'
  _ADDRESSTYPE._serialized_start=6032
  _ADDRESSTYPE._serialized_end=6235
  _FLAVOR._serialized_start=6237
  _FLAVOR._serialized_end=6308
  _SCOPE._serialized_start=6311
  _SCOPE._serialized_end=6476
  _APIFEATURE._serialized_start=32
  _APIFEATURE._serialized_end=113
  _ADDRESS._serialized_start=115
  _ADDRESS._serialized_end=223
  _ANALYSIS._serialized_start=226
  _ANALYSIS._serialized_end=454
  _ARCHFEATURE._serialized_start=456
  _ARCHFEATURE._serialized_end=539
  _ATTACKSPEC._serialized_start=541
  _ATTACKSPEC._serialized_end=637
  _BASICBLOCKFEATURE._serialized_start=639
  _BASICBLOCKFEATURE._serialized_end=714
  _BASICBLOCKLAYOUT._serialized_start=716
  _BASICBLOCKLAYOUT._serialized_end=761
  _BYTESFEATURE._serialized_start=763
  _BYTESFEATURE._serialized_end=848
  _CHARACTERISTICFEATURE._serialized_start=850
  _CHARACTERISTICFEATURE._serialized_end=953
  _CLASSFEATURE._serialized_start=955
  _CLASSFEATURE._serialized_end=1041
  _COMPOUNDSTATEMENT._serialized_start=1043
  _COMPOUNDSTATEMENT._serialized_end=1118
  _EXPORTFEATURE._serialized_start=1120
  _EXPORTFEATURE._serialized_end=1207
  _FEATURECOUNTS._serialized_start=1209
  _FEATURECOUNTS._serialized_end=1280
  _FEATURENODE._serialized_start=1283
  _FEATURENODE._serialized_end=2170
  _FORMATFEATURE._serialized_start=2172
  _FORMATFEATURE._serialized_end=2259
  _FUNCTIONFEATURECOUNT._serialized_start=2261
  _FUNCTIONFEATURECOUNT._serialized_end=2325
  _FUNCTIONLAYOUT._serialized_start=2327
  _FUNCTIONLAYOUT._serialized_end=2419
  _FUNCTIONNAMEFEATURE._serialized_start=2421
  _FUNCTIONNAMEFEATURE._serialized_end=2521
  _IMPORTFEATURE._serialized_start=2523
  _IMPORTFEATURE._serialized_end=2611
  _LAYOUT._serialized_start=2613
  _LAYOUT._serialized_end=2657
  _LIBRARYFUNCTION._serialized_start=2659
  _LIBRARYFUNCTION._serialized_end=2717
  _MBCSPEC._serialized_start=2719
  _MBCSPEC._serialized_end=2808
  _MAECMETADATA._serialized_start=2811
  _MAECMETADATA._serialized_end=2965
  _MATCH._serialized_start=2968
  _MATCH._serialized_end=3226
  _MATCH_CAPTURESENTRY._serialized_start=3159
  _MATCH_CAPTURESENTRY._serialized_end=3218
  _MATCHFEATURE._serialized_start=3228
  _MATCHFEATURE._serialized_end=3313
  _METADATA._serialized_start=3316
  _METADATA._serialized_end=3455
  _MNEMONICFEATURE._serialized_start=3457
  _MNEMONICFEATURE._serialized_end=3548
  _NAMESPACEFEATURE._serialized_start=3550
  _NAMESPACEFEATURE._serialized_end=3643
  _NUMBERFEATURE._serialized_start=3645
  _NUMBERFEATURE._serialized_end=3741
  _OSFEATURE._serialized_start=3743
  _OSFEATURE._serialized_end=3822
  _OFFSETFEATURE._serialized_start=3824
  _OFFSETFEATURE._serialized_end=3921
  _OPERANDNUMBERFEATURE._serialized_start=3923
  _OPERANDNUMBERFEATURE._serialized_end=4050
  _OPERANDOFFSETFEATURE._serialized_start=4052
  _OPERANDOFFSETFEATURE._serialized_end=4179
  _PROPERTYFEATURE._serialized_start=4181
  _PROPERTYFEATURE._serialized_end=4305
  _RANGESTATEMENT._serialized_start=4307
  _RANGESTATEMENT._serialized_end=4434
  _REGEXFEATURE._serialized_start=4436
  _REGEXFEATURE._serialized_end=4521
  _RESULTDOCUMENT._serialized_start=4524
  _RESULTDOCUMENT._serialized_end=4668
  _RESULTDOCUMENT_RULESENTRY._serialized_start=4610
  _RESULTDOCUMENT_RULESENTRY._serialized_end=4668
  _RULEMATCHES._serialized_start=4670
  _RULEMATCHES._serialized_end=4766
  _RULEMETADATA._serialized_start=4769
  _RULEMETADATA._serialized_end=5035
  _SAMPLE._serialized_start=5037
  _SAMPLE._serialized_end=5102
  _SECTIONFEATURE._serialized_start=5104
  _SECTIONFEATURE._serialized_end=5193
  _SOMESTATEMENT._serialized_start=5195
  _SOMESTATEMENT._serialized_end=5281
  _STATEMENTNODE._serialized_start=5284
  _STATEMENTNODE._serialized_end=5472
  _STRINGFEATURE._serialized_start=5474
  _STRINGFEATURE._serialized_end=5561
  _SUBSCOPESTATEMENT._serialized_start=5563
  _SUBSCOPESTATEMENT._serialized_end=5661
  _SUBSTRINGFEATURE._serialized_start=5663
  _SUBSTRINGFEATURE._serialized_end=5756
  _ADDRESSES._serialized_start=5758
  _ADDRESSES._serialized_end=5796
  _PAIR_ADDRESS_MATCH._serialized_start=5798
  _PAIR_ADDRESS_MATCH._serialized_end=5868
  _TOKEN_OFFSET._serialized_start=5870
  _TOKEN_OFFSET._serialized_end=5925
  _INTEGER._serialized_start=5927
  _INTEGER._serialized_end=5971
  _NUMBER._serialized_start=5973
  _NUMBER._serialized_end=6029
# @@protoc_insertion_point(module_scope)
