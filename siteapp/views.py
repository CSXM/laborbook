from django.shortcuts import render

from django.http import HttpResponse

from models import Skill, SkillLevelType, Category

# Create your views here.
def site_index(request):
    index_str = "<body><h2>Laborbook</h2>Implement your own views!<br>Look at the source code.<br><br>"

    # This is a hack to automatically load test views into the index page
    index_str += "Some test views to try:<br>"
    for t_view in getTestViews():
        for link in t_view['links']:
            index_str += '<a href="http://localhost:8000/%s">%s</a><br>' % (link, link)

    index_str += "</body>"
    return HttpResponse(index_str)

# Test views to automatically show in main page should have docstring in format:
# ^expression_to_page, link_after_localhost
def test_view(request, some_id):
    """^(?P<some_id>\d+), 12345"""
    return HttpResponse("TNumber: %s" % str(some_id))

def testing(request):
    """^testing, testing"""
    sk = Skill.objects.filter(skill_level_type=SkillLevelType.objects.all()[0])[1]
    return HttpResponse("Testing skill: <br><br>%s " % sk.getSkillHTML())

def testing2(request):
    """^testing2, testing2"""
    category = Category.objects.all()[1]
    return HttpResponse("Testing category: <br><br>%s " % category.getCategoryHTML())

def testing3(request):
    """^testing3, testing3"""
    root_category = Category.objects.filter(is_root=True)[0]
    category_tree = getCategoryTree(root_category)

    return HttpResponse("Testing category tree: <br><br>%s " % str(category_tree))

def testing4(request):
    """^testing4, testing4"""
    category = Category.objects.filter(is_root=True)[0]
    return HttpResponse(category.getCategoryHTML(test=True))
    # return HttpResponse("Testing category: <br><br>%s" % category.getCategoryHTML())

# TODO: Will this be obsolete/not needed?
def getCategoryTree(base_category):
    tree = {base_category.id: []}
    for category in base_category.getSubcategories():
        tree[base_category.id].append(getCategoryTree(category))
        tree[base_category.id].append([s.name for s in category.getSkills()])
    return tree


def getTestViews():
    # Some hack code to automatically put test views into the index view, rest of the hack
    # code is in urls.py
    from sys import modules

    names = dir(modules['siteapp.views'])
    names.sort()
    names.reverse()
    names = [x for x in names if not x.startswith('__')]
    test_views = []
    for name in names:
        try:
            n = getattr(modules['siteapp.views'], name)
            if n.__doc__.startswith('^'):
                doc_split = n.__doc__.split(',')
                url_string = doc_split[0].strip()
                links = [x.strip() for x in doc_split[1:]]
                test_views.append({'name': name, 'url_string': url_string, 'links': links})
        except Exception, e:
            print e

    return test_views