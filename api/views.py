# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny  # ✅ এটা add কর

class UserAPIView(APIView):
    # যেকোনো user access করতে পারবে
    permission_classes = [AllowAny]

    def get(self, request):
        user_data = {
            "id": "12345",
            "name": "Amit Kumar Biswas",
            "email": "amit@example.com",
            "roles": ["admin", "user"],
            "created_at": "2025-10-31T12:00:00Z"
        }
        settings_data = {
            "theme": "dark",
            "notifications": True,
            "language": "bn"
        }
        response_data = {
            "status": "success",
            "data": {
                "user": user_data,
                "settings": settings_data
            },
            "message": "User data fetched successfully."
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        response_data = {
            "status": "success",
            "data_received": data,
            "message": "Data posted successfully."
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
