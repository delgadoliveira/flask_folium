import folium
from flask import Flask
from flask import request

app = Flask(__name__)

# Example of link: http://127.0.0.1:5000/?lat=40&lon=80
@app.route('/')
def index():
    lat = request.args.get('lat', '')
    lon = request.args.get('lon', '')
    start_coords = (lat, lon)
    folium_map = folium.Map(location=start_coords, zoom_start=8)
    return folium_map._repr_html_()

# @app.route('/export_kml')
# def export_kml():
#     return 

if __name__ == '__main__':
    app.run(debug=True)