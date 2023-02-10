from .models import Category, Advertisement, Image
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import CategorySerializers, AdvertisementSerializers, ImageSerializers, ADSSerializer


class ADSView(generics.ListCreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = ADSSerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class AdvertisementView(generics.ListCreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializers

    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        image_urls = request.POST.getlist('image_urls')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            for img in images:
                Image.objects.create(ad_id=obj.id, image=img)
        print(serializer.errors)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ImageView(generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializers

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.errors)
        return Response(serializer.data, status=status.HTTP_200_OK)
