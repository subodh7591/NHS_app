import json

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from django.views import View
from django.views.decorators.csrf import csrf_exempt

from home_page.forms import UserForm
from home_page.models import FeedBack, Department


class HomePage(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request):
        return render(request=request,
                      template_name="index.html",
                      context={"data": [request.user]})

    def post(self, request):
        return HttpResponse("homepage")


class RegisterView(View):
    def get(self, request):
        form = UserForm()
        return render(request=request,
                      template_name="registration/register.html",
                      context={"register_form": form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Success")
            return redirect("homepage")
        messages.error(request, "Unsuccessful registration. Try again")
        form = UserForm()
        return render(request=request,
                      template_name="registration/register.html",
                      context={"register_form": form})


@method_decorator(csrf_exempt, name='post')
class PostFeedback(View):
    def post(self, request):
        department = None
        feedback = ''
        for key, value in request.POST.items():
            args = json.loads(key)
            feedback = args.get('feedback')
            department_name = args.get('department')
            department = Department.objects.get(name=department_name)

        payload = dict(
            feedback=feedback,
            user=request.user,
            forwarded_to=department
        )
        feedback_obj = FeedBack(**payload)
        feedback_obj.save()
        return HttpResponse("successfully posted")


class ListFeedback(View):
    def get(self, request):
        feedbacks = FeedBack.objects.filter(user=request.user)
        return render(request=request,
                      template_name="data_list.html",
                      context={"data": feedbacks})


class ListUser(View):
    def get(self, request):
        users = User.objects.filter(is_superuser=False)
        return render(request=request,
                      template_name="user_list.html",
                      context={"data": users})


class DeleteFeedback(View):
    def get(self, request):
        try:
            feedback_id = request.GET.get('query')
            feedback = FeedBack.objects.get(feedback_id=feedback_id)
            feedback.delete()
        except Exception as e:
            print(e)
        feedbacks = FeedBack.objects.filter(user=request.user)
        return render(request=request,
                      template_name="data_list.html",
                      context={"data": feedbacks})


class DeleteUser(View):
    def get(self, request):
        try:
            user_id = request.GET.get('query')
            user = User.objects.get(id=user_id)
            user.delete()
        except Exception as e:
            print(e)
        users = User.objects.filter(is_superuser=False)
        return render(request=request,
                      template_name="user_list.html",
                      context={"data": users})


class ShowFeedback(View):
    def get(self, request):
        feedback_id = request.GET.get('query')
        feedbacks = FeedBack.objects.filter(feedback_id=feedback_id)
        return render(request=request,
                      template_name="feedback_detail.html",
                      context={"data": feedbacks})


class CheckFeedback(View):
    def get(self, request):
        feedbacks = FeedBack.objects.all()
        return render(request=request,
                      template_name="check_feedback_list.html",
                      context={"data": feedbacks})
