import os
ENV = os.getenv("DJANGO_ENV", "dev")   # dev | prod
if ENV == "prod":
    from .prod import *   # noqa
else:
    from .dev import *    # noqa
