from rest_framework import serializers
from .models import Recipe, Ingredient, Instructions
from comment.serializers import CommentSerializer

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'item_name', 'quantities']

class InstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructions
        fields = ['id', 'recipe']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    instructions = InstructionsSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')

    class Meta:
        model = Recipe
        fields = ['id', 'user', 'title', 'preparation_time', 'ingredients', 'instructions', 'comments']
