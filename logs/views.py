from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Log
from .serializers import LogSerializer
from json2html import json2html  # Import json2html
import logging

class LogListView(APIView):
    """
    View to list and create logs.
    """
    def get(self, request):
        # Retrieve all logs from the database
        logs = Log.objects.all()
        serializer = LogSerializer(logs, many=True)
        
        # Convert the JSON response to a structured HTML format
        html_response = json2html.convert(json=serializer.data)

        # Return the HTML response (instead of JSON)
        return Response(html_response, content_type="text/html")  # Specify that the response is HTML
    
    def post(self, request):
        # Handle POST request to create new logs

        print("Raw request body:", request.body)  # Debug line
        print("Parsed data:", request.data)       # Debug line
        logger = logging.getLogger(__name__)
        logger.warning(f"Received data: {request.data}")
        print(request.data)
        serializer = LogSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()  # Save the logs to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created logs in JSON format
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if validation fails
