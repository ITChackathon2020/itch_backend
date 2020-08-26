cd ./app
export MONGO_DB_URI="mongo+srv://dbusername:dbpass@cluster.abcde.mongodb.net/<dbname>?retryWrites=true&w=majority"
export SECRET_KEY=b'\xe9S\xc6a\tR\x95t\x97/\x8a\rh\x8cp\x12\xfd\x15\xf8;\xdf\xce\xda`-\xce\xa8vg\x02\x9d`'

uvicorn main:app --reload

# deploy with 
# gunicorn -w 3 -k uvicorn.workers.UvicornWorker main:app