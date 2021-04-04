from api import StravaAPI

api = StravaAPI()
# print(StravaAPI.get_segment_explore(api, bounds=((40.005981, 116.368721), (40.026885, 116.410263))))
# print(StravaAPI.get_segment_explore(api, bounds=((39.9795,116.0064), (40.0846,116.0682))))
# print(StravaAPI.get_segment_explore(api, bounds=((40.00692, 116.175044), (40.034293, 116.191725))))

# top 10 in Beijing
# print(StravaAPI.get_segment_explore(api, bounds=((39.8128,115.7272), (40.818,117.213))))

# top 10 in Campus
print(StravaAPI.get_segment_explore(api, bounds=((55.9004, -3.3381), (55.9173, -3.3132))))

#failed
print(StravaAPI.get_segment_leaderboard(api, 9732319))

print(StravaAPI.get_segment_detail(api,9732319))

