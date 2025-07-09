import json

from mcdreforged.plugin.si.plugin_server_interface import PluginServerInterface

from better_locate.command import Command
from better_locate.config import Config
from better_locate.permission_level import PermissionLevel
from better_locate.schema import ShortcutSchema


async def on_load(server: PluginServerInterface, _):
    structures = []
    with server.open_bundled_file("data/structures.json") as file_handler:
        content = file_handler.read().decode('utf-8')
        structures = ShortcutSchema.model_validate(json.loads(content))

    biomes = []
    with server.open_bundled_file("data/biomes.json") as file_handler:
        content = file_handler.read().decode('utf-8')
        biomes = ShortcutSchema.model_validate(json.loads(content))

    Command(server, structures, biomes).register_to(server)
