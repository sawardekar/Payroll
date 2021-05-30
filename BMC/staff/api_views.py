from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from staff.models import *
from staff import serializers
from django.http import Http404


class EmployeeAPI(APIView):
    """
    APIView define Create/edit/retrieve  Employee
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        """
        GET method to retrieve specific/ALL customer order details.
        :param request:
        :param pk:
        :return:
        """
        if pk:
            emp = self.get_object(pk)
            serializer = serializers.EmployeeSerializer(emp)
        else:
            emp = Employee.objects.all()
            serializer = serializers.EmployeeSerializer(emp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        POST method to Create EMP
        :param request:
        :return:
        """
        mutable = request.POST._mutable
        request.POST._mutable = True
        request.data["created_by"] = request.user.id
        print(">>>>>>data>>>>>",request.data)
        serializer = serializers.EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        PUT method to edit specific Employee details
        :param request:
        :param pk:
        :return:
        """
        if not request.POST._mutable:
            request.POST._mutable = True
        order = self.get_object(pk)
        request.data["edited_by"] = request.user.id
        serializer = serializers.EmployeeSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)