# ~~~~~~~~~~~~~~~~~~~~~ Main Server Settings ~~~~~~~~~~~~~~~~~~~~~ #
HOST = '127.0.0.1'
PORT = 80
# ~~~~~~~~~~~~~~~~~~~~~ Main Server Settings ~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~ Main database Settings ~~~~~~~~~~~~~~~~~~~~~ #
db_url = 'sqlite://database.db'
generate_schemas = True
add_exception_handlers = True

models = [
    'app.models',
]

default_db_values = {
    'profile': {
        'work': 'Не указанно',
        'sex': 'Не указанно',
        'age': 0,
        'education': 'Не указанно',
        'hobby': 'Не указанно',
        'quote': 'Не указанно',
        'phone': 'Не указанно',
        'country': 'Не указанно',
        'website': 'Не указанно'
    },
    'rating_base': {
        'score': 0
    },
    'email_validation': {
        'done': False
    },
}
# ~~~~~~~~~~~~~~~~~~~~~ Main database Settings ~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~ Main app Settings ~~~~~~~~~~~~~~~~~~~~~ #
app_title = 'AitiSpace'
app_description = 'AitiSpace'
app_version = '0.4.0'
# ~~~~~~~~~~~~~~~~~~~~~ Main app Settings ~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~ Main CORS Settings ~~~~~~~~~~~~~~~~~~~~~ #
allow_origins = [
    '*'
]
allow_credentials = True
allow_methods = ["*"]
allow_headers = ["*"]
# ~~~~~~~~~~~~~~~~~~~~~ Main CORS Settings ~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~ Main Sentry SDK Settings ~~~~~~~~~~~~~~~~~~~~~ #
dsn = "https://095db58be12ddc97d99d63cf67b708b4@o4506262420520960.ingest.sentry.io/4506262426550272"
traces_sample_rate = 1.0
profiles_sample_rate = 1.0
# ~~~~~~~~~~~~~~~~~~~~~ Main Sentry SDK Settings ~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~ Main Redis Settings ~~~~~~~~~~~~~~~~~~~~~ #
redis_url = "redis://localhost:6379"
# ~~~~~~~~~~~~~~~~~~~~~ Main Redis Settings ~~~~~~~~~~~~~~~~~~~~~ #


# ~~~~~~~~~~~~~~~~~~~~~ Main JWT Settings ~~~~~~~~~~~~~~~~~~~~~ #
jwt_private = '''-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgGqLX6sPxUjuRhxPpBkw1cv3S1JBSYpnTr1Kv+j45Irgk8YwPpnD
nfFW5YaYBkSmPWX2piIgH/4yTbkIqIsI/dqiOzkg+UNIHcWEL1U9+KiuHC+puYVD
4b3QRwVFO/1tbC0LBB7fnTYpeAn1QpjEz9A4hlrIGT4GYsAk5h0SM1StAgMBAAEC
gYAUxfvvNHH42ExfNMAAEV9+F0deUFBwZdgaXDqyx+R3l3X4jGuIO3XOGm1CIt4G
AIu0F7Uori7OtywkSaXjBevItSIgeFVvj+o4kZi8J8BjwHoBgF19pXp7u6VE7dfR
ANzVVZtlJWkLsH+1XC825I6OSsGklzpUVjOwRdsmcwi6GQJBAM36xr5BXzrh3a4z
GWSZo8NM2QQOhBkcwFxPlz83gSLEPGEBB8O8y6sO+JnMvaPBzoAAbQODCUfdMNzv
5qMc5f8CQQCEavfEAeZtw6Y07CGN3tlOELs2arveWwYQsiOiJqW1kCKfBMIRDd9D
ey6HkI9xkGn0JZ3F4/0JsL6STRNo+T1TAkAgG79vWPFnVF4iEYUb0XddslUB9OFS
qNCzkxSYniZbLQvcczSqpnt5JtRJ5UiKhmOSQH691WdU9H3xctQZCSAxAkBTzvvn
06gLGsRsRHNsPnpc3VwQMfeb4RJyqLzC2SESTBqNeM53SsdfB2zIomcXYmac/t3f
rM+vPW0wXZYGX5E/AkEAr206M6is5KpU3/4+2HxlqYa7XZKm4xWH2U+2TCyxnWp3
iMSlI6seGuoVrXU32VQZIvSBZqwdz0tLOfz3ohwRfg==
-----END RSA PRIVATE KEY-----'''

jwt_public = '''-----BEGIN PUBLIC KEY-----
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgGqLX6sPxUjuRhxPpBkw1cv3S1JB
SYpnTr1Kv+j45Irgk8YwPpnDnfFW5YaYBkSmPWX2piIgH/4yTbkIqIsI/dqiOzkg
+UNIHcWEL1U9+KiuHC+puYVD4b3QRwVFO/1tbC0LBB7fnTYpeAn1QpjEz9A4hlrI
GT4GYsAk5h0SM1StAgMBAAE=
-----END PUBLIC KEY-----'''

algorithm = 'RS256'

# ~~~~~~~~~~~~~~~~~~~~~ Main JWT Settings ~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~ Main VK OAUTH Settings ~~~~~~~~~~~~~~~~~~~~~ #
vk_token = 'd945393ed945393ed945393ed7da5307badd945d945393ebc09ca09a3bd83c6f3511985'
# ~~~~~~~~~~~~~~~~~~~~~ Main VK OAUTH Settings ~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~ Main Google OAUTH Settings ~~~~~~~~~~~~~~~~~~~~~ #
google_app = '325872434874-jagdj7khlgans5s8b3bi5ssf5c2vva7r.apps.googleusercontent.com'
# ~~~~~~~~~~~~~~~~~~~~~ Main Google OAUTH Settings ~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~ Main Logging Settings ~~~~~~~~~~~~~~~~~~~~~ #
SpaceLog_host = 'http://127.0.0.1:81'
SpaceLog_service = 'user'
SpaceLog_project = 'AitiSpace'
# ~~~~~~~~~~~~~~~~~~~~~ Main Logging Settings ~~~~~~~~~~~~~~~~~~~~~ #
