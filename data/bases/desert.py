import Base
import dynamic_mission
import VS
import gettext


time_of_day=''
weap=-1
room0=-1
plist=VS.musicAddList('desert.m3u')
VS.musicPlayList(plist)
dynamic_mission.CreateMissions()
room = Base.Room ('Landing_Pad')
room0 = room
Base.Texture (room, 'background', 'bases/desert/desert_landing'+time_of_day+'.spr', 0, 0)
Base.Ship (room, 'my_ship', (-0.101074,-0.458464,2), (0, 0.93, -0.34), (-1, 0, 0))

room = Base.Room ('Main_Tent')
room1 = room
Base.Texture (room, 'background', 'bases/desert/desert_concourse'+time_of_day+'.spr', 0, 0)
import bar
room2 = bar.MakeMiningBar(room1,'Main_Tent','bases/desert/desert_bar'+time_of_day,'bases/bartender_default.py')

room = Base.Room ('Weapon_Room')
room3 = room
Base.Texture (room, 'background', 'bases/desert/desert_weaponroom'+time_of_day+'.spr', 0, 0)
Base.Ship (room, 'my_ship', (-1.289941,-0.194401,11), (0, 0.93, -0.34), (-1, 0, 0))

room = Base.Room ('Trade_Center')
room4 = room
Base.Texture (room, 'background', 'bases/desert/desert_exterior5'+time_of_day+'.spr', 0, 0)

room = Base.Room ('Exterior_Of_Tent')
room65 = room
Base.Texture (room, 'background', 'bases/desert/desert_exterior3'+time_of_day+'.spr', 0, 0)
Base.Ship (room, 'my_ship', (-0.2149414,-0.538047,16), (0, 0.93, -0.34), (-1, 0, 0))

room = Base.Room ('Radar_Dishes')
room66 = room
Base.Texture (room, 'background', 'bases/desert/desert_exterior4'+time_of_day+'.spr', 0, 0)

room = Base.Room ('Dish_Field')
room67 = room
Base.Texture (room, 'background', 'bases/desert/desert_exterior2'+time_of_day+'.spr', 0, 0)

Base.LaunchPython (room0, 'my_launch_id', 'bases/launch_music.py', -0.529297, -0.796875, 0.777344, 0.53125, _('Launch'))
Base.Link (room0, 'my_link_id', -0.826172, -0.265625, 0.503906, 1.10938, _('Main_Tent'), room1)
Base.Link (room1, 'my_link_id', 0.427734, -0.21875, 0.371094, 0.567708, _('Landing_Pad'), room0)
Base.Comp (room1, 'my_comp_id', -0.966797, -0.00260417, 0.5, 0.481771, _('Mission_Computer'), 'Missions News Info ')
Base.Link (room1, 'my_link_id', -0.46875, -0.164062, 0.142578, 0.351562, _('Weapon_Room'), room3)
Base.Link (room1, 'my_link_id', 0.150391, -0.0416667, 0.232422, 0.273438, _('Bar'), room2)
Base.Link (room1, 'my_link_id', -0.279297, -0.104167, 0.349609, 0.286458, _('Trade_Center'), room4)
Base.Comp (room3, 'my_comp_id', 0.283203, -0.528646, 0.390625, 0.596354, _('Upgrade_Starship'), 'Upgrade Info ')
Base.Comp (room3, 'my_comp_id', -0.962891, -0.838542, 1.09766, 0.945312, _('Ship_Dealer'), 'ShipDealer Info ')
Base.Link (room3, 'my_link_id', -0.998047, -0.997396, 1.99414, 0.174479, _('Main_Tent'), room1)
Base.Comp (room4, 'my_comp_id', 0.419922, -0.278646, 0.548828, 0.520833, _('Trade_Cargo'), 'Cargo News Info ')
Base.Link (room4, 'my_link_id', -0.541016, -0.611979, 0.9375, 0.848958, _('Explore_Surface'), room65)
Base.Link (room65, 'my_link_id', -0.244141, -0.632812, 0.226562, 0.276042, _('Landing_Bay'), room0)
Base.Link (room65, 'my_link_id', -0.523438, -0.351562, 0.123047, 0.174479, _('Cargo_Trading_Center'), room4)
Base.Link (room65, 'my_link_id', -0.470703, -0.330729, 0.400391, 0.393229, _('Main_Concourse'), room1)
Base.Link (room65, 'my_link_id', 0.431641, -0.645833, 0.441406, 0.846354, _('Explore_Dishes'), room66)
Base.Link (room65, 'my_link_id', -0.953125, 0.15625, 0.642578, 0.408854, _('Hike_To_Farther_Dishes'), room67)
Base.Comp (room66, 'my_comp_id', 0.046875, -0.484375, 0.412109, 0.622396, _('News'), 'News Info ')
Base.Link (room66, 'my_link_id', -0.994141, -0.986979, 0.505859, 0.989583, _('Return_To_Main_Tent'), room65)
Base.Link (room67, 'my_link_id', -0.234375, 0.440104, 0.263672, 0.226563, _('Return_To_Main_Tent'), room65)
Base.Comp (room67, 'my_comp_id', -0.757812, 0.174479, 0.0820312, 0.210937, _('News'), 'News Info ')
Base.Link (room67, 'my_link_id', 0.224609, 0.221354, 0.435547, 0.364583, _('Explore_Dishes'), room66)
