from payload.parser import parse

themes = [
    {
        "name":"nether",
        "white_tile":"warped_nylium",
        "black_tile":"crimson_nylium",
        "white_selected":"glowstone",
        "black_selected":"shroomlight",
        "white_move":"warped_stem[axis=z]",
        "black_move":"crimson_stem[axis=z]",
        "white_attack":"red_nether_bricks",
        "black_attack":"nether_bricks",
        "white_pawn":"quartz_pillar",
        "black_pawn":"polished_basalt",
        "check_unselected":"ancient_debris",
        "check_selected":"netherite_block",
        "stalemate":"netherite_block",
        "checkmate":"magma_block",
        "check_assisted":"gilded_blackstone"
    },{
        "name":"stone",
        "white_tile":"stone",
        "black_tile":"blackstone",
        "white_selected":"sandstone",
        "black_selected":"red_sandstone",
        "white_move":"basalt",
        "black_move":"tuff",
        "white_attack":"granite",
        "black_attack":"diorite",
        "white_pawn":"prismarine",
        "black_pawn":"netherrack",
        "check_unselected":"dripstone_block",
        "check_selected":"calcite",
        "stalemate":"obsidian",
        "checkmate":"bedrock",
        "check_assisted":"crying_obsidian"
    },{
        "name":"wood",
        "white_tile":"beehive",
        "black_tile":"barrel[facing=down]",
        "white_selected":"note_block",
        "black_selected":"note_block",
        "white_move":"piston[facing=up]",
        "black_move":"piston[facing=up]",
        "white_attack":"target",
        "black_attack":"target",
        "white_pawn":"smoker",
        "black_pawn":"barrel[facing=up,open=true]",
        "check_unselected":"observer[facing=down]",
        "check_selected":"dispenser[facing=up]",
        "stalemate":"raw_gold_block",
        "checkmate":"tnt",
        "check_assisted":"piston[facing=down]"
    },{
        "name":"spiral",
        "white_tile":"stripped_oak_log",
        "black_tile":"stripped_spruce_log",
        "white_selected":"yellow_shulker_box[facing=down]",
        "black_selected":"orange_shulker_box[facing=down]",
        "white_move":"lime_shulker_box[facing=down]",
        "black_move":"green_shulker_box[facing=down]",
        "white_attack":"red_shulker_box[facing=down]",
        "black_attack":"brown_shulker_box[facing=down]",
        "white_pawn":"white_shulker_box[facing=down]",
        "black_pawn":"gray_shulker_box[facing=down]",
        "check_unselected":"stripped_mangrove_log",
        "check_selected":"target",
        "stalemate":"warped_stem",
        "checkmate":"crimson_stem",
        "check_assisted":"stripped_acacia_log"
    },{
        "name":"ore",
        "white_tile":"stone",
        "black_tile":"deepslate[axis=z]",
        "white_selected":"gold_ore",
        "black_selected":"deepslate_gold_ore",
        "white_move":"emerald_ore",
        "black_move":"deepslate_emerald_ore",
        "white_attack":"redstone_ore",
        "black_attack":"deepslate_redstone_ore",
        "white_pawn":"lodestone",
        "black_pawn":"netherite_block",
        "check_unselected":"netherrack",
        "check_selected":"nether_gold_ore",
        "stalemate":"gold_block",
        "checkmate":"redstone_block",
        "check_assisted":"red_concrete"
    },{
        "name":"nature",
        "white_tile":"grass_block",
        "black_tile":"mycelium",
        "white_selected":"rooted_dirt",
        "black_selected":"podzol",
        "white_move":"sand",
        "black_move":"gravel",
        "white_attack":"warped_nylium",
        "black_attack":"crimson_nylium",
        "white_pawn":"clay",
        "black_pawn":"mud",
        "check_unselected":"tuff",
        "check_selected":"smooth_basalt",
        "stalemate":"dark_prismarine",
        "checkmate":"sea_lantern",
        "check_assisted":"prismarine"
    },{
        "name":"end",
        "white_tile":"end_stone",
        "black_tile":"obsidian",
        "white_selected":"shulker_box",
        "black_selected":"purple_shulker_box",
        "white_move":"amethyst_block",
        "black_move":"crying_obsidian",
        "white_attack":"red_shulker_box",
        "black_attack":"red_shulker_box",
        "white_pawn":"quartz_pillar",
        "black_pawn":"purpur_pillar",
        "check_unselected":"bedrock",
        "check_selected":"reinforced_deepslate",
        "stalemate":"jigsaw[orientation=down_west]",
        "checkmate":"structure_block",
        "check_assisted":"smithing_table"
    },{
        "name":"sculk",
        "white_tile":"end_stone",
        "black_tile":"sculk",
        "white_selected":"honeycomb_block",
        "black_selected":"obsidian",
        "white_move":"prismarine",
        "black_move":"netherrack",
        "white_attack":"blue_ice",
        "black_attack":"magma_block",
        "white_pawn":"amethyst_block",
        "black_pawn":"gilded_blackstone",
        "check_unselected":"melon",
        "check_selected":"pumpkin",
        "stalemate":"bedrock",
        "checkmate":"reinforced_deepslate",
        "check_assisted":"crying_obsidian"
    },{
        "name":"NAME GOES HERE",
        "white_tile":"stripped_pale_oak_log",
        "black_tile":"respawn_anchor",
        "white_selected":"white_shulker_box[facing=down]",
        "black_selected":"gray_concrete",
        "white_move":"white_shulker_box[facing=down]",
        "black_move":"gray_concrete",
        "white_attack":"purple_shulker_box",
        "black_attack":"purple_shulker_box",
        "white_pawn":"jigsaw[orientation=down_west]",
        "black_pawn":"jigsaw[orientation=down_west]",
        "check_unselected":"red_shulker_box",
        "check_selected":"red_concrete_powder",
        "stalemate":"light_gray_concrete",
        "checkmate":"bedrock",
        "check_assisted":"purple_shulker_box"
    #},{
    #    "name":"light",
    #    "white_tile":"sea_lantern",
    #    "black_tile":"glowstone",
    #    "white_selected":"verdant_froglight",
    #    "black_selected":"pearlescent_froglight",
    #    "white_move":"stripped_bamboo_block",
    #    "black_move":"bamboo_block",
    #    "white_attack":"ochre_froglight",
    #    "black_attack":"shroomlight",
    #    "white_pawn":"respawn_anchor[charges=4]",
    #    "black_pawn":"respawn_anchor",
    #    "check_unselected":"redstone_lamp[lit=false]",
    #    "check_selected":"redstone_lamp[lit=true]",
    #    "stalemate":"sculk_catalyst",
    #    "checkmate":"sculk_catalyst[bloom=true]",
    #    "check_assisted":"magma_block"
    }
]
commands = {
    "white_move":"execute at @n[tag=chess.main] as @e[tag=chess.calculate.moveable,tag=!chess.calculate.selected,tag=!chess.calculate.check,distance=..7,nbt={Fire:0s},nbt=!{Item:{}}] on vehicle at @s unless entity @e[tag=chess.calculate.move,distance=...5,nbt={data:{passant:1}}] run setblock ~ ~-.1 ~ $(white_move)",
    "black_move":"execute at @n[tag=chess.main] as @e[tag=chess.calculate.moveable,tag=!chess.calculate.selected,tag=!chess.calculate.check,distance=..7,nbt={Fire:1s},nbt=!{Item:{}}] on vehicle at @s unless entity @e[tag=chess.calculate.move,distance=...5,nbt={data:{passant:1}}] run setblock ~ ~-.1 ~ $(black_move)",
    "white_attack":"execute at @n[tag=chess.main] as @e[tag=chess.calculate.moveable,tag=!chess.calculate.selected,tag=!chess.calculate.check,distance=..7,nbt={Fire:0s}] on vehicle at @s unless block ~ ~-.1 ~ $(white_move) run setblock ~ ~-.1 ~ $(white_attack)",
    "black_attack":"execute at @n[tag=chess.main] as @e[tag=chess.calculate.moveable,tag=!chess.calculate.selected,tag=!chess.calculate.check,distance=..7,nbt={Fire:1s}] on vehicle at @s unless block ~ ~-.1 ~ $(black_move) run setblock ~ ~-.1 ~ $(black_attack)",
    "white_selected":"execute at @n[tag=chess.main] as @e[tag=chess.calculate.selected,tag=!chess.calculate.check,distance=..7,nbt={Fire:0s}] on vehicle at @s run setblock ~ ~-.1 ~ $(white_selected)",
    "black_selected":"execute at @n[tag=chess.main] as @e[tag=chess.calculate.selected,tag=!chess.calculate.check,distance=..7,nbt={Fire:1s}] on vehicle at @s run setblock ~ ~-.1 ~ $(black_selected)",
    "white_tile":"execute at @n[tag=chess.main] as @e[tag=chess.item,tag=!chess.calculate.moveable,tag=!chess.calculate.check,distance=..7,nbt={Fire:0s}] on vehicle at @s run setblock ~ ~-.1 ~ $(white_tile)",
    "black_tile":"execute at @n[tag=chess.main] as @e[tag=chess.item,tag=!chess.calculate.moveable,tag=!chess.calculate.check,distance=..7,nbt={Fire:1s}] on vehicle at @s run setblock ~ ~-.1 ~ $(black_tile)",
    "check_unselected":"execute at @n[tag=chess.main] as @e[tag=chess.calculate.check,tag=!chess.calculate.selected,distance=..7] on vehicle at @s run setblock ~ ~-.1 ~ $(check_unselected)",
    "stalemate":"execute at @n[tag=chess.calculate] unless entity @e[tag=chess.calculate.legal,distance=..7] as @e[tag=chess.item,nbt={Item:{components:{\\'minecraft:custom_data\\':{Chess:[king]}}}},scores={chess.team=1},distance=..7] at @s unless entity @e[tag=chess.calculate.piece,distance=...5,scores={chess.score=1..}] store result entity @n[tag=chess.calculate] data.end int 1 on vehicle at @s run setblock ~ ~-.1 ~ $(stalemate)",
    "checkmate":"execute at @n[tag=chess.calculate] unless entity @e[tag=chess.calculate.legal,distance=..7] as @e[tag=chess.item,nbt={Item:{components:{\\'minecraft:custom_data\\':{Chess:[king]}}}},scores={chess.team=1},distance=..7] at @s at @e[tag=chess.calculate.piece,distance=...5,scores={chess.score=1..}] store result entity @n[tag=chess.calculate] data.end int 1 on vehicle at @s run setblock ~ ~-.1 ~ $(checkmate)",
    "check_selected":"execute at @n[tag=chess.main] as @e[tag=chess.calculate.check,tag=chess.calculate.selected,distance=..7] on vehicle at @s run setblock ~ ~-.1 ~ $(check_selected)",
    "check_assisted":"execute at @n[tag=chess.calculate,nbt={data:{end:1}}] at @e[tag=chess.calculate.king_move,scores={chess.team=1},distance=..8] unless entity @e[tag=chess.item,nbt=!{Item:{Chess:[king]}},distance=...5,scores={chess.team=1}] at @e[tag=chess.calculate.move,tag=!pwnfwd,distance=...5,scores={chess.team=2,chess.move=1..}] as @e[tag=chess.item,scores={chess.team=2},distance=..8] if score @s chess.id = @n[tag=chess.calculate.move] chess.id on vehicle at @s run setblock ~ ~-.1 ~ $(check_assisted)",
    "white_pawn":"data merge the block display $(white_pawn)",
    "black_pawn":"data merge the block display $(black_pawn)"
}

def get_theme_commands():
    data = {}
    for block_type, command in commands.items():
        data[block_type] = []
        for theme in themes:
            parsed_command = ""
            for substring in parse.split_by_actions(command):
                if len(substring) > 0 and substring[0] == "$":
                    parsed_command = parsed_command + theme[substring[1:]]
                else:
                    parsed_command = parsed_command + substring
            data[block_type].append(parsed_command)
        data[block_type] = '["' + '","'.join(data[block_type]) + '"]'
    return data