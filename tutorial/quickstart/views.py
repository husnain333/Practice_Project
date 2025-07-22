from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer
from django.shortcuts import get_object_or_404
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all() 
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]  

class GroupList(generics.ListAPIView):
    queryset = Group.objects.all().order_by('id')  # Added ordering to avoid pagination warning
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]  

    

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    multiple_lookup_fields = ['id', 'username']
    def get_object(self):
        queryset = self.get_queryset()
        print("Queryset:", queryset)
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj
    
   
    
class AddUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                self.perform_create(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({
                    'error': 'Username already exists.'
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class userdetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class destroy(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

class UpdateUserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    lookup_field = 'username'
    
class DeleteUserView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

class multipleFieldLookupMixin:
    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter={}
        for field in self.lookup_fields:
            if self.kwargs.get(field): 
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter) 
        self.check_object_permissions(self.request, obj)
        return obj

class RetrieveUserView(multipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ['username', 'email']
    permission_classes = [AllowAny]
