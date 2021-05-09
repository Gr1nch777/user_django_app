from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, View, FormView, DetailView
from user.models import User
from user.forms import UserForm


class UserListView(ListView):

    model = User
    template_name = 'all_users.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user.html'


class AddUserView(FormView):

    form_class = UserForm
    template_name = 'add_user.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)
        return response


class DeleteUserView(View):

    def get(self, request, user_id):

        user = User.objects.get(pk=user_id)
        user.delete()

        return HttpResponse(f'Deleted {user.username}')


class EditUserView(View):

    def get(self, request, user_id):

        form = UserForm()

        context = {
            'form': form
        }

        return render(
            template_name='add_user.html',
            request=request,
            context=context,
        )

    def post(self, request, user_id):

        user = User.objects.get(id=user_id)

        username = request.POST['username']
        e_mail = request.POST['e_mail']

        if len(username) != 0:
            user.username = username

        if len(e_mail) != 0:
            user.e_mail = e_mail

        user.save()

        context = {
            'username': user.username,
            'e_mail': user.e_mail
        }

        return render(
            template_name='user_post.html',
            request=request,
            context=context,
        )
