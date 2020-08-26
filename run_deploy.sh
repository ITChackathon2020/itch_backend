cd ./app
export MONGO_DB_URI="mongodb+srv://itchMaster:lz4fhsQuHmB37J29@crm-template.rrvgs.mongodb.net/<dbname>?retryWrites=true&w=majority"
export SECRET_KEY=b'\x89\xbd\x00\x08\xcf,A|\xa2\x9d\xc4\x9c\xfaF\xc2\x03\x8b\x7f\xaf\xde\xdfJ\xd7n2\xb4\x852\x0e\xc7\x91f'

gunicorn -w 3 -k uvicorn.workers.UvicornWorker main:app
