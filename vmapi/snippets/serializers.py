from rest_framework import serializers
from snippets.models import Snippet
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ipaddress = serializers.CharField(max_length=20)
    vm_type = serializers.IntegerField()
    cpu = serializers.DecimalField(max_digits=5, decimal_places=2)
    mem = serializers.DecimalField(max_digits=5, decimal_places=2)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.ipaddress = validated_data.get('ipaddress', instance.ipaddress)
        instance.vm_type = validated_data.get('vm_type', instance.vm_type)
        instance.cpu = validated_data.get('cpu', instance.cpu)
        instance.mem = validated_data.get('mem', instance.mem)

        # instance.title = validated_data.get('title', instance.title)
        # instance.code = validated_data.get('code', instance.code)
        # instance.linenos = validated_data.get('linenos', instance.linenos)
        # instance.language = validated_data.get('language', instance.language)
        # instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'ipaddress', 'vm_type', 'cpu', 'mem')
