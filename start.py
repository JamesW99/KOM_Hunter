# get top 10 segment ID in a area
# how to use: BOTTOM_LEFT= bottom left of area, TOP_RIGHT= top right of the area
# Please use the latitude and longitude from OSM. www.openstreetmap.org


import segment_explore
BOTTOM_LEFT_LATITUDE = 55.9004
BOTTOM_LEFT_LONGITUDE = -3.3381
TOP_RIGHT_LATITUDE = 55.9173
TOP_RIGHT_LONGITUDE = -3.3132

if __name__ == '__main__':
    # segment_explore.getTopSegments(BOTTOM_LEFT_LATITUDE, BOTTOM_LEFT_LONGITUDE, TOP_RIGHT_LATITUDE, TOP_RIGHT_LONGITUDE)
    segment_explore.getTopSegments(55.9004, -3.3381, 55.9173, -3.3132)

