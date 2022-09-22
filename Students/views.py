# Create all of the endpoints
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def student_list(request):
    # get all the students
    # Serialize them
    # return json
    
    if request.method == 'GET':
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse({'student':serializer.data}, safe= False)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def student_id(request,id):

    try:
        stu = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(stu)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(stu,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors, status = status.HTTP_404_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        stu.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)