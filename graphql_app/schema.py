import graphene

# define a query with a field called 'hello'
class Query(graphene.ObjectType):
    hello = graphene.String()

    # The resolution function for each field starts with 'resolve_' followed by the name of field
    def resolve_hello(self, info):
        return "Hello!"


schema = graphene.Schema(query=Query)
