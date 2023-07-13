# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
from sem_10.task_6 import Fish, Birds, Mammal


class Factory:
    def create_object(class_name, name, specific):
        dict_classes = {"Fish": Fish, "Birds": Birds, "Mammal": Mammal}
        if dict_classes[class_name]:
            return dict_classes[class_name](name, specific)
        else:
            return 'invalid class'


b1 = Factory.create_object('Fish', 'karas', 1)
c1 = Factory.create_object('Birds', 'penguin', 2)
print(b1)
print(b1.specific)
print(b1.get_specific())
print(c1)
print(c1.name)
print(c1.get_specific())
