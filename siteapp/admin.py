from django.contrib import admin

from siteapp.models import Category, SkillLevelType, SkillLevel, Skill, UserSkillLevel

admin.site.register(Category)
admin.site.register(SkillLevelType)
admin.site.register(SkillLevel)
admin.site.register(Skill)
admin.site.register(UserSkillLevel)
