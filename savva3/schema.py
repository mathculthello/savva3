import graphene

from base.schema import Query as BaseQuery
from events.schema import Query as EventQuery

class Query(BaseQuery, EventQuery, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
