import graphene
from graphene import Mutation, ObjectType, String, Field
from models import Card

class CardType(graphene.ObjectType):
    id = graphene.String()
    title = graphene.String()
    description = graphene.String()
    status = graphene.String()

class Query(ObjectType):
    card = Field(CardType, id=String(required=True))

    def resolve_card(self, info, id):
        card = Card.get_card(id)
        if card:
            return CardType(**card)
        return None

class CreateCard(Mutation):
    class Arguments:
        id = String(required=True)
        title = String(required=True)
        description = String(required=True)
        status = String(required=True)

    card = Field(lambda: CardType)

    def mutate(self, info, id, title, description, status):
        Card.create_card(id, title, description, status)
        card = Card(id=id, title=title, description=description, status=status)
        return CreateCard(card=card)

class UpdateCard(Mutation):
    class Arguments:
        id = String(required=True)
        title = String()
        description = String()
        status = String()

    card = Field(lambda: CardType)

    def mutate(self, info, id, title=None, description=None, status=None):
        Card.update_card(id, title, description, status)
        card = Card(id=id, title=title, description=description, status=status)
        return UpdateCard(card=card)

class DeleteCard(Mutation):
    class Arguments:
        id = String(required=True)

    card = Field(lambda: CardType)

    def mutate(self, info, id):
        card = Card.get_card(id)
        if card:
            Card.delete_card(id)
            return DeleteCard(card=card)
        return None

class Mutation(ObjectType):
    create_card = CreateCard.Field()
    update_card = UpdateCard.Field()
    delete_card = DeleteCard.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
