from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에서 데이터 모두 보기
#all_movies = list(db.movies.find())

# 참고) MongoDB에서 특정 조건의 데이터 모두 보기
find_movie = db.movies.find_one({'title':'매트릭스'})      
find_star = find_movie['star']
star_movie = list(db.movies.find({'star':find_star}))
for x in star_movie:
    print(x['title'])

# 바꾸기 - 예시
db.movies.update_many({'star':find_star},{'$set':{'star':0}})