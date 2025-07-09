from enum import Enum

from mcdreforged.command.builder.nodes.arguments import GreedyText
from mcdreforged.command.builder.nodes.basic import Literal
from mcdreforged.plugin.si.plugin_server_interface import PluginServerInterface

from better_locate.handler import handle_structure_command, handle_list_structure_command, handle_biome_command, \
    handle_list_biome_command
from better_locate.schema import ShortcutSchema


class Command:
    command = Literal('!!locate')

    @staticmethod
    def shortcuts_to_enum(shortcuts: ShortcutSchema):
        members = {item.id: item.id for item in shortcuts.root}
        return Enum('ShortcutIdEnum', members)

    def __init__(self, server: PluginServerInterface, structures: ShortcutSchema, biomes: ShortcutSchema):
        self.command.then(
            # like !!locate structure <id>
            Literal('structure').then(
                GreedyText('id').runs(
                    handle_structure_command(server)
                )
            ).runs(handle_list_structure_command(structures))
        ).then(
            # like !!locate s <id>, simplified version of structure
            Literal('s').then(
                GreedyText('id').runs(
                    handle_structure_command(server)
                )
            ).runs(handle_list_structure_command(structures))
        ).then(
            # !!locate biome <id>
            Literal('biome').then(
                GreedyText('id').runs(
                    handle_biome_command(server)
                )
            ).runs(handle_list_biome_command(biomes))
        ).then(
            # like !!locate b <id>, simplified version of biome
            Literal('b').then(
                GreedyText('id').runs(
                    handle_biome_command(server)
                )
            ).runs(handle_list_biome_command(biomes))
        )

    def register_to(self, server: PluginServerInterface):
        server.register_command(self.command)
