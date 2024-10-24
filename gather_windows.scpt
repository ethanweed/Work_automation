#!/usr/bin/osascript

property processesToIgnore : {}
tell application "Finder"
	set _b to bounds of window of desktop
	set screen_width to item 3 of _b
	set screen_height to item 4 of _b
end tell
tell application "System Events"
	set allProcesses to application processes
	set _results to ""
	repeat with i from 1 to count allProcesses
		set doIt to 1
		repeat with z from 1 to count processesToIgnore
			if process i = process (item z of processesToIgnore) then
				set doIt to 0
			end if
		end repeat
		if doIt = 1 then
			tell process i
				repeat with x from 1 to (count windows)
					set winPos to position of window x
					set _x to item 1 of winPos
					set _y to item 2 of winPos
					if (_x < 0 or _y < 0 or _x > screen_width or _y > screen_height) then
						set position of window x to {0, 22}
					end if
				end repeat
			end tell
		end if
	end repeat
end tell