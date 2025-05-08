from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# ─── добавляем эти 3 строки ─────────────────────────────
import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
# ─────────────────────────────────────────────────────────

# ─────── добавляем два импорта ──────────────────────────────────────────────
from app.core.config import settings           # берём параметры БД
from app.db.base import Base                   # здесь объявлены все модели
# ────────────────────────────────────────────────────────────────────────────

config = context.config

# ←–– важно: подставляем строку соединения в объект config
config.set_main_option(
    "sqlalchemy.url",
    f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}",
)

# настройка логирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# metadata для autogenerate
target_metadata = Base.metadata            # ← вместо None

# остальной шаблонный код оставляем без изменений
# ----------------------------------------------------------------------------
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
