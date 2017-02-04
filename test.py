from TwitterAPI import TwitterAPI
api = TwitterAPI("sNjj2O9xgtclg2l4Y3batJNmD", "iKMk9pye8bBZLPzGBupCco2cEVKG8buESq4m2UUuaI5Br7c1RH", "2382398376-zmcPodEblLN3v3aiJ1uHoEAAJp2XJQ5lDO7xc5a", "17X7Dk2LrWY4BEUhsBsjtciSCGJXdslNSRqk4hmWfebhg")
r = api.request('search/tweets', {'q':'pizza'})
for item in r:
        print(item)