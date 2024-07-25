from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from todo.models import Todo, Category,Tag
from django.contrib.auth.decorators import login_required


@login_required(login_url="/admin/login/")
def tag_view(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    todos = tag.todo_set.filter(user=request.user)
    context = dict(
           todos = todos,
            tag=tag,
    )
    return render(request, 'todo/todo_list.html',context)

@login_required(login_url="/admin/login/")
def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    todos = Todo.objects.filter(
        category = category,
        is_active=True,
    )
    context = dict(
        category = category,
        todos = todos
    )
    return render(request, 'todo/todo_list.html',context)

@login_required(login_url="/admin/login/")
def home(request):
    #todos = Todo.objects.filter(is_active=True)
    #todos = Todo.objects.filter(is_active=True,title__icontains = "todo")
    #todos = Todo.objects.filter(is_active=False).update(is_active=True)
    #todos = Todo.objects.filter(is_active=True)
    todos = Todo.objects.filter(
        is_active=True,
        user = request.user
    )
    
    contex = dict(
        todos=todos,
    )
    return render(request, 'todo/todo_list.html', contex)

    def __str__(self):
        return self.title
    
@login_required(login_url="/admin/login/")   
def todo_detail(request, id, category_slug):
    # try:
        #  todo =  Todo.objects.get(pk=id)
        #  context = dict(
            #  todo=todo
            #  )
        #  return render(request, 'todo/todo_detail.html', context)
    # except Todo.DoesNotExist:
        # raise Http404

    context = dict(
        todo = get_object_or_404(Todo, pk=id, category__slug=category_slug, user=request.user)
    )
    return render(request, 'todo/todo_detail.html',context)
