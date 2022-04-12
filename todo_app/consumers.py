from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin

from .serializers import UserSerializer, TodoSerializer
from .models import User, Todo


class MyConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    @model_observer(Todo)
    async def todo_activity(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @todo_activity.serializer
    def todo_activity(self, instance, action, **kwargs):
        return dict(data=TodoSerializer(instance).data, action=action.value)

    @todo_activity.groups_for_signal
    def todo_activity(self, instance: Todo, **kwargs):
        yield f'owner__{instance.owner_id}'
        yield f'pk__{instance.pk}'

    @todo_activity.groups_for_consumer
    def todo_activity(self, owner=None, **kwargs):
        if owner is not None:
            yield f'owner__{owner}'

    @action()
    async def subscribe_to_todo_activity(self, pk,  **kwargs):
        if "user" in self.scope and self.scope["user"].is_authenticated:
            await self.todo_activity.subscribe(owner=pk)
