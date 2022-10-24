import './style.css';
import {Map, View} from 'ol';
import OSM from 'ol/source/OSM';
import {transform} from 'ol/proj';
import TileLayer from 'ol/layer/Tile';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import {GeoJSON} from 'ol/format';


const geo_data_url = "http://127.0.0.1:8000/get_geo_vector_data?area_of_interest=wellington&year=21&quarter=3&version=0";
const center = transform([174.772996908, -41.28666552], 'EPSG:4326', 'EPSG:3857');


const base_layer = new TileLayer({
    source: new OSM()
})

const geojson_layer = new VectorLayer({
    source: new VectorSource({
        format: new GeoJSON(),
        url: geo_data_url,
    }),
    visible: true,
    title: "Area of Interest",
})

let layers = [base_layer, geojson_layer]

const map = new Map({
  target: 'map',
  layers: layers,
  view: new View({
    center: center,
    zoom: 10
  })
});
