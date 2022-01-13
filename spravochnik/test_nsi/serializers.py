from rest_framework import serializers


class DictionarySerializer(serializers.Serializer):
    identifier = serializers.CharField(source='sprid')
    name = serializers.CharField()
    s_name = serializers.CharField(source='shortname')
    description = serializers.CharField()
    version = serializers.CharField()
    datefrom = serializers.DateField()
    dateto = serializers.DateField()


class DictionaryItemSerializer(serializers.Serializer):
    identifier = serializers.CharField(source='id')
    dict_id = serializers.CharField(source='dictionary_id')
    parent_id = serializers.IntegerField()
    item_code = serializers.CharField()
    item_value = serializers.CharField()
