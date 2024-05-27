import graphene
from graphene import Mutation, ObjectType, String, Field, List, Int, Enum
from models import Card

class StatusEnum(Enum):
    IN_PROGRESS = "In Progress"
    TO_DO = "To Do"
    DONE = "Done"

class CardType(graphene.ObjectType):
    id = graphene.String()
    title = graphene.String()
    description = graphene.String()
    status = graphene.String()

class Query(ObjectType):
    card = Field(CardType, id=String(required=True))
    cards_by_status = Field(List(CardType), status=List(StatusEnum), last_evaluated_key=String(), limit=Int(default_value=10))

    def resolve_card(self, info, id):
        card = Card.get_card(id)
        if card:
            return CardType(**card)
        return None

    def resolve_cards_by_status(self, info, status=None, last_evaluated_key=None, limit=10):
        all_cards = []
        status_values = status
        if status is None or len(status) == 0:
            status_values = [e.value for e in StatusEnum._meta.enum.__members__.values()]
        for stat in status_values:
            cards, last_key = Card.query_cards_by_status(stat, last_evaluated_key, limit)
            all_cards.extend(cards)
        return all_cards

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
