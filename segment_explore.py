from api import StravaAPI
import database_control

api = StravaAPI()


def getTopSegments(blla, bllo, trla, trlo):

    ten_segment = StravaAPI.get_segment_explore(api, bounds=((blla, bllo), (trla, trlo))).values()
    ten_segment_list = list(ten_segment)[0]  # this is a list include 10 segment dict

    try:
        list(ten_segment)[1]
    except IndexError:
        pass
    else:
        print("ERROR, should not print this line. Dict format change!")

    for n in range(10):
        del ten_segment_list[n]['resource_state']  # 2 is cycling
        del ten_segment_list[n]['start_latlng']
        del ten_segment_list[n]['end_latlng']
        del ten_segment_list[n]['points']
        del ten_segment_list[n]['starred']
        del ten_segment_list[n]['elevation_profile']
        del ten_segment_list[n]['local_legend_enabled']
        database_control.upload_segment_to_database(ten_segment_list[n])


    if __name__ == '__main__':
        return ten_segment_list


if __name__ == '__main__':
    if getTopSegments(55.9004, -3.3381, 55.9173, -3.3132):
        print("api is working")
