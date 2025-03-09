from django.shortcuts import render,get_object_or_404
import requests
from django.db.models import Count
from django.http import JsonResponse
from home.models import ContactMessage,Project,Post,Education,Experience,Skill,Category,Tag
# Create your views here.
def home(request):
    context={'success':'home','name':'','projects':'','posts':''}
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        if name and email and subject and message:
            contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
            contact_message.save()
            context['success']='submitted'
            context['name']=name
        else:
            context['success']='error'
        # return render(request, 'index.html')
    projects = Project.objects.all()
    educations=Education.objects.all()
    Experiences=Experience.objects.all()
    Skills=Skill.objects.all()


    context['projects']=projects
    context['educations']=educations
    context['Experiences']=Experiences
    context['skills']=Skills

    blogs =  Post.objects.order_by('-created_on')[:3]
    context['posts']=blogs
    return render(request, 'index.html',context)

def chat(request):
    bot_message=""
    if request.method == "POST":
        print("asdasdasdas")
        user_message = request.POST.get('chat-input', '')
        
        api_key = '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'
        api_url = 'https://api.openai.com/v1/your-api-endpoint'

        # Set up the API request payload.
        payload = {
            'model': 'text-davinci-002',
            'prompt': user_message,
            'max_tokens': 50,
        }

        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
        }

        try:
            # Make the API request.
            response = requests.post(api_url, json=payload, headers=headers)
            response_data = response.json()
            bot_message = response_data['choices'][0]['text']
            print(JsonResponse({'response': bot_message}))
            return JsonResponse({'response': bot_message})

        except Exception as e:
            print(JsonResponse({'response': bot_message}))
            return JsonResponse({'error': str(e)})
    print(JsonResponse({'response': bot_message}))
    # return JsonResponse({'error': 'Invalid request method'})
    return render(request, 'chat.html')

def blog_post(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    tags = blog.tags.all()
    categories = Category.objects.annotate(blog_count=Count('post'))
    all_tags=Tag.objects.all()
    blogs =  Post.objects.order_by('-created_on')[:5]
    return render(request, 'blog_post.html', {'blog': blog,'posts':blogs,'tags':tags,'categories':categories,'allTags':all_tags})

def project_detail(request, project_id):
    # Retrieve the project from the database using get_object_or_404
    project = get_object_or_404(Project, pk=project_id)
    projects =  Project.objects.order_by('name')[:5]

    # Render the template with the project data
    return render(request, 'project.html', {'project': project,'projects':projects})

def blog_result(request ):
    blogs = Post.objects.all()
    # tags = blog.tags.all()

    # categories = Category.objects.annotate(blog_count=Count('post'))
    # all_tags=Tag.objects.all()
    # blogs =  Post.objects.order_by('-created_on')[:5]
    return render(request, 'blog_results.html', {'posts':blogs,'title':"Our"})

def category_blogs(request, category_id):
    # Get the selected category
    category = get_object_or_404(Category, id=category_id)

    # Get all blogs in the selected category
    posts = category.post_set.all()

    return render(request, 'blog_results.html', {'posts': posts,'title':category})

def tags_blogs(request, tags_id):
    # Get the selected tag
    tags = get_object_or_404(Tag, id=tags_id)

    # Get all blogs in the selected tags
    posts = tags.post_set.all()

    return render(request, 'blog_results.html', {'posts': posts,'title':tags})


