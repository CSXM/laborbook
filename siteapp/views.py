from django.shortcuts import render

from django.http import HttpResponse

from models import Skill, SkillLevelType, Category

# Create your views here.
def site_index(request):
    return HttpResponse("<h2>Laborbook</h2>Implement your own views!<br>Look at the source code.")

# def test_view(request, some_id):
#     return HttpResponse("This id: %s" % str(some_id))
#
# def testing(request):
#     sk = Skill.objects.filter(skill_level_type=SkillLevelType.objects.all()[0])[1]
#     return HttpResponse("Testing skill: <br><br>%s " % sk.getSkillHTML())
#
# def testing2(request):
#     category = Category.objects.all()[1]
#     return HttpResponse("Testing category: <br><br>%s " % category.getCategoryHTML())