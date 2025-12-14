from django.contrib.auth.mixins import LoginRequiredMixin


class AuthorRequiredMixin(LoginRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):

        obj = self.get_object()
        if obj.author != request.user:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)