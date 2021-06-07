#  Идея паттерна проста. У нас есть класс controller, что контролирует скажем state и хранит внутри себя список тех,
#  кому важны изменения в стэйте. Таким образом, каждый раз когда state меняется controller может послать сообщения
#  своим подпищитам.

#  Точно так и работает скажем Redux

from abc import ABC, abstractmethod


class ReactComponent(ABC):
    def __init__(self, state):
        self._state = state

    def update(self, state):
        self._state.update(state)

    @abstractmethod
    def render(self):
        pass


class ReduxState:
    def __init__(self, subscribers):
        self.subscribers = subscribers

    def add_sub(self, sub):
        self.subscribers.append(sub)

    def remove_sub(self, sub):
        self.subscribers.remove(sub)

    def update_state(self, state):
        for sub in self.subscribers:
            sub.update(state)


class Header(ReactComponent):
    def render(self):
        print(f'Rendering {self._state["header"]}')


class Footer(ReactComponent):
    def render(self):
        print(f'Rendering {self._state["footer"]}')


header = Header({'header': '<header></header>'})
footer = Footer({'footer': '<footer></footer>'})

store = ReduxState([header])
store.add_sub(footer)

footer.render()  # Rendering <footer></footer>
header.render()  # Rendering <header></header>

store.update_state({'header': '<header>Some value</header>', 'footer': '<footer></footer>'})
header.render()  # Rendering <header>Some value</header>
footer.render()  # Rendering <footer></footer>
