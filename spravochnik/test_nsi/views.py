from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Dictionary, DictionaryItem
from .serializers import DictionarySerializer, DictionaryItemSerializer


# Create your views here.


class GetDictionariesInfoView(APIView):
    def get(self, request):
        date1 = request.query_params.get('date', None)
        # Получаем набор всех записей из таблицы Dictionary
        if date1 == None:
            queryset = Dictionary.objects.order_by('sprid').all()
        # Получаем набор всех записей из таблицы Dictionary актуальных на указанную дату
        else:
            queryset = Dictionary.objects.raw(
                'select * from nsi.dictionary where (coalesce(dateto, current_date) > %s or (dateto is null and coalesce(dateto, %s) >= %s)) and datefrom <= %s',
                [date1, date1, date1, date1])
        # Сериализуем извлечённый набор записей
        serializer_for_queryset = DictionarySerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)


class GetDictionaryItemInfoView(APIView):
    def get(self, request):
        dictid = request.query_params.get('id', None)
        vers = request.query_params.get('version', None)
        print(dictid)
        print(vers)
        queryset = None

        if dictid is not None:
            queryset = DictionaryItem.objects.all().filter(dictionary_id__sprid=dictid)
            if vers is not None:
                queryset = queryset.filter(dictionary_id__version=vers) # получение элементов заданного справочника указанной версии
            else:
                queryset = queryset.filter(dictionary_id__dateto__isnull=True) # получение элементов заданного справочника текущей версии

            print(queryset.query)

        serializer_for_queryset = DictionaryItemSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)



