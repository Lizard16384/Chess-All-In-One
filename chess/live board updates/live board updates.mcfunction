summon falling_block ~ ~.8 ~ {BlockState:{Name:redstone_block},Passengers:[{id:falling_block,BlockState:{Name:activator_rail}},
{id:command_block_minecart,Command:"setblock ~ ~-2 ~ repeating_command_block{auto:1,Command:'fill ~ ~ ~ ~ ~2 ~ air'}"},

execute align y run summon armor_stand ~ ~-2 ~ {UUID:uuid('68656c6c-6f20-7468-6572-65207772656e'),Health:0,DeathTime:19,Marker:1,Invisible:1,equipment:{mainhand:{id:waxed_weathered_cut_copper_stairs,components:{item_model:air}}}}"},{id:command_block_minecart,Command:"

setblock $(+setup_n) command_block[facing=$(setup_next)]{auto:1,Command:'setblock ~ ~ ~ air'}"},{id:command_block_minecart,Command:'
setblock $(+setup_n) chain_command_block[facing=$(setup_next)]{auto:1,UpdateLastExecution:0,Command:\'execute as 68656c6c-6f20-7468-6572-65207772656e run item modify entity @s weapon.mainhand {"function":"minecraft:set_name","entity":"this","name":[]}\'}'},{id:command_block_minecart,Command:"
setblock $(+setup_n) chain_command_block[facing=$(setup_next)]{auto:1,UpdateLastExecution:0,Command:'enchant 68656c6c-6f20-7468-6572-65207772656e projectile_protection'}"},{id:command_block_minecart,Command:"
setblock $(+setup_n) chain_command_block[facing=$(setup_next)]{auto:1,UpdateLastExecution:0,Command:'data modify block $(setup_n:->:setup_n+1) Command set from block $(setup_n:->:setup_n-1) LastOutput.extra[0].extra[0].with[0]'}"},{id:command_block_minecart,Command:"
setblock $(+setup_n) chain_command_block[facing=$(setup_next)]{auto:1,UpdateLastExecution:0}"},{id:command_block_minecart,Command:"
setblock $(+setup_n) chain_command_block[facing=$(setup_next)]{auto:1,UpdateLastExecution:0,Command:'data remove entity 68656c6c-6f20-7468-6572-65207772656e data.commands[0]'}"},{id:command_block_minecart,Command:"
setblock $(+setup_n) chain_command_block[facing=$(setup_n:~:setup2)]{auto:1,UpdateLastExecution:0,Command:'execute unless data entity 68656c6c-6f20-7468-6572-65207772656e data.commands[0] run setblock $(setup_n:->:setup2) chain_command_block[facing=$(setup2:~:init1)]{auto:1,UpdateLastExecution:0}'}"},{id:command_block_minecart,Command:"

summon marker $(entity_light_tile) {Tags:[chess.live,chess.live.light_tile],data:{set:[
    'execute at @n[tag=chess.menu.entity,type=command_block_minecart] run data modify block $(menu:->:light_tile) Command set value \\'',{nbt:'data.command',entity:'@n[tag=chess.live.light_tile]',interpret:1},'\\''
    ],command:[
    'execute at @n[tag=chess.main] as @e[tag=chess.item,tag=!chess.calculate.moveable,tag=!chess.calculate.check,distance=..7,nbt={Fire:0s}] on vehicle at @s run clone ',
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.light_tile]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.light_tile]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.light_tile]'},' ',{nbt:'data.pos_x','entity':'@n[tag=chess.live.light_tile]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.light_tile]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.light_tile]'},
    ' ~ ~-.1 ~']}}"},{id:command_block_minecart,Silent:1,Command:"
summon marker $(entity_light_selected) {Tags:[chess.live,chess.live.light_selected],data:{set:[
    'execute at @n[tag=chess.menu.entity,type=command_block_minecart] run data modify block $(menu:->:light_selected) Command set value \\'',{nbt:'data.command',entity:'@n[tag=chess.live.light_selected]',interpret:1},'\\''
    ],command:[
    'execute at @n[tag=chess.main] as @e[tag=chess.calculate.selected,tag=!chess.calculate.check,distance=..7,nbt={Fire:0s}] on vehicle at @s run clone ',
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.light_selected]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.light_selected]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.light_selected]'},' ',{nbt:'data.pos_x','entity':'@n[tag=chess.live.light_selected]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.light_selected]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.light_selected]'},
    ' ~ ~-.1 ~']}}"},{id:command_block_minecart,Silent:1,Command:"
summon marker $(entity_light_moveable) {Tags:[chess.live,chess.live.light_moveable],data:{set:[
    'execute at @n[tag=chess.menu.entity,type=command_block_minecart] run data modify block $(menu:->:light_moveable) Command set value \\'',{nbt:'data.command',entity:'@n[tag=chess.live.light_moveable]',interpret:1},'\\''
    ],command:[
    'execute at @n[tag=chess.main] as @e[tag=chess.calculate.moveable,tag=!chess.calculate.selected,tag=!chess.calculate.check,distance=..7,nbt={Fire:0s},nbt=!{Item:{}}] on vehicle at @s unless entity @e[tag=chess.calculate.move,distance=...5,nbt={data:{passant:1}}] run clone ',
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.light_moveable]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.light_moveable]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.light_moveable]'},' ',{nbt:'data.pos_x','entity':'@n[tag=chess.live.light_moveable]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.light_moveable]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.light_moveable]'},
    ' ~ ~-.1 ~']}}"},{id:command_block_minecart,Silent:1,Command:"
summon marker $(entity_light_attack) {Tags:[chess.live,chess.live.light_attack],data:{set:[
    'execute at @n[tag=chess.menu.entity,type=command_block_minecart] run data modify block $(menu:->:light_attack) Command set value \\'',{nbt:'data.command',entity:'@n[tag=chess.live.light_attack]',interpret:1},'\\''
    ],command:[
    'execute at @n[tag=chess.main] as @e[tag=chess.calculate.moveable,tag=!chess.calculate.selected,tag=!chess.calculate.check,distance=..7,nbt={Fire:0s}] on vehicle at @s unless blocks ~ ~-.1 ~ ~ ~-.1 ~ ',
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.light_moveable]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.light_moveable]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.light_moveable]'},
    ' all run clone '
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.light_attack]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.light_attack]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.light_attack]'},' ',{nbt:'data.pos_x','entity':'@n[tag=chess.live.light_attack]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.light_attack]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.light_attack]'},
    '~ ~-.1 ~']}}"},{id:command_block_minecart,Silent:1,Command:"
summon marker $(entity_dark_tile) {Tags:[chess.live,chess.live.dark_tile],data:{set:[
    'execute at @n[tag=chess.menu.entity,type=command_block_minecart] run data modify block $(menu:->:dark_tile) Command set value \\'',{nbt:'data.command',entity:'@n[tag=chess.live.dark_tile]',interpret:1},'\\''
    ],command:[
    'execute at @n[tag=chess.main] as @e[tag=chess.item,tag=!chess.calculate.moveable,tag=!chess.calculate.check,distance=..7,nbt={Fire:1s}] on vehicle at @s run clone '
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.dark_tile]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.dark_tile]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.dark_tile]'}, ' ',{nbt:'data.pos_x','entity':'@n[tag=chess.live.dark_tile]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.dark_tile]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.dark_tile]'},
    ' ~ ~-.1 ~']}}"},{id:command_block_minecart,Silent:1,Command:"
summon marker $(entity_dark_selected) {Tags:[chess.live,chess.live.dark_selected],data:{set:[
    'execute at @n[tag=chess.menu.entity,type=command_block_minecart] run data modify block $(menu:->:dark_selected) Command set value \\'',{nbt:'data.command',entity:'@n[tag=chess.live.dark_selected]',interpret:1},'\\''
    ],command:[
    'execute at @n[tag=chess.main] as @e[tag=chess.calculate.selected,tag=!chess.calculate.check,distance=..7,nbt={Fire:1s}] on vehicle at @s run clone '
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.dark_selected]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.dark_selected]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.dark_selected]'}, ' ',{nbt:'data.pos_x','entity':'@n[tag=chess.live.dark_selected]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.dark_selected]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.dark_selected]'},
    ' ~ ~-.1 ~']}}"},{id:command_block_minecart,Silent:1,Command:"
summon marker $(entity_dark_moveable) {Tags:[chess.live,chess.live.dark_moveable],data:{set:[
    'execute at @n[tag=chess.menu.entity,type=command_block_minecart] run data modify block $(menu:->:dark_moveable) Command set value \\'',{nbt:'data.command',entity:'@n[tag=chess.live.dark_moveable]',interpret:1},'\\''
    ],command:[
    'execute at @n[tag=chess.main] as @e[tag=chess.calculate.moveable,tag=!chess.calculate.selected,tag=!chess.calculate.check,distance=..7,nbt={Fire:1s},nbt=!{Item:{}}] on vehicle at @s unless entity @e[tag=chess.calculate.move,distance=...5,nbt={data:{passant:1}}] run clone '
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.dark_moveable]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.dark_moveable]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.dark_moveable]'}, ' ',{nbt:'data.pos_x','entity':'@n[tag=chess.live.dark_moveable]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.dark_moveable]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.dark_moveable]'},
    ' ~ ~-.1 ~']}}"},{id:command_block_minecart,Silent:1,Command:"
summon marker $(entity_dark_attack) {Tags:[chess.live,chess.live.dark_attack],data:{set:[
    'execute at @n[tag=chess.menu.entity,type=command_block_minecart] run data modify block $(menu:->:dark_attack) Command set value \\'',{nbt:'data.command',entity:'@n[tag=chess.live.dark_attack]',interpret:1},'\\''
    ],command:[
    'execute at @n[tag=chess.main] as @e[tag=chess.calculate.moveable,tag=!chess.calculate.selected,tag=!chess.calculate.check,distance=..7,nbt={Fire:1s}] on vehicle at @s unless blocks ~ ~-.1 ~ ~ ~-.1 ~ ',
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.dark_moveable]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.dark_moveable]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.dark_moveable]'},
    ' all run clone '
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.dark_attack]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.dark_attack]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.dark_attack]'},' ',{nbt:'data.pos_x','entity':'@n[tag=chess.live.dark_attack]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.dark_attack]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.dark_attack]'},
    '~ ~-.1 ~']}}"},{id:command_block_minecart,Silent:1,Command:"
summon marker $(entity_check_unselected) {Tags:[chess.live,chess.live.check_unselected],data:{set:[
    'execute at @n[tag=chess.menu.entity,type=command_block_minecart] run data modify block $(menu:->:check_unselected) Command set value \\'',{nbt:'data.command',entity:'@n[tag=chess.live.check_unselected]',interpret:1},'\\''
    ],command:[
    'execute at @n[tag=chess.main] as @e[tag=chess.calculate.check,tag=!chess.calculate.selected,distance=..7] on vehicle at @s run clone '
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.check_unselected]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.check_unselected]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.check_unselected]'}, ' ',{nbt:'data.pos_x','entity':'@n[tag=chess.live.check_unselected]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.check_unselected]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.check_unselected]'},
    ' ~ ~-.1 ~']}}"},{id:command_block_minecart,Silent:1,Command:"
summon marker $(entity_check_selected) {Tags:[chess.live,chess.live.check_selected],data:{set:[
    'execute at @n[tag=chess.menu.entity,type=command_block_minecart] run data modify block $(menu:->:check_selected) Command set value \\'',{nbt:'data.command',entity:'@n[tag=chess.live.check_selected]',interpret:1},'\\''
    ],command:[
    'execute at @n[tag=chess.main] as @e[tag=chess.calculate.check,tag=chess.calculate.selected,distance=..7] on vehicle at @s run clone '
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.check_selected]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.check_selected]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.check_selected]'}, ' ',{nbt:'data.pos_x','entity':'@n[tag=chess.live.check_selected]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.check_selected]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.check_selected]'},
    ' ~ ~-.1 ~']}}"},{id:command_block_minecart,Silent:1,Command:"
summon marker $(entity_checkmate) {Tags:[chess.live,chess.live.checkmate],data:{set:[
    'execute at @n[tag=chess.menu.entity,type=command_block_minecart] run data modify block $(menu:->:checkmate) Command set value \\'',{nbt:'data.command',entity:'@n[tag=chess.live.checkmate]',interpret:1},'\\''
    ],command:[
    'execute at @n[tag=chess.calculate] unless entity @e[tag=chess.calculate.legal,distance=..7] as @e[tag=chess.item,nbt={Item:{components:{\\"minecraft:custom_data\\":{Chess:[king]}}}},scores={chess.team=1},distance=..7] at @s at @e[tag=chess.calculate.piece,distance=...5,scores={chess.score=1..}] store result entity @n[tag=chess.calculate] data.end int 1 on vehicle at @s run clone '
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.checkmate]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.checkmate]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.checkmate]'}, ' ',{nbt:'data.pos_x','entity':'@n[tag=chess.live.checkmate]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.checkmate]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.checkmate]'},
    ' ~ ~-.1 ~']}}"},{id:command_block_minecart,Silent:1,Command:"
summon marker $(entity_stalemate) {Tags:[chess.live,chess.live.stalemate],data:{set:[
    'execute at @n[tag=chess.menu.entity,type=command_block_minecart] run data modify block $(menu:->:stalemate) Command set value \\'',{nbt:'data.command',entity:'@n[tag=chess.live.stalemate]',interpret:1},'\\''
    ],command:[
    'execute at @n[tag=chess.calculate] unless entity @e[tag=chess.calculate.legal,distance=..7] as @e[tag=chess.item,nbt={Item:{components:{\\"minecraft:custom_data\\":{Chess:[king]}}}},scores={chess.team=1},distance=..7] at @s unless entity @e[tag=chess.calculate.piece,distance=...5,scores={chess.score=1..}] store result entity @n[tag=chess.calculate] data.end int 1 on vehicle at @s run clone '
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.stalemate]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.stalemate]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.stalemate]'}, ' ',{nbt:'data.pos_x','entity':'@n[tag=chess.live.stalemate]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.stalemate]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.stalemate]'},
    ' ~ ~-.1 ~']}}"},{id:command_block_minecart,Silent:1,Command:"
summon marker $(entity_check_assisted) {Tags:[chess.live,chess.live.check_assisted],data:{set:[
    'execute at @n[tag=chess.menu.entity,type=command_block_minecart] run data modify block $(menu:->:check_assisted) Command set value \\'',{nbt:'data.command',entity:'@n[tag=chess.live.check_assisted]',interpret:1},'\\''
    ],command:[
    'execute at @n[tag=chess.calculate,nbt={data:{end:1}}] at @e[tag=chess.calculate.king_move,scores={chess.team=1},distance=..8] unless entity @e[tag=chess.item,nbt=!{Item:{Chess:[king]}},distance=...5,scores={chess.team=1}] at @e[tag=chess.calculate.move,tag=!pwnfwd,distance=...5,scores={chess.team=2,chess.move=1..}] as @e[tag=chess.item,scores={chess.team=2},distance=..8] if score @s chess.id = @n[tag=chess.calculate.move] chess.id on vehicle at @s run clone '
    {nbt:'data.pos_x','entity':'@n[tag=chess.live.check_assisted]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.check_assisted]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.check_assisted]'}, ' ',{nbt:'data.pos_x','entity':'@n[tag=chess.live.check_assisted]'},' ',{nbt:'data.pos_y','entity':'@n[tag=chess.live.check_assisted]'},' ',{nbt:'data.pos_z','entity':'@n[tag=chess.live.check_assisted]'},
    ' ~ ~-.1 ~']}}"},{id:command_block_minecart,Silent:1,Command:"

execute as @e[tag=chess.live] store result entity @s data.pos_x int 1 run data get entity @s Pos[0]"},{id:command_block_minecart,Silent:1,Command:"
execute as @e[tag=chess.live] store result entity @s data.pos_y int 1 run data get entity @s Pos[1]"},{id:command_block_minecart,Silent:1,Command:"
execute as @e[tag=chess.live] store result entity @s data.pos_z int 1 run data get entity @s Pos[2]"},{id:command_block_minecart,Silent:1,Command:"

execute align xz run kill @e[type=command_block_minecart,dy=0]"}]}