from django.http import HttpResponse, JsonResponse
from main.models import Home
from main.serializers import HomeSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


@api_view(["GET", "POST"])
def home_list(request):
    """
    List all homes or create a home
    """

    if request.method == "GET":
        homes = Home.objects.all()
        serializer = HomeSerializer(homes, many=True)

        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = HomeSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def home_detail(request, pk):
    """
    Retrieve a home
    """

    try:
        home = Home.objects.get(pk=pk)
    except Home.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = HomeSerializer(home)

        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
