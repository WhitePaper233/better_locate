# BetterLocate

The locate command in MCDR, but more easier to use!

[中文文档](README_zh.md)

BetterLocate is a Minecraft server plugin for MCDReforged that enhances the default locate command with shortcuts and a user-friendly interface for finding structures and biomes in Minecraft.

## Features

- **Easy structure and biome locating**: Quickly find Minecraft structures and biomes with simple commands
- **Quick shortcuts**: Use simplified commands like `!!locate s` for structures and `!!locate b` for biomes
- **Interactive list interface**: Clickable list of available structures and biomes to locate
- **Chinese localization**: Commands and responses are in Chinese with colored text formatting
- **Integrated with Minecraft locate command**: Uses the native Minecraft `/locate` command in the background

## Commands

- `!!locate structure <id>` - Locate a specific Minecraft structure by ID
- `!!locate s <id>` - Shortcut for locating a structure
- `!!locate biome <id>` - Locate a specific Minecraft biome by ID
- `!!locate b <id>` - Shortcut for locating a biome
- `!!locate structure` - List all available structures to locate
- `!!locate biome` - List all available biomes to locate

## Predefined Structures

The plugin includes shortcuts for common Minecraft structures:
- Desert Village, Plains Village, Savanna Village, Taiga Village, Snowy Village
- Stronghold, Mineshaft
- Desert Pyramid, Jungle Pyramid, Swamp Hut
- Monument, Mansion
- Bastion Remnant, Ancient City
- Pillager Outpost, End City
- Fortress (Nether Fortress)

## Predefined Biomes

The plugin includes shortcuts for common Minecraft biomes:
- Plains, Forest, Flower Forest, Birch Forest, Dark Forest
- Taiga, Snowy Taiga
- Savanna, Jungle, Bamboo Jungle
- Desert, Badlands, Swamp, Mangrove Swamp
- Mountains, Meadow, Snowy Plains, Snowy Slopes
- Windswept Hills, Stony Peaks
- Beach, Ocean, Warm Ocean, Frozen Ocean
- River, Mushroom Fields
- Dripstone Caves, Lush Caves, Deep Dark
- Nether biomes: Nether Wastes, Warped Forest, Crimson Forest, Soul Sand Valley, Basalt Deltas
- End biomes: End Highlands, End Midlands, End Barrens, Small End Islands

## Permissions

The plugin has configurable permission levels:
- `any`: Permission level required to use locate commands (default: admin)
- `favourite_list`: Permission level required to view the shortcut lists (default: user)

## Configuration

The plugin can be configured by modifying the `config.py` file to adjust permission levels for different commands.

## How It Works

The plugin works by sending commands to the Minecraft server using RCON to execute the native `/locate` command, then parsing the response to extract coordinates and distance information. The results are formatted with rich text and sent back to the player.

## Requirements

- MCDReforged >= 2.1.4
- Minecraft server with RCON enabled
- Python 3.8 or higher
