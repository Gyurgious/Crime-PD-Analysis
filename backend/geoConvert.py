import geopandas as gpd

# Read your shapefile
gdf = gpd.read_file("ZIPCODE.shp")

# Reproject to WGS84
gdf = gdf.to_crs(epsg=4326)

# Export to GeoJSON
gdf.to_file("output.geojson", driver="GeoJSON")

