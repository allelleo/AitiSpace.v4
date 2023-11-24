# ~~~~~~~~~~~~~~~~~~~~~ Main Server Settings ~~~~~~~~~~~~~~~~~~~~~ #
HOST = '127.0.0.1'
PORT = 81
# ~~~~~~~~~~~~~~~~~~~~~ Main Server Settings ~~~~~~~~~~~~~~~~~~~~~ #

# ~~~~~~~~~~~~~~~~~~~~~ Main database Settings ~~~~~~~~~~~~~~~~~~~~~ #
db_url = 'sqlite://database.db'
generate_schemas = True
add_exception_handlers = True

models = [
    'spacelog.models',
]
# ~~~~~~~~~~~~~~~~~~~~~ Main database Settings ~~~~~~~~~~~~~~~~~~~~~ #
