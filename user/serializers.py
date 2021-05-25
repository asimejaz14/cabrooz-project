import os

from rest_framework import serializers
from .models import User

from Cabrooz_App import settings


class UserSerializer(serializers.ModelSerializer):

    profile_picture = serializers.SerializerMethodField(required=False)

    def get_profile_picture(self, obj):
        try:
            if self.context['request'].method == 'POST' or self.context['request'].method == 'PATCH':
                req = self.context['request']
                if req.data.get('image'):
                    if not os.path.exists("media/users/profile_images/" + str(req.data.get('image'))):
                        obj.profile_image = req.data.get('image')
                        obj.save()
                        return self.context['request'].build_absolute_uri(obj.profile_image.url)
                    elif os.path.exists("media/users/profile_images/" + str(req.data.get('image'))):
                        obj.profile_image = 'users/profile_images/' + str(req.data.get('image'))
                        obj.save()
                        return self.context['request'].build_absolute_uri(obj.profile_image.url)
                else:
                    obj.profile_image = None
                    obj.save()
            elif self.context['request'].method == 'GET':
                try:
                    return self.context['request'].build_absolute_uri(obj.profile_image.url)
                except:
                    self.context['request'].build_absolute_uri(obj['profile_image']['url'])

        except Exception as e:
            print("IMAGE NOT SAVED", e)


    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'gender',
            'country',
            'profile_picture',
            'phone_number',
            'username',
            'status',
            'type'
        ]

