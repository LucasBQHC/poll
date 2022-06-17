from nyoibo import Entity, fields


class OwnerDTO(Entity):

    _first_name = fields.StrField(required=True)
    _last_name = fields.StrField(required=True)
    _username = fields.StrField(required=True)
