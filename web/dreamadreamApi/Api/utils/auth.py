from datetime import datetime, timedelta

from oauth2_provider.admin import Application
from oauth2_provider.models import AccessToken, RefreshToken
from oauth2_provider.settings import oauth2_settings
from oauthlib.oauth2.rfc6749.tokens import random_token_generator


def get_token(request, user, application_name):
    expire_seconds = oauth2_settings.user_settings['ACCESS_TOKEN_EXPIRE_SECONDS']
    scopes = oauth2_settings.user_settings['SCOPES']

    application = Application.objects.get(name=application_name)
    expires = datetime.now() + timedelta(seconds=expire_seconds)
    access_token = AccessToken.objects.create(
                    user=user,
                    application=application,
                    token=random_token_generator(request),
                    expires=expires,
                    scope=scopes)

    refresh_token = RefreshToken.objects.create(
                    user=user,
                    token=random_token_generator(request),
                    access_token=access_token,
                    application=application)

    token = {
        'access_token': access_token.token,
        'token_type': 'Bearer',
        'expires_in': expire_seconds,
        'refresh_token': refresh_token.token,
        'scope': scopes
    }

    return token


def refresh_auth_token(request, refresh_token, user, application_name):

    # Allow Auth Token Generation only if refresh_token found in RefreshToken

    expire_seconds = oauth2_settings.user_settings['ACCESS_TOKEN_EXPIRE_SECONDS']
    scopes = oauth2_settings.user_settings['SCOPES']

    application = Application.objects.get(name=application_name)
    expires = datetime.now() + timedelta(seconds=expire_seconds)
    try:
        r = RefreshToken.objects.get(token=refresh_token)

        # Remove refresh_token and it's access_token
        r.revoke()

        # Generate new refresh_token
        access_token = AccessToken.objects.create(
            user=user,
            application=application,
            token=random_token_generator(request, refresh_token=True),
            expires=expires,
            scope=scopes)

        refresh_token = RefreshToken.objects.create(
            user=user,
            token=random_token_generator(request),
            access_token=access_token,
            application=application)

        token = {
            'access_token': access_token.token,
            'token_type': 'Bearer',
            'expires_in': expire_seconds,
            'refresh_token': refresh_token.token,
            'scope': scopes
        }

        return token
    except RefreshToken.DoesNotExist as e:
        print("RefreshToken Not found")
        return None
    except Exception as e:
        print("Auth exception")
        return None
