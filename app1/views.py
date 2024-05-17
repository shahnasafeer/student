from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer

class StudentView(APIView):

    def get(self, request):
        result = Students.objects.all()
        serializers = StudentSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class StudentDetailView(APIView):

    def get(self, request, id):
        result = get_object_or_404(Students, id=id)
        serializer = StudentSerializer(result)
        return Response({'status': 'success', "students": serializer.data}, status=200)

    def patch(self, request, id):
        result = get_object_or_404(Students, id=id)
        serializer = StudentSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        result = get_object_or_404(Students, id=id)
        result.delete()
        return Response({"status": "success", "data": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
