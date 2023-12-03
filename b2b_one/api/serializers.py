from rest_framework import routers, serializers, viewsets
from users.models import CustomUser
from tenant.models import Tenant


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):

    # options = serializers.HyperlinkedRelatedField(
    #     view_name='user-detail',
    #     lookup_field = 'email',
    #     many=True,
    #     read_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'company', 'password']
        lookup_field = 'email'


class TenantSerializer(serializers.HyperlinkedModelSerializer):

    # options = serializers.HyperlinkedRelatedField(
    #     view_name='user-detail',
    #     lookup_field = 'email',
    #     many=True,
    #     read_only=True)

    class Meta:
        model = Tenant
        fields = ['company', 'type', 'subdomain_prefix']
        lookup_field = 'email'
