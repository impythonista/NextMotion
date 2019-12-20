from django.conf import settings
from django.core.mail import send_mail

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Invitation
from invitation_app.serializers import InvitationSerializer, InvitationCreateSerializer, InvitationPatchSerializer


class InvitationModelViewSet(viewsets.ModelViewSet):
    """
    It's the invitation api, it's perform the operation of creat, update, delete and list invitation.
    below are the endpoints of the api.

        GET api/invitations/ List all the invitations (with pagination) 
        POST api/invitations/ Create an invitation
        PATCH api/invitations/<id>/ Modify the invitation with the given id
        DELETE api/invitations/<id>/ Delete the invitation with the given id
    
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer


    def create(self, request):
        serializer = InvitationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        invitation = serializer.save(creator=self.request.user)

        send_mail(
            'Sample Invitaiton email',
            "It's the sample  email invitation email.",
            settings.EMAIL_HOST_USER,
            [invitation.email,],
            fail_silently=False,
        )
        
        response = self.serializer_class(invitation)
        return Response({
            'status' : status.HTTP_201_CREATED,
            'message' : 'Successfully created invitation.',
            'data' : response.data
        })

    def partial_update(self, request, pk=None):
        try:
            invitation = Invitation.objects.get(id=pk)
        except Invitation.DoesNotExist as e:
            invitation = None
        
        if invitation:
            serializer = InvitationPatchSerializer(data=request.data, instance=invitation)
            serializer.is_valid(raise_exception=True)
            invitation = serializer.save()

            send_mail(
                'Sample Patched Invitaiton email',
                "It's the sample  patched email invitation.",
                settings.EMAIL_HOST_USER,
                [invitation.email,],
                fail_silently=False,
            )
            
            response = self.serializer_class(invitation)
            return Response({
                'status' : status.HTTP_200_OK,
                'message' : 'Successfully updated invitation.',
                'data' : response.data
            })
        else:
            return Response({
                'status' : status.HTTP_404_NOT_FOUND,
                'message' : 'Not found.',
            })

