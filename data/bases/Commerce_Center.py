import Base
import VS
import dynamic_mission
import fixers
import gettext
#import bar_lib
#import weapons_lib

plist=VS.musicAddList ('commerce_center.m3u')
VS.musicPlayList(plist)
dynamic_mission.CreateMissions()
room0 = Base.Room ('Landing Platform')
room1 = Base.Room ('Mission Room')
room2 = Base.Room ('Main Concourse')
room3 = Base.Room ('Shopping Mall')
Base.Texture (room0, 'tex', 'bases/generic/base_entrance.spr', 0, 0)
Base.Texture (room1, 'tex', 'bases/commerce/missioninside.spr', 0, 0)
Base.Texture (room2, 'tex', 'bases/commerce/concourse.spr', 0, 0)
Base.Texture (room3, 'tex', 'bases/commerce/shoppingmall.spr', 0, 0)

Base.Ship (room0, 'ship', (0,-.3*2,2*2),(0,.93,-.34) ,(-1,0,0))
Base.LaunchPython (room0, 'launch','bases/launch_music.py', -0.841797, -0.859375, 1.5625, 0.565104, _('Launch Your Ship'))
Base.Link (room0, 'Conc', -0.453125, -0.291667, 0.767578, 0.770833, _('Main Concourse'),room2)

Base.Comp (room1, 'missioncomp', 0.2775, -0.28, 0.7175, 0.503333, _('Mission Computer'), 'Missions News')
Base.Link (room1, 'Conc', -0.9975, -0.996667, 1.9925, 0.373333, _('Main Concourse'), room2)
fixers.CreateFixers(room1,[(-.9, -0.61, 0.25, 0.667)])

Base.Link (room2, 'launchplat', -1, -0.993333, 1.9875, 0.363333, _('Landing Platform'), room0)
Base.Comp (room2, 'buysell', -0.0625, -0.62, 0.7575, 0.3, _('Cargo Computer'), 'Cargo')
Base.Link (room2, 'mall', -0.6675, -0.623333, 0.2375, 0.28, _('Shopping Mall'), room3)
Base.Link (room2, 'mission', -0.8925, -0.34, 1.89, 0.446667, _('Mission Room'), room1)

Base.Link (room3, 'Conc', -0.7025, -0.756667, 0.3375, 1.75667, _('Main Concourse'), room2)
Base.Link (room3, 'Conc', -1 ,-0.98,  2, .045667, _('Main Concourse'), room2)
Base.Comp (room3, 'upg', -0.3625, -0.726667, 0.2925, 1.72, _('Upgrade Ship'), 'Upgrade Info')
Base.Comp (room3, 'shd', 0.06, -0.68, 0.345, 0.74, _('Ship Dealer'), 'ShipDealer')
