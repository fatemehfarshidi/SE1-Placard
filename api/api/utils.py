from .serializers import PostSerializer


def create(serializer):
    if serializer.filter(**serializer.data).exists():
        raise serializers.ValidationError('This data already exists')

    if serializer.is_valid():
        serializer.save()
        return serializer.data


def update(serializer):
    if serializer.is_valid():
        serializer.save()
        return serializer.data
