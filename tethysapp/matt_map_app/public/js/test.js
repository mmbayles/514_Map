// require([
//       "esri/views/MapView",
//       "esri/Map",
//       "esri/layers/MapImageLayer",
// 	  "esri/layers/FeatureLayer",
// 	  "dojo/on",
//       "dojo/domReady!"
//     ], function(
//       MapView, Map,FeatureLayer, MapImageLayer
//     ) {
//
//       /************************************************************
//        * Creates a new WebMap instance. A WebMap must reference
//        * a PortalItem ID that represents a WebMap saved to
//        * arcgis.com or an on-premise portal.
//        *
//        * To load a WebMap from an on-premise portal, set the portal
//        * url with esriConfig.portalUrl.
//        ************************************************************/
//
//       var map = new Map({
// 		basemap: "streets"
// 		});
//
//         const fl = new FeatureLayer({
//             url: "http://geoserver2.byu.edu/arcgis/rest/services/TeamWon/Utah_bus_stops/MapServer"
//           });
//           map.add(fl);  // adds the layer to the map
//         layer1 = new FeatureLayer({
//             url: "http://geoserver2.byu.edu/arcgis/rest/services/TeamWon/utah_raster/MapServer"
//             // url: "http://geoserver2.byu.edu/arcgis/rest/services/TeamWon/Flowdir/MapServer"
//             // url: "http://geoserver2.byu.edu/arcgis/rest/services/TeamWon/Flowdir/MapServer"
//         });
//         // featureLayer = new FeatureLayer({
//         //     url: "http://geoserver2.byu.edu/arcgis/rest/services/TeamWon/feature_food/FeatureServer/",
//         // });
//
// 		map.layers.add(layer1);
// 		// map.layers.add(featureLayer);
//
//
//
//       var view = new MapView({
//         map: map,
//         container: "viewDiv",
// 		center: [-111.5,40.5],
// 		zoom:8
//       });
//       view.on("click", bufferPoint);
//       function bufferPoint(event) {console.log('hello')}
//     });