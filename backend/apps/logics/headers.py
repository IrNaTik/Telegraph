OPTIONS = {
    'Access-Control-Allow-Origin': 'http://localhost:3000',
    'Access-Control-Allow-Credentials': 'true',
    'Allow': 'OPTIONS, GET, POST',
}


LOGIN_OPTIONS = {**OPTIONS}
LOGIN_OPTIONS.update({'Access-Control-Allow-Headers':
                                '''Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers, Authorization'''})

    