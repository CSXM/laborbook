from django.shortcuts import render

from django.http import HttpResponse

from models import Skill, SkillLevelType, Category

# Create your views here.
def site_index(request):
    return HttpResponse("<body><h2>Laborbook</h2>Implement your own views!<br>Look at the source code.</body>")

def test_view(request, some_id):
    return HttpResponse("TNumber: %s" % str(some_id))

def testing(request):
    sk = Skill.objects.filter(skill_level_type=SkillLevelType.objects.all()[0])[1]
    return HttpResponse("Testing skill: <br><br>%s " % sk.getSkillHTML())

def testing2(request):
    category = Category.objects.all()[1]
    return HttpResponse("Testing category: <br><br>%s " % category.getCategoryHTML())

def testing3(request):
    root_category = Category.objects.filter(is_root=True)[0]
    category_tree = getCategoryTree(root_category)

    return HttpResponse("Testing category tree: <br><br>%s " % str(category_tree))

def testing4(request):
    category = Category.objects.filter(is_root=True)[0]
    return HttpResponse("<body>Testing category: <br><br>%s </body>" % category.getCategoryHTML())

# TODO: Will this be obsolete/not needed?
def getCategoryTree(base_category):
    tree = {base_category.id: []}
    for category in base_category.getSubcategories():
        tree[base_category.id].append(getCategoryTree(category))
        tree[base_category.id].append([s.name for s in category.getSkills()])
    return tree
