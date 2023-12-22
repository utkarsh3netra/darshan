import json
import graphene
import os


class Query(graphene.ObjectType):
    name = graphene.String(value = graphene.String( default_value="Darshan"))
    age = graphene.String()

    def resolve_name(self, info, value):
        return value
    def resolve_age(self, info):
        return "23"


schema = graphene.Schema(query=Query)
print(schema)


# Graph QL Query

query_test = '''
query myquery{
    my_name: name(value:"Darshan Ladani")
    my_age: age
}
'''
result = schema.execute(query_test)
print(json.dumps(result.data, indent=5))
