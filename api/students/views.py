from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView

from .models import Students
from .serializers import StudentsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from django.conf import settings


class StudentsViewSet(viewsets.ModelViewSet):

    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = (IsAuthenticated,)


    def list(self, request, *args, **kwargs):
        name = request.GET.get("name", None)
        age = request.GET.get("age", None)
        if name:
            queryset = Students.objects.filter(name=name)
        elif age:
            current_date = date.today()
            old_date = current_date - relativedelta(years=int(age))

            queryset = Students.objects.filter(date_of_birth__gte=old_date)
        else:
            queryset = Students.objects.all()

        serializer = StudentsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmailAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        subject = self.request.data.get('subject')
        txt_ = self.request.data.get('text')
        html_ = self.request.data.get('html')
        recipient_list = self.request.data.get('recipient_list')
        from_email = settings.DEFAULT_FROM_EMAIL

        if subject is None and txt_ is None and html_ is None and recipient_list is None:
            return Response({'msg': 'There must be a subject, a recipient list, and either HTML or Text.'}, status=200)
        elif html_ is not None and txt_ is not None:
            return Response({'msg': 'You can either use HTML or Text.'}, status=200)
        elif html_ is None and txt_ is None:
            return Response({'msg': 'Either HTML or Text is required.'}, status=200)
        elif recipient_list is None:
            return Response({'msg': 'Recipient List required.'}, status=200)
        elif subject is None:
            return Response({'msg': 'Subject required.'}, status=200)
        else:
            sent_mail = send_mail(
                subject,
                txt_,
                from_email,
                recipient_list,
                html_message=html_,
                fail_silently=False,
            )
            return Response({'msg': sent_mail}, status=200)

