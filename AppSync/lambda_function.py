try:
    import json

    import os
    import shutil
    import uuid
    print("All Modules are ok ...")
except Exception as e:
    print("Error in Imports ")


def getUsers(event, context):

    if event.get("info").get("fieldName") == "getUsers":
        """
        Add business Logic here 
        """
        return {
                "GSI_1_pk": "Hello, world!",
                "GSI_1_sk": "Hello, world!",
                "pk":"Darshan#darshan",
                "sk": "Hello, world!"
            }