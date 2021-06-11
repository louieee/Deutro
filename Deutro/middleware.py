from tenant_schemas.middleware import DefaultTenantMiddleware


class MyDefaultTenantMiddleware(DefaultTenantMiddleware):
    DEFAULT_SCHEMA_NAME = 'default'
