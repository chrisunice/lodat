"""
1. Open MongoDB Compass
2. Open mongo shell (MONGOSH)
3. Type
    use admin
    db.createUser(
      {
        user: "cunice",
        pwd: passwordPrompt(),
        roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase", "dbAdminAnyDatabase" ]
      }
    )
4. Should see an {ok:1} response
5. Open mongod.cfg file in C:\Program Files\MongoDB\Server\4.2\bin
6. Add the following to the #security section
    security:
      authorization: enabled
7. Save the file
8. Restart MongoDB using services.msc
    WIN + R
    services.msc
    right click MongoDB
    restart
9. Run the below python code to confirm

To update roles:
Example adding the ability to drop databases

1. mongo -u cunice --authenticationDatabase admin -p
    access database using authentication and prompt for password

2. use admin
    switch to admin database

3. db.grantRolesToUser("cunice", [{ role: "dbAdminAnyDatabase", db: "admin" }])
    add a new role to the user

4. db.getUser("cunice")
    show that the new role was added
"""
import pymongo

mongo_host = '127.0.0.1'
mongo_port = 27017

# Connect without authentication
client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
print(client.list_database_names())     # should throw an error

# Connect with authentication
username = 'myusername'     # TODO replace
password = 'mypassword'     # TODO replace
auth_source = 'admin'  # The authentication database, usually 'admin'
uri = f"mongodb://{username}:{password}@{mongo_host}:{mongo_port}/{auth_source}"
client = pymongo.MongoClient(uri)
print(client.list_database_names())     # should print database names
