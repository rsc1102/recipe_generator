from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.http import require_POST
import json
from openai import OpenAI
from decouple import config
from app.models import recipeGenerationModel

client = OpenAI(api_key=config('OPENAI_API_KEY'))

def index(request):
    template = loader.get_template("app/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


@require_POST
def generate_recipes(request):
    try:
        ingredients = json.loads(request.body)['items']
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    if len(ingredients) < 4:
        return JsonResponse({'error': 'Not enough ingredients'}, status=400)
    
    completion = client.beta.chat.completions.parse(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a master chef tasked with creating recipes from the user provided ingredients. Assume you have salt, black pepper, oil and water."},
                    {
                        "role": "user",
                        "content": f"Generate a recipe using the following ingredients: {', '.join(ingredients)}. Include detailed instructions."
                    }
                ],
                max_tokens=1000,
                temperature=0.7,
                response_format=recipeGenerationModel,
                n = 1,
            )
    output = completion.choices[0].message.parsed.model_dump()
    return JsonResponse(output)