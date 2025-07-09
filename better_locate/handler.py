import re
from typing import Callable, cast

from mcdreforged.api.decorator import new_thread
from mcdreforged.command.builder.common import CommandContext
from mcdreforged.command.builder.nodes.basic import RUNS_CALLBACK
from mcdreforged.command.command_source import CommandSource, InfoCommandSource
from mcdreforged.minecraft.rtext.style import RColor, RAction
from mcdreforged.minecraft.rtext.text import RTextList, RText
from mcdreforged.plugin.si.plugin_server_interface import PluginServerInterface

from better_locate.schema import ShortcutSchema

pattern = r'at \[([-\d]+),\s*([~\d\-]+),\s*([-\d]+)\] \((\d+) blocks away\)'


def handle_structure_command(server: PluginServerInterface) -> Callable:
    @new_thread
    def inner(source: CommandSource, context: CommandContext):
        # ignore when command is not from player
        if not source.is_player:
            return

        # just type cast
        source = cast(InfoCommandSource, source)

        # parse structure id
        structure_id = context['id']

        # build query command
        command = f'execute at {source.get_info().player} run locate structure {f'{structure_id}'}'
        # handle query result
        result = server.rcon_query(command)

        # handle could not find
        if not result or result.startswith('Could not find'):
            source.reply(RText(f'无法找到结构: {f'{structure_id}'}', RColor.red))

        # match result message
        match = re.search(pattern, result)
        if match is not None:
            x, y, z, distance = match.groups()
            # reply result
            source.reply(RTextList(
                RText('最近的 '),
                RText(f'{structure_id}', RColor.aqua),
                RText(' 位于 '),
                RText(f'[{x}, {y}, {z}]', RColor.green),
                RText(f' ('),
                RText(f'{distance}', RColor.yellow),
                RText('个方块外)')
            ))

    return inner


def handle_list_structure_command(shortcuts: ShortcutSchema) -> RUNS_CALLBACK:
    def inner(source: CommandSource, _: CommandContext):
        texts = RTextList('\n=========== 快捷查询列表 ===========')
        for item in shortcuts.root:
            texts.append(
                RText('\n'),
                RText('[ + ]', RColor.aqua).h(f'点击查询结构: {item.id}').c(
                    RAction.run_command, f'!!locate structure {item.id}'
                ),
                RText(f' {item.name}', RColor.yellow),
            )
        source.reply(texts)

    return inner

def handle_biome_command(server: PluginServerInterface) -> Callable:
    @new_thread
    def inner(source: CommandSource, context: CommandContext):
        # ignore when command is not from player
        if not source.is_player:
            return

        # just type cast
        source = cast(InfoCommandSource, source)

        # parse biome id
        biome_id = context['id']

        # build query command
        command = f'execute at {source.get_info().player} run locate biome {f'{biome_id}'}'
        # handle query result
        result = server.rcon_query(command)

        # handle could not find
        if not result or result.startswith('Could not find'):
            source.reply(RText(f'无法找到群系: {f'{biome_id}'}', RColor.red))

        # match result message
        match = re.search(pattern, result)
        if match is not None:
            x, y, z, distance = match.groups()
            # reply result
            source.reply(RTextList(
                RText('最近的 '),
                RText(f'{biome_id}', RColor.aqua),
                RText(' 位于 '),
                RText(f'[{x}, {y}, {z}]', RColor.green),
                RText(f' ('),
                RText(f'{distance}', RColor.yellow),
                RText('个方块外)')
            ))

    return inner


def handle_list_biome_command(shortcuts: ShortcutSchema) -> RUNS_CALLBACK:
    def inner(source: CommandSource, _: CommandContext):
        texts = RTextList('\n=========== 快捷查询列表 ===========')
        for item in shortcuts.root:
            texts.append(
                RText('\n'),
                RText('[ + ]', RColor.aqua).h(f'点击查询群系: {item.id}').c(
                    RAction.run_command, f'!!locate biome {item.id}'
                ),
                RText(f' {item.name}', RColor.yellow),
            )
        source.reply(texts)

    return inner
