from tethys_sdk.base import TethysAppBase, url_map_maker


class MattMapApp(TethysAppBase):
    """
    Tethys app class for Matt Map App.
    """

    name = 'Matt Map App'
    index = 'matt_map_app:home'
    icon = 'matt_map_app/images/icon.gif'
    package = 'matt_map_app'
    root_url = 'matt-map-app'
    color = '#27ae60'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='matt-map-app',
                controller='matt_map_app.controllers.home'
            ),
            UrlMap(
                name='map_view',
                url='map_view',
                controller='matt_map_app.controllers.map_view'
            ),
            UrlMap(
                name='data_services',
                url='data_services',
                controller='matt_map_app.controllers.data_services'
            ),
            UrlMap(
                name='about',
                url='about',
                controller='matt_map_app.controllers.about'
            ),
            UrlMap(
                name='mockup',
                url='mockup',
                controller='matt_map_app.controllers.mockup'
            ),
            UrlMap(
                name='proposal',
                url='proposal',
                controller='matt_map_app.controllers.proposal'
            ),
        )

        return url_maps
