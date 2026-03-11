"""
At a cultural festival, multiple performances are scheduled on a single stage. However, 
due to last-minute changes, some performances need to be rescheduled or canceled. The 
festival organizers use a stack to manage these changes efficiently.

You are given a list changes of strings where each string represents a change action. 
The actions can be:

"Schedule X": Schedule a performance with ID X on the stage.
"Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
"Reschedule": Reschedule the most recently canceled performance to be the next on stage.
Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.


"""


def manage_stage_changes(changes):