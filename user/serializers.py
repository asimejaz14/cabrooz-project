import os

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User, UserWallet, UserLiveLocation, OnlineUser

from Cabrooz_App import settings


class UserWalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserWallet
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    profile_picture = serializers.SerializerMethodField(required=False)
    cnic_front = serializers.SerializerMethodField(required=False)
    cnic_back = serializers.SerializerMethodField(required=False)
    license_front = serializers.SerializerMethodField(required=False)
    license_back = serializers.SerializerMethodField(required=False)
    type_id = serializers.CharField(max_length=200, allow_null=True, allow_blank=True)
    status_id = serializers.CharField(max_length=200, allow_null=True, allow_blank=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

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


    def get_cnic_front(self, obj):
        try:
            if self.context['request'].method == 'POST' or self.context['request'].method == 'PATCH':
                req = self.context['request']
                if req.data.get('cnic_front'):
                    if not os.path.exists("media/users/documents/" + str(req.data.get('cnic_front'))):
                        obj.cnic_front = req.data.get('cnic_front')
                        obj.save()
                        return self.context['request'].build_absolute_uri(obj.cnic_front.url)
                    elif os.path.exists("media/users/profile_images/" + str(req.data.get('cnic_front'))):
                        obj.cnic_front = 'users/profile_images/' + str(req.data.get('cnic_front'))
                        obj.save()
                        return self.context['request'].build_absolute_uri(obj.cnic_front.url)
                else:
                    obj.cnic_front = None
                    obj.save()
            elif self.context['request'].method == 'GET':
                try:
                    return self.context['request'].build_absolute_uri(obj.cnic_front.url)
                except:
                    self.context['request'].build_absolute_uri(obj['cnic_front']['url'])

        except Exception as e:
            print("IMAGE NOT SAVED", e)

    def get_cnic_back(self, obj):
        try:
            if self.context['request'].method == 'POST' or self.context['request'].method == 'PATCH':
                req = self.context['request']
                if req.data.get('cnic_back'):
                    if not os.path.exists("media/users/documents/" + str(req.data.get('cnic_back'))):
                        obj.cnic_back = req.data.get('cnic_back')
                        obj.save()
                        return self.context['request'].build_absolute_uri(obj.cnic_back.url)
                    elif os.path.exists("media/users/documents/" + str(req.data.get('cnic_back'))):
                        obj.cnic_back = 'users/documents/' + str(req.data.get('cnic_back'))
                        obj.save()
                        return self.context['request'].build_absolute_uri(obj.cnic_back.url)
                else:
                    obj.cnic_back = None
                    obj.save()
            elif self.context['request'].method == 'GET':
                try:
                    return self.context['request'].build_absolute_uri(obj.cnic_back.url)
                except:
                    self.context['request'].build_absolute_uri(obj['cnic_back']['url'])

        except Exception as e:
            print("IMAGE NOT SAVED", e)

    def get_license_front(self, obj):
        try:
            if self.context['request'].method == 'POST' or self.context['request'].method == 'PATCH':
                req = self.context['request']
                if req.data.get('license_front'):
                    if not os.path.exists("media/users/documents/" + str(req.data.get('license_front'))):
                        obj.license_front = req.data.get('license_front')
                        obj.save()
                        return self.context['request'].build_absolute_uri(obj.license_front.url)
                    elif os.path.exists("media/users/documents/" + str(req.data.get('license_front'))):
                        obj.license_front = 'users/documents/' + str(req.data.get('license_front'))
                        obj.save()
                        return self.context['request'].build_absolute_uri(obj.license_front.url)
                else:
                    obj.license_front = None
                    obj.save()
            elif self.context['request'].method == 'GET':
                try:
                    return self.context['request'].build_absolute_uri(obj.license_front.url)
                except:
                    self.context['request'].build_absolute_uri(obj['license_front']['url'])

        except Exception as e:
            print("IMAGE NOT SAVED", e)


    def get_license_back(self, obj):
        try:
            if self.context['request'].method == 'POST' or self.context['request'].method == 'PATCH':
                req = self.context['request']
                if req.data.get('license_back'):
                    if not os.path.exists("media/users/documents/" + str(req.data.get('license_back'))):
                        obj.license_back = req.data.get('license_back')
                        obj.save()
                        return self.context['request'].build_absolute_uri(obj.license_back.url)
                    elif os.path.exists("media/users/documents/" + str(req.data.get('license_back'))):
                        obj.license_back = 'users/documents/' + str(req.data.get('license_back'))
                        obj.save()
                        return self.context['request'].build_absolute_uri(obj.license_back.url)
                else:
                    obj.license_back = None
                    obj.save()
            elif self.context['request'].method == 'GET':
                try:
                    return self.context['request'].build_absolute_uri(obj.license_back.url)
                except:
                    self.context['request'].build_absolute_uri(obj['license_back']['url'])

        except Exception as e:
            print("IMAGE NOT SAVED", e)





    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'gender',
            'country',
            'profile_picture',
            'phone_number',
            'username',
            'status_id',
            'type_id',
            'cnic_front',
            'cnic_back',
            'license_front',
            'license_back',
            'password',
        ]


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password', 'user_permissions', 'groups', 'is_staff', 'is_active']


class UserLiveLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLiveLocation
        fields = '__all__'


class OnlineUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = OnlineUser
        fields = '__all__'