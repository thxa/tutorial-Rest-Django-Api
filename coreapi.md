Load The schema
    
    coreapi get http://127.0.0.1:8000/schema/

Listing the existing <app>

    coreapi action <app> list

See detail app

    coreapi action <app> <detail> --param id=<id the app detail>

Authenticating

    coreapi credentials add 127.0.0.1 <username>:<password> --auth basic
    coreapi reload
    coreapi action <app> create --param <detail>="Example" --param <detail>="test"

Delete the app

    coreapi action <app> delete --param id=<id the app detail>
