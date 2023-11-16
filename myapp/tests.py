import pytest

from helpers.tests import BaseModelTest, BaseModelFieldTest, BaseTestFieldRelated
from myapp.models import UserProfile

from django.contrib.auth.models import User

from django.db import models


class BaseTestUserProfile:
    model = UserProfile


class TestModelUserProfile(BaseTestUserProfile, BaseModelTest):
    model = UserProfile

    @pytest.mark.django_db
    def test_has_all_attributes(self, instance):
        assert hasattr(instance, 'user')
        assert hasattr(instance, 'bio')
        assert hasattr(instance, 'profile_picture')
        assert hasattr(instance, 'settings')

        assert hasattr(instance, "change_theme_preference")
        assert hasattr(instance, "get_theme_preference")

    @pytest.mark.django_db
    def test_change_theme_preference(self, instance):
        instance.change_theme_preference("dark")
        assert instance.settings["theme"] == "dark"

    @pytest.mark.django_db
    def test_get_theme_preference_should_get_auto_if_not_set(self, instance):
        assert instance.get_theme_preference() == "auto"

    @pytest.mark.django_db
    def test_get_theme_preference_set_in_db(self, instance):
        # Set the theme
        instance.settings["theme"] = "dark"
        instance.save()

        # Assert the value
        assert instance.get_theme_preference() == "dark"


class TestFieldUserProfileBio(BaseModelFieldTest):
    field_name = "bio"
    field_type = models.TextField
    model = UserProfile

    null = True
    blank = True


class TestFieldUserProfileProfilePicture(BaseModelFieldTest):
    field_name = "profile_picture"
    field_type = models.URLField
    model = UserProfile

    null = True
    blank = True


class TestFieldUserProfileSettings(BaseModelFieldTest):
    field_name = "settings"
    field_type = models.JSONField
    model = UserProfile

    default = dict


class TestFieldUserProfileUser(BaseTestFieldRelated):
    field_name = "user"
    field_type = models.OneToOneField
    model = UserProfile

    db_index = True
    unique = True
    related_model = User
