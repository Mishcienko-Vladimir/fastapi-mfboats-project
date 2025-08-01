from fastapi_users.authentication import AuthenticationBackend

from core.repositories.authentication.transport import bearer_transport
from .strategy import get_database_strategy


authentication_backend = AuthenticationBackend(
    name="access-token-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
