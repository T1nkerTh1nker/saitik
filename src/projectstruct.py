class ProjectStruct:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_dict(self):
        ret = {'name': self.name, 'description': self.description}
