# Tips & Tricks

## Make Sublime as Default text editor
- find a plain text file in Finder and click 'Get Info'
- Under 'Opens with:', select Sublime Text
- click 'Change All.

## Must have tools
### jsonlint
- Install : `brew install jsonlint`
- Usage: `echo '<json>' | jsonlint -p`


## Command Line Tips
- Avoid your computer to sleep when a specific app is open: `caffeinate -w <pid>`
- List top resources consuming process: `top`
- Look at the Mac OS Version: `sw_vers`
- Look at the detailed information about the system: `system_profiler -listDataTypes`
- Look details about the specific dataTypes in system profile: `system_profiler <DataTypeName>`
- Look Detailed Software Version of Mac: `system_profiler SPSoftwareDataType`
- Look Detailed Network Information of Mac: `system_profiler SPNetworkDataType`
- Look which tcp traffic the system is connected to: `nettop -m tcp`
- Get info about disk utility: `diskutil list`
- Get size of a folder: `du -sh <path-of-folder>`
