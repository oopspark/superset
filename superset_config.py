
SECRET_KEY = "NVYQgTiQmIHsnbWo0/a7ele6M1smULHqWoiWoFawrGlNQoBTEYnMJXeP"

ALLOWED_SQLALCHEMY_DATASOURCE_URIS = [
    "sqlite://",
    "sqlite+pysqlite://",
    "sqlite"
]

SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://supersetuser:StrongPassword123!@localhost:5432/supersetdb"
