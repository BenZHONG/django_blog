import markdown

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post, Category
from comments.forms import  CommentForm


class IndexView(ListView):
    """
    要写一个类视图，首先需要继承 Django 提供的某个类视图。至于继承哪个类视图，需要根据你的视图功能而定。
    比如这里 IndexView 的功能是从数据库中获取文章（Post）列表，ListView 就是从数据库中获取某个模型列表数据的，
    所以 IndexView 继承 ListView。
    """
    # 要获取的模型是 Post。
    model = Post
    # 指定这个视图渲染的模板
    template_name = 'blog/index.html'
    # 指定获取的模型列表数据保存的变量名。这个变量会被传递给模板
    context_object_name = 'post_list'


# class CategoryView(ListView):
#     """
#     category 视图函数的功能也是从数据库中获取文章列表数据，不过其和 index 视图函数不同的是，它获取的是某个分类下的全部文章。
#     因此 category 视图函数中多了一步，即首先需要根据从 URL 中捕获的分类 id 并从数据库获取分类，
#     然后使用 filter 函数过滤出该分类下的全部文章。
#     """
#     model = Post
#     template_name = 'blog/index.html'
#     context_object_name = 'post_list'
#
#     # 覆写了父类的 get_queryset 方法。该方法默认获取指定模型的全部列表数据。
#     # 为了获取指定分类下的文章列表数据，我们覆写该方法，改变它的默认行为。
#     def get_queryset(self):
#         cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
#         return super((CategoryView, self).get_queryset().filter(category=cate))


class CategoryView(IndexView):
    """
    CategoryView 类中指定的属性值和 IndexView 中是一模一样的，所以可以直接继承 IndexView
    """

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super((CategoryView, self).get_queryset().filter(category=cate))


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    # 其作用是如果用户访问的详细不存在，则返回一个 404 错误页面以提示用户访问的资源不存在。
    post = get_object_or_404(Post, pk=pk)

    # 阅读量 +1
    # 当用户请求访问某篇文章时，处理该请求的视图函数为 detail 。
    # 一旦该视图函数被调用，说明文章被访问了一次，因此我们修改 detail 视图函数，让被访问的文章在视图函数被调用时阅读量 +1。
    post.increase_views()

    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk) # 其作用是如果用户访问的分类不存在，则返回一个 404 错误页面以提示用户访问的资源不存在。
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


