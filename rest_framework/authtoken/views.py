from rest_framework.views import APIView
from rest_framework import parsers
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.authtoken.models import APIKey
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import jwt


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    model = APIKey

    def post(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            token, created = APIKey.objects.get_or_create(user=serializer.object['user'])
            return Response({'user': serializer.object['user'].username, 'apikey': token.key, 'email': serializer.object['email']})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObtainTestJWTToken(APIView):

    renderer_classes = (renderers.JSONRenderer,)

    def get(self, request):
        claims = {'user_id': '4'}
        token = jwt.generate_jwt(claims)
        return Response({'token': token})


obtain_jwt = ObtainTestJWTToken.as_view()
obtain_auth_token = ObtainAuthToken.as_view()
