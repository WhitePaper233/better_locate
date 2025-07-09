from pydantic import BaseModel

from better_locate.permission_level import PermissionLevel


class PermissionConfig(BaseModel):
    any: PermissionLevel.Kind = 'admin'
    favourite_list: PermissionLevel.Kind = 'user'

class Config(BaseModel):
    permission: PermissionConfig = PermissionConfig()
