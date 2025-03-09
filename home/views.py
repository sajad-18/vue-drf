from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Question
from .serializer import PersonSerializer, QuestionSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from permissions import IsOwnerOrReadOnly
from rest_framework.parsers import JSONParser


class HomeView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(persons, many=True)
        return Response(data=ser_data.data)


class QuestionListView(APIView):
    throttle_scope = 'questions'

    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    """
        Create a new question
    """
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    serializer_class = QuestionSerializer

    def post(self, request):
        if request.user.is_authenticated:
            print(f"User {request.user.username} is logged in.")
        else:
            print("No user is logged in.")
        try:
            print("Request User:", request.user)  # چاپ اطلاعات کاربر
            print("Request Data:", request.data)  # چاپ داده‌های درخواست

            srz_data = QuestionSerializer(data=request.data)

            # بررسی صحت داده‌ها
            if srz_data.is_valid():
                print("Data is valid. Saving...")
                # ذخیره داده‌ها و تعیین کاربر
                srz_data.save(user=request.user)

                print("Data saved successfully")
                return Response(srz_data.data, status=status.HTTP_201_CREATED)

            # در صورت نامعتبر بودن داده‌ها
            print("Invalid data:", srz_data.errors)
            return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("Unexpected error occurred:", e)
            return Response(
                {"detail": "An unexpected error occurred.", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly, ]

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message': 'question deleted'}, status=status.HTTP_200_OK)







