from rest_framework import serializers
from notes.apps.account.models import User, UserProfile


class Account(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        user = User(
            e_mail=validated_data['e_mail'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
         instance.e_mail = validated_data.get('e_mail', instance.e_mail)

         instance.save()

         password = validated_data.get('password', None)
         confirm_password = validated_data.get('confirm_password', None)

         if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()

         return instance

    class Meta:
        model = User
        fields = ('id', 'e_mail', 'password', 'confirm_password')


class Profile(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'place', 'state')



