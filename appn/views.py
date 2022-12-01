from django.db.models.query import QuerySet
from rest_framework import serializers
from appn.models import Course, CourseSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework .viewsets import ViewSet,ModelViewSet
from rest_framework import status
from django.http import Http404
#mixins
from rest_framework import mixins,generics
class CourseListView(ModelViewSet):
    queryset=Course.objects.all()
    print("queryset","hii")
    serializer_class=CourseSerializer
    
    
    
    
    
'''
class CourseListView(ViewSet):
    def list(self,request):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses,many=True)
        return Response(serializer.data)
    def create(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors)
    def retrieve(self,request,pk):
        try:
            course=Course.objects.get(pk=pk)
            serializer=CourseSerializer(course)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    


class CourseListView(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class CourseDetailView(generics.RetrieveDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
 
(generics.RetrieveUpdateAPIView
class CourseListView(generics.CreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class CourseDetailView(generics.DestroyAPIView,generics.UpdateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    '''  
#generics.RetrieveAPIView
'''
class CourseListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
     
class CourseDetailView(generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def put(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)



class CourseListView(APIView):
    def get(self,request):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():         
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)
class CourseDetailView(APIView):
    def get_course(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404             
    def get(self,request,pk):
        course=self.get_course(pk)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    def put(self,request,pk):
        course=self.get_course(pk)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
    def delete(self,request,pk):
        course=self.get_course(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
'''
