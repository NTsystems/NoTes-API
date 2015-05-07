from rest_framework import serializers
from notes.apps.account.models import User, UserProfile


class UserSerializer(serializers.ModelSerializer):
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


class ProfileSerializer(serializers.ModelSerializer):



    # def create(self, validated_data):
    #
    #     profile = UserProfile(user=self.context['request'].user, **validated_data)
    #     profile.save()
    #     return profile
    #
    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
    #     instance.place = validated_data.get('place', instance.place)
    #     instance.state = validated_data.get('state', instance.state)
    #
    #     instance.save()
    #     return instance

    class Meta:
        model = UserProfile
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'place', 'state')



