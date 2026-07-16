import os


class Settings:
    app_name: str = os.getenv("APP_NAME", "Smart Retail Platform")
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:Nani1925@localhost:5432/retail_db",
    )
    cors_origins: list[str] = [
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
    ]


settings = Settings()
