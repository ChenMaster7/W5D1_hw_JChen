from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'topfive/home.html')


def my_top_five(request):
    top_five_boston_restaurants = [
        {
            'restaurant': 'Dumpling Gourmet',
            'location': 'Boston Chinatown',
            'speciality': 'Dumplings',
            'cost ($-$$$$$)': '$$$'
        },
        {
            'restaurant': 'Victoria Seafood',
            'location': 'Allston',
            'speciality': 'Seafoods, traditional dishes, softshell crabs',
            'cost ($-$$$$$)': '$$'
        },
        {
            'restaurant': "Ming's Dim Sum",
            'location': 'Malden',
            'speciality': 'Dim sum, boujee authentic chinese restaurant',
            'cost ($-$$$$$)': '$$$$'
        },
        {
            'restaurant': 'Spring Shabu Shabu',
            'location': 'North Allston',
            'speciality': 'All-you-can-eat hotpot',
            'cost ($-$$$$$)': '$$$'
        },
        {
            'restaurant': 'Bon Chon',
            'location': 'Allston, Lowell, Harvard Square',
            'speciality': 'Korean fried chicken',
            'cost ($-$$$$$)': '$$'
        },
    ]
    context = {'top_five': top_five_boston_restaurants}
    return render(request, 'topfive/topfive.html', context)