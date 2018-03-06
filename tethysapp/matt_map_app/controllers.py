from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import *

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    text_data = '<h3>Welcome to the Mapapp</h3>' \
                '<li>Created for CEEN 514: Geospatial Software Developlment</li>' \
                '<li>Created on: Feburary 25, 2018' \
                '<li>Assignment Number 13</li>' \
                '<h4>Assignment Requirements</h4>' \
                """
                <ol><li>Build a new Tethys app called "mapapp" on your Ubuntu server, 
                using the scaffold command.</li>
                <li>Remove all of the default content of the app while keeping the side bar, 
                bottom, top, and main app areas - just remove the excess HTML.</li>
                <li>Create 4 links on the sidebar:</li>
                <ul>
                <li>Home</li>
                <li>Map View</li>
                <li>Data Services</li>
                <li>About</li>
                </ul>
                <li>Each of these links should open a new page in the main view. </li>
                <li>Submit a document with screenshots showing all required elements 
                running on your computer.</li>
                <li>Be prepared to do a quick 2 minute demo of your app in class on Tuesday.</li> </ol>
                """

    datatable_default = DataTableView(column_names=('Name', 'Age', 'Job'),
                                      rows=[('Bill', 30, 'contractor'),
                                            ('Fred', 18, 'programmer'),
                                            ('Bob', 26, 'boss')],
                                      searching=False,
                                      orderClasses=False,
                                      lengthMenu=[[10, 25, 50, -1], [10, 25, 50, "All"]],
                                      )
    date_picker = DatePicker(name='date1',
                             display_text='Date',
                             autoclose=True,
                             format='MM d, yyyy',
                             start_date='2/15/2014',
                             start_view='decade',
                             today_button=True,
                             initial='February 15, 2014')
    text_input = TextInput(display_text='Text',
                           name='inputAmount',
                           placeholder='e.g.: 10.00',
                           prepend='$')
    context = {
        'text_data': text_data,
        'datatable_view': datatable_default,
        'date_picker':date_picker,
        'text_input':text_input
    }

    return render(request, 'matt_map_app/home.html', context)

def map_view(request):
    """
    Controller for the app home page.
    """

    context = {

    }
    return render(request, 'matt_map_app/map_view.html', context)

def data_services(request):
    """
    Controller for the app home page.
    """

    text_data = '<h3>Data Services</h3>' \
                'The data for this map is stored <a target="_blank" ' \
                'href="http://geoserver2.byu.edu/arcgis/rest/services/TeamWon"' \
                '>here.</a> The raster data was obtained from the State of Utah. ' \
                'The restaurant locations were obatined ' \
                'by using Google\'s API for location searching combined with a custom Python script. ' \
                'The restaruants ' \
                'shown are only for the City of Provo and include Wendy\'s, McDonalds\' and Taco Bell. ' \
                'These two data sets were then published to an ArcSever using ArcGIS.'
    context = {
        'text_data': text_data
    }

    return render(request, 'matt_map_app/home.html', context)


def about(request):
    """
    Controller for the app home page.
    """

    text_data = '<h3>About</h3>' \
                'My name is Matthew Bayles and I am a Graduate Student in Civil Engineering at' \
                'BYU. My interests include programming, reading, playing video games, and spending time with my lovely wife.' \
                '<p>' \
                '<img src="https://media.licdn.com/mpr/mpr/shrinknp_400_400/p/6/005/020/0a6/0801d1b.jpg"><p>' \
                '<h4>Contact Information</h4><p>' \
                '<a href="mailto:mmbayles@gmail.com?subject=Mapapp"> ' \
                '<img style="height:100px" src="http://icons.iconarchive.com/icons/hamzasaleem/stock/512/Mail-icon.png">' \
                '</a>' \
                '<a href="https://www.linkedin.com/in/matthew-bayles-180b7780/" target="_blank">' \
                '<img style="height:100px" src="https://cdn.business2community.com/wp-content/uploads/2017/12/' \
                'linkedin_1512525898.png"' \
                '</a>' \
                '<p>'
    context = {
        'text_data': text_data
    }

    return render(request, 'matt_map_app/home.html', context)

def proposal(request):
    """
    Controller for the app home page.
    """

    text_data = '<iframe src="https://docs.google.com/document/d/e/2PACX-1vS_KNtwc5DkRbqYF2VFvtRgj1TI6iCqLJGwBRenKPZNavE_Z6fkca8t5FrK5skBWQHYscXtQD9rqgxH/pub?embedded=true" style="height: -webkit-fill-available; width: -webkit-fill-available;"></iframe>'
    context = {
        'text_data': text_data
    }

    return render(request, 'matt_map_app/home.html', context)
def mockup(request):
    """
    Controller for the app home page.
    """

    text_data = '<iframe src="https://docs.google.com/document/d/e/2PACX-1vRVjlsyowjU_cJTydXpeOeBL1GBFJipzw7TXgQn80q46jBmg6JGQ1w2JYk2AW62-IYqGbBiHsVk-xDu/pub?embedded=true" style="height: -webkit-fill-available; width: -webkit-fill-available;"></iframe>'
    context = {
        'text_data': text_data
    }

    return render(request, 'matt_map_app/home.html', context)