var app;
require([
    "esri/Map",
    "esri/layers/GraphicsLayer",
    "esri/Graphic",
    "esri/geometry/Point",
    "esri/tasks/Geoprocessor",
    "esri/tasks/support/LinearUnit",
    "esri/tasks/support/FeatureSet",
  "esri/views/MapView",
  "esri/layers/FeatureLayer",
  "esri/symbols/SimpleLineSymbol",
  "dojo/domReady!"
], function(Map, GraphicsLayer, Graphic, Point, Geoprocessor, LinearUnit, FeatureSet, MapView, FeatureLayer,SimpleLineSymbol ){

	//a map with basemap
	var map = new Map({
    basemap: "streets"
	});
    // featureLayer = new FeatureLayer({
    //         url: "http://geoserver2.byu.edu/arcgis/rest/services/TeamWon/Utah_bus_stops/FeatureServer/",
    //     });
    // map.layers.add(featureLayer);


    leg_dem = document.getElementById("legend_dem")
			leg_rest = document.getElementById("legend_rest")

            leg_dem.onchange =function(){
				layer1.visible = leg_dem.checked
			}
            leg_rest.onchange =function(){
				featureLayer.visible = leg_rest.checked
			}
    //a graphics layer to show input point and output polygon
    var graphicsLayer = new GraphicsLayer();
    map.add(graphicsLayer);

    var view = new MapView({
    container: "viewDiv",
    map: map,
	center: [-111.67266235351346, 40.24052798830994],
	zoom: 10
    });

	// symbol for input point
	var markerSymbol = {
          type: "simple-marker", // autocasts as new SimpleMarkerSymbol()
          color: [255, 0, 0],
          outline: { // autocasts as new SimpleLineSymbol()
            color: [255, 255, 255],
            width: 2
          }
        };

	// symbol for buffered polygon
    var fillSymbol = {
          type: "simple-fill", // autocasts as new SimpleFillSymbol()
          color: [226, 119, 40, 0.75],
          outline: { // autocasts as new SimpleLineSymbol()
            color: [255, 255, 255],
            width: 1
          }
        };



    var symbolLine = {
      type: "simple-line",  // autocasts as new SimpleLineSymbol()
      color: [225, 51, 204],
      width: "2px",
      style: "short-dot"
	};
    // Geoprocessing service url
	// var gpUrl = "http://geoserver2.byu.edu/arcgis/rest/services/sherry/BufferPoints/GPServer/Buffer%20Points";
	// var gpUrl = "http://geoserver2.byu.edu/arcgis/rest/services/TeamWon/BufferPoints/GPServer/Buffer%20Points";
	var gpUrl = "http://geoserver2.byu.edu/arcgis/rest/services/TeamWon/CreateWatershedPolygon/GPServer/Create%20Watershed%20Polygon";
	var gpUrl_clip = "http://geoserver2.byu.edu/arcgis/rest/services/TeamWon/Provo_Repro/GPServer/Provo_clip";

    // create a new Geoprocessor
	var gp = new Geoprocessor(gpUrl);
	var gp_clip = new Geoprocessor(gpUrl_clip);


	// define output spatial reference
    gp.outSpatialReference = { // autocasts as new SpatialReference()
          wkid: 102100 //EPSG3857
          // wkid: 4326 //EPSG3857
        };

	//add map click function
    view.on("click", bufferPoint);
    // view.on("click", clip_bus);

	//main function
    function bufferPoint(event) {
        console.log(event.mapPoint.longitude)
        console.log(event.mapPoint.latitude)
          graphicsLayer.removeAll();
          var point = new Point({
            longitude: event.mapPoint.longitude,
            latitude: event.mapPoint.latitude
          });

          var inputGraphic = new Graphic({
            geometry: point,
            symbol: markerSymbol
          });

          graphicsLayer.add(inputGraphic);

          var inputGraphicContainer = [];
          inputGraphicContainer.push(inputGraphic);
          
          var featureSet = new FeatureSet();
          featureSet.features = inputGraphicContainer;

          var bfDistance = new LinearUnit();
          bfDistance.distance = 100;
          bfDistance.units = "miles";

		  // input parameters
          // var params = {
           //  "Point": featureSet,
           //  "Distance": bfDistance
          // };

          // var params = {
          //   "Input_Features": featureSet,
          //   "Distance": bfDistance
          // };
           var params = {
            "Pour_Point": featureSet,
          };

          gp.submitJob(params).then(completeCallback, errBack, statusCallback);
    }

    function clip_bus(event) {

          graphicsLayer.removeAll();

            sql_expression = "\"Name\":'Provo'"
           var params = {
            "BusRoutes_UTA ": "BusRoutes_UTA",
               // "Expression":sql_expression

          };
          gp_clip.submitJob(params).then(completeCallback_clip, errBack, statusCallback);
    }

	function completeCallback(result){

        gp.getResultData(result.jobId, "Output_Watershed ").then(drawResult, drawResultErrBack);

	}

	function completeCallback_clip(result){

        gp_clip.getResultData(result.jobId, "Clip_bus_Project").then(drawResult_clip, drawResultErrBack);

	}

	function drawResult(data){
        console.log(data)
	    var polygon_feature = data.value.features[0];
		polygon_feature.symbol = fillSymbol;
		graphicsLayer.add(polygon_feature);
	}
	function drawResult_clip(data){
        console.log(data)
        console.log('CCCCCCCCCCCCCCCCCCCClip')
        var polygon_feature3 = data.value.features;
        for (fea in polygon_feature3){
            polygon_feature3[fea].symbol = symbolLine;


            // var polygon_feature1 = data.value.features[1];
            // graphicsLayer.add(polygon_feature);
            graphicsLayer.add( polygon_feature3[fea]);
            // graphicsLayer.add(polygon_feature1);
        }
	}

	function drawResultErrBack(err) {
        console.log("draw result error: ", err);
    }

	function statusCallback(data) {
        console.log(data.jobStatus);
    }

    function errBack(err) {
        console.log("gp error: ", err);
    }
app = {clip_bus: clip_bus};

});

