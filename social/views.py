from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from social.models import FollowUser, MyPost, MyProfile, PostComment, PostLike, PostRating, Friend_Request
from django.views.generic.detail import DetailView
from django.db.models import Q
from social.forms import CommentForm
from django.views.generic.edit import UpdateView, CreateView ,DeleteView
from django.http.response import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect,get_object_or_404
from django.shortcuts import HttpResponse

from accounts.models import ProfcessUser
# Create your views here.

@method_decorator(login_required, name="dispatch")
class HomeView(TemplateView):
    template_name = "social/home.html"
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        followedList = FollowUser.objects.filter(followed_by=self.request.user.myprofile)
        followedList2 = []
        for e in followedList:
            followedList2.append(e.profile)
            print(e.profile)
        postList = MyPost.objects.filter(uploaded_by__in=followedList2).order_by("-id")
        for p1 in postList:
            p1.liked = False
            p1.comments = PostComment.objects.filter(post_by=p1).order_by("-id")
            ob = PostLike.objects.filter(post=p1, liked_by=self.request.user.myprofile)
            if ob:
                p1.liked = True
            obList = PostLike.objects.filter(post=p1)
            p1.likedno = obList.count()
            p1.comment_form = CommentForm()
        
        #Bhavin's Task
        #if post is rated or not 
        for p2 in postList:
            p2.rated = False
            ob = PostRating.objects.filter(post=p2, rate_by=self.request.user.myprofile)
            if ob:
                p2.rated = True
                rc = PostRating.objects.values_list('rate').filter(post=p2,rate_by=self.request.user.myprofile)
                for i in rc:
                    rate_score = i[0]   
                p2.rating_sore = rate_score   

        context["mypost_list"] = postList
        return context;


# @method_decorator(login_required, name="dispatch")
# class HomeView(TemplateView):
#     template_name = "social/home.html"
#
#     def get_context_data(self, **kwargs):
#         context = TemplateView.get_context_data(self, **kwargs)
#         followedList = FollowUser.objects.filter(followed_by=self.request.user.myprofile)
#         followedList2 = []
#         for e in followedList:
#             followedList2.append(e.profile)
#         postList = MyPost.objects.filter(uploaded_by__in=followedList2).order_by("-id")

        # for p1 in postList:
        #     p1.liked = False
        #     ob = PostLike.objects.filter(post=p1, liked_by=self.request.user.myprofile)
        #     if ob:
        #         p1.liked = True
        #     obList = PostLike.objects.filter(post=p1)
        #     p1.likedno = obList.count()
        # context["mypost_list"] = postList
        # return context;



class MyProfilePostListView(ListView):
    model = MyPost
    template_name = 'social/myprofile_detail.html'
    context_object_name = 'mypost_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(MyProfile, user_id = self.kwargs.get('pk'))
        followerList = FollowUser.objects.filter(profile = user)
        followedList = FollowUser.objects.filter(followed_by = user)
        followedList2= []

        for e in followedList:
            followedList2.append(e.profile)
        
        context['following_count'] = followedList2.__len__()
        context['follower_count'] = followerList.__len__()

        context["mypost_list"] = MyPost.objects.filter(uploaded_by = user).order_by('-id')
        return context
    


class AboutView(TemplateView):
    template_name = "social/about.html"

class ContactView(TemplateView):
    template_name = "social/contact.html"

@method_decorator(login_required, name="dispatch")
class MyProfileUpdateView(UpdateView):
    model = MyProfile
    fields = ["age", "address", "status", "gender", "phone_no", "description"]




# @login_required
# def MyProfileUpdateView(request, pk):
#     user = ProfcessUser.objects.get(id=pk)
#     form= UserProfileUpdationForm(instance=request.user.applicantuserprofile)
#     if request.method == "POST":
#         print("hello")
#         form = UserProfileUpdationForm(request.POST, instance= request.user.applicantuserprofile)
#         if form.is_valid():
#             form.save()
#             return render(request, "applicant_app/thanks.html")
#
#     args = {'form': form}
#     return render(request, 'applicant_app/userprofileform.html', args)

@method_decorator(login_required, name="dispatch")
class MyPostCreate(CreateView):
    model = MyPost
    fields = ["subject", "msg", "pic"]
    def form_valid(self, form):
        self.object = form.save()
        self.object.uploaded_by = self.request.user.myprofile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name="dispatch")
class MyPostListView(ListView):
    model = MyPost
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return MyPost.objects.filter(Q(uploaded_by = self.request.user.myprofile)).filter(Q(subject__icontains = si) | Q(msg__icontains = si)).order_by("-id");

@method_decorator(login_required, name="dispatch")
class MyPostDetailView(DetailView):
    model = MyPost

@method_decorator(login_required, name="dispatch")
class MyPostDeleteView(DeleteView):
    model = MyPost

@method_decorator(login_required, name="dispatch")
class MyProfileListView(ListView):
    model = MyProfile
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        #return MyProfile.objects.filter(Q(name__icontains = si) | Q(address__icontains = si) | Q(gender__icontains = si) | Q(status__icontains = si)).order_by("-id");
        #profList2 = Friend_Request.objects.filter(to_user=self.request.user.myprofile)

        profList = MyProfile.objects.filter(Q(user_id__first_name__icontains = si) | Q(address__icontains = si) | Q(gender__icontains = si) | Q(status__icontains = si)).order_by("-id");
        for p1 in profList:
            p1.followed = False
            p1.request_sent= False
            p1.followback= False
            p1.request_received = False
            p1.myfollower = False
            ob = FollowUser.objects.filter(profile = p1 ,followed_by=self.request.user.myprofile)
            if ob:
                p1.followed = True

            ob = Friend_Request.objects.filter(to_user= p1.user_id,from_user=self.request.user.id)
            if ob:
                p1.request_sent= True

            ob = FollowUser.objects.filter(profile = self.request.user.id, followed_by= p1)
            if ob:
                p1.followback= True

            ob = Friend_Request.objects.filter(to_user=self.request.user.id , from_user=p1.user_id)
            if ob:
                p1.request_received = True
            ob = FollowUser.objects.filter(profile= self.request.user.myprofile , followed_by= p1)
            if ob:
                p1.myfollower = True
        return profList




@method_decorator(login_required, name="dispatch")
class MyProfileDetailView(DetailView):
    model = MyProfile

def follow(req, pk):
    user = MyProfile.objects.get(pk=pk)
   # user = get_object_or_404(pk=pk)
    FollowUser.objects.create(profile=user, followed_by = req.user.myprofile)
    return HttpResponseRedirect(redirect_to="/social/myprofile")

def unfollow(req, pk):
    user = MyProfile.objects.get(pk=pk)
    FollowUser.objects.filter(profile=user, followed_by = req.user.myprofile).delete()
    return HttpResponseRedirect(redirect_to="/social/myprofile")

#radzzz
def send_friend_request(request,userID):
    from_user = request.user
    to_user = ProfcessUser.objects.get(id=userID)
    print(from_user)
    print(to_user)
    #Friend_Request.objects.created(from_user=from_user, to_user=to_user)
    friend_request, created= Friend_Request.objects.get_or_create(
        from_user=from_user, to_user=to_user)
    if created:
        return HttpResponse('Friend request sent')
    else:
        return HttpResponse('Friend request was already sent')


def accept_friend_request(request,requestID):
    userfrom = ProfcessUser.objects.get(id=requestID)
    userto = ProfcessUser.objects.get(id=request.user.id)
    user = MyProfile.objects.get(id=requestID)
    user1 = MyProfile.objects.get(id=request.user.id)
    print(user.name)
    FU = FollowUser.objects.create(profile= user1, followed_by= user)
    FU.save()
    FR = Friend_Request.objects.get(Q(from_user= userfrom) & Q(to_user=userto))
    FR.delete()
    print(FR)

    return HttpResponse('friend request accepted')


"""
def accept_friend_request(request,requestID):
    friend_request=Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.add(friend_request.from_user)
        friend_request.from_user.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('friend request not accepted')
"""
#radzz code ends..

def like(req, pk):
    post = MyPost.objects.get(pk=pk)
    PostLike.objects.create(post=post, liked_by = req.user.myprofile)
    return HttpResponseRedirect(redirect_to="/social/home")

def unlike(req, pk):
    post = MyPost.objects.get(pk=pk)
    PostLike.objects.filter(post=post, liked_by = req.user.myprofile).delete()
    return HttpResponseRedirect(redirect_to="/social/home")

def comment(request,pk):
    post = MyPost.objects.get(pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            content = request.POST.get('content')
            postcomment = PostComment.objects.create(post_by=post, commented_by=request.user, content=content)
            postcomment.save()
            return HttpResponseRedirect(redirect_to="/social/home")
    # else:
    #     comment_form = CommentForm()
    return HttpResponseRedirect(redirect_to="/social/home")

def followers(req, pk):
    user = MyProfile.objects.get(pk=pk)
    cnt = 0
    cnt = FollowUser.objects.filter(profile=user, followed_by = req.user.myprofile).count()
    print(cnt)
    user_data = ApplicantUserProfile()
    #context = {'form': user_data}
    return HttpResponseRedirect(redirect_to="/social/home", context= {'form': user_data})

#=============================================================
#====================== Rating =========================
#bhavin tasks

def rate_post(req,pk):
    #stores login user details
    user_data = req.user.myprofile
    post = MyPost.objects.get(pk=pk)
    # post = MyPost.objects.all()
    res = PostRating.objects.all().filter(post=post,rate_by=user_data)
    # for i in res:
    #     user = i
        # print(user)
    # print("post===>>",post)

    if(res):
        #if the post already rated 
        #select post,rate from postrating table where id = login user
        rating_record = PostRating.objects.values_list('post','rate').filter(post=post,rate_by=user_data)
        for i in rating_record:
            rated_post_id= i[0]
            rated_score = i[1]
        # print("Alread Rated")
    else:
        #if the post is NOT already rated 
        if req.method == 'POST':
            # print("INSIDE rate post!!!! ")
            rate_post = req.POST.get('product')
            post_id = req.POST.get('postid')
            # print("post id====> ",post)
            print("rateing====> ",rate_post)
            

                
            PostRating.objects.create(post=post, rate=rate_post, rate_by= req.user.myprofile)

    return HttpResponseRedirect(redirect_to="/social/home")
            
   
#====================== End of Rating function =========================


'''def home(request):
    return render(request, "social/home.html")'''


