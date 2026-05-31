from datetime import tzinfo
from pathlib import Path

import pytz
from PIL import Image
from pydantic_settings import BaseSettings, SettingsConfigDict

SRC_DIR = Path(__file__).resolve(strict=True).parent
REPO_DIR = SRC_DIR.parent


class Constants(BaseSettings):
    # =============== // METADATA // ===============

    title: str = "Demo App"
    description: str = "A demo app"

    # =============== // Database Configurations // ===============
    # dialect[+driver]://user:password@host/dbname[?key=value..]
    # e.g. engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/test")
    db_connection_string: str
    db_echo: bool = False

    default_picture: str = "https://gravatar.com/avatar/580b828f66630050b21aeaf8c20b89b3?s=400&d=mp&r=x"

    # =============== // DIRECTORIES AND PATHS // ===============

    root_dir: Path = SRC_DIR
    repo_dir: Path = REPO_DIR
    static_dir: Path = SRC_DIR / "static"

    favicon: Image.Image = Image.open(SRC_DIR / "static" / "datatreehouse.circle.png")

    logo_banner_path: str = "static/datatreehouse.banner.png"
    logo_circle_path: str = "static/datatreehouse.banner.png"
    buy_us_a_coffee_path: str = "static/buy-us-a-coffee.png"

    pages_path: str = "app/pages"

    # =============== // LINKS // ===============

    datatreehouse_url: str = "https://datatreehouse.org"
    snapscan_url: str = "https://pos.snapscan.io/qr/Ew6rBAsV"

    # =============== // UMAMI // ===============

    umami_website_id: str
    umami_host: str

    tz: tzinfo = pytz.timezone("Africa/Johannesburg")

    model_config = SettingsConfigDict(
        env_file=str(REPO_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )


c = Constants()  # type: ignore
