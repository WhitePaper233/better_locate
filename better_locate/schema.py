from typing import List

from pydantic import BaseModel, RootModel


class ShortcutSchemaItem(BaseModel):
    id: str
    name: str

class ShortcutSchema(RootModel[List[ShortcutSchemaItem]]):
    pass
