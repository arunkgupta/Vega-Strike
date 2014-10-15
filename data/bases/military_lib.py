import gettext

def MakeMilitaryBase(bartendername='bases/bartender_default.py',time_of_day=''):
    import Base
    import dynamic_mission
    import VS
    weap=-1
    room0=-1
    dynamic_mission.CreateMissions()
    room = Base.Room ('Hangar')
    room0 = room
    Base.Texture (room, 'background', 'bases/military/military_landing'+time_of_day+'.spr', 0, 0)
    Base.Ship (room, 'my_ship', (0.143555,-0.258203,6), (0, 1, 0), (-0.85, 0.03, -0.89))

    room = Base.Room ('Main _concourse')
    room1 = room
    Base.Texture (room, 'background', 'bases/military/military_concourse'+time_of_day+'.spr', 0, 0)


    room = Base.Room ('Bridge')
    room3 = room
    Base.Texture (room, 'background', 'bases/civilian/civilian_traderoom'+time_of_day+'.spr', 0, 0)

    room = Base.Room ('Military_Decks')
    room4 = room
    Base.Texture (room, 'background', 'bases/military/military_restricted'+time_of_day+'.spr', 0, 0)


    room = Base.Room ('Weapon_Surplus_Stores')
    room6 = room
    Base.Texture (room, 'background', 'bases/military/military_weapons'+time_of_day+'.spr', 0, 0)
    Base.Ship (room, 'my_ship', (-0.08927734,0.209375,3), (0, 0.93, -0.34), (-1, 0, 0))

    Base.LaunchPython (room0, 'my_launch_id', 'bases/launch_music.py', -0.0976562, -0.373958, 0.308594, 0.299479, _('Launch'))
    Base.Link (room0, 'my_link_id', -1, -0.997396, 0.142578, 1.9974, _('Main _concourse'), room1)
    Base.Link (room0, 'my_link_id', -1, -0.997396, 1.99805, 0.140625, _('Main _concourse'), room1)
    Base.Comp (room1, 'my_comp_id', -0.974609, 0.0286458, 0.607422, 0.388021, _('Mission_Computer'), 'Missions News Info ')
    Base.Link (room1, 'my_link_id', -0.261719, -0.0651042, 0.335938, 0.223958, _('Bridge'), room3)
    import bar
    bar = bar.MakeMiningBar (room1,'Main _concourse','bases/mining/mining_bar'+time_of_day,bartendername)
    Base.Link (room1, 'bar', 0.125, -0.119792, 0.208984, 0.320312, _('Bar'), bar)
    Base.Link (room1, 'my_link_id', 0.451172, -0.169271, 0.242188, 0.445312, _('Hangar'), room0)
    Base.Link (room1, 'my_link_id', -0.505859, -0.304688, 0.179688, 0.455729, _('Weapon_Surplus_Stores'), room6)
    Base.Link (room1, 'my_link_id', -1, -0.997396, 1.99805, 0.0598958, _('Military_Decks'), room4)
    Base.Comp (room3, 'my_comp_id', -0.423828, 0.143229, 0.587891, 0.34375, _('Trade_Cargo/Services'), 'Cargo Missions News Info ')
    Base.Link (room3, 'my_link_id', -0.998047, -0.994792, 1.99609, 0.143229, _('Main _concourse'), room1)
    Base.Link (room3, 'my_link_id', 0.0449219, -0.078125, 0.136719, 0.140625, _('Military_Decks'), room4)
    Base.Link (room4, 'my_link_id', -0.158203, -0.171875, 0.228516, 0.140625, _('Bridge'), room3)
    Base.Link (room4, 'my_link_id', 0.314453, -0.182292, 0.220703, 0.179688, _('Restricted_Area'), room4)
    Base.Link (room4, 'my_link_id', -1, -0.997396, 1.99805, 0.111979, _('Main _concourse'), room1)
    Base.Comp (room6, 'my_comp_id', -0.966797, -0.973958, 0.558594, 1.29427, _('Upgrade_Starship'), 'Upgrade Info ')
    Base.Comp (room6, 'my_comp_id', -0.289062, -0.733333, 0.513672, 0.400937, _('Shipyard'), 'ShipDealer Info ')
    Base.Link (room6, 'my_link_id', -0.574219, -0.986979, 1.57031, 0.286458, _('Main _concourse'), room1)
    return (room0,room1,bar,room6)
