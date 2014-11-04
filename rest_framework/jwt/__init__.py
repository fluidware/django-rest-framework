from datetime import datetime
from calendar import timegm
from base64 import urlsafe_b64encode
from os import urandom

from django.conf import settings
from itsdangerous import URLSafeSerializer


SECRET_KEY = settings.SECRET_KEY


def generate_jwt(claims, lifetime=None, expires=None, not_before=None):
    """
    Generate a JSON Web Token.

    - **exp** (*IntDate*) -- The UTC expiry date and time of the token, in number of seconds from 1970-01-01T0:0:0Z UTC.
    - **iat** (*IntDate*) -- The UTC date and time at which the token was generated.
    - **nbf** (*IntDate*) -- The UTC valid-from date and time of the token.
    - **jti** (*str*) -- A unique identifier for the token.
    """
    claims = dict(claims)

    now = datetime.utcnow()

    claims['iat'] = timegm(now.utctimetuple())
    claims['nbf'] = timegm((not_before or now).utctimetuple())
    claims['jti'] = urlsafe_b64encode(urandom(128))

    if lifetime:
        claims['exp'] = timegm((now + lifetime).utctimetuple())
    elif expires:
        claims['exp'] = timegm(expires.utctimetuple())

    signer = URLSafeSerializer(SECRET_KEY)

    return signer.dumps(claims)
