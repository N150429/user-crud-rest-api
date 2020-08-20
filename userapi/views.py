from rest_framework import status

from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import UsersSerializer
from rest_framework.response import Response
from .models import Users

# Create views here.
@api_view(['GET'])
def userapiOverview(request):
	api_urls = {
		'Users':'/users/',
		'Detail View of user':'/user/<str:pk>/',
		'Create':'/user-create/',
		'Update':'/user-update/<str:pk>/',
		'Patch':'/user-patch/<str:pk>',
		'Delete':'/user-delete/<str:pk>/',
	}
	return Response(api_urls)
@api_view(['GET'])
def users(request):
	tasks = Users.objects.all().order_by('-id')
	serializer = UsersSerializer(tasks, many=True)
	return Response(serializer.data)
@api_view(['POST'])
def userCreate(request):
	serializer = UsersSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)
@api_view(['GET'])
def userDetail(request, pk):
	tasks = Users.objects.get(id=pk)
	serializer = UsersSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def userUpdate(request, pk):
	task = Users.objects.get(id=pk)
	serializer = UsersSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)
@api_view(['PATCH'])
def patch(request, pk):
        testmodel_object = Users.objects.get(id=pk)
        serializer = UsersSerializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def userDelete(request, pk):
	task = Users.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')