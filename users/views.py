from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from users.models import User
from users.serializers import UserSerializer,RoleChangeSerializer
from rest_framework.decorators import action
from api.permissions import IsAdminOnly



class ChangeUserRoleView(ModelViewSet):
    """
   API endpoint for managing Role in the online school
     - Allow authenticated  admin to change role
     - Allows only admin can view every user role
    
   """

    queryset = User.objects.all()
    serializer_class = RoleChangeSerializer
    permission_classes = [IsAdminOnly]
    http_method_names = ['get','put']

    @action(detail=True, methods=['put'])
    def change_role(self,request,pk=None):
        user = self.get_object()
        new_role = request.data.get('role')
        if new_role not in dict(User.ROLE_CHOICES):
            return Response({'error':'invalid role'},status=status.HTTP_400_BAD_REQUEST)
        
        old_role = user.role 
        user.role = new_role
        user.save()
        return Response({"message": f"{user.first_name} {old_role} changed to {new_role}"}, status=status.HTTP_200_OK)

   
        
