from django.contrib import admin
from .models import (
    UserProfile,
    ContactProfile,
    Testimonial,
    Media,
    Portfolio,
    Blog,
    Certificate,
    Skill,
    Experience,
    FooterDetail
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'worked_at', 'start', 'end', 'summary')


@admin.register(FooterDetail)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('id', 'facebook', 'instagram', 'twitter', 'linkedin')
