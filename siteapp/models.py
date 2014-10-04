from django.db import models
from django.contrib.auth.models import User

from django.template import loader, Context

# There can be basically infinite hierarchy of categories
class Category(models.Model):
    """ A Category for Skills
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    parent_category = models.ForeignKey("self", null=True, blank=True, default=None)
    is_root = models.BooleanField(default=False)

    def getSkills(self):
        return Skill.objects.filter(category__id=self.id).order_by('name')

    def getSubcategories(self):
        return Category.objects.filter(parent_category__id=self.id).order_by('name')

    def getCategoryHTML(self, level=1, traverse=True, hide_top_level=False, test=False):
        template = loader.get_template('siteapp/category.html')
        context = Context(
            {
                'name': self.name,
                'skills': self.getSkills(),
                'subcategories': self.getSubcategories(),
                'level': level,
                'next_level': level + 1,
                'traverse': traverse,
                'hide_top_level': hide_top_level, # FIXME: Implement logic
                'test': test,
            }
        )
        return template.render(context)

    def __unicode__(self):
        return self.name

# Used to map certain type of skill levels to skills
# E.g. "Numeric", "String", "Grade", ...
class SkillLevelType(models.Model):
    """ Type of Skill Levels.
    """
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

# Levels per level type
class SkillLevel(models.Model):
    """ Level of the skill
    """
    level = models.CharField(max_length=50)
    skill_level_type = models.ForeignKey(SkillLevelType)

    def __unicode__(self):
        return self.level

# Skills. Can be under any category,
# Each skill should determine which type of level can be defined for it
class Skill(models.Model):
    """ Skill. Belongs to a category. Specifies type of skill levels. May have a description.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    skill_level_type = models.ForeignKey(SkillLevelType)
    category = models.ForeignKey(Category)

    def getValidLevels(self):
        return SkillLevel.objects.filter(skill_level_type__id = self.skill_level_type.id)

    def getLevelsHTMLDropDownList(self):
        template = loader.get_template('siteapp/levels.html')
        context = Context(
            {
                'levels_type': self.skill_level_type.name, # For html class
                'levels': self.getValidLevels()
            })
        return template.render(context)

    def getSkillHTML(self, select_function_name='function_name'):
        template = loader.get_template('siteapp/skill.html')
        context = Context(
            {
                'skill': self,
                'select_function_name': select_function_name,
                'level_dropdownbox_html': self.getLevelsHTMLDropDownList()
            }
        )
        return template.render(context)

    def __unicode__(self):
        return self.name

# Map skills and their levels for user
class UserSkillLevel(models.Model):
    user = models.ForeignKey(User)
    skill = models.ForeignKey(Skill)
    level = models.ForeignKey(SkillLevel)

    def __unicode__(self):
        return "Skill level for user '%s'" % str(self.user.username)

