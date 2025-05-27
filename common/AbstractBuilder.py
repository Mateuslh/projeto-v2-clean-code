class AbstractBuilder:
    """
    Builder genérico: cria a entidade, aplica setters fluentes
    e executa a validação antes de devolver o objeto pronto.
    """
    def __init__(self, entity=None):
        self.entity = entity or self._create_entity()
        self._skip_validate = False

    def _create_entity(self):
        raise NotImplementedError

    def skip_validate_(self):
        self._skip_validate = True
        return self

    def build(self):
        if not self._skip_validate:
            self.validate()
        return self.entity

    def validate(self):
        pass
