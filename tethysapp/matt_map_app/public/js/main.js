require([
      "esri/views/MapView",
      "esri/Map",
      "esri/layers/MapImageLayer",
	  "esri/layers/FeatureLayer",
	  "dojo/on",
      "dojo/domReady!"
    ], function(
      MapView, Map, MapImageLayer, FeatureLayer, on
    ) {

      /************************************************************
       * Creates a new WebMap instance. A WebMap must reference
       * a PortalItem ID that represents a WebMap saved to
       * arcgis.com or an on-premise portal.
       *
       * To load a WebMap from an on-premise portal, set the portal
       * url with esriConfig.portalUrl.
       ************************************************************/

      var map = new Map({
		basemap: "streets"
		});



		layer1 = new MapImageLayer({
            url: "http://geoserver2.byu.edu/arcgis/rest/services/TeamWon/utah_raster/MapServer"
        });
		featureLayer = new FeatureLayer({
            url: "http://geoserver2.byu.edu/arcgis/rest/services/TeamWon/feature_food/FeatureServer/",
        });

		map.layers.add(layer1);
		map.layers.add(featureLayer);

			leg_dem = document.getElementById("legend_dem")
			leg_rest = document.getElementById("legend_rest")

            leg_dem.onchange =function(){
				layer1.visible = leg_dem.checked
			}
            leg_rest.onchange =function(){
				featureLayer.visible = leg_rest.checked
			}

		var template = {
		  title: "Restaurant Name: {Field1}"
		};
		featureLayer.popupTemplate = template;

      var view = new MapView({
        map: map,
        container: "viewDiv",
		center: [-111.5,40.5],
		zoom:8
      });
    });