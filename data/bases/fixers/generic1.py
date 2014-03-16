import fixers
import mission_lib
import Base
import VS

fixers.DestroyActiveButtons ()
if VS.numActiveMissions()>1:
    Base.Message(_('You are already doing a mission. Finish that instead.'))
else:
    fixers.CreateChoiceButtons(Base.GetCurRoom(),[
            fixers.Choice("bases/fixers/yes.spr","bases/fixers/generic1b.py",_("Accept This Agreement")),
            fixers.Choice("bases/fixers/no.spr","bases/fixers/no.py",_("Decline This Agreement"))])
    mission_lib.BriefLastMission(1,0)
