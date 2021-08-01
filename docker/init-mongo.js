db.createUser(
    {
        user : fielder,
        pwd : dbPass,
        roles: [
            {
                role    : "readWrite",
                db  :   "forms"
            }
        ]
    
    }
)