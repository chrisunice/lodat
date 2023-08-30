# Mongo shell needs to be installed in the /bin folder for the MongoDB server
# Typically located in C:\Program Files\MongoDB\Server\6.0\bin
# The /bin folder must also exist in the environment variables
mongosh
use admin
db.createUser(
    {
        user: "cunice",
        pwd: passwordPrompt(),
        roles: [
            {role: "userAdminAnyDatabase", db: "admin" },
            {role: "readWriteAnyDatabase", db: "admin" }
        ]
    }
)