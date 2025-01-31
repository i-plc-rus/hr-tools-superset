FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "ENABLE_JAVASCRIPT_CONTROLS": True,
}

# Настройки CORS (Cross-Origin Resource Sharing)
ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': ['*'],  # Укажите домен вашего фронтенда вместо '*'
}