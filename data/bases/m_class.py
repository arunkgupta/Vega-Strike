import Base
import dynamic_mission
import VS
import gettext

time_of_day=''
bar=-1
weap=-1
room0=-1
plist=VS.musicAddList('agricultural.m3u')
VS.musicPlayList(plist)
dynamic_mission.CreateMissions()
room = Base.Room ('Landing_Pad')
room0 = room
Base.Texture (room, 'background', 'bases/agriculture/agricultural_landing'+time_of_day+'.spr', 0, 0)
Base.Ship (room, 'my_ship', (0.783125,-0.259167,3), (0, 0.93, -0.34), (-.86, 0, .86))

room = Base.Room ('Commodity_Exchange')
room1 = room
Base.Texture (room, 'background', 'bases/agriculture/agricultural_traderoom'+time_of_day+'.spr', 0, 0)


room = Base.Room ('Main_Concourse')
room2 = room
Base.Texture (room, 'background', 'bases/agriculture/agricultural_concourse'+time_of_day+'.spr', 0, 0)
import bar
room = bar.MakeAgriculturalBar(room2,'Main_Concourse',"bases/agriculture/agricultural_bar"+time_of_day,"bases/bartender_agricultural.py")
room3 = room
#Base.Texture (room, 'background', 'bases/agriculture/agricultural_bar'+time_of_day+'.spr', 0, 0)

room = Base.Room ('Weapon_Room')
room4 = room
Base.Texture (room, 'background', 'bases/agriculture/agricultural_weaponsroom'+time_of_day+'.spr', 0, 0)

room = Base.Room ('View_From_Tower')
room5 = room
Base.Texture (room, 'background', 'bases/agriculture/agricultural_exterior1'+time_of_day+'.spr', 0, 0)

room = Base.Room ('View_From_Sea')
room6 = room
Base.Texture (room, 'background', 'bases/agriculture/agricultural_exterior3'+time_of_day+'.spr', 0, 0)

room = Base.Room ('View_From_Lighthouse')
room7 = room
Base.Texture (room, 'background', 'bases/agriculture/agricultural_exterior2'+time_of_day+'.spr', 0, 0)

Base.Link (room0, 'my_link_id', -0.24, 0.08, 0.215, 0.18, _('Commodity_Exchange'), room1)
Base.LaunchPython (room0, 'my_launch_id', 'bases/launch_music.py', 0.16, -0.88, 0.5775, 0.733333, _('Launch'))
Base.Link (room0, 'my_link_id', -0.9725, -0.97, 0.515, 1.92333, _('Main_Concourse'), room2)
Base.Link (room0, 'my_link_id', 0.3175, 0.163333, 0.485, 0.313333, _('View_From_Sea'), room6)
Base.Comp (room1, 'my_comp_id', -0.97, -0.663333, 1.2375, 0.813333, _('Buy/Sell Cargo'), 'Cargo ')
Base.Link (room1, 'my_link_id', 0.425, -0.966667, 0.545, 0.89, _('Landing_Pad'), room0)
Base.Link (room1, 'my_link_id', -.97, -0.97, 2.0, 0.2, _('Landing_Pad'), room0)
Base.Link (room1, 'my_link_id', -0.6075, 0.313333, 0.3825, 0.503333, _('View_From_Tower'), room5)
Base.Comp (room2, 'my_comp_id', -0.1975, -0.0433333, 0.33, 0.216667, _('Buy/Sell Cargo'), 'Cargo News Info ')
Base.Link (room2, 'my_link_id', 0.1725, -0.226667, 0.215, 0.596667, _('Bar'), room3)
Base.Link (room2, 'my_link_id', -0.995, -0.98, 1.325, 0.273333, _('Return_to_Landing_Pad'), room0)
Base.Link (room2, 'my_link_id', 0.4675, -0.646667, 0.5, 1.48667, _('Return_to_Landing_Pad'), room0)
Base.Link (room2, 'my_link_id', -0.705, -0.193333, 0.42, 0.37, _('Ship Dealer/Weapon Room'), room4)
Base.Comp (room2, 'my_comp_id', -0.6075, -0.646667, 0.19, 0.68, _('Mission Computer'), 'Missions News Info ')

Base.Comp (room3, 'my_comp_id', -0.9875, -0.45, 0.375, 1.08, _('Missions'), 'Missions News Info ')
Base.Comp (room4, 'my_comp_id', -0.555, 0.173333, 0.7675, 0.386667, _('Upgrade Starship'), 'Upgrade Info ')
Base.Comp (room4, 'my_comp_id', 0.3375, 0.13, 0.6275, 0.393333, _('Purchase_Starship'), 'ShipDealer Info ')
Base.Link (room4, 'my_link_id', -0.9725, -0.96, 1.9325, 0.483333, _('Return_to_Concourse'), room2)
Base.Link (room5, 'my_link_id', -0.175, -0.286667, 0.065, 0.0866667, _('Commodity_Exchange'), room1)
Base.Link (room5, 'my_link_id', 0.16, -0.55, 0.1025, 0.223333, _('Landing_Pad'), room0)
Base.Link (room5, 'my_link_id', 0.435, -0.31, 0.1575, 0.223333, _('View_From_Sea'), room6)
Base.Link (room5, 'my_link_id', -0.0075, -0.04, 0.08, 0.153333, _('View_From_Lighthouse'), room7)
Base.Link (room6, 'my_link_id', 0.28, 0.17, 0.23, 0.296667, _('View_From_Lighthouse'), room7)
Base.Link (room6, 'my_link_id', -0.365, 0.0433333, 0.1375, 0.14, _('Return_To_Landing_Pad'), room0)
Base.Link (room7, 'my_link_id', -0.6525, 0.233333, 0.08, 0.33, _('View_From_Sea'), room6)
Base.Link (room7, 'my_link_id', 0.0275, 0.67, 0.0975, 0.153333, _('View_From_Tower'), room5)
