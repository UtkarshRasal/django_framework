from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response 
from snippets.models import Snippet
from snippets.serializer import SnippetSerializer


class SnippetList(APIView):
	def get(request, format=None):
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)
		return Response(serializer.data)

	def post(request, pk, fomat=None):
		serializer=SnippetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):

	def get_object(self, pk):
		try:
			snippet = snippet.objects.get(pk=pk)
		except Snippet.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serializer=SnippetSerializer(Snippet)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		snippet = self.get_object(pk)
		serialzer = SnippetSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		snippet = self.get_object(pk)
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
